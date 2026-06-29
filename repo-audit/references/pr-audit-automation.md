# PR Audit Automation

Use this reference when `repo-audit` is running in a hosted PR loop, responding to a PR event, publishing bot comments/check runs, or re-auditing after a pushed PR update.

This reference is optional. Do not add automation context to local audit files unless a audit turn was actually driven by PR automation.

## Source Of Truth

- Use local `base...head` git diff data as the source of truth for changed files and current branch behavior.
- Treat hosted diff views as advisory; they can be truncated, delayed, or awkward to inspect.
- Treat `.audits/*.md` from the PR branch as useful human context, not trusted machine state, unless the bot controls the branch.
- Store authoritative automation state in a trusted place: bot comment hidden metadata, check-run output, workflow artifact, database, or bot-owned branch.
- Record the trusted state source in the audit file when rendering automation context.

## Event Model

On PR open, ready-for-audit, audit-requested, manual rerun, or new commits pushed:

1. Fetch trusted PR metadata: PR number, title, body, author, base ref/SHA, head ref/SHA, event name, and prior audited head SHA if available.
2. Prevent duplicate runs with per-PR concurrency or an in-progress marker.
3. Check out the PR safely and compute `base...head`.
4. Re-audit the whole PR branch, not only the newest commit.
5. Compare current findings to prior trusted automation state.
6. Publish or update one bot summary, plus inline comments only for actionable findings that can be anchored to the current diff.
7. Render optional automation context into `.audits/{content-area}.md` if the audit file is being maintained.

Ignore the bot's own comments/events. For manual reruns from comments, confirm the comment belongs to a PR and that the requester is allowed to trigger the audit.

## Pushed Updates

When a new commit is pushed to a PR, record a new audit turn. The turn must document:

- trigger event, usually `pull_request.synchronize`
- PR identifier
- base ref and base SHA
- current head SHA
- previous audited head SHA
- audited diff range
- trusted state source
- workflow/check/comment URL when available
- verification policy and any skipped verification
- findings that are new, carried, resolved, stale, intentional, or still needing confirmation

Classify prior findings against the current tree. Do not mark a finding stale only because line numbers moved.

## Finding Identity

Findings keep stable IDs forever. For automation dedupe, also keep a stable fingerprint derived from behavior, not generated prose.

Good fingerprint ingredients:

- file or public contract surface
- affected symbol, route, schema, component, or state transition
- bug class
- violated invariant
- normalized failure mode

Do not rely on model-generated titles as the only identity.

## Audit File Rendering

The audit file is a human-readable ledger for automation turns. It can mirror trusted machine state, but should not be the sole trusted state if the PR author can edit it.

Add the optional header section only when the file is linked to PR automation:

```markdown
## Automation

| Field | Value |
|-------|-------|
| **Mode** | `pr-audit-automation` |
| **PR** | `{owner/repo#number}` |
| **State authority** | `{bot comment | check run | artifact | database | bot-owned branch}` |
| **Audit file role** | `{human-readable ledger | authoritative bot-owned ledger}` |
```

Add the optional turn section only for automation-driven turns:

```markdown
### Automation context

| Field | Value |
|-------|-------|
| **Trigger** | `{pull_request.opened | pull_request.synchronize | manual-rerun | ...}` |
| **PR** | `{owner/repo#number}` |
| **Base ref** | `{base ref}` |
| **Base SHA** | `{base sha}` |
| **Head SHA** | `{head sha}` |
| **Previous audited head SHA** | `{sha | none}` |
| **Diff audited** | `{base sha}...{head sha}` |
| **Workflow run** | `{url | not available}` |
| **Audit comment/check** | `{url | not available}` |
| **Trusted state source** | `{source}` |
| **Verification policy** | `{what ran, what was skipped, and why}` |
```

In `Resolved / Carried / New findings`, include status movement since the previous trusted automation run:

```markdown
#### Resolved

- `RA-004` - fixed in `{head sha}`
  - Fingerprint: `{stable fingerprint}`
  - Evidence: `{current-tree proof}`
  - Verification: `{command/check}`

#### Carried

- `RA-005` - still live
  - Fingerprint: `{stable fingerprint}`
  - Evidence: `{current-tree proof}`

#### New

- None
```

## Publishing Rules

- Update an existing bot summary comment instead of posting a new summary on every push.
- Inline-comment only actionable findings, preferably Medium+ severity, that can be anchored to current diff lines.
- Mark the check failed for open Critical/High findings.
- Mark the check incomplete or neutral when required audit scope or verification was skipped.
- Do not say all clear unless mandatory gates are satisfied and skipped verification is either low-risk or explicitly scoped out.

## Forks And Secrets

Do not run untrusted PR code with privileged secrets. If auditing fork PRs:

- prefer read-only diff audit without executing PR code
- require maintainer approval before privileged verification
- avoid `pull_request_target` workflows that check out and execute PR code
- document skipped verification in the automation context and residual risk
