# Design - UI/CX Journeys Mode

Use this mode for user experience, customer journeys, UI flows, interaction states, screen content, accessibility, and visible behaviour. Keep the output in local Markdown with optional Mermaid diagrams only.

## Purpose

Define how users, customers, admins, support, finance, providers, or other actors experience the demand from trigger to outcome. Preserve the golden thread from business design and requirements into journeys, surfaces, states, and acceptance criteria.

## File

Write to `02-design/ui-cx-journeys.md`. Update `traceability.md` with `UX-*` items mapped to `BR-*`, `BD-*`, and later `TC-*`.

## Minimum fact base

Use:

- Shaping high-level customer journey;
- `BR-*` requirements;
- current screens or product behaviour if relevant;
- personas, actors, roles, permissions, and journey triggers;
- constraints such as accessibility, content, policy, legal, or support needs.

## Workflow

1. Read Discovery and Requirements outputs.
2. Decide whether the demand needs an end-to-end customer journey, task-specific journeys, screen/state design, or all three.
3. Split materially different personas into separate journey sections within the same file.
4. Define journey phases, steps, touchpoints, visible states, decisions, backstage involvement, pain/control points, and outcomes.
5. Define screen inventory, interaction rules, content/labelling notes, empty/loading/error/success states, permissions, and accessibility requirements.
6. Add UX acceptance criteria.
7. Update `traceability.md`.

## Output contract

Use this structure:

```markdown
# UI / CX Journeys

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: 01-discovery/shaping.md, 02-design/requirements.md
Blocks: none

## UX objective

## Personas and journey goals
| Persona / actor | Goal | Trigger | Success outcome | Related BRs |
|---|---|---|---|---|

## End-to-end customer journey
| UX ID | Phase | Actor action | Touchpoint / surface | Visible state / decision | Backstage activity | Pain or control point | Outcome | Related BRs |
|---|---|---|---|---|---|---|---|---|
| UX-AREA-001 |  |  |  |  |  |  |  | BR-AREA-001 |

## Persona-specific journeys
### [Persona / actor] journey
| Step | Objective | Action | State | Content need | Error / recovery | Moment of truth |
|---|---|---|---|---|---|---|

## Surface / screen inventory
| UX ID | Surface / screen | Purpose | Entry point | States | Related BRs | Status |
|---|---|---|---|---|---|---|

## User flows

```mermaid
flowchart LR
  A[Start] --> B[Step]
```

## Interaction rules
| UX ID | Rule | Applies to | Related BRs | Status |
|---|---|---|---|---|

## Content and labelling notes
| Surface | Content / label | Rationale | Open question |
|---|---|---|---|

## Accessibility notes
| Area | Requirement | Validation |
|---|---|---|

## UX acceptance criteria
| UX ID | Criteria | Related BRs | Test handoff |
|---|---|---|---|

## Open questions / decisions needed

## Handoff notes
```

## Review gate

UI/CX is not ready unless:

- material personas or actor groups have clear journey coverage;
- each journey shows concrete actor action, touchpoint, visible state, backstage involvement where relevant, and outcome;
- screen states cover loading, empty, error, permission, success, and edge cases where relevant;
- UX items map to `BR-*`;
- accessibility and content decisions are not left implicit;
- unresolved product rules are routed back to Requirements instead of hidden in UX wording.
