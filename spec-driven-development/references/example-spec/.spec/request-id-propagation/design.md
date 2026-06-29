---
title: Request ID Propagation Across API and Worker Flows
scope: request-id-propagation
status: implementation-ready
repo_root: /repo
change_class: platform
risk_level: medium
owner: platform-team
reviewers: api-lead, sre-lead
approvers: platform-director
implementation_owner: platform-team
operations_owner: sre-team
last_updated: 2026-04-22
---

# Design Document: Request ID Propagation Across API and Worker Flows

## Summary
- Introduce consistent request ID generation and propagation from inbound HTTP requests into application logs, queue messages, and worker logs.
- This improves debugging and incident response without changing external behavior.
- The design enables traceable request journeys across synchronous and asynchronous boundaries.

## Scope Statement
- This spec governs request-context propagation through the API gateway, application services, queue publishing, and worker execution.
- It does not add distributed tracing vendors or redesign logging formats beyond the request ID field.

## Original Plan Alignment Audit
- Original plan or prompt excerpts reviewed: add request ID propagation from API requests into worker logs.
- Explicit requirements confirmed from the original plan: preserve public API behavior, keep queue compatibility, and improve support correlation.
- Plan items excluded or deferred, with reason: distributed tracing vendor adoption is excluded because the requested outcome only needs request ID correlation.
- Gaps, contradictions, or stale assumptions found: none.
- Upstream artifact changes required before continuing: none.
- Architecture standards reviewed: middleware ownership, internal contract compatibility, async boundary behavior, observability, rollback.
- Agent judgment or justified architecture-standard deviations: none.
- Post-design audit outcome: design remains aligned with the request and architecture standards.

## Repository Discovery Summary

### Repo Root
- `/repo`

### Repo-Specific Profile and House Patterns
- `.spec/_shared/repo-profile.md` states that request-scoped metadata should be introduced through middleware rather than ad hoc route logic.
- The repo profile also prefers extending the existing structured logger instead of introducing a second logging facade.

### Entry Points and Execution Path
- `src/server/middleware/auth.ts`
- `src/server/routes/orders.ts`
- `src/server/services/order-service.ts`
- `src/queues/publish-order-events.ts`
- `src/workers/order-events/processor.ts`

### Confirmed Code and Runtime Facts
- `src/lib/logger.ts` already accepts structured metadata objects.
- `src/queues/publish-order-events.ts` publishes JSON envelopes to the worker queue.
- `tests/integration/orders/create-order.test.ts` exercises the API-to-worker path.

### Related Code and Pattern Inventory
- `src/server/middleware/request-timing.ts` already injects per-request metadata into `res.locals`.
- `src/workers/shared/job-context.ts` already normalizes worker metadata before calling handlers.
- The design reuses the existing structured logger and middleware style rather than introducing a new request context framework.

### Adjacent Pattern Comparison
- Preferred existing pattern: request-scoped metadata enters through middleware and is forwarded using existing logger helpers.
- Why it applies: this change is another request-scoped metadata concern and should follow the same ingress pattern.
- Conformance: the proposal follows the middleware-plus-logger pattern.
- Divergence: none.

### Blast Radius Review
- Shared utilities used by the target code: `src/lib/logger.ts`, `src/workers/shared/job-context.ts`.
- Callers of the target code: API route handlers and queue publishers.
- Imports into and from the target code: routes depend on middleware ordering; workers depend on queue envelope shape.
- Sibling modules in the same domain: request timing middleware and worker context hydration.
- Feature flags, config, or env vars affecting the path: none.

### Recent Related Repository History
- A recent logging cleanup standardized JSON field names, so the design preserves `snake_case` metadata.
- A prior queue-envelope change required backward compatibility during rollout, so this design keeps `request_id` optional.

### Impacted Boundaries and Adjacent Systems
- API handlers consuming `res.locals`
- queue producers and consumers exchanging JSON envelopes
- log pipelines and support workflows that search by structured fields

### Data, Contracts, and Config Surfaces
- internal queue message envelope
- log field schema for `request_id`
- no external API contract change

### Existing Tests and Operational Signals
- `tests/integration/orders/create-order.test.ts`
- `tests/workers/order-events/processor.test.ts`
- existing Kibana searches rely on structured JSON log fields from `src/lib/logger.ts`

### Static Analyzer and Audit Evidence
- Relevant audit/review artifacts: not applicable for this exemplar.
- Analyzer commands, modes, configs, baselines, suppressions, allowlists, and thresholds: not applicable.
- Duplication, health, module-budget, boundary, or coverage signals that influence the design: no analyzer-backed signals available.
- Gate vs advisory inventory distinction: not applicable.
- For each analyzer result: not applicable.
- CI parity: not applicable.
- Accepted-debt register: none.

