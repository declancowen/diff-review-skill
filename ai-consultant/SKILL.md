---
name: ai-consultant
description: Run end-to-end demand consulting work in local Markdown. Use when creating, shaping, decomposing, designing, planning, delivering, QA testing, releasing, or reviewing a demand through Discovery, Design, Deliver, and Review. Create and maintain an `AI consultant/<demand-name>/` folder with stage folders, Markdown artefacts, a root `qualify.md` control plan, `quality-gates.md`, traceability from business design and business requirements to technical requirements, delivery slices, QA evidence, release decisions, review outcomes, architecture standards, slice/final diff reviews, optional repo audits, optional Graphify codebase maps, and optional Fallow static-analysis evidence. Route to detailed lifecycle mode files and update completion status in the relevant Markdown files.
---

# AI Consultant

Operate a local-file demand lifecycle for product, business, CX, process, technical, delivery, QA, launch, and review work. Treat this file as the router and operating contract. Read every selected mode file before creating or updating artefacts.

This skill is Markdown-first. It must not write to external systems or create external design artefacts unless the user explicitly asks for that outside this skill's normal workflow.

## Required architecture

```text
ai-consultant/
  SKILL.md
  scripts/
    scaffold_demand.py
  modes/
    discovery-ideation.md
    discovery-shaping.md
    design-requirements.md
    design-ui-cx-journeys.md
    design-process.md
    design-solution.md
    design-technical.md
    deliver-planning.md
    deliver-development.md
    deliver-qa-testing.md
    deliver-release.md
    review-hypercare.md
    review-outcomes.md
    review-optimisation.md
```

The core routes and governs. Mode files define the questions, evidence, workflow, output contract, review gate, and handoff for each stage.

## Demand workspace

Create or update demand artefacts under this structure by default:

```text
AI consultant/
  <demand-slug>/
    qualify.md
    quality-gates.md
    traceability.md
    01-discovery/
      ideation.md
      shaping.md
    02-design/
      requirements.md
      ui-cx-journeys.md
      process-design.md
      solution-design.md
      technical-design/
        technical-requirements.md
        technical-design.md
        technical-tasks.md
    03-deliver/
      delivery-plan.md
      build-slices.md
      qa-testing.md
      release.md
    04-review/
      hypercare-support.md
      outcomes-benefits.md
      learnings-optimisation.md
```

Use `scripts/scaffold_demand.py` to create the folder structure when starting a new demand:

```bash
python3 path/to/ai-consultant/scripts/scaffold_demand.py "Demand name"
```

If the user gives a different destination, create the same structure there. If the folder already exists, update existing files rather than replacing them.

The scaffold may create placeholder files for all lifecycle modes so the workspace has predictable navigation. Treat `Not started` files as stubs, not selected work. Populate, deepen, and mark active only the modes that are useful for the demand or explicitly requested by the user.

## Non-negotiable operating contract

- Use the user's latest instruction as the primary authority for intent and scope.
- Work locally in Markdown files. Do not update task trackers, design tools, or external systems unless the user explicitly asks outside this skill's normal workflow.
- Use the integrated quality gates as part of the workflow, not as an afterthought. When a backing skill is unavailable, record it in `quality-gates.md`, apply the closest local reasoning directly, and continue unless that absence makes the work unsafe.
- Use only evidence relevant to the current demand. Never import another demand's requirements as source truth.
- Keep internal agent, connector, migration, coverage, audit-process, and source-handling language out of demand artefacts.
- Apply a horses-for-courses approach. Populate and deepen only the modes and artefacts that materially help the demand, unless the user explicitly asks to run the whole lifecycle.
- Keep each mode inside its responsibility boundary. Route gaps back to the earliest affected mode.
- Preserve useful existing facts. Correct drift without deleting valid context.
- Separate confirmed facts, assumptions, open questions, and blocking decisions.
- Act as an expert subject-matter partner, not a passive formatter. Challenge weak inputs and identify missing commercial, product, operational, CX, technical, QA, release, and review thinking.
- Mark work as `Done` only when the relevant artefact has evidence, acceptance criteria, traceability, and no unresolved blocking decision.

