---
title: Email Normalization Backfill and Read-Path Migration
scope: email-normalization-migration
status: implementation-ready
repo_root: /repo
change_class: migration
risk_level: high
owner: identity-platform
reviewers: data-lead, api-lead
approvers: engineering-manager
implementation_owner: identity-platform
operations_owner: sre-team
last_updated: 2026-04-22
---

# Requirements Document: Email Normalization Backfill and Read-Path Migration

## Source Artifacts
- `.spec/email-normalization-migration/design.md`

## Scope Statement
- This document defines the behavioral, migration, and operational requirements for normalized email rollout.

## Upstream Alignment Audit
- Original plan requirements reviewed: preserve login, safely backfill normalized email, observe rollout health, and keep rollback viable.
- Design decisions reviewed: DES-001.
- Repository evidence and current tests reviewed: migration, repository, login service, backfill job, and integration test surfaces named in `design.md`.
- Architecture standards implications reviewed: data ownership, migration sequencing, auth lookup invariant ownership, observability, rollback.
- Requirements added, changed, or rejected during audit: none.
- Design updates required before continuing: none.
- Agent judgment or justified architecture-standard deviations: none.
- Post-requirements audit outcome: requirements remain aligned with the design and original plan.

## Cross-Cutting Coverage
- Security: Covered by `REQ-FUNC-001`
- Privacy: Covered by `REQ-DATA-001`
- Performance: Covered by `REQ-NFR-001`
- Resilience: Covered by `REQ-OPS-001`
- Migration: Covered by `REQ-DATA-001`
- Observability: Covered by `REQ-OPS-001`
- Supportability: Covered by `REQ-OPS-001`
- Backward compatibility: Covered by `REQ-FUNC-001`, `REQ-DATA-001`

## Requirements

### REQ-FUNC-001: Preserve successful login during normalized-email rollout
Source Design Decisions:
- DES-001

Priority: High

Rationale:
- Login continuity is the primary invariant.

Requirement:
- THE system SHALL preserve successful user login across schema expansion, backfill, dual-read rollout, and cleanup stages.

Verification Method:
- Integration and staged rollout verification

Risk if Unmet:
- Users are locked out.

Acceptance Criteria
1. WHEN a row is not yet backfilled, THEN login SHALL still succeed via the compatibility path.
2. WHEN a row is backfilled, THEN login SHALL resolve using normalized semantics.

Negative Cases
1. WHEN normalization data is missing or malformed, THEN the system SHALL fail safely without merging accounts.

### REQ-DATA-001: Roll out normalized email with rollback-safe migration sequencing
Source Design Decisions:
- DES-001

Priority: High

Rationale:
- The data change must remain reversible until validation is complete.

Requirement:
- THE system SHALL use expand, migrate, switch, and cleanup sequencing for normalized email rollout and SHALL not enforce uniqueness until reconciliation succeeds.

Verification Method:
- Migration, reconciliation, and rollback verification

Risk if Unmet:
- Data corruption, login breakage, or irreversible rollback failure.

Acceptance Criteria
1. WHEN schema expansion lands, THEN the legacy lookup path SHALL remain functional.
2. WHEN backfill completes and reconciliation passes, THEN uniqueness enforcement MAY proceed.

Negative Cases
1. WHEN reconciliation fails, THEN cleanup and uniqueness enforcement SHALL remain blocked.

### REQ-NFR-001: Bound rollout overhead
Source Design Decisions:
- DES-001

Priority: Medium

Rationale:
- Safety cannot come with unacceptable login or backfill performance degradation.

Requirement:
- THE system SHALL keep dual-read and backfill overhead within acceptable bounds during rollout.

Target Metrics:
- p95 login lookup increase below 5 ms, backfill throughput at or above 5k rows per minute, login failure-rate increase below 0.1 percentage points.

Verification Method:
- Performance and operational verification

Risk if Unmet:
- Rollout overloads the database or degrades login performance.

Acceptance Criteria
1. WHEN dual-read is enabled, THEN login latency SHALL remain within the target.
2. WHEN backfill runs, THEN throughput SHALL remain within the target without exhausting DB capacity.

Negative Cases
1. WHEN thresholds are exceeded, THEN rollout SHALL pause.

### REQ-OPS-001: Expose migration health and rollback readiness
Source Design Decisions:
- DES-001

Priority: High

Rationale:
- Operators need visibility to know when to continue or abort.

Requirement:
- THE system SHALL emit backfill progress, mismatch counts, and login health signals and SHALL define abort and rollback conditions before cleanup begins.

Verification Method:
- Operational verification

Risk if Unmet:
- Unsafe rollout decisions are made without evidence.

Acceptance Criteria
1. WHEN backfill runs, THEN operators SHALL be able to observe progress and mismatch counts.
2. THEN rollout guidance SHALL define abort thresholds before the read switch and cleanup steps.

Negative Cases
1. WHEN health signals are unavailable, THEN cleanup SHALL not proceed.

## Traceability Matrix
- DES-001 -> REQ-FUNC-001, REQ-DATA-001, REQ-NFR-001, REQ-OPS-001
