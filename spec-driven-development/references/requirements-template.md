---
title: <Spec Title>
scope: <scope>
status: <draft|discovery-blocked|design-ready|requirements-ready|implementation-ready|superseded>
repo_root: <repo-root>
change_class: <feature|refactor|migration|integration|platform|security|ops|bugfix|audit-remediation|architecture-transition|quality-gate>
risk_level: <low|medium|high|critical>
owner: <team-or-person>
reviewers: <comma-separated reviewers>
approvers: <comma-separated approvers>
implementation_owner: <team-or-person>
operations_owner: <team-or-person|not-applicable>
last_updated: YYYY-MM-DD
---

# Requirements Document: <Spec Title>

Use this template for `.spec/<scope>/requirements.md`.

This file is downstream from `design.md`. It must not introduce scope or certainty that the design has not established.

## Source Artifacts
- `.spec/<scope>/design.md`

## Scope Statement
- What requirement set this document governs

## Upstream Alignment Audit
- Original plan requirements reviewed:
- Design decisions reviewed:
- Repository evidence and current tests reviewed:
- Architecture standards implications reviewed:
- Requirements added, changed, or rejected during audit:
- Design updates required before continuing:
- Agent judgment or justified architecture-standard deviations:
- Post-requirements audit outcome:

## Cross-Cutting Coverage
- Security:
- Privacy:
- Performance:
- Resilience:
- Migration:
- Architecture transition:
- Observability:
- Supportability:
- Backward compatibility:
- For each item, cite requirement IDs or state `Not applicable` with a reason

## Requirements

### REQ-FUNC-001: <Capability name>
Source Design Decisions:
- DES-001

Priority: High

Rationale:
- Why this requirement exists

Requirement:
- THE system SHALL ...

Verification Method:
- Unit, integration, end-to-end, manual, operational, or migration verification

Risk if Unmet:
- User, business, security, reliability, or operational consequence

Acceptance Criteria
1. WHEN ...
2. IF ...
3. THEN ...

Negative Cases
1. WHEN ...
2. THEN ...

Notes
- Optional clarifications

### REQ-DATA-001: <Data, contract, or persistence requirement>
Source Design Decisions:
- DES-002

Priority: High

Rationale:
- Why this requirement exists

Requirement:
- THE system SHALL ...

Verification Method:
- Migration, schema, compatibility, or integration verification

Risk if Unmet:
- Data loss, corruption, incompatibility, or rollback failure

Acceptance Criteria
1. ...

Negative Cases
1. ...

### REQ-NFR-001: <Non-functional or operational requirement>
Source Design Decisions:
- DES-001

Priority: Medium

Rationale:
- Why this requirement exists

Requirement:
- THE system SHALL ...

Target Metrics:
- Numeric target or `Not applicable` with a reason

Verification Method:
- Performance, resilience, observability, or operational verification

Risk if Unmet:
- Degraded reliability, support burden, hidden regressions, or failed scale assumptions

Acceptance Criteria
1. ...

Negative Cases
1. ...

### REQ-ARCH-001: <Architecture transition requirement>
Source Design Decisions:
- DES-001

Priority: High

Rationale:
- Which current-state failure mode this prevents from recurring

Requirement:
- THE system SHALL ...

Verification Method:
- Static analyzer gate, module budget, dependency rule, contract test, browser smoke, integration test, or operational verification

Risk if Unmet:
- Ownership drift, boundary bypass, duplicated policy, hidden regression, or permanent transition debt

Acceptance Criteria
1. ...

Negative Cases
1. ...

### REQ-QUAL-001: <Static analyzer quality gate>
Source Design Decisions:
- DES-001

Priority: High

Rationale:
- Which analyzer-backed failure mode this prevents from recurring

Requirement:
- THE system SHALL report and enforce the relevant analyzer gate with command, `HEAD`, date, mode, scope, baseline or budget, result, and accepted-debt status.

Verification Method:
- Static analyzer gate, CI workflow review, preflight output, or audit record

Risk if Unmet:
- False clean conclusions, stale evidence, hidden duplication debt, or non-blocking CI treated as enforcement

Acceptance Criteria
1. WHEN analyzer evidence is used for release or all-clear, THEN production gate, full inventory, changed-file audit, and accepted baseline status are named separately.
2. IF a duplication/health/module budget remains at baseline, THEN owner, cap, reason, evidence date, and revisit trigger are recorded.
3. IF CI and package scripts differ, THEN the requirement names which command blocks and which is advisory.

Negative Cases
1. WHEN only `fallow audit --changed-since` passes, THEN the repo MUST NOT be described as fully clean.
2. WHEN CI uses `continue-on-error`, THEN it MUST NOT be described as a blocking gate.

## Traceability Matrix
- DES-001 -> REQ-FUNC-001, REQ-NFR-001
- DES-002 -> REQ-DATA-001

## Authoring notes
- Every requirement must cite one or more `DES-*` IDs.
- Before authoring requirements, review `design.md`, the original plan, current code evidence, current tests, and applicable architecture standards.
- After authoring requirements, audit them against `design.md`, the original plan, current code evidence, and applicable architecture standards.
- Architecture-standard requirements should be embedded into the relevant functional/data/security/performance requirements as well as any final `REQ-ARCH-*` audit requirement.
- If requirement authoring exposes missing or wrong design intent, update `design.md` first and then revise `requirements.md`.
- Use clear requirement IDs such as `REQ-FUNC-001`, `REQ-DATA-001`, `REQ-SEC-001`, `REQ-NFR-001`, `REQ-OPS-001`, `REQ-ARCH-001`, and `REQ-QUAL-001`.
- Do not use vague verbs without measurable acceptance criteria.
- Include negative-path acceptance criteria for risky or failure-prone behavior.
- For audit/refactor-driven specs, include architecture-transition requirements that define ownership, no-new-bypass behavior, analyzer/budget gates, and cleanup of accepted exceptions.
- If a cross-cutting area is truly out of scope, say `Not applicable` and explain why.
- NFR requirements should prefer numeric targets over adjectives whenever the design governs performance, timing, scale, or reliability.
