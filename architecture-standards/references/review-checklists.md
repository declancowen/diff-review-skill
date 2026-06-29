# Review Checklists

Use this when reviewing architecture or implementation for architectural quality.

## Architecture Review Checklist

- Is the business capability and failure impact clear?
- Does the actual code shape match the claimed architecture, or only the target-state document?
- Does the latest change still fit the accumulated branch architecture, or did it invalidate an earlier branch decision/proof while fixing a local issue?
- Is the chosen architecture proportional, and was a simpler option considered?
- Is the smallest complete design explicit, and is there evidence that any more elaborate shape is necessary now?
- Does every abstraction, dependency, layer, shared surface, and runtime mechanism pay rent through a current requirement or risk?
- Did the design prefer one working vertical slice over broad speculative scaffolding?
- Are module boundaries based on cohesion, ownership, and change patterns?
- Do duplication, health, churn, or module-size signals reveal missing concepts or unclear ownership?
- Are presentation, application, domain, data, infrastructure, and API concerns separated where it matters?
- Does the API boundary simplify callers while preserving clear inward ownership, or merely concentrate every responsibility in one controller, hook, handler, service, or RPC?
- Are framework constructs being treated as delivery mechanisms rather than assumed owners of business logic?
- Are entrypoints, middleware/guards, use cases, domain policy, data access, and infrastructure adapters each limited to the concerns they actually own?
- Are transport DTOs, domain models, and persistence models distinct where differences matter?
- Across meaningful boundaries, are commands/queries/results, error semantics, required context, side-effect timing, and failure behavior explicit without ceremonial wrappers?
- Are transaction, consistency, conflict, ordering, freshness, and partial-result decisions appropriate for the journey rather than accidental framework defaults?
- Is data ownership explicit?
- If authority, contracts, sources of truth, query/acquisition paths, fallbacks, or generated artifacts moved, are old invariants re-proven at the new owner boundary?
- Can invalid related candidates enter through direct id lookup, scope scan, relation/link expansion, stale reference, fallback page, generated artifact, stream key, cache, optimistic state, or API error branch?
- If admitted or eligible candidates feed downstream ids, joins, aggregates, metadata, previews, counters, or generated rows, are those derived fetches based only on authorized candidates and validated again at the target owner where needed?
- Are migrations, indexing, pagination, retention, and expensive query paths considered?
- Are authentication, authorization, tenancy isolation, and secrets handling explicit?
- Are hot paths, N+1 risks, batching opportunities, and latency budgets considered?
- Are request budgets defined around complete user journeys rather than isolated endpoints?
- Does one user action require chatty client CRUD, repeated authorization, partial writes, or broad cache invalidation?
- Does a coarse API hide unbounded database work or over-fetching?
- Where scale matters, are fan-out, concurrency, memory, retries, queue work, and resource lifecycle bounded and observable?
- Were caches, read models, queues, batching, and parallelism selected from evidence and tradeoffs rather than treated as mandatory best practices?
- Where cost can grow materially, is the complete cost curve understood across normal, idle, peak, failure/recovery, retention, transfer, third-party, and operational behavior?
- Can material spend be attributed to useful outcomes, architecture paths, environments, and owners?
- Does the design avoid accidental cost amplification from polling, subscriptions, reconnects, broad invalidation, retries, no-op writes, per-item calls, or unbounded data?
- Were architecture alternatives compared by total cost of ownership without assuming one technology or design style is inherently cheaper?
- Are timeouts, retries, idempotency, duplicate delivery, and partial failure handled?
- Where consequences justify it, are mixed-version rollout/rollback, recovery objectives, and restore/rebuild paths credible and exercised?
- Are logs, metrics, traces, dashboards, and runbooks sufficient for critical paths?
- Can core rules be tested without spinning up the full stack?
- Does the design create clean seams for future extraction or scaling?
- If workload grows 10x, does the system degrade gracefully or break catastrophically?
- If the repo is in transition, are containment gates, transition slices, and accepted debt explicit?
- If Fallow/static analysis exists, are production gates, full inventories, changed-code audits, baselines, and suppressions separated?
- Does CI enforce the same analyzer policy as local scripts, or are some checks advisory/`continue-on-error`?
- Are old analyzer counts tied to `HEAD`, date, command, mode, and scope, or have they gone stale?

