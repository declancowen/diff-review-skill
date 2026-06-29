---
name: notion-demand
description: Orchestrate Recipe Room demand work in the live Notion Product Roadmap and Tasks databases. Use when creating, classifying, shaping, cleaning, reviewing, decomposing, or progressing a demand through Ideation, Shaping, Requirements, UX Design, Process Design, Solution Design, Technical Design, Development, Testing / QA, Launch, or Review. Route to detailed lifecycle mode files, use only valid live Notion properties and options, choose stages on a horses-for-courses basis, keep Discovery on the parent demand, keep later artefacts in linked tasks, and prevent scope leakage between demands and stages.
---

# Notion Demand

Operate Recipe Room's demand lifecycle in Notion. Treat this file as the router and operating contract. Read the selected mode file before producing or changing a demand artefact.

## Required architecture

```text
notion-demand/
  SKILL.md
  modes/
    discovery-ideation.md
    discovery-shaping.md
    design-requirements.md
    design-ux.md
    design-process.md
    design-solution.md
    design-technical.md
    delivery-development.md
    delivery-qa.md
    launch-release-readiness.md
    launch-go-live.md
    review-hypercare.md
    review-outcomes.md
    review-optimisation.md
```

The core routes and governs. Mode files define the detailed questions, evidence, workflow, output contract, review gate, and handoff for their stage.

## Non-negotiable operating contract

- Fetch the live Recipe Room Demand and Tasks schemas before any Notion write. The live schema overrides this skill if it changes.
- Use the Recipe Room workspace, not a legacy workspace or similarly named database.
- Never invent a property, option, lifecycle, stage, status, or demand type.
- Use the user's latest instruction as the primary authority for intent and scope.
- Use only evidence relevant to the current demand. Never use another demand as a source of requirements.
- Keep internal agent, connector, migration, coverage, audit-process, and source-handling language out of product artefacts.
- Apply a horses-for-courses approach. Create only the stages and tasks that materially help the demand.
- Keep each mode inside its responsibility boundary. Route gaps back to the earliest affected mode.
- Preserve useful existing facts. Correct drift without deleting valid context.
- Separate confirmed facts, assumptions, open questions, and blocking decisions.
- Do not update Notion when the user asks only for local drafting or review.
- Act as an expert subject-matter partner, not a passive formatter. Challenge weak demand inputs, identify missing commercial/product/operational/technical thinking, and ask sharp questions when the answer would materially improve the demand.

## Live Recipe Room schema baseline

Always verify this baseline before writing.

### Parent demand

- Data source: `Demand`
- Title: `Demand`
- Writable working properties: `Type`, `Size`, `Stage`, `Lifecycle`, `Owner`, `Status`, `Priority`, `Summary`, `Timeline`, `Dates`, `Tasks`, `Is Blocking`, `Blocked By`
- Valid `Type`: `Feature`, `CX`, `Bug`, `CI`
- Valid `Lifecycle`: `Discovery`, `Design`, `Delivery`, `Launch`, `Review`
- Valid `Stage`: `Ideation`, `Shaping`, `Requirements`, `UX Design`, `Process Design`, `Solution Design`, `Technical Design`, `Development`, `Testing / QA`, `Release Readiness`, `Go-live`, `Hypercare / Support`, `Measure Outcomes`, `Benefits Review`, `Capture Learnings`, `Identify Optimisation Opportunities`, `Optimisation / Enhancement Request`
- Valid `Status`: `Backlog`, `Review`, `Planning`, `In Progress`, `Done`, `Cancelled`, `Paused`
- Demand `Status` is a live Notion status property. Use the exact spelling returned by the live schema. As of the last schema check, the Demand database exposes `Cancelled` with two Ls and does not expose `Archived`.
- Valid `Priority`: `Low`, `Medium`, `High`
- Valid `Size`: `XS`, `S`, `M`, `L`, `XL`, `XXL`

### Child task

- Data source: `Tasks`
- Title: `Task`
- Writable working properties: `Status`, `Lifecycle`, `Stage`, `Priority`, `Workstream`, `Project`, `Parent-task`, `Sub-tasks`, `Assignee`, `Due`, `Completed on`, `Files`, `Media`
- Valid `Workstream`: `Product`, `UX`, `Process`, `Technical`, `Legal`, `Finance`, `Accounting`, `Operations`, `Reporting`, `Compliance`, `Payments`, `Data`, `Admin`
- Link every lifecycle task to its demand through `Project`.
- Put source documents and source HTML in `Files` when upload is available.
- Put extracted screenshots and visual assets in `Media` when upload is available.
- Do not use the page body as file storage when the file properties can be used.
- Use `Lifecycle = Discovery` with `Stage = Ideation` or `Stage = Shaping` for both parent demands and Discovery tasks.

## Demand type rules

| Type | Use when primary intent is |
|---|---|
| `Feature` | Add or materially extend a capability, workflow, or product function. |
| `CX` | Improve an existing user experience, interaction, content, clarity, or journey. |
| `Bug` | Correct behaviour that is broken, incorrect, inconsistent, or regressed. |
| `CI` | Make a bounded continuous improvement that is not best represented as a Feature, CX item, or Bug. |

