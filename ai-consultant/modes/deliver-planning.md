# Deliver - Planning Mode

Use this mode to turn approved Design and Technical Design into an execution plan. Delivery Planning is the bridge between what must be true and how the work will be sliced, sequenced, validated, and completed.

## Purpose

Define:

- delivery scope;
- slices (`DS-*`);
- sequencing and dependencies;
- ownership;
- quality gates;
- done criteria;
- delivery risks and blockers;
- how development, QA, release, and review will stay traceable to requirements.

## File

Write to `03-deliver/delivery-plan.md`. Update `qualify.md` and `traceability.md` with `DS-*` delivery slices.

## Minimum fact base

Use:

- `02-design/requirements.md`;
- `02-design/ui-cx-journeys.md`;
- `02-design/process-design.md`;
- `02-design/solution-design.md`;
- all technical design files;
- current blockers and decisions from `qualify.md`.

If core requirements or technical tasks are missing, create a blocked delivery plan rather than inventing them.

## Workflow

1. Read all Design artefacts and traceability.
2. Identify delivery outcomes and non-negotiable acceptance conditions.
3. Load/read and apply `$architecture-standards` when available to confirm each slice respects owners, boundaries, contracts, invariants, and enforcement.
4. Group `TT-*` tasks into coherent `DS-*` slices by user value, technical dependency, architecture boundary, risk, and validation path.
5. Sequence slices to reduce risk and unblock QA early.
6. Add quality gates to each slice: architecture checkpoint, implementation verification, QA coverage, slice diff-review loop, and evidence.
7. Define done criteria, evidence, review points, and handoff to QA.
8. Update `qualify.md`, `quality-gates.md`, and `traceability.md`.

## Output contract

Use this structure:

```markdown
# Delivery Plan

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: traceability.md, 02-design/technical-design/technical-tasks.md
Blocks: none

## Delivery objective

## Scope of delivery
| In scope | Out of scope | Blocked / dependent |
|---|---|---|

## Delivery slices
| ID | Slice | User / business value | Includes TT IDs | Depends on | QA focus | Required quality gates | Done criteria | Status |
|---|---|---|---|---|---|---|---|---|
| DS-AREA-001 |  |  | TT-AREA-001 |  | TC-AREA-001 | Architecture checkpoint; implementation verification; slice diff-review |  | Draft |

## Sequencing plan
| Order | Slice | Why now | Entry criteria | Exit criteria |
|---|---|---|---|---|

## Requirement coverage plan
| BR / UX / PR / SD / TR | Covered by slices | QA / release check |
|---|---|---|

## Risks and blockers
| ID | Risk / blocker | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|

## Delivery governance
| Checkpoint | Purpose | Evidence | Decision |
|---|---|---|---|

## Quality gate plan
| DS ID | Architecture checkpoint | Diff-review trigger | Fallow impact | Repo-audit impact | Evidence target |
|---|---|---|---|---|---|

## Handoff to development and QA
```

## Review gate

Delivery Planning is not ready unless:

- every must-have `BR-*`, material `TR-*`, and relevant `UX-*`, `PR-*`, or `SD-*` item is covered by a slice or explicitly blocked;
- slices have done criteria and validation handoff;
- each code-changing slice has a planned diff-review loop and architecture checkpoint;
- sequencing accounts for dependencies and risk;
- unresolved upstream gaps are visible in `qualify.md`.