## Lifecycle router

The parent lifecycle has four stage folders:

| Lifecycle | Files | Read |
|---|---|---|
| Discovery | `01-discovery/ideation.md` | [modes/discovery-ideation.md](modes/discovery-ideation.md) |
| Discovery | `01-discovery/shaping.md` | [modes/discovery-shaping.md](modes/discovery-shaping.md) |
| Design | `02-design/requirements.md` | [modes/design-requirements.md](modes/design-requirements.md) |
| Design | `02-design/ui-cx-journeys.md` | [modes/design-ui-cx-journeys.md](modes/design-ui-cx-journeys.md) |
| Design | `02-design/process-design.md` | [modes/design-process.md](modes/design-process.md) |
| Design | `02-design/solution-design.md` | [modes/design-solution.md](modes/design-solution.md) |
| Design | `02-design/technical-design/technical-requirements.md`, `technical-design.md`, `technical-tasks.md` | [modes/design-technical.md](modes/design-technical.md) |
| Deliver | `03-deliver/delivery-plan.md` | [modes/deliver-planning.md](modes/deliver-planning.md) |
| Deliver | `03-deliver/build-slices.md` | [modes/deliver-development.md](modes/deliver-development.md) |
| Deliver | `03-deliver/qa-testing.md` | [modes/deliver-qa-testing.md](modes/deliver-qa-testing.md) |
| Deliver | `03-deliver/release.md` | [modes/deliver-release.md](modes/deliver-release.md) |
| Review | `04-review/hypercare-support.md` | [modes/review-hypercare.md](modes/review-hypercare.md) |
| Review | `04-review/outcomes-benefits.md` | [modes/review-outcomes.md](modes/review-outcomes.md) |
| Review | `04-review/learnings-optimisation.md` | [modes/review-optimisation.md](modes/review-optimisation.md) |

Discovery:
- Ideation: first articulation of the idea, early business design, problem/opportunity, initial commercial/product model, scope, early actors, and open shaping questions.
- Shaping: shaped model, option and rationale, commercial strategy, business scenarios, operating model, capability impact, high-level customer journey, design principles, and design focus.

Design:
- Requirements: testable business requirements, rules, states, acceptance criteria, priority, and requirement status.
- UI/CX journeys: customer journeys, screens, interactions, content, accessibility, state handling, and CX acceptance criteria.
- Process design: operational ownership, handoffs, exceptions, support process, controls, and process evidence.
- Solution design: conceptual responsibilities, source of truth, data/API concepts, end-to-end solution architecture, controls, and system boundaries.
- Technical design: split into technical requirements, technical design, and technical tasks because the content is often large.

Deliver:
- Delivery planning: translate approved design into an execution plan, slices, sequencing, dependencies, quality gates, and done criteria.
- Development: track build slices and implementation tasks back to technical tasks and business requirements.
- QA/testing: validate delivered work against requirements, technical design, acceptance criteria, customer journeys, and process scenarios.
- Release: readiness, go-live, rollback, support handoff, and immediate post-release verification.

Review:
- Hypercare/support: live stability, issues, operational readiness, and exit criteria.
- Outcomes/benefits: actual results against intended outcomes, adoption, quality, operational impact, and evidence gaps.
- Learnings/optimisation: learnings, follow-up opportunities, new demand candidates, and closure recommendation.

## Operational mode selection

