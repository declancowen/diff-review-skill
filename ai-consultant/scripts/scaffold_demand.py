#!/usr/bin/env python3
"""Create the local AI consultant demand folder structure."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


FILES = {
    "qualify.md": "# Qualify\n",
    "quality-gates.md": "# Quality Gates\n",
    "traceability.md": "# Traceability\n",
    "01-discovery/ideation.md": "# Ideation\n",
    "01-discovery/shaping.md": "# Shaping\n",
    "02-design/requirements.md": "# Requirements\n",
    "02-design/ui-cx-journeys.md": "# UI / CX Journeys\n",
    "02-design/process-design.md": "# Process Design\n",
    "02-design/solution-design.md": "# Solution Design\n",
    "02-design/technical-design/technical-requirements.md": "# Technical Requirements\n",
    "02-design/technical-design/technical-design.md": "# Technical Design\n",
    "02-design/technical-design/technical-tasks.md": "# Technical Tasks\n",
    "03-deliver/delivery-plan.md": "# Delivery Plan\n",
    "03-deliver/build-slices.md": "# Build Slices\n",
    "03-deliver/qa-testing.md": "# QA / Testing\n",
    "03-deliver/release.md": "# Release\n",
    "04-review/hypercare-support.md": "# Hypercare / Support\n",
    "04-review/outcomes-benefits.md": "# Outcomes / Benefits\n",
    "04-review/learnings-optimisation.md": "# Learnings / Optimisation\n",
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "untitled-demand"


def metadata(title: str, source: str = "qualify.md") -> str:
    today = date.today().isoformat()
    return (
        f"{title}\n\n"
        "Status: Not started\n"
        "Owner: TBC\n"
        f"Last updated: {today}\n"
        f"Source artefacts: {source}\n"
        "Blocks: none\n\n"
    )


def qualify_template(name: str) -> str:
    today = date.today().isoformat()
    return f"""# Qualify

Status: In progress
Owner: TBC
Last updated: {today}
Source artefacts: user instruction
Blocks: none

## Demand
| Field | Value |
|---|---|
| Name | {name} |
| Summary | TBC |
| Type | TBC |
| Priority | TBC |
| Current lifecycle | Discovery |
| Current mode | Ideation |

## Quality gate summary
| Gate | Status | Evidence | Next action |
|---|---|---|---|
| Architecture Standards | Not started | quality-gates.md | Decide applicability |
| Graphify | Not started | quality-gates.md | Decide applicability |
| Diff Review | Not started | quality-gates.md | Decide applicability |
| Fallow | Not started | quality-gates.md | Decide applicability |
| Repo Audit | Not started | quality-gates.md | Decide applicability |

## Latest instruction

## Selected modes and rationale
| Mode | Use / omit | Rationale | Status | File |
|---|---|---|---|---|

## Plan
| Step | Mode | Goal | Status | Notes |
|---|---|---|---|---|

## Stage checklist
| Stage | File | Status | Blocker |
|---|---|---|---|
| Discovery | 01-discovery/ideation.md | Not started | none |
| Discovery | 01-discovery/shaping.md | Not started | none |
| Design | 02-design/requirements.md | Not started | none |
| Design | 02-design/ui-cx-journeys.md | Not started | none |
| Design | 02-design/process-design.md | Not started | none |
| Design | 02-design/solution-design.md | Not started | none |
| Design | 02-design/technical-design/technical-requirements.md | Not started | none |
| Design | 02-design/technical-design/technical-design.md | Not started | none |
| Design | 02-design/technical-design/technical-tasks.md | Not started | none |
| Deliver | 03-deliver/delivery-plan.md | Not started | none |
| Deliver | 03-deliver/build-slices.md | Not started | none |
| Deliver | 03-deliver/qa-testing.md | Not started | none |
| Deliver | 03-deliver/release.md | Not started | none |
| Review | 04-review/hypercare-support.md | Not started | none |
| Review | 04-review/outcomes-benefits.md | Not started | none |
| Review | 04-review/learnings-optimisation.md | Not started | none |

## Open decisions and blockers
| ID | Decision / blocker | Impact | Owner | Status |
|---|---|---|---|---|

## Assumptions
| ID | Assumption | Why acceptable for now | Validation |
|---|---|---|---|

## Next recommended action
"""


def quality_gates_template() -> str:
    today = date.today().isoformat()
    return f"""# Quality Gates

