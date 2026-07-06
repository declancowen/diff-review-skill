# Deliver - Release Mode

Use this mode for release readiness, go-live, rollback, support handoff, communications, and immediate post-release verification.

## Purpose

Decide whether the demand can safely launch and document the release runbook.

## File

Write to `03-deliver/release.md`. Update `qualify.md` and `traceability.md` with `RC-*` release checks.

## Minimum fact base

Use:

- Delivery Plan;
- Build Slices;
- QA / Testing;
- unresolved defects and blockers;
- support/process readiness;
- operational, finance, reporting, compliance, data, security, or provider dependencies;
- rollout, migration, and rollback constraints.

## Workflow

1. Read Delivery and QA outputs.
2. Define release scope and readiness criteria.
3. Confirm all required slice diff reviews are clean, blocked, or explicitly accepted by the user, with `.reviews/*` evidence linked from `quality-gates.md`.
4. Load/read and apply the `$fallow` workflow when applicable before final release readiness. Preserve run state, command modes, findings, exceptions, repeated checks, and evidence in `quality-gates.md` and `.audits/fallow.md` when available.
5. Load/read and apply the `$repo-audit` workflow when the change is material, broad, architectural, high-risk, or needs whole-repo confidence. Link `.audits/*` evidence, remediate findings through new slices, and repeat slice diff-review.
6. Load/read and apply a final branch-total `$diff-review` after Fallow, repo-audit, and remediation. Loop until clean, blocked, or accepted residual risk; do not treat earlier slice reviews as a substitute for final branch-total review.
7. Identify go/no-go checks and owners.
8. Document go-live sequence, rollback/fallback, monitoring, communications, and support handoff.
9. Record launch decision and immediate verification.
10. Update `qualify.md` and `quality-gates.md` with release status and Review handoff.

## Output contract

Use this structure:

```markdown
# Release

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: 03-deliver/qa-testing.md, 03-deliver/build-slices.md
Blocks: none

## Release scope

## Readiness checklist
| RC ID | Check | Owner | Evidence | Status | Blocks launch? |
|---|---|---|---|---|---|
| RC-AREA-001 |  |  |  | Draft | Yes |

## Go / no-go decision
| Decision | Rationale | Conditions | Approver / owner | Date |
|---|---|---|---|---|

## Go-live runbook
| Step | Owner | Action | Timing | Evidence / confirmation |
|---|---|---|---|---|

## Monitoring and stop conditions
| Signal | Threshold / condition | Owner | Action |
|---|---|---|---|

## Rollback / fallback
| Scenario | Trigger | Action | Owner | Communication |
|---|---|---|---|---|

## Communications
| Audience | Message | Channel | Owner | Timing |
|---|---|---|---|---|

## Immediate post-release verification
| Check | Evidence | Result | Follow-up |
|---|---|---|---|

## Final quality gates
| Gate | Required? | Result | Evidence | Release impact |
|---|---|---|---|---|

## Review handoff
```

## Review gate

Release is not ready unless:

- launch blockers are explicit;
- QA sign-off position is reflected;
- required slice diff reviews, Fallow, repo-audit, and final diff-review are clean, not applicable, blocked, or accepted residual risk;
- final quality gate evidence links to `.reviews/*`, `.audits/fallow.md`, and `.audits/*` where those gates ran;
- rollback/fallback is credible for material failure modes;
- support and monitoring owners are named or marked TBC as a blocker;
- Review has clear hypercare and outcome measurement handoff.
