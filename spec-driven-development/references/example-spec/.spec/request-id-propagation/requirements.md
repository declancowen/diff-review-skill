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

# Requirements Document: Request ID Propagation Across API and Worker Flows

## Source Artifacts
- `.spec/request-id-propagation/design.md`

## Scope Statement
- This document defines the behavioral and operational requirements for request ID propagation across API and worker boundaries.

## Upstream Alignment Audit
- Original plan requirements reviewed: propagate request IDs across API and worker logs while preserving compatibility.
- Design decisions reviewed: DES-001, DES-002, DES-003.
- Repository evidence and current tests reviewed: middleware, logger, queue publisher, worker context, and integration/worker test surfaces named in `design.md`.
- Architecture standards implications reviewed: middleware ownership, internal contract compatibility, async boundary behavior, observability, rollback.
- Requirements added, changed, or rejected during audit: none.
- Design updates required before continuing: none.
- Agent judgment or justified architecture-standard deviations: none.
- Post-requirements audit outcome: requirements remain aligned with the design and original plan.

## Cross-Cutting Coverage
- Security: Covered by `REQ-SEC-001`
- Privacy: Covered by `REQ-SEC-001`
- Performance: Covered by `REQ-NFR-001`
- Resilience: Covered by `REQ-NFR-002`
- Migration: Not applicable because no persisted data migration occurs
- Observability: Covered by `REQ-OPS-001`
- Supportability: Covered by `REQ-OPS-001`
- Backward compatibility: Covered by `REQ-DATA-001`

## Requirements

### REQ-FUNC-001: Resolve a stable request ID at request ingress
Source Design Decisions:
- DES-001

Priority: High

Rationale:
- Correlation must begin at the inbound request boundary to remain stable across downstream work.

Requirement:
- THE system SHALL resolve one stable `request_id` for each inbound API request by accepting a client-supplied value when valid or generating one when absent.

Verification Method:
- Unit and integration verification of middleware behavior

Risk if Unmet:
- Logs from one user action cannot be correlated reliably.

Acceptance Criteria
1. WHEN an inbound request includes a valid request ID header, THE system SHALL reuse that value.
2. WHEN an inbound request does not include a request ID header, THE system SHALL generate one before route handling begins.
3. THEN route and service logs emitted during request handling SHALL include the resolved `request_id`.

Negative Cases
1. WHEN an inbound request ID header is malformed, THEN THE system SHALL generate a safe replacement value instead of propagating the malformed one.

### REQ-DATA-001: Preserve backward compatibility for internal queue envelopes
Source Design Decisions:
- DES-002
- DES-003

Priority: High

Rationale:
- Queue producers and consumers must evolve without breaking in-flight or pre-rollout jobs.

Requirement:
- THE system SHALL add `request_id` to internal queue envelopes as an optional field and SHALL preserve worker compatibility with envelopes that do not include it.

Verification Method:
- Integration and worker compatibility verification

Risk if Unmet:
- Worker failures or dropped jobs during rollout or rollback.

Acceptance Criteria
1. WHEN a new queue message is published from an API-originated flow, THE envelope SHALL include `request_id`.
2. IF a worker receives an older envelope without `request_id`, THEN the worker SHALL continue processing successfully.
3. THEN worker logs SHALL include `request_id` when present and continue logging safely when absent.

Negative Cases
1. WHEN a worker receives an envelope with an unexpected non-string `request_id`, THEN it SHALL ignore the value and continue processing without failing the job.

### REQ-NFR-001: Keep propagation overhead operationally negligible
Source Design Decisions:
- DES-001
- DES-002

Priority: Medium

Rationale:
- Correlation should improve debugging without materially increasing request or worker cost.

Requirement:
- THE system SHALL add request ID propagation with negligible payload and logging overhead relative to current behavior.

Target Metrics:
- p95 request latency increase SHALL remain below 2 ms, and worker failure rate SHALL not increase by more than 0.1 percentage points.

Verification Method:
- Smoke and performance verification in staging

Risk if Unmet:
- Debugging improvements come at the cost of hot-path performance.

Acceptance Criteria
1. WHEN request ID propagation is enabled, THEN request handling behavior SHALL remain functionally unchanged.
2. WHEN worker processing includes request ID hydration, THEN job completion behavior SHALL remain functionally unchanged.

Negative Cases
1. WHEN log enrichment fails, THEN core request or worker processing SHALL continue without aborting the business flow.

### REQ-SEC-001: Prevent request ID from becoming a trust or data boundary
Source Design Decisions:
- DES-001
- DES-003

Priority: High

Rationale:
- Correlation metadata must never influence authorization or expose sensitive data.

Requirement:
- THE system SHALL treat `request_id` as opaque non-authoritative metadata and SHALL not use it for authorization, tenancy, or business decisions.

Verification Method:
- Code review and negative-path verification

Risk if Unmet:
- Security or correctness issues caused by user-controlled metadata.

Acceptance Criteria
1. WHEN `request_id` is present, THEN it SHALL only be used for logging and correlation.
2. THEN authorization and business logic outcomes SHALL remain independent of `request_id`.

Negative Cases
1. WHEN an attacker supplies a forged request ID, THEN the system SHALL not grant any additional access or alter business logic outcomes.

### REQ-OPS-001: Make request ID searchable for support and incident response
Source Design Decisions:
- DES-002
- DES-003

Priority: Medium

Rationale:
- The operational value of the change depends on support being able to find correlated logs quickly.

Requirement:
- THE system SHALL emit `request_id` in structured API and worker logs and SHALL define post-deploy verification steps that confirm end-to-end correlation.

Verification Method:
- Operational verification in staging or production

Risk if Unmet:
- The feature ships without improving debugging or support workflows.

Acceptance Criteria
1. WHEN a request traverses the API and queue flow successfully, THEN support SHALL be able to find both API and worker logs by the same `request_id`.
2. THEN post-deploy verification SHALL include a sampled correlation check across both surfaces.

Negative Cases
1. WHEN request ID propagation is absent for an older job, THEN support guidance SHALL still describe how to identify that limitation without treating it as a worker failure.

## Traceability Matrix
- DES-001 -> REQ-FUNC-001, REQ-NFR-001, REQ-SEC-001
- DES-002 -> REQ-DATA-001, REQ-NFR-001, REQ-OPS-001
- DES-003 -> REQ-DATA-001, REQ-SEC-001, REQ-OPS-001