Status: In progress
Owner: TBC
Last updated: {today}
Source artefacts: qualify.md
Blocks: none

## Gate availability and applicability
| Gate | Skill | Available? | Applicable? | Status | Evidence | Notes |
|---|---|---|---|---|---|---|
| Architecture Standards | `$architecture-standards` | TBC | TBC | Not started |  | Load/read and apply throughout architecture, technical design and delivery decisions when available |
| Graphify codebase map | `$graphify` | TBC | TBC | Not started |  | Apply for codebase-aware consultation; create the first graph, then update on later consultations |
| Slice diff review | `$diff-review` | TBC | TBC | Not started |  | Load/read and apply after every implemented delivery slice |
| Final diff review | `$diff-review` | TBC | TBC | Not started |  | Load/read and apply after Fallow, repo-audit and remediation |
| Fallow static analysis | `$fallow` | TBC | TBC | Not started |  | Load/read and apply for TypeScript/JavaScript or configured Fallow repos |
| Repo audit | `$repo-audit` | TBC | TBC | Not started |  | Load/read and apply for material/broad codebase changes or final whole-repo confidence |

## Architecture Standards checkpoints
| Checkpoint | Applies to | Decision / evidence | Status | Follow-up |
|---|---|---|---|---|

## Graphify codebase map
| Run | Scope | Mode | Outputs | Key signals used | Status |
|---|---|---|---|---|---|

## Per-slice review loop
| DS ID | Slice | Architecture checkpoint | Verification | Review file / turn | Diff-review result | Findings / fixes | Branch-interaction proof | Final status |
|---|---|---|---|---|---|---|---|---|

## Fallow evidence
| Run | Run state | Commands / mode | Findings | Fixes / exceptions | Status | Evidence |
|---|---|---|---|---|---|---|

## Repo-audit evidence
| Run | Scope | Audit file / turn | Findings | Remediation slices | Status | Evidence |
|---|---|---|---|---|---|---|

## Final quality closure
| Gate | Required final state | Current state | Blocker / accepted risk |
|---|---|---|---|
| Slice diff reviews | Clean or accepted residual risk | Not started | none |
| Fallow | Clean, not applicable, or accepted residual risk | Not started | none |
| Repo audit | Clean, not applicable, or accepted residual risk | Not started | none |
| Final diff review | Clean or accepted residual risk | Not started | none |

## Open quality findings
| ID | Source gate | Severity | Finding | Owner | Remediation slice | Status |
|---|---|---|---|---|---|---|
"""


def traceability_template() -> str:
    today = date.today().isoformat()
    return f"""# Traceability

Status: In progress
Owner: TBC
Last updated: {today}
Source artefacts: qualify.md
Blocks: none

## End-to-end traceability
| Business design | Business requirement | UX / CX | Process | Solution | Technical requirement | Technical task | Delivery slice | Test case | Defect / issue | Release check | Review metric | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Completion checklist
- [ ] Business design is represented by `BD-*`
- [ ] Business requirements are represented by `BR-*`
- [ ] Technical requirements map back to business requirements
- [ ] Delivery slices cover technical tasks and must-have requirements
- [ ] QA test cases cover requirements and technical tasks
- [ ] Open defects or failed validations are linked to affected requirements and release checks
- [ ] Release checks reflect QA and support readiness
- [ ] Review metrics map back to intended outcomes
"""


def create_demand(root: Path, name: str, force: bool) -> Path:
    demand_dir = root / slugify(name)
    demand_dir.mkdir(parents=True, exist_ok=True)

    for rel_path, title in FILES.items():
        path = demand_dir / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and not force:
            continue

        if rel_path == "qualify.md":
            content = qualify_template(name)
        elif rel_path == "quality-gates.md":
            content = quality_gates_template()
        elif rel_path == "traceability.md":
            content = traceability_template()
        else:
            content = metadata(title.rstrip(), "qualify.md")
        path.write_text(content, encoding="utf-8")

    return demand_dir


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Demand name")
    parser.add_argument(
        "--root",
        default="AI consultant",
        help="Root folder for demand workspaces. Defaults to 'AI consultant'.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files. Existing files are preserved by default.",
    )
    args = parser.parse_args()

    demand_dir = create_demand(Path(args.root), args.name, args.force)
    print(demand_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
