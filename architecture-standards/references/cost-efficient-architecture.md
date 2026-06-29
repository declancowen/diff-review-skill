# Cost-Efficient Architecture

Use this when designing or reviewing a material user/system journey, data path, background workflow, integration, realtime mechanism, storage model, or infrastructure decision whose cost can grow with usage, data, time, retries, or operational complexity.

This guidance is agnostic of technology, vendor, and architecture style. It applies to monoliths, services, client-server systems, local-first systems, event-driven systems, managed platforms, and self-hosted infrastructure. It does not assume one design is inherently cheaper.

## Contents

- cost stance and universal cost model
- cost-design workflow and amplification analysis
- context-dependent design practices
- architecture-choice comparisons
- enforcement, evidence, and review smells

## Cost Stance

Treat infrastructure cost as an architecture quality attribute alongside correctness, security, reliability, performance, and maintainability.

- Optimize total cost for the required outcome, not one provider line item.
- Include engineering effort, operational burden, failure recovery, and migration risk when comparing designs.
- Prefer the simplest design that satisfies present correctness, experience, reliability, and scale needs within an acceptable cost curve.
- Do not weaken authorization, correctness, durability, or recovery merely to reduce spend.
- Do not add caches, queues, read models, services, or self-hosted infrastructure unless their total benefit exceeds their complexity and operating cost.
- Revisit decisions when workload shape, pricing model, data volume, or product behavior changes.

Cost efficiency is a design constraint, not a demand to minimize every operation.

## Universal Cost Model

Reason about cost in units that match the selected technology and provider:

```text
total cost
  = fixed baseline
  + executions * work per execution
  + retained data and derived copies
  + data transfer
  + third-party usage
  + operational and engineering overhead
```

For a material journey or workflow, inspect amplification:

```text
journey cost
  = trigger frequency
  * fan-out
  * rerun/retry/reconciliation amplification
  * work per execution
```

The exact billable dimensions vary, but commonly include:

- process/runtime duration, CPU, memory, concurrency, or reserved capacity
- function, request, query, mutation, job, message, or workflow executions
- database rows/documents/bytes read and written, transactions, indexes, and replicas
- network transfer, egress, payload size, and cross-region/cross-service chatter
- primary storage, files, indexes, search/vector data, logs, backups, and retained history
- queue, stream, scheduler, observability, build, deployment, and external API usage
- human operational load, incident response, and specialized infrastructure knowledge

Do not assume fewer requests, fewer services, or lower latency automatically means lower cost. Measure the complete cost path.

Do not assume cached, indexed, no-op, fast, or operationally healthy work is free. It may still incur invocation, connection, lookup, transfer, memory, storage, observability, or downstream invalidation cost.

## Cost-Design Workflow

For a material design:

1. **Name the unit of value.** Examples: active session, page load, search, mutation, uploaded asset, processed job, tenant, or monthly active user.
2. **Map the complete trigger path.** Include UI/render triggers, delivery boundaries, internal calls, queries, writes, invalidations, events, retries, jobs, integrations, and cleanup.
3. **Identify billable work and owners.** Record which layer/capability creates each cost and which team/module can control it.
4. **Calculate amplification.** Include active usage, idle/open-client behavior, fan-out, subscriptions, polling, reconnects, retries, duplicate delivery, write invalidation, derived work, and retained data growth.
5. **Model normal, peak, failure, and recovery cases.** A cheap happy path can become expensive during retries, reconnect storms, backfills, incidents, or large-tenant activity.
6. **Estimate the cost curve.** Use current scale plus credible larger cases. Prefer per-value-unit and per-tenant/workspace estimates over one undifferentiated monthly total.
7. **Choose the simplest proportionate design.** Compare alternatives using correctness, experience, reliability, engineering complexity, and total cost.
8. **Define evidence and guardrails.** Instrument the material dimensions, set budgets/alerts where useful, and prevent known amplification shapes from returning.

Use estimates to guide design, then replace them with measured production evidence.

## Context-Dependent Design Practices

Select only the practices that fit the workload and architecture.

### Demand And Trigger Ownership

- Make work demand-driven where product semantics allow it.
- Identify and justify work performed while no user or system outcome is changing.
- Avoid render loops, polling, heartbeats, scheduled work, retries, and background refreshes whose frequency is disconnected from freshness or correctness needs.
- Scope subscriptions, listeners, streams, and invalidations to the smallest useful audience and lifecycle.
- Include connection duration, reconnect/handshake frequency, open-session count, and inactive/background clients when calculating recurring cost.
- Use freshness classes so every surface does not pay for the strongest realtime guarantee.
- Gate reconnect, focus, online, and retry behavior to avoid synchronized refresh storms.

### Bounded Work

- Bound page size, candidate pools, fan-out, nested expansion, concurrency, retries, batch size, memory, and work per execution.
- Prefer indexed or directly addressable access over broad acquisition followed by local filtering when the datastore/workload supports it.
- Avoid loading a broad tenant/workspace/snapshot merely to authorize or render a narrow action.
- Keep hot-path query and response shapes proportional to the immediate journey.
- Use deterministic pagination or continuation where lists can grow beyond a safe bound.

### Read And Write Amplification

