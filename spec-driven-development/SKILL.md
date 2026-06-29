---
name: spec-driven-development
description: Use this skill when a user wants a codebase-grounded spec package for a feature, refactor, migration, integration, platform change, audit remediation, architecture transition, or system enhancement authored under `.spec/<scope>/` as separate `design.md`, `requirements.md`, and `tasks.md` files. It forces repository discovery first, applies architecture standards during design, compares related code and existing patterns, incorporates audit/static-analysis evidence when relevant, derives traceable requirements from explicit design decisions, derives executable tasks from those requirements with validation, compatibility, rollout, and risk controls, and requires iterative review loops before and after deliverables, implementation slices, test creation, and slice-level diff reviews.
---

# Spec-Driven Development

Use this skill to create or update implementation-ready spec packages for planned software changes.

Default output:

```text
.spec/
  _shared/
    repo-profile.md            # optional but strongly recommended
  <scope>/
    design.md
    requirements.md
    tasks.md
    reviews.md                  # required when implementing from the spec
```

This skill is for spec authoring, not implementation, unless the user explicitly asks for both.

## Companion skills

### Mandatory architecture skill

Always apply `architecture-standards` throughout the spec and implementation lifecycle: discovery, design, requirements, tasks, implementation review, test review, and drift review.

- Use it proportionally for lower-risk changes.
- Use it rigorously for cross-module, data, contract, security, platform, or operational changes.
- Treat it as the architectural quality bar for boundaries, dependency direction, tradeoffs, and cross-cutting concerns.
- Embed the architecture-standard lens inside every slice and every material change decision, then still run the end-of-slice and end-of-plan architecture audits. Do not treat architecture standards as only a final checklist.
- Use it as a lens for every artifact and code decision, while still allowing the implementing agent to choose a justified repo-specific path when the literal recommendation does not fit.
- For audit-driven refactors or messy-repo transitions, use its current-state diagnosis, target-state design, refactor-design, and static-analyzer-policy references before finalizing design decisions.
- When Fallow is installed/configured or Fallow evidence is part of the work, also use the `fallow` skill references `analysis-primitives.md` and `quality-benchmarks.md` to preserve mode semantics and negative all-clear behavior.

### Preferred diff review skill

When implementing from a spec, prefer using `diff-review` after each requirement slice and again at final total-diff review.

- A requirement slice is the smallest coherent set of leaf tasks that completes one requirement or a tightly coupled requirement cluster. A slice may be one task such as `2.1`, or a small sequence such as `2.1` and `2.2` when separating them would create false confidence.
- Do not batch unrelated requirement families just to reduce review overhead.
- For each slice, run a deep diff review first, scoped to the slice diff, original user request, linked `DES-*`, linked `REQ-*`, current tests, and `architecture-standards`.
- Each slice review must check the slice against the accumulated branch diff, prior resolved findings, and branch-wide architecture assumptions, not only the latest patch.
- If findings appear, fix them, then run normal diff-review passes with `architecture-standards` until the slice is clean.
- After all slices are complete, run a final deep diff review across the total branch/worktree diff against the original plan, the full spec package, live repo evidence, tests, and `architecture-standards`; fix findings and repeat normal diff reviews until clean.
- Store slice and final review records in `.spec/<scope>/reviews.md`. If `diff-review` also creates `.reviews/*` records, summarize or cross-reference them from `.spec/<scope>/reviews.md` so the spec folder remains the implementation review ledger.
- If `diff-review` is unavailable, run an equivalent manual diff review using the same scope and record that fallback, the review criteria, findings, fixes, validation, and residual risk in `.spec/<scope>/reviews.md`.

#### Task-file review loop requirement

When implementation is in scope, `tasks.md` must explicitly encode the deep-first review loop before code work starts. Each implementation slice must say that it will:

- run a deep `diff-review` first with `architecture-standards`;
- fix deep-review findings before moving to the next slice;
- run normal `diff-review` passes until the slice is clean;
- record validation, findings, fixes, architecture decisions, spec drift decisions, requirement audit, and residual risk in `.spec/<scope>/reviews.md`.

