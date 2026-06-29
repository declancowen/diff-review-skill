# Simplicity Gate

Use this before adding abstractions, layers, dependencies, shared modules, background systems, or broad scaffolding. The goal is not minimum code at any cost. The goal is the fewest concepts needed to keep the current system correct, operable, and easy to change.

## Default Shape

Start with:

- one capability-local implementation
- existing repository patterns and dependencies
- one authoritative source of truth
- synchronous execution for short interactive work
- direct, explicit orchestration
- narrow public interfaces
- tests through real public behavior

Escalate only when current evidence shows this shape is insufficient.

## Complexity Must Pay Rent

Before introducing a new architectural concept, name:

1. **Present problem:** the current requirement, failure mode, ownership gap, or measured constraint.
2. **Simpler option:** the least-complex implementation that could work.
3. **Why it fails:** concrete evidence that the simpler option is unsafe or materially worse.
4. **Added concept:** the abstraction, dependency, layer, store, queue, cache, service, or framework being introduced.
5. **Proof:** the test, metric, boundary rule, or operational evidence showing the added concept solves the problem.

If the simpler option does not clearly fail, use it.

## Evidence Thresholds

### New Abstraction Or Shared Helper

Add only when at least one is true:

- two or more current callers share the same owned invariant and should change together
- one authoritative rule must be protected from multiple entrypoints
- a real provider, environment, or policy/mechanism boundary exists now
- extraction makes a meaningful rule independently testable without widening production APIs

Do not extract because code looks similar, might be reused later, or reduces line count.

### New Layer Or Module

Add only when it creates a clear owner, prevents a dependency violation, or separates responsibilities that already change independently.

Do not create `service`, `repository`, `manager`, `engine`, `factory`, or `base` layers that only forward calls or rename framework operations.

### New Dependency

Add only when it removes more complexity or risk than it introduces. Account for API surface, upgrades, bundle/runtime cost, security, configuration, and team knowledge.

Prefer the standard library or an existing dependency when the behavior is small and stable.

### New Runtime Mechanism

Queues, caches, events, background jobs, read models, and additional datastores require a named current need plus ownership for failure, retries, observability, reconciliation, and cleanup.

Do not add operational architecture for hypothetical scale.

### New Generalized Framework Or Scaffold

Do not generate every foreseeable variant, CRUD endpoint, component state, adapter, or configuration option. Build the required vertical slice first. Generalize only from demonstrated variation.

## Complexity Ledger

For material changes, reason through:

- concepts added
- files/modules added
- public exports added
- dependencies added
- runtime processes or stores added
- concepts/files/paths removed or replaced
- net effect on the number of places a maintainer must understand or change

This does not require a document for normal work. It is a design check. If net complexity rises, the current requirement or risk must justify it.

## Thin-Slice Rule

Prefer one complete, working path over broad scaffolding:

1. implement the smallest end-to-end behavior
2. verify it through the public boundary
3. observe the actual second use or variation
4. extract only the stable repeated concept

Keep small, meaningful duplication when the correct abstraction is not yet clear.

## Journey Request Budget

Do not equate simple CRUD endpoints with an efficient user journey. Map the complete interaction and count:

- client-to-server round trips
- sequential versus parallel requests
- database queries and transactions behind each request
- repeated authentication, authorization, and hydration work
- cache invalidations, refetches, and optimistic-state reconciliation
- payload size and over-fetching

Prefer one coarse-enough capability command or query when a user action must complete atomically, requires several related reads/writes, or would otherwise make the client orchestrate business rules.

Keep separate CRUD operations when actions are genuinely independent, independently authorized, and do not create a chatty or partially completed workflow.

Do not solve chatty CRUD by creating a generic endpoint that returns everything. Shape journey-specific commands and queries with explicit contracts, bounded payloads, and server-owned authorization.

For material journeys, define a proportional request budget and verify it. Example: one primary fetch for a detail screen, one command for an atomic state transition, and bounded follow-up work that does not block the user.

## AI Overcoding Smells

Stop and simplify when a change introduces:

- speculative extension points or configuration
- interfaces with one implementation and no real boundary
- wrappers that only forward calls
- generic helpers that hide capability ownership
- parallel models that repeat the same shape without a contract need
- state, caches, or stores that duplicate an existing source of truth
- client-orchestrated request chains that repeat authorization or split one business transaction across several calls
- generic aggregation endpoints that hide unbounded database work
- broad error, logging, retry, or event frameworks for one local flow
- unrelated refactors, generated docs, or test matrices
- large comment blocks explaining avoidable indirection
- more test setup than behavior proof

## Review Questions

- What is the smallest complete change?
- What can be reused, deleted, or left local?
- Which new concept is strictly necessary now?
- Can a maintainer trace the primary path without jumping through unnecessary wrappers?
- Does every abstraction have a real owner and current caller?
- Did the change reduce the number of places that must change together?
- Is remaining complexity caused by the domain, or by the implementation?

## Completion Standard

A proportionate implementation:

- solves the requested journey end to end
- adds no speculative capability
- introduces the fewest justified concepts
- keeps ownership and authority explicit
- has focused proof for meaningful behavior and risk
- leaves an obvious path to evolve when real requirements appear