Choose one parent type from the primary intent. Mixed supporting work does not create extra parent types. Never use `Platform`, `Foundation`, `Platform / Foundation`, or `BAU`; they are not valid Recipe Room options.

## Lifecycle router

Discovery has two stages and two mode files:

- `Lifecycle = Discovery`, `Stage = Ideation`: use for the first high-level articulation of the idea, initial business design, initial product/business model, commercial proposition, high-level business/commercial/model options, early sales/pricing/go-to-market posture, early end-to-end story, initial value, initial scope, early decision history, and early operating-model impact.
- `Lifecycle = Discovery`, `Stage = Shaping`: use to add the meat to the bones: shaped model, proposed option and rationale, commercial strategy definition, sales/pricing/go-to-market direction, commercial cost structure, business scenarios, strategic decisions, design principles, feasibility, substantive operating-model assessment, business capability impact, high-level solution direction, current/open Discovery decisions, and recommended Design focus.

| Lifecycle | Parent/task stage | Read |
|---|---|---|
| Discovery | `Ideation` | [modes/discovery-ideation.md](modes/discovery-ideation.md) |
| Discovery | `Shaping` | [modes/discovery-shaping.md](modes/discovery-shaping.md) |
| Design | `Requirements` | [modes/design-requirements.md](modes/design-requirements.md) |
| Design | `UX Design` | [modes/design-ux.md](modes/design-ux.md) |
| Design | `Process Design` | [modes/design-process.md](modes/design-process.md) |
| Design | `Solution Design` | [modes/design-solution.md](modes/design-solution.md) |
| Design | `Technical Design` | [modes/design-technical.md](modes/design-technical.md) |
| Delivery | `Development` | [modes/delivery-development.md](modes/delivery-development.md) |
| Delivery | `Testing / QA` | [modes/delivery-qa.md](modes/delivery-qa.md) |
| Launch | `Release Readiness` | [modes/launch-release-readiness.md](modes/launch-release-readiness.md) |
| Launch | `Go-live` | [modes/launch-go-live.md](modes/launch-go-live.md) |
| Review | `Hypercare / Support` | [modes/review-hypercare.md](modes/review-hypercare.md) |
| Review | `Measure Outcomes` or `Benefits Review` | [modes/review-outcomes.md](modes/review-outcomes.md) |
| Review | `Capture Learnings`, `Identify Optimisation Opportunities`, or `Optimisation / Enhancement Request` | [modes/review-optimisation.md](modes/review-optimisation.md) |

## Parent and task ownership

- Keep Ideation and Shaping narrative on the parent demand page by default.
- Convert concrete Discovery outcomes into linked child tasks when the parent Ideation/Shaping content implies distinct work, ownership, or deliverables. Example: if Shaping says "we need a go-to-market strategy", create or update a linked Discovery task such as `Define go-to-market strategy` with `Lifecycle = Discovery`, `Stage = Shaping`, and the relevant parent context carried into the task body.
- Create a Discovery task when the user explicitly requests one, a separate owner/deliverable makes it useful, or a shaped business scenario needs actionable follow-through before Design.
- Put Design, Delivery, Launch, and Review artefacts in linked child tasks by default.
- Keep the parent demand's `Lifecycle` and `Stage` aligned to the demand's current overall position. Child tasks may exist across multiple later stages.
- Name tasks by a clear outcome or artefact. Do not prefix standard Technical Design task names with the demand name.

## Operational mode selection

| User asks for... | Use mode |
|---|---|
| Turn a rough idea into a demand | Ideation |
| Explain the idea, initial product/business model, or high-level end-to-end story | Ideation |
| Define the early business design for a demand before detailed shaping | Ideation |
| Clarify or shape the demand | Shaping |
| Build out the operating-model assessment, business scenarios, strategic decisions, or design direction from an idea | Shaping |
| Define behaviours, rules, states, or acceptance criteria | Requirements |
| Define screens, journeys, interaction states, or content | UX Design |
| Define operational ownership, handoffs, exceptions, or support process | Process Design |
| Define system responsibilities, source of truth, data/API concepts, conceptual architecture, detailed end-to-end solution architecture, or cross-cutting solution ownership | Solution Design |
| Create a codebase-aware implementation plan | Technical Design |
| Break approved design into build work | Development |
| Validate delivered work against scenarios and requirements | Testing / QA |
| Decide whether the release can safely launch | Release Readiness |
| Run or document the launch | Go-live |
| Stabilise after launch | Hypercare / Support |
| Measure results or benefits | Measure Outcomes / Benefits Review |
| Capture learnings or identify follow-up improvements | Learnings and Optimisation |

When the user's request spans multiple modes, start with the earliest mode that could materially change downstream work. Do not silently skip unresolved upstream gaps.

## Stage selection and task decomposition: horses for courses

Do not create every lifecycle stage automatically.

Create a stage/task when at least one applies:

- it produces a distinct decision or artefact;
- it has a distinct owner or specialist input;
- it controls material product, operational, technical, legal, data, or release risk;
- it is required to remove ambiguity before a downstream stage;
- it creates a useful review or sign-off boundary.
- it covers a distinct user journey, screen group, system area, workstream, release risk, validation area, or handoff boundary that would be hard to review inside a larger task.

Split tasks when any of these are materially different:

