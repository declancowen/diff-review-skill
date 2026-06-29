# Diff Review Skill

Reviews local git diffs before pushing, with emphasis on production risk rather than style feedback.

## Includes

- `SKILL.md`: operating router for diff review, re-review, external finding triage, optional remediation planning, and all-clear gates.
- `agents/openai.yaml`: agent configuration.
- `scripts/review-preflight.sh`: collects branch, PR, changed-file, history, hotspot, and verification context.
- `references/`: workflow, gates, finding format, remediation-planning handoff, PR automation, deep dual-pass review, maintainability rubric, static-analysis guidance, stack references, escaped-finding learning, and calibration material.

## Use When

- Reviewing working-tree, staged, branch, or PR changes.
- Re-reviewing after fixes.
- Triage external GitHub, CI, bot, or user findings.
- Running deep, harsh, or branch-total review before a push.
- Turning selected live review findings into executor-ready remediation plans.