The final task must explicitly require a total-diff deep review, normal clean-loop re-reviews, final prompt/requirements audit, and any requested publish step such as commit, push, and PR creation with the requested target branch and draft state. Do not call a spec implementation-ready if `tasks.md` only says "review" or "run diff review" without spelling out this loop.

## Repo-specific overlay

If the target repository contains a shared profile, read it before authoring:

- `<repo_root>/.spec/_shared/repo-profile.md`
- `<repo_root>/.spec/_shared/house-patterns.md`
- `<repo_root>/.spec/_shared/policy-packs/*.md` for any repo-local overlays relevant to the change

If neither exists and the repo is important enough to merit one, recommend creating a repo profile using [references/repo-profile-template.md](references/repo-profile-template.md).

To bootstrap a repository with the shared profile and CI wiring, prefer:

```bash
python3 scripts/bootstrap_spec_repo.py --repo-root <repo-root> --seed-house-patterns --policy-pack <pack>
```

This installs the repo-local validation runtime under `.spec/_shared/spec-tools/`, scaffolds `.spec/_shared/repo-profile.md`, and can seed repo-local policy-pack references under `.spec/_shared/policy-packs/`.

Use the repo profile to anchor:

- module boundaries and naming conventions
- preferred abstractions and architectural patterns
- test strategy and coverage norms
- migration and rollout conventions
- auth, tenancy, and observability expectations
- known footguns and historical problem areas

## Non-negotiable contract

- Write specs under `.spec/<scope>/`.
- Use concise kebab-case for `<scope>`.
- Keep three separate artifacts: `design.md`, `requirements.md`, and `tasks.md`.
- Author in order: `design.md`, then `requirements.md`, then `tasks.md`.
- `requirements.md` must derive from design decisions in `design.md`.
- `tasks.md` must derive from requirements in `requirements.md`.
- `tasks.md` must track execution status explicitly so reviewers can see what is `todo`, `in-progress`, `completed`, `deferred`, or `blocked`.
- Downstream artifacts must not introduce new scope.
- Every artifact must contain mandatory frontmatter:
  - `title`
  - `scope`
  - `status`
  - `repo_root`
  - `change_class`
  - `risk_level`
  - `owner`
  - `reviewers`
  - `approvers`
  - `implementation_owner`
  - `operations_owner`
  - `last_updated`
- `status` must be one of:
  - `draft`
  - `discovery-blocked`
  - `design-ready`
  - `requirements-ready`
  - `implementation-ready`
  - `superseded`
- Every artifact must be grounded in the real repository, not in generic software patterns.
- The spec is guidance; the original user request is authoritative for the target outcome, `architecture-standards` is the review lens for how the work should be shaped, and live repository evidence is authoritative for current reality.
- When implementing from the spec, `.spec/<scope>/reviews.md` must track per-slice and final diff-review outcomes, including whether `diff-review` was used or an equivalent manual fallback was required.
- Every meaningful design decision must have a stable `DES-*` ID.
- Every requirement must have a stable `REQ-*` ID and cite one or more `DES-*` IDs.
- Every implementation task must cite one or more `REQ-*` IDs.
- Every deliverable must include a before-and-after audit against upstream artifacts, the original user plan, repository evidence, and `architecture-standards`.
- Every implementation slice and test addition must include a post-implementation review and spec drift check.
- Every leaf task must include a slice review loop that calls for deep diff-review plus `architecture-standards`, a normal-review fix loop until clean, and a `.spec/<scope>/reviews.md` record.
- Every implementation slice must state how `architecture-standards` shaped the slice before editing, not only how the finished diff was reviewed afterward.
- If an upstream artifact changes materially, revisit all affected downstream artifacts.

Recommended `change_class` values include `feature`, `refactor`, `migration`, `integration`, `platform`, `security`, `ops`, `bugfix`, `audit-remediation`, `architecture-transition`, and `quality-gate`.

## Hard evidence gate

Do not write requirements or implementation tasks until you have a minimum fact base from the real codebase.

Minimum fact base:

