# Cost Efficiency Audit

Use this when cost is requested, spend evidence exists, or usage, data, idle work, fan-out, retries, retention, third parties, or operational complexity can create material cost amplification. This is a diagnostic workflow independent of vendor, technology, and architecture style.

Use `architecture-standards/references/cost-efficient-architecture.md` as the target model. This reference discovers and proves where an existing repository fails that model.

## Audit Stance

- Treat cost as an architecture quality attribute, not only an infrastructure configuration issue.
- Optimize total system cost for useful outcomes, including engineering and operational burden.
- Do not assume fast, healthy, cached, indexed, managed, self-hosted, monolithic, distributed, synchronous, asynchronous, push, or pull is inherently cost-efficient.
- Separate measured cost, credible modeled exposure, and unsupported suspicion.
- Do not recommend weakening correctness, security, reliability, durability, or recovery merely to lower spend.

For full audits, determine whether material cost exposure exists. Run a deep cost audit only when evidence or workload justifies it.

## Evidence Hierarchy

Prefer:

1. bills, provider usage, spend dashboards, workload metrics, and production traces
2. function/query/job/route logs with execution, reads/writes, duration, payload, transfer, retry, or fan-out data
3. load tests, seeded large-data tests, and before/after deployment comparisons
4. code/config patterns with a calculable amplification path
5. estimates with explicit assumptions

Operational health and performance dashboards are not proof of cost efficiency. A path may be fast and healthy while executing unnecessarily often.

## Current-State Cost Map

For each material journey or workflow, record:

| Field | Question |
|---|---|
| Useful outcome | What user/system value does the work produce? |
| Trigger | What starts it: action, render, open session, event, schedule, retry, write, or migration? |
| Frequency/lifecycle | How often and how long does it run, including idle/background behavior? |
| Fan-out | How many clients, tenants, records, services, jobs, indexes, or integrations receive work? |
| Rerun amplification | What retries, reconnects, invalidations, reconciliation, or duplicate delivery repeat it? |
| Work per execution | What compute, memory, reads/writes, serialization, transfer, or external usage occurs? |
| Retained/derived cost | What data, indexes, replicas, logs, files, read models, search/analytics copies, or backups grow? |
| Owner and bounds | Who controls it, and what limits prevent runaway work? |
| Evidence | What measured or modeled proof supports the conclusion? |

Use:

```text
journey cost
  = trigger frequency
  * fan-out
  * rerun/retry/reconciliation amplification
  * work per execution
```

Also inspect fixed baseline, retained data, transfer, third parties, and operational overhead.

## Amplification-Path Audit

Trace normal, idle, peak, failure, recovery, and data-growth cases.

### Trigger And Idle Work

Search for polling, subscriptions/listeners, heartbeats, presence, reconnect/focus/online refresh, render/effect loops, schedules, workers, watchers, and work continuing after its owner no longer needs it.

Ask whether frequency and lifecycle match a freshness, correctness, or product requirement.

### Read And Compute Amplification

Search for broad snapshots, full scans/collect-all/load-all, local filtering, missing bounds/pagination, N+1/per-item calls, nested fan-out, repeated authorization/hydration, repeated transforms/media/inference/external calls, and clean public requests hiding large internal work.

Determine whether access remains bounded as data and tenant size grow.

### Write And Invalidation Amplification

Search for semantically unchanged writes, broad invalidation/recomputation, per-write derived indexes/notifications/audit/search/analytics/webhooks, retries without idempotency/deduplication, and client-orchestrated multi-write workflows.

Count downstream work, not only the initial mutation.

### Retention, Transfer, And Environments

Search for unbounded data/history/logs/files/indexes/replicas/backups/derived copies, missing indexed incremental cleanup, large/repeated payloads, duplicate transfer/processing, and development/test/preview/automation targeting costly production paths.

Check quotas, budgets, alerts, rate/admission controls, dry-runs, and kill switches where runaway spend is credible.

## Generic Discovery Commands

Adapt these clues to the repository:

```bash
rg -n 'setInterval|poll|heartbeat|subscribe|listener|reconnect|retry|cron|schedule|worker'
rg -n 'collect|scan|findAll|listAll|SELECT \*|Promise\.all|map\(async|for await'
rg -n 'invalidate|refresh|recompute|rebuild|notify|webhook|analytics|audit'
rg -n 'retention|archive|purge|cleanup|ttl|lifecycle|backup|replica'
rg -n 'budget|quota|spend|cost|usage|billing|rate.?limit|concurrency'
```

Use provider/runtime/CLI insights when available, but do not make provider-specific tooling a prerequisite.

## Finding Calibration

- **Critical:** credible runaway spend, financial control failure, or severe immediate production-cost exposure.
- **High:** dominant or rapidly scaling cost path, unbounded amplification, or costly production behavior without practical control.
- **Medium:** meaningful inefficiency likely to matter with normal growth or repeated usage.
- **Low/Observation:** bounded cold-path inefficiency or evidence gap without demonstrated exposure.

Raise severity when spend is silent, idle-driven, shared, difficult to stop, or multiplied during failure/recovery.

## Remediation And Closure

For each material finding:

- identify architectural root cause and owner
- define immediate containment/spend control
- compare proportionate alternatives using total cost of ownership
- specify the smallest complete transition slice and obsolete paths to delete
- preserve correctness, security, reliability, and user experience
- add prevention: bounded defaults, tests, static checks, metrics, alerts, budgets, quotas, or kill switches
- define before/after evidence and revisit trigger

Do not mark a cost finding resolved because code looks more efficient. Require proportionate proof that amplification is bounded or removed, relevant variants were covered, sibling paths were checked, and before/after evidence or a defensible model exists.
