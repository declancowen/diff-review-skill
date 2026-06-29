# Design — Requirements Mode

Use this mode when creating or updating a linked child task with `Lifecycle = Design` and `Stage = Requirements`.

Requirements Mode translates the shaped demand into clear, testable product and business requirements. It is the main bridge between Discovery/Shaping and downstream UX, Process, Solution, Technical Design, Delivery, and QA.

## Purpose

Requirements Mode defines what must be true, without prematurely deciding how it will be implemented.

It should define:

- functional behaviours;
- business rules;
- financial/cost rules where the demand has payments, subscriptions, fees, payout, verification, tax, FX, or provider-cost implications;
- user/admin/system roles;
- eligibility and permissions;
- states and transitions;
- data/content needs;
- edge cases and failure states;
- acceptance criteria;
- prioritised requirement backlog;
- traceability back to business scenarios;
- analytics/measurement requirements where relevant.

Requirements are not UI design, process design, solution architecture, or implementation tasks.

## Required requirements shape

A Requirements task must define the requirement as a complete business/product requirement, not just a context note plus acceptance criteria. Use the sections below unless the demand is so small that a section is explicitly marked `Not applicable`.

| Component | What it answers | Notes |
|---|---|---|
| Requirement title | What is this about? | Use a clear outcome or behaviour name. |
| Business objective | Why are we doing this? | Tie to parent Discovery/Shaping value, risk, or operating-model impact. |
| Scope | What is included and excluded? | Include in-scope and out-of-scope boundaries for this specific task. |
| User story | Who needs what, and why? | Use only when it clarifies actor intent; avoid generic filler. |
| Functional requirements | What must the system do? | Use stable `BR-[AREA]-###` business requirement IDs and normative language. |
| Business rules | What rules control the behaviour? | Include policy, eligibility, state, permission, and exception rules. |
| Financial / cost rules | What costs, fees, deductions, reserves, FX treatment, provider fees, cost recoveries, or absorbed costs apply? | Include amount or TBC marker, who bears the cost, when it is incurred, disclosure/preview needs, ledger/ERP treatment, reporting/audit needs, and confirmation status. |
| Acceptance criteria | How do we know it works? | Use Given/When/Then or equivalent testable criteria. |
| Data requirements | What data is captured, stored, shown, or validated? | Include content, labels, statuses, metadata, audit fields, and reporting fields where relevant. |
| Validation rules | What makes the data or action acceptable? | Include required fields, formats, limits, allowed states, and blocked conditions. |
| Process / workflow | What are the steps or states? | Keep business workflow here; detailed ownership/handoffs move to Process Design when material. |
| User roles / permissions | Who can do what? | Include customer/user/admin/system/provider distinctions where relevant. |
| Non-functional requirements | How well must it work? | Include performance, accessibility, security, privacy, reliability, auditability, supportability where relevant. |
| Error handling | What happens when something goes wrong? | Cover blocked, denied, invalid, duplicate, expired, external failure, and unavailable states. |
| Dependencies | What does this rely on? | Include upstream decisions, providers, services, policies, data, designs, or repo capabilities. |
| Assumptions | What are we assuming to be true? | Label assumptions; do not disguise them as requirements. |
| Out of scope | What are we not solving here? | Repeat the local task boundary even if the parent has wider exclusions. |
| Reporting / audit needs | What needs to be tracked? | Include events, metrics, audit trail, moderation/history, and operational reporting needs. |
| Design / UX notes | Any interface expectations? | Keep to product-facing expectations and handoff notes; detailed UI belongs in UX Design. |

Do not omit a component just because the source note did not mention it. If the component matters and evidence is missing, add an Open Question or Decision Needed.

## Notion mapping

Create or update a **linked child task**.

Task properties:

| Task field | Expected value |
|---|---|
| `Task` | Descriptive, outcome-focused requirements task name. |
| `Lifecycle` | `Design`. |
| `Stage` | `Requirements`. |
| `Status` | Use a valid live task status. |
| `Priority` | Align to parent demand unless there is a clear reason to differ. |
| `Project` | Relation to parent demand. |

Do not write full requirements onto the parent demand unless the demand is tiny and the user explicitly wants a lightweight parent-only treatment.

## Diagram and FigJam handling

