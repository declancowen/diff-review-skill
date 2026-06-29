# Architecture Scorecard

Use this for whole-repo architecture reviews or repo audits. It helps produce a governance-quality assessment without turning the skill into a documentation exercise.

Score each area:

- **0:** absent or actively harmful
- **1:** inconsistent, mostly convention-based
- **2:** mostly sound, some gaps
- **3:** strong and enforceable

## Score Areas

### Capability Boundaries

- modules map to business capabilities or clear platform responsibilities
- public interfaces are narrow
- cross-boundary reach-through is rare or impossible
- duplication/refactor evidence does not show the same capability concept scattered across unrelated modules

### Dependency Direction

- inner policy does not depend on frameworks, transport, vendor SDKs, or UI
- imports reflect intended layers
- cycles are absent or contained
- static/import checks or architecture tests protect important boundaries when drift has happened before

### Separation Of Concerns

- presentation depends on capability-level commands/queries rather than datastore mechanics
- application use cases own orchestration, authorization, transaction boundaries, and side-effect coordination
- durable business policy is not trapped in controllers, hooks, ORM queries, or vendor adapters
- data and infrastructure concerns have explicit owners and do not leak outward
- clean external APIs do not hide god controllers, services, hooks, or database functions

### Cross-Layer Semantics

- meaningful boundaries use deliberate commands, queries, results, events, and error semantics
- transport, application, domain, persistence, and vendor shapes are mapped where their meanings differ without ceremonial duplication
- required identity/tenant, correlation, deadline/cancellation, and idempotency context reaches the correct owner
- transaction, consistency, conflict, ordering, freshness, side-effect timing, and partial-failure behavior are explicit where relevant
- important work is not hidden behind implicit queries, silent retries, global mutable context, or swallowed failures

### Data Ownership

- each data model has a clear owner
- authoritative writes are centralized
- caches/read models/fallbacks are not shadow sources of truth
- bootstrap, seed, fixture, recovery, and migration paths preserve the same ownership rules as normal writes

### Contract Ownership

- API/event/schema contracts have clear owners
- create/update/import/direct mutation paths are aligned
- compatibility is explicit where old clients/data exist
- CLI, webhook, docs/import/export, and generated-client contracts are not duplicated in unowned shapes

### Security And Tenancy

- authn/authz are enforced server-side
- tenant/scope boundaries are explicit in lookups and mutations
- secrets and sensitive data stay at safe boundaries

### Async And Reliability

- retries are idempotent
- partial failure is handled
- important jobs/streams have visibility and recovery

### Operability

- critical flows have useful logs, metrics, traces, status, or alerts
- failure ownership is clear
- rollout/rollback paths are realistic

### Testability

- core rules are testable without full stack
- boundary and compatibility tests exist where risk justifies them
- tests protect architectural invariants, not only happy paths
- shared test helpers preserve runtime semantics and do not hide unclear architecture

### Evolvability

- architecture debt is visible enough to manage
- exceptions have cleanup paths
- new features can follow existing patterns without guessing
- broad analyzer inventories are classified into fixed, deferred, accepted, policy-modeled, deployment-gated, and inventory-only states

### Current-State Fitness

- actual code shape matches the claimed architecture
- duplication, complexity, churn, and module-size signals do not contradict the score
- target-state plans include transition slices and containment gates
- accepted baselines, suppressions, and allowlists have owners and revisit triggers

### Simplicity And Proportionality

- the system uses the fewest concepts needed for current requirements and risks
- abstractions, layers, dependencies, and runtime mechanisms solve named present-day problems
- speculative scaffolding, forwarding wrappers, and unused extension points are absent
- maintainers can trace primary journeys without unnecessary indirection
- complexity added by recent work is balanced by removed paths, reduced risk, or clear operational value

### Journey Efficiency

- user journeys use bounded client round trips and payloads
- capability-level commands and queries own multi-step or atomic workflows
- clients do not orchestrate durable business rules through chatty CRUD chains
- server/database work is measured separately from API request count
- caches, optimistic state, and invalidation do not create excessive reconciliation work
- material paths bound query/fan-out work, concurrency, memory, retries, and queue/job work
- performance mechanisms are selected proportionately and retain clear source-of-truth, failure, and operational ownership

### Cost Efficiency

- material costs are attributable to useful outcomes, capabilities, environments, and owners
- normal, idle, peak, failure/recovery, and data-growth amplification are understood
- calls/work, fan-out, retries, retained/derived data, transfer, and third-party usage are bounded where needed
- architecture options are compared by total cost of ownership rather than technology preference
- costly paths have proportionate evidence, budgets/alerts, and regression guardrails
- cost optimization does not weaken correctness, security, reliability, or maintainability without an explicit accepted tradeoff

## Output Format

```markdown
| Area | Score | Evidence | Main risk | Next action |
|------|-------|----------|-----------|-------------|
| Data ownership | 2 | writes mostly centralized, fallback path drift exists | stale read model authority | add reconciliation guard/test |
```

## Interpretation

- Any `0` in security, data ownership, contract ownership, or async reliability is a high-priority architecture risk.
- Repeated `1`s indicate governance drift: the architecture relies on humans remembering rules.
- A `3` should have enforcement evidence, not just tidy folders.
- A high target-state score is not credible if current-state fitness is low. Diagnose why the target architecture is not being expressed in the code before declaring the repo architecturally healthy.
