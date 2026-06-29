# Layer Standards

Use this when placing code, defining module boundaries, or reviewing dependency direction.

## Contents

- module and dependency rules
- layer interaction and boundary compression
- separation tests and pragmatic capability slices
- delivery-agnostic ownership
- presentation, application, domain, data, infrastructure, and API/integration responsibilities

## Module And Dependency Rules

- Define modules around business capability, ownership, and change boundaries.
- Split by capability first, then by layer where it clarifies responsibility.
- Outer layers may depend inward. Inner layers must not depend outward.
- Frameworks, SDKs, transport types, and vendor APIs belong at edges.
- Define interfaces in the layer that owns the policy, not in the adapter layer.
- Cross-module access should go through public interfaces, application services, or deliberate events.
- One capability/service should not read or mutate another capability/service private datastore directly.
- Shared libraries are for true cross-cutting primitives, not business logic dumping grounds.
- Avoid catch-all `services`, `helpers`, `managers`, and `utils` that mix unrelated responsibilities.

Common shape:

```text
capability/
  presentation/
  application/
  domain/
  data/
  infrastructure/
```

Frontend-heavy equivalent:

```text
feature/
  ui/
  application/
  domain/
  data/
```

Folder names matter less than responsibility clarity and dependency direction.

## Layer Interaction Standards

Layers collaborate through explicit semantics, not merely function calls or folder placement. Apply these practices where the boundary is meaningful; do not create DTOs, interfaces, or mapping layers that only rename identical local shapes.

- Pass the narrowest command, query, result, or event needed for the owned use case.
- Make identity, tenant/scope, trusted authorization context or scoped capability, deadline/cancellation, correlation, and idempotency context explicit when the downstream owner needs it. Keep authoritative authorization enforcement with its owner.
- Translate transport, application, domain, persistence, and vendor models at the boundary where their meanings diverge.
- Translate lower-level failures into stable owner-level error semantics. Preserve diagnostic causes for operations without exposing vendor details to callers.
- Define whether a multi-step interaction is atomic, eventually consistent, compensating, or allowed to return partial results.
- Choose transaction scope, conflict handling, ordering, and freshness from business correctness needs rather than framework defaults.
- Keep side effects visible in the application workflow. Decide whether they occur inside the transaction, after commit, through an outbox/job, or as best-effort work.
- Avoid hidden work at boundaries: implicit queries, unbounded fan-out, silent retries, global mutable context, and service-locator dependencies.
- Propagate resource limits and lifecycle deliberately: timeouts, cancellation, bounded concurrency, connection/pool use, backpressure, and graceful shutdown where relevant.
- Observe important boundaries with stable correlation and outcome signals so failures and cost can be attributed to the owning journey.

The goal is enough explicitness to preserve meaning and ownership across layers, not maximum ceremony.

## Boundary Compression vs Responsibility Concentration

A strong boundary should simplify callers without turning the boundary implementation into a monolith.

- **Boundary compression:** a capability-level command or query hides storage, authorization, workflow, and integration mechanics from callers through a narrow contract. This is desirable.
- **Responsibility concentration:** a controller, hook, handler, RPC, or service personally owns transport parsing, authorization, business policy, persistence queries, side effects, and response mapping. This is not separation of concerns, even when callers see one clean API.

Review both sides of a boundary:

1. **Upward effect:** Does the boundary reduce presentation/client knowledge, round trips, cache reconciliation, and business-rule duplication?
2. **Inward implementation:** Does each concern still have a clear owner, with orchestration visible and durable rules enforced at authoritative layers?

Do not reward a clean external API if it merely moves all complexity into a god controller or database function. Do not reject a coarse capability endpoint merely because it performs several internal steps; those steps belong behind the boundary when they form one owned workflow.

## Layer Separation Test

For a representative journey, identify:

- **Presentation:** renders or receives input, validates transport shape, maps output
- **Application:** coordinates the use case, authorization, transaction, and side effects
- **Domain/business:** decides durable rules and valid state transitions
- **Data:** executes owned queries and enforces datastore invariants
- **Infrastructure:** implements vendor mechanisms such as storage, email, queues, and notifications

Then ask:

- Can the presentation layer complete the journey without knowing tables, joins, vendor APIs, or durable business sequencing?
- Can business policy be understood and tested without HTTP/UI, ORM, or vendor setup?
- Is the transaction boundary owned by the application use case?
- Does the data layer protect true invariants rather than relying only on caller behavior?
- Can infrastructure failures be observed and retried without changing business policy?

Use the lightest separation that answers these questions. A small CRUD use case may remain one explicit application function; it does not need one class or file per layer.

## Pragmatic Capability Slice

Do not force every capability to contain every layer. Start with the minimum owned shape and split only when a responsibility becomes meaningful.

Small use case:

```text
recipes/
  route-or-ui-entry
  create-recipe-use-case
```

The entrypoint owns transport/presentation mapping. The use case owns authorization, orchestration, transaction choice, and direct persistence when the query is simple and capability-local.

Evolved use case:

```text
recipes/
  presentation/
  application/
  domain/
  data/
  infrastructure/
```