| User asks for... | Use mode |
|---|---|
| Turn a rough idea into a demand | Ideation |
| Explain the idea, initial product/business model, or early business design | Ideation |
| Clarify or shape the demand | Shaping |
| Build business scenarios, operating model, commercial strategy, or design direction | Shaping |
| Define behaviours, rules, states, acceptance criteria, or prioritised backlog | Requirements |
| Define screens, CX journeys, customer journeys, interactions, content, accessibility, or visual states | UI/CX Journeys |
| Define operational ownership, handoffs, exceptions, controls, support, or back-office process | Process Design |
| Define system responsibilities, source of truth, data/API concepts, conceptual architecture, or end-to-end solution architecture | Solution Design |
| Create codebase-aware technical requirements, technical design, or technical tasks | Technical Design |
| Build the run plan, slices, sequence, dependencies, and done criteria | Delivery Planning |
| Track or plan build execution | Development |
| Validate delivered work against requirements and design | QA/Testing |
| Decide whether the release can safely launch or document go-live | Release |
| Stabilise after launch | Hypercare / Support |
| Measure results or benefits | Outcomes / Benefits |
| Capture learnings or identify follow-up improvements | Learnings / Optimisation |

When a request spans multiple modes, start with the earliest mode that could materially change downstream work. Do not silently skip unresolved upstream gaps.

## Status and completion model

Every demand file must include this front matter block near the top:

```markdown
Status: Not started | In progress | Blocked | Ready for review | Done
Owner: [name or TBC]
Last updated: YYYY-MM-DD
Source artefacts: [files used]
Blocks: [none or blocking decision IDs]
```

Use checkboxes for concrete work items:

```markdown
- [ ] BR-AREA-001 - Requirement summary
- [x] TR-AREA-001 - Technical requirement summary
- [ ] TT-AREA-001 - Build task summary
- [ ] TC-AREA-001 - Test case summary
```

Mark a checkbox complete only when:

- the artefact states what was done;
- the evidence or source file is linked;
- the traceability back to upstream requirements is present;
- acceptance or review criteria are satisfied;
- no blocking decision remains for that item.

Use `Blocked` rather than `Done` when a required upstream decision, source, design, test result, release condition, or review metric is missing.

## Root control files

### `qualify.md`

`qualify.md` is the demand control plan. It tells the next agent what to do, what is done, what remains, and where truth lives.

Always keep it current with:

- demand name, slug, short summary, type, priority, lifecycle position, and current status;
- latest user instruction and date;
- selected lifecycle modes and intentionally omitted modes with rationale;
- current plan of work across Discovery, Design, Deliver, and Review;
- stage checklist with file paths and status;
- open decisions, blockers, and assumptions;
- completion rules for this demand;
- next recommended action.

### `traceability.md`

`traceability.md` is the cross-lifecycle map. It prevents delivery and QA from drifting away from business design and technical requirements.

Always keep it current with:

- business design points from Ideation/Shaping;
- business requirements (`BR-*`);
- UX/CX journey references (`UX-*` or journey section names);
- process requirements or controls (`PR-*` when useful);
- solution design decisions (`SD-*`);
- technical requirements (`TR-*`);
- technical tasks (`TT-*`);
- delivery slices (`DS-*`);
- test cases (`TC-*`);
- defects, failed validations, and live issues (`DF-*`);
- release checks (`RC-*`);
- review metrics or benefits (`RM-*`);
- current status and evidence links.

### `quality-gates.md`

`quality-gates.md` is the lifecycle quality ledger. Keep it current whenever a demand uses codebase evidence, technical design, delivery slices, QA, release, or review.

Always track:

- backing skill/workflow availability and whether each gate is required, used, skipped, blocked, or not applicable;
- Architecture Standards checkpoints and decisions;
- Graphify graph creation/update status when codebase context is in scope;
- per-slice diff-review status and final branch-total diff-review status;
- Fallow run state, findings, exceptions, and evidence when the repository is TypeScript/JavaScript or Fallow is already configured;
- repo-audit status for material or broad codebase changes;
- unresolved findings, accepted residual risks, and next quality action.

Use this status vocabulary: `Not applicable`, `Available`, `Unavailable`, `Required`, `In progress`, `Blocked`, `Clean`, `Findings open`, `Accepted residual risk`.

## Integrated quality gates

AI Consultant remains the active orchestration skill. The gates below are skill-backed workflows to load, read, and apply inside the current AI Consultant lifecycle when they are available and applicable. Availability does not make every gate mandatory for every prompt; applicability depends on whether the demand touches architecture, codebase evidence, implementation, or release risk. If a gate is skipped, record why in `quality-gates.md`.

