# Discovery — Ideation Mode

Use this mode when a demand is new, rough, exploratory, or currently in `Lifecycle = Discovery` and `Stage = Ideation`.

Ideation is not requirements, UX, solution design, or build planning. It is the first structured pass that decides whether an idea is worth shaping.

Ideation must also define the early **business design** for the demand. That means explaining how the idea should work as a business, product, service, commercial, operating, governance, or capability concept before later modes turn it into detailed requirements, process, UX, solution, or technical design.

## Purpose

Ideation Mode turns a rough idea into a clear early demand concept.

It should answer:

- What is the executive summary of the idea, in plain language?
- What is the idea in plain English?
- What is the initial business design related to the demand?
- What is the product/business model at a concept level?
- What is the commercial proposition: what is being offered, to whom, why they would pay, and why Recipe Room should offer it?
- What are the early commercial products, revenue streams, pricing ideas, fees, commission, royalties, discounts, cost ownership, or monetisation options?
- What is the early sales, adoption, route-to-market, or go-to-market posture, if the demand changes how Recipe Room sells, launches, positions, supports, or operates a commercial offer?
- What high-level business, operating, commercial, service, ownership, funding, policy, or route-to-market options are available?
- How would the idea work end to end for the main actors?
- What problem or opportunity might it address?
- Who is affected?
- Why might it matter now?
- What value could it create?
- What strategic decisions or design principles appear to be implied?
- What material decision history should be preserved so Shaping can see which options were considered, rejected, parked, or carried forward?
- What is the likely demand type?
- What is the high-level scope and not-scope?
- What might this mean for the operating model?
- What needs to be investigated in Shaping?

## Codebase context source

Use local Recipe Room repository context lightly when it helps identify current product surfaces, existing capabilities, likely technical area, or operating-model clues for the idea.

Do not turn Ideation into technical design. Treat codebase findings as context for the problem, opportunity, scope, assumptions, and shaping questions.

## Notion mapping

Write Ideation output to the **parent demand page**.

Update parent fields where appropriate:

| Parent field | Expected use |
|---|---|
| `Demand` | Clear demand name, short and specific. |
| `Type` | `Feature`, `CX`, `Bug`, or `CI` based on primary intent. |
| `Status` | Usually Backlog or Planning. Use In Progress only if actively being shaped. |
| `Lifecycle` | `Discovery`. |
| `Stage` | `Ideation`. |
| `Priority` | Recommend Low/Medium/High from impact and urgency. |
| `Size` | Initial valid live size estimate. Mark as provisional where uncertain. |
| `Timeline` | Set a date or date range only when supported by evidence. |
| `Summary` | 1-3 plain-language sentences. |

Keep Ideation content on the parent demand page. Create linked Discovery tasks only when the user explicitly asks for separate task tracking or when there is a concrete follow-up outcome that needs separate ownership before Shaping. Do not move Ideation sections into grouped child pages by default.

## Diagram accessibility and readability

When Ideation includes a meaningful diagram such as an option model, early operating story, actor/value flow, or commercial model sketch, follow the core Diagram and FigJam contract.

Do not simplify away material options, actors, value movements, commercial logic, or decisions to make the diagram easier to draw. Make the diagram readable by using a white containing canvas, larger spacing, readable full labels, clean line routing, and separate FigJam pages where needed. The hard no-overlap QA gate applies: no line may cross through a box/text/label, no box or background may cover another element, and no text may be clipped or ellipsised. Run a visual QA pass and fix the layout before treating the diagram as complete.

## Minimum fact base

Before writing, gather enough context to avoid creating a vague demand:

1. Identify the idea or user request in plain English.
2. Identify the initial business design: value proposition, actor roles, operating concept, commercial/economic logic, policy/control needs, capability impact, and success lens.
3. Identify the initial product/business model: what is being created, sold, changed, enabled, restricted, automated, or improved.
4. Identify the initial commercial proposition and strategy for commercial demands: commercial products, customer/seller/admin proposition, revenue streams, pricing, subscription or one-time models, commission/retained revenue, royalty or payout economics, discounts, cost/fee ownership, sales/adoption route, route-to-market, launch posture, support implications, and commercial open decisions.
5. Identify material high-level solution or model options. These are not technical architectures; they are business/model choices such as reseller vs agent, free vs paid, self-serve vs reviewed, subscription vs one-time fee, internal operation vs partner-led, manual control vs automation, or different funding/settlement models.
6. Identify the basic end-to-end concept: who starts, what happens, who receives value, and what outcome is produced.
7. Identify the affected user group, even if provisional.
8. Identify the affected product, service, experience, operational, commercial, governance, data, or technical area.
9. Identify whether the primary intent is a Feature, CX improvement, Bug, or CI item.
10. Identify what is known, assumed, and unknown.
11. Identify whether this may overlap with an existing demand.

