#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Update SOURCES.md and CHECKSUMS.txt for files in originals/ (recursive).

- Recurse into all subfolders of originals/
- Exclude the folder originals/not public
- Use relative paths (with forward slashes) in CHECKSUMS.txt and SOURCES.md entries
- Keep Notes section always at the end (and only once)
- Detect moved files: if basename + SHA match an existing entry, update its **File:** path instead of creating a new entry
- Warn about entries listed but no longer present.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from datetime import date
from typing import Dict, Tuple, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent  # script in tools/
ORIGINALS_DIR = REPO_ROOT / "originals"
CHECKSUMS_TXT = ORIGINALS_DIR / "CHECKSUMS.txt"
SOURCES_MD = ORIGINALS_DIR / "SOURCES.md"
META_JSON = ORIGINALS_DIR / "sources_meta.json"

HEADER_MD = """# FOY Originals – Sources & Checksums

This document lists the origin of all files in the `originals/` folder.  
Each entry includes the source and a SHA-256 checksum for verification.  
This ensures provenance and long-term integrity of preserved materials.
"""

NOTES_MD = """
## Notes
- This list must always reflect the exact contents of the `originals/` folder.  
- New entries: add at the bottom of the relevant section.  
- For each **file**, document at least **source** and **checksum**(SHA-256).
- Only files stored in `originals/` are listed here. For active attributions in-game, see [`ATTRIBUTION.md`](../ATTRIBUTION.md).
""".lstrip()

NEW_FILES_SECTION = "## New Files"
EXCLUDED_TOP_DIR = "not public"  # exclude originals/not public/**

# --- Utilities ---------------------------------------------------------------

def relpath_unix(p: Path) -> str:
    """Return path relative to ORIGINALS_DIR using forward slashes."""
    return p.relative_to(ORIGINALS_DIR).as_posix()

def sha256_file(path: Path) -> str:
    """Return hex SHA-256 digest (uppercase) for file at path."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def load_meta() -> Dict[str, Dict[str, str]]:
    """Load optional sources_meta.json mapping; return {} if absent/invalid."""
    if META_JSON.exists():
        try:
            data = json.loads(META_JSON.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return {str(k): dict(v) for k, v in data.items() if isinstance(v, dict)}
        except Exception:
            pass
    return {}

def write_checksums_txt(checksums: Dict[str, str]) -> None:
    """Write originals/CHECKSUMS.txt in the requested format."""
    CHECKSUMS_TXT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# SHA-256 checksums for originals/ (generated on {date.today().isoformat()})",
        ""
    ]
    for rel in sorted(checksums.keys(), key=lambda s: s.lower()):
        lines.append(f"{checksums[rel]}  {rel}")
    CHECKSUMS_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")

# --- SOURCES.md parsing/updating --------------------------------------------

def ensure_base_document(md_text: Optional[str]) -> str:
    """Ensure SOURCES.md has a header; create minimal doc if missing."""
    if not md_text or not md_text.strip():
        return HEADER_MD
    if not md_text.lstrip().startswith("# FoY Originals"):
        return HEADER_MD + "\n" + md_text
    return md_text

def remove_notes_section(md_text: str) -> str:
    """Remove exactly the '## Notes' section (if present), preserving everything after it."""
    pattern = re.compile(r"^## Notes[\s\S]*?(?=^## |\Z)", re.MULTILINE)
    return pattern.sub("", md_text).rstrip()

def ensure_notes_at_end(md_text: str) -> str:
    """Append NOTES_MD exactly once at the end."""
    md_text = remove_notes_section(md_text)
    return md_text.rstrip() + "\n\n" + NOTES_MD

def find_file_blocks(md_text: str) -> Dict[str, Tuple[int, int]]:
    """
    Build an index: shown_filename -> (block_start_pos, block_end_pos)
    We use the exact text inside backticks after '- **File:**'.
    """
    file_block_map: Dict[str, Tuple[int, int]] = {}
    pattern = re.compile(r"- \*\*File:\*\* `([^`]+)`", re.MULTILINE)
    matches = list(pattern.finditer(md_text))
    boundaries = [m.start() for m in matches] + [len(md_text)]
    for i, m in enumerate(matches):
        shown = m.group(1)
        start = m.start()
        next_pos = boundaries[i + 1]
        section_m = re.search(r"^## .*$", md_text[start:next_pos], flags=re.MULTILINE)
        end = start + section_m.start() if section_m else next_pos
        file_block_map[shown] = (start, end)
    return file_block_map

def extract_sha_from_block(block: str) -> Optional[str]:
    """Extract the SHA-256 hex from a block, if present."""
    m = re.search(r"- \*\*SHA-256:\*\* `([A-Fa-f0-9]{64})`", block)
    return m.group(1).upper() if m else None

def replace_file_line(block: str, new_shown: str) -> str:
    """Replace the **File:** line's backticked content with new_shown."""
    return re.sub(r"(- \*\*File:\*\* `)([^`]+)(`)", rf"\1{new_shown}\3", block, count=1)