At the start of every AI Consultant invocation, update or confirm the quality-gate applicability matrix. For `$graphify`, if codebase context is in scope and the graph exists, apply its update workflow; if no graph exists, create the first graph when install/runtime approval allows it. If codebase context is not in scope, record Graphify as `Not applicable` rather than applying it.

When a gate is applicable and the backing skill is available, load/read that skill's own `SKILL.md` and required references, then execute its workflow inside the current AI Consultant run. Do not ask the user to invoke the dependent skill separately and do not hand off unless the user explicitly redirects. Do not reduce `$diff-review`, `$fallow`, or `$repo-audit` to a shell command or a short checklist. Their review/audit ledgers are source evidence and must be linked from `quality-gates.md`.

| Gate | Use when | Timing | Output / evidence |
|---|---|---|---|
| `$architecture-standards` | Any Solution Design, Technical Design, delivery slice, implementation decision, boundary, source-of-truth, public contract, persistence, async workflow, auth/tenancy, shared abstraction, operability, cost, or maintainability concern. | Throughout Solution Design, Technical Design, Delivery Planning, Development, QA, Release, and any remediation loop. | Architecture decisions, boundary ownership, implementation placement, enforcement/tests, residual risks. |
| `$graphify` | Codebase understanding would materially affect solution, technical design, delivery slicing, QA risk, or review. | At the start of each codebase-aware demand consultation. Apply full graph creation on first use, then update the graph on later consultations when the graph exists. | `graphify-out/GRAPH_REPORT.md`, `graphify-out/graph.html`, `graphify-out/graph.json`, plus key god nodes / surprising connections captured in `quality-gates.md`. |
| `$diff-review` | A delivery slice changed code, config, schemas, tests, scripts, generated artefacts, or repo policy. | End of every implemented delivery slice and again at the final end after Fallow/repo-audit/remediation. Loop fixes and re-review until clean, blocked, or residual risk is explicitly accepted. | `.reviews/*`, findings, verification evidence, final all-clear or remaining risk. |
| `$fallow` | The repository is TypeScript/JavaScript, Fallow is installed/configured, static analysis affects confidence, or the user asked for Fallow. | Near the end after implementation and focused tests, before final repo-audit/diff-review closure. Repeat after meaningful remediation that could change dead code, duplication, health, boundaries, or analyzer policy. | `.audits/fallow.md` or concise Fallow assessment, command evidence, accepted exceptions, remaining findings. |
| `$repo-audit` | Material or broad codebase changes, architecture remediation, cross-cutting changes, high-risk release, messy current state, or the user wants whole-repo confidence beyond the diff. | Final end once delivery slices and slice diff reviews are clean; repeat after remediation until clean, blocked, or residual risk is explicitly accepted. | `.audits/*`, current-state findings, transition slices, clean conclusion or remaining risk. |

### Diff-review execution contract

Treat the loaded `$diff-review` workflow as the authoritative branch/change validation gate for code-changing slices.

- Apply after each implemented `DS-*` slice that changes code, config, schemas, tests, generated files, scripts, dependencies, feature gates, analyzer policy, or repo structure.
- Apply again at the final end after Fallow, repo-audit, and remediation.
- Use `.reviews/{content-area}.md` as the persistent review ledger. Link the relevant review file and turn in `quality-gates.md`.
- A slice or final branch state is not `Clean` unless `$diff-review`'s all-clear gate is satisfied: current branch state reviewed, changed files and connected paths traced as needed, relevant verification run or explicitly scoped, no open Critical/High findings, and residual uncertainty is minor or accepted.
- If findings exist, mark the gate `Findings open`, create or update remediation work in the relevant Delivery files, fix through the owning boundary, and repeat the `$diff-review` workflow.
- For every fix/re-review loop, require branch-interaction proof: the latest patch must not reopen prior findings, weaken branch-wide assumptions, or invalidate earlier architecture decisions.
- Do not mark Release `Done` while required slice or final diff-review has open Critical/High findings.

