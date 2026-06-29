---
title: Public API Response Versioning for Customer Lookup
scope: public-api-versioning-blocked
status: design-ready
repo_root: /repo
change_class: integration
risk_level: high
owner: api-platform
reviewers: api-lead, support-lead
approvers: engineering-manager
implementation_owner: api-platform
operations_owner: sre-team
last_updated: 2026-04-22
---

# Design Document: Public API Response Versioning for Customer Lookup

## Summary
- Introduce versioned customer lookup responses so the API can evolve a nested address shape.
- The change matters because downstream clients need richer address data.
- The design remains blocked until external consumer compatibility requirements are confirmed.

## Scope Statement
- Covers the public customer lookup endpoint, serializer layer, consumer communication, and rollout controls.

## Original Plan Alignment Audit
- Original plan or prompt excerpts reviewed: introduce versioned customer lookup responses without breaking existing consumers.
- Explicit requirements confirmed from the original plan: preserve old response shape until public-contract compatibility is confirmed.
- Plan items excluded or deferred, with reason: implementation is deferred until the critical public-contract decision is resolved.
- Gaps, contradictions, or stale assumptions found: the consumer compatibility window remains unresolved.
- Upstream artifact changes required before continuing: resolve DES-001 before implementation tasks can be authored.
- Architecture standards reviewed: public contract ownership, compatibility, rollout, observability, and supportability.
- Agent judgment or justified architecture-standard deviations: none.
- Post-design audit outcome: design is intentionally blocked until consumer compatibility is confirmed.

## Repository Discovery Summary

### Repo Root
- `/repo`

### Repo-Specific Profile and House Patterns
- `.spec/_shared/repo-profile.md` states that public API changes require compatibility windows and support coordination.

### Entry Points and Execution Path
- `src/api/customers/routes.ts`
- `src/api/customers/serializers.ts`
- `src/contracts/public/customer.ts`

### Confirmed Code and Runtime Facts
- Public endpoints are contract-tested under `tests/contracts/public/`.
- Existing version negotiation uses the `X-Api-Version` header.

### Related Code and Pattern Inventory
- `src/api/orders/serializers.ts` already uses versioned serializers.

### Adjacent Pattern Comparison
- Preferred existing pattern: header-based version negotiation.
- The design intends to conform.

### Blast Radius Review
- Client SDKs, support documentation, and contract tests all consume the current shape.

### Recent Related Repository History
- A previous public payload change required a quick rollback because one SDK consumer was missed.

### Impacted Boundaries and Adjacent Systems
- External clients, SDK maintainers, support playbooks, and API monitoring.

### Data, Contracts, and Config Surfaces
- Public JSON payload shape and version header handling.

### Existing Tests and Operational Signals
- `tests/contracts/public/customer_lookup.test.ts`
- API error-rate dashboard for customer lookup.

### Static Analyzer and Audit Evidence
- Relevant audit/review artifacts: not applicable for this exemplar.
- Analyzer commands, modes, configs, baselines, suppressions, allowlists, and thresholds: not applicable.
- Duplication, health, module-budget, boundary, or coverage signals that influence the design: no analyzer-backed signals available.
- Gate vs advisory inventory distinction: not applicable.
- For each analyzer result: not applicable.
- CI parity: not applicable.
- Accepted-debt register: none.

## Problem Statement and Context
- Consumers need structured address fields instead of a flattened string.
- If the change is wrong, external clients break.

## Current-State Analysis
- The endpoint returns a flat `address_line` field.
- Serializer logic is not yet version-aware.

## Target-State Architecture
- Intended owner for each durable invariant: the public serializer owns response shape selection; contract tests own compatibility proof; support owns consumer communication.
- Dependency direction and public surfaces: version negotiation stays at the API boundary and does not leak into persistence or domain logic.
- Contracts, data ownership, async/reliability, and operational ownership: the public JSON payload remains versioned and contract-tested before rollout.
- What must stop happening after the transition: public response shape changes must not ship as unversioned in-place mutations.
- Fitness functions that prove the target state is holding: old/new contract tests, version-usage telemetry, and support signoff.

## Goals
- Support a richer address payload without breaking existing consumers.

## Non-Goals
- Redesigning unrelated customer fields.

## Confirmed Facts
- Version negotiation is already supported elsewhere in the repo.

## Assumptions
- Existing consumers can tolerate a one-release compatibility window.

## Open Questions
- Whether the SDK auto-updates response parsing.

## Decision Needed
- [critical][public-contract] Confirm whether any external consumer requires the old response shape beyond one release window.

## Proposed Design

### Solution Overview
- Use header-based version negotiation and serializer branching, but defer execution until the consumer compatibility window is confirmed.

