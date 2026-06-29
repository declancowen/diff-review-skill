# Review - Outcomes and Benefits Mode

Use this mode with `Lifecycle = Review` and `Stage = Measure Outcomes` or `Stage = Benefits Review`.

Measure Outcomes establishes what changed. Benefits Review judges whether that change delivered the intended value.

## Purpose

Compare intended and actual:

- outcomes and success measures;
- adoption, usage, experience, operational, risk, or financial effects;
- qualitative feedback;
- costs, trade-offs, and unintended consequences;
- realised and unrealised benefits;
- evidence quality and measurement gaps;
- recommendation to close, optimise, or create a follow-up demand.

## Planning depth

Before creating or expanding tasks in this mode, confirm whether the user wants lightweight coordination or a detailed downstream breakdown when that choice is not already clear.

- Lightweight means one concise checkpoint/plan that developers can use and update while they own detailed tasking.
- Detailed means a fuller set of downstream tasks, subtasks, owners, sequencing, and handoffs.

Default to lightweight only when the user asked for it, detailed tasking would duplicate existing developer-owned planning, or granular tasks already exist.

## Notion mapping

| Task field | Expected value |
|---|---|
| `Task` | Outcome-measurement or benefits-review outcome. |
| `Lifecycle` | `Review`. |
| `Stage` | `Measure Outcomes` or `Benefits Review`. |
| `Status` | Use a valid live task status. |
| `Project` | Relation to parent demand. |

## Inputs and evidence gate

Use the parent demand's intended value, Shaping goals and benefits, Requirements success criteria, analytics, operational data, research, feedback, support signals, and Hypercare caveats.

Do not claim an outcome or benefit without evidence. Classify evidence as:

- strong: direct, reliable, and sufficiently representative;
- directional: useful but incomplete or early;
- unavailable: required evidence does not exist.

## Workflow

1. Recover the intended outcomes, benefits, baseline, and time horizon.
2. Confirm the measurement method and evidence quality.
3. Compare expected and actual results.
4. Identify external factors, caveats, costs, and unintended consequences.
5. Determine which benefits were realised, partially realised, or not realised.
6. Explain gaps without inventing causality.
7. Recommend close, continue measuring, optimise, or create follow-up demand.

## Output contract

```markdown
# Outcomes / Benefits Review

## Review scope and evidence quality
...

## Intended outcomes and benefits
| Outcome / benefit | Baseline | Target | Time horizon |
|---|---|---|---|
| ... | ... | ... | ... |

## Actual outcomes
| Measure | Expected | Actual | Evidence quality | Interpretation |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Qualitative feedback and operational impact
...

## Benefits assessment
| Benefit | Status | Evidence | Caveat |
|---|---|---|---|
| ... | realised / partial / not realised / unknown | ... | ... |

## Costs, trade-offs, and unintended consequences
...

## Measurement gaps
...

## Recommendation
Close / continue measuring / optimise / create follow-up demand.
```

## Review gate

The review passes only when conclusions trace to evidence, caveats are explicit, intended value is assessed, and the recommendation follows from the findings.

## Guardrails

- Do not confuse output completion with outcome achievement.
- Do not infer causality from correlation without evidence.
- Do not hide missing measurement.
- Do not rewrite original targets after seeing results.
