# Design Gates

Use this before and after material architecture-guided implementation. Apply only the lenses relevant to the journey and risk. For local, reversible work, state why a lens is not material and keep the implementation simple.

## Architecture Risk Levels

Use these levels before dropping into detailed bug categories. The detailed categories are examples of how a higher-level architecture failure can show up; they are not the primary goal.

1. **Outcome and intent:** Does the change still deliver the user/business outcome, or did generated tasks, local fixes, or partial remediation narrow the problem incorrectly?
2. **Ownership and authority:** Did the source of truth, validation owner, authorization owner, state owner, or route/API owner move, and is the invariant enforced at the new owner boundary?
3. **Dataflow and materialization:** Can invalid, stale, legacy, or unauthorized data enter through an acquisition path; can admitted or eligible data drive unsafe secondary reads, joins, aggregates, previews, metadata, or generated rows?
4. **Contract and compatibility:** Did serialized public shape, error semantics, generated artifacts, migration behavior, old clients, or fallback semantics change across layers?
5. **Operational and cost behavior:** Did the change alter polling, snapshots, fan-out, hot writes, retries, pagination, retention, observability, or failure recovery?
6. **Verification and enforcement:** Does the proof exercise the real public behavior, negative variants, sibling paths, and recurrence guard instead of only the happy path or helper internals?

When a level is relevant, solve at that level first. Prefer authoritative admission rules, source-of-truth derivation from eligible inputs, target-owner validation, stable public contract mapping, bounded cost behavior, and tests/static/runtime guards that make the invariant hard to regress. If a level is not relevant, record a short reason and keep the implementation simple.

## Code Design Gate

Before building code that introduces or changes a module, shared helper, state owner, schema, API route, data model, background job, integration, cache/fallback, or cross-feature behavior, answer through the implementation:

- **What is the smallest complete change?** Define the required journey, non-goals, and the simplest end-to-end implementation before adding scaffolding.
- **What can be reused, deleted, or kept local?** Prefer existing paths and capability-local code over new shared surfaces.
- **What complexity is being added?** Name new concepts, files, public exports, dependencies, stores, or runtime processes. Each must solve a current problem.
- **Why is the simpler option insufficient?** Do not add an abstraction, layer, dependency, queue, cache, or generalized framework without concrete present-day evidence.
- **Where should this code live?** Put it in the owning capability/layer, not where the request first appears.
- **Who owns the invariant?** Enforce business rules, permissions, tenancy, generated IDs, and persistence constraints at the authoritative layer.
- **What is the public boundary?** Expose the narrowest command, query, component, hook, schema, adapter, or event callers need.
- **Is this export a real runtime/API boundary?** Do not export internals from production modules only for tests or coverage. Move stable testable primitives into owner-local modules that production imports, or test through the existing public behavior.
- **Will this grow into a monolith?** If a component/function is accumulating rendering, state transitions, effects, data shaping, persistence, and adapter logic, split by owner now: state/policy, view model, render primitives, effects/adapters, and route/data boundary.
- **What must not depend on what?** Keep inner policy free of framework, transport, vendor, and presentation dependencies.
- **What path bypasses this?** Check alternate UI surfaces, API routes, jobs, scripts, imports, direct mutations, and fallback/read-model paths.
- **What invariant is being transferred?** When replacing a broad path, snapshot, backend authority, selector, route contract, cache, or generated artifact, name the old guarantee and where it is enforced now.
- **How can invalid candidates enter?** For direct id lookups, scope scans, relation/link expansion, stale references, fallback pages, generated artifacts, stream keys, caches, optimistic state, and API error branches, prove candidates pass their own owned validation before return or persistence.
- **What downstream reads do admitted candidates drive?** If candidates feed secondary ids, joins, aggregates, metadata, previews, counters, generated rows, or child records, derive keys from the eligible source set and validate materialized targets through their own owner.
- **What is the journey request budget?** Count client round trips, database work, repeated authorization, payload size, and cache/refetch effects. Prefer capability commands and queries when client-side CRUD orchestration would be chatty or non-atomic.
- **What are the end-to-end budgets?** For material paths, decide which latency, throughput, payload, query/fan-out, concurrency, freshness, and cost expectations matter. Allocate attention across the complete journey instead of optimizing one layer in isolation.
- **What is the cost curve and amplification path?** Identify the unit of value, billable work, idle behavior, fan-out, reruns/retries, invalidation/reconciliation, retention, transfer, third-party usage, and operational burden. Compare designs using total cost rather than one provider metric.
- **Does the boundary compress or merely concentrate complexity?** A narrow API should simplify callers while keeping presentation, application workflow, business policy, data access, and infrastructure responsibilities owned inward.
- **What crosses each boundary?** Make commands, queries, results, errors, identity/tenant context, deadlines, and side-effect expectations explicit where differences matter. Map between transport, application, domain, persistence, and vendor shapes rather than leaking one shape through every layer by convenience.
- **What consistency and concurrency semantics are required?** Choose transaction scope, conflict handling, ordering, freshness, idempotency, and reconciliation based on the journey's correctness needs. Do not pay for stronger guarantees than the use case needs.
- **What public contract is serialized?** Distinguish internal option names from route/API/query/storage keys, and assert the public serialized contract in tests for auth, redirects, webhooks, routes, jobs, and persisted data.
- **How is this enforced?** Prefer tests, types, schemas, runtime guards, dependency rules, or CI/lint checks over comments.
- **What is the failure mode?** Design retries, idempotency, rollback, user feedback, observability, and partial-failure behavior where relevant.
- **What gets deleted later?** If this is a shim, fallback, feature flag, compatibility path, or exception, make the cleanup path visible.

If the answer is "just add it to the closest component/handler/helper," stop and check whether that scatters policy, duplicates a rule, or bypasses the real owner.

If the answer is "add a reusable framework in case we need it later," stop and implement the required vertical slice first.

## Transition Gate

When current architecture cannot change safely in one step:

- contain the live risk or cost growth first
- move one complete journey through the correct owner
- delete the bypass, duplicate policy, or obsolete compatibility path included in that slice
- add proof and recurrence prevention before starting the next slice
- record deferred debt with owner and revisit trigger

Load `completion-and-output.md` before finishing material work.
