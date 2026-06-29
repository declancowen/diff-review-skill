---
name: architecture-standards
description: Use this skill when designing target architecture, diagnosing messy current-state architecture, scaffolding a new application/service/feature, refactoring toward cleaner boundaries, reviewing code for architectural quality, or making implementation decisions that affect ownership, layering, contracts, persistence, async workflows, auth/tenancy, shared abstractions, operability, cost, or long-term maintainability. The skill guides code design and remediation planning with practical, enforceable boundaries rather than documentation ceremony.
---

# Architecture Standards

Design and build code with clear ownership, proportionate architecture, enforceable boundaries, and practical tradeoffs. Architecture should be visible in module placement, public interfaces, types, schemas, tests, runtime guards, dependency boundaries, and operational checks.

Use progressive disclosure: keep this file as the operating router, and load focused references only when needed.

## Reference Map

- `references/decision-framework.md`: frame meaningful decisions, proportionality, tradeoffs, governance triggers, and revisit conditions.
- `references/design-gates.md`: use before and after material implementation work to check ownership, authority, dataflow, contracts, cost, failure behavior, and enforcement.
- `references/operating-modes.md`: detailed responsibilities for Build, Governance / Audit, Current-State Diagnosis, and Target-State Design modes, plus the reusable learning rule.
- `references/simplicity-gate.md`: use before adding abstractions, layers, dependencies, shared modules, runtime mechanisms, or broad scaffolding, and when work risks AI overcoding.
- `references/architecture-shapes.md`: use when choosing modular monolith vs services, sync vs async, CRUD vs domain model, CQRS/read models, API style, persistence, jobs, or abstraction level.
- `references/layer-standards.md`: use when placing code, defining boundaries, or checking dependency direction across presentation, application, domain, data, infrastructure, and API/integration layers.
- `references/implementation-recipes.md`: use when building or changing a feature, material journey, validation rule, API, middleware, persistence model, shared component, background job, cache/fallback, or integration.
- `references/enforcement-patterns.md`: use when an architecture rule needs tests, types, schemas, runtime guards, lint/static checks, dependency rules, or operational checks.
- `references/cross-cutting-standards.md`: use for security, performance, reliability, observability, testability, maintainability, and general efficiency.
- `references/cost-efficient-architecture.md`: use when cost can scale with usage, data, time, fan-out, retries, retention, environments, third parties, or operational complexity.
- `references/current-state-diagnosis.md`: use when an existing repo is structurally messy or architecture standards are not holding.
- `references/target-state-design.md`: use when defining or evaluating what an existing or new system should become.
- `references/smell-triage.md`: use to classify architecture debt as `must fix now`, `should fix if cheap/safe`, or `defer`.
- `references/refactor-design.md`: use for broad refactors, duplication reduction, health hotspots, module pressure, and transition planning.
- `references/static-analyzer-policy.md`: use when analyzer config, findings, baselines, suppressions, boundaries, health thresholds, or coverage affect architecture decisions.
- `references/architecture-scorecard.md`: use for whole-repo architecture or governance assessments.
- `references/review-checklists.md`: use before finalizing architecture or implementation reviews.
- `references/completion-and-output.md`: use before finishing architecture-guided implementation or repo-level architecture work.
- `fallow` skill reference `quality-benchmarks.md`: use when Fallow evidence exposes missed structural debt or calibrates architecture fitness.
- `scripts/architecture-preflight.sh`: run from repo root for broad architecture reviews or fragmented repo context.

## Core Workflow

1. Frame the work as a business capability, user/system journey, and failure consequence.
2. Identify the current repo architecture and preserve coherent existing patterns unless evidence justifies changing them.
3. Define the smallest complete change, explicit non-goals, and what can be reused, deleted, or kept local.
4. Identify the owner of each relevant invariant, source of truth, public contract, side effect, and operational responsibility.
5. Choose the lightest architecture shape that keeps the system correct, operable, cost-conscious, and evolvable.
6. Implement through the owning boundary, not the closest file.
7. Encode important decisions through proportionate tests, types, schemas, guards, static rules, metrics, or operational controls.
8. For analyzer-driven or broad refactor work, define the structural prevention rule before editing: what shape should stop recurring, which owner will hold it, and which fitness function will catch relapse.
9. Verify the complete journey, relevant negative variants, bypass paths, and recurrence guard.
10. State only material tradeoffs, residual risks, and revisit conditions.

