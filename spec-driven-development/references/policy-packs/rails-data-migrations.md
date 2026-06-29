# Rails Data Migrations

Load this pack when the change lands in a Rails application or follows Rails-style schema/data migration patterns.

## Focus areas

- schema migration versus data backfill separation
- lock risk and transactional behavior
- background backfill patterns and resumability
- reversible migration expectations
- model callbacks, validations, and migration-time safety
- dual-read or dual-write compatibility windows

## Spec prompts

- Can the change follow expand, migrate, switch, cleanup sequencing?
- Which migrations must remain reversible?
- Which model callbacks or validations are unsafe inside migrations?
- How will the rollout prove data correctness before cleanup?