Follow the core skill's Diagram and FigJam contract.

Requirements usually do not need a FigJam view. Use a small Mermaid diagram only when a state model, decision flow, or simple workflow materially clarifies the requirement without replacing UX, Process, or Solution Design. When FigJam work is in scope and the requirements diagram is useful for review, create/update a matching FigJam view. Do not insert FigJam URLs, embeds, bookmarks, markdown links, preview blocks, or generic FigJam link lists into the Requirements task as part of this mode. Do not export static images by default.

If a Requirements diagram is created, it must preserve the requirement's real states, decisions, rules, edge cases and acceptance-critical paths. Do not simplify away rules or failure states to make the diagram easier to draw. Use a white containing canvas, readable full labels and clean connector routing. The hard no-overlap QA gate applies: no line may cross through a box/text/label, no box or background may cover another element, and no text may be clipped or ellipsised. Run visual QA and fix the layout before treating the FigJam view as complete.

## Inputs to use

Use:

- parent Discovery/Shaping content;
- business scenarios;
- user-provided notes/files/screenshots;
- existing Requirements task if refining;
- relevant policy/product context;
- directly relevant UX/Process/Solution only when aligning or correcting existing work.

Do not use Development, QA, Launch, or Review tasks as source-of-truth.

## Minimum fact base

Before finalising requirements, identify:

1. Parent demand and current scope.
2. Target users/actors.
3. Affected objects, records, or surfaces.
4. Business scenarios from Shaping.
5. In-scope and out-of-scope boundaries.
6. Business/policy rules.
7. Permissions and state rules.
8. Data/content required to support behaviour.
9. Known edge cases or failure states.
10. Analytics/measurement needs where relevant.

If this fact base is weak, write a draft requirements task with Open Questions or Decision Needed. Do not present the requirements as final.

## Requirement ID convention

Use stable business requirement IDs for anything material.

Recommended format:

```text
BR-[AREA]-001
BR-[AREA]-002
```

Example: `BR-[AREA]-001`

`BR` means Business Requirement. These are the canonical product/business requirements for the demand.

Do not use `TR-*` in Requirements Mode. `TR-*` belongs to Technical Design Mode.

If an older Requirements task already uses `REQ-*`, preserve it if downstream traceability already depends on it. When creating new Requirements tasks, or fully rewriting a task before downstream traceability exists, use `BR-*`. Do not renumber existing IDs unless the task is being fully rewritten and traceability is not yet in use.

## Requirement types to consider

| Type | What to capture |
|---|---|
| Functional | What the user/admin/system must be able to do. |
| Eligibility | Who can perform the action and under what conditions. |
| Permissions | Owner/viewer/admin/public/private access rules. |
| State | Relevant lifecycle, visibility, permission, eligibility, or completion states. |
| Content/data | Required fields, statuses, labels, reasons, files, copy, metadata. |
| Policy | Trust/safety, reporting, verification, appeals, privacy, eligibility. |
| Edge cases | Deleted content, unavailable actions, missing data, duplicate action, blocked user, revoked access. |
| Failure states | Error, blocked, denied, validation failure, expired state, external failure. |
| Analytics | Events, metrics, outcomes, success measures. |
| Financial / cost | Store fees, commissions, subscription fees, verification/IDV costs, payout/KYC costs, withdrawal fees, FX/conversion costs, bank/intermediary fees, reserves, thresholds, fee previews, deductions, cost recovery, absorbed costs, ERP records, and reporting/audit requirements. |
| Non-functional | Performance, accessibility, security, reliability, auditability, supportability where relevant. |

## EARS and acceptance criteria

Use EARS where it improves clarity:

```text
WHEN [condition/event], THE SYSTEM SHALL [expected behaviour].
```

Use Given/When/Then for acceptance criteria where easier to test:

```text
Given [context]
When [action]
Then [expected result]
```

Good requirements are normative and testable. Avoid vague verbs like `support`, `improve`, or `handle` unless the acceptance criteria make them measurable.

## Requirements workflow