def build_name_sha_map(md_text: str) -> Dict[Tuple[str, str], Tuple[str, Tuple[int, int]]]:
    """
    Map (basename.lower(), sha) -> (shown_filename, (start, end)).
    Used to detect moved files by same basename + same checksum.
    """
    idx = find_file_blocks(md_text)
    name_sha_map: Dict[Tuple[str, str], Tuple[str, Tuple[int, int]]] = {}
    for shown, (start, end) in idx.items():
        block = md_text[start:end]
        sha = extract_sha_from_block(block)
        if not sha:
            continue
        base = Path(shown).name.lower()
        name_sha_map[(base, sha)] = (shown, (start, end))
    return name_sha_map

def update_sha_in_block(block: str, new_sha: str) -> str:
    """Replace or insert the SHA-256 line within a file block."""
    sha_pattern = re.compile(r"- \*\*SHA-256:\*\* `([A-Fa-f0-9]{64})`")
    if sha_pattern.search(block):
        return sha_pattern.sub(f"- **SHA-256:** `{new_sha}`", block, count=1)
    return block.rstrip() + "\n    - **SHA-256:** `{}`\n".format(new_sha)

def ensure_section(md_text: str, section_title: str) -> Tuple[str, int]:
    """Ensure a section '## section_title' exists; return (md_text, insert_pos_after_header)."""
    sec_re = re.compile(rf"^## {re.escape(section_title)}\s*$", re.MULTILINE)
    m = sec_re.search(md_text)
    if m:
        line_end = md_text.find("\n", m.end())
        insert_pos = line_end + 1 if line_end != -1 else len(md_text)
        return md_text, insert_pos
    to_append = f"\n\n## {section_title}\n"
    return md_text + to_append, len(md_text) + len(to_append)

def render_file_entry(shown_name: str, sha: str, source: str, date_archived: str) -> str:
    """Render a new file entry block."""
    return (
        f"- **File:** `{shown_name}`\n"
        f"    - **Source:** {source}\n"
        f"    - **Date Archived:** {date_archived}\n"
        f"    - **SHA-256:** `{sha}`\n\n"
    )

def apply_block_replacement(md_text: str, start: int, end: int, new_block: str) -> str:
    return md_text[:start] + new_block + md_text[end:]

