# Review - Learnings / Optimisation Mode

Use this mode to capture learnings, identify follow-up improvements, and decide whether new demands are needed.

## Purpose

Convert review evidence into actionable learnings and optimisation candidates without rewriting the original demand's history.

## File

Write to `04-review/learnings-optimisation.md`. Update `qualify.md` with closure or follow-up status.

## Minimum fact base

Use:

- Hypercare;
- Outcomes / Benefits;
- defects, support themes, stakeholder feedback, metrics, missed expectations, delivery retrospectives, and open risks.

## Workflow

1. Read Review outputs and traceability.
2. Capture what worked, what did not, what surprised the team, and what should change.
3. Compare review outcomes against `quality-gates.md` to identify missed architecture, diff-review, Fallow, repo-audit, or Graphify signals.
4. Separate remediation, optimisation, new capability, and parked ideas.
5. Prioritise follow-up opportunities by value, urgency, risk, effort, and dependency.
6. Recommend close, monitor, remediate, or create new demand(s).
7. Update `qualify.md` and `quality-gates.md` with final status and any follow-up demand candidates.

## Output contract

Use this structure:

```markdown
# Learnings / Optimisation

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: 04-review/hypercare-support.md, 04-review/outcomes-benefits.md
Blocks: none

## Learnings
| Learning | Evidence | Impact | Applies to |
|---|---|---|---|

## Optimisation opportunities
| Opportunity | Source | Value | Risk reduced | Effort | Recommendation |
|---|---|---|---|---|---|

## Remediation candidates
| Issue | Root cause | Required action | Owner | Urgency |
|---|---|---|---|---|

## New demand candidates
| Demand candidate | Why separate | Suggested priority | Source evidence |
|---|---|---|---|

## Quality-system learnings
| Gate | What it caught / missed | Process update | Follow-up |
|---|---|---|---|

## Closure recommendation

## Final checklist
- [ ] Traceability is up to date
- [ ] Follow-up actions are captured
- [ ] Demand can be closed or has a named blocker
```

## Review gate

Learnings / Optimisation is not complete unless:

- learnings are evidence-backed;
- follow-up work is separated from historical intent;
- optimisation candidates are prioritised;
- closure recommendation is explicit;
- `qualify.md` records the final status.
