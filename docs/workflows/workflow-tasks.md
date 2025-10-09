# Workflow, Milestone Tasks and Sub-Tasks

This guide explains the three-layer flow used in this repo: **Milestone Task → Deliverable Task → Sub-Tasks**. It standardizes titles, labels, and checklists, and shows how to link everything so that progress rolls up automatically.

## Goals
- Clear planning structure that stays consistent across all milestones,
- One parent issue per milestone, one parent issue per deliverable, concrete sub-tasks for actual work,
- Automatic progress via checkboxes and linked issues.

## Layers at a glance
1. **Milestone Task**, the umbrella for one milestone  
   Title, `[Mxx][Task] <Title>`  
   Checklist contains **deliverables** only, not sub-tasks.

2. **Deliverable Task**, the umbrella for one outcome inside the milestone  
   Title, `[DEL][<KIND>] <Deliverable Title>`  
   Checklist contains the **sub-tasks**.

3. **Sub-Tasks**, atomic work items  
   Title, `[<TYPE>][R-###] <Short title>`, for example `[CODE] Interaction system, verbcoin prototype`.

## Naming and prefixes
- Milestone Task, `[M01][Task] Vertical Slice Tech`  
- Deliverable kinds, `VS` Vertical Slice, `REL` Release, `DOC` Documentation Package, `SYS` System or Feature, `OPS` Publishing or Website  
- Sub-Task types, `BG`, `ART`, `LD`, `NAR`, `AUD`, `CODE`, `DOC`, `TD`

> Labels can be auto-applied from prefixes by a workflow if enabled.

## Step-by-step

### 1) Create a Milestone Task
- Use the **Milestone Task** issue form,
- Set the milestone in the sidebar,
- Fill the checklist with **deliverables** only, example:
    - [ ] [DEL][VS] Create Vertical Slice
    - [ ] [DEL][REL] Publish Vertical Slice build (ZIP + website link)
    - [ ] [DEL][DOC] Create GDD
    - [ ] [DEL][DOC] Create TDD

- Convert each line to an issue via **… → Convert to issue**, choose **Deliverable Task**.

### 2) Create a Deliverable Task
- Use the **Deliverable Task** form,
- Fill the **Milestone** field, and link the **Parent Milestone Task**,
- Add a checklist with **sub-tasks**, one line each, then **Convert to issue**, choose **Sub-Task** or a specialized form,
- Keep acceptance criteria concise and testable.

See detailed guide, [Deliverable Tasks](./deliverable-tasks.md).

### 3) Create Sub-Tasks
- Use the **Sub-Task** form,
- Pick **Type** (`BG`, `ART`, `LD`, `NAR`, `AUD`, `CODE`, `DOC`, `TD`),
- Provide a **Reference** like `R-214` for a room or a module id,
- Set **Parent Deliverable** to the issue number of the deliverable.

Guides per type:
- [Background Tasks](docs/workflows/subtasks/background-tasks.md)
- [Art Tasks](docs/workflows/subtasks/art-tasks.md)
- [Room-Design Tasks](docs/workflows/subtasks/room-design-tasks.md)
- [Narrative Tasks](docs/workflows/subtasks/narrative-tasks.md)
- [Audio Tasks](docs/workflows/subtasks/audio-tasks.md)
- [Tech-Debt Tasks](docs/workflows/subtasks/techdebt-tasks.md)
- [Code Tasks](docs/workflows/subtasks/code-tasks.md)
- [Documentation Tasks](docs/workflows/subtasks/doc-tasks.md)

## Progress roll-up
- Closing a Sub-Task ticks its checkbox in the **Deliverable** automatically,
- Closing a Deliverable ticks its checkbox in the **Milestone Task** automatically,
- The milestone progress bar updates accordingly.

## Example, M01 Vertical Slice
- Milestone Task, `[M01][Task] Vertical Slice Tech`,
- Deliverable, `[DEL][VS] Create Vertical Slice`, sub-tasks for Code, Background, Art, Audio, Narrative, Level-Design, Docs,
- Deliverable, `[DEL][REL] Publish Vertical Slice build`.

<!-- Maintainer note, this repo is public, keep sensitive links out of public docs -->