Add the relevant owner-local layer only when:

- durable policy needs independent ownership or reuse
- query/persistence complexity deserves an explicit data boundary
- vendor mechanisms need isolation
- multiple entrypoints must share one application workflow

Do not create empty layers, one-method forwarding classes, repository interfaces over trivial ORM calls, or separate models that only rename identical fields.

## Delivery-Agnostic Ownership

Apply the same ownership rules regardless of framework, transport, runtime, or interface.

- **Delivery entrypoints** receive input, validate transport shape, invoke a capability use case, and map output.
- **Interaction state** owns transient user/request lifecycle state, including loading, optimistic presentation, rollback, and reconciliation.
- **Application use cases** own workflow orchestration, authoritative authorization, transaction boundaries, and side-effect coordination.
- **Domain/business policy** owns durable rules, calculations, and valid state transitions.
- **Data access** owns query shape, persistence mapping, and datastore interaction.
- **Infrastructure adapters** own vendor and runtime mechanisms.
- **Middleware and guards** own broad edge concerns such as identity, authentication context, request correlation, security headers, rate limits, and transport validation.

Keep capability-specific policy and workflow decisions in the owning application/domain boundary. Keep delivery entrypoints and middleware focused on their narrow edge responsibilities.

Framework constructs are mechanisms, not automatic architecture owners. A controller, route, resolver, hook, command handler, job, or script should own only the responsibility assigned to it by the capability design.

## Presentation Layer

Owns:

- transport/delivery concerns: HTTP, GraphQL, RPC, CLI, UI, message entrypoints
- request shape validation
- mapping input to application commands/queries
- response/view formatting

Should:

- keep controllers, handlers, and route modules thin
- keep UI components focused on rendering and interaction
- enforce authn/authz server-side even if UI hides actions
- delegate real workflow/state transitions inward
- depend on capability-level commands/queries rather than orchestrating direct datastore CRUD for one journey

Should not:

- own durable business policy
- call low-level infrastructure/database directly
- collapse DTO, API, domain, and persistence types into one shape when differences matter
- coordinate multi-step durable workflows through client-side request chains

## Application Layer

Owns:

- use cases and workflow orchestration
- transaction boundaries
- authorization decisions
- idempotency and side-effect coordination
- calls to domain and infrastructure through deliberate boundaries

Should:

- expose clear command/query paths where helpful
- define transaction boundaries around consistency-sensitive work
- choose and expose conflict, ordering, freshness, and partial-failure semantics where the use case needs them
- coordinate retries, background handoff, and side effects deliberately
- compress a complete user/system journey behind a narrow capability boundary when it owns one transaction or workflow

Should not:

- become a god service owning transport, policy, persistence, and vendor details
- launch background work without delivery guarantees where correctness matters
- parallelize work that races on shared mutable state or causes confusing partial failure
- become a forwarding layer that adds indirection without owning orchestration, authorization, transactions, or policy coordination

## Domain / Business Layer

Owns:

- invariants, policies, calculations, business language, state transitions

Use:

- value objects for constrained concepts
- entities/aggregates where behavior and invariants belong with the model
- domain services for business policies spanning entities
- policy/specification objects for complex reusable decisions

Should not:

- depend on frameworks, ORMs, request objects, or vendor SDKs
- hide simple CRUD behind needless modeling
- use domain events as vague substitutes for ordinary method calls

## Data Layer

Owns:

- schema, migrations, indexing, querying, persistence mapping, retention, partitioning, read/write access patterns

Should:

- enforce true invariants with datastore constraints where possible
- use repositories/query services only where they protect meaningful boundaries
- design indexes from real query patterns
- use cursor pagination for large mutable lists
- use deterministic ordering for pagination and conflict-aware writes where concurrent changes matter
- keep retention, archival, and purge strategies explicit when data volume matters

Should not:

- leak persistence models into APIs/domain by default
- let every module query every table directly
- hide important query behavior behind generic repositories
- use cache to mask poor schema/indexing

## Infrastructure Layer

Owns:

- mechanisms for databases, queues, caches, search, object storage, email, third-party APIs, observability, and config

Should:

- map vendor models/errors at the adapter edge
- use timeouts on outbound calls
- retry only with backoff/jitter and idempotency safeguards
- respect cancellation/deadlines and bound concurrency/resource use where supported and material
- externalize config/secrets
- isolate vendor SDKs from inner policy layers

Should not:

- decide business rules
- leak vendor exceptions/types into domain/application logic
- hide failure behavior so much it becomes opaque

## API / Integration Layer

Owns:

- external contracts, endpoint semantics, event schemas, webhook payloads, versioning, error models, pagination, filtering, rate limits, compatibility

Should:

- use deliberate boundary DTOs
- keep error taxonomy consistent
- define authn/authz at contract boundary
- use idempotency for retried unsafe operations
- verify webhook signatures, timestamps, and replay protection
- evolve contracts additively where possible

Should not:

- expose table/ORM shapes
- vary semantics arbitrarily across endpoints
- emit vague events with no ownership or evolution policy
