# Review Gates

Use this before concluding a diff review, especially for medium/high-risk branches.

## All-Clear Bar

Do not say "all clear" unless:

- intended change is understood and diff matches it
- every changed file in scope was reviewed
- high-risk connected paths were traced far enough
- latest-patch proof was checked against the accumulated branch diff, prior resolved findings, and branch-wide architecture assumptions
- required dual-pass review was completed when risk, scope, or user request called for it
- if prior local review missed a live issue, escaped-finding learning was completed and sibling paths were swept by acquisition mode
- devex and feature-gate changes were treated as behavioral risk, not ignored as configuration noise
- relevant checks were run or missing verification is explicitly accepted as low risk
- no open Critical or High findings remain
- residual uncertainty is minor enough to ship defensibly

For Fallow/static-analysis diffs, also require:

- changed-file gates, production configured gates, full advisory inventories, and baselines are not collapsed into one "clean" claim
- CI analyzer behavior is compared with package scripts, including whether CI uses `continue-on-error`
- accepted debt for duplication budgets, suppressions, allowlists, or health exceptions has owner, cap, reason, evidence date, and revisit trigger
- stale analyzer evidence is rerun or marked stale with `HEAD`, command, mode, and scope
- coverage-aware health uses a refreshed coverage artifact when test changes are part of the fix
- production dead-code is rerun after coverage-oriented helper exports or broad testability extraction
- broad refactors or boundary moves have full validation or an explicit low-risk rationale for narrower checks

For broad remediation, large PRs, or presentation-heavy diffs, also require:

- broad UI/presentation refactors have browser/visual smoke for representative changed screens, or a recorded reason this risk is low and not smokeable
- large PRs with truncated or incomplete hosted diff views have a local branch-vs-base review path and owner/batch ledger; hosted tooling limitations are not treated as review coverage

For maintainability-heavy diffs, also require:

- the implementation was checked for simpler behavior-preserving structure, not only correctness
- visible file-size growth, special-case branching, wrapper/cast churn, and wrong-layer logic were reviewed or explicitly scoped out
- structural findings are ranked by expected future bug risk and codebase cost, not by style preference

When remediation plans are created, also require:

- each plan links to current-tree live review finding IDs
- each plan labels branch relationship as `introduced`, `exposed pre-existing`, or `pre-existing/out of scope`
- each plan has a planned-at SHA, drift check, in/out-of-scope files, verification gates, STOP conditions, and re-review requirement
- broad architecture, migration, platform, or product work is routed to `spec-driven-development` instead of compressed into a thin plan

For Medium+ risk, also read `all-clear-antipatterns.md`.

## Risk Score

- **Low:** localized change, small blast radius, strong direct coverage, easy rollback.
- **Medium:** multiple files/flows, moderate shared-surface impact, some uncertainty.
- **High:** shared abstractions, contracts, auth/data integrity, migrations, concurrency, broad blast radius.
- **Critical:** money, permissions, destructive data paths, one-way transforms, infra toggles, severe failure consequences.

Expected review depth:

- Low: targeted review and targeted verification.
- Medium: full flow tracing, targeted verification, safety-net checks.
- High: full flow tracing, broader verification, compatibility/release-safety review, challenger pass.
- Critical: strongest available verification, explicit residual risks, challenger pass.

Use `severity-calibration.md` for ambiguous or externally supplied findings.

Structural maintainability findings usually start at Medium when they are likely to cause near-term bugs, spread a broken model, hide an invariant, or make future fixes materially harder. Escalate when the structural issue weakens a shared boundary, contract, permission model, migration path, or state authority.

## Deep Review Gate

Use `deep-review-dual-pass.md` when the review is Medium+ risk, broad, user-requested as deep/harsh, or touches devex, feature gates, security, shared contracts, migrations, broad UI, or meaningful structural complexity.

Before synthesis, keep these passes distinct:

- **Correctness/safety:** behavior, security, data integrity, devex, feature-gate leaks, compatibility, rollout, fallback, and partial failure.
- **Maintainability/structure:** simplification, decomposition, branching complexity, layer ownership, boundary/type clarity, wrappers/casts, duplication, and atomicity.

Do not approve a deep review solely because Pass A is clean. If Pass B finds a clear structural regression with a concrete lower-complexity remedy, carry it as a finding.

