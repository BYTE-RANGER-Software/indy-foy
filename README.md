![Status](https://img.shields.io/badge/status-Pre--Pre--Production-yellow)
![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-blue)
[![Project Maintenance](https://img.shields.io/maintenance/yes/2025.svg)](https://github.com/byte-ranger-software/indy-foy 'GitHub Repository')

# Fountain of Youth (FoY)

> **Non-profit fan-made point-and-click adventure in the spirit of early 1990s cinematic puzzle games — continued by BYTE RANGER Software.**

---

## Table of Contents
- [About the Project](#about-the-project)
- [Status](#status)
- [Website](#website)
- [Features](#features)
- [Screenshots](#screenshots)
- [Releases & Nightly Builds](#releases--nightly-builds)
- [Roadmap](#roadmap)
- [Roadmap Progress](#roadmap-progress)
- [Contributing](#contributing)
- [Development Setup](#development-setup)
- [Repository Layout](#repository-layout)
- [Cloning](#cloning)
- [License](#license)
- [Legal Notice](#legal-notice)
- [Attribution & Credits](#attribution--credits)
- [Contact](#contact)

---

## About the Project
**Fountain of Youth** is a non-commercial fan adventure in classic LucasArts style.  
Originally initiated and developed by AGS community contributors, including members of the Screen 7 team (1999–2021).

This continuation is an independent effort by **BYTE RANGER Software** and is not affiliated with Screen 7, Lucasfilm, or Disney.  
This repository hosts the active continuation: planning, source/assets, builds, and documentation.

> **Name disclaimer:** This project is **not related to any film** or other media titled *Fountain of Youth* or similar.

📖 For a detailed **project history** see the [Project Website → History](https://byte-ranger-software.github.io/indy-foy/#history).

## Status
🚧 Early pre-pre-production.  
We are currently focusing on collecting and archiving original materials related to FoY.  
Next step: Creation and completion of the GDD (Game Design Document).

## Website
Project website is published via **GitHub Pages**.
- **URL:** https://byte-ranger-software.github.io/indy-foy/
- Source for the site lives in `docs/` (see [Repository Layout](#repository-layout)).

## Features
- Classic point-and-click mechanics (verb UI / inventory)
- Story-driven puzzles, exploration, and action
- Original music & SFX
- Chapters include **Bimini, Europe & Asia**
- Over **150 hand-drawn backgrounds** in retro low-res look
- Classic **"Atlantis"-style GUI** & mechanics
- Antiquities, sidekicks & leather jackets!

> *Note:* The exact feature set depends on the current AGS implementation stage.

## Screenshots

<p align="center">
  <a href="docs/assets/screenshot-1.jpg">
    <img src="docs/assets/screenshot-1.jpg" alt="Screenshot 1" width="46%" />
  </a>
  <a href="docs/assets/screenshot-2.jpg">
    <img src="docs/assets/screenshot-2.jpg" alt="Screenshot 2" width="46%" />
  </a>
</p>

> Click to view full size.  

## Releases & Nightly Builds
Verified releases appear on the **GitHub Releases** page.

| File | Version | Date | SHA-256 |
|------|---------|------|---------|
|  –   |    –    |  –   |    –    |

*(Nightly builds may be pre-releases and unstable.)*

## Roadmap

- **M00 — Pre-Pre-Production / Discovery & Preservation**  
  Collect prior materials into `originals/` (with SHA-256 + source).  
  Draft initial `ATTRIBUTION.md` document.  
  
- **M01 — Pre-Production / Vertical Slice Tech** 
  Create or complete `GDD.docx` (Game Design Document – includes game concept, storyline, mechanics, art & sound, UI, technical aspects, project details) and `RDD.xlsx` (Room Design Document).  
  Create `TDD.docx` (Technical Design Document based on GDD/RDD)  
  Create Vertical Slice  
  Publish Vertical Slice build (ZIP + website link)  

- **M02 — Core Gameplay Systems**  
  Implement room transitions & pathfinding.  
  Hotspots, objects & inventory flow.  
  Basic dialog system.  
  Save/load system.  
  Blocking volumes & options menu.  

- **M03 — Content Production I: (Public Demo)**  
  3–6 rooms, 5–8 puzzles.  
  One mini-cutscene.  
  First audio pass (music & SFX).  
  QA & packaging for public demo release.  

- **M04 — Content Production II: Main Chapters**  
  Expand rooms, puzzles & story progression.  
  Implement additional characters & animations.  
  Intermediate builds for internal testing.  

- **M05 — Alpha (Feature Complete)**  
  All core mechanics & chapters implemented.  
  Placeholder graphics/audio replaced by finals.  
  Full playthrough possible (bugs expected).  

- **M06 — Beta (Closed Testing)**  
  Bugfixing, balancing of puzzles & difficulty.  
  Performance optimization.  
  External testers (closed group) with feedback loop.  

- **M07 — Release Candidate (RC)**  
  All assets, features, and texts finalized.  
  Translations/localization where applicable.  
  Packaging & installer.  
  Marketing material (trailer, screenshots).  

- **M08 — Release 1.0**  
  Public launch of the full game.  
  Distribution via GitHub, itch.io, etc.  
  Announcements & community posts.  

- **M09 — Post-Release Support**  
  Patches & hotfixes.  
  Possible bonus content.  
  Documentation & optional open-source release.  

## Roadmap Progress

- 🚧[M00 — Pre-Pre-Production / Discovery & Preservation](https://github.com/byte-ranger-software/indy-foy/milestone/1)  
- ☐ [M01 — Pre-Production / GDD, RDD, TDD & Vertical Slice Tech](https://github.com/byte-ranger-software/indy-foy/milestone/2)  
- ☐ [M02 — Core Gameplay Systems](https://github.com/byte-ranger-software/indy-foy/milestone/3)  
- ☐ [M03 — Content Production I: Public Demo](https://github.com/byte-ranger-software/indy-foy/milestone/4)  
- ☐ [M04 — Content Production II: Main Chapters](https://github.com/byte-ranger-software/indy-foy/milestone/5)  
- ☐ [M05 — Alpha (Feature Complete)](https://github.com/byte-ranger-software/indy-foy/milestone/6)  
- ☐ [M06 — Beta (Closed Testing)](https://github.com/byte-ranger-software/indy-foy/milestone/7)  
- ☐ [M07 — Release Candidate](https://github.com/byte-ranger-software/indy-foy/milestone/8)  
- ☐ [M08 — Release 1.0](https://github.com/byte-ranger-software/indy-foy/milestone/9)  
- ☐ [M09 — Post-Release Support](https://github.com/byte-ranger-software/indy-foy/milestone/10)  

> Legend:
>- ✅ Done  
>- 🚧 In Progress  
>- ☐ To Do 

👉 See [Issues → Milestones](https://github.com/byte-ranger-software/indy-foy/milestones) for live progress tracking.

## Contributing
Contributions are possible **after prior coordination**,  
please open an Issue first and describe your proposal, uncoordinated PRs may be declined.

1. Open an Issue, include goal, scope, sample art or mocks if available  
2. After approval: create a branch `\<type\>/\<scope\>/\<short-description\>`  
   - Allowed `<type>`: `feature`, `bugfix`, `hotfix`, `chore`, `docs`, `meta`  
   - `<scope>` is optional, use kebab-case  
3. Open a PR, link the Issue, attach screenshots or GIFs  
4. Use **Git LFS** for large sources only

👉 For details, see the full guide in [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md).


## Development Setup
- **Engine/Framework:** **AGS (Adventure Game Studio)**
- **Dependencies:** _TBA_  
- **Build:** AGS Editor → "Build / Rebuild" or "Save compiled game"  
- **Run:** Execute the compiled game

### Rendering & Resolution
- **Native:** 320×200 (16:10), crisp pixels, nearest-neighbour scaling  
- Aspect-preserving integer scaling for 1280×800 / 1920×1200  
- Optional pipeline: draw masters at 1280×800 and downscale for current builds

## Repository Layout
```
.github/                       # workflows, issue templates, etc. (not shipped)
design/                        # design docs & mockups (not shipped)
docs/                          # website for GitHub Pages (not shipped)
    index.html
    main.js
    assets/
        logo.png
        main.png
        ...
        downloads/
    workflows/                 # workflow descriptions and notes
originals/                     # Git submodule, archival/reference only (not shipped)
dist/                          # release packages (ZIPs/installers) for new game releases (not shipped)
framework/                     # Git submodule, AGS framework for FoY (not shipped)
src/                           # new game source code
    assets/                    # game assets (sources for AGS)
    AudioCache/                # cache for imported audio files, safe to ignore
    Compiled/                  # compiled game output (packaged into ../dist)
    Speech/                    # voice files for .vox creation 
tools/                         # build/release scripts and developer utilities (not shipped)
    packaging/                 # zip/installer scripts
    ci/                        # CI helpers used by GitHub Actions
    dev/                       # local dev tools (linters, formatters, one-off scripts)
        vscode-ags-extension   # Git submodule, AGS Script extension for VS Code

```
> **Note on** `originals/`, Git submodule, archival/reference only, excluded from builds and releases,  
> currently private, becomes public after license clearance.

> **Note on** `framework/`, Git submodule for the AGS framework,  
> currently private, becomes public when finished.

## Cloning

Most users do **not** need the `originals/` and `framework/` submodule to build or run the game.


- **Regular clone, no submodules**
  
  ```bash
  git clone https://github.com/byte-ranger-software/indy-foy.git
  ```

- **Developers who need access to archived resources in `originals/`**
  
  ```bash
  # Requires read access to the private submodule
  git clone --recurse-submodules https://github.com/byte-ranger-software/indy-foy.git
  # or, if already cloned
  git submodule update --init originals
  ```
---

## License
Unless otherwise noted, all contents are licensed under  
**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.  
Full license text: https://creativecommons.org/licenses/by-sa/4.0/

## Legal Notice
This is a **non-commercial fan project**.

Certain names and properties referenced in this repository may be trademarks of their respective owners (e.g., Lucasfilm Ltd.).  
This project is **not affiliated with or endorsed by Lucasfilm, Disney, or Screen 7**.  
All other trademarks are the property of their respective owners.

Unless otherwise noted, repository contents are provided under **CC BY‑SA 4.0**.
If you are a rights holder and have concerns, please contact us: ByteRanger@gmx.de.

### Name Disclaimer
The use of the title **Fountain of Youth** refers to the mythical motif only, and this project is **not affiliated with, endorsed by, or connected to any film, TV production, book, or other work** titled *Fountain of Youth* or with a similar name.

**Fountain of Youth** was previously coordinated by contributors associated with Screen 7 (1999–2021).  
Current continuation is independent and unaffiliated.

## Attribution & Credits
See **[ATTRIBUTION.md](ATTRIBUTION.md)** for sources, acknowledgments, and detailed credits.  
Maintainer: **BYTE RANGER Software (CalDymos)**

## Contact
- **Issues:** https://github.com/byte-ranger-software/indy-foy/issues  
- **E-mail:** ByteRanger@gmx.de  
- **Project website:** https://byte-ranger-software.github.io/indy-foy/

