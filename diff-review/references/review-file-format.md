# Review File Format

Use this when creating or updating `.reviews/{content-area}.md`.

## Rules

- One markdown file per content area.
- Newest turn appears first after the header.
- Header tracks project context, cumulative scope, hotspots, and review status.
- Local human review turn state lives in the review file, not a sidecar.
- For PR automation, the review file may render the human-readable ledger, but trusted machine state can live outside the PR branch; record the state authority when present.
- Automation sections are optional. Omit them when the review was not driven by PR automation.
- `.reviews/` is local review state and can be committed with the branch when useful.
- Durable regression tests belong in normal test directories, not `.reviews/`.

## Header Skeleton

```markdown
# Review: {content area}

## Project context

| Field | Value |
|-------|-------|
| **Repository** | {repo} |
| **Remote** | {remote} |
| **Branch** | {branch} |
| **Stack** | {stack} |

## Scope

- `{path}` — added Turn N

## Hotspots

- `{bug family}` — added Turn N

## Review status

| Field | Value |
|-------|-------|
| **Review started** | {date time} |
| **Last reviewed** | {date time} |
| **Total turns** | {N} |
| **Open findings** | {count} |
| **Resolved findings** | {count} |
| **Accepted findings** | {count} |
```

Optional, only when the file is linked to PR automation:

```markdown
## Automation

| Field | Value |
|-------|-------|
| **Mode** | `pr-review-automation` |
| **PR** | {owner/repo#number} |
| **State authority** | {bot comment | check run | artifact | database | bot-owned branch} |
| **Review file role** | {human-readable ledger | authoritative bot-owned ledger} |
```

## Turn Skeleton

```markdown
## Turn N — {date time}

| Field | Value |
|-------|-------|
| **Commit** | {sha} |
| **IDE / Agent** | {agent} |

{Optional, only for automation-driven turns:}

### Automation context

| Field | Value |
|-------|-------|
| **Trigger** | {pull_request.opened | pull_request.synchronize | manual-rerun | ...} |
| **PR** | {owner/repo#number} |
| **Base ref** | {base ref} |
| **Base SHA** | {base sha} |
| **Head SHA** | {head sha} |
| **Previous reviewed head SHA** | {sha | none} |
| **Diff reviewed** | {base sha}...{head sha} |
| **Workflow run** | {url | not available} |
| **Review comment/check** | {url | not available} |
| **Trusted state source** | {source} |
| **Verification policy** | {what ran, what was skipped, and why} |

**Summary:** {...}
**Outcome:** {all clear | all clear with low-risk unknowns | partial review | blocked by open findings | blocked by missing verification}
**Risk score:** {low | medium | high | critical} — {why}
**Change archetypes:** {tags}
**Intended change:** {...}
**Intent vs actual:** {...}
**Confidence:** {high | medium | low} — {why}
**Coverage note:** {...}
**Finding triage:** {...}
**Static/analyzer evidence:** {changed gates, duplication/refactor signals, policy drift, baselines/suppressions, or not used}
**Architecture impact:** {current-state failure mode improved/worsened/unchanged, or not applicable}
**Deep-review evidence:** {dual pass completed/not needed; correctness/safety result; maintainability/structure result}
**Remediation plans:** {linked plan files, recommended plans, or not requested}
**Bug classes / invariants checked:** {...}
**Branch totality:** {...}
**Sibling closure:** {...}
**Remediation impact surface:** {...}
**Residual risk / unknowns:** {...}

### Validation

- `{command}` — passed/failed/not run

### Branch-totality proof

- **Non-delta files/systems re-read:** {...}
- **Prior open findings rechecked:** {...}
- **Prior resolved/adjacent areas revalidated:** {...}
- **Hotspots or sibling paths revisited:** {...}
- **Dependency/adjacent surfaces revalidated:** {...}
- **Why this is enough:** {...}

### Challenger pass

- `{done | not needed | blocked}` — {...}

### Resolved / Carried / New findings

{finding sections}

### Recommendations

1. **Fix first:** {...}
2. **Then address:** {...}
3. **Patterns noticed:** {...}
4. **Suggested approach:** {...}
5. **Architecture transition:** {...}
6. **Defer on purpose:** {...}
```

## Key Requirements

- Every turn states outcome, risk, confidence, coverage, triage, branch totality, validation, and residual risk.
- Turn 2+ proves branch-totality concretely; generic "rechecked branch" is insufficient.
- External findings get current-tree triage and bug-class classification.
- Serious findings require sibling closure and remediation impact notes.
- No findings still requires proof.
- Deep reviews must record whether both passes ran and what each pass contributed, even when the final result is no findings.
- Refactor-heavy reviews must say whether the change improved ownership/current-state architecture, not only whether metrics or tests passed.
- When remediation plans are created, refreshed, blocked, or rejected, the turn records the linked plan files and stable finding IDs. Plans do not replace finding resolution notes.
- PR automation turns must record the trigger, PR identity, base/head SHAs, previous reviewed head SHA, diff range, trusted state source, verification policy, and finding movement since the previous trusted automation run.
- Do not treat PR-branch `.reviews/` files as the trusted automation state unless the bot controls the branch.
- If anything important was not reviewed, mark partial and name what remains.
