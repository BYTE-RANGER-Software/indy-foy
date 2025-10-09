# Code Tasks, Modules and Scripting (AGS)

**Purpose**, implement AGS modules and gameplay scripts, integrate systems like interaction, inventory, dialog glue, room flow, save/load.

## Creation
- Create a checklist line in the **Deliverable**, for example `- [ ] Interaction system, verbcoin prototype`.
- Convert to issue with **Code Sub-Task** (or **Sub-Task** with **Type = CODE**).
- Title, `[CODE] Interaction system, verbcoin prototype`.

## Deliverables
- **Module or script** with public API, clear inputs, outputs, events.
- **Integration** points, rooms, GUIs, characters affected are listed.
- **Tests / smoke steps** to verify behavior in-engine.
- **Docs** updated where needed (TDD section).

## Acceptance criteria
- Integrated in-engine, no compile errors or warnings,
- API documented in **TDD**, edge cases covered,
- No regressions in affected rooms or GUIs,
- Naming and paths follow project conventions.

## Minimal body template
```md
### Scope
What is implemented, which rooms/GUI/characters are affected.

### Interfaces (API)
Public functions, events, expected inputs/outputs.

### Integration
Rooms (e.g., R-214), GUIs, global flags/vars, save/load impact.

### Test plan
Steps to verify, expected results, edge cases.

### Parent
#<deliverable-issue>

[Back to the main workflow](../workflow-tasks.md)
