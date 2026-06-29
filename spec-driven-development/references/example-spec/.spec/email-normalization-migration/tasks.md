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

# Task Plan: Email Normalization Backfill and Read-Path Migration

## Source Artifacts
- `.spec/email-normalization-migration/design.md`
- `.spec/email-normalization-migration/requirements.md`

## Gating Status
- Ready for implementation
- Blocking design decisions:
  - None

## Execution Status Summary
- To do: 1.1, 2.1, 3.1
- In progress: none
- Completed: none
- Deferred: none
- Blocked: none

## Sequencing Notes
- Schema expansion and compatibility logic must land before backfill and enforcement.

## Implementation Authority And Review Loop
- The spec is guidance; the original user request is authoritative for the target outcome, architecture standards are the review lens for solution shape, and live code/current tests are authoritative for current reality.
- Before each leaf task, read linked `DES-*` entries, linked `REQ-*` entries, the task entry, relevant code, and current tests.
- After each implementation slice, run focused validation, review the diff against requirements, and check architecture standards proportional to risk.
- After test creation, verify tests prove requirement behavior and relevant negative cases rather than implementation details.
- If code reality and spec intent diverge, update `design.md`, then `requirements.md`, then `tasks.md` before continuing.
- The implementing agent may challenge a stale task or skill interpretation, but must document the rationale and update upstream artifacts before continuing.

## Blocking Work
- None.

## Tasks

- [ ] 1. Expand schema and compatibility path
  - [ ] 1.1 Add nullable normalized email column and compatibility read support
    - Status: todo
    - Depends on: none
    - Likely areas: `db/migrations/20260422_add_normalized_email.sql`, `src/users/user-repository.ts`
    - Validation: migration and integration verification
    - Exit criteria: schema expands without breaking existing login
    - Rollback impact: reversible because legacy path remains
    - Blocking unknowns: none
    - Pre-implementation context check: review DES-001, REQ-FUNC-001, REQ-DATA-001, migration conventions, repository lookup code, and login tests before editing
    - Test creation review: migration and integration tests prove compatibility reads and schema expansion behavior rather than only checking column existence
    - Post-implementation review: diff reviewed against cited requirements and architecture standards for migration sequencing and invariant ownership; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live repository migration patterns differ from the spec
    - _Requirements: REQ-FUNC-001, REQ-DATA-001_

- [ ] 2. Backfill and observe
  - [ ] 2.1 Implement batch backfill job and reconciliation metrics
    - Status: todo
    - Depends on: 1.1
    - Likely areas: `src/jobs/backfill-normalized-email.ts`, `src/metrics/auth.ts`
    - Validation: job and operational verification
    - Exit criteria: backfill progress and mismatch counts are visible
    - Rollback impact: safe because read compatibility remains
    - Blocking unknowns: none
    - Pre-implementation context check: review DES-001, REQ-DATA-001, REQ-NFR-001, REQ-OPS-001, job framework code, metrics patterns, and operational tests before editing
    - Test creation review: tests prove batching, reconciliation, and metric behavior rather than only asserting job function calls
    - Post-implementation review: diff reviewed against cited requirements and architecture standards for job ownership, retry safety, and observability; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live job or metrics patterns differ from the spec
    - _Requirements: REQ-DATA-001, REQ-NFR-001, REQ-OPS-001_

- [ ] 3. Switch and enforce
  - [ ] 3.1 Switch primary reads to normalized lookup and enforce uniqueness after reconciliation
    - Status: todo
    - Depends on: 2.1
    - Likely areas: `src/auth/login-service.ts`, `db/migrations/20260429_enforce_normalized_email_unique.sql`
    - Validation: integration, rollback, and performance verification
    - Exit criteria: login succeeds through normalized reads and reconciliation passes before enforcement
    - Rollback impact: revert to compatibility reads until cleanup
    - Blocking unknowns: none
    - Pre-implementation context check: review DES-001, all linked requirements, login service code, repository lookup code, migration enforcement pattern, and rollback tests before editing
    - Test creation review: tests prove normalized lookup, legacy fallback, enforcement gating, and rollback behavior rather than only asserting helper output
    - Post-implementation review: diff reviewed against cited requirements and architecture standards for auth lookup ownership and cleanup sequencing; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live auth or migration patterns invalidate the planned sequence
    - _Requirements: REQ-FUNC-001, REQ-DATA-001, REQ-NFR-001, REQ-OPS-001_

## Post-Deploy Verification
- Confirm login succeeds for pre-backfill and post-backfill accounts.
- Confirm mismatch counts remain within tolerance.
- Confirm rollback remains viable until cleanup.

## Traceability Matrix
- REQ-FUNC-001 -> 1.1, 3.1
- REQ-DATA-001 -> 1.1, 2.1, 3.1
- REQ-NFR-001 -> 2.1, 3.1
- REQ-OPS-001 -> 2.1, 3.1

## Coverage Checklist
- Every `REQ-*` appears in at least one leaf task
- No leaf task introduces scope absent from the requirements
- Validation is included near risky changes
- Rollout and rollback work is present when needed
- Every leaf task includes pre-implementation context review, test creation review, post-implementation review, and spec drift check fields
- `Depends on` references form a valid acyclic graph
- Every leaf task and blocking spike appears exactly once in `Execution Status Summary`
