# Contributing Guide

Thanks for your interest in contributing. This project uses a three-layer issue workflow and a simple, explicit branching scheme. Please read this short guide before opening issues or pull requests.

> New here, start with **How we plan work** below, then see the branch naming rules.

---

## How we plan work

We manage work in three layers: **Milestone Task → Deliverable Task → Sub-Tasks**. This keeps planning predictable, and progress rolls up automatically.

1) **Milestone Task**, one umbrella issue per milestone  
   Title, `[Mxx][Task] <Title>`  
   The checklist lists **deliverables** only, not sub-tasks.  
   → Guide, [`Workflow, Milestone Tasks and Sub-Tasks`](docs/workflows/workflow-tasks.md)

2) **Deliverable Task**, one umbrella per outcome inside the milestone  
   Title, `[DEL][<KIND>] <Deliverable Title>` where `<KIND>` is `VS`, `REL`, `DOC`, `SYS`, `OPS`  
   The checklist lists the **sub-tasks** that implement the deliverable.  
   → Guide, [`Deliverable Tasks`](docs/workflows/deliverable-tasks.md)

3) **Sub-Tasks**, atomic work items  
   Title, `[<TYPE>][R-###] <Short title>` with `<TYPE>` in `BG`, `ART`, `LD`, `NAR`, `AUD`, `CODE`, `DOC`, `TD`  
   → Per-type guides,  
   [`Background`](docs/workflows/subtasks/background-tasks.md), [`Art`](docs/workflows/subtasks/art-tasks.md), [`Level-Design`](docs/workflows/subtasks/level-design-tasks.md), [`Narrative`](docs/workflows/subtasks/narrative-tasks.md), [`Audio`](docs/workflows/subtasks/audio-tasks.md), [`Tech-Debt`](docs/workflows/subtasks/techdebt-tasks.md), [`Code`](docs/workflows/subtasks/code-tasks.md), [`Documentation`](docs/workflows/subtasks/doc-tasks.md)

**Create the right issue type, quick links**

- Milestone Task → `issues/new?template=milestone-task.yml`  
- Deliverable Task → `issues/new?template=deliverable-task.yml`  
- Sub-Task, generic → `issues/new?template=sub-task.yml`  
- Sub-Task, specialized → `issues/new?template=code-sub-task.yml`, `issues/new?template=art-sub-task.yml`, `issues/new?template=doc-sub-task.yml`

> Tip, write one checklist line per item, then use **… → Convert to issue** and pick the correct form.

---

## Branch Naming Convention

When creating branches, please use the following structure:

```
<type>/<scope>/<short-description>
```

### Allowed `<type>` values

| Type      | Description                                |
|-----------|--------------------------------------------|
| `feature` | New feature or enhancement                 |
| `bugfix`  | Fix for a reported bug                     |
| `hotfix`  | Critical or urgent fix (e.g. in production)|
| `chore`   | Maintenance, cleanup, or refactoring       |
| `docs`    | Documentation-related changes              |
| `meta`    | Project structure, GitHub setup, etc.      |

### 🗂 Optional `<scope>` examples

- `code`, `art`, `issue-forms`, `assets`, `repo`, `docs`, etc.

### Examples

- `meta/issue-template/bg-v0.1`
- `feature/art/bg-r-102-temple-entrance`

✅ Use `kebab-case` (lowercase with hyphens)  
🚫 Do **not** use spaces, uppercase letters, or special characters

---

## Pull requests

1. **Discuss first**, open an Issue describing goal, scope, and samples if applicable.  
2. **Branch**, follow the naming rules above.  
3. **Link**, connect your PR to its issue using **Linked issues**.  
4. **Screenshots or GIFs**, add visuals for UI, art, room changes.  
5. **Git LFS**, use LFS only for large source files or binaries.

### PR checklist

- CI is green, including docs lint, link check, script lint, and asset guard.  
- Issue is linked, labels are set by prefix or manually.  
- Docs updated if behavior, rooms, or assets changed, for example GDD, RDD, TDD.  
- For releases, the ZIP is built by CI from tags, version mismatch checks pass.

---

## Naming, prefixes, labels

- **Milestone Task**, `[Mxx][Task] <Title>`, example, `[M01][Task] Vertical Slice Tech`  
- **Deliverable Task**, `[DEL][<KIND>] <Title>`, examples, `[DEL][VS] Create Vertical Slice`, `[DEL][REL] Publish Vertical Slice`  
- **Sub-Task**, `[<TYPE>][R-###] <Short title>`, example, `[CODE][R-214] Interaction system, verbcoin prototype`

If enabled, labels are applied automatically from prefixes by a workflow. Keep titles consistent to benefit from auto-labeling and reports.

---

## Scope of sub-tasks, examples

- **CODE**, AGS modules and gameplay scripts, integration with rooms, GUIs, save/load, API documented in TDD.  
- **ART**, backdrops, walkable and walk-behind, views, inventory icons, GUI elements, imported and tested in-engine.  
- **BG**, lore and world background, consistent with timeline and references.  
- **LD**, room setup, exits, hotspots, interaction stubs, z-order checks.  
- **NAR**, dialogues, branches, flags, no dead ends.  
- **AUD**, ambient loops, SFX, music, triggers and mixing rules.  
- **DOC**, GDD, RDD, TDD sections aligned with the current build.  
- **TD**, cleanup, structure, build, scripting hygiene.

---

## Notes

- This repository is public, keep sensitive links out of public docs.  
- Use issue templates located under `.github/ISSUE_TEMPLATE/`, all workflow guides live in `docs/workflows/`.

<!-- Maintainer note: keep CONTRIBUTING concise, detailed per-discipline guidance belongs to docs/workflows/*. -->
