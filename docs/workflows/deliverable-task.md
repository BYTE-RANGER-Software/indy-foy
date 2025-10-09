# Deliverable Tasks

A Deliverable Task groups Sub-Tasks that together produce a concrete outcome, for example a Vertical Slice or a Release package.

## Title and fields
- Title, `[DEL][<KIND>] <Deliverable Title>`, examples:
  - `[DEL][VS] Create Vertical Slice`
  - `[DEL][REL] Publish Vertical Slice build`
  - `[DEL][DOC] Create TDD`
- Kind, pick from the form, `VS`, `REL`, `DOC`, `SYS`, `OPS`,
- Milestone, fill the field in the form, a workflow can auto-assign the actual milestone,
- Parent, link back to the **Milestone Task** via Linked issues, relation “tracked by”.

## Checklist pattern
Keep each sub-task on its own line, then **Convert to issue** and choose **Sub-Task** or a specialized form:

- [ ] [CODE] Interaction system, verbcoin prototype
- [ ] [BG][R-101] Docks, night, lore pass
- [ ] [ART][R-214] Backdrop docks night, final
- [ ] [AUD] Ambient loop for docks
- [ ] [NAR] Dialogue, dock worker, first pass
- [ ] [LD][R-214] Room setup, walkable and walk-behind
- [ ] [DOC] Update TDD section, Interaction system

## Acceptance criteria, example
- Demoable end to end in-engine,
- Blocking bugs resolved for the scope of this deliverable,
- Release ZIP uploaded and linked where applicable,
- Docs updated, GDD or RDD or TDD as applicable.

## Good linking hygiene
- Deliverable ↔ Milestone Task, use Linked issues, relation “tracked by”,
- Sub-Tasks ↔ Deliverable, same relation.

<!-- Maintainer note, prefix-based auto-labeling can be enabled via workflow -->

