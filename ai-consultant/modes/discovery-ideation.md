# Discovery - Ideation Mode

Use this mode for the first structured articulation of a demand. Ideation is business and product focused. It creates enough clarity to decide whether shaping is worth doing.

## Purpose

Define:

- the idea in plain language;
- the problem or opportunity;
- the intended customer, user, operational, or commercial value;
- the initial business design and model;
- early scope and non-goals;
- early risks, assumptions, and open questions;
- whether the demand should move into Shaping.

## File

Write to `01-discovery/ideation.md`. Update `qualify.md` and `traceability.md` when new `BD-*` items, assumptions, or decisions are introduced.

## Minimum fact base

Before writing, establish:

- demand name and one-sentence intent;
- requester or owner if known;
- primary actors or affected groups;
- problem/opportunity;
- expected outcome or value;
- known constraints or deadlines;
- current product/process/business context if relevant;
- whether this is a net-new capability, change, bug, CX improvement, or continuous improvement.

If these are unknown, proceed with labelled assumptions only when they do not materially change direction.

## Workflow

1. Read `qualify.md` and any existing Discovery files.
2. Clarify the demand into a concise idea statement.
3. Separate confirmed facts from assumptions.
4. Define early business design points with `BD-*` IDs.
5. Identify initial users, actors, and impacted operations.
6. Record early options when materially different business, commercial, service, ownership, policy, or operating models are possible.
7. Capture open shaping questions.
8. Decide whether to recommend Shaping, stop, split the demand, or park it.

## Output contract

Use this structure:

```markdown
# Ideation

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: qualify.md
Blocks: none

## Idea summary

## Problem / opportunity

## Intended outcome

## Early business design
| ID | Design point | Rationale | Status | Evidence |
|---|---|---|---|---|
| BD-AREA-001 |  |  | Assumption |  |

## Initial model options
| Option | Description | Pros | Cons / risks | Recommendation |
|---|---|---|---|---|

## Users, actors and stakeholders
| Actor | Need / job | Impact | Notes |
|---|---|---|---|

## Early scope
| In scope | Out of scope | Unknown |
|---|---|---|

## Initial operating impact
| Area | Impact | Owner / team | Risk | Follow-up |
|---|---|---|---|---|

## Assumptions
| ID | Assumption | Why acceptable for now | Validation needed |
|---|---|---|---|

## Open questions for shaping
| ID | Question | Why it matters | Blocks progression? |
|---|---|---|---|

## Ideation recommendation
```

## Review gate

Ideation is not complete unless:

- the idea can be explained without relying on internal shorthand;
- at least one business design point exists or the demand is explicitly too small to need one;
- scope and non-goals are not contradictory;
- assumptions are labelled;
- shaping questions identify the decisions that matter next;
- `qualify.md` names the recommended next mode.

## Handoff

Handoff to Shaping when the idea is valuable enough to explore but still needs model, option, operating, commercial, or design direction. Handoff directly to Requirements only for small, low-risk demands with no material model ambiguity.
