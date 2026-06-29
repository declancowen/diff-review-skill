# Data Migrations Safety Checklist

Use this when the change touches schemas, stored data, indexes, cache keys, or persistence behavior.

## Design coverage

- current schema and data ownership
- expand, migrate, switch, and cleanup sequencing
- backfill approach and progress visibility
- data integrity checks and reconciliation
- lock, load, and downtime considerations
- rollback safety and what is irreversible
- dual-write, dual-read, or compatibility window if needed

## Requirement coverage

- schema compatibility guarantees
- migration and rollback expectations
- preservation of existing records and semantics
- validation and reconciliation requirements

## Task coverage

- migration creation
- backfill execution
- verification and rollback rehearsal
- cleanup tasks after the compatibility window ends
