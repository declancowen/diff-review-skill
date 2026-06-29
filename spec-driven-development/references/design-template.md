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

# Design Document: <Spec Title>

Use this template for `.spec/<scope>/design.md`.

Apply `architecture-standards` while authoring this file.

## Summary
- What is changing
- Why it matters
- What outcome the design enables

## Scope Statement
- What this spec covers
- What implementation boundary this document governs

## Original Plan Alignment Audit
- Original plan or prompt excerpts reviewed:
- Explicit requirements confirmed from the original plan:
- Plan items excluded or deferred, with reason:
- Gaps, contradictions, or stale assumptions found:
- Upstream artifact changes required before continuing:
- Architecture standards reviewed:
- Agent judgment or justified architecture-standard deviations:
- Post-design audit outcome:

## Repository Discovery Summary

### Repo Root
- `<repo-root>`

### Repo-Specific Profile and House Patterns
- Shared repo profile path, if present
- Key local conventions or known footguns that matter to this change

### Entry Points and Execution Path
- User entry points, API routes, jobs, workers, handlers, or commands affected

### Confirmed Code and Runtime Facts
- Concrete paths, symbols, tables, cache keys, env vars, feature flags, or runtime surfaces confirmed in the repository

### Related Code and Pattern Inventory
- Existing repository patterns or analogous implementations that should be reused
- Shared abstractions, helpers, middleware, hooks, services, or migration patterns already present

### Adjacent Pattern Comparison
- Preferred existing pattern
- Why it applies here
- Whether the proposed solution conforms or diverges
- If it diverges, why

### Blast Radius Review
- Shared utilities used by the target code
- Callers of the target code
- Imports into and from the target code
- Sibling modules in the same domain
- Feature flags, config, or env vars affecting the path

### Recent Related Repository History
- Recent related commits, migrations, rollouts, reverts, or incidents that should influence the design

### Impacted Boundaries and Adjacent Systems
- Upstream callers, downstream consumers, integrations, jobs, analytics, support flows, or documentation that could be affected

### Data, Contracts, and Config Surfaces
- Schemas, payloads, events, cache keys, settings, policies, or contracts implicated by the change

### Existing Tests and Operational Signals
- Current tests, monitors, dashboards, alerts, logs, or runbooks that describe or protect the existing behavior

### Static Analyzer and Audit Evidence
- Relevant audit/review artifacts
- Analyzer commands, modes, configs, baselines, suppressions, allowlists, and thresholds
- Duplication, health, module-budget, boundary, or coverage signals that influence the design
- Gate vs advisory inventory distinction
- For each analyzer result: command, `HEAD`, date, mode, scope, baseline or gate, raw result, interpretation, and design impact
- CI parity: package scripts versus CI workflow commands, blocking versus advisory/`continue-on-error`
- Accepted-debt register: owner, reason, cap/budget, evidence command/date, and revisit trigger for baselines, budgets, suppressions, allowlists, or module exceptions

## Problem Statement and Context
- Business or user problem
- Why now
- Failure consequences if the change is wrong

## Current-State Analysis
- Current architecture or flow
- Known limitations, risks, or inefficiencies
- Current coupling, assumptions, and fragility points
- Structural failure modes if this is audit/refactor-driven: unclear ownership, scattered policy, weak boundary, mixed responsibility module, unowned contract, or missing fitness function

## Target-State Architecture
- Intended owner for each durable invariant
- Dependency direction and public surfaces
- Contracts, data ownership, async/reliability, and operational ownership
- Invariant-transfer plan for any moved authority, source of truth, query path, fallback, generated artifact, or public contract: old guarantee, new owner, enforcement mechanism, and proof
- Data admission risk plan for how records, states, references, events, or generated artifacts are allowed into outputs/effects across the chosen implementation shape
- Derived-output risk plan for secondary reads, joins, aggregates, metadata, previews, counters, or generated rows produced from admitted data
- What must stop happening after the transition
- Fitness functions that prove the target state is holding
- Static analyzer fitness functions, if relevant: changed-file gate, production gate, full advisory inventory, duplication budget ratchet, boundary policy, and stale-evidence rule

## Goals
- In-scope outcomes

## Non-Goals
- Explicit exclusions

## Confirmed Facts
- Facts supported by repository evidence

## Assumptions
- Provisional statements that inform thinking but do not yet justify implementation commitments

## Open Questions
- Unresolved items that matter but do not yet block the design
- Use `- None.` when there are none

## Decision Needed
- Use this exact tagging format for each unresolved decision:
  - `[critical|non-critical][domain] description`