1. Confirm the target repository root and spec folder location.
2. Identify the primary entry points or user/system flows affected.
3. Identify the concrete code paths, modules, handlers, jobs, schemas, or configs likely to change.
4. Identify at least one related implementation or existing pattern already used in the repository.
5. Identify adjacent callers, consumers, producers, or shared abstractions that could break if the change is wrong.
6. Identify impacted tests, fixtures, dashboards, alerts, or validation surfaces.
7. Identify runtime, deployment, rollback, flag, or operational constraints that matter.
8. Identify relevant audit, review, static analyzer, baseline, suppression, duplication, health, module-budget, or architecture-transition evidence when it exists.
9. Identify recent related repository history for non-trivial changes so you do not repeat reverted or problematic patterns.
10. Identify delivery-correctness risks: ambiguous user intent, missing surfaces, conflicting requirements, stale assumptions, likely overbuild, likely underbuild, and places where architecture standards could change the implementation shape.

If this evidence is incomplete or weak:

- Write or update `design.md` only.
- Record the unknowns under `Open Questions` or `Decision Needed`.
- Do not finalize `requirements.md` or implementation tasks.
- If the user still wants downstream artifacts present, mark them as blocked and do not author implementation commitments from guesswork.

## Continuous feedback and authority model

The spec is not a one-way handoff from plan to design to requirements to tasks to code. It is a checked guide for an implementation agent that remains responsible for the live codebase.

Authority model:

- The original user plan or change request is authoritative for what outcome must be delivered.
- User corrections or clarifications during planning or implementation are authoritative deltas to that request. Treat "this drifted" feedback as a stop signal: refresh `design.md`, then `requirements.md`, then `tasks.md` before continuing code.
- `architecture-standards` and repo-local architecture/policy overlays are authoritative for how the solution should be designed, decomposed, implemented, tested, and reviewed.
- Live repository evidence, current tests, and runtime behavior are authoritative for what currently exists and whether spec assumptions are still true.
- `design.md`, `requirements.md`, and `tasks.md` are guidance artifacts. They must be corrected whenever they drift from user intent, architecture standards, or live code reality.

Agent judgment rule:

- The implementing agent remains accountable for the final technical judgment. Skills, specs, templates, and checklists are guardrails and review lenses, not scripts to follow blindly.
- If `architecture-standards` points toward an approach that does not fit the current repository or the user's requested outcome, the agent must pause, explain the conflict, choose the smallest defensible path, and record the rationale in the relevant artifact.
- If the spec asks for work that now appears wrong, incomplete, overbroad, or contrary to the original request, the agent must update the spec instead of silently implementing the stale task.
- If the agent finds a missed requirement by rereading the original plan, it must add or correct the upstream artifact before continuing downstream.
- The agent may challenge a skill or spec interpretation, but may not silently contradict the user's request, ignore architecture standards, or invent unrelated scope.

Per-deliverable audit loop:

1. Before creating or updating `design.md`, `requirements.md`, or `tasks.md`, inspect the original plan, upstream artifacts, related code, tests, and relevant `architecture-standards` references.
2. After creating or updating that deliverable, audit it against the original plan, upstream artifacts, live repo evidence, and `architecture-standards`.
3. If the audit finds a missing requirement, stale assumption, unsafe design, architecture-standard conflict, or scope mismatch, update the upstream artifact first before changing downstream artifacts.
4. Record the review outcome inside the artifact, even when the outcome is "no upstream changes required."

Implementation loop when the user asks for spec plus code:

