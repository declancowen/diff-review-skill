# Repo Audit Skill

Audits a repository's current state for correctness, security, architecture-standards alignment, cost efficiency, performance, operability, maintainability, tech debt, and escaped bug patterns.

## Includes

- `SKILL.md`: operating router for full or focused repo audits, re-audits, external finding triage, optional remediation planning, and clean-conclusion gates.
- `agents/openai.yaml`: agent configuration.
- `scripts/audit-preflight.sh`: collects repo shape, branch/PR context, existing audit/review history, hotspots, risky surfaces, and candidate verification commands.
- `references/`: audit workflow, gates, finding format, remediation-planning handoff, architecture-standards inverse audit, cost-efficiency audit, deep audit dual-pass guidance, maintainability rubric, escaped-finding learning, PR audit automation, static-analysis guidance, stack references, and calibration material.

## Use When

- Auditing a whole repo or high-risk subsystem.
- Assessing code health, architecture, security, performance, or tech debt.
- Importing external findings into an audit ledger.
- Planning prioritized remediation from repo-wide evidence.
- Turning selected live audit findings into executor-ready remediation plans.
