# Architecture Transition Planning

Use this when a spec is driven by repo-audit findings, Fallow/static-analysis evidence, broad duplication, health hotspots, large modules, boundary drift, or a target-state redesign.

The purpose is to stop audit remediation from becoming a list of mechanical cleanups. A transition spec must explain how the current codebase moves toward an enforceable target state while preserving behavior.

## Evidence To Gather

Collect concrete evidence before writing design decisions:

- audit and review files that describe the problem
- static analyzer configs, baselines, suppressions, allowlists, and thresholds
- duplication groups and whether they are exact, semantic, local, or cross-boundary
- health hotspots, file scores, module budgets, and large-file allowlists
- boundary rules, dependency rules, lint rules, and CI gates
- code paths that currently own, duplicate, or bypass the relevant invariant
- tests, browser smokes, coverage, or deployment evidence that prove behavior

Do not treat a clean configured gate as proof that the architecture is clean. Baselines, skipped local duplication, advisory inventories, production-only modes, and deployment-gated checks all have different meanings.

For Fallow-backed transitions, record:

- command, `HEAD`, date, mode, scope, baseline/gate, result, interpretation, and design impact for each count
- configured production gates separately from full non-production inventories
- changed-file audit separately from repo-wide evidence
- CI parity between package scripts and workflow commands, including `continue-on-error`
- accepted debt for duplication budgets, suppressions, allowlists, and health exceptions with owner, cap, reason, evidence date, and revisit trigger
- stale-evidence rule: old counts cannot support implementation-ready status unless rerun or marked stale

## Design Shape

Every architecture transition design should name:

- **Current-state failure mode:** the actual structural problem, such as scattered policy, unclear owner, mixed responsibility module, weak public boundary, or unowned contract.
- **Target-state rule:** the specific owner, dependency direction, public surface, contract, or enforcement rule that should prevent recurrence.
- **Transition slices:** safe, reviewable steps from current code to target state.
- **Containment gate:** what prevents the problem from getting worse during the transition.
- **Fitness function:** test, static rule, CI gate, module budget, browser smoke, contract test, or deployment check that proves the rule holds.
- **Accepted exception:** any baseline, allowlist, suppression, or module-budget cap that remains, with owner and revisit trigger.
- **Ratchet rule:** how duplication, health, or module-budget debt can only stay flat or decrease unless a new accepted-debt entry is approved.

## Mapping Findings To Specs

Use this translation:

- Duplication across owners -> decide which capability owns the invariant before extracting shared code.
- Duplication inside one UI surface -> decide whether it is local presentation shape or reusable component state.
- Health hotspot -> split by responsibility and public interface, not by arbitrary line count.
- Large module allowlist -> define the intended module split and the metric that removes the allowlist.
- Boundary warning -> decide whether the import is a real violation or the boundary model is wrong.
- Dead export -> decide whether it is dead code, public API, generated contract, dynamic entry, or compatibility shim.
- Suppression/baseline -> decide whether it models reality, hides debt, or needs a cleanup slice.

## Spec Artifact Requirements

In `design.md`, include:

- static analyzer and audit evidence with mode/scope notes
- current-state failure modes
- target-state decisions with `DES-*` IDs
- transition slices and containment gates
- fitness functions and verification plan
- residual transition debt

In `requirements.md`, include requirements that make the transition enforceable:

- ownership and public-surface requirements
- no-new-bypass requirements
- behavior preservation requirements
- analyzer/budget/CI requirements where appropriate
- explicit cleanup requirements for accepted exceptions
- scope-safe reporting requirements so production gates, full inventories, changed-file gates, and accepted baselines are not described as the same thing

In `tasks.md`, sequence work so behavior stays safe:

1. Containment and tests before broad movement.
2. Extract or move one owner/boundary at a time.
3. Update callers through the new public surface.
4. Remove old bypasses and dead paths.
5. Tighten static gates or budgets after the code supports them.
6. Close or reclassify baselines, suppressions, and allowlists.
7. Run full tests or record a low-risk rationale before closing broad refactors, helper extraction, or boundary movement.

## Anti-Patterns

- Spec says "split modules" without naming the owner of each new module.
- Spec says "reduce duplication" without identifying the repeated invariant.
- Tasks chase warning counts while leaving target-state boundaries unspecified.
- Requirements describe desired cleanliness but lack verification.
- Baselines, suppressions, or module-budget allowlists are treated as completion.
- Transition skips containment, so new code can keep adding to the old pattern.
- `fallow audit --changed-since` is treated as a full repo audit.
- Production-only analyzer cleanliness is stated as full-repo cleanliness.
- Duplication budget passes at baseline but no accepted-debt owner or revisit trigger exists.