## Implementation Review Checklist

- Did the code land in the capability/layer that owns the invariant?
- Did the implementation add only the concepts required for the requested behavior?
- Could any new wrapper, interface, helper, configuration, dependency, or layer be removed without losing behavior or an owned invariant?
- Was uncertain variation kept local until a stable abstraction was demonstrated?
- Did the implementation measure or inspect both client round trips and server/database work for affected journeys?
- Did the change introduce recurring, idle, usage-priced, retained, or derived work; if so, are its outcome, lifecycle, amplification, bound, owner, and evidence explicit?
- Where cost risk is material, does code-level enforcement prevent known expensive shapes from returning?
- Did a capability-level boundary remove presentation/client knowledge without creating an inward god module?
- Did the implementation preserve prior branch fixes and architecture assumptions that touch the same capability, contract, source of truth, or dataflow?
- Did the implementation reuse the existing architecture path instead of creating a bypass?
- Is the public surface narrow enough for callers but explicit enough to avoid hidden policy?
- If this change reduces duplication or health warnings, did it improve ownership and behavior preservation rather than only metrics?
- Are framework/vendor/transport details kept at the edge where practical?
- Is authoritative validation enforced server-side or at the owned domain/application boundary?
- Are legacy data, old callers, direct jobs/scripts, and fallback/read-model paths considered where relevant?
- If the change pulls candidate data from related records or retained references, does every candidate pass its own owned authorization/validity rule before return or persistence?
- If the change derives secondary fetch keys from candidates, do tests or code prove both the derived fetch input and the returned derived records cannot include unauthorized, stale, deleted, or legacy-inconsistent targets?
- If backend behavior or public contracts changed, are failure branches and serialized response/event/storage shapes asserted, not only happy paths?
- Is the architecture protected by code-level enforcement: tests, types, schemas, runtime guards, lint/static rules, or dependency boundaries?
- If a temporary exception was introduced, is its cleanup path visible in code or final implementation notes?
- If analyzer policy changed, does it model a real architecture fact rather than masking current-state failure?
- If duplication or health debt remains budgeted, is there an accepted-debt owner, cap, reason, evidence date, and revisit trigger?
- If the change moved helpers, boundaries, public surfaces, or route/server ownership, did full validation run or is focused-only validation defensibly low risk?

## Anti-Patterns To Flag

- business rules embedded only in controllers, routes, components, ORMs, or SQL
- presentation code calling databases, repositories, or vendor SDKs directly
- one giant service class per feature
- shared helper libraries that become the hidden business layer
- duplicate business rules normalized through generic utilities with no owner
- analyzer baselines, suppressions, or module-budget allowlists treated as architecture completion
- production-only Fallow cleanliness presented as full-repo cleanliness
- duplication budgets raised or held at baseline without accepted-debt ownership
- `fallow audit --changed-since` treated as a full repo audit
- analyzer CI jobs marked `continue-on-error` treated as blocking gates
- APIs/events shaped directly from tables
- caches with no invalidation, TTL, ownership, or fallback behavior
- async workflows with no idempotency, replay, status visibility, or dead-letter handling
- distributed services coupled through shared databases or constant synchronous chatter
- security or observability deferred to "later"
- folder structures that look layered while dependencies are tangled
- indirection added for style rather than a real seam
- speculative extension points, generalized scaffolding, or configuration added for hypothetical future requirements
- interfaces with one implementation and no current boundary need
- wrappers, repositories, managers, or services that only forward calls
- new dependencies or runtime mechanisms without a named current problem and proof
- recurring polling, subscriptions, listeners, heartbeats, reconnects, retries, or jobs with no cost/lifecycle bound
- cached, indexed, fast, or healthy operations treated as evidence that the cost curve is acceptable

## Decision Hygiene

For meaningful architecture decisions, state:

- requirement, risk, or constraint driving it
- why the chosen pattern is proportionate
- simpler option considered
- complexity intentionally avoided
- assumption that would change the design later
- enforcement mechanism that keeps the decision true in code
- if a listed checklist lens does not fit, why it is not applicable rather than forcing a rigid pattern
