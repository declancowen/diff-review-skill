# Design - Requirements Mode

Use this mode to define testable business requirements. Requirements own behaviour, rules, states, acceptance criteria, priority, and completion status.

## Purpose

Create or update `BR-*` requirements that downstream UI/CX, Process, Solution, Technical, Delivery, and QA artefacts can trace back to.

## File

Write to `02-design/requirements.md`. Update `traceability.md` for every new, changed, or completed `BR-*`.

## Minimum fact base

Use:

- Ideation and Shaping business design;
- business scenarios;
- current product/process evidence when relevant;
- user constraints and priorities;
- open decisions from Discovery.

Do not invent UI, process, or technical implementation details here. Flag those for the relevant mode.

## Requirement shape

Each material requirement should include:

- stable ID: `BR-[AREA]-###`;
- statement in testable language;
- actor;
- trigger or condition;
- expected behaviour/outcome;
- priority;
- acceptance criteria;
- source business design or scenario;
- status: `Draft`, `Ready`, `Blocked`, `Done`, or `Removed`;
- evidence or validation link when complete.

Use EARS-style phrasing where it helps:

- `When [trigger], the system/process shall [response].`
- `While [state], the user shall [capability].`
- `If [condition], the system/process shall [response].`

## Workflow

1. Read root control files and Discovery outputs.
2. Pull business scenarios and design decisions into requirement candidates.
3. Deduplicate overlapping requirements.
4. Split requirements that contain multiple behaviours, actors, states, or acceptance paths.
5. Mark missing upstream decisions as blockers rather than guessing.
6. Add acceptance criteria and priority.
7. Update `traceability.md`.
8. Update `qualify.md` with requirement status and next modes.

## Output contract

Use this structure:

```markdown
# Requirements

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: 01-discovery/shaping.md, traceability.md
Blocks: none

## Requirements summary

## Scope and assumptions

## Business requirements
| ID | Requirement | Actor | Trigger / condition | Acceptance criteria | Priority | Source | Status |
|---|---|---|---|---|---|---|---|
| BR-AREA-001 |  |  |  |  | Must | BD-AREA-001 | Draft |

## Business rules
| ID | Rule | Applies to | Exception | Source | Status |
|---|---|---|---|---|---|

## States and transitions
| ID | State / transition | Trigger | Expected result | Source | Status |
|---|---|---|---|---|---|

## Non-functional business expectations
| ID | Expectation | Rationale | Validation |
|---|---|---|---|

## Open questions / decisions needed
| ID | Question | Impact | Blocks |
|---|---|---|---|

## Handoff notes
```

## Review gate

Requirements are not ready unless:

- every must-have business behaviour has a `BR-*` ID;
- acceptance criteria are measurable or reviewable;
- each requirement traces to a business design point, scenario, user instruction, or evidence source;
- UI, process, solution, and technical gaps are routed to the right modes;
- no requirement is marked `Done` without evidence.