### Fallow execution contract

Treat the loaded `$fallow` workflow as a static-analysis signal gate when the repository is TypeScript/JavaScript, Fallow is installed/configured, analyzer evidence affects confidence, or the user explicitly asks for it.

- First classify run state: first adoption, configured-without-history, rerun-with-history, CI/audit-only, or remediation pass.
- Prefer local package scripts or package-manager execution. Use `npx --yes fallow` only when Fallow is not locally available and normal network/tool approval allows it.
- Keep Fallow modes distinct: changed-file gate, production gate, full advisory inventory, semantic duplication, health/hotspot, baseline, and CI policy are different evidence. Do not collapse one clean result into broad repo cleanliness.
- Preserve JSON evidence where possible and record commands, run state, config state, findings, exceptions, verification, and residual risk in `.audits/fallow.md` or a concise assessment if repo-audit is unavailable.
- Load/read and apply `$architecture-standards` when Fallow findings affect ownership, boundaries, public API, shared abstractions, runtime entry points, data/API contracts, health thresholds, or duplication remediation.
- If Fallow reports findings, group them by owner/root cause, remediate through delivery slices when code changes are needed, repeat focused Fallow checks, then repeat the baseline signal set before calling the Fallow gate clean.
- If Fallow is unavailable but applicable, record `Blocked` or `Accepted residual risk` in `quality-gates.md`; do not silently skip it.

### Repo-audit execution contract

Treat the loaded `$repo-audit` workflow as the final whole-repo confidence gate when the work is material, broad, architecture-sensitive, high-risk, or beyond the confidence of diff review alone.

- Apply after slice diff reviews are clean and after applicable Fallow evidence is collected, unless the audit itself is being used to diagnose current state before remediation.
- Use `.audits/{scope}.md` as the persistent audit ledger. Link the audit file and turn in `quality-gates.md`.
- A repo-audit gate is not `Clean` unless `$repo-audit`'s clean conclusion gates are satisfied for the stated scope: repo-total current state reassessed, high-risk areas traced, relevant verification run or scoped, static-analysis/Fallow evidence considered when available, and no open Critical/High findings remain.
- If repo-audit finds issues, create remediation `DS-*` slices, load/read and apply `$architecture-standards` for target boundaries and ownership, implement/fix, apply slice `$diff-review`, then repeat the `$repo-audit` workflow before final closure.
- Keep repo-audit and diff-review coupled: repo-audit proves current-state and whole-repo risk; diff-review proves the branch changes and remediation are safe. Final release needs both where both are applicable.

### Quality gate sequence for code-changing demands

1. Load/read and apply `$architecture-standards` during Solution Design and Technical Design to choose target boundaries, owners, contracts, source-of-truth decisions, and enforcement.
2. If codebase context is in scope and `$graphify` is available, create or update the graph before finalizing technical design or delivery slices. If graph creation would require installing the package, install only when normal tool/network approval allows it; otherwise record `Blocked` or `Unavailable`.
3. During Delivery Planning, include quality gates in each `DS-*` slice: architecture checkpoint, implementation verification, QA tests, slice diff review, and evidence.
4. At the end of each implemented `DS-*` slice, apply the `$diff-review` workflow against the slice/branch state. Fix findings, update artefacts, and repeat diff review until it is clean, blocked, or a residual risk is explicitly accepted by the user.
5. After all slices are implemented and QA is ready, apply the `$fallow` workflow when applicable. Fix or document findings by loading/reading and applying `$architecture-standards` for boundary/ownership decisions.
6. Apply the `$repo-audit` workflow for material or broad codebase changes after Fallow and slice reviews are clean. If repo-audit finds issues, create remediation slices, load/read and apply `$architecture-standards`, then repeat slice `$diff-review`.
7. Apply final branch-total `$diff-review` after Fallow, repo-audit, and any remediation. Do not mark release or delivery `Done` while Critical/High findings remain open.

