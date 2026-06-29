# Review - Learnings and Optimisation Mode

Use this mode with `Lifecycle = Review` and one of:

- `Capture Learnings`
- `Identify Optimisation Opportunities`
- `Optimisation / Enhancement Request`

This mode converts evidence and learning into proportionate follow-up action.

## Purpose

Define:

- what worked, failed, or surprised;
- reusable product, delivery, operational, and measurement learning;
- optimisation opportunities and their evidence;
- whether each opportunity is a small continuation or a new parent demand;
- value, effort, risk, priority, dependency, and timing;
- final recommendation and ownership.

## Planning depth

Before creating or expanding tasks in this mode, confirm whether the user wants lightweight coordination or a detailed downstream breakdown when that choice is not already clear.

- Lightweight means one concise checkpoint/plan that developers can use and update while they own detailed tasking.
- Detailed means a fuller set of downstream tasks, subtasks, owners, sequencing, and handoffs.

Default to lightweight only when the user asked for it, detailed tasking would duplicate existing developer-owned planning, or granular tasks already exist.

## Notion mapping

| Task field | Expected value |
|---|---|
| `Task` | Learning or optimisation outcome. |
| `Lifecycle` | `Review`. |
| `Stage` | The exact relevant live Review stage. |
| `Status` | Use a valid live task status. |
| `Project` | Relation to the original parent demand. |

Create a new parent demand when an opportunity has a materially different outcome, users, scope, owner, release path, risk, or independent value case.

## Inputs and evidence gate

Use Outcomes/Benefits Review, Hypercare, support themes, analytics, research, operational evidence, delivery lessons, and unresolved risks.

Do not propose an optimisation solely because it is imaginable. Require a clear evidence signal, value hypothesis, or unresolved strategic need.

## Workflow

1. Capture evidence-backed learnings.
2. Identify root causes and avoid symptom-only recommendations.
3. Generate opportunities tied to a finding or strategic objective.
4. Assess value, effort, risk, dependencies, and confidence.
5. Classify each as close/no action, small optimisation, experiment, or new demand.
6. Prioritise and assign ownership.
7. Preserve traceability to the original finding.

## Output contract

```markdown
# Learnings and Optimisation

## Learnings
| Learning | Evidence | Reuse / implication |
|---|---|---|
| ... | ... | ... |

## Opportunities
| Opportunity | Evidence / problem | Value | Effort | Risk | Confidence | Classification |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | optimisation / experiment / new demand / no action |

## Prioritisation and recommendation
| Opportunity | Priority | Timing | Owner | Next action |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## New demand candidates
| Candidate | Why separate | Proposed type | Source finding |
|---|---|---|---|
| ... | ... | Feature / CX / Bug / CI | ... |

## Closure recommendation
...
```

## Review gate

The output passes when opportunities trace to evidence, classifications are proportionate, major new scope is separated into new demands, and ownership is clear.

## Guardrails

- Do not hide major scope inside the original demand.
- Do not create follow-up demands without a distinct outcome and rationale.
- Do not present assumptions as lessons.
- Do not prioritise solely by ease.
