# Escaped Finding Learning

Use this when an external auditer, CI, production signal, or user catches a live issue after a local audit or architecture pass was recorded clean.

The goal is not to add a checklist for the exact bug. The goal is to identify the audit failure mechanism and make the next audit attack that mechanism before clean conclusion.

These lenses are proportional, not mechanical. Use them when the change moves an authority boundary, public contract, source of truth, acquisition path, fallback, generated artifact, or high-risk invariant. For small local changes, a short explicit "not applicable because..." is enough. If a different proof fits the repository better than a listed lens, use it and record the reason.

## Learning Abstraction Rule

Do not add future audit prompts for the exact escaped bug, file, framework, storage engine, entity name, or implementation tactic. Convert the issue into a reusable audit mechanism at the highest useful level.

Use this abstraction ladder:

1. **Incident:** what failed in this repo today. Keep this in the audit ledger.
2. **Mechanism:** the generic failure mode, such as moved authority, unsafe admission, derived propagation, stale reference, contract transfer, cost amplification, or weak verification.
3. **Architecture level:** outcome/intent, ownership/authority, dataflow/materialization, contract/compatibility, operational/cost, or verification/enforcement.
4. **Proof pattern:** what future audits must verify, independent of whether a repo uses filters, queries, joins, guards, policies, reducers, schemas, cache keys, route mappings, or another implementation shape.

Only the mechanism, architecture level, and proof pattern belong in reusable skill guidance.

## Escape Triage

For every escaped live finding, record:

- **Boundary that moved:** which authority, contract, source of truth, persistence path, query path, fallback, or projection changed.
- **Invariant that failed to transfer:** what rule was true before, or should have been true, but was not re-proven in the new path.
- **Acquisition mode:** how the bad record/state entered the output: direct id lookup, scope scan, relation/link expansion, retained/stale reference, fallback page, generated artifact, stream key, cache, optimistic state, or API error branch.
- **Derived sink:** whether the admitted source set also feeds downstream ids, joins, aggregates, metadata fetches, counters, paudits, permission summaries, side effects, or generated rows.
- **Variant missed:** access lost, deleted/tombstoned, legacy-inconsistent data, missing generated binding, empty result, full first page, old client, duplicate scope/name, or stale route/link.
- **Wrong proof used:** selector output, UI visibility, happy-path route shape, old snapshot data, final output admission without checking derived inputs/effects, test fixture narrowness, type success, or lack of current-head external comments.
- **Prevention artifact:** regression test, static guard, invariant helper at the owner boundary, contract test for serialized output, generated freshness check, or audit-ledger prompt.

## Root-Cause Patterns To Generalize

Use these patterns as audit lenses. Do not mention the concrete escaped bug unless it is relevant to the current code.

### Invariant Transfer

When a broad source, snapshot, helper, route, backend authority, or selector is replaced by a narrower path, prove each old invariant transferred deliberately.

Check:

- authorization, tenancy, privacy, and ownership rules
- public route/API status, body, and error-code contracts
- stale/deleted/lost-access behavior
- generated or derived contract freshness
- bounded-read semantics under sparse or tombstoned data
- optimistic/persisted reconciliation

Do not accept "the new path is scoped" as proof. Name where the invariant is enforced now.

### Data Admission

When state, records, references, events, caches, generated artifacts, or external inputs enter an output, state transition, side effect, or persistence path, the owning validity/safety rule must decide whether that data is eligible.

Audit each acquisition mode separately. An eligible parent, event, cache entry, generated row, or retained reference does not automatically make related data or downstream effects eligible.

### Derived ID Propagation

When an admitted or eligible collection is used to derive ids for another fetch, join, aggregate, metadata load, counter, paudit, or generated row, prove those derived inputs came only from authorized sources and are validated again at the target owner when needed.

Trace:

- source candidates before admission
- owner rule applied to decide admission
- ids derived after admission
- downstream fetches that use those ids
- downstream materialized records admitted by their own owner rule

Do not accept "the final output was admitted" if a derived lookup or side effect can still observe or return forbidden targets, metadata, aggregates, participant/member data, child rows, attachments, reactions, or summaries.

### Projection Is Not Authority

Selectors, DTO projections, UI-visible collections, and response shape are not permission proof unless they are explicitly the authoritative boundary. If authorization depends on projected fields being present, check omitted-field selectors and minimal payload variants.

### Access-Loss And Stale Reference

Any retained reference can outlive current access or current existence: notifications, links, bookmarks, route params, subscriptions, stream keys, optimistic state, cache entries, and persisted UI settings.

Before clean conclusion, test or inspect the behavior when the referenced object is missing, deleted, hidden, moved, or no longer readable.

### Bounded Fallback Semantics

Cost fixes that cap reads, pages, retries, or polling must still preserve the user-visible semantic for sparse data. Attack "first page full but all rows unusable", "oldest useful row just outside the first page", and "all candidates filtered out".

If full correctness is intentionally bounded, record the cap, failure behavior, and why it is acceptable.

### Error Contract Transfer

When backend behavior changes from returning `null` or filtered data to throwing, route/API handlers must re-map expected business states to the public contract. Check status, body keys, codes, retryability, logging, and whether access text leaks.

Unexpected infrastructure/provider errors should remain observable and should not be hidden behind not-found handling.

### Generated And Derived Contract Freshness

When adding modules, schema fields, generated clients, route maps, or static guards, prove the derived artifacts used by CI/build/runtime are fresh. Generated-contract failures are architecture contract failures, not clerical noise.

## Audit Procedure After An Escape

1. Import the finding normally.
2. Assign bug classes from `bug-class-taxonomy.md`.
3. Add the escape triage fields above to the audit turn.
4. Sweep sibling paths by **acquisition mode**, not by filename proximity.
5. Re-run the variant that would have caught the issue against the current tree.
6. Before the next clean conclusion, add a short "escape prevention" note: what audit question, test, guard, or architecture rule now prevents the class.

## All-Clear Addendum

If the branch has had an escaped live finding, do not give clean conclusion until:

- the failed invariant was restated in owner/boundary terms
- sibling paths using the same acquisition mode were checked
- downstream derived inputs/effects from admitted candidates were traced and checked
- at least one stale/lost-access/deleted/legacy or failure-branch variant was attacked where relevant
- the public serialized contract was asserted when a route/API contract was involved
- the audit file records why the new proof is stronger than the prior clean audit