## Problem Statement and Context
- A single user action currently produces multiple log lines that cannot be reliably correlated across API and worker boundaries.
- Incident response requires manual timestamp and payload correlation.
- If the change is wrong, worker processing could lose context or queue payload compatibility.

## Current-State Analysis
- API requests log locally with request metadata, but background jobs lose that context.
- Queue envelopes do not carry a stable correlation field.
- Worker logs include job IDs but not the original inbound request identifier.

## Target-State Architecture
- Intended owner for each durable invariant: API middleware owns request ID creation; queue publishers own envelope propagation; worker context owns log hydration.
- Dependency direction and public surfaces: request ID metadata flows from API boundary to internal queue envelope to worker logging without domain logic depending on transport details.
- Contracts, data ownership, async/reliability, and operational ownership: queue envelopes carry an optional internal `request_id`; SRE owns dashboard/support verification.
- What must stop happening after the transition: worker logs must not require manual timestamp/payload matching for API-originated jobs.
- Fitness functions that prove the target state is holding: middleware tests, queue envelope integration tests, worker compatibility tests, and staging log-search verification.

## Goals
- Propagate one stable request ID from ingress to worker completion.
- Preserve current queue behavior and logging style.
- Improve debugging without changing public API behavior.

## Non-Goals
- Adding a tracing vendor
- Renaming the entire log schema
- Correlating historical jobs that predate rollout

## Confirmed Facts
- The structured logger accepts arbitrary metadata keys.
- Queue envelopes are versionless internal JSON payloads.
- Existing middleware patterns already enrich request-local metadata.

## Assumptions
- Internal queue consumers can safely ignore unknown envelope fields.

## Open Questions
- None.

## Decision Needed
- None.

## Proposed Design

### Solution Overview
- Generate or accept a request ID at the API boundary, attach it to request-local context, include it in queue envelopes, and hydrate worker log context from that field.

### Transition Plan From Current State
- Containment gate: worker compatibility for missing `request_id` lands before publishers emit the field.
- Safe implementation slices: middleware, optional queue field, worker hydration, support verification.
- Old bypasses or compatibility paths to remove: none.
- Baselines, suppressions, allowlists, or module-budget caps that remain temporarily: none.
- Revisit trigger for each accepted exception: not applicable.

### End-to-End Flow
- API middleware resolves `request_id`.
- Route and service logs emit `request_id`.
- Queue publishers include `request_id` in the job envelope.
- Worker context loader reads `request_id` and injects it into worker logs.

### Component and Module Changes

#### UI or Client
- Not applicable.

#### API or Application Layer
- Add request ID middleware near the existing request timing middleware.
- Ensure route handlers and service logs pass the value through existing logger helpers.

#### Domain or Business Logic
- No domain rule changes.

#### Data Model and Persistence
- No database changes.

#### Integrations, Events, or Background Jobs
- Extend internal queue envelopes with `request_id`.
- Update worker context hydration to read the new field.

#### Security and Permissions
- Request IDs are opaque correlation values, not secrets or authorization inputs.

#### Performance and Scalability
- Negligible payload and logging overhead.

#### Observability and Operations
- Add dashboard filter examples for `request_id`.

## Impacted Surfaces Matrix
- UI: Not impacted.
- API: `src/server/middleware`, `src/server/routes`, `src/server/services`
- Domain logic: Not impacted.
- Persistence: Not impacted.
- Integrations: queue envelope producers and consumers
- Auth: no auth boundary change
- Infra: log search dashboards
- Telemetry: structured log field coverage
- Tests: API integration and worker tests
- Docs: support debugging notes

## Change Impact Map
- Direct impact: inbound middleware, queue publishers, worker context hydration, support logging guidance.
- Indirect impact: dashboard filters and incident response workflows that rely on structured log fields.
- Unchanged but risk-adjacent areas: authorization logic, business rules, and existing queue retry semantics.

## Invariants and Forbidden Outcomes
- Existing requests must continue to succeed without a client-supplied request ID.
- Queue consumers must not fail when `request_id` is missing on pre-rollout jobs.
- `request_id` must never be used for authorization or business decisions.

## Compatibility Matrix
- Public API: Compatible. Optional inbound header only.
- Internal API: Compatible. Existing logger metadata pattern reused.
- Data schema: Not applicable.
- Events: Compatible. Added optional internal field.
- Cache keys: Not applicable.
- Config: Not applicable.
- External consumers: Not applicable.
- Rollback compatibility: Rollback is safe because workers treat `request_id` as optional.

