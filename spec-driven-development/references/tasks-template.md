---
title: <Spec Title>
scope: <scope>
status: <draft|discovery-blocked|design-ready|requirements-ready|implementation-ready|superseded>
repo_root: <repo-root>
change_class: <feature|refactor|migration|integration|platform|security|ops|bugfix|audit-remediation|architecture-transition|quality-gate>
risk_level: <low|medium|high|critical>
owner: <team-or-person>
reviewers: <comma-separated reviewers>
approvers: <comma-separated approvers>
implementation_owner: <team-or-person>
operations_owner: <team-or-person|not-applicable>
last_updated: YYYY-MM-DD
---

# Task Plan: <Spec Title>

Use this template for `.spec/<scope>/tasks.md`.

This file is downstream from `design.md` and `requirements.md`. It is the execution plan, not a second design doc.

## Source Artifacts
- `.spec/<scope>/design.md`
- `.spec/<scope>/requirements.md`
- `.spec/<scope>/reviews.md` (required once implementation starts)

## Gating Status
- `Ready for implementation` or `Blocked`
- Blocking design decisions:
  - `DES-*` IDs, if any

## Execution Status Summary
- To do: `1.1`, `2.1`, `3.1`, `4.1`
- In progress: none
- Completed: none
- Deferred: none
- Blocked: none

## Sequencing Notes
- Why the work is ordered this way
- Key dependency or rollback constraints
- For architecture transitions, containment and behavior proof should precede broad movement, and analyzer/budget gates should tighten only after code supports them
- For Fallow-backed work, changed-file audit, production gate, full advisory inventory, CI parity, stale-evidence check, and accepted-debt ledger should be explicit tasks or validation under the owning task

## Implementation Authority And Review Loop
- The spec is guidance; the original user request is authoritative for the target outcome, architecture standards are the review lens for solution shape, and live code/current tests are authoritative for current reality.
- Before each leaf task, read linked `DES-*` entries, linked `REQ-*` entries, the task entry, relevant code, and current tests.
- During each leaf task, use architecture standards to shape every material design/code/test decision, not only the final review.
- When a slice moves an authority boundary, source of truth, query/acquisition path, fallback, generated artifact, or public contract, prove invariant transfer before all-clear: old guarantee, new owner, enforcement, and tests or static/runtime proof.
- When a slice materializes related candidates by id, scope, link, retained reference, stream key, cache, fallback page, optimistic state, or generated artifact, validate each candidate through the owning rule before return or persistence.
- When admitted data feeds secondary ids, joins, aggregates, metadata, counters, previews, or generated rows, use architecture standards and diff-review to prove the derived behavior remains valid for the chosen implementation shape.
- These lenses are proportional. If they do not apply to a local slice, record a short reason instead of forcing unnecessary architecture ceremony.
- Treat a requirement slice as one leaf task or a small group of tightly coupled leaf tasks that completes one requirement or requirement cluster; do not batch unrelated requirements just to reduce review overhead.
- After each implementation slice, run focused validation, then run a deep diff-review scoped to that slice with architecture standards as the architecture lens.
- If diff-review is unavailable, run an equivalent manual deep diff review and record the fallback.
- Fix slice review findings, then run normal diff-review passes with architecture standards until the slice is clean before moving on.
- Each slice review checks the latest slice against the accumulated branch diff, prior resolved findings, and branch-wide architecture assumptions.
- Record every slice review and the final total-diff review in `.spec/<scope>/reviews.md`.
- After test creation, verify tests prove requirement behavior and relevant negative cases rather than implementation details.
- If code reality and spec intent diverge, update `design.md`, then `requirements.md`, then `tasks.md` before continuing.
- If the user corrects a generated artifact or says an item drifted, treat that correction as authoritative and refresh upstream spec artifacts before continuing.
- The implementing agent may challenge a stale task or skill interpretation, but must document the rationale and update upstream artifacts before continuing.

## Blocking Work
- Use this section only when implementation is blocked by unresolved design decisions
- Blocking spike format:
  - [ ] SPIKE-001 Clarify <decision or unknown>
    - Status: todo
    - Blocks: DES-003
    - Likely areas: `path/to/code`, `path/to/test`
    - Validation: decision review, prototype, or proof
    - Exit criteria: decision recorded in `design.md`
- Use `- None.` when there is no blocking work