- user or actor;
- surface, journey, screen group, feature area, system area, or operational process;
- lifecycle-stage output or artefact;
- owner, specialist discipline, dependency, risk, review path, sign-off, delivery sequence, or QA approach.

Usually omit or combine a stage when:

- the demand is small and the output would duplicate another artefact;
- the stage has no meaningful decisions, work, or risk;
- the same owner can cover it clearly in one bounded task;
- the output would exist only to complete a template.
- separate tasks would be artificial slices of the same coherent decision, pattern, or artefact.

Record omitted or combined stages and rationale when omission or combination could otherwise be mistaken for an oversight. If a single proposed task contains multiple logical tasks, split it before writing unless the combination is explicitly justified.

## Downstream planning depth

Before creating or expanding Delivery, Launch, or Review tasks, determine the planning depth. If the user has not clearly specified the depth, ask whether they want:

- **Lightweight:** a small set of coordination/checkpoint artefacts that lets developers own the detailed tasking; or
- **Detailed:** a fuller downstream breakdown of Development, QA, Release Readiness, Go-live, Hypercare, Outcomes, and Optimisation tasks.

Default to lightweight only when the user has already asked for lightweight, when detailed tasking would duplicate existing developer-owned planning, or when the demand already has granular build tasks. Do not create a large downstream task set by default. Make it explicit that developers can review, correct, and add their own Delivery/Launch/Review tasks in Notion.

## Mode boundaries

| Mode | Owns | Must not silently own |
|---|---|---|
| Ideation | concept, problem/opportunity, initial business design, initial product/business model, commercial proposition, commercial products/revenue ideas, high-level business/commercial/model options, early sales/pricing/GTM posture, high-level end-to-end story, vision, value, high-level users and scope, early decision history, early operating-model impact | detailed requirements, process maps, solution architecture, or implementation |
| Shaping | shaped product/business model, selected or proposed business/model option and rationale, commercial strategy definition, commercial products, pricing, revenue/fee/royalty/subscription/discount logic, commercial cost structure, sales/GTM direction, strategic decisions, design principles, business scenarios, core operating flow, feasibility, end-to-end scope, substantive operating-model assessment, business capability impact, high-level solution direction, capability fit, design implications, current/open Discovery decisions, design focus | detailed requirements or implementation |
| Requirements | testable behaviour, rules, states, acceptance criteria, prioritised backlog | UI design or technical approach |
| UX Design | UI, screens, flows, interactions, content, visual states, accessibility | requirements, business process, or architecture |
| Process Design | as-is/to-be process, actors, ownership, handoffs, decisions, exceptions | UI design or code design |
| Solution Design | conceptual responsibilities, detailed end-to-end solution architecture, data/service/API concepts, source of truth, integration direction, cross-cutting solution ownership | code-level implementation |
| Technical Design | evidence-backed implementation plan and exactly three technical artefacts | product scope invention or build execution |
| Development | execution plan and build tasks from approved design | new product decisions |
| Testing / QA | scenario validation, regression, quality evidence, blockers | new scope |
| Launch | readiness, rollout, go-live control, support handoff | unresolved design invention |
| Review | live outcomes, benefits, learnings, and follow-up demand | rewriting historical intent |

UX Design is for UI and interaction work. Behavioural rules belong in Requirements; operational flows belong in Process Design; system responsibilities belong in Solution Design.

## Requirement ID namespaces and alignment

Keep product/business requirements and technical requirements in different ID namespaces.

- Requirements Mode uses `BR-[AREA]-###` for business requirements.
- Technical Design Mode uses `TR-[AREA]-###` for technical requirements.
- Technical decisions use `TD-[AREA]-###`.
- Technical tasks use `TT-[AREA]-###`.
- Correctness properties use `CP-[AREA]-###`.

Older Requirements tasks may still contain `REQ-*` IDs. Treat those as legacy business requirement IDs, not technical IDs. Preserve them where downstream traceability already depends on them; use `BR-*` for new or fully rewritten Requirements tasks.

Technical Requirements must map each material `TR-*` back to upstream business requirements (`BR-*` or legacy `REQ-*`) and to relevant UX, Process, and Solution artefacts. If Technical Design discovers a missing product rule, UI state, operational handoff, or solution/source-of-truth decision, route back to the earliest affected mode instead of silently adding product scope inside Technical Requirements.

## Create vs update rules

- If the correct parent or child artefact already exists, update it rather than creating a replacement.
- If no correct artefact exists and the stage is genuinely useful, create it.
- If a duplicate or near-duplicate artefact exists, consolidate only when safe; otherwise ask before merging or replacing.
- Never create a new stage task just because a template exists.
- Never create a replacement artefact only because the current one is imperfect; preserve valid facts and correct drift.
- If an existing artefact is materially wrong, identify the earliest wrong artefact, correct that first, then refresh affected downstream work.

## Codebase context source

Use available local Recipe Room repositories or the current workspace first when codebase context is needed. If local code is unavailable and a GitHub connector is available, inspect the relevant Recipe Room backend and/or frontend repository. Do not force GitHub links into Codex artefacts when the local repo is already available.