- Allowed critical domains include `auth`, `data-model`, `public-contract`, and `rollout`
- Use `- None.` when there are no unresolved decisions

## Proposed Design

### Solution Overview
- The chosen solution and why it fits this repository

### Transition Plan From Current State
- Containment gate that prevents further drift
- Safe implementation slices
- Old bypasses or compatibility paths to remove
- Baselines, suppressions, allowlists, or module-budget caps that remain temporarily
- Revisit trigger for each accepted exception

### End-to-End Flow
- Step-by-step runtime flow after the change

### Component and Module Changes

#### UI or Client
- Affected screens, hooks, components, or clients

#### API or Application Layer
- Routes, handlers, services, orchestrators, or controllers

#### Domain or Business Logic
- Rules, policies, invariants, or orchestration logic

#### Data Model and Persistence
- Schema, storage, indexes, migrations, backfills, caches, or retention changes

#### Integrations, Events, or Background Jobs
- Producers, consumers, retries, replay, ordering, or schedule changes

#### Security and Permissions
- AuthN, authZ, tenancy, secrets, abuse boundaries, and auditability

#### Performance and Scalability
- Hot paths, latency, throughput, concurrency, and capacity implications

#### Observability and Operations
- Logs, metrics, traces, dashboards, alerts, support notes, and runbooks

## Impacted Surfaces Matrix
- UI:
- API:
- Domain logic:
- Persistence:
- Integrations:
- Auth:
- Infra:
- Telemetry:
- Tests:
- Docs:

## Change Impact Map
- Direct impact:
- Indirect impact:
- Unchanged but risk-adjacent areas:

## Invariants and Forbidden Outcomes
- Invariants that must remain true after the change
- Explicit regressions or unsafe states that must never occur
- Stale, deleted, lost-access, legacy-inconsistent, sparse/fallback, and failure-branch variants that must be preserved or deliberately bounded
- If an invariant-transfer, candidate-acquisition, or derived-fetch lens is not applicable, why it is not applicable

## Compatibility Matrix
- Public API:
- Internal API:
- Data schema:
- Events:
- Cache keys:
- Config:
- External consumers:
- Rollback compatibility:
- Use `Not applicable` explicitly where appropriate

## Contract Examples and Before/After Payloads
- Request examples:
- Response examples:
- Event or message examples:
- Before/after comparisons:
- Use `Not applicable` if no contract shape changes exist

## Cross-Cutting Applicability Matrix
- Security:
- Privacy:
- Performance:
- Resilience:
- Migration:
- Observability:
- Supportability:
- Backward compatibility:
- Mark each item as covered or `Not applicable` with a reason

## Success Metrics and Numeric NFR Targets
- Latency targets:
- Throughput or concurrency targets:
- Error-rate or availability targets:
- Timeout, retry, or queue-depth limits:
- Use `Not applicable` with a reason if the change has no numeric NFRs

## Decision Register

### DES-001: <Decision title>
- Context:
- Current-state gap:
- Decision:
- Rationale:
- Tradeoffs:
- Affected surfaces:
- Fitness signal:

### DES-002: <Decision title>
- Context:
- Current-state gap:
- Decision:
- Rationale:
- Tradeoffs:
- Affected surfaces:
- Fitness signal:

## Risk Register
- Risk:
  - Impact:
  - Mitigation:
  - Residual risk:

## Test Impact Matrix
- Existing tests to update:
- New tests required:
- Compatibility tests:
- Rollback-safety tests:
- Use `Not applicable` only with a reason

## Validation Strategy
- Unit validation
- Integration validation
- End-to-end validation
- Migration or rollback validation

## Post-Design Review
- Original plan coverage review:
- Repository evidence review:
- Architecture standards review:
- Requirements readiness:
- Required upstream changes before requirements authoring:
- Performance validation
- Operational validation

## Rollout, Abort, and Reversal
- Rollout strategy
- Feature flags or progressive exposure
- Abort thresholds
- Rollback preconditions
- Reversal mechanics
- Post-deploy checks

## Forbidden Shortcuts and Guardrails
- Unsafe shortcuts explicitly forbidden for this change
- Existing repo conventions that must not be bypassed

## Alternatives Considered
- Alternative:
  - Why rejected:

## Residual Risks
- Risks intentionally accepted after mitigation

## Authoring notes
- Keep every required section, even if the answer is `Not applicable`.
- Name concrete repository paths and symbols whenever known.
- Do not let `Assumptions` or `Decision Needed` items leak into downstream commitments.
