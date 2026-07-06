# Discovery - Shaping Mode

Use this mode to add the meat to the bones. Shaping turns an idea into a coherent direction that Design can preserve.

## Purpose

Define:

- shaped product/business model;
- selected or proposed option and rationale;
- commercial strategy and cost structure when relevant;
- business scenarios and operating model;
- high-level customer journey;
- capability impact and feasibility;
- design principles and downstream Design focus.

## File

Write to `01-discovery/shaping.md`. Update `qualify.md` and `traceability.md` with `BD-*` decisions and Design focus items.

## Minimum fact base

Before writing, use:

- `01-discovery/ideation.md` when available;
- latest user instruction;
- relevant current product, process, customer, operational, commercial, legal, financial, or technical evidence;
- open questions from Ideation.

If Shaping discovers the idea is actually multiple demands, record the split recommendation in `qualify.md` before continuing.

## Workflow

1. Read Ideation and root control files.
2. Confirm or revise the demand intent without losing decision history.
3. Compare material business/model options.
4. Choose or recommend the shaped direction and explain why.
5. Define business scenarios that downstream Requirements and QA can test.
6. Capture operating model implications, ownership, controls, and handoffs at a high level.
7. Define commercial proposition, pricing, fees, costs, route to market, or adoption approach when relevant.
8. Create a high-level customer journey when the demand affects multiple actors or journey moments.
9. Record design principles and Design-stage focus areas.
10. Update `traceability.md` with shaped business design points.

## Output contract

Use this structure:

```markdown
# Shaping

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: 01-discovery/ideation.md, qualify.md
Blocks: none

## Shaping executive summary

## Shaped demand

## Option assessment
| Option | Model / approach | Benefits | Trade-offs | Decision |
|---|---|---|---|---|

## Selected direction and rationale

## Business design decisions
| ID | Decision | Rationale | Alternatives rejected / parked | Downstream impact |
|---|---|---|---|---|
| BD-AREA-001 |  |  |  |  |

## Commercial / adoption strategy
| Area | Direction | Cost / revenue / adoption implication | Open risk |
|---|---|---|---|

## Business scenarios
| Scenario ID | Scenario | Actors | Trigger | Expected outcome | Downstream requirement focus |
|---|---|---|---|---|---|

## High-level customer journey
| Phase | Actor action | Touchpoint | Backstage / operational involvement | Pain or control point | Outcome |
|---|---|---|---|---|---|

## Operating model assessment
| Area | Current state | Target direction | Owner | Risk / control | Design follow-up |
|---|---|---|---|---|---|

## Capability and feasibility view
| Capability | Reuse / change / new | Feasibility | Risk | Design implication |
|---|---|---|---|---|

## Design principles
| Principle | Why it matters | Applies to |
|---|---|---|

## Recommended Design focus
| Mode | Focus | Rationale | Priority |
|---|---|---|---|

## Open decisions carried forward
| ID | Decision needed | Owner | Blocks |
|---|---|---|---|
```

## Review gate

Shaping is not complete unless:

- the selected or recommended option is explicit;
- material alternatives are captured or intentionally omitted;
- business scenarios are testable enough to feed Requirements and QA;
- commercial, operating, legal, data, support, and technical implications are covered when relevant;
- Design focus tells the next agent which modes matter and why;
- unresolved decisions are marked as blocking or non-blocking.

## Handoff

Handoff to Requirements for behavioural rules, UI/CX for journeys/screens, Process for operations, Solution for architecture, and Technical Design only after product/business gaps that would affect implementation are resolved or explicitly blocked.
