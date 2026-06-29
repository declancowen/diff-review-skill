# Explicit `Not applicable` Examples

Use concise, justified exclusions instead of omitting sections.

## Good examples

- `Data schema: Not applicable. The change only reorders existing UI rendering and does not change persisted state.`
- `Public API: Not applicable. The affected endpoint is internal-only and its payload shape is unchanged.`
- `Migration: Not applicable. No stored records, cache keys, or message formats change.`
- `Operations owner: not-applicable. The change does not alter runtime behavior, alerting, or support workflows.`
- `Target Metrics: Not applicable. This requirement governs access control correctness rather than performance or scale.`

## Bad examples

- `Not applicable.`
- `None.`
- `No changes.`

The exclusion should explain why the section is out of scope for this change.
