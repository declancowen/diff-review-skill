# Deliver - Development Mode

Use this mode to track build execution and implementation status. It should not invent new scope; it should execute against approved technical tasks and delivery slices.

## Purpose

Maintain the build plan and completion evidence for `DS-*` slices and `TT-*` tasks.

## File

Write to `03-deliver/build-slices.md`. Update `traceability.md` and `qualify.md` when implementation status changes.

## Minimum fact base

Use:

- `03-deliver/delivery-plan.md`;
- `02-design/technical-design/technical-tasks.md`;
- code changes, commits, files, test output, local verification, or implementation notes when available.

## Workflow

1. Read delivery plan and technical tasks.
2. Load/read and apply `$architecture-standards` when available before implementing or changing a material boundary, public contract, source of truth, persistence lifecycle, async workflow, shared abstraction, or operational behavior.
3. For each active slice, list included tasks, status, evidence, and validation state.
4. Record implementation notes only where they help QA, review, support, or future maintenance.
5. At the end of each code-changing `DS-*` slice, load/read and apply the `$diff-review` workflow when available. Use its `.reviews/{content-area}.md` ledger, fix findings, update evidence, and repeat the workflow until clean, blocked, or accepted residual risk.
6. Mark tasks complete only when done criteria, verification evidence, and required slice review status exist.
7. Route scope/design changes back to upstream modes.
8. Update `traceability.md`, `quality-gates.md`, and `qualify.md`.

## Output contract

Use this structure:

```markdown
# Build Slices

Status: In progress
Owner: TBC
Last updated: YYYY-MM-DD
Source artefacts: 03-deliver/delivery-plan.md, 02-design/technical-design/technical-tasks.md
Blocks: none

## Build status summary

## Slice execution
| DS ID | Slice | Included TT IDs | Implementation status | Evidence | QA status | Diff-review status | Blockers |
|---|---|---|---|---|---|---|---|

## Task completion
| TT ID | Task | Done criteria | Evidence | Status | Notes |
|---|---|---|---|---|---|

## Implementation decisions made during delivery
| ID | Decision | Why needed | Upstream impact | Follow-up |
|---|---|---|---|---|

## Local verification
| Check | Command / method | Result | Evidence |
|---|---|---|---|

## Handoff to QA
| DS / TT | What QA must validate | Related TC IDs | Notes |
|---|---|---|---|

## Slice quality review
| DS ID | Architecture check | Verification | Diff-review file / turn | Findings | Branch-interaction proof | Final status |
|---|---|---|---|---|---|---|
```

## Review gate

Development tracking is not ready unless:

- completion status is evidence-backed;
- each code-changing completed slice has a clean, blocked, or accepted-risk diff-review status;
- each slice re-review proves the latest patch did not reopen prior findings or weaken branch-wide assumptions;
- each completed `TT-*` links to validation or QA handoff;
- scope changes are not hidden as implementation notes;
- unresolved blockers are reflected in `qualify.md`.
