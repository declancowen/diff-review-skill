# Operating Modes

Use this for the detailed responsibilities of each architecture-standards mode. The router selects the mode; this reference preserves the full operating guidance.

## Build Mode

Use for normal feature, bugfix, refactor, and scaffolding prompts.

The agent should:

- make the smallest change that preserves architecture and keeps an upgrade path
- implement one complete vertical slice before generalizing, and keep uncertain duplication local
- require each new abstraction, dependency, layer, or runtime mechanism to solve a named current problem that a simpler option cannot safely solve
- put code in the capability/layer that owns the rule
- reuse existing flows instead of creating bypasses
- avoid broad refactors unless the current task would otherwise leave a live architecture risk
- load `implementation-recipes.md` for the relevant code shape
- load `enforcement-patterns.md` when the invariant is likely to be violated again
- explain architecture only briefly in the final answer when the decision is material

## Governance / Audit Mode

Use for whole-repo architecture decisions, repo audits, platform changes, system design, or cross-team/system work.

The agent should:

- evaluate decision quality, ownership, enforcement, and drift
- diagnose current-state architecture before designing the target state
- evaluate whether the target state is specific and enforceable enough to correct current-state failure modes
- treat duplication and refactor reports as architecture evidence: where rules are scattered, ownership is unclear, modules mix responsibilities, or transition debt needs a closure plan
- separate configured gates, production inventories, full inventories, baselines, and accepted debt before declaring the target state credible
- synthesize repeated findings into missing design concepts before recommending mechanical cleanup
- identify owners for capabilities, data, contracts, and operational workflows
- use `architecture-scorecard.md` for repo-level health
- use `smell-triage.md` to separate must-fix risks from refactor preferences
- recommend code-level enforcement before documentation
- call out exceptions, cleanup paths, and missing fitness functions

## Current-State Diagnosis Mode

Use when the repo is already messy or an audit shows the architecture standards are not functioning effectively.

The agent should:

- map what the code actually does, not what docs say it should do
- identify structural failure modes: unclear ownership, scattered policy, boundary bypasses, helper dumping grounds, mixed responsibilities, unowned contracts, weak tests, and stale exceptions
- use duplication, health, churn, module size, and audit-transition evidence as design input
- use Fallow/static-analysis evidence as both path evidence and shape evidence: trace runtime/user journeys, then cluster clone groups, health hotspots, module pressure, and helper sprawl to infer missing design concepts
- produce a transition architecture: immediate containment, sequence of safe refactors, enforcement to prevent relapse, and explicit accepted debt
- avoid declaring a target state successful until the current state has fitness functions that prove movement toward it

## Target-State Design Mode

Use when defining what the architecture should become or when an audit shows the previous target state was too weak.

The agent should:

- derive target-state requirements from current-state evidence, product journeys, failure consequences, and audit findings
- define capability ownership, dependency direction, data ownership, API/contracts, async/reliability, operational ownership, and test/enforcement gates
- specify what must stop happening: duplicated policy, boundary bypasses, generic helper dumping, unowned contracts, permanent allowlists, or deployment-only assumptions
- include migration/transition slices so the target state can be reached from the current code without unsafe rewrites
- make the target state falsifiable with fitness functions: tests, static rules, CI gates, module budgets, smoke checks, or deployment evidence
- treat a budgeted baseline, suppression, allowlist, or production-only clean result as transition state until it has owner, cap, reason, evidence command/date, and revisit trigger

## Learning Abstraction Rule

When PR review, production, CI, or user feedback exposes a missed issue, do not train the architecture skill on the concrete incident. Extract the reusable architecture mechanism at the highest useful level, then choose implementation patterns only as examples.

Record learning in this shape:

- **Level:** outcome/intent, ownership/authority, dataflow/materialization, contract/compatibility, operational/cost, or verification/enforcement.
- **Mechanism:** what kind of architecture guarantee failed or could fail.
- **Design pressure:** what future designs should make explicit.
- **Implementation options:** examples such as query predicates, guard clauses, policy checks, schema constraints, route mapping, reducers, cache keys, joins, tests, static checks, or runtime checks. Do not require one option unless the repo architecture already does.
- **Proof pattern:** the smallest evidence that shows the mechanism is closed for this change.