If the fact base is too weak to explain the idea or initial model, keep the demand in Ideation, write a short ideation stub, and mark the missing model questions. Do not invent detailed scope.

## Idea, model, and business design articulation

Ideation must make the idea understandable before later modes define requirements or architecture. Do not skip the basic concept because downstream artefacts already contain detail.

For each material idea, explain:

| Area | Ideation prompt |
|---|---|
| Core idea | What are we trying to create, change, or enable? |
| Business design | How should the business work around the demand at a concept level: value proposition, actors, ownership, incentives, controls, operating responsibilities, policy boundaries, and capability changes? |
| Product/business model | How does the idea work commercially, operationally, or as a product/service concept? Who gives what, who gets what, and what is exchanged or changed? |
| Commercial proposition | What is being offered, to whom, why it matters, why someone would pay or adopt it, and how Recipe Room benefits? |
| Commercial products and strategy | What products, tiers, prices, fees, commissions, subscriptions, royalties, discounts, cost ownership, packaging or monetisation paths are in play? |
| Go-to-market posture | How might this be launched, positioned, phased, sold, adopted, trialled, discounted, or rolled out? Which channels, cohorts, timing or commercial constraints matter? |
| High-level solution options | Which materially different business/model paths could solve the demand? Examples include own-name sale vs marketplace, one-time fee vs subscription, free vs paid, self-serve vs reviewed, partner-led vs internal, model 1 vs model 2 funding, or manual vs automated controls. |
| Actor journey | What is the simple end-to-end story from the main actor's trigger to outcome? |
| Key model choices | What model choices appear material, such as own-name sale vs marketplace, free vs paid, self-serve vs reviewed, automated vs manual, internal vs partner-led? |
| Design principles | What principles should guide shaping, such as trust, simplicity, transparency, compliance, seller control, buyer protection, auditability, or low operational overhead? |
| Model uncertainty | What parts of the model are assumptions, open questions, or decisions needed? |

Keep this conceptual. Do not write detailed requirements, UI flows, solution architecture, or implementation tasks in Ideation.

## Business design lens

Use this lens to define the demand as a business change, not just a product idea. Capture the early direction and the questions Shaping must resolve.

| Area | Ideation question |
|---|---|
| Strategic intent | Why should Recipe Room do this, and how does it support the product/company direction? |
| Value proposition | What value is created for customers, sellers, admins, operators, partners, or Recipe Room? |
| Business model | What is sold, licensed, enabled, restricted, automated, subsidised, charged for, discounted, paid out, or governed? |
| Actors and roles | Who participates, who owns the relationship, who approves, who pays, who receives value, who bears cost/risk, and who supports exceptions? |
| Commercial / economic logic | What revenue, cost, fee, discount, royalty, risk, compliance, or operating economics may matter? |
| Commercial proposition | What is the offer and why is it attractive to the buyer, seller, admin/operator, partner, or Recipe Room? |
| Commercial products | What paid products, plan tiers, access products, subscriptions, licences, add-ons, discounts, promotions, commissions, royalties, fees or payout economics may exist? |
| Sales / adoption / go-to-market | What sales motion, adoption route, launch path, cohort, commercial positioning, migration/transition, discount posture, enablement, or support implication may matter? |
| Product / service boundaries | What is the service promise, what is included, what is deliberately excluded, and what needs clear customer-facing language? |
| Controls and policy | What eligibility, verification, trust, safety, legal, accounting, support, audit, reporting, or governance controls may be needed? |
| Capability and operating impact | What capability is created, extended, changed, replaced, or retired across product, process, people, technology, data, finance, legal, and operations? |
| Success lens | What early outcome or measure would show the demand is worth shaping further? |

Keep the business design at concept level. Detailed business rules belong in Requirements; detailed process ownership belongs in Process Design; detailed system responsibility belongs in Solution Design; implementation belongs in Technical Design.

## Narrative and table use

Ideation must be readable before it becomes structured. Start with a short executive summary that explains the actual idea, why it matters, how the business concept works, the main early options, and what Shaping needs to resolve.

Every substantial table should have a short demand-specific synopsis before it. Use the synopsis to summarise the actual finding, decision, option set, or implication; use the table to organise detail. Do not write meta lead-ins such as "this table captures..." or explain what the framework section is for.

Use paragraphs for:

- executive summary;
- plain-English idea;
- problem/opportunity;
- desired outcome;
- short recommendation.

Use tables for:

- idea charter;
- initial model;
- business design components;
- high-level solution/model option comparison;
- end-to-end story;
- strategic decisions and design principles;
- early decision history;
- early scope;
- operating-model impact;
- assumptions, open questions, and task candidates when structure improves readability.