## Invariant-First Gate

For meaningful shared UI, contract, persistence, optimistic-state, batch-operation, or fallback-path changes, identify:

- authority: who owns IDs/defaults/validation/permissions/timestamps/persisted values
- preservation: what fields/relationships must not change
- state variants: empty, legacy-invalid, read-only/editable, parent/child, filtered/grouped, duplicate labels
- interaction variants: click, keyboard, menu, modal, inline editor, autosave/explicit save
- lifecycle: can the owner unmount before async/confirmation completes?
- identity: are keys/lookups/cache IDs unique under duplicate render/scope?
- atomicity: what happens on partial batch/fan-out failure?
- contract encoding: do internal helper names, public query/form/body keys, cookies, storage keys, and persisted payload keys match every consumer?
- invariant transfer: if a broad path, source of truth, backend authority, selector, or route contract changed, are old invariants re-proven in the new owner?
- acquisition mode: did data enter through direct id lookup, scope scan, relation/link expansion, stale reference, fallback page, generated artifact, stream key, cache, optimistic state, or API error branch?
- derived behavior: if admitted/eligible data feeds downstream ids, joins, aggregates, metadata, counters, previews, side effects, or generated rows, are those inputs, effects, and returned records constrained by the owning rules?

For Medium+ risk, record main invariants checked. For High/Critical risk, attack the weakest invariant directly.

## Variant Matrix

Build a small matrix when a shared component, selector, helper, dialog, menu, or store action changes:

- value: empty, populated, invalid legacy, `null`, `undefined`
- mode: editable, read-only, inline, detail, surface/list/card, create, rename/update
- scope: tenant/workspace/team/project, no scope, duplicate labels, stale/retained scope
- flow: click, keyboard, programmatic submit, optimistic submit, server failure, retry, reconciliation
- container: mounted component, menu/popover, nested dialog, route transition, fallback/skeleton, retained data

## Resolution Gate

Mark a finding resolved only when:

- root cause is addressed
- sibling/family sweep is complete
- the fix does not reopen or weaken prior resolved findings, branch-wide invariants, or accepted architecture decisions
- remediation shape is coherent across the family
- impact surface was assessed across callers, consumers, dependencies, contracts, and side effects
- must-fix adjacent weaknesses are fixed, carried, or explicitly blocked
- non-primary paths were checked where plausible
- targeted verification ran
- recurrence risk was reduced with a prevention artifact or consciously ruled out
- no obvious companion change is missing

Otherwise use `Partially addressed` or `Still open`.

## Challenger Pass

Required for High/Critical reviews. Assume one serious issue remains and hunt in:

- weakest-evidence areas
- untouched dependencies
- deleted safeguards
- compatibility assumptions
- migrations/rollout paths
- tests that may create false confidence
- non-primary callers and bypass paths

## Confidence Penalties

Lower confidence when:

- sibling closure is incomplete
- only primary path was tested
- only route/UI path was reviewed for a contract bug
- serialized contract keys were not asserted on validation, failure, retry, redirect, or non-happy branches
- non-primary caller audit was skipped where bypasses likely exist
- external findings were not current-tree triaged
- branch-totality was not reassessed on Turn 2+
- hotspot ledger was not checked
- adjacent resolved findings were not revalidated after nearby change
- Fallow is present but only lint/typecheck/tests were used as quality evidence
- production-only analyzer cleanliness is described as full-repo cleanliness
- duplication budget passing at baseline is treated as debt removal
- hosted PR diff tooling is truncated/incomplete and no local branch-vs-base review compensates
- broad UI/presentation movement has no browser or visual smoke despite layout/navigation/empty-state risk
- remediation plan exists but no current-tree review proof or re-review closure path is recorded

## Final Self-Audit

Before "no findings" or "all clear", answer:

- what serious issue could still be missing?
- which bug class is most represented by this branch?
- which assumption matters most?
- which high-risk path has weakest evidence?
- which sibling surface could still carry the same bug?
- which acquisition mode could still materialize a bad record or state?
- which state variant was least checked?
- what invariant used to be enforced by the old path, and where is it enforced now?
- if this caused an incident tomorrow, where would you investigate first?
- if plans were created, which plan is most likely to drift or be executed out of scope?
