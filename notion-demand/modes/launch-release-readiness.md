# Launch - Release Readiness Mode

Use this mode when creating or updating a linked task with `Lifecycle = Launch` and `Stage = Release Readiness`.

Release Readiness decides whether the approved scope can launch safely. It does not repair missing design or redefine release scope.

## Purpose

Confirm:

- exact release scope and deferred scope;
- requirement and QA completion;
- accepted known issues;
- rollout, rollback, and fallback;
- configuration, permissions, data, and migration readiness;
- analytics, monitoring, and alerting;
- operational, support, communications, policy, and legal readiness;
- accountable owners and launch decision.

## Planning depth

Before creating or expanding tasks in this mode, confirm whether the user wants lightweight coordination or a detailed downstream breakdown when that choice is not already clear.

- Lightweight means one concise checkpoint/plan that developers can use and update while they own detailed tasking.
- Detailed means a fuller set of downstream tasks, subtasks, owners, sequencing, and handoffs.

Default to lightweight only when the user asked for it, detailed tasking would duplicate existing developer-owned planning, or granular tasks already exist.

## Notion mapping

| Task field | Expected value |
|---|---|
| `Task` | Release-readiness outcome. |
| `Lifecycle` | `Launch`. |
| `Stage` | `Release Readiness`. |
| `Status` | Use a valid live task status. |
| `Priority` | Align to release risk and parent priority. |
| `Project` | Relation to parent demand. |

## Inputs

Use only relevant approved evidence:

- parent demand and agreed release scope;
- Requirements and acceptance criteria;
- relevant UX, Process, Solution, and Technical Design decisions;
- Development completion evidence;
- QA results, defects, and sign-off;
- rollout, migration, configuration, monitoring, support, communications, and policy evidence.

Route material gaps back to the owning mode. Do not hide them in a readiness checklist.

## Evidence gate

Before recommending launch, establish:

1. Included and deferred scope.
2. Requirement and scenario coverage.
3. QA status and unresolved defect severity.
4. Data/configuration/migration actions and verification.
5. Rollout mechanism and stop conditions.
6. Rollback or fallback feasibility.
7. Monitoring signals and accountable responders.
8. Support process and escalation route.
9. Communications and documentation readiness.
10. Any legal, policy, privacy, security, or operational sign-off.

If a launch-critical item has no evidence, mark readiness blocked or ready with an explicit accepted risk. Never infer readiness from silence.

## Workflow

1. Confirm the release candidate and scope.
2. Trace release scope to approved requirements and QA evidence.
3. Separate blockers, accepted risks, deferred work, and non-blocking known issues.
4. Validate rollout, rollback/fallback, configuration, data, and dependency readiness.
5. Validate monitoring, support, communications, and ownership.
6. Record required approvals and the launch decision.
7. Define go-live entry criteria and immediate stop conditions.
8. Run the review gate.

## Output contract

```markdown
# Release Readiness

## Release decision
Ready / ready with accepted risks / blocked.

## Release scope
| Scope item | Evidence | Status |
|---|---|---|
| ... | ... | ... |

## Deferred / out of scope
| Item | Reason | Follow-up |
|---|---|---|
| ... | ... | ... |

## Readiness assessment
| Area | Evidence | Status | Owner | Action |
|---|---|---|---|---|
| Requirements and QA | ... | ... | ... | ... |
| Defects and known issues | ... | ... | ... | ... |
| Data and migration | ... | ... | ... | ... |
| Configuration and permissions | ... | ... | ... | ... |
| Dependencies | ... | ... | ... | ... |
| Rollout and fallback | ... | ... | ... | ... |
| Monitoring and alerting | ... | ... | ... | ... |
| Support and escalation | ... | ... | ... | ... |
| Communications and documentation | ... | ... | ... | ... |
| Policy / legal / privacy / security | ... | ... | ... | ... |

## Risks and blockers
| Item | Classification | Impact | Owner | Resolution / acceptance |
|---|---|---|---|---|
| ... | blocker / accepted risk / known issue | ... | ... | ... |

## Go-live entry criteria
- ...

## Stop conditions
- ...

## Approvals
| Approval | Owner | Status | Notes |
|---|---|---|---|
| ... | ... | ... | ... |
```

## Review gate

Release Readiness passes only when:

- scope and deferred work are explicit;
- every launch-critical area has evidence;
- unresolved defects and risks are classified and owned;
- rollout, fallback, monitoring, and support are executable;
- blockers are resolved or the launch decision is blocked;
- the final recommendation is unambiguous.

## Handoff

Hand off to Go-live with the approved scope, checklist, owners, monitoring plan, accepted risks, stop conditions, and fallback plan.

## Guardrails

- Do not label an item ready without evidence.
- Do not downgrade a blocker to a risk to preserve a launch date.
- Do not use Launch to invent missing requirements or solution decisions.
- Do not include unrelated future scope.
