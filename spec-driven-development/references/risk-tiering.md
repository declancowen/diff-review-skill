# Risk Tiering

Use this to calibrate depth, not to skip required sections.

## Low

Examples:

- copy-only UI behavior clarifications
- isolated non-breaking internal cleanup

Expected depth:

- concise current-state analysis
- concise impacted surface notes
- explicit `Not applicable` for unused safety sections

## Medium

Examples:

- feature work within an existing bounded area
- refactors that touch shared logic but not public contracts

Expected depth:

- concrete repository discovery
- related-pattern analysis
- explicit validation and rollout notes

## High

Examples:

- data model changes
- new background workflows
- contract changes for internal or external consumers
- auth or permission changes

Expected depth:

- detailed compatibility, failure-mode, migration, and rollback coverage
- strong traceability
- explicit operational readiness and post-deploy checks

## Critical

Examples:

- security-sensitive or privacy-sensitive changes
- public API changes with external consumers
- changes that can cause data loss, corruption, or broad outages

Expected depth:

- exhaustive cross-cutting coverage
- explicit abort thresholds and reversal strategy
- detailed consumer impact and residual risk analysis
- no downstream authoring on unresolved critical design decisions