## Operating Modes

### Build Mode

Use for normal features, bug fixes, refactors, and scaffolding.

- Load `operating-modes.md` for the detailed mode responsibilities.
- Load `design-gates.md` and the relevant implementation recipe when the change is material.
- Implement one complete vertical slice before generalizing.
- Keep uncertain duplication local and avoid broad refactors unless the task would otherwise leave a live architecture risk.
- Require each new abstraction, dependency, layer, or runtime mechanism to solve a named current problem.

### Governance / Audit Mode

Use for whole-repo architecture decisions, platform changes, system design, or cross-system work.

- Load `operating-modes.md` for the detailed mode responsibilities.
- Diagnose current state before designing target state.
- Evaluate ownership, dependency direction, contracts, operational behavior, enforcement, and drift.
- Load `architecture-scorecard.md`, `current-state-diagnosis.md`, and `target-state-design.md` as relevant.
- Separate coherent choices and accepted deviations from harmful drift.

### Current-State Diagnosis Mode

Use when architecture is already messy or a prior target state is not holding.

- Load `operating-modes.md` for the detailed mode responsibilities.
- Map what the code actually does, not what folders or documents claim.
- Cluster symptoms into missing owners, weak boundaries, mixed responsibilities, unowned contracts, cost amplification, or missing fitness functions.
- Define immediate containment, safe transition slices, prevention, and explicit accepted debt.

### Target-State Design Mode

Use when defining what the architecture should become.

- Load `operating-modes.md` for the detailed mode responsibilities.
- Derive target decisions from current-state evidence, product journeys, failure consequences, and constraints.
- Define owners, boundaries, contracts, dependency direction, operational behavior, transition slices, and fitness functions.
- Keep the target falsifiable and proportionate; do not prescribe architecture fashion.

## Architecture Stance

- Treat architecture practices as context-dependent options, not universal rules.
- Prefer capability ownership and explicit authority over folder aesthetics.
- Keep business policy inward and frameworks, vendors, protocols, storage, and presentation at edges where practical.
- A narrow public boundary should simplify callers without concentrating every responsibility in one god module.
- Measure and budget complete journeys, not isolated endpoints or provider metrics.
- Treat cost as an architecture quality attribute, but do not weaken correctness, security, reliability, or recovery merely to lower spend.
- Prefer code-level enforcement over documentation; use documentation only when the repo already relies on it or the decision cannot be encoded.
- Complexity must pay rent. If a simpler option does not clearly fail the current requirement, use it.

## Mandatory Gates

Load `design-gates.md` when work changes a durable system decision or meaningful risk surface, including:

- capability/module boundary, source of truth, data ownership, or public contract
- auth, authorization, tenancy, privacy, or audit behavior
- async workflow, retry/idempotency model, cache/read model, integration, or persistence lifecycle
- shared abstraction, broad refactor, analyzer policy, module budget, or long-lived exception
- material performance, cost, infrastructure, deployment, recovery, or operational ownership

Load `simplicity-gate.md` before introducing a new abstraction, layer, dependency, shared surface, runtime mechanism, or generalized scaffold.

Before finalizing broad architecture or implementation reviews, load `review-checklists.md`.
Before finishing material work, load `completion-and-output.md`.

## Skill Boundaries

- `repo-audit` owns inverse diagnosis: reconstruct current state, prove harmful gaps, and define evidence-backed transition slices.
- `architecture-standards` owns forward design and implementation: choose the proportionate target and encode it through the correct owner.
- `diff-review` owns branch/change validation: prove a proposed change preserves behavior and strengthens the intended architecture.

When remediation is requested, move one proven risk-first slice from repo audit into Build Mode, verify it, then re-audit before closure.

## Output Standard

For implementation work, architecture should be evident in code: owner-aligned placement, narrow public interfaces, authoritative validation, deliberate boundary translation, and focused invariant proof.

For repo-level architecture work, report current-state failure modes, target-state decisions, transition slices, enforcement/fitness functions, accepted deviations, and residual risks. Avoid vague phrases such as "clean architecture" or "best practice" without naming the concrete rule or consequence.

For broad architecture reviews, run:

```bash
~/.codex/skills/architecture-standards/scripts/architecture-preflight.sh
```

Treat preflight output as context, not proof. Keep final answers concise and mention only material decisions, tradeoffs, enforcement, and residual risk.
