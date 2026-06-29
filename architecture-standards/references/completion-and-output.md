# Completion And Output

Use this before finishing architecture-guided implementation, architecture reviews, or repo-level target-state work.

## Implementation Output Standard

For local build work, architecture should be evident in code:

- module/file placement reflects ownership
- exported interfaces are narrow
- authoritative validation is in the owning layer
- framework/vendor details stay at edges where practical
- tests protect meaningful invariants
- repeated boundary violations get stronger enforcement

For final answers, be concise. Mention only material architecture decisions, tradeoffs, enforcement added, and residual risks.

For repo-level architecture reviews, include:

- current-state diagnosis and structural failure modes
- current architecture shape
- intended architecture direction
- target-state design quality: owners, boundaries, contracts, enforcement, and transition feasibility
- transition plan from current state to target state
- ownership gaps
- enforcement mechanisms or missing fitness functions
- accepted exceptions and cleanup paths
- architecture health score and top risks

Avoid vague phrases like "clean architecture" or "best practice" without naming the concrete rule, boundary, enforcement mechanism, or operational risk.

## Broad Review Preflight

For broad architecture reviews, run:

```bash
~/.codex/skills/architecture-standards/scripts/architecture-preflight.sh
```

Use the output to identify module boundaries, architecture docs/specs, config/enforcement signals, high-risk surfaces, and smell clusters. The script is a context collector, not a substitute for reading code.

## Final Check

Before finishing architecture-guided work:

- Did the code land in the owning capability/layer?
- Did the implementation reuse the existing architecture path instead of creating a bypass?
- Is the public surface narrow and explicit?
- Are inner rules free of framework/vendor/transport details where practical?
- Is authoritative validation enforced at the correct layer?
- Were legacy data, old callers, jobs/scripts, and fallback/read-model paths considered where relevant?
- Is the architecture protected by tests, types, schemas, guards, lint/static rules, or dependency boundaries where risk justifies it?
- If the work moved broad presentation code, were representative user-facing screens browser/visually smoke-tested or explicitly scoped out with a reason?
- If analyzer config, duplication exceptions, refactor targets, or module-budget policy changed, does the policy model a real architecture fact rather than hiding debt?
- If broad refactor work changed public surfaces or testability, was production dead-code checked so test-only production exports did not become the new architecture?
- If cost can scale materially, is recurring/idle work, fan-out, retries, retention, and environment usage bounded or explicitly accepted with evidence?
- If a temporary path, exception, suppression, baseline, or allowlist remains, does it have an owner and revisit trigger?
- Were the complete journey, relevant negative variants, sibling/bypass paths, and recurrence guard verified?

If a listed lens is not material, record a short reason rather than forcing ceremony.
