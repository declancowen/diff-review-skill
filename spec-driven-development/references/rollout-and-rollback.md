# Rollout and Rollback Safety Checklist

Use this when the change can affect production behavior materially.

## Design coverage

- rollout shape: big bang, staged, shadow, canary, feature flag, or cohort-based
- prerequisites before release
- abort thresholds and who decides
- rollback mechanics and what is reversible
- data rollback constraints
- post-deploy verification steps

## Requirement coverage

- safe-release expectations
- reversal expectations
- monitoring and verification requirements

## Task coverage

- feature flag or config work
- staged rollout tasks
- post-deploy checks
- rollback rehearsal or documentation
