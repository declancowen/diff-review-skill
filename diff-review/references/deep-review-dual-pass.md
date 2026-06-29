# Deep Review Dual Pass

Use this when a diff is medium/high risk, broad, security-sensitive, devex-sensitive, feature-gated, or maintainability-heavy.

The goal is to simulate two independent reviewers inside one Codex thread. Keep the passes separate long enough to avoid blending concerns too early, then synthesize.

## When To Use

- High or Critical risk
- Medium risk with shared contracts, security, migrations, async state, broad UI, devex, or feature flags
- Large PRs or branches with many changed files
- Re-review after a serious escaped finding
- User asks for a deep, harsh, thermonuclear, or very thorough review
- Diff adds visible structural complexity even when behavior appears correct

Do not use this as the default for tiny localized diffs. For Low risk, a normal targeted review is usually enough.

## Pass A: Correctness And Safety

Review the diff for behavior that can break users, data, security, operations, or developer workflow.

Check:

- changed behavior vs intended behavior
- breaking changes across callers, consumers, persisted data, and old clients
- authn/authz, tenant/workspace/team scope, permission bypasses
- validation, serialization, storage, cache keys, and public contracts
- optimistic/persisted drift, fallback paths, retries, rollback, partial success
- feature flag or internal-only leaks
- environment variables, secrets, scripts, ports, local setup, build/dev commands
- migrations, rollout, rollback, idempotency, generated clients, compatibility windows
- deleted safeguards, old guards moved to weaker layers, or checks only present in the UI
- dependency/config changes that alter runtime behavior

Do not report pre-existing issues in untouched code unless the diff now exposes, worsens, or depends on them.

## Pass B: Maintainability And Structure

Review the diff as if behavior is correct but the implementation still has to earn its place in the codebase.

Load `maintainability-rubric.md` and check:

- whether the change can be reframed to delete complexity
- file-size growth and decomposition
- ad hoc branching, modes, flags, nullable state, and special cases
- unnecessary abstractions, wrappers, casts, optionality, or generic machinery
- wrong-layer logic and feature details leaking through shared boundaries
- duplicated helpers where a canonical utility exists
- orchestration that is unnecessarily sequential or leaves partial state harder to reason about
- type, schema, and boundary clarity

Do not bury structural blockers behind a clean behavioral review. A diff can be functionally correct and still fail the review because it makes the codebase meaningfully harder to maintain.

## Fresh-Eyes Rule

When external PR comments, bot reviews, CI findings, or user-provided findings exist:

1. Perform Pass A and Pass B from the current tree first.
2. Then read the external findings.
3. Triage each external finding against the current tree.
4. Dedupe against your own findings.
5. If external review found something you missed, include it and lower confidence until the missed class is swept across sibling paths.

This keeps the first audit independent while still benefiting from external signals.

## Synthesis

After both passes:

- dedupe findings by root cause, not by line number
- treat overlap between passes as stronger evidence
- keep severity tied to production/user/security/data risk, not reviewer annoyance
- distinguish behavior blockers from structural blockers
- make remediation concrete: quick fix, proper fix, validation, sibling sweep
- state remaining uncertainty plainly

If the review is partial, name which pass or surface is incomplete.

## Optional Multi-Thread Mode

Codex does not have the same shared-context subagent model as some other tools. Separate Codex threads can approximate independent reviewers, but this is slower and requires manual synthesis.

Use separate threads only when the user explicitly asks or the branch is large enough that independent context windows are worth the coordination cost. The default deep mode is the single-thread dual pass above.