## Tasks

- [ ] 1. Foundation and enabling changes
  - [ ] 1.1 Implement <concrete work item>
    - Status: todo
    - Depends on: none
    - Likely areas: `path/to/module`, `path/to/test`
    - Validation: unit or integration coverage
    - Exit criteria: observable done condition
    - Rollback impact: none or explicit rollback consideration
    - Blocking unknowns: none
    - Pre-implementation context check: review linked `DES-*`, linked `REQ-*`, current code, and current tests before editing
    - Invariant-transfer and candidate-acquisition check: identify moved owners/acquisition paths, prove candidate and derived-fetch validity at the owning boundary, or record why this lens is not applicable
    - Test creation review: tests prove requirement behavior and relevant negative cases, not implementation details
    - Slice review loop: after this requirement slice, run focused validation, deep diff-review plus architecture standards, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/<scope>/reviews.md`
    - Post-implementation review: diff reviewed against requirements and architecture standards; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live code invalidates the spec
    - _Requirements: REQ-FUNC-001, REQ-DATA-001_

- [ ] 2. Application and integration changes
  - [ ] 2.1 Implement <concrete work item>
    - Status: todo
    - Depends on: 1.1
    - Likely areas: `path/to/api`, `path/to/service`
    - Validation: integration or end-to-end coverage
    - Exit criteria: observable done condition
    - Rollback impact: explicit impact statement
    - Blocking unknowns: none
    - Pre-implementation context check: review linked `DES-*`, linked `REQ-*`, current code, and current tests before editing
    - Invariant-transfer and candidate-acquisition check: identify moved owners/acquisition paths, prove candidate and derived-fetch validity at the owning boundary, or record why this lens is not applicable
    - Test creation review: tests prove requirement behavior and relevant negative cases, not implementation details
    - Slice review loop: after this requirement slice, run focused validation, deep diff-review plus architecture standards, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/<scope>/reviews.md`
    - Post-implementation review: diff reviewed against requirements and architecture standards; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live code invalidates the spec
    - _Requirements: REQ-FUNC-002, REQ-NFR-001_

- [ ] 3. Rollout and operational readiness
  - [ ] 3.1 Add or update telemetry, release safeguards, and verification
    - Status: todo
    - Depends on: 2.1
    - Likely areas: `path/to/metrics`, `path/to/dashboard`, `path/to/runbook`
    - Validation: operational verification
    - Exit criteria: rollout readiness confirmed
    - Rollback impact: release can be reversed safely
    - Blocking unknowns: none
    - Pre-implementation context check: review linked `DES-*`, linked `REQ-*`, current code, and current tests before editing
    - Invariant-transfer and candidate-acquisition check: identify moved owners/acquisition paths, prove candidate and derived-fetch validity at the owning boundary, or record why this lens is not applicable
    - Test creation review: tests prove requirement behavior and relevant negative cases, not implementation details
    - Slice review loop: after this requirement slice, run focused validation, deep diff-review plus architecture standards, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/<scope>/reviews.md`
    - Post-implementation review: diff reviewed against requirements and architecture standards; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live code invalidates the spec
    - _Requirements: REQ-OPS-001, REQ-NFR-002_

- [ ] 4. Architecture transition closure
  - [ ] 4.1 Remove obsolete bypasses, suppressions, allowlists, or module-budget exceptions
    - Status: todo
    - Depends on: 2.1
    - Likely areas: `path/to/config`, `path/to/module`, `path/to/test`
    - Validation: static analyzer gate, module budget, dependency rule, or focused regression test
    - Exit criteria: accepted transition debt is removed or reclassified with owner and revisit trigger
    - Rollback impact: explicit impact statement
    - Blocking unknowns: none
    - Pre-implementation context check: review linked `DES-*`, linked `REQ-*`, current code, and current tests before editing
    - Invariant-transfer and candidate-acquisition check: identify moved owners/acquisition paths, prove candidate and derived-fetch validity at the owning boundary, or record why this lens is not applicable
    - Test creation review: tests prove requirement behavior and relevant negative cases, not implementation details
    - Slice review loop: after this requirement slice, run focused validation, deep diff-review plus architecture standards, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/<scope>/reviews.md`
    - Post-implementation review: diff reviewed against requirements and architecture standards; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live code invalidates the spec
    - _Requirements: REQ-ARCH-001_