1. Read parent Discovery/Shaping.
2. Identify scenarios and actors.
3. Extract required behaviours.
4. Group requirements by capability/surface/journey.
5. Write requirement IDs.
6. Define business rules.
7. Define financial/cost rules where material: cost component, amount/TBC marker, provider, economic owner, timing, disclosure/preview, recovery or absorption, ledger/ERP treatment, reporting/audit and confirmation status.
8. Define permissions and state rules.
9. Define data/content needs.
10. Define edge cases and failure states.
11. Add acceptance criteria.
12. Add analytics/measurement needs.
13. Mark assumptions and open questions.
14. Review against parent scope and business scenarios.
15. State readiness for UX, Process, Solution, and Technical Design.

## Output contract

Write this structure in the child task body.

```markdown
# Requirements

## Source context
| Source | Used for |
|---|---|
| Parent demand | ... |
| Business scenarios | ... |
| File / screenshot / note | ... |

## Requirements summary
...

## Business objective
...

## Scope
| In scope | Out of scope |
|---|---|
| ... | ... |

## Users / actors
| Actor | Role in this demand |
|---|---|
| ... | ... |

## User story
As a ..., I want ..., so that ...

## Requirement groups
| Group | Purpose |
|---|---|
| ... | ... |

## Functional requirements
| Ref | Requirement | Scenario / rationale | Validation |
|---|---|---|---|
| BR-... | WHEN ..., THE SYSTEM SHALL ... | ... | ... |

## Business rules
| Rule | Applies to | Notes |
|---|---|---|
| ... | ... | ... |

## Financial / cost rules
| Cost / fee / deduction | Amount or basis | Economic owner | Timing | System behaviour | Ledger / reporting treatment | Status |
|---|---|---|---|---|---|---|
| ... | ... | Creator / Recipe Room / buyer / shared / TBC | ... | ... | ... | Confirmed / Assumption / TBC |

## User roles / permissions and state rules
| Role/state | Allowed | Blocked | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

## Data / content requirements
| Data/content | Required for | Notes |
|---|---|---|
| ... | ... | ... |

## Validation rules
| Rule | Applies to | Expected behaviour |
|---|---|---|
| ... | ... | ... |

## Process / workflow
| Step/state | Actor/system | Expected outcome |
|---|---|---|
| ... | ... | ... |

## Non-functional requirements
| Requirement | Applies to | Target / constraint |
|---|---|---|
| ... | ... | ... |

## Edge cases and failure states
| Case | Expected behaviour | Requirement ref |
|---|---|---|
| ... | ... | ... |

## Error handling
| Error / exception | User/system response | Requirement ref |
|---|---|---|
| ... | ... | ... |

## Dependencies
| Dependency | Why it matters | Status |
|---|---|---|
| ... | ... | Confirmed / Assumption / Decision needed |

## Analytics / measurement
| Event / measure | Purpose | Notes |
|---|---|---|
| ... | ... | ... |

## Reporting / audit needs
| Need | Required detail | Notes |
|---|---|---|
| ... | ... | ... |

## Design / UX notes
- ...

## Assumptions
- ...

## Open questions / decisions needed
- ...

## Readiness for downstream design
| Next mode | Ready? | Notes |
|---|---|---|
| UX Design | Yes/No | ... |
| Process Design | Yes/No | ... |
| Solution Design | Yes/No | ... |
| Technical Design | Yes/No | ... |
```

## Review gate

Before marking requirements ready:

- Does every requirement tie back to shaped scope or a scenario?
- Are actors and affected objects clear?
- Are permissions and states covered?
- Are financial/cost rules explicit where the demand has payments, subscriptions, fees, payout, verification, tax, FX, or provider-cost implications?
- Are failure states and edge cases covered?
- Are assumptions and decisions separated?
- Is there enough detail for UX and Solution Design?
- Is there enough detail for Technical Design to avoid guessing?
- Has unrelated scope been removed?
- Are acceptance criteria testable?

## Handoff

Requirements can hand off to:

- UX Design when screens/flows/states are needed.
- Process Design when ownership, handoffs, or operational flow matters.
- Solution Design when data/source-of-truth/system responsibility needs definition.
- Technical Design when enough product/design context exists for codebase-aware planning.
- QA later, as the baseline for validation.

## Guardrails

Do not:

- design UI layouts;
- define backend implementation details;
- create development tasks;
- skip edge cases;
- add scope not present in parent/Shaping;
- allow UX or Technical Design to silently become the source of truth for missing requirements.