1. Choose the next requirement slice: one leaf task or a small group of tightly coupled leaf tasks that completes one requirement or requirement cluster.
2. Before each leaf task in the slice, read the linked `DES-*` entries, linked `REQ-*` entries, the task entry, relevant code, and current tests.
3. Implement only that coherent slice and keep the diff aligned with the cited requirements.
4. Add or update tests that prove the requirement behavior, including negative cases where risk warrants it.
5. After test creation, verify the tests prove the requirement instead of merely asserting implementation details.
6. During each slice, use `architecture-standards` to shape the design/code/test choices as they are made, especially ownership boundaries, data flow, privacy, performance, and proportionality.
7. After the slice, run focused validation, then run a deep `diff-review` scoped to the slice with `architecture-standards` as the architecture lens. If `diff-review` is unavailable, run an equivalent manual deep diff review and record the fallback.
8. If the deep slice review finds issues, fix them, then run normal diff-review passes with `architecture-standards` until the slice is clean.
9. Record the slice review in `.spec/<scope>/reviews.md`: slice ID, linked tasks, linked requirements, validation commands, review mode, findings, fixes, architecture-standard decisions, spec drift decisions, and residual risk.
10. Move to the next requirement slice only after the current slice is clean or explicitly blocked.
11. After all slices are complete, run a final deep diff review over the total branch/worktree diff against the original plan, the full spec package, live repo evidence, tests, and `architecture-standards`; fix findings and repeat normal diff reviews until clean.
12. If code reality, architecture judgment, and spec intent meaningfully diverge at any point, stop implementation long enough to refresh the spec in this order: `design.md`, then `requirements.md`, then `tasks.md`.

Delivery correctness and process efficiency review:

- Keep asking whether the artifact or code still implements the user's original request, not merely the previous generated document.
- Flag and correct overbuild, speculative scope, broad rewrites, or extra abstractions that do not help deliver the requested outcome under architecture standards.
- Flag and correct underbuild where an item from the original request disappeared, became vague, or lost an important surface, state, permission rule, or verification path.
- Avoid duplicated analysis and stale handoffs; reuse prior evidence only after checking it is still current.
- Treat code/runtime performance, render churn, N+1s, overfetching, reliability, security, operability, and maintainability as `architecture-standards` concerns that must be applied when relevant.
- Document any deliberate deviation from an apparent skill/template recommendation with the reason, affected requirement, and architecture tradeoff.

Reviewers must flag specs or completed task entries that show evidence of blind task execution without fresh repository/code re-evaluation. Do not mark them clean while the gap is live, but allow the agent to correct the artifact, use a better repo-specific proof, or document why the check is not applicable.

## Related code, patterns, and blast-radius analysis

This is mandatory. Before articulating the change, inspect how the repository already solves similar problems and which nearby surfaces would be affected indirectly.

Always identify:

- sibling features that solve a comparable problem
- shared abstractions, base classes, hooks, helpers, middleware, or libraries that should be reused
- extension points and framework conventions already used in the affected area
- related config, flags, environment variables, schemas, migrations, jobs, or caches
- adjacent tests that express the current contract
- relevant audit, review, static-analysis, duplication, health, module-budget, baseline, suppression, or transition-plan artifacts
- callers, consumers, or downstream systems that could regress
- observability, auth, rollback, and release patterns already used nearby
- architecture-sensitive surfaces from `architecture-standards`, including ownership boundaries, public contracts, auth, persistence, async workflows, observability, performance hot paths, and operational cost
- imports into the target code, imports from the target code, and sibling modules in the same domain

Rules:

- Prefer existing repository patterns unless there is a documented reason to introduce a new one.
- Call out where the proposed change intentionally diverges from an existing pattern.
- Name the likely blast radius, not just the target file or feature.
- Do not document a local change in isolation if shared code, contracts, or assumptions are touched.

Read [references/related-code-and-patterns.md](references/related-code-and-patterns.md) during discovery.

## Architecture transition planning

Read [references/architecture-transition-planning.md](references/architecture-transition-planning.md) when the spec is driven by a repo audit, Fallow/static-analysis findings, broad duplication, health hotspots, large modules, boundary drift, or target-state redesign.

For these specs, `design.md` must name:

- the current-state failure mode being fixed
- the target-state architecture rule
- the transition slices from current code to target state
- the fitness functions that prove the target state is holding
- analyzer baselines, allowlists, suppressions, and module budgets that remain as transition debt

For `audit-remediation`, `architecture-transition`, `quality-gate`, or Fallow-backed refactor scopes, do not mark downstream artifacts `implementation-ready` unless `design.md` contains static analyzer evidence with command, mode, scope, baseline/gate status, result, interpretation, and design impact. If evidence is unavailable, keep requirements/tasks blocked or scoped to evidence-gathering spikes.