For non-code or early-stage demand consultation, still record quality gates as `Not applicable` or `Deferred` in `quality-gates.md` when the user expects later delivery. Do not run Fallow, repo-audit, diff-review, or Graphify just to fill a template.

## ID namespaces

Use separate namespaces. Do not reuse one ID for multiple meanings.

| Prefix | Meaning |
|---|---|
| `BD-*` | Business design point or model decision |
| `BR-*` | Business requirement |
| `UX-*` | UI/CX journey, screen, flow, or experience requirement |
| `PR-*` | Process requirement, control, handoff, or operating rule |
| `SD-*` | Solution design decision, source-of-truth point, or architecture responsibility |
| `TR-*` | Technical requirement |
| `TD-*` | Technical decision |
| `TT-*` | Technical task |
| `DS-*` | Delivery slice |
| `TC-*` | Test case |
| `DF-*` | Defect, failed validation, or unresolved QA issue |
| `RC-*` | Release check |
| `RM-*` | Review metric, outcome, or benefit measure |

Technical requirements must map each material `TR-*` back to upstream `BR-*` and relevant `UX-*`, `PR-*`, or `SD-*` items. QA test cases must map back to `BR-*`, `TR-*`, delivery slices, and acceptance criteria.

## Stage selection and decomposition

Do not create every lifecycle artefact automatically unless the user asks to run the full lifecycle.

Create or deepen a mode when at least one applies:

- it produces a distinct decision or artefact;
- it controls material product, business, operational, technical, legal, data, QA, release, or support risk;
- it is required to remove ambiguity before a downstream stage;
- it creates a useful review or sign-off boundary;
- it covers a distinct customer journey, screen group, system area, workstream, validation area, release risk, or handoff boundary.

Usually omit or combine a mode when:

- the demand is small and the output would duplicate another artefact;
- the mode has no meaningful decisions, work, or risk;
- the same owner can cover the work clearly in one bounded file;
- the output would exist only to complete a template.

Record omitted or combined modes in `qualify.md` when omission could be mistaken for an oversight.

## Mode boundaries

| Mode | Owns | Must not silently own |
|---|---|---|
| Ideation | concept, opportunity, early business design, high-level model, value, early scope, open shaping questions | detailed requirements, process, solution, or implementation |
| Shaping | selected business/model option, scenarios, commercial strategy, operating model, design principles, high-level journey, design focus | detailed requirements or implementation |
| Requirements | testable behaviours, rules, states, acceptance criteria, priority, requirement status | UI design or technical approach |
| UI/CX Journeys | customer journeys, screens, interactions, content, accessibility, visible states | product rules, operating process, or architecture |
| Process Design | as-is/to-be process, actors, ownership, handoffs, exceptions, controls, support | UI design or code design |
| Solution Design | conceptual architecture, source of truth, system responsibilities, data/API concepts, controls, solution traceability | code-level implementation |
| Technical Design | technical requirements, design, tasks, evidence-backed implementation plan | new product scope or build execution |
| Delivery Planning | execution plan, slices, sequencing, dependencies, done criteria | new product decisions |
| Development | build progress, implementation status, evidence, task completion | new design invention |
| QA/Testing | scenario validation, regression, quality evidence, defects, blockers | new scope |
| Release | readiness, go-live, rollback, support handoff, immediate verification | unresolved design invention |
| Review | live outcomes, benefits, learnings, optimisation candidates | rewriting historical intent |

## Codebase context source

Use the current workspace or relevant local repositories first when codebase context is needed. If local code is unavailable and a connector is available, inspect the relevant repository only when it would materially affect existing behaviour, frontend/backend/admin/data surfaces, feasibility, reuse, source of truth, implementation dependencies, QA risk, release constraints, or support impact.

Treat current code as evidence, not automatic target-state truth. Classify the relationship as one of: net-new capability, lands on existing capability, extends existing capability, changes existing capability, replaces legacy capability, or validates uncertain/transitional capability.

## Authority and evidence

Use this authority order:

