# Delivery — QA Mode

Use this mode when creating or updating linked child tasks with `Lifecycle = Delivery` and `Stage = Testing / QA`.

QA Mode validates that delivered work matches approved requirements, UX, process, solution, technical design, and business scenarios.

## Purpose

QA Mode should build release confidence before Launch.

It should define:

- scenario test coverage;
- acceptance criteria validation;
- regression coverage;
- permissions/security tests;
- UX state tests;
- data/correctness checks;
- edge and failure cases;
- launch blockers;
- sign-off criteria.

## Planning depth

Before creating or expanding tasks in this mode, confirm whether the user wants lightweight coordination or a detailed downstream breakdown when that choice is not already clear.

- Lightweight means one concise checkpoint/plan that developers can use and update while they own detailed tasking.
- Detailed means a fuller set of downstream tasks, subtasks, owners, sequencing, and handoffs.

Default to lightweight only when the user asked for it, detailed tasking would duplicate existing developer-owned planning, or granular tasks already exist.

## Notion mapping

Create or update linked QA child tasks.

Task properties:

| Task field | Expected value |
|---|---|
| `Task` | QA-focused name describing the scenario or release scope under test. |
| `Lifecycle` | `Delivery`. |
| `Stage` | `Testing / QA`. |
| `Status` | Use a valid live task status. |
| `Project` | Relation to parent demand. |

## Inputs to use

Use:

- Requirements;
- UX Design;
- Process Design;
- Solution Design;
- Technical Requirements/Design/Tasks;
- Development outputs;
- known defects/regression risks;
- release constraints.

Do not use QA to create new scope. If QA finds a product/design gap, route it back to the relevant mode or raise a follow-up demand.

## Minimum fact base

Before finalising QA, identify:

1. Business scenarios.
2. Requirements and acceptance criteria.
3. UX states and flows.
4. Permission/state variations.
5. Data/correctness properties.
6. Regression areas.
7. Launch-critical risks.
8. Known defects or incomplete work.

## QA workflow

1. Identify scenarios to test.
2. Map scenarios to requirements.
3. Validate happy paths.
4. Validate edge and failure paths.
5. Validate permission/security states.
6. Validate UX states and copy.
7. Validate data integrity and correctness properties.
8. Validate regression risks.
9. Identify launch blockers.
10. Define sign-off criteria.

## Output contract

```markdown
# QA Plan

## Source context
...

## Scenario coverage
| Scenario | Requirements covered | Test approach |
|---|---|---|
| ... | ... | ... |

## Functional tests
...

## Permission/security tests
...

## UX/state tests
...

## Regression tests
...

## Data/correctness checks
...

## Launch blockers
...

## Sign-off checklist
...

## Open issues / follow-up
...
```

## Review gate

Before marking QA ready for Launch:

- Are all critical requirements covered?
- Are primary and negative paths covered?
- Are permissions and state variations covered?
- Are UX states covered?
- Are data/correctness checks covered?
- Are launch blockers explicit?
- Is sign-off clear?

## Guardrails

Do not:

- accept tests that only prove implementation details while missing required behaviour;
- hide launch blockers;
- add scope without routing it back;
- skip negative paths for risky work.
