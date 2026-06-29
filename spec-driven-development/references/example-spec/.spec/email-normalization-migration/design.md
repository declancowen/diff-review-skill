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

# Design Document: Email Normalization Backfill and Read-Path Migration

## Summary
- Add a normalized email column, backfill existing users, dual-read during rollout, and retire legacy read paths after verification.
- This enables consistent uniqueness enforcement and safer login lookups.

## Scope Statement
- Covers schema changes, backfill workflow, login read-path changes, observability, and rollback controls.

## Original Plan Alignment Audit
- Original plan or prompt excerpts reviewed: normalize email lookup with safe migration and backfill sequencing.
- Explicit requirements confirmed from the original plan: preserve login, backfill safely, enforce uniqueness only after reconciliation, and keep rollback viable.
- Plan items excluded or deferred, with reason: display casing changes are excluded because the request is about lookup normalization.
- Gaps, contradictions, or stale assumptions found: none.
- Upstream artifact changes required before continuing: none.
- Architecture standards reviewed: migration sequencing, data ownership, auth lookup invariants, rollback, observability.
- Agent judgment or justified architecture-standard deviations: none.
- Post-design audit outcome: design remains aligned with the request and architecture standards.

## Repository Discovery Summary

### Repo Root
- `/repo`

### Repo-Specific Profile and House Patterns
- The repo profile requires expand, migrate, switch, cleanup sequencing for data changes.

### Entry Points and Execution Path
- `db/migrations/`
- `src/auth/login-service.ts`
- `src/users/user-repository.ts`
- `src/jobs/backfill-normalized-email.ts`

### Confirmed Code and Runtime Facts
- User lookup currently filters on `users.email`.
- Background backfills run through the jobs framework in `src/jobs/`.

### Related Code and Pattern Inventory
- `db/migrations/20260115_add_slug_column.sql` used a two-phase expand and backfill pattern.

### Adjacent Pattern Comparison
- Preferred existing pattern: add nullable column, backfill, dual-read, enforce, cleanup.
- The design conforms.

### Blast Radius Review
- Login flows, admin search, imports, and uniqueness checks all read the email field.

### Recent Related Repository History
- A previous direct uniqueness migration caused lock contention, so the design avoids in-place constraint flips until data is clean.

### Impacted Boundaries and Adjacent Systems
- Auth service, admin tooling, import jobs, analytics exports.

### Data, Contracts, and Config Surfaces
- `users` table, auth queries, job configuration, and metrics.

### Existing Tests and Operational Signals
- `tests/integration/login_lookup.test.ts`
- user-login error-rate dashboard

### Static Analyzer and Audit Evidence
- Relevant audit/review artifacts: not applicable for this exemplar.
- Analyzer commands, modes, configs, baselines, suppressions, allowlists, and thresholds: not applicable.
- Duplication, health, module-budget, boundary, or coverage signals that influence the design: no analyzer-backed signals available.
- Gate vs advisory inventory distinction: not applicable.
- For each analyzer result: not applicable.
- CI parity: not applicable.
- Accepted-debt register: none.

## Problem Statement and Context
- Email casing differences create inconsistent lookups and uniqueness behavior.
- A naive migration risks data integrity and login failures.

## Current-State Analysis
- The system stores user-entered casing in the primary lookup column.
- Queries and constraints are not normalized.

## Target-State Architecture
- Intended owner for each durable invariant: write paths own normalization; repositories own lookup behavior; migrations/jobs own backfill and enforcement sequencing.
- Dependency direction and public surfaces: auth and admin flows use repository methods rather than duplicating normalization rules.
- Contracts, data ownership, async/reliability, and operational ownership: the `users` table gains `normalized_email`; SRE owns rollout monitoring and abort signals.
- What must stop happening after the transition: login and search must not depend on user-entered email casing.
- Fitness functions that prove the target state is holding: migration tests, dual-read integration tests, reconciliation metrics, and rollout checks.

## Goals
- Introduce deterministic normalized lookup without breaking login.

## Non-Goals
- Changing display casing shown to users.

## Confirmed Facts
- Existing login code depends on the repository abstraction, making dual-read practical.

## Assumptions
- Invalid historical email data volume is small enough for manual remediation.

## Open Questions
- None.

## Decision Needed
- None.

## Proposed Design

### Solution Overview
- Add `normalized_email`, backfill it, dual-read and dual-write during rollout, enforce uniqueness only after reconciliation, then clean up the legacy lookup path.

### End-to-End Flow
- Expand schema.
- Backfill in batches.
- Switch reads to normalized fallback logic.
- Enforce uniqueness after data validation.
- Retire legacy fallback.

### Component and Module Changes

#### UI or Client
- Not applicable.

#### API or Application Layer
- Login service and admin search adopt normalized lookups.

#### Domain or Business Logic
- Email normalization becomes a write-path invariant.

