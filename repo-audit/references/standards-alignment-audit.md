# Architecture Standards Inverse Audit

Use this for full-repo, architecture, health, messy-repo, or remediation audits. It applies `architecture-standards` in reverse:

- `architecture-standards` starts from desired outcomes and designs the smallest sound architecture.
- `repo-audit` starts from the existing repository, reconstructs its actual architecture, proves where it fails or cannot hold those standards, and designs the safest route back toward alignment.

The audit owns discovery, evidence, risk classification, and current-state diagnosis. Architecture standards supply context-dependent design pressure, target-state choices, proportionality, and enforcement guidance.

## Inverse-Audit Stance

- Audit what the repository actually does, not what folders or architecture documents claim.
- Start from observed code paths, product journeys, failure consequences, runtime evidence, and structural signals.
- Work backward from symptoms to missing owners, weak boundaries, unsafe dataflow, unclear contracts, unbounded work, or absent enforcement.
- Treat a standards difference as a finding only when evidence shows live risk, credible cost/operability exposure, unsafe change pressure, repeated confusion, or a meaningful enforcement gap.
- Record coherent, evidence-backed deviations as intentional choices rather than forcing one architecture style.
- Prefer capability-owned transition slices over broad rewrites.

## Reverse Mapping

Use the architecture standards risk levels as the inverse audit spine:

| Architecture standard | Inverse audit question |
|---|---|
| Outcome and intent | Which important journeys or outcomes does the current shape fail, endanger, or make costly to change? |
| Ownership and authority | Where are invariants, permissions, state, writes, or operations duplicated, bypassable, or unowned? |
| Dataflow and materialization | How can invalid, stale, legacy, or unauthorized data enter and drive secondary work? |
| Contract and compatibility | Where do serialized shapes, errors, schemas, events, clients, jobs, or migrations drift? |
| Operational and cost behavior | Which triggers, fan-out, retries, reads/writes, retention, or failure paths amplify work or spend? |
| Verification and enforcement | Which architecture decisions rely on memory because proof or recurrence guards are missing? |

Trace representative journeys through delivery, application workflow, business policy, data access, infrastructure, integrations, and operations. Folder names are supporting evidence, not the conclusion.

## Current-State Evidence Map

For a full audit, map proportionately:

- capabilities and representative user/system journeys
- delivery entrypoints, application workflows, business policy, data access, infrastructure, and integrations
- sources of truth, authoritative writes, caches/read models/fallbacks, and derived data
- public contracts, compatibility, errors, and serialization
- authentication, authorization, tenancy/scope, and bypass paths
- synchronous/async work, side effects, retries, idempotency, and recovery
- performance and cost paths, including idle work, fan-out, retention, and third parties
- operational ownership, observability, rollout/rollback, and environment boundaries
- test/static/runtime enforcement, exceptions, baselines, and accepted debt

Trace a small set of representative journeys first. Expand only when evidence reveals another architecture shape or risk family.

## Inverse-Audit Workflow

1. Load `architecture-standards` in Governance / Audit and Current-State Diagnosis modes.
2. Describe the actual architecture and representative journeys from code/runtime evidence.
3. Score current-state fitness using the architecture scorecard as an evidence framework; a score is not a finding by itself.
4. Identify symptoms: bugs, duplication, hotspots, bypasses, mixed responsibilities, chatty/unbounded work, cost amplification, weak tests, and stale exceptions.
5. Work backward to the missing architecture guarantee or owner.
6. Classify each gap as live risk, structural pressure, transition debt, accepted deviation, or evidence gap.
7. Derive a proportionate target decision using architecture standards; do not assume the answer before diagnosis.
8. Define containment, complete transition slices, deletion, prevention, proof, and explicit deferred debt.
9. Challenge the remediation with the simplicity gate: it must reduce risk or complexity without speculative architecture.

## Required Alignment Lenses

For full audits, assess each lens or state why it is not materially applicable:

- capability ownership and public boundaries
- dependency direction and separation of concerns
- data ownership, authority, admission, and materialization
- contract ownership and compatibility
- cross-layer context, transaction, consistency, side-effect, and failure semantics
- security and tenancy across all entrypoints and derived paths
- async reliability, retries, idempotency, recovery, and lifecycle
- journey efficiency, bounded work, and material cost amplification
- operability, deployment, rollback, restore, and environment safety
- simplicity, proportionality, testability, and enforcement

## Gap Classification

- **Live risk:** current correctness, security, data, compatibility, reliability, operability, or cost consequence.
- **Structural pressure:** no current failure proven, but repeated complexity, duplication, churn, or weak ownership makes failures credible.
- **Transition debt:** an intended target exists, but old paths, shims, snapshots, bypasses, or exceptions remain.
- **Accepted deviation:** the repo intentionally differs from a general practice, with coherent ownership and evidence.
- **Evidence gap:** architecture may be sound, but tests, runtime data, deployment proof, or operational signals are insufficient.

Do not inflate structural pressure into a production bug. Do not dismiss live risk as "tech debt."

## Alignment Matrix

For repo-level audits, maintain a compact matrix:

```markdown
| Area | Current-state evidence | Missing guarantee or accepted choice | Consequence | Status | Transition / proof |
|---|---|---|---|---|---|
| Data ownership | UI and jobs write the same field directly | authoritative write boundary missing | drift and bypass risk | live risk | contain direct writes; add owned command and boundary test |
```

Group repeated symptoms by root cause. Avoid one row per file when several files expose the same missing architecture concept.

## Remediation Design

For each material gap, define:

- **Owner:** capability/layer responsible for the invariant
- **Containment:** smallest action that stops risk or cost worsening
- **Transition slice:** complete vertical change that moves one journey through the correct owner
- **Deletion:** bypass, duplicate policy, compatibility path, or obsolete mechanism removed
- **Prevention:** test, type, schema, guard, import/static rule, metric, alert, budget, or operational check
- **Proof:** journey, negative variant, sibling/bypass path, and relevant runtime/cost evidence
- **Revisit trigger:** condition that changes the target decision or accepted debt

A remediation that adds more concepts than it removes must justify that complexity with current evidence.

When remediation is requested, hand each proven gap to `architecture-standards` Build Mode one risk-first transition slice at a time, then re-audit the resulting current state before closure.

## Closure

Do not describe a repo as aligned merely because folders resemble layers, docs exist, tests pass, static analysis is clean, or findings were converted into a backlog.

Alignment requires current-state proof, context-appropriate target decisions, a realistic transition path for material gaps, and fitness functions that make recurrence harder.