## Operating model impact lens

Use this lens to understand how the idea may change the Recipe Room operating model. This is not a lightweight filler table and not a request to create a generic "business engine" artefact. The point is to guide Shaping: what might change, who is affected, which capabilities are reused or changed, and where deeper Design work may be needed.

In Ideation, consider each area and capture only the material impacts, uncertainties, or shaping questions. Omit areas only when they are genuinely not relevant.

| Area | Ideation question |
|---|---|
| Policy | What rules, governance, trust/safety, privacy, verification, eligibility, reporting, moderation, commercial, or content policies may be affected? |
| People | Which users, customers, admins, operators, support roles, reviewers, or decision owners may be affected? Who benefits, acts, approves, or is accountable? |
| Process | Which user, admin, support, operational, commercial, or governance process may change? Is there an as-is process to understand before design? |
| Technology | Which app, backend, admin, data, integration, analytics, infrastructure, or tooling areas may be touched? Is this likely to land on existing technology or require something new? |
| Organisation | Does this change ownership, support model, escalation, review, governance, handoff, operating rhythm, or cross-team responsibility? |
| Value | What user, operational, revenue, trust, quality, risk, efficiency, or learning value might the change create? |
| Capability | Which existing capability might be reused, extended, changed, replaced, or retired? What new capability might be needed? |

Use Strategy, goals/objectives, customer/user, product/service, and commercial/GTM context where relevant, but do not let those replace the operating-model impact assessment above.

## Ideation workflow

1. Restate the idea in simple terms.
2. Write a concise executive summary for the demand.
3. Define the early business design in plain English.
4. Explain the initial product/business model.
5. Define the early commercial proposition and commercial strategy where material.
6. Define the early sales, adoption, pricing, and go-to-market posture where material.
7. Compare material high-level solution/model options and tradeoffs.
8. Record early decision history: options considered, current direction, rejected/parked options, and what must be carried into Shaping.
9. Sketch the simple end-to-end actor journey.
10. Identify material strategic decisions and design principles.
11. Identify the likely demand type.
12. Identify the primary user/persona affected.
13. Write the problem or opportunity.
14. Write the desired outcome.
15. Define high-level scope and out of scope.
16. Capture initial operating-model impact.
17. Capture initial value/benefit hypothesis.
18. Identify assumptions.
19. Identify open questions for Shaping.
20. Recommend whether to shape, split, merge, park, or reject.

## Output contract

Use this structure on the parent demand page.