- [ ] 5. Static analyzer evidence and ratchet closure
  - [ ] 5.1 Capture analyzer evidence, CI parity, and accepted-debt status
    - Status: todo
    - Depends on: 4.1
    - Likely areas: `.fallowrc.json`, `package.json`, `.github/workflows/`, `.audits/`, `.reviews/`
    - Validation: Fallow changed-file audit, production gates, full inventories, CI parity review, stale-evidence check
    - Exit criteria: command, `HEAD`, date, mode, scope, baseline/budget, result, and owner/revisit trigger are recorded for remaining debt
    - Rollback impact: analyzer policy can revert independently if it only tightens gates after code support exists
    - Blocking unknowns: none
    - Pre-implementation context check: review linked `DES-*`, linked `REQ-*`, current code, and current tests before editing
    - Invariant-transfer and candidate-acquisition check: identify moved owners/acquisition paths, prove candidate and derived-fetch validity at the owning boundary, or record why this lens is not applicable
    - Test creation review: tests prove requirement behavior and relevant negative cases, not implementation details
    - Slice review loop: after this requirement slice, run focused validation, deep diff-review plus architecture standards, fix findings, rerun normal diff-review until clean, and record the outcome in `.spec/<scope>/reviews.md`
    - Post-implementation review: diff reviewed against requirements and architecture standards; justified deviations recorded
    - Spec drift check: update `design.md`, then `requirements.md`, then `tasks.md` if live code invalidates the spec
    - _Requirements: REQ-QUAL-001, REQ-ARCH-001_

## Post-Deploy Verification
- Checks to run immediately after release
- Signals to watch
- Abort conditions

## Traceability Matrix
- REQ-FUNC-001 -> 1.1
- REQ-DATA-001 -> 1.1
- REQ-FUNC-002 -> 2.1
- REQ-NFR-001 -> 2.1
- REQ-OPS-001 -> 3.1
- REQ-ARCH-001 -> 4.1

## Coverage Checklist
- Every `REQ-*` appears in at least one leaf task
- No leaf task introduces scope absent from the requirements
- Validation is included near risky changes
- Rollout and rollback work is present when needed
- Architecture-transition specs include containment, behavior preservation, boundary/public-surface movement, and closure of accepted exceptions
- Fallow-backed specs include changed-file gate, production gate, full advisory inventory, CI parity, stale-evidence check, full-test confidence rule, and accepted-debt ratchet where relevant
- Every leaf task includes pre-implementation context review, test creation review, slice review loop, post-implementation review, and spec drift check fields
- Every leaf task includes invariant-transfer, candidate-acquisition, and derived-fetch checks, or records why those checks are not applicable
- Every leaf task includes a slice review loop field that requires deep slice diff-review, fix/re-review until clean, architecture standards, and `.spec/<scope>/reviews.md` logging
- When implementation has started, `.spec/<scope>/reviews.md` records every completed slice and the final total-diff review
- `Depends on` references form a valid acyclic graph
- Every leaf task and blocking spike appears exactly once in `Execution Status Summary`

## Authoring notes
- Leaf tasks must include `Status`, `Depends on`, `Likely areas`, `Validation`, `Exit criteria`, `Rollback impact`, `Blocking unknowns`, `Pre-implementation context check`, `Invariant-transfer and candidate-acquisition check`, `Test creation review`, `Slice review loop`, `Post-implementation review`, `Spec drift check`, and `_Requirements: ..._`.
- Allowed status values are `todo`, `in-progress`, `completed`, `deferred`, and `blocked`.
- Checked tasks must use `Status: completed`; incomplete tasks must not.
- If critical design decisions remain unresolved, do not author implementation tasks. Keep `Gating Status` as `Blocked` and use `Blocking Work` only.
- Keep tasks concrete enough that an implementation agent does not need to reverse-engineer intent.
- The implementing agent is responsible for live code correctness. Task text must require re-checking current code and tests before editing, using architecture standards during the change, then reviewing the resulting diff and tests against requirements and architecture standards.
- For each requirement slice, the implementing agent must run a deep diff review first, fix findings, rerun normal reviews until clean, then record the review loop in `.spec/<scope>/reviews.md` before moving to the next slice.
- The implementing agent is allowed to challenge stale or poor task guidance, but must update upstream artifacts and record the reason rather than silently diverging.