## Contract Examples and Before/After Payloads
- Request examples: `X-Request-Id: a3f2c5fd-2b1a-4d2a-80a8-51ab2e2d2e01`
- Response examples: Not applicable. No response payload change.
- Event or message examples:
  - Before: `{ "event": "order.created", "job_id": "job-123", "payload": { ... } }`
  - After: `{ "event": "order.created", "job_id": "job-123", "request_id": "a3f2c5fd-2b1a-4d2a-80a8-51ab2e2d2e01", "payload": { ... } }`
- Before/after comparisons: queue messages gain one optional field; public HTTP payloads stay unchanged.

## Cross-Cutting Applicability Matrix
- Security: Covered. The field is non-authoritative and non-secret.
- Privacy: Covered. No user data added.
- Performance: Covered. Negligible overhead.
- Resilience: Covered. Missing field is tolerated.
- Migration: Not applicable. No persisted data migration.
- Observability: Covered. Log correlation improves.
- Supportability: Covered. Support can search by one field.
- Backward compatibility: Covered. Internal field is optional.

## Success Metrics and Numeric NFR Targets
- Latency targets: Added middleware and logging metadata must keep p95 request latency change below 2 ms.
- Throughput or concurrency targets: Queue consumers must sustain existing worker concurrency without observable throughput degradation.
- Error-rate or availability targets: No increase in worker job failure rate above 0.1 percentage points during rollout.
- Timeout, retry, or queue-depth limits: Existing job timeout and retry values remain unchanged.

## Decision Register

### DES-001: Resolve request ID at the API boundary
- Context: Correlation is only reliable if one value is established at ingress.
- Decision: Add middleware that accepts an inbound request ID header or generates one.
- Rationale: This reuses the existing middleware pattern and keeps handlers simple.
- Tradeoffs: Middleware order becomes slightly more important.
- Affected surfaces: `src/server/middleware`, `src/server/routes`

### DES-002: Propagate request ID through internal queue envelopes
- Context: Worker logs need the same correlation value used by the API layer.
- Decision: Add an optional `request_id` field to internal queue envelopes.
- Rationale: This is the narrowest change that spans async boundaries.
- Tradeoffs: Queue envelope schema grows slightly.
- Affected surfaces: `src/queues`, `src/workers`

### DES-003: Keep request ID optional for backward compatibility
- Context: Pre-rollout jobs and internal callers may not provide the field immediately.
- Decision: Treat `request_id` as optional everywhere except freshly handled API requests.
- Rationale: This allows staged rollout and safe rollback.
- Tradeoffs: Some logs remain uncorrelated until rollout completes.
- Affected surfaces: queue consumers, worker context, support docs

## Risk Register
- Risk:
  - Impact: Worker consumers fail on older payloads.
  - Mitigation: Treat the field as optional and cover the missing-field path in tests.
  - Residual risk: Low.

## Test Impact Matrix
- Existing tests to update: `tests/integration/orders/create-order.test.ts`, `tests/workers/order-events/processor.test.ts`
- New tests required: middleware unit coverage for malformed and missing headers.
- Compatibility tests: worker processing of envelopes without `request_id`.
- Rollback-safety tests: publisher rollback while workers continue to accept both shapes.

## Validation Strategy
- Unit validation for middleware request ID resolution
- Integration validation for API-to-queue propagation
- End-to-end validation for API log to worker log correlation
- Migration or rollback validation not applicable
- Performance validation through smoke testing log and payload overhead
- Operational validation through dashboard searches in staging

## Post-Design Review
- Original plan coverage review: the design covers ingress, queue propagation, worker logging, compatibility, and support verification.
- Repository evidence review: the design uses existing middleware, logger, queue, worker, and test surfaces.
- Architecture standards review: ownership, internal contract compatibility, async reliability, and observability were reviewed.
- Requirements readiness: ready.
- Required upstream changes before requirements authoring: none.

## Rollout, Abort, and Reversal
- Roll out worker compatibility first, then queue publisher changes, then API ingress middleware.
- No feature flag required because the compatibility order is safe.
- Abort if workers show schema handling errors or logging failures.
- Roll back publishers and middleware independently if needed.
- Post-deploy checks: confirm a sampled request ID appears in API and worker logs.

## Forbidden Shortcuts and Guardrails
- Do not bypass the existing middleware stack by generating request IDs inside routes.
- Do not make `request_id` mandatory in queue consumers before compatibility lands.
- Do not use `request_id` for authorization, tenancy, or business decisions.

## Alternatives Considered
- Alternative:
  - Why rejected: Full distributed tracing instrumentation was rejected because it is heavier than needed for the current problem.

## Residual Risks
- Historical jobs remain uncorrelated until they drain.