Use codebase context when it would materially affect existing product behaviour, affected frontend/backend/admin/data surfaces, technical feasibility, capability reuse, source of truth, implementation dependencies, QA/regression risk, release constraints, or operating-model impact. Do not inspect the repository just to fill a template, and do not turn codebase observations into product requirements unless supported by demand intent or approved upstream artefacts.

Treat repo schemas, models, routes, UI, and admin surfaces as current-state evidence, not automatic target-state decisions. Current implementation may be correct baseline, transitional scaffolding, outdated legacy, partial delivery, or the thing the demand intends to replace. When anchoring design to code, explicitly classify the relationship as one of: net-new capability, lands on existing capability, extends existing capability, changes existing capability, replaces legacy capability, or validates uncertain/transitional capability. Preserve this distinction in Solution and Technical artefacts so Design does not accidentally freeze stale schema or overrule the to-be demand.

## Authority and evidence

Use this authority order:

1. User's latest explicit instruction.
2. Live Recipe Room Notion schema for property names and options.
3. Current parent demand for approved Discovery/Shaping intent.
4. Approved upstream artefacts for downstream work.
5. Relevant source evidence such as files, designs, research, live product behaviour, repository context, or external policy.
6. Mode instructions as operating guardrails.

Classify material statements:

- **Confirmed fact:** directly supported by authoritative evidence.
- **Assumption:** a named working assumption that permits progress.
- **Open question:** unresolved but not currently blocking.
- **Decision needed:** unresolved and blocks progression or materially changes the output.

Do not disguise an assumption as a requirement. Do not make implementation commitments from a blocking unknown.

## Scope isolation

Before using source content, test whether it belongs to the current demand:

- Does it support the same primary outcome?
- Does it affect the same users or actors?
- Is it approved upstream context for this demand?
- Would including it change scope, release timing, ownership, or risk?

Exclude unrelated content even when it shares a screen, service, database, or product area. Never include examples from previous demands in reusable skill output.

## Demand decomposition

Split into separate parent demands when the work has materially different outcomes, users, owners, release timing, dependencies, or independent validation paths.

Keep one parent demand when work supports one coherent outcome and can be designed, delivered, and released together. Use linked tasks to separate stage artefacts and workstreams.

## Orchestration workflow

1. Identify the target demand and the user's requested action.
2. Fetch the live Demand and Tasks schemas before any write.
3. Read the parent demand, its relevant linked tasks, and only directly relevant evidence.
4. Confirm the primary demand type and current lifecycle/stage.
5. Check for duplicate or overlapping demands before creating anything new.
6. Decide which stage or stages are actually useful using the horses-for-courses rules.
7. Decide whether codebase context is needed and inspect the local repo or connector only when it would change the artefact, risk assessment, scope, priority, or next step.
8. Read every selected mode file completely.
9. Establish the minimum fact base required by the selected mode.
10. Produce or update the correct parent or child artefact.
11. Run the selected mode's review gate.
12. Check schema validity, scope isolation, stage boundaries, parent/task ownership, and plain-language quality.
13. State the next useful stage, any intentionally omitted stage, and any blocker.

## Refresh rule

When later work exposes drift:

1. Identify the earliest incorrect or incomplete artefact.
2. Correct or explicitly block that upstream artefact first.
3. Refresh every downstream artefact materially affected by the correction.
4. Leave unaffected downstream work unchanged.

Do not silently patch downstream artefacts while leaving their source of truth wrong.

## Writing standard

- Write clearly, directly, and without generic AI phrasing.
- Start major Discovery sections with short narrative prose about the actual demand, findings, decisions, options, or implications. The parent page should be readable by a person skimming for the point, not only by an agent parsing fields.
- When a parent contains both Ideation and Shaping, include a short cross-Discovery executive summary that states the actual idea, selected direction, major rejected/parked options, commercial posture, and what Design must preserve. Do not explain the Discovery framework.
- Put a short synopsis before substantial tables that summarises the specific content, finding, decision, or implication in that section. Do not write meta-explanations such as "this table covers..." or explain what the lifecycle/framework stage is for.
- Prefer paragraphs for executive summaries, intent, problem/opportunity, business rationale, shaped narrative, and important context.
- Prefer tables for decisions, scope, requirements, responsibilities, scenarios, comparisons, operating-model assessment, traceability, and other structured detail.
- In Discovery, record material business/model options before settling on a preferred direction. Options are not technical architectures; they are business, operating, commercial, service, ownership, funding, policy, route-to-market, or control models that materially change the demand.
- In Shaping, state the selected or proposed option, why it is preferred, and which alternatives were rejected or parked. Keep enough rationale that a later strategy change can understand the decision history.
- For commercial demands, explicitly cover the commercial proposition, commercial products, revenue streams, pricing, fees/commission, royalties/payout economics, subscriptions, discounts, commercial cost structure, sales/adoption route, launch cohort, support implications, and open commercial risks. Do not assume "commercial strategy" is covered because pricing appears elsewhere.
- For payments, payout, marketplace, seller earnings/royalties, subscriptions, verification, or multi-currency demands, explicitly define the cost structure: cost component, estimated amount or TBC marker, charged-by/provider, who bears the economic cost, when it is incurred, how it is previewed or disclosed, how it is recovered or absorbed, ledger/ERP treatment, reporting/audit treatment, currency/FX treatment, and confirmation status. Do not collapse this into a vague "seller eats costs" statement.
- For complex or model-heavy demands, include a business-level operating flow diagram and a Design implications table so Requirements, UX, Process, Solution, and Technical Design can preserve the golden thread.
- For multi-persona or journey-heavy demands, include a high-level customer journey flow in Discovery/Shaping based on the shaped personas and actors. The parent journey should show the main customer/admin/provider roles, trigger, key journey moments, handoffs, decisions, outcomes, and major pain/control points without becoming detailed UI, process, or solution design.
- For complex, cross-cutting, financial, operational, or integration-heavy demands, Solution Design should create or update a detailed `End-to-end solution architecture` task. This is not a lightweight recap. It must describe the full target solution across actors, surfaces, capabilities, source-of-truth records, integrations, controls, reporting, ERP/accounting outputs, state transitions, failures, reconciliation, and traceability to Requirements, UX, Process, Solution, and Technical Design validation.
- End Discovery with current confirmed decisions and open decisions carried forward when the demand has material model, commercial, legal, finance, compliance, data, or technical uncertainty.
- Do not write framework narration into demand pages. Avoid sections that explain what Discovery, Ideation, Shaping, parent lifecycle, or stage properties mean unless the user explicitly asks for process documentation.
- Use Mermaid when a diagram clarifies a journey, process, state, sequence, or architecture.
- Keep Discovery product/business focused.
- Make every task actionable and reviewable.
- Avoid filler, duplicated sections, invented precision, and internal working notes.