## Risk calibration

Read [references/risk-tiering.md](references/risk-tiering.md) before deciding how deep the spec must go.

## Policy packs

Load narrower policy packs when the repository stack or change domain warrants them:

- Next.js or app-router frontend work: [references/policy-packs/nextjs-patterns.md](references/policy-packs/nextjs-patterns.md)
- Rails data or migration-heavy work: [references/policy-packs/rails-data-migrations.md](references/policy-packs/rails-data-migrations.md)
- Event, queue, or workflow-driven systems: [references/policy-packs/event-driven-services.md](references/policy-packs/event-driven-services.md)

Prefer the smallest relevant set of packs. These refine the base skill; they do not replace repository discovery.

If the target repo already has repo-local copies under `.spec/_shared/policy-packs/`, prefer those first and fall back to the bundled references when the repo-local overlay is absent.

Rules:

- All mandatory sections still need to exist for every spec.
- Lower-risk specs may use concise content and explicit `Not applicable` statements.
- Higher-risk specs must go deeper on compatibility, migration, failure modes, rollback, numeric NFRs, and operational safety.

## Workflow

### 1. Establish scope and initialize the spec folder

- Derive a stable scope name from the change domain.
- Reuse an existing `.spec/<scope>/` folder if it already represents the same change.
- If the repo has `CODEOWNERS` and you know the intended touched paths, infer frontmatter ownership fields before authoring:

```bash
python3 scripts/suggest_owners.py --repo-root <repo-root> --path <repo-relative-path>
```

- Prefer running:

```bash
python3 scripts/init_spec.py --repo-root <repo-root> --scope <scope> --title "<Spec Title>"
```

### 2. Discover the codebase before authoring

- Build the `Repository Discovery Summary`.
- Build the `Related Code and Pattern Inventory`.
- Build the `Adjacent Pattern Comparison`.
- Build the `Blast Radius Review`.
- Build the `Static Analyzer and Audit Evidence` map when reports or analyzer tooling exist.
- Build the `Current-State / Target-State Architecture Evidence` map for audit-driven refactors.
- Build the `Recent Related Repository History` section for non-trivial changes.
- Capture actual repo-relative paths, symbols, contracts, tables, jobs, tests, and operational surfaces.
- Use repository evidence, not assumptions, for the current-state analysis.

If the change touches specific domains, also load the relevant safety reference:

- data or schema changes: [references/data-migrations.md](references/data-migrations.md)
- API, event, or payload changes: [references/api-contracts.md](references/api-contracts.md)
- auth, permission, tenant, or security boundaries: [references/auth-and-permissions.md](references/auth-and-permissions.md)
- jobs, queues, events, retries, or replay behavior: [references/events-and-jobs.md](references/events-and-jobs.md)
- rollout, flags, staged release, or rollback: [references/rollout-and-rollback.md](references/rollout-and-rollback.md)
- telemetry, alerts, dashboards, supportability, or incident response: [references/observability.md](references/observability.md)

### 3. Write `design.md`

Read [references/design-template.md](references/design-template.md) first.

`design.md` is the authoritative source for:

- repository-grounded current-state analysis
- target-state architecture quality when architecture is in scope
- transition slices and containment gates from current state to target state
- proposed solution shape
- impacted boundaries, adjacent systems, and blast radius
- invariants and forbidden outcomes
- compatibility, contract examples, migration, rollout, and reversal strategy
- cross-cutting applicability and risk handling
- explicit design decisions in the `Decision Register`
- fitness functions that prove the architecture/design is holding
- change impact mapping and test impact mapping
- numeric NFR targets where performance, reliability, or scale are part of the change
- architecture standards assessment for ownership, boundaries, contracts, cross-cutting concerns, and proportionality
- original-plan alignment, repository-evidence review, and post-design audit outcome

Use `architecture-standards` while writing this file. Do not skip it.

Before finalizing `design.md`, audit it against the original user plan, current repository evidence, related tests, and `architecture-standards`. If the audit exposes missing discovery, unresolved architecture questions, or stale assumptions, keep the design in `draft` or `discovery-blocked` until those gaps are resolved or explicitly recorded.

