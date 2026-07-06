# Review - Hypercare / Support Mode

Use this mode after release to track live stability, user/support feedback, defects, mitigations, and exit criteria.

## Purpose

Confirm whether the released demand is stable enough to leave hypercare and move into outcomes review.

## File

Write to `04-review/hypercare-support.md`. Update `qualify.md` and `traceability.md` when live issues affect requirements, release checks, or review metrics. Use `DF-*` for live defects or failed validations that need remediation; keep non-defect feedback clearly separate.

## Minimum fact base

Use:

- release runbook and immediate verification;
- monitoring, logs, incidents, support tickets, feedback, operational evidence, and known defects;
- unresolved QA defects or release conditions.

## Workflow

1. Read Release and QA outputs.
2. Define hypercare scope, duration, owners, and exit criteria.
3. Track live health and issues.
4. Identify operational/support themes.
5. Record mitigations, fixes, residual risks, and follow-up demands.
6. Decide whether hypercare can exit.

## Output contract

Use this structure:

```markdown
# Hypercare / Support

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: 03-deliver/release.md, 03-deliver/qa-testing.md
Blocks: none

## Hypercare scope and exit criteria

## Live health
| Signal | Expected | Actual | Evidence | Status |
|---|---|---|---|---|

## Issues and feedback
| ID | Issue / feedback | Source | Impact | Owner | Status | Related BR / TR / TC |
|---|---|---|---|---|---|---|

## Operational and support themes

## Fixes, mitigations and residual risks
| Item | Action | Evidence | Residual risk | Follow-up |
|---|---|---|---|---|

## Hypercare decision

## Outcomes review handoff
```

## Review gate

Hypercare is not complete unless:

- exit criteria are explicit;
- live issues are triaged and linked to requirements, tests, defects, or release checks where relevant;
- unresolved risks have owners and next actions;
- outcome measurement can proceed or is blocked for a stated reason.