## Diagram and FigJam contract

Use diagrams when they materially improve understanding of a journey, process, state model, sequence, capability map, data model, integration boundary, solution architecture, dependency graph, release flow, or operating model.

Mermaid in Notion is the source diagram embedded in the artefact. FigJam is the editable companion view when the user asks for Figma/FigJam output or when the current work explicitly includes diagram creation in Figma.

This section is an internal creation and quality contract. Do not write diagram QA rules, connector mechanics, tool limitations, generation notes, accessibility checks, or modelling-method explanations into the Notion artefact body or the FigJam canvas unless the user explicitly asks for methodology documentation.

Customer journey maps are first-class UX artefacts. Use them when a demand has meaningful user, customer, seller, buyer, admin, support, provider, or finance personas whose experience needs to stay coherent from Discovery into UX Design. The parent Shaping page may include a high-level customer journey flow. UX Design has two journey levels: each UX task should include a task-specific customer journey flow for its own surface, screen group, or interaction scope, and larger/multi-surface demands should also create a canonical `End-to-end customer journey` task, analogous to Process Design's `End-to-end process design` and Solution Design's `End-to-end solution architecture`. A journey map should show the persona lane or actor perspective, journey stage, concrete steps inside each stage, user/admin action performed at each step, touchpoint or surface, visible state or decision, backstage/process/system involvement where relevant, decision or pain point, moment of success, outcome/handoff, and open question/control where relevant.

For larger multi-persona customer journeys, do not force materially different personas into one dense combined map. This applies in both Shaping and UX Design. Keep one customer-journey artefact page for the stage, but split the visual content inside that page into separate persona journey maps when buyer, seller, admin, support, finance, or provider actors have different goals, touchpoints, decisions, states, or controls. Do not create separate Shaping persona pages unless the user explicitly asks for separate page ownership.

For larger multi-persona UX journeys, the canonical `End-to-end customer journey` Notion task should remain one task. It should explain the overall journey, why the personas are split, key cross-persona handoffs, which UX tasks own the detailed surfaces, and then contain separate detailed journey sections for each material persona or actor group. It must not contain a Figma page inventory or FigJam audit table. Do not create separate persona-specific Notion tasks unless the user explicitly asks for separate task ownership. The matching FigJam page should use the stage-prefixed canonical name `UX Design - End-to-end customer journey` and contain separate detailed visual journey maps for each material persona or actor group.

Customer journey map templates are internal skill guidance, not demand artefacts. Do not create a `Template`, `Journey map template`, `UX template`, or example page inside a demand's Figma/FigJam file. Use the template structure below to create each actual journey page, then create only the demand-specific Shaping, UX, admin, support, or task-level journey pages.

Internal customer journey map visual template:

