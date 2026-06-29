# Repo Profile Template

Use this to create `<repo_root>/.spec/_shared/repo-profile.md`.

This file should be concise and repo-specific. It exists to reduce architectural drift and keep specs aligned with the actual codebase rather than generic best practices.

## Recommended contents

- Repository purpose and major domains
- Preferred architecture and module-boundary rules
- Naming conventions and folder conventions
- Shared abstractions and preferred extension points
- Test strategy and minimum quality gates
- Migration and rollback conventions
- API or event contract conventions
- Auth, tenancy, and security guardrails
- Observability and rollout expectations
- Known footguns, legacy traps, and areas that often regress

## Anti-pattern

- Do not turn this into a giant README.
- Keep only the conventions and history that materially help an agent avoid breaking changes.