```markdown
## About this project
[Short explanation of what the demand is.]

## Discovery

### Ideation executive summary
[2-4 short paragraphs explaining the actual idea, why it matters, the initial business design, the main options under consideration, and what Shaping needs to resolve. Do not explain the Discovery framework or repeat every table row.]

### Idea charter
[Briefly summarise the actual idea charter: the proposed demand, affected users, business model, expected value, initial priority, and initial size.]

| Area | Direction |
|---|---|
| Idea | ... |
| Initial business design | ... |
| Product / business model | ... |
| Demand type | ... |
| Primary users | ... |
| Product area | ... |
| Expected value | ... |
| Initial size | ... |
| Initial priority | ... |

### Initial model
[Briefly summarise the actual initial model: what changes, who acts, who receives value, what is exchanged or controlled, and which model uncertainties remain.]

| Area | Early direction |
|---|---|
| What changes | ... |
| How it works | ... |
| Who acts | ... |
| Who receives value | ... |
| What is exchanged / controlled | ... |
| Key model choices | ... |
| Model uncertainty | ... |

### Initial business design
[Briefly summarise the actual business design: strategic intent, value proposition, actor roles, commercial logic, controls, capability impact, and success lens.]

| Area | Early direction |
|---|---|
| Strategic intent | ... |
| Value proposition | ... |
| Business model | ... |
| Actors and roles | ... |
| Commercial / economic logic | ... |
| Product / service boundaries | ... |
| Controls and policy | ... |
| Capability and operating impact | ... |
| Success lens | ... |

### Initial commercial proposition and strategy
[Briefly summarise the actual commercial proposition and early commercial strategy. Explain what is being offered, who it is for, how Recipe Room may make money, what the main commercial products are, what prices/fees/commission/royalties/subscriptions/discounts are in play, how costs are borne, and what GTM or launch posture needs shaping.]

| Area | Early direction |
|---|---|
| Commercial proposition | ... |
| Commercial products | ... |
| Revenue streams | ... |
| Pricing / fees / commission | ... |
| Royalty / payout economics | ... |
| Subscription / discount logic | ... |
| Cost ownership | ... |
| Go-to-market / launch posture | ... |
| Sales / adoption posture | ... |
| Support / enablement implications | ... |
| Commercial risks / open decisions | ... |

### Initial sales, pricing and go-to-market posture
[Briefly summarise the actual early sales/adoption direction: who the initial audience or cohort is, how they may discover or adopt the offer, how pricing and packaging may work, how the launch may be phased, what support or enablement is implied, and which commercial unknowns Shaping must resolve.]

| Area | Early direction |
|---|---|
| Target segment / cohort | ... |
| Sales / adoption route | ... |
| Pricing posture | ... |
| Packaging / plan posture | ... |
| Launch / rollout posture | ... |
| Support / enablement implications | ... |
| GTM risks / open questions | ... |

### High-level solution options
[Briefly summarise the actual business/model options being considered and the early direction for each. For commercial demands, include the commercial strategy choices: pricing, revenue model, fees/commission, royalty or payout economics, subscriptions, discounts, launch posture, route-to-market, and commercial risks. These are business/model options, not technical architectures.]

| Option | What it means | Pros / why consider it | Cons / risks | Initial view |
|---|---|---|---|---|
| ... | ... | ... | ... | Explore / reject / carry into Shaping |

### Early decision history
[Briefly summarise the actual material decisions already made or emerging from Ideation, including why rejected or parked options are not the current path. This preserves context for later strategy changes without treating early choices as final implementation commitments.]

| Decision area | Options considered | Current direction | Why | Carry into Shaping |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### Initial end-to-end story
[Briefly summarise the actual end-to-end story from trigger to outcome across the main actors.]

| Step | Actor | What happens | Notes / uncertainty |
|---|---|---|---|
| 1 | ... | ... | ... |

### Strategic decisions and design principles
[Briefly summarise the actual early model choices and design principles that should guide Shaping.]

| Item | Direction / principle | Why it matters |
|---|---|---|
| ... | ... | ... |

### Problem / opportunity
...

### Desired outcome
...

### Early scope
[Briefly summarise the actual early scope boundary: what belongs in the demand and what is deliberately excluded for now.]

| In scope | Out of scope for now |
|---|---|
| ... | ... |

### Initial operating model impact
[Briefly summarise the actual early operating-model impacts and the shaping questions they create.]

| Area | Early impact / shaping question |
|---|---|
| Policy | ... |
| People | ... |
| Process | ... |
| Technology | ... |
| Organisation | ... |
| Value | ... |
| Capability | ... |

### Assumptions
- ...

### Open questions for shaping
- ...

### Discovery task candidates
[Briefly summarise the actual candidate follow-up work only where separate ownership, decisioning, or investigation would help Shaping.]

| Candidate task | Why it is useful | Stage |
|---|---|---|
| ... | ... | Ideation / Shaping |

### Ideation recommendation
Shape / split / merge / park / reject, with short rationale.

```

Use the operating-model rows that matter. Omit rows that are genuinely not relevant rather than filling with generic text. If an area is uncertain but likely material, write the uncertainty as a shaping question.

## Review gate

Before marking Ideation ready for Shaping, check:

- Is there an executive summary that makes the idea understandable before the tables?
- Is the idea understandable in plain English?
- Is the initial business design clear enough to guide Shaping?
- Is the initial product/business model explained well enough that Shaping is not guessing?
- Is the commercial proposition clear where the demand has a commercial, monetisation, pricing, subscription, fee, royalty, discount, sales, launch, or GTM dimension?
- Are commercial products, revenue streams, pricing/fee/commission/royalty/subscription/discount logic, cost ownership, sales/adoption route, support implications, and go-to-market questions captured at the right level?
- Are material high-level business/model options compared before the demand locks into one path?
- Is material early decision history preserved, including rejected or parked options where it would help Shaping?
- Is the simple end-to-end actor story clear?
- Is the idea understandable in one minute?
- Is the problem/opportunity clear?
- Is the target user or actor named?
- Is the likely demand type reasonable?
- Is the high-level value clear?
- Are material strategic decisions or design principles captured?
- Is the initial operating-model impact clear enough to shape?
- Are assumptions separated from facts?
- Are open questions specific enough for Shaping?
- Is unrelated demand scope removed?

If the answer is no, keep the demand in Ideation and add the missing questions.

## Handoff to Shaping

Ideation can move to Shaping when:

- the idea is worth progressing;
- the primary problem/opportunity is clear enough;
- the affected product/customer/admin area is known;
- the next questions are about feasibility, end-to-end scope, scenarios, value, capability, or operating model.

## Guardrails

Do not:

- create technical specs;
- create detailed UX flows;
- create build tasks;
- create all lifecycle tasks;
- write internal tool/process language into the parent;
- force a weak idea into a full demand;
- use later-stage tasks as evidence of what the idea should have been.
