# Review - Outcomes / Benefits Mode

Use this mode to measure actual outcomes and benefits against the demand's original intent.

## Purpose

Assess whether the delivered demand achieved its intended customer, business, operational, quality, commercial, or technical outcomes.

## File

Write to `04-review/outcomes-benefits.md`. Update `traceability.md` with `RM-*` measures and `qualify.md` with review status.

## Minimum fact base

Use:

- Ideation and Shaping intended outcomes;
- Requirements acceptance criteria;
- Release and Hypercare evidence;
- metrics, support feedback, usage, operational data, revenue/cost data, quality data, or stakeholder feedback.

If evidence is unavailable, record the measurement gap rather than inventing a result.

## Workflow

1. Read the full demand traceability chain.
2. Reconstruct intended outcomes and benefits.
3. Compare actual results with baseline or expected direction.
4. Assess qualitative feedback and operational impact.
5. Review `quality-gates.md` to identify whether architecture, diff-review, Fallow, repo-audit, or Graphify evidence predicted or missed live outcomes.
6. Identify costs, trade-offs, unintended consequences, and evidence gaps.
7. Recommend close, continue measuring, remediate, or create an optimisation demand.

## Output contract

Use this structure:

```markdown
# Outcomes / Benefits

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: qualify.md, traceability.md, 04-review/hypercare-support.md
Blocks: none

## Review scope and evidence quality

## Intended outcomes and benefits
| RM ID | Outcome / benefit | Source | Expected signal | Evidence needed |
|---|---|---|---|---|
| RM-AREA-001 |  | BD-AREA-001 |  |  |

## Actual outcomes
| RM ID | Actual result | Evidence | Confidence | Assessment |
|---|---|---|---|---|

## Qualitative feedback and operational impact

## Benefits assessment
| Benefit | Achieved / partial / not achieved | Rationale | Follow-up |
|---|---|---|---|

## Costs, trade-offs and unintended consequences

## Measurement gaps
| Gap | Impact | How to close | Owner |
|---|---|---|---|

## Quality gate hindsight
| Gate | Signal before release | Outcome observed | Learning / follow-up |
|---|---|---|---|

## Recommendation
```

## Review gate

Outcomes Review is not complete unless:

- intended outcomes are traced back to Discovery or Requirements;
- actual results are evidence-backed or marked as evidence gaps;
- trade-offs and unintended consequences are considered;
- recommendation is explicit.
