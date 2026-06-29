# API and Contract Safety Checklist

Use this when the change touches HTTP APIs, RPC methods, events, payloads, serialization, or published interfaces.

## Design coverage

- producer and consumer inventory
- request and response shape changes
- versioning or compatibility window
- validation, defaults, and error semantics
- idempotency and retry behavior
- timeout, rate-limit, and backpressure considerations
- deprecation plan for removed fields or behaviors

## Requirement coverage

- compatibility guarantees
- observable status and error behavior
- negative-path handling
- consumer impact obligations

## Task coverage

- contract tests
- consumer communication or documentation updates
- staged rollout and verification