- Count underlying reads/writes and invalidated/recomputed work, not only public requests.
- Suppress semantically unchanged writes when doing so preserves required side effects.
- Make retryable writes idempotent and deduplicate repeated delivery where repetition would multiply work.
- Batch compatible work when it reduces repeated overhead without obscuring correctness or ownership.
- Scope invalidation and recomputation to affected capabilities, tenants, records, or read models where practical.
- Treat derived indexes, search, analytics, notifications, audit, and integrations as write amplification that must be budgeted.

### Materialization, Caching, And Duplication

- Add caches, denormalized data, projections, or read models only when their measured read savings justify write amplification, storage, invalidation, rebuild, and reconciliation costs.
- Define the authoritative source, freshness, lifecycle, and rebuild/recovery path.
- Prefer a cheaper read path only when it preserves authorization and correctness.
- Remove obsolete copies, indexes, projections, logs, and compatibility paths after migrations complete.

### Async And Failure Behavior

- Move work async when it improves user latency, absorbs bursts, or enables efficient batching, not merely to hide expensive work.
- Bound retries and use backoff, jitter, deduplication, dead-letter/recovery, and admission control where relevant.
- Budget failure and replay cost; a degraded dependency must not trigger unbounded retry or fan-out.
- Batch or coalesce events when individual processing has no product value.

### Data Lifecycle And Transfer

- Define retention, archival, deletion, compaction, backup, and rebuild behavior before data grows materially.
- Make cleanup indexed, incremental, bounded, observable, and safe to rerun.
- Budget primary data plus indexes, replicas, search/vector representations, files, logs, backups, and analytics copies.
- Minimize unnecessary payloads, duplicate transfer, cross-region movement, and repeated asset processing.
- Place computation and data to avoid avoidable transfer while preserving reliability and compliance.

### Environments And Operational Work

- Make development, test, preview, staging, and production targets visible and difficult to confuse.
- Prevent tests, agents, local loops, previews, backfills, and load tests from accidentally generating production-scale spend.
- Use dry-run, explicit limits, resumability, and progress visibility for maintenance and migration operations.
- Add spend alerts, quotas, rate/admission controls, or kill switches where runaway cost is credible.
- Attribute costs to capability, journey, environment, tenant, and owner where the platform allows it.

## Architecture Choices

Do not declare an architecture style cheapest by default. Compare its cost curve for the actual workload.

- **Single process vs distributed services:** compare baseline/runtime cost and operational simplicity against independent scaling, isolation, and cross-service chatter.
- **Synchronous vs asynchronous:** compare immediate work and simplicity against queue/workflow executions, retries, storage, and recovery.
- **Pull/poll vs push/subscription/realtime:** compare idle calls and freshness delay against connection/subscription cost, invalidation fan-out, and reruns.
- **Normalized source model vs denormalized/read models:** compare repeated joins/reads against write amplification, storage, invalidation, and rebuild.
- **On-demand vs reserved/provisioned capacity:** compare variable unit cost and cold behavior against idle baseline and utilization.
- **Managed vs self-hosted:** compare provider premium against engineering time, operations, upgrades, reliability, and incident ownership.
- **One store vs specialized stores:** compare simpler ownership against synchronization, duplicated data, transfer, and operational overhead.
- **Client work vs server work:** compare device capability, battery, privacy, consistency, and payloads against centralized compute and repeated processing.

The correct choice is the least costly complete system that meets the current requirements and preserves a credible evolution path.

## Evidence And Enforcement

Use proportionate evidence:

- per-journey or per-value-unit cost estimates
- calls/executions, rows/documents/bytes read and written, duration, memory, payload, egress, storage growth, retries, and fan-out
- top-cost functions, routes, queries, jobs, integrations, tenants, or capabilities
- idle/open-session cost and failure/recovery cost
- before/after comparisons tied to deployments or architecture changes
- large-tenant and high-frequency test fixtures

Possible guardrails:

- static checks against known expensive hot-path shapes
- bounded defaults and maximums encoded in code/configuration
- tests proving no-op write suppression, scoped invalidation, pagination, retention, and retry bounds
- load/cost regression tests for critical journeys
- dashboards, budgets, alerts, anomaly detection, quotas, and kill switches
- review triggers for new subscriptions, polling, scans, fan-out, indexes, derived stores, high-volume jobs, and external calls

Do not treat a budget as proof of efficiency. Budgets expose drift; architecture still determines the cost curve.

## Cost Smells

- meaningful spend while the product is idle or lightly used
- cost scales with open screens/connections rather than useful outcomes
- cached, indexed, no-op, fast, or healthy executions are assumed to be free
- broad snapshots or full-scope reads used for narrow actions
- local filtering after broad acquisition on hot paths
- one write invalidates or recomputes unrelated scopes
- retries, reconnects, listeners, or jobs multiply work invisibly
- unchanged writes repeatedly trigger downstream work
- per-item calls inside growing loops
- unbounded lists, fan-out, history, logs, indexes, or derived copies
- optimization of one bill line that increases total system or engineering cost
- no owner can explain which journeys or capabilities generated the bill
- health/performance dashboards are treated as proof of cost efficiency without usage-cost evidence
- test, preview, local, or automation traffic reaches a costly production path

## Review Output

For a material cost review, report:

- dominant current or expected cost dimensions
- costly journeys and their amplification paths
- idle, peak, failure, recovery, and data-growth exposure
- current guardrails and missing evidence
- proportionate design options with correctness and complexity tradeoffs
- owner, measurement, and revisit trigger for accepted cost risk
