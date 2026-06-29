# Maintainability Rubric

Use this for strict implementation-quality review. The bar is not "does it work"; the bar is "does this make the codebase easier to understand, change, and trust?"

## Core Questions

For every meaningful change, ask:

- Can the change be reframed so fewer concepts, branches, helpers, or modes are needed?
- Is there a behavior-preserving restructuring that deletes complexity instead of relocating it?
- Did the diff improve or degrade local ownership and architecture?
- Did a cohesive module become more coupled, stateful, conditional, or difficult to scan?
- Is the logic in the canonical package, service, component, or module?
- Did the diff add repeated conditionals that suggest a missing model or helper?
- Is the abstraction earning its keep, or is it a pass-through layer?
- Did casts, `any`, `unknown`, optional parameters, or ad hoc object shapes hide a real invariant?
- Did feature logic leak into shared paths or implementation details leak through public APIs?
- Is orchestration sequential or non-atomic in a way that makes the code harder to reason about?

## Structural Blockers

Escalate these when the path to a cleaner structure is visible:

- a complicated implementation where a simpler framing can remove whole branches or concepts
- refactors that move complexity without reducing what the reader must hold in mind
- a file pushed past roughly 1000 lines without a strong organizational reason
- ad hoc conditionals inserted into already busy flows
- one-off flags, nullable modes, or optional parameters that spread state complexity
- feature-specific checks scattered through shared code
- generic or magical handling that hides simple data-shape assumptions
- wrapper/helper layers that add indirection without clarifying ownership or behavior
- duplicated logic where an existing helper or canonical layer should own the concept
- casts or loose types used to bypass a boundary that should be explicit
- special-case handling placed in the middle of an unrelated or already dense function
- temporary branches likely to become permanent debt
- local fixes that ignore sibling flows with the same invariant
- partial-update flows that can leave related state half-applied

## File Size And Decomposition

Treat these as review signals, not automatic failures:

- file grows across 1000 lines
- component gains multiple unrelated responsibilities
- tests become large because setup has no reusable fixture boundary
- helper extraction would isolate pure logic, policy, formatting, or orchestration
- new code is easier to test after being split from rendering, IO, or mutation side effects

Waive file-size concerns only when the file remains clearly organized and the alternative would create worse indirection.

## Preferred Remedies

Prefer suggestions that reduce the number of moving pieces:

- delete unnecessary layers instead of polishing them
- reframe the state model so branches disappear
- move logic to the layer that already owns the concept
- isolate feature-specific behavior behind a dedicated boundary
- replace condition chains with an explicit typed model or dispatcher
- extract pure helpers for policy, mapping, formatting, validation, or reconciliation
- collapse duplicate branches into one clearer flow
- remove wrappers that do not clarify the API
- reuse canonical helpers rather than adding near-duplicates
- make type/schema boundaries explicit instead of relying on fallback casts
- separate orchestration from business logic
- make related writes atomic when partial state is otherwise hard to reason about
- parallelize independent work when that simplifies, not merely optimizes, the flow

## Finding Bar

Do not flood the review with cosmetic comments. Prefer a small set of high-confidence structural findings that would materially improve maintainability or prevent likely future bugs.

Good maintainability findings include:

- the implementation is correct but preserves avoidable incidental complexity
- the design spreads a concept across too many places
- the branch adds a special case where the existing model should absorb the behavior
- the type boundary hides the real state variants
- the code solves a local problem by weakening a shared abstraction
- the remediation can be described concretely enough for the author to act

Approval requires no clear structural regression, no obvious missed simplification with material payoff, no unjustified file-size sprawl, no avoidable spaghetti branching, no wrong-layer feature leakage, and no unnecessary wrapper/cast/optionality churn that obscures the real design.
