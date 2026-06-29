# Delivery — Development Planning Mode

Use this mode when creating or updating linked child tasks with `Lifecycle = Delivery` and `Stage = Development`.

Development Planning converts approved design and technical planning into outcome-based build work.

## Purpose

Development Planning should create a clear build plan without re-deciding product scope.

It should define:

- build outcomes;
- implementation slices;
- dependencies;
- workstreams/subtasks;
- sequencing;
- blockers;
- validation expectations;
- QA handoff.

## Planning depth

Before creating or expanding tasks in this mode, confirm whether the user wants lightweight coordination or a detailed downstream breakdown when that choice is not already clear.

- Lightweight means one concise checkpoint/plan that developers can use and update while they own detailed tasking.
- Detailed means a fuller set of downstream tasks, subtasks, owners, sequencing, and handoffs.

Default to lightweight only when the user asked for it, detailed tasking would duplicate existing developer-owned planning, or granular tasks already exist.

## Notion mapping

Create or update linked **Delivery child tasks**.

Task properties:

| Task field | Expected value |
|---|---|
| `Task` | Outcome-based build name, not a technical layer name. |
| `Lifecycle` | `Delivery`. |
| `Stage` | `Development`. |
| `Status` | Use a valid live task status. |
| `Priority` | Align to parent or technical priority. |
| `Project` | Relation to parent demand. |
| `Parent-task` / `Sub-tasks` | Use for workstreams where supported. |

Top-level Development tasks should represent build outcomes.

Represent top-level tasks as independently reviewable build outcomes.

Usually avoid as top-level tasks:

- Frontend work.
- Backend work.
- API work.
- Database work.

Use those as sub-items/checklist workstreams under an outcome.

## Inputs to use

Use approved:

- Requirements;
- UX Design;
- Process Design;
- Solution Design;
- Technical Requirements;
- Technical Design;
- Technical Tasks.

Do not invent new product decisions in Delivery. If a gap appears, route back to the relevant Design mode.

## Minimum fact base

Before creating Development tasks, confirm:

1. Approved requirements exist or are intentionally lightweight.
2. UX/process/solution/technical context exists where relevant.
3. Technical Tasks identify dependencies or blockers.
4. Work can be sliced into outcomes.
5. QA expectations are known.
6. Critical decisions are resolved.

If critical decisions remain open, create blocker/spike tasks only.

## Workflow

1. Read approved upstream artefacts.
2. Identify build outcomes.
3. Group technical tasks under outcome-based delivery tasks.
4. Identify dependencies and sequencing.
5. Identify workstreams/subtasks.
6. Identify validation required per outcome.
7. Identify blockers and decisions needed.
8. Prepare QA handoff.

## Output contract

```markdown
# Development Plan

## Source context
| Source | Used for |
|---|---|
| Requirements | ... |
| UX / Process / Solution | ... |
| Technical Design | ... |
| Technical Tasks | ... |

## Build outcomes
| Outcome | Requirements covered | Notes |
|---|---|---|
| ... | ... | ... |

## Development tasks
### Task 1 — [Outcome]
- Scope:
- Requirements covered:
- Technical tasks covered:
- Dependencies:
- Workstreams:
- Validation:
- Risks:
- Notes:

## Sequencing
...

## Blockers / decisions needed
...

## QA handoff
...
```

## Review gate

Before marking Development Planning ready:

- Are tasks outcome-based?
- Are dependencies clear?
- Are workstreams detailed enough for execution?
- Are blockers explicit?
- Is validation mapped to requirements?
- Is QA handoff clear?
- Has new scope been avoided?

## Guardrails

Do not:

- use Delivery to make hidden product decisions;
- create disconnected frontend/backend/API/data top-level tasks;
- lose traceability to requirements;
- continue if Technical Design says implementation is blocked;
- create build work for unrelated demand scope.