- Header/lens: demand name, lifecycle/stage, journey name, artefact level, persona or actor, scenario, actor goal/job-to-be-done, trigger, start point, end point, scope boundary, source artefacts, confidence/evidence level, and date/update context where useful.
- Visual layout: customer journey maps must read left to right across journey phases/stages. Do not render the primary FigJam journey as a top-down table, single vertical list, or generic card dump. A vertical/table format is acceptable in Notion for traceability, but the FigJam map must be horizontal.
- Stage sections: journey phases are ordered left to right as wide stage sections. Each section should have a stage name, stage goal/context, and the stage-level question the actor is trying to resolve. Use high-level phases for Shaping and more specific phases for UX task journeys.
- Steps inside each stage: each stage section must contain the concrete ordered moments the actor moves through, with the step boxes laid out side-by-side from left to right inside that stage. The number of steps is demand-specific and stage-specific. Do not force a fixed count such as two steps per stage; use one, two, three, or more steps based on the real size and complexity of that stage. Only use one step in a stage when the stage is genuinely a single moment and the artefact makes that obvious.
- Step detail tiles: each step has its own step header box. Under that step header, use separate labelled detail boxes/tiles for step objective, step description, activities/actions performed, touchpoints/channels/surfaces, visible UI/system state or decision, thoughts/questions/mental model, emotional state or confidence/friction level, pain points/control risks, moment of truth or success criteria, KPI/measure, opportunities/design implications, owner/backstage handoff where relevant, evidence/assumptions/open questions, and a bottom `Backend activities` tile. Put `Description` above `Activities` so the reader understands what the step is about before reading the actions. The backend tile should describe the backstage, system, provider, admin, record, event, entitlement, ledger, notification, audit, or support activity that makes the visible step work. If no backend/backstage work is material for that step, write `None / not material`. Do not cram all step detail into one dense card.
- Activities are not the same as the step title. Under each step, write the actual things the user/admin does, such as reviews a recipe card, opens a modal, compares price, accepts terms, waits for verification, retries, contacts support, reviews a balance, exports a line item, or confirms withdrawal.
- Lanes/maps: one map per materially different persona or actor perspective. Use buyer and seller maps first for marketplace/customer journeys. Add admin, support, finance, provider, or backstage/system maps when they materially affect the experience, control, handoff, or visible state. Do not blend different personas into one vague journey.
- Footer/legend: scope boundaries, traceability to Notion task or parent section, key open decisions, and confidence/assumption markers. Keep methodology notes out of the Figma/FigJam artefact unless the user asks for a methodology page.
- Detail level: Shaping journey maps are high-level and business-facing, but still need stages, key steps, activities, touchpoints, major decisions, pain/control points, opportunities, and outcomes per persona. UX end-to-end maps are more detailed and must include screen groups, entry points, staged steps, activities, visible states, decision points, permissions/role differences, emotions/friction, moments of truth, outcomes, and owning UX tasks. Task-specific UX maps are the most detailed around the relevant screen group, UI states, error/success/loading states, permissions, content decisions, recovery paths, and edge cases.
- QA failure conditions: a journey map is too shallow if it has one card per stage, uses only `action/state/success`, omits step description, omits user activities, omits thoughts/questions or emotions/friction, omits pain points and opportunities, lacks touchpoints/surfaces, lacks success criteria or KPI/measure, lacks the bottom `Backend activities` tile, or cannot show what the actor actually does inside a stage. If a FigJam journey ends up with one step per stage, a top-down layout, vertical step stacks where steps should run side-by-side, or summary cards without separate detail tiles under each step, treat it as failed QA and rebuild it.

Treat any Mermaid block in a parent demand or child task as a diagram candidate. The agent must decide whether that Mermaid block should also exist as a FigJam view. Rule of thumb: if the diagram is part of the artefact's meaning and a person would reasonably review it visually, create or update the matching FigJam view when diagram work is in scope.

This applies to parent Discovery content as well as child tasks. For example, Discovery/Shaping `Core operating flow`, `Business capability model`, `High-level solution design`, and other parent/guidance diagrams should follow the same Mermaid-first, FigJam-second workflow when they are meaningful visual artefacts.

Do not limit FigJam promotion to Tasks database pages. If the meaningful diagram lives only inside the parent demand page, create or update a FigJam page for that parent section when FigJam work is in scope. For example, a parent-only `Core operating flow` diagram should become a FigJam page such as `Shaping - Core operating flow` even when there is no separate Notion task for it.

Do not compress a complex diagram into a small high-level sketch just because the canvas or preview is easier to manage. The FigJam view must preserve the artefact's real level of detail. For complex, financial, operational, regulated, integration-heavy, or multi-actor demands, use a larger diagram with clear boundaries, readable labels, and enough nodes, flows, records, providers, events, controls, and handoffs for review. A simplified overview is acceptable only when it is explicitly labelled as an overview and the detailed artefact still exists elsewhere.

If an existing FigJam page is cramped, bunched up, built from an older visual pattern, or too messy to review, rebuild it on a clean wider canvas instead of trying to salvage the old layout node by node. Preserve the artefact content and improve the structure, spacing, routing, and readability.

Every FigJam diagram page must be readable as a standalone artefact:

- place a white or near-white containing canvas/frame behind the full diagram so the diagram is legible against the FigJam dotted background. The containing canvas should read as a proper square/rectangular canvas, not a large pill-shaped card;
- size nodes so all text is visible; do not accept truncated labels or ellipses inside boxes as the final output. Text inside diagram boxes, stage labels, lane labels, and decision gateways should be centred horizontally and vertically unless a specific artefact needs a different alignment;
- preserve the full intended diagram content; do not remove steps, records, actors, decisions, handoffs, providers, controls, exceptions, or data flows merely to make the drawing easier;
- use the connector style appropriate to the artefact. Process diagrams should use elbowed connectors with clean bends; do not use freeform curved connectors for process maps unless the user explicitly asks for that style;
- label connectors where the flow meaning is not obvious. For Process Design diagrams, every connector must have a short flow label that explains the trigger, handoff, decision outcome, event, state change, or data/money/control movement;
- route connector lines cleanly with enough spacing; avoid lines crossing through boxes, overlapping labels, stacking on top of each other, or making the main path hard to follow;
- keep boxes, labels, lane headers, sections, connector labels, and background containers from covering each other; fix z-order and spacing before considering the diagram complete;
- for logical architecture and Solution Design diagrams, use a wide canvas and generous gutters between entry points, platform services, source-of-truth records, and external providers so relationship labels have room to sit between nodes without overlapping boxes or other labels;
- if automatic routing creates messy overlaps, adjust the layout, increase spacing, split the diagram, or use cleaner intermediate waypoints/sections rather than leaving an unreadable diagram;
- prefer larger canvases with clear whitespace over compact diagrams that are difficult to read.
- run a visual QA pass after creating each FigJam page. If the screenshot/preview shows overlapping connectors, hidden text, truncated labels, or boxes covering content, fix the diagram before treating it as complete.

