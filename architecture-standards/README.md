# Architecture Standards Skill

Provides architecture guidance for current-state diagnosis, target-state design, refactoring, scaffolding, architectural review, and static-analyzer policy.

## Includes

- `SKILL.md`: operating router for architecture diagnosis, design, review, and build support.
- `agents/openai.yaml`: agent configuration.
- `scripts/architecture-preflight.sh`: collects repository shape, architecture signals, hotspots, and candidate verification context.
- `references/`: architecture shapes, layer standards, decision frameworks, enforcement patterns, cost-efficient architecture, design gates, review checklists, and implementation recipes.

## Use When

- Designing or reviewing architecture for a feature, refactor, migration, platform change, or remediation.
- Diagnosing messy current-state architecture and deriving a proportionate target state.
- Checking ownership boundaries, data flow, contracts, cross-cutting concerns, simplicity, or enforcement.
- Strengthening repo-audit, diff-review, spec-driven-development, and static-analysis decisions.
