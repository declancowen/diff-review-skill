# Review - Hypercare / Support Mode

Use this mode after go-live with `Lifecycle = Review` and `Stage = Hypercare / Support`.

Hypercare stabilises the released outcome and establishes whether it can move into normal support and outcome measurement.

## Purpose

Track:

- live health and expected behaviour;
- incidents, defects, feedback, and operational friction;
- severity, impact, ownership, and response;
- urgent fixes, mitigations, and escalation;
- known risks and support themes;
- readiness to exit hypercare.

## Planning depth

Before creating or expanding tasks in this mode, confirm whether the user wants lightweight coordination or a detailed downstream breakdown when that choice is not already clear.

- Lightweight means one concise checkpoint/plan that developers can use and update while they own detailed tasking.
- Detailed means a fuller set of downstream tasks, subtasks, owners, sequencing, and handoffs.

Default to lightweight only when the user asked for it, detailed tasking would duplicate existing developer-owned planning, or granular tasks already exist.

## Notion mapping

| Task field | Expected value |
|---|---|
| `Task` | Hypercare / Support outcome. |
| `Lifecycle` | `Review`. |
| `Stage` | `Hypercare / Support`. |
| `Status` | Use a valid live task status. |
| `Priority` | Align to live impact. |
| `Project` | Relation to parent demand. |

## Inputs and evidence gate

Use Go-live handoff, monitoring evidence, support feedback, incidents, defects, operational observations, user feedback, and known issues.

Before closing Hypercare / Support, confirm:

1. Launch-critical monitoring is stable or understood.
2. Critical/high-impact issues are resolved, mitigated, or formally owned.
3. Recurring support themes and operational friction are documented.
4. Normal support ownership and escalation are active.
5. Measurement can proceed without unresolved instability invalidating results.

## Workflow

1. Confirm monitoring focus, owners, cadence, and exit criteria.
2. Gather live signals and feedback.
3. Classify issues by severity, impact, scope, and root-cause confidence.
4. Separate urgent fixes, design gaps, support actions, and follow-up demand candidates.
5. Track mitigation, resolution, and residual risk.
6. Assess operational and support readiness.
7. Decide whether to extend or exit hypercare.
8. Hand off reliable signals and caveats to Outcomes Review.

## Output contract

```markdown
# Hypercare / Support

## Hypercare scope and exit criteria
...

## Live health
| Signal | Expected | Actual | Interpretation | Owner |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Issues and feedback
| Item | Severity | Impact | Classification | Action | Owner | Status |
|---|---|---|---|---|---|---|
| ... | ... | ... | defect / support / design gap / follow-up | ... | ... | ... |

## Operational and support themes
...

## Fixes, mitigations, and residual risks
| Item | Response | Evidence | Residual risk |
|---|---|---|---|
| ... | ... | ... | ... |

## Hypercare decision
Exit / extend / blocked, with rationale.

## Outcomes Review handoff
- Reliable signals:
- Measurement caveats:
- Unresolved issues:
- Follow-up candidates:
```

## Review gate

Hypercare can exit only when live health is understood, urgent issues are controlled, normal ownership is active, and measurement caveats are explicit.

## Guardrails

- Do not hide a material design gap as a support issue.
- Do not close hypercare because a fixed time period elapsed.
- Do not create unapproved scope inside urgent-fix tracking.
- Raise substantial new outcomes as follow-up demands.