Hard no-overlap QA gate:

- A FigJam page is not complete if any connector/line crosses through a box, lane label, section title, node text, callout, or decision diamond.
- A FigJam page is not complete if any box, lane, section, label, callout, or background container overlaps another content element or hides any part of it.
- A FigJam page is not complete if any visible text is clipped, truncated, ellipsised, too small to read, or covered by another element.
- Background canvases, lane bands, columns, and section containers must sit behind content and must never cover nodes, labels, connectors, or arrowheads.
- Run a QA pass before treating the FigJam view as complete: inspect the rendered page/preview, check for box overlaps, check for connector crossings through content, and fix the layout until the page is readable.
- If the connector tool cannot route a clean line automatically, use a larger layout, move nodes, split the view, or create clearer intermediate routing space. Do not accept an unreadable route as a tooling limitation.

Use the right modelling convention for the artefact instead of forcing every diagram into the same shape:

- Process Design diagrams should use BPMN-style process-flow discipline where practical: visible actor swimlanes, start/end events, task/activity boxes, decision gateways, labelled sequence flows, bounded process areas, exceptions, and cross-lane handoffs. A responsibility matrix, static card layout, or architecture map is not a substitute for a process diagram.
- Solution Design and Shaping `High-level solution design` diagrams should use logical architecture / ArchiMate-style architecture discipline where practical: clear business/application/data/technology/provider/control layers or boundaries; explicit actors, capabilities, business services, application services/components, data objects, technology/integration services, and external providers; and labelled relationships such as triggering, flow, access/read-write, serving, realisation, assignment/responsibility, composition, event publication, import/export, settlement, funding, reconciliation, reporting output, or ERP posting. Use the reusable visual design pattern demonstrated by the canonical end-to-end logical architecture view as the standard for Solution Design architecture pages: left-side entry points/product/admin surfaces, central Recipe Room platform/service boundary, right-side source-of-truth records, and external provider/bank/ERP/reporting/payment systems outside the platform boundary, with labelled data/event/money/control flows. This means reusing the layout pattern, not copying the specific end-to-end diagram content. Scale that pattern to the domain scope; do not switch domain-level Solution Design diagrams into swimlanes, process maps, linear row tables, or simple column traceability diagrams. Use column/traceability layouts only as secondary summaries. Use ArchiMate as a practical viewpoint standard, not as methodology narration. Do not force formal ArchiMate icons if FigJam does not support them; use clear labels, a small legend when helpful, and consistent colours/boundaries.
- In Solution Design logical architecture maps, use rounded-corner rectangles for services, records, providers, controls, actors, and surfaces by default. Do not use cylinder/database shapes unless the user explicitly asks for formal data-store notation.
- Shaping diagrams, except customer journey maps, should use straight connectors by default and rounded-corner boxes. `Core operating flow`, `Business capability model`, `Business capability impact assessment`, and `High-level solution design` are Discovery/Shaping guidance views. They must preserve shaped business/model detail without becoming detailed process maps, implementation diagrams, or row-based traceability templates.
- Technical Design diagrams should use the notation that best proves implementation correctness, such as sequence, state, ERD/data model, dependency, service, rollout, or architecture diagrams.

When creating or updating a diagram-enabled artefact:

