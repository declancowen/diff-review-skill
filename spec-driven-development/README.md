# Spec Driven Development Skill

Creates codebase-grounded spec packages for features, refactors, migrations, integrations, platform changes, architecture transitions, and audit remediation.

## Includes

- `SKILL.md`: operating router for spec package creation, review loops, implementation planning, and drift checks.
- `agents/openai.yaml`: agent configuration.
- `assets/`: reusable CI asset for spec linting.
- `references/`: design, requirements, task, rollout, risk, policy-pack, and domain guidance.
- `scripts/`: spec initialization, linting, summaries, drift checks, ownership suggestions, and traceability tools.
- `tests/`: tests and golden outputs for the spec tooling.

## Use When

- Turning a codebase-grounded change into `.spec/<scope>/design.md`, `requirements.md`, and `tasks.md`.
- Planning audit remediation, architecture transitions, migrations, integrations, or high-risk refactors.
- Enforcing traceability from design decisions to requirements, tasks, verification, and review records.
- Bootstrapping repo-local spec tooling and CI checks.
