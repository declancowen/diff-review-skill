# Spec Review Checklist

Use this for human review after the agent has produced the spec package.

## Reviewer checks

- The design is grounded in actual repository paths, symbols, and runtime surfaces.
- The design includes an original-plan alignment audit and a post-design review against repository evidence and architecture standards.
- The design identifies related code, existing patterns, blast radius, and recent relevant repo history.
- The design states what must not break, not just what should change.
- The design names invariant-transfer risks when authority, source of truth, query/acquisition path, fallback, generated artifact, or public contract changes.
- The design names data-admission risks when records, states, references, events, or generated artifacts can enter outputs/effects through the chosen implementation shape.
- The design names derived-output risks when admitted data feeds secondary reads, joins, aggregates, metadata, counters, previews, or generated rows.
- Any contract or schema change has compatibility and rollback coverage.
- Any operationally significant change has observability, rollout, and post-deploy verification coverage.
- Requirements include an upstream alignment audit and do not outrun the design or current code evidence.
- Requirements are traceable to `DES-*` decisions and are behavior-focused rather than implementation-flavored.
- Tasks are traceable to `REQ-*` IDs and are concrete enough to execute safely.
- Each leaf task includes `Pre-implementation context check`, `Test creation review`, `Slice review loop`, `Post-implementation review`, and `Spec drift check`.
- Completed task entries show that the implementing agent re-read current code, relevant tests, linked `DES-*`, and linked `REQ-*` before editing.
- Completed task entries show architecture standards shaped the implementation choices during the slice, not only in a final audit note.
- Completed task entries show invariant-transfer, candidate-acquisition, and derived-fetch checks were applied where relevant, or explicitly scoped out as not applicable.
- Completed requirement slices have review records in `.spec/<scope>/reviews.md`.
- Slice review records show a deep diff-review pass first, architecture standards applied as the review lens, fixes for findings, and normal diff-review reruns until clean.
- Slice review records show the latest slice was checked against cumulative branch changes and prior resolved findings, not only against files touched in that slice.
- If `diff-review` was unavailable, the review record clearly states that and documents an equivalent manual review fallback.
- The agent used skills and specs as guardrails, but corrected stale or poor guidance when repo evidence, user intent, or architecture judgment required it.
- Any deliberate deviation from a skill/template/spec recommendation is documented with rationale, affected requirements, and architecture tradeoff.
- Test additions prove requirement behavior and relevant negative cases rather than only implementation details.
- Post-implementation reviews compare the diff against requirements and architecture standards.
- The final review record covers the total branch/worktree diff against the original plan, the full spec package, live repo evidence, tests, and architecture standards.
- Final architecture/plan audits exist, but they do not substitute for architecture-standard checks embedded inside each slice and material change decision.
- Critical unknowns are not disguised as settled requirements or implementation tasks.
- `Not applicable` entries are justified rather than used to skip hard thinking.
- The dependency graph in `tasks.md` looks credible and non-circular.

## How to treat flags

These checks are design guidance and review pressure, not automatic blockers. When a review flags a boundary move, acquisition path, or invariant-transfer gap, the expected response is to prove the invariant, adjust the design, add the right validation, or record why the lens does not apply. Do not force unnecessary architecture ceremony for a local low-risk change.

Do not mark the package implementation-ready only when a live, material gap remains unresolved after that correction path, especially for auth, tenancy, public contracts, data loss, cost, reliability, or migration risk.

## Flag for correction before all-clear if

- it reads like a generic template with shallow repository references
- it changes shared behavior without naming adjacent consumers
- it moves an authority boundary or acquisition path without proving how old invariants transfer to the new owner
- it allows data into outputs/effects without proving the owning validity, safety, or authorization rule for the chosen implementation shape
- it derives secondary outputs from admitted data without proving the derived behavior remains inside the owning validity, safety, or authorization rules
- it introduces a new pattern without comparing it to the existing one
- it ignores migration, rollback, auth, or observability for a risky change
- it shows evidence of blind implementation from stale tasks without fresh repository/code re-evaluation
- it shows evidence of blind obedience to a skill or spec when repo evidence or the original request required a correction
- it silently contradicts the user's request, architecture standards, or current repo evidence
- a completed task lacks post-implementation review or spec drift check evidence
- a completed requirement slice lacks a `.spec/<scope>/reviews.md` record
- slice reviews are batched into one late monolithic review without per-slice review evidence
- the final total-diff deep review is missing after all slices are complete
- tests assert implementation details without proving the cited requirement behavior
- a meaningful code/spec mismatch was found but `design.md`, `requirements.md`, and `tasks.md` were not refreshed in that order
