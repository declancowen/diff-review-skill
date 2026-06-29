# Review Workflow

Use this for ordinary diff-review and re-review turns.

## Start

1. Run `scripts/review-preflight.sh` from the repo root when the review is medium/high risk, long-running, includes external findings, or context is fragmented.
2. Create `.reviews/` if needed.
3. Read every `.reviews/*.md` file; they are the turn history and hotspot context.
4. Choose the review target in this order:
   - local working changes first
   - explicit PR/review-request diff second
   - branch vs base fallback third
5. Exclude `.reviews/` from code diffs.
6. If a hosted PR diff is too large, truncated, delayed, or incomplete, do not rely on it for coverage. Review local branch-vs-base diff as the source of truth, then use GitHub only for review comments, thread state, checks, and latest commit/SHA evidence.
7. For deep reviews, run the single-thread dual pass before synthesis: correctness/safety first, maintainability/structure second, then dedupe findings by root cause.
8. If the user asks for a remediation plan, backlog, handoff, or delegated execution, keep the review first: prove the finding is live in the current tree, then load `remediation-planning.md`.

Useful commands:

```bash
mkdir -p .reviews
git diff -- . ':!.reviews/'
git diff --staged -- . ':!.reviews/'
git diff main...HEAD -- . ':!.reviews/'
git diff --name-only main...HEAD -- . ':!.reviews/'
git diff --stat main...HEAD -- . ':!.reviews/'
```

## Turn 1

1. Determine intended change from user request, PR description, commit messages, issue links, and changed files.
2. Detect repo shape and relevant stack references.
3. Name the review file by content area, not branch name.
4. Build a review graph for risky/shared surfaces: producers, validators, transformers, persistors, consumers, read-side helpers, tests.
5. Read every changed file in scope, not only hunks.
6. Trace callers, consumers, shared types, schemas, tests, config, and non-primary paths until blast radius is clear.
7. Assign risk score and archetype tags.
8. If risk is Medium+, user requested a deep/harsh review, or the diff touches devex, feature gates, broad shared surfaces, or meaningful structural complexity, load `deep-review-dual-pass.md`.
9. If the maintainability pass applies, load `maintainability-rubric.md` and review structure independently from behavior before synthesis.
10. Run relevant verification.
11. If planning is requested, recommend which live findings should become plans and record any created plan links in the turn.
12. Write the review file with findings, validation, residual risk, and recommendations.

## Turn 2+

1. Read all existing review files.
2. Collect both current-turn delta and cumulative branch diff.
3. Update cumulative scope and hotspot ledger.
4. Triage prior and external findings against the current tree.
5. Re-read current diff files, prior open finding files, nearby resolved finding files, hotspot families, sibling surfaces, and remediation impact paths.
6. Apply the resolution gate before marking anything resolved.
7. If the branch remains Medium+ risk or structural risk changed, rerun the dual pass against both the current-turn delta and cumulative branch state.
8. Re-run verification that proves the fix and any non-primary sibling path where relevant.
9. Analyse the full current branch state for new findings, not only the latest patch.
10. For large branches, refresh the owner/batch ledger and note any hosted PR diff limits, automated-review status, and unresolved thread state.
11. Reconcile any `plans/` entries tied to resolved, stale, or still-open findings when planning artifacts exist.
12. Append the newest turn at the top of the review body and update header counts.

## Code Context Standard

For every changed file:

- read the whole file
- trace imports and exported symbols
- inspect callers/consumers/renderers
- inspect shared schemas/types/config/permissions/tests
- review deletions and removed guards with the same scrutiny as additions
- search for sibling patterns once a risk is found

## MCP / External Context

Use connected MCP/app context read-only when it materially improves review quality: GitHub PRs/CI, docs, database schema/RLS, architecture docs, or linked issues. If unavailable but needed, record the gap.

## External Findings

When findings are pasted from GitHub/Devin/CI/users:

- load `external-finding-import.md`
- if the task is a broad review rather than only triage, complete the independent audit before reading PR discussion or bot comments
- classify current-tree status: live, already fixed, stale, intentional, needs confirmation
- load `bug-class-taxonomy.md`
- write a miss retrospective if a prior review should have caught it

## Recertification

Every 5 turns or after a major fix cluster, do a short branch-risk recertification:

- what remains highest risk?
- what bug family is most likely under-reviewed?
- what previously fixed area should be rechecked?
- what has not been re-verified recently enough?
