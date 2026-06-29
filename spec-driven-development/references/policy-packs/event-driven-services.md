# Event-Driven Services

Load this pack when the design touches queues, event buses, workflow engines, background consumers, or asynchronous orchestration.

## Focus areas

- producer and consumer ownership boundaries
- event versioning and compatibility windows
- retry, timeout, idempotency, deduplication, and dead-letter handling
- ordering guarantees and replay safety
- poison message handling and operational visibility
- eventual consistency and user-facing lag

## Spec prompts

- Which events are authoritative and who owns their schema?
- What happens on duplicate delivery, replay, or out-of-order arrival?
- How will operators detect stuck or poisoned work?
- Which consumers break if the event changes shape?