### 4. Apply the downstream gating rule

Requirements and implementation tasks may proceed only if design-critical unknowns are resolved enough to support stable commitments.

Critical unresolved items include tagged `Decision Needed` entries in these domains:

- `auth`
- `data-model`
- `public-contract`
- `rollout`

If any of those remain unresolved:

- do not author implementation tasks
- do not convert assumptions into requirements
- mark downstream artifacts as `blocked` if they exist
- if useful, capture blocker-resolution spike work only under `Blocking Work`

### 5. Write `requirements.md`

Read [references/requirements-template.md](references/requirements-template.md) first.

Requirements must:

- cite one or more `DES-*` IDs
- use normative, testable language
- cover negative paths, not just happy paths
- include priority, rationale, verification method, and risk if unmet
- include numeric targets where the requirement governs performance, scale, timing, capacity, or reliability
- include architecture/cross-cutting requirements or explicit `Not applicable` justification when `architecture-standards` identifies ownership, boundary, security, performance, reliability, operability, or maintainability implications
- include cross-cutting coverage or an explicit `Not applicable` justification
- stay aligned with the impact map and forbidden outcomes in the design
- include an upstream alignment audit against the original plan, `design.md`, repository evidence, and architecture standards

Never let a requirement outrun the design.

If requirement authoring reveals missing or wrong design intent, update `design.md` first, then revise `requirements.md`.

### 6. Write `tasks.md`

Read [references/tasks-template.md](references/tasks-template.md) first.

Tasks must:

- remain within scope already defined by the requirements
- be concrete enough for an engineer or agent to execute
- include execution status, dependency, validation, and exit metadata per leaf task
- include `Pre-implementation context check`, `Test creation review`, `Slice review loop`, `Post-implementation review`, and `Spec drift check` fields per leaf task
- include `architecture-standards` validation in risky leaf tasks, covering the relevant ownership, boundary, contract, cross-cutting, and proportionality checks
- cover migrations, observability, rollout, post-deploy verification, and rollback where relevant
- include blocking spikes instead of implementation tasks when the design is not yet stable
- include an `Execution Status Summary` section that stays aligned with the per-task status fields
- form a valid dependency graph with no broken references or cycles

Task authoring must not assume the task list will be executed blindly. Each leaf task must tell the implementing agent to re-check linked design decisions, requirements, current code, and current tests before acting, then verify the diff, tests, and architecture fit after acting.

When implementation is in scope, create or update `.spec/<scope>/reviews.md` and use it as the spec-local review ledger for slice and final diff reviews.

### 7. Validate the package

Run these scripts and fix issues before considering the spec complete:

```bash
python3 scripts/lint_spec.py --spec-dir .spec/<scope>
python3 scripts/check_code_refs.py --spec-dir .spec/<scope> --min-path-refs 8
python3 scripts/traceability_report.py --spec-dir .spec/<scope> --strict
python3 scripts/spec_summary.py --spec-dir .spec/<scope> --write
python3 scripts/spec_summary.py --spec-dir .spec/<scope> --format pr-comment --write
```

When code already exists or a PR is in progress, also check for spec drift:

```bash
python3 scripts/spec_drift_check.py --spec-dir .spec/<scope> --diff-base origin/main
```

Manual validation is still required after scripts pass: read the deliverables as a chain and confirm the package guides iterative planning, implementation, testing, and architecture review rather than blind task execution.

### 8. Enforce in CI and review

- Integrate the validation scripts into repo CI using [references/ci-enforcement.md](references/ci-enforcement.md) and [assets/github-actions-spec-lint.yml](assets/github-actions-spec-lint.yml) as a starting point.
- Use [references/spec-review-checklist.md](references/spec-review-checklist.md) for human review.
- Use the exemplars under [references/example-spec/](references/example-spec/) as the quality bar.
- Prefer attaching the `pr-comment` output to code review or CI job summaries so the spec is visible in the PR, not only on disk.

## Unknown handling rules

Separate uncertainty into these buckets:

