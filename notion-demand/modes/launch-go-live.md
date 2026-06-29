# Launch - Go-live Mode

Use this mode when creating or updating a linked task with `Lifecycle = Launch` and `Stage = Go-live`.

Go-live controls the approved release, verifies live behaviour, and hands ownership into Hypercare / Support.

## Purpose

Coordinate:

- final release scope and decision;
- ordered activation or deployment actions;
- owners, timing, dependencies, and checkpoints;
- monitoring and stop conditions;
- rollback or fallback;
- stakeholder and support communications;
- immediate live verification;
- known issues and hypercare handoff.

## Planning depth

Before creating or expanding tasks in this mode, confirm whether the user wants lightweight coordination or a detailed downstream breakdown when that choice is not already clear.

- Lightweight means one concise checkpoint/plan that developers can use and update while they own detailed tasking.
- Detailed means a fuller set of downstream tasks, subtasks, owners, sequencing, and handoffs.

Default to lightweight only when the user asked for it, detailed tasking would duplicate existing developer-owned planning, or granular tasks already exist.

## Notion mapping

| Task field | Expected value |
|---|---|
| `Task` | Go-live outcome. |
| `Lifecycle` | `Launch`. |
| `Stage` | `Go-live`. |
| `Status` | Use a valid live task status. |
| `Priority` | Align to release risk. |
| `Project` | Relation to parent demand. |

## Inputs

Use the approved Release Readiness artefact, release candidate, rollout/fallback instructions, monitoring plan, known issues, support plan, and communications plan.

If readiness changed after approval, pause and reassess Release Readiness before continuing.

## Evidence gate

Before starting go-live, confirm:

1. Release decision and approved scope.
2. Named launch decision-maker and action owners.
3. Executable sequence and dependencies.
4. Required access, configuration, data, or migration readiness.
5. Monitoring signals and stop conditions.
6. Rollback/fallback owner and procedure.
7. Support and escalation availability.
8. Communication recipients and timing.

## Workflow

1. Reconfirm readiness and scope.
2. Record start decision, owners, and timing.
3. Execute the ordered checklist.
4. Verify each checkpoint using observable evidence.
5. Monitor stop conditions and known risks.
6. Roll back, fall back, or pause when criteria are met.
7. Complete immediate post-launch checks.
8. Record final state, issues, decisions, and communications.
9. Hand off to Hypercare / Support.

## Output contract

```markdown
# Go-live

## Launch decision and scope
...

## Go-live runbook
| Order | Action | Owner | Dependency | Evidence / checkpoint | Status |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## Monitoring and stop conditions
| Signal | Expected | Stop / escalation threshold | Owner |
|---|---|---|---|
| ... | ... | ... | ... |

## Rollback / fallback
| Trigger | Action | Owner | Verification |
|---|---|---|---|
| ... | ... | ... | ... |

## Communications
| Audience | Message | Timing | Owner | Status |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Immediate post-launch verification
| Check | Evidence | Result | Owner |
|---|---|---|---|
| ... | ... | ... | ... |

## Issues and decisions
| Item | Impact | Decision / action | Owner | Status |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Hypercare handoff
- Monitoring focus:
- Known issues:
- Risks:
- Owners:
- Next checkpoint:
```

## Review gate

Go-live is complete only when:

- the approved sequence is complete or an explicit rollback/fallback decision is recorded;
- live checks provide observable evidence;
- issues and deviations are documented and owned;
- support and Hypercare / Support ownership is active;
- the final release state is clear.

## Guardrails

- Do not proceed when readiness has materially changed.
- Do not treat checklist completion as proof of live correctness.
- Do not omit failed actions, deviations, or rollback decisions.
- Do not expand scope during go-live.