def main() -> None:
    if not ORIGINALS_DIR.exists():
        raise SystemExit(f"Folder not found: {ORIGINALS_DIR}")

    # Collect files recursively, exclude originals/not public/**
    files = []
    for p in ORIGINALS_DIR.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ORIGINALS_DIR)
        if rel.as_posix() in {"CHECKSUMS.txt", "SOURCES.md", "sources_meta.json"}:
            continue
        if len(rel.parts) > 0 and rel.parts[0] == EXCLUDED_TOP_DIR:
            continue
        files.append(p)

    # Checksums keyed by relative unix path
    checksums: Dict[str, str] = {}
    for p in files:
        checksums[relpath_unix(p)] = sha256_file(p)

    # generate CHECKSUMS.txt
    write_checksums_txt(checksums)

    # Load + prep SOURCES.md
    md_text = SOURCES_MD.read_text(encoding="utf-8") if SOURCES_MD.exists() else ""
    md_text = ensure_base_document(md_text)
    md_text = remove_notes_section(md_text)
    meta = load_meta()

    # Create dictionaries
    file_blocks = find_file_blocks(md_text)
    name_sha_map = build_name_sha_map(md_text)

    # Helper for meta lookup
    def meta_for(rel: str) -> Dict[str, str]:
        base = Path(rel).name
        if rel in meta:
            return meta[rel]
        if base in meta:
            return meta[base]
        return {}

    # Update existing blocks by exact shown path
    for rel, sha in checksums.items():
        shown = rel
        if shown in file_blocks:
            start, end = file_blocks[shown]
            block = md_text[start:end]
            new_block = update_sha_in_block(block, sha)
            if new_block != block:
                md_text = apply_block_replacement(md_text, start, end, new_block)
                file_blocks = find_file_blocks(md_text)
                name_sha_map = build_name_sha_map(md_text)

    # Detect moved files (same basename + same SHA) and update **File:** path
    moved_handled = set()
    for rel, sha in checksums.items():
        if rel in file_blocks:
            continue
        base = Path(rel).name.lower()
        key = (base, sha)
        if key in name_sha_map:
            old_shown, (start, end) = name_sha_map[key]
            block = md_text[start:end]
            new_block = replace_file_line(block, rel)
            if new_block != block:
                md_text = apply_block_replacement(md_text, start, end, new_block)
                # Rebuild indices after mutation
                file_blocks = find_file_blocks(md_text)
                name_sha_map = build_name_sha_map(md_text)
                moved_handled.add(rel)

    # Append truly missing files (not matched by exact path and not moved)
    missing = [rel for rel in checksums.keys() if rel not in file_blocks and rel not in moved_handled]
    if missing:
        buckets: Dict[str, str] = {}
        today = date.today().isoformat()
        for rel in sorted(missing, key=lambda s: s.lower()):
            m = meta_for(rel)
            section = m.get("section") or NEW_FILES_SECTION
            source = m.get("source") or "TBD"
            date_archived = m.get("date_archived") or today
            entry = render_file_entry(rel, checksums[rel], source, date_archived)
            buckets[section] = buckets.get(section, "") + entry

        for section, content in buckets.items():
            md_text, insert_pos = ensure_section(md_text, section)
            md_text = md_text[:insert_pos] + content + md_text[insert_pos:]

    # Warn about entries listed but no longer present
    listed_filenames = set(find_file_blocks(md_text).keys())
    present_filenames = set(checksums.keys())
    missing_on_disk = sorted(listed_filenames - present_filenames, key=str.lower)
    footer_note_tag = "<!-- MISSING_ON_DISK -->"
    if missing_on_disk:
        note_lines = [footer_note_tag,
                      "The following entries refer to files no longer present in `originals/`:",
                      "", *[f"- `{n}`" for n in missing_on_disk], footer_note_tag]
        if footer_note_tag in md_text:
            md_text = re.sub(rf"{re.escape(footer_note_tag)}.*?{re.escape(footer_note_tag)}", "", md_text, flags=re.DOTALL)
        md_text = md_text.rstrip() + "\n\n" + "\n".join(note_lines) + "\n"

    # Attach notes below and write
    md_text = ensure_notes_at_end(md_text)
    SOURCES_MD.write_text(md_text, encoding="utf-8")

    # Summary
    print(f"Updated: {CHECKSUMS_TXT.relative_to(REPO_ROOT)}")
    print(f"Updated: {SOURCES_MD.relative_to(REPO_ROOT)}")
    if missing:
        print(f"Added {len(missing)} new entr{'y' if len(missing)==1 else 'ies'} under section(s).")
    if moved_handled:
        print(f"Updated paths for {len(moved_handled)} moved entr{'y' if len(moved_handled)==1 else 'ies'}.")

if __name__ == "__main__":
    main()