- `Confirmed Facts`: supported by repository evidence
- `Assumptions`: provisional statements that do not yet justify downstream commitments
- `Open Questions`: unresolved items that matter but do not yet block the spec
- `Decision Needed`: unresolved items requiring a decision before the design or plan is stable

Rules:

- Do not turn an `Assumption` into a requirement unless the design explicitly resolves it.
- Do not turn a `Decision Needed` item into an implementation task.
- If a critical decision is unresolved, block downstream implementation planning.
- When a downstream artifact exposes a missing upstream decision, update upstream first.
- When implementation or test creation exposes a mismatch with the spec, update upstream artifacts before continuing with additional tasks.

## Hard rules

- No vague requirement verbs such as `support`, `improve`, or `handle` without measurable acceptance criteria.
- No design may omit related code, adjacent pattern comparison, blast-radius review, or repository history review.
- No data change may omit migration, compatibility, and rollback coverage.
- No API, event, or payload change may omit consumer impact, concrete before/after examples, and compatibility analysis.
- No production behavior change may omit observability and post-deploy verification.
- No background job or integration change may omit retry, timeout, idempotency, and failure semantics.
- No security-sensitive change may omit authorization boundaries, abuse cases, and failure handling.
- No artifact or completed task may omit original-request alignment and architecture-standard review; performance-sensitive concerns are handled through `architecture-standards` when relevant.
- No implementation tasks may be authored while critical `Decision Needed` items remain unresolved.
- No implementation task may be executed from a stale spec without re-reading current code, linked requirements, linked design decisions, and current tests.
- No completed leaf task may omit a post-implementation review and spec drift check.
- No completed requirement slice may omit a `.spec/<scope>/reviews.md` record showing the deep slice diff review, fix loop status, architecture-standard check, and any spec drift decision.
- No test addition may be accepted unless it proves requirement behavior and relevant negative cases instead of only implementation details.
- No spec may propose unsafe shortcuts that violate the repository’s existing compatibility, migration, auth, or release conventions without explicit justification.

## Spec refresh rule

If implementation, test creation, validation, or review reveals a meaningful mismatch between code reality and spec intent:

1. Update `design.md` first.
2. Update `requirements.md` to reflect the revised design decisions.
3. Update `tasks.md` to reflect the revised requirements.
4. Re-run lint, reference validation, traceability, and summary generation.

Do not continue implementation from stale downstream tasks after a drift finding. Do not let implementation drift silently away from the spec.

## Slice review ledger

When implementation occurs, `.spec/<scope>/reviews.md` should be concise but auditable. Use chronological or newest-first order consistently.

Each slice entry should include:

- slice ID and completion status
- linked leaf tasks and linked `REQ-*` IDs
- diff scope reviewed
- validation commands and results
- whether `diff-review` was used, or why a manual fallback was used
- deep slice review findings and resolution status
- normal review reruns after fixes, until clean
- `architecture-standards` decisions or tradeoffs
- test adequacy review
- spec drift decision: no drift, upstream artifact updated, or blocked pending correction
- residual risk and follow-up, if any

Final entry:

- total diff scope reviewed
- original-plan alignment audit
- full spec alignment audit
- final deep diff review outcome
- fix/re-review loop status until clean
- final `architecture-standards` assessment

## Output expectation

A complete spec package should be strong enough that an implementation agent can act on it without guessing and that a reviewer can audit it for safety, blast radius, and operational readiness.

Residual limitation:

- The tooling now validates structure, traceability, refs, ownership hints, drift signals, and some symbol semantics.
- It still does not prove that the design perfectly matches runtime truth.
- The main defense against that remaining gap is deeper repository discovery, high-quality repo profiles and policy packs, and repeated implementation-time re-checks against live code and tests.

At minimum, produce or update:

- `.spec/<scope>/design.md`
- `.spec/<scope>/requirements.md`
- `.spec/<scope>/tasks.md`

And validate them with:

- `scripts/lint_spec.py`
- `scripts/check_code_refs.py`
- `scripts/traceability_report.py`
- `scripts/spec_summary.py`
- `scripts/spec_drift_check.py`
