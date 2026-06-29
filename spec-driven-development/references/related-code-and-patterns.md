# Related Code and Pattern Analysis

Read this during repository discovery. The goal is to stop the spec from describing a change as if it lives alone.

## Mandatory questions

- Which sibling feature already solves a similar problem?
- Which shared abstraction, helper, middleware, hook, service, or base component is already responsible for this concern?
- Which adjacent caller or consumer will observe the change first?
- Which hidden coupling points exist: config, cache keys, env vars, events, permissions, indexes, templates, or docs?
- Which tests already lock in the current behavior?
- Which release, migration, rollback, or observability pattern is already used in this area?
- Which existing pattern is the preferred one for this change, and why?
- If the proposed change diverges from that pattern, why is the divergence justified?
- Which imports into and from the target code reveal hidden coupling?
- Which recent related commits, reverts, incidents, or migrations should shape the proposal?

## Evidence to capture

- repo-relative code paths
- key symbols or modules
- analogous implementation pattern
- adjacent pattern comparison
- blast-radius notes across callers, consumers, siblings, and shared utilities
- recent relevant repository history
- adjacent system or consumer impact
- existing tests and operational signals
- any place the proposed change diverges from a known pattern

## Failure modes this check is meant to prevent

- introducing a new pattern where a safe existing one already exists
- changing a shared abstraction without noticing its other consumers
- documenting a local fix that breaks adjacent flows
- missing required telemetry, auth, migration, or rollback patterns already established elsewhere in the repo
- repeating a previously reverted or problematic approach because repo history was ignored