1. User's latest explicit instruction.
2. Existing files in the current `AI consultant/<demand-slug>/` folder.
3. Approved upstream artefacts in the same demand folder.
4. Relevant source evidence such as repository context, product behaviour, research, policy, metrics, screenshots, logs, or support feedback.
5. Mode instructions as operating guardrails.

Classify material statements:

- **Confirmed fact:** directly supported by evidence.
- **Assumption:** a named working assumption that permits progress.
- **Open question:** unresolved but not currently blocking.
- **Decision needed:** unresolved and blocks progression or materially changes the output.

Do not disguise an assumption as a requirement. Do not make implementation commitments from a blocking unknown.

## Orchestration workflow

1. Identify the target demand and requested action.
2. Locate or create `AI consultant/<demand-slug>/` and update `qualify.md`.
3. Read `qualify.md`, `quality-gates.md`, `traceability.md`, and relevant upstream stage files.
4. Confirm the current lifecycle position and selected modes.
5. Decide which stage or stages are useful using the horses-for-courses rules.
6. Decide whether codebase or evidence inspection is needed, and update the quality-gate applicability matrix.
7. Read every selected mode file completely.
8. Establish the minimum fact base required by each selected mode.
9. Produce or update the correct Markdown artefacts.
10. Update `traceability.md` with new or changed IDs and status.
11. Update `quality-gates.md` with applicable architecture, Graphify, diff-review, Fallow, and repo-audit status.
12. Update `qualify.md` with status, blockers, omitted modes, and next action.
13. Run each selected mode's review gate and every applicable integrated quality gate.
14. State what changed, what remains blocked, and the recommended next useful mode.

## Refresh rule

When later work exposes drift:

1. Identify the earliest incorrect or incomplete artefact.
2. Correct or explicitly block that upstream artefact first.
3. Refresh every downstream artefact materially affected by the correction.
4. Leave unaffected downstream work unchanged.

Do not silently patch downstream files while leaving their source of truth wrong.

## Writing standard

- Write clearly, directly, and without generic AI phrasing.
- Put the actual demand content first; avoid framework narration.
- Prefer paragraphs for executive summaries, intent, rationale, shaped narrative, and important context.
- Prefer tables for decisions, requirements, responsibilities, scenarios, traceability, risks, tests, and delivery status.
- Use Mermaid in Markdown when a diagram clarifies a journey, process, state, sequence, dependency, or architecture. Keep diagram output in local Markdown unless the user explicitly asks for another format.
- Make every artefact actionable and reviewable.
- Avoid filler, duplicated sections, invented precision, and internal working notes.
- Use `TBC` for unknown values rather than making them up.

## Response standard after work

After producing or updating artefacts, respond briefly with:

- the mode or modes used;
- files created or changed;
- quality gates run, skipped, blocked, or left not applicable;
- what is blocked or still uncertain;
- the recommended next useful mode;
- any intentionally omitted mode and why.

Let the edited Markdown files carry the detail.

## Final audit

Before completing work, confirm:

- the correct demand folder was used;
- relevant mode files were read and followed;
- `qualify.md` reflects the latest status and next action;
- `quality-gates.md` records backing skill/workflow availability, applicability, evidence, skipped gates, and open quality risks;
- `traceability.md` links business design, business requirements, technical requirements, delivery slices, QA, release, and review where applicable;
- only useful stages were selected, or full lifecycle execution was explicitly requested;
- architecture-standards was used where architectural decisions or implementation boundaries mattered, or unavailability was recorded;
- graphify was created/updated when codebase context materially affected decisions, or unavailability/not-applicable status was recorded;
- slice and final diff reviews were run for code-changing delivery, looped until clean/blocked/accepted risk, or marked not applicable;
- Fallow was run for applicable TypeScript/JavaScript/static-analysis contexts, or skipped with rationale;
- repo-audit was run for material/broad codebase changes, or skipped with rationale;
- no external-system assumptions leaked into the artefacts;
- facts, assumptions, questions, and decisions are distinguishable;
- each updated artefact has status, evidence, completion criteria, and a clear handoff.
