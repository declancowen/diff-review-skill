# Codex Skills

This repository mirrors the local Codex skill pack for review, audit, architecture, static-analysis, demand, and spec-driven planning work.

Primary skills:

- `architecture-standards`
- `diff-review`
- `fallow`
- `notion-demand`
- `repo-audit`
- `spec-driven-development`

## Contents

`architecture-standards`
- Provides architecture guidance for current-state diagnosis, target-state design, refactoring, scaffolding, architectural review, and static-analyzer policy.
- Includes architecture reference packs and `scripts/architecture-preflight.sh`.

`diff-review`
- Reviews local git diffs for bugs, security issues, regressions, external findings, code quality, developer experience, feature gates, and maintainability before pushing.
- Includes review workflow, gates, finding format, remediation-planning handoff, PR automation guidance, static-analysis guidance, stack references, and `scripts/review-preflight.sh`.

`fallow`
- Guides free-version Fallow adoption, configuration, reruns, remediation, and interpretation for TypeScript/JavaScript codebase intelligence.
- Includes Fallow workflow, analysis primitive, package internals, and quality benchmark references.

`notion-demand`
- Orchestrates Recipe Room demand work in the live Notion Product Roadmap and Tasks databases.
- Includes lifecycle mode files for Discovery, Design, Delivery, Launch, and Review work.

`repo-audit`
- Runs full repository audits across correctness, security, architecture-standards alignment, cost efficiency, performance, operability, maintainability, tech debt, and escaped bug patterns.
- Includes audit workflow, gates, finding format, remediation-planning handoff, architecture-standards inverse audit, cost-efficiency audit, deep audit dual-pass guidance, maintainability rubric, escaped-finding learning, PR audit automation guidance, stack references, and `scripts/audit-preflight.sh`.

`spec-driven-development`
- Produces codebase-grounded spec packages for features, refactors, migrations, integrations, architecture transitions, and audit remediation.
- Includes requirement/design/task templates, risk tiering, API/auth/data/event/observability references, spec linting and drift scripts, CI assets, and tests.

## How They Work Together

- `architecture-standards` strengthens both review and audit work by grounding architectural claims in current-state evidence and target-state rules.
- `diff-review` focuses on branch and working-tree changes before they ship.
- `diff-review` and `repo-audit` can turn selected live findings into lightweight executor-ready `plans/` handoff files.
- `fallow` can provide static-analysis evidence for review, audit, and architecture decisions when the target repo uses it.
- `notion-demand` manages product-demand lifecycle artifacts in Notion.
- `repo-audit` focuses on the current repository state and broader health risks.
- `spec-driven-development` turns larger planned changes or remediation work into requirements, design, task, ownership, rollout, and verification artifacts.

The skills work independently, but they are designed to reinforce each other when installed together.

## Layout

```text
.
├── architecture-standards/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── scripts/architecture-preflight.sh
├── diff-review/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── scripts/review-preflight.sh
├── fallow/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── notion-demand/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── modes/
├── repo-audit/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── scripts/audit-preflight.sh
├── spec-driven-development/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── assets/
│   ├── references/
│   ├── scripts/
│   └── tests/
└── README.md
```
