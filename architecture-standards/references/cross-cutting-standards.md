# Cross-Cutting Standards

Use this when checking security, performance, reliability, observability, testability, or cost.

## Contents

- security and privacy
- performance, scale, and cross-layer semantics
- reliability, resilience, observability, and operability
- maintainability, testability, efficiency, and cost

## Security And Privacy

- Enforce authentication and authorization server-side.
- Prefer least privilege for users, services, jobs, and infrastructure roles.
- Default deny where risk justifies it.
- Use RBAC for broad role access; add ABAC/relationship policies when access depends on resource attributes, ownership, hierarchy, or tenant context.
- Validate input shape at the edge; enforce business rules inward.
- Encode/sanitize output where injection risk exists.
- Keep secrets out of code, logs, analytics, and client bundles.
- Encrypt sensitive data where risk/compliance requires it.
- Minimize sensitive data collection and retention.
- Make tenancy isolation explicit in queries, cache keys, jobs, and mutations.
- Treat dependencies, build artifacts, deployment pipelines, and third-party code as trust boundaries; add provenance, pinning, scanning, or update controls where risk justifies them.

Common failures:

- authorization only in frontend
- scattered inconsistent permission checks
- tenant scoping by convention instead of guardrails
- sensitive data in logs or analytics

## Performance And Scale

Treat these as context-dependent practices. Select them from measured behavior, credible growth expectations, and the journey's correctness needs; do not apply every optimization to every system.

- Define end-to-end latency, throughput, payload, query/fan-out, concurrency, freshness, and cost expectations for material paths.
- Measure complete journeys and attribute cost across delivery, application, data, infrastructure, and external dependencies.
- Prefer capability-shaped commands and queries when they reduce chatty orchestration or preserve one workflow, while keeping payloads and internal work bounded.
- Remove waterfall and N+1 patterns before adding caches.
- Parallelize only independent work, with bounded concurrency and understood partial-failure behavior.
- Batch reads/writes when it materially reduces roundtrips without obscuring ownership or correctness.
- Use projections, partial selects, deterministic pagination, and streaming when data size or access patterns justify them.
- Consider cursor pagination for large mutable datasets; use simpler pagination when its tradeoffs are acceptable.
- Consider async handoff for slow, bursty, retryable, or non-user-critical work; keep work inline when immediate completion or simplicity matters more.
- Consider read models or caches when measured read patterns justify them. Define source of truth, freshness, invalidation/rebuild, TTL, fallback, reconciliation, and operational ownership.
- Bound candidate pools, page sizes, fan-out, retries, queue concurrency, memory use, and work per request/job where growth could otherwise make cost unbounded.
- Design indexes and query shapes from real access patterns and inspect execution behavior for material paths.
- Measure hot paths before complex optimization and re-measure after meaningful changes.

Common failures:

- cache without invalidation
- unbounded page sizes or in-memory full dataset loads
- excessive fan-out or pool exhaustion
- optimizing theoretical hot spots while ignoring measured bottlenecks
- reducing client request count by hiding unbounded or repeatedly executed server work

## Cross-Layer Semantics

- Keep contracts narrow and explicit enough to preserve meaning across layers.
- Map models and errors where semantics differ; avoid ceremonial mapping where they do not.
- Propagate required identity, tenant/scope, correlation, deadline/cancellation, and idempotency context deliberately.
- Define transaction, consistency, ordering, conflict, freshness, and partial-result expectations at the owning use case.
- Keep side-effect timing and delivery semantics visible.
- Avoid hidden database/network work, silent retries, swallowed failures, and implicit global context.
- Make time, randomness, identity generation, and external effects injectable or controllable when deterministic behavior matters.

## Reliability And Resilience

- Time out external calls.
- Propagate cancellation/deadlines and release resources promptly where the runtime supports it and the path justifies it.
- Retry only transient failures with backoff and jitter.
- Make retried operations idempotent.
- Protect against duplicate delivery and partial failure.
- Use graceful degradation when business semantics allow it.
- Use backpressure/admission control when the system can be overwhelmed.
- Define connection, worker, queue, and memory limits where resource exhaustion is credible.
- Keep state changes and emitted side effects consistent through outbox/transactional patterns where needed.
- Use compensating actions when distributed work cannot be atomic.
- Support graceful startup/shutdown and draining when abrupt lifecycle changes could lose or corrupt work.
- Define availability and recovery objectives, backup/restore or rebuild paths, and recovery tests where loss or prolonged outage has meaningful consequences.
- Design mixed-version rollout, migration, and rollback compatibility when a change cannot be deployed atomically.

Common failures:

- aggressive/infinite retries
- side effects before durable commit
- silent divergence after partial failure
- async work without status visibility or dead-letter recovery

## Observability And Operability

- Emit structured logs with stable keys.
- Capture metrics for traffic, errors, latency, saturation, and business-critical outcomes.
- Trace critical paths across service/job boundaries.
- Carry correlation IDs across requests and background work.
- Define health/readiness/dependency checks where needed.
- Alert on user/business impact, not noisy raw thresholds.
- Make operational ownership visible for critical systems.
- Prefer feature flags for sensitive rollout/rollback.

Common failures:

- verbose but unqueryable logs
- metrics with no actionability
- critical background flows with no visibility
- backups or rollback claims that have never been exercised

## Maintainability And Testability

- Keep responsibilities crisp and public surfaces narrow.
- Put core logic where it can be tested cheaply and deterministically.
- Use unit tests for rules, integration tests for boundaries, contract tests for integrations, and e2e tests for critical journeys.
- Use architecture tests/lint rules when boundaries matter and are repeatedly violated.
- Name modules after capabilities, not generic technical buckets.
- Prefer explicit control flow over hidden framework magic when correctness matters.

Common failures:

- too many e2e tests for logic that should be unit tested
- shared test helpers hiding architecture problems
- folder layering without dependency layering

## Efficiency And Cost

Treat cost as an end-to-end architecture attribute, independent of vendor and architecture style. Load `cost-efficient-architecture.md` for material cost design or review.

- Use infrastructure and operational complexity proportional to the problem.
- Attribute cost to useful journeys, capabilities, environments, and owners where practical.
- Understand the complete cost curve: fixed baseline, executions, work per execution, fan-out/reruns/retries, retained/derived data, transfer, third parties, and operational burden.
- Avoid idle work, service sprawl, duplicated storage, broad invalidation, unbounded fan-out, and chatty internal APIs unless their value justifies their total cost.
- Design archival, retention, purge, cleanup, and rebuild before large datasets accumulate.
- Compare architecture options using total cost of ownership rather than assuming managed/self-hosted, monolith/services, sync/async, normalized/denormalized, or push/pull is inherently cheaper.
- Favor simpler operations unless complexity buys a clear correctness, experience, reliability, scale, or total-cost benefit.

Common failures:

- splitting services before workload/team needs justify it
- retaining all historical data forever
- internal call chains adding latency/cost without value
- usage-priced work multiplied by polling, subscriptions, reconnects, retries, invalidation, or no-op writes
- optimizing one provider line item while increasing complete-system or engineering cost
- no evidence connecting spend to product journeys or architecture decisions
