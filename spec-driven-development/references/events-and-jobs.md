# Events and Jobs Safety Checklist

Use this when the change touches queues, background jobs, schedulers, event producers, or consumers.

## Design coverage

- producer and consumer inventory
- delivery semantics
- retry policy and dead-letter behavior
- idempotency and replay safety
- ordering assumptions
- timeout and concurrency controls
- operational visibility into stuck or poisoned work

## Requirement coverage

- retry and failure semantics
- duplicate delivery or replay behavior
- visibility and alerting expectations

## Task coverage

- producer changes
- consumer changes
- replay or failure-path validation
- operational instrumentation