### End-to-End Flow
- Client sends version header.
- Router selects serializer branch.
- Support and dashboards track version uptake.

### Component and Module Changes

#### UI or Client
- Not applicable.

#### API or Application Layer
- Versioned serializer branching in the customer lookup route.

#### Domain or Business Logic
- No business rule changes.

#### Data Model and Persistence
- No persistence changes.

#### Integrations, Events, or Background Jobs
- External client integrations consume the public contract.

#### Security and Permissions
- No auth boundary change.

#### Performance and Scalability
- Negligible serializer overhead.

#### Observability and Operations
- Add version-usage monitoring and support guidance.

## Impacted Surfaces Matrix
- UI: Not applicable.
- API: `src/api/customers/routes.ts`, `src/api/customers/serializers.ts`
- Domain logic: Not applicable.
- Persistence: Not applicable.
- Integrations: external clients and SDKs
- Auth: Not impacted.
- Infra: API gateway header passthrough
- Telemetry: version-usage dashboard
- Tests: contract tests
- Docs: public API changelog and support notes

## Change Impact Map
- Direct impact: public serializer and contract tests.
- Indirect impact: client SDKs and support workflows.
- Unchanged but risk-adjacent areas: auth, caching, and persistence.

## Invariants and Forbidden Outcomes
- Existing clients must keep working during the compatibility window.
- The endpoint must not silently change shape for clients pinned to the old version.

## Compatibility Matrix
- Public API: Blocked pending consumer decision.
- Internal API: Not applicable.
- Data schema: Not applicable.
- Events: Not applicable.
- Cache keys: Not applicable.
- Config: Version negotiation header routing.
- External consumers: High impact.
- Rollback compatibility: Version branching permits rollback if the old path remains.

## Contract Examples and Before/After Payloads
- Request examples: `GET /customers/123` with `X-Api-Version: 2026-10`
- Response examples: Old flat string vs new structured address object.
- Event or message examples: Not applicable.
- Before/after comparisons: The `address_line` field becomes an `address` object for new-version callers.

## Cross-Cutting Applicability Matrix
- Security: Not applicable. No auth change.
- Privacy: Covered. Customer data surface is unchanged in sensitivity.
- Performance: Covered. Serializer overhead only.
- Resilience: Covered. Old version remains available during rollout.
- Migration: Not applicable. No stored data change.
- Observability: Covered. Version-usage telemetry required.
- Supportability: Covered. Support must know which version a client uses.
- Backward compatibility: Covered and currently blocked on confirmation.

## Success Metrics and Numeric NFR Targets
- Latency targets: p95 endpoint latency increase below 5 ms.
- Throughput or concurrency targets: No change required.
- Error-rate or availability targets: No increase above 0.1 percentage points during rollout.
- Timeout, retry, or queue-depth limits: Not applicable.

## Decision Register

### DES-001: Use header-based API version negotiation
- Context: The repo already versions selected public payloads via request headers.
- Decision: Reuse the existing `X-Api-Version` pattern.
- Rationale: This minimizes implementation novelty and consumer confusion.
- Tradeoffs: Version handling logic becomes more explicit in route serialization.
- Affected surfaces: routes, serializers, client docs

## Risk Register
- Risk:
  - Impact: External clients break if compatibility assumptions are wrong.
  - Mitigation: Block implementation until consumer confirmation is documented.
  - Residual risk: Medium even after confirmation.

## Test Impact Matrix
- Existing tests to update: `tests/contracts/public/customer_lookup.test.ts`
- New tests required: version negotiation contract tests
- Compatibility tests: old-version and new-version clients side by side
- Rollback-safety tests: old serializer path remains available

## Validation Strategy
- Contract validation, compatibility validation, and staged rollout checks

## Post-Design Review
- Original plan coverage review: the design covers version negotiation, compatibility blocking, support coordination, and rollout controls.
- Repository evidence review: the design uses existing public route, serializer, contract test, and version-header surfaces.
- Architecture standards review: public contract ownership, compatibility, observability, and rollback were reviewed.
- Requirements readiness: partially ready; implementation remains blocked by DES-001.
- Required upstream changes before requirements authoring: none for stable blocking requirements.

## Rollout, Abort, and Reversal
- Rollout is blocked until the public contract decision is resolved.

## Forbidden Shortcuts and Guardrails
- Do not change the payload shape in place without version negotiation.
- Do not ship before the consumer inventory is confirmed.

## Alternatives Considered
- Alternative:
  - Why rejected: In-place contract mutation was rejected because the blast radius is too high.

## Residual Risks
- External consumer behavior remains the dominant risk.
