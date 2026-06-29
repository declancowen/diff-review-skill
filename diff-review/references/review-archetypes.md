# Review Archetypes

Use this to choose mandatory checks for a turn. Assign one or more tags at the top of every turn.

## Tags

- `contract`
- `shared-ui`
- `optimistic-state`
- `parallel-entity`
- `fallback-state`
- `migration`
- `release-safety`
- `infra`
- `security`
- `devex`
- `feature-gate`
- `performance`
- `maintainability`

On Turn 2+, tags are based on current branch state plus current-turn delta.

## Contract Stack

When payload fields, schemas, validators, typed errors, or public contracts change, check:

- create / update / patch / rename / delete / import / direct mutation
- route-layer validation
- shared schemas and validators
- client/store validation
- server-wrapper mappings and direct callers
- backend handlers and persistence rules
- optimistic paths and reconciliation
- read-side parsing/normalization
- error mapping and compatibility tests

## Shared UI / Local Forks

When a shared component or one screen-local copy changes, check:

- shared component itself
- screen-local forks and duplicated implementations
- alternate consumers and render surfaces
- hooks/selectors/stores feeding it
- tests at shared level and at least one consumer level

## Optimistic vs Persisted State

Check:

- optimistic payload construction
- server defaults/fallbacks
- sync/update wrapper contract
- reconciliation after success
- failure rollback/retry
- read-side normalization/display helpers

## Parallel Entity Parity

When one entity flow changes, search for the same concept in:

- work items, projects, views, docs, users, teams, labels, or peer domain objects
- sibling services/packages
- client and server copies
- primary and fallback implementations

## Fallback vs Persisted Path

When fallback/local-only state exists beside shared/persisted state, check:

- local-only path
- persisted/shared path
- correction/reconciliation layer
- mutation affordances on both
- tests proving no silent drift

## Migration / Compatibility

Check:

- old stored data
- old client payloads
- create vs update constraints
- idempotency and rollback
- generated clients/types
- backfill ordering and partial failure

## Release Safety

For High/Critical risk, review:

- rollout path
- rollback path
- compatibility window
- feature flag defaults and cleanup
- migration/backfill ordering
- observability and operator recovery

## Developer Experience

When local setup, environment, package scripts, ports, generated files, credentials, or config loading changes, check:

- renamed, moved, added, or newly required env vars
- secrets read from a different source or at a different lifecycle point
- scripts, package-manager commands, task runners, and generated artifacts
- ports, host binding, networking, local proxy, callbacks, and tunnel assumptions
- manual setup steps that did not previously exist
- CI vs local command drift
- docs or examples that still teach the old workflow
- fallback behavior when optional local config is absent

Treat broken local build/run/test flows as review findings when the diff changes the workflow developers rely on.

## Feature Gate / Internal Boundary

When a flag, entitlement, rollout check, internal-only route, beta surface, or conditional exposure changes, check:

- default flag values and missing-flag behavior
- server-side enforcement, not only UI hiding
- read, write, import/export, deep-link, and API bypass paths
- cached or preloaded data that may expose hidden capability
- old clients, disabled tenants, and non-member scopes
- analytics, notifications, search, webhooks, or background jobs that may leak the feature
- cleanup changes that remove a gate before all consumers are ready

Do not assume a feature remains gated because the primary UI path is hidden.

## Security

Check:

- authn/authz on server side
- tenant/scope isolation
- secrets and env exposure
- input validation and output encoding
- dependency/config changes
- non-primary callers that bypass UI/route guards

## Performance / Hot Path

Check:

- render frequency and data size
- query/index assumptions
- fan-out and N+1 paths
- cache invalidation and key scope
- repeated serialization/deep comparisons
- bounded concurrency

## Maintainability / Structure

When a diff adds non-trivial implementation complexity, load `maintainability-rubric.md` and check:

- whether behavior can be preserved with fewer concepts, branches, helpers, or modes
- large file growth and decomposition opportunities
- ad hoc conditionals in already busy flows
- unclear ownership across modules, packages, services, or components
- feature-specific logic leaking into shared paths
- duplicated helpers or missed canonical utilities
- wrappers, casts, optionality, or loose types that obscure invariants
- non-atomic or overly sequential orchestration that makes state harder to reason about
