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

# Task Plan: Request ID Propagation Across API and Worker Flows

## Source Artifacts
- `.spec/request-id-propagation/design.md`
- `.spec/request-id-propagation/requirements.md`
- `.spec/request-id-propagation/reviews.md` (required once implementation starts)

## Gating Status
- Ready for implementation
- Blocking design decisions:
  - None

## Execution Status Summary
- To do: 1.1, 2.1, 2.2, 3.1
- In progress: none
- Completed: none
- Deferred: none
- Blocked: none

## Sequencing Notes
- Worker compatibility should land before queue publisher changes so pre-rollout and rollback paths remain safe.
- Middleware and route logging changes can follow once downstream compatibility exists.

## Implementation Authority And Review Loop
- The spec is guidance; the original user request is authoritative for the target outcome, architecture standards are the review lens for solution shape, and live code/current tests are authoritative for current reality.
- Before each leaf task, read linked `DES-*` entries, linked `REQ-*` entries, the task entry, relevant code, and current tests.
- Treat a requirement slice as one leaf task or a small group of tightly coupled leaf tasks that completes one requirement or requirement cluster.
- After each implementation slice, run focused validation, then run a deep diff-review scoped to that slice with architecture standards as the architecture lens.
- If diff-review is unavailable, run an equivalent manual deep diff review and record the fallback.
- Fix slice review findings, then run normal diff-review passes with architecture standards until the slice is clean before moving on.
- Record every slice review and the final total-diff review in `.spec/request-id-propagation/reviews.md`.
- After test creation, verify tests prove requirement behavior and relevant negative cases rather than implementation details.
- If code reality and spec intent diverge, update `design.md`, then `requirements.md`, then `tasks.md` before continuing.
- The implementing agent may challenge a stale task or skill interpretation, but must document the rationale and update upstream artifacts before continuing.

## Blocking Work
- None.

## Tasks

- [ ] 1. Add request ID resolution at the API boundary
  - [ ] 1.1 Introduce request ID middleware and attach the resolved value to request-local context
    - Status: todo
    - Depends on: none
    - Likely areas: `src/server/middleware/request-id.ts`, `src/server/index.ts`, `tests/unit/request-id-middleware.test.ts`
    - Validation: middleware unit coverage and route integration coverage
    - Exit criteria: inbound requests consistently expose a resolved `request_id` to downstream handlers
    - Rollback impact: middleware can be removed without changing public API behavior
    - Blocking unknowns: none
    - Pre-implementation context check: review DES-001, REQ-FUNC-001, REQ-SEC-001, middleware entry points, and existing request tests before editing
    - Test creation review: middleware and route tests prove request ID behavior and missing-header fallback rather than only asserting helper internals
    - Slice review loop: run focused validation, deep diff-review plus architecture standards for slice 1.1, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/request-id-propagation/reviews.md`
    - Post-implementation review: diff reviewed against cited requirements and architecture standards for boundary ownership; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live API middleware differs from the planned integration point
    - _Requirements: REQ-FUNC-001, REQ-SEC-001_

- [ ] 2. Propagate request ID through async boundaries
  - [ ] 2.1 Extend queue publishing to include optional `request_id`
    - Status: todo
    - Depends on: 1.1
    - Likely areas: `src/queues/publish-order-events.ts`, `tests/integration/orders/create-order.test.ts`
    - Validation: integration coverage for envelope contents
    - Exit criteria: API-originated queue messages include `request_id`
    - Rollback impact: safe because the field is optional
    - Blocking unknowns: none
    - Pre-implementation context check: review DES-002, REQ-DATA-001, REQ-NFR-001, queue publisher code, and envelope tests before editing
    - Test creation review: tests prove optional `request_id` propagation and absent-value compatibility rather than only field assignment
    - Slice review loop: run focused validation, deep diff-review plus architecture standards for slice 2.1, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/request-id-propagation/reviews.md`
    - Post-implementation review: diff reviewed against cited requirements and architecture standards for contract compatibility; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live queue envelope shape differs from the spec
    - _Requirements: REQ-DATA-001, REQ-NFR-001_
  - [ ] 2.2 Hydrate worker log context from queue envelope metadata
    - Status: todo
    - Depends on: 2.1
    - Likely areas: `src/workers/shared/job-context.ts`, `src/workers/order-events/processor.ts`, `tests/workers/order-events/processor.test.ts`
    - Validation: worker compatibility coverage for present and absent `request_id`
    - Exit criteria: worker logs include `request_id` when available and tolerate older envelopes
    - Rollback impact: safe because absent values remain supported
    - Blocking unknowns: none
    - Pre-implementation context check: review DES-002, REQ-DATA-001, REQ-NFR-001, REQ-OPS-001, worker context code, and worker compatibility tests before editing
    - Test creation review: tests prove present and absent `request_id` worker behavior rather than only context setter calls
    - Slice review loop: run focused validation, deep diff-review plus architecture standards for slice 2.2, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/request-id-propagation/reviews.md`
    - Post-implementation review: diff reviewed against cited requirements and architecture standards for async boundary ownership; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live worker context differs from the spec
    - _Requirements: REQ-DATA-001, REQ-NFR-001, REQ-OPS-001_

- [ ] 3. Update operational safeguards and verification
  - [ ] 3.1 Add support guidance and post-deploy verification for end-to-end correlation
    - Status: todo
    - Depends on: 2.2
    - Likely areas: `docs/support/log-search.md`, `dashboards/api-workers.ndjson`
    - Validation: staging verification using a sampled request ID across API and worker logs
    - Exit criteria: support can follow a documented correlation workflow and deployment checklists include it
    - Rollback impact: documentation and dashboards can be reverted independently
    - Blocking unknowns: none
    - Pre-implementation context check: review DES-003, REQ-OPS-001, support docs, dashboard definitions, and existing rollout checklists before editing
    - Test creation review: verification proves support can trace one request across API and worker logs rather than only checking docs changed
    - Slice review loop: run focused validation, deep diff-review plus architecture standards for slice 3.1, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/request-id-propagation/reviews.md`
    - Post-implementation review: diff reviewed against cited requirements and architecture standards for operational ownership; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live observability surfaces differ from the spec
    - _Requirements: REQ-OPS-001_

## Post-Deploy Verification
- Create one test request in staging and confirm the same `request_id` appears in API and worker logs.
- Verify older queued jobs without `request_id` still process successfully.
- Watch worker error rate and structured logging volume after rollout.

## Traceability Matrix
- REQ-FUNC-001 -> 1.1
- REQ-SEC-001 -> 1.1
- REQ-DATA-001 -> 2.1, 2.2
- REQ-NFR-001 -> 2.1, 2.2
- REQ-OPS-001 -> 2.2, 3.1

## Coverage Checklist
- Every `REQ-*` appears in at least one leaf task
- No leaf task introduces scope absent from the requirements
- Validation is included near risky changes
- Rollout and rollback work is present where needed
- Every leaf task includes pre-implementation context review, test creation review, slice review loop, post-implementation review, and spec drift check fields
- `Depends on` references form a valid acyclic graph
- Every leaf task and blocking spike appears exactly once in `Execution Status Summary`
