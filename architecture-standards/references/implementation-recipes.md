# Implementation Recipes

Use these when building code with architecture standards. They are not templates to copy blindly; they are decision recipes for common implementation shapes.

## Contents

- features, material journeys, validation, and shared presentation
- APIs/actions, middleware/guards, and persistence
- background work, caches/read models, and third-party integrations

## Add A New Feature

1. Identify the capability that owns the behavior.
2. Put orchestration in the application/use-case layer or nearest existing equivalent.
3. Put durable business rules in domain/shared domain helpers, not in UI or route handlers.
4. Put persistence mapping and query shape in the data layer or existing store/repository boundary.
5. Keep UI/components focused on interaction and rendering.
6. Add tests at the cheapest layer that proves the invariant, plus one boundary test when integration risk matters.

Avoid:

- adding business rules to the first component or route touched
- creating a generic helper before there is a real variation point
- bypassing existing application/store/service flows for speed

## Add Or Change A Material User/System Journey

Use this recipe when a journey is performance-sensitive, crosses several layers, performs multiple reads/writes, or has meaningful failure consequences. Apply only the steps relevant to the codebase and use case.

1. Trace the complete journey across delivery, application, domain, data, infrastructure, and external dependencies.
2. Define the correctness contract first: authority, transaction/consistency needs, conflict behavior, ordering, freshness, partial failure, and user-visible completion.
3. Establish proportional budgets for client/internal round trips, latency, payload, query/fan-out work, concurrency, memory, and cost.
4. Shape a capability command/query when it reduces caller knowledge, chatty CRUD, or split transactions without hiding unbounded server work.
5. Remove waterfalls and N+1 work; consider projections, batching, bounded parallelism, and deterministic pagination where they materially help.
6. Move work async only when its delivery, idempotency, status, retry, and recovery semantics are acceptable.
7. Add caches or read models only when the read pattern justifies their ownership, freshness, invalidation/rebuild, reconciliation, and operational cost.
8. Instrument the critical boundaries and verify the resulting journey rather than assuming fewer endpoints means better performance.

Avoid:

- optimizing one layer while making the complete journey slower or less reliable
- replacing chatty client calls with one endpoint that performs unbounded work
- making independent work sequential without a correctness reason
- parallelizing dependent or consistency-sensitive work
- adding queues, caches, or read models without a measured or credible need

## Add Or Change Validation

1. Decide whether the rule is shape validation, business validation, permission validation, or compatibility validation.
2. Enforce shape at the edge.
3. Enforce business/permission invariants at the authoritative layer.
4. Mirror user-friendly validation in UI, but do not make UI the authority.
5. For update paths, check legacy stored data and partial updates separately from create paths.

Avoid:

- reusing strict create schemas for update/edit paths without checking compatibility
- adding only UI validation for server-critical rules
- spreading the same min/max or enum rule across components without a shared source

## Add Or Change A Shared Component/Hook

1. Confirm it represents a stable repeated concept, not just two similar screens.
2. Define the narrowest props/API that encode behavior without leaking caller internals.
3. Keep policy out of presentational primitives unless the component owns that policy by design.
4. Check all render modes: empty, disabled, read-only, editable, loading, error, nested/transient container.
5. Add at least one consumer-level test for a non-happy-path behavior when the component is shared widely.

Avoid:

- turning screen-specific behavior into a global abstraction too early
- hiding important permission or state differences behind generic props
- creating shared components that still require every caller to duplicate policy

## Add Or Change An API/Route/Action

1. Define the command/query contract explicitly.
2. Compose the edge pipeline visibly: request identity, authentication context, risk-tiered rate limit, transport validation, capability use case, and response/error mapping as applicable.
3. Keep transport parsing and response mapping at the edge.
4. Delegate business rules and state transitions inward.
5. Use a consistent success, error, and pagination contract across the public boundary.
6. Shape commands and queries around complete capability journeys when several CRUD calls form one workflow.
7. Keep list queries bounded with explicit pagination and maximum limits.
8. Decide which cross-cutting concerns belong in middleware/guards and which capability concerns belong in the application use case.
9. Check direct/bypass callers: jobs, scripts, store actions, webhooks, imports, tests.
10. Decide idempotency and retry behavior for unsafe operations.
11. Add contract/error tests for invalid input and compatibility-sensitive paths.

Avoid:

- accepting client-controlled authoritative fields
- exposing persistence models directly
- letting route handlers become the only place business rules exist
- putting capability-specific authorization or workflow policy in global middleware
- wrapping every route in generic machinery that obscures its contract and use case

## Add Or Change Middleware Or A Guard

1. Confirm the concern truly applies broadly before placing it in middleware.
2. Keep middleware deterministic, bounded, and cheap.
3. Attach request context or reject/redirect at the edge; delegate capability decisions inward.
4. Measure repeated external or datastore work performed on every request.
5. Test ordering, bypass paths, public routes, failure semantics, and sensitive logging.

Middleware and guard concerns include:

- request/correlation identity
- coarse authentication/session establishment
- security headers, CORS, locale, and rate limits
- transport-shape validation at a scoped route boundary

Keep resource ownership, durable business rules, multi-step workflows, and feature-specific response shaping in their owning application, domain, or presentation boundary.

## Add Or Change Persistence

1. Name the source of truth and ownership boundary.
2. Add schema constraints/indexes for true invariants where the datastore can enforce them.
3. Shape reads for the owning capability journey rather than exposing generic datastore access to callers.
4. Choose transaction scope, isolation/conflict handling, and ordering from the consistency needs of the use case.
5. Parallelize independent reads when it reduces latency and preserves understandable failure semantics.
6. Keep migrations/backfills idempotent when possible.
7. Check read model, cache, search, and projection consistency.
8. Define retention, deletion, and recovery semantics if data lifecycle changes.

Avoid:

- relying only on application code for uniqueness or tenancy invariants
- duplicating truth across stores without sync ownership
- changing stored shape without compatibility or migration strategy

## Add Or Change Background Work

1. Decide why the work is async instead of inline.
2. Define delivery guarantee, idempotency, retry, dead-letter/recovery, and visibility.
3. Ensure state changes and side effects cannot diverge silently.
4. Keep job handlers authoritative for the rules they execute; do not assume UI/route prevalidation.
5. Add tests for retry or duplicate delivery when failure matters.

Avoid:

- backgrounding user-critical work without status visibility
- non-idempotent retries
- fan-out with unclear partial-failure semantics

## Add Or Change A Cache/Fallback/Read Model

1. Name the source of truth.
2. Define freshness, invalidation, and reconciliation rules.
3. Check empty, stale, lost-access, and deleted-source cases.
4. Ensure fallback data cannot outlive the authority indefinitely.
5. Add targeted tests around merge/reconciliation if bugs would persist across refreshes.

Avoid:

- letting fallback state become a shadow source of truth
- applying optimistic overrides indefinitely
- caching without ownership or invalidation

## Add Or Change A Third-Party Integration

1. Put vendor SDK and response types at the edge.
2. Map vendor errors into internal error taxonomy.
3. Define timeout, retry, idempotency, rate-limit, and circuit-breaker behavior where relevant.
4. Keep secrets and credentials out of client bundles and logs.
5. Add contract tests or adapter tests around the mapping.

Avoid:

- leaking vendor types into domain/application layers
- retrying unsafe operations without idempotency
- coupling core business logic to provider-specific quirks