- write the diagram in Mermaid in the Notion artefact first, using the mode's output contract;
- create or update the corresponding FigJam diagram view when Figma/FigJam work is in scope;
- use one FigJam file per demand where possible, named after the demand;
- inspect the target Figma/FigJam file before writing. Confirm `editorType`, existing page names, and whether `figma.root.children` exposes `PAGE` nodes and `typeof figma.createPage === "function"`;
- inside the demand's FigJam file, create a separate FigJam page for each diagram when the active workflow/tooling exposes true `PAGE` nodes or `figma.createPage`. Some FigJam boards in this environment expose real pages even though generic FigJam guidance may say otherwise; use the live API capability of the target file, not a stale assumption;
- name each FigJam page with the lifecycle or stage plus the diagram or task name, so the stage is clear at a glance, for example `Process Design - End-to-end process design`, `Solution Design - End-to-end solution architecture`, `Shaping - Business capability model`, `Ideation - Core operating flow`, `UX Design - Buyer purchase and entitlement flow`, or `Technical Design - Source-of-truth data model`;
- for customer journey maps, use the same FigJam file and page convention with explicit journey names. Shaping uses `Shaping - Customer journey map` for the parent high-level customer journey. The canonical UX end-to-end journey uses `UX Design - End-to-end customer journey`. In both cases, keep separate persona maps inside that one page rather than creating separate persona pages, unless the user explicitly asks for separate pages. Task-specific UX journey pages use `UX Design - [journey or UX task name]`, for example `UX Design - Creator onboarding, terms and verification journey`, `UX Design - Paid recipe discovery journey`, or `UX Design - Admin finance, reconciliation, funding and approval journey`;
- if a matching FigJam page already exists, update it instead of creating a duplicate. Match by the full stage-prefixed page name first, then by a clearly equivalent legacy journey name;
- do not apply the FigJam page/view/section naming convention to Notion task titles; Notion task names should remain clean artefact names such as `End-to-end process design` or `End-to-end solution architecture`;
- do not use a diagram generator path for multi-page FigJam work unless it has been verified to place the diagram on the intended FigJam page; if generator placement is not reliable, build the diagram directly on the target FigJam page using the FigJam API/workflow instead of dumping all diagrams onto the first page;
- do not silently use one FigJam page with multiple sections as a substitute when the user has asked for separate FigJam pages. If the active connector/workflow genuinely cannot create true FigJam pages after feature detection, stop before writing diagrams, state the limitation in chat, and ask whether the user wants to create pages manually, use sections as a fallback, or use separate FigJam files;
- do not insert FigJam URLs, embeds, bookmarks, markdown links, preview blocks, or generic FigJam link lists into Notion artefacts as part of this skill. FigJam creation and Notion content authoring are separate outputs;
- if the user needs FigJam placement in Notion, provide the relevant FigJam page names and URLs in chat for manual insertion. Do not write FigJam URLs or preview placeholders into Notion from this skill;
- do not paste restricted, draft-only, claim, private, or agent-session links into Notion artefacts;
- place every supporting document, source link, file reference, or visual reference exactly where it is used in the parent/task content;
- do not dump supporting links, docs, embeds, or previews at the bottom of the page unless the section itself is a deliberate source/reference appendix;
- if one document supports several sections, link it at the most specific repeated points only when useful, or in a clearly named `Source context` table at the top; do not leave orphaned links after the main content;
- before a FigJam view exists, keep the Mermaid diagram visible in the relevant section so the artefact is still reviewable;
- when a FigJam view exists, keep the Mermaid source visible in the relevant Notion section unless the user explicitly asks to hide or collapse it;
- when no FigJam view exists, keep the Mermaid diagram visible in the relevant section unless the user asks otherwise;
- do not export diagram screenshots or extract images for Notion unless the user explicitly asks for static image attachments;
- do not use `Media` for FigJam diagram screenshots by default; FigJam remains the editable external diagram artefact;
- if the FigJam connector cannot create true pages, do not proceed with diagram writing unless the user explicitly approves a fallback; state the limitation in the chat response, not in the product artefact;
- keep the Notion artefact readable without opening FigJam.

Do not create diagrams merely because a template has a diagram slot. Omit or mark `Not applicable` when a diagram would repeat the table/narrative without adding clarity.

Use the following diagram ownership rules:

| Artefact area | Diagram expectation |
|---|---|
| Discovery / Shaping | Business-level operating flow, capability map, high-level conceptual flow when the demand is complex, commercial, financial, regulated, integration-heavy, or multi-actor. |
| Discovery / Shaping customer journey | High-level customer journey flow based on personas/actors when the demand has more than one material persona, journey, role, or end-to-end customer experience to preserve. |
| Requirements | Usually no diagram; use one only for a state model or simple workflow that materially clarifies requirements without replacing Process or Solution Design. |
| UX Design | Task-specific customer journey flow in each UX task; canonical `End-to-end customer journey` task when the demand spans multiple personas, surfaces, or journey phases; user/admin flow or screen-state flow in detailed UX tasks where screens and state transitions need review. |
| Process Design | BPMN-style process flow with bounded process areas and clearly visible actor swimlanes; canonical `End-to-end process design` for cross-cutting demands. |
| Solution Design | ArchiMate-style architecture map, end-to-end solution architecture, integration/data flow, source-of-truth view, financial/ERP flow where relevant. |
| Technical Design | Technical architecture, data model, sequence/state/dependency diagram where needed for implementation planning. |
| Delivery / QA / Launch / Review | Diagram only when a release, validation, incident, hypercare, or outcome flow materially benefits from a visual. |

## Response standard after work

After producing or updating artefacts, respond briefly with:

- the mode or modes used;
- what changed;
- what is blocked or still uncertain;
- the recommended next useful stage;
- any intentionally omitted stage and why.

Keep chat concise. Let the edited Notion artefacts carry the detail.

## Final audit

Before completing work, confirm:

- The live Recipe Room schema was checked.
- Every property and option is valid.
- The correct parent/task stage spelling was used.
- Only useful stages were selected.
- The correct mode files were read and followed.
- Relevant local Recipe Room repo or GitHub context was checked when current product, technical, operating-model, QA, release, or support context was materially relevant.
- Parent and child responsibilities are correct.
- UX contains UI/interaction work only.
- No unrelated demand examples or scope leaked in.
- Facts, assumptions, questions, and decisions are distinguishable.
- Each artefact passes its mode review gate and has a clear handoff.
