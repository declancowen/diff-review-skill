# Deliver - QA / Testing Mode

Use this mode to validate delivered work against business design, business requirements, technical requirements, technical tasks, UX/CX journeys, process design, and release criteria.

## Purpose

Create and maintain a QA plan, test cases, regression coverage, evidence, defects, blockers, and sign-off position.

## File

Write to `03-deliver/qa-testing.md`. Update `traceability.md` with `TC-*` test cases and `DF-*` defects.

## Minimum fact base

Use:

- `traceability.md`;
- Requirements, UI/CX, Process, Solution, Technical Requirements, Technical Design, Technical Tasks;
- Delivery Plan and Build Slices;
- actual test output, screenshots, logs, manual verification notes, or reproduction steps where available.

## Workflow

1. Read upstream design and delivery artefacts.
2. Build test coverage from `BR-*`, `UX-*`, `PR-*`, `SD-*`, `TR-*`, `TT-*`, and `DS-*`.
3. Define functional, permissions/security, UX/state, process, data/correctness, regression, and release-blocker tests.
4. Run or document available tests.
5. Record evidence and defects.
6. Check `quality-gates.md` for slice diff-review findings and make sure any user-visible, data, security, architecture, or release-impacting findings are represented in QA or release blockers.
7. Mark requirements done only when test evidence supports them and required slice reviews are clean, blocked, or accepted risk.
8. Update `traceability.md`, `quality-gates.md`, and `qualify.md`, including `DF-*` rows for failed validations and live-blocking issues.

## Output contract

Use this structure:

```markdown
# QA / Testing

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: traceability.md, 03-deliver/build-slices.md
Blocks: none

## QA objective

## Coverage matrix
| TC ID | Scenario / test | Covers BRs | Covers TRs | Covers DS / TT | Type | Priority | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| TC-AREA-001 |  | BR-AREA-001 | TR-AREA-001 | DS-AREA-001 / TT-AREA-001 | Functional | Must | Draft |  |

## Functional tests

## Permission and security tests

## UX, content and state tests

## Process, support and operational tests

## Data, reporting and correctness checks

## Regression tests

## Defects and failed validations
| DF ID | Issue | Found by TC | Severity | Requirement impact | Owner | Status | Retest evidence |
|---|---|---|---|---|---|---|---|

## Test evidence
| Evidence | Source / command / file | Covers | Result |
|---|---|---|---|

## Release blockers
| Blocker | Impact | Required decision / fix | Owner | Status |
|---|---|---|---|---|

## QA sign-off position
```

## Review gate

QA is not ready unless:

- must-have `BR-*` and material `TR-*` have test coverage or an explicit blocker;
- user journeys and process exceptions are validated where relevant;
- failed tests become `DF-*` defects or blockers and are linked in `traceability.md`;
- slice diff-review findings that affect quality or release risk are reflected in QA status;
- evidence is linked or described clearly enough to repeat;
- release blockers are carried into `03-deliver/release.md`.