#### Data Model and Persistence
- New nullable column, backfill, index, and eventual uniqueness constraint.

#### Integrations, Events, or Background Jobs
- Backfill job emits progress metrics.

#### Security and Permissions
- No auth boundary change beyond lookup correctness.

#### Performance and Scalability
- Dual-read is temporary and bounded.

#### Observability and Operations
- Add backfill progress, mismatch counts, and login error monitoring.

## Impacted Surfaces Matrix
- UI: Not applicable.
- API: login and admin-search handlers
- Domain logic: email normalization rules
- Persistence: `users` table and indexes
- Integrations: user-import jobs
- Auth: login lookup path
- Infra: migration runner and job scheduler
- Telemetry: backfill and login metrics
- Tests: integration and migration tests
- Docs: operational runbook

## Change Impact Map
- Direct impact: user schema, repository queries, backfill job.
- Indirect impact: login reliability and admin search correctness.
- Unchanged but risk-adjacent areas: user display casing and permissions.

## Invariants and Forbidden Outcomes
- Users must continue to log in during every rollout phase.
- No data loss or accidental account merges may occur.

## Compatibility Matrix
- Public API: Not applicable.
- Internal API: Repository methods gain normalized lookup semantics.
- Data schema: New nullable column and eventual uniqueness constraint.
- Events: Not applicable.
- Cache keys: Not applicable.
- Config: Backfill batch-size settings.
- External consumers: Not applicable.
- Rollback compatibility: Dual-read and legacy column preserve rollback safety until cleanup.

## Contract Examples and Before/After Payloads
- Request examples: Not applicable.
- Response examples: Not applicable.
- Event or message examples: Not applicable.
- Before/after comparisons: login lookup goes from `WHERE email = ?` to normalized dual-read until cleanup.

## Cross-Cutting Applicability Matrix
- Security: Covered. Login correctness is security-sensitive.
- Privacy: Covered. No new sensitive data class.
- Performance: Covered. Temporary dual-read overhead is bounded.
- Resilience: Covered. Dual-read preserves fallback behavior.
- Migration: Covered. Expand, migrate, switch, cleanup plan is explicit.
- Observability: Covered. Backfill and login metrics required.
- Supportability: Covered. Runbook required for remediation.
- Backward compatibility: Covered. Legacy read path remains during rollout.

## Success Metrics and Numeric NFR Targets
- Latency targets: p95 login lookup increase below 5 ms during dual-read.
- Throughput or concurrency targets: Backfill throughput sustains 5k rows per minute without exhausting DB connections.
- Error-rate or availability targets: login failure rate increase stays below 0.1 percentage points.
- Timeout, retry, or queue-depth limits: backfill retries capped at 3; queue backlog below 10 minutes.

## Decision Register

### DES-001: Use expand, migrate, switch, cleanup for normalized email rollout
- Context: Data changes affecting login must remain rollback-safe.
- Decision: Keep legacy reads available until backfill and validation complete.
- Rationale: This matches the repo’s safe-migration pattern.
- Tradeoffs: Temporary query complexity and dual-read overhead.
- Affected surfaces: migrations, repositories, login service, jobs

## Risk Register
- Risk:
  - Impact: Incorrect backfill or premature cleanup could break login.
  - Mitigation: Dual-read, reconciliation metrics, and staged enforcement.
  - Residual risk: Medium.

## Test Impact Matrix
- Existing tests to update: `tests/integration/login_lookup.test.ts`
- New tests required: migration tests, normalization write-path tests, reconciliation tests
- Compatibility tests: dual-read with partially backfilled rows
- Rollback-safety tests: rollback before cleanup retains working login

## Validation Strategy
- Schema, migration, integration, performance, and operational validation

## Post-Design Review
- Original plan coverage review: the design covers schema expansion, backfill, read-path migration, uniqueness enforcement, observability, and rollback.
- Repository evidence review: the design uses existing migration, repository, auth, job, and test surfaces.
- Architecture standards review: ownership, data migration sequencing, rollback, and operational fitness were reviewed.
- Requirements readiness: ready.
- Required upstream changes before requirements authoring: none.

## Rollout, Abort, and Reversal
- Roll out schema first, then backfill, then read switch, then uniqueness enforcement, then cleanup.
- Abort if login failures or mismatch counts exceed thresholds.
- Reversal keeps legacy reads until cleanup is complete.

## Forbidden Shortcuts and Guardrails
- Do not replace lookup logic in one step.
- Do not add uniqueness enforcement before reconciliation passes.
- Do not delete the legacy path before rollback is no longer needed.

## Alternatives Considered
- Alternative:
  - Why rejected: One-shot rewrite of the email column was rejected due to data-loss and outage risk.

## Residual Risks
- Historical malformed data may require manual cleanup before constraint enforcement.
