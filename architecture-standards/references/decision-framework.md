# Decision Framework

Use this when choosing architecture shape or explaining a meaningful implementation decision.

## Operating Stance

- Start from business capability, user journey, data sensitivity, failure consequence, and ownership, not framework preference.
- Prefer the simplest design that keeps a clean upgrade path.
- Separate policy from mechanism: business rules belong inward; frameworks, vendors, protocols, storage, and UI belong at edges.
- Respect coherent existing architecture. Improve incrementally unless it is actively causing harm.
- For existing systems, derive target-state decisions from current-state evidence: code shape, duplication, hotspots, bypasses, module budgets, analyzer policy, audit findings, and operational failure modes.
- Optimize for evolvability: clear ownership, safe change, testability, and operability under expected growth.

## Frame The Problem

Before designing, identify:

- business capability being implemented
- actors, systems, and teams that depend on it
- greenfield vs extension vs refactor
- current-state architecture gap if this is an existing system
- critical user journeys and failure consequences
- throughput, latency, concurrency, data volume, and growth expectations
- expected cost dimensions, unit-of-value cost, idle/failure amplification, and operational burden
- consistency, ordering, freshness, conflict, and partial-result expectations where state crosses boundaries
- data sensitivity, compliance, auditability, and tenancy model
- operational expectations: uptime, recovery, support, on-call
- integration surface: modules, queues, third-party APIs, reporting, search, storage, background work

If information is missing, state minimal assumptions. Do not design around speculative complexity.

## Proportionality Rule

Increase rigor when:

- failure has financial, legal, operational, security, or reputational cost
- sensitive data, compliance, tenancy, or permissions are involved
- the code is hot-path, high-scale, or low-latency
- cost scales materially with usage, data growth, open sessions, retries, fan-out, retention, or third-party calls
- rules are complex, cross-cutting, or likely to change
- multiple teams or systems depend on the boundary
- external systems or async workflows are involved
- operability, auditability, rollback, or resiliency matter

Reduce ceremony when:

- the change is local, low risk, and easy to reverse
- the code is a thin adapter over an established core
- the lifetime is short and blast radius is genuinely small
- extra layers would mostly add indirection

Complexity must pay rent. If a simpler option does not clearly fail the current correctness, ownership, operability, or scale requirement, use the simpler option.

Even in small work, do not relax security, data correctness, dependency direction, or testability.

Extra invariant-transfer and data-admission proof is proportional. Apply it when authority, contracts, data acquisition, fallback semantics, generated artifacts, or high-risk rules move. For local low-risk changes, state why those lenses do not apply and keep the implementation simple.

## Simplicity Gate

Before choosing a more elaborate shape, state the smallest complete implementation and why it is insufficient. New abstractions, layers, dependencies, shared modules, stores, queues, caches, or frameworks must solve a named present-day problem and provide proof that the added complexity pays for itself.

Prefer:

- one complete vertical slice before broad scaffolding
- capability-local code before shared code
- explicit orchestration before generic frameworks
- existing dependencies and patterns before new ones
- small meaningful duplication before an uncertain abstraction
- deleting or replacing paths before adding parallel paths

For detailed thresholds and AI overcoding smells, load `simplicity-gate.md`.

## Decision Output

For material decisions, make these clear through code or final answer:

- **Decision:** what shape was chosen
- **Current-state gap:** what structural failure or risk this decision addresses
- **Owner:** which module/layer owns the invariant
- **Reason:** requirement, risk, or constraint driving it
- **Tradeoff:** simpler option rejected and why
- **Enforcement:** tests, types, schemas, guards, boundaries, or tooling
- **Fitness signal:** what would prove the target state is holding in code
- **Revisit trigger:** assumption that would change the design
- **Complexity delta:** concepts, dependencies, public surfaces, and runtime mechanisms added versus removed

Avoid vague "best practice" claims. Name the concrete boundary or risk.

## Governance Trigger

Do not create process artifacts for every change. Treat work as a durable architecture decision when it changes:

- module or capability boundary
- broad refactor, duplication reduction, health-hotspot remediation, large-file split, or module-budget exception
- static analyzer policy that encodes boundaries, public API, runtime entry points, ignored paths, baselines, thresholds, suppressions, or production/test scope
- source of truth or data ownership rule
- public API, event, webhook, schema, SDK, or integration contract
- auth, authorization, tenancy, privacy, or audit boundary
- background workflow, queue, stream, scheduler, retry, or idempotency model
- cost model, billing dimension, high-frequency/idle execution path, broad invalidation/fan-out path, or spend-control exception
- shared abstraction used by multiple features or teams
- persistence, migration, retention, archival, or deletion policy
- infrastructure, deployment, observability, or operational ownership
- deliberate exception to an existing architecture rule

When triggered, encode the decision in the implementation boundary first: module placement, public interface, validation location, state ownership, tests, static checks, or runtime guard. If it cannot be encoded directly, state the decision, owner, enforcement gap, and revisit condition in the final answer or in the repo's existing architecture artifact.
