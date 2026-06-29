#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from spec_utils import (
    extract_section,
    extract_decision_needed_items,
    extract_design_decision_ids,
    extract_design_links,
    extract_heading_blocks,
    extract_requirement_ids,
    extract_requirement_links,
    parse_checkbox_blocks,
    parse_frontmatter,
    read_text,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Print a DES -> REQ -> TASK traceability report.")
    parser.add_argument("--spec-dir", required=True, help="Path to .spec/<scope>")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on uncovered IDs")
    args = parser.parse_args()

    spec_dir = Path(args.spec_dir).resolve()
    design_path = spec_dir / "design.md"
    requirements_path = spec_dir / "requirements.md"
    tasks_path = spec_dir / "tasks.md"

    missing = [path for path in (design_path, requirements_path, tasks_path) if not path.exists()]
    if missing:
        for path in missing:
            print(f"ERROR: Missing required file: {path}")
        return 1

    design_frontmatter, design_body = parse_frontmatter(read_text(design_path))
    _, requirements_body = parse_frontmatter(read_text(requirements_path))
    _, tasks_body = parse_frontmatter(read_text(tasks_path))

    design_ids = extract_design_decision_ids(design_body)
    requirement_blocks = extract_heading_blocks(requirements_body, "REQ-")
    requirement_ids = extract_requirement_ids(requirements_body)
    task_blocks = parse_checkbox_blocks(tasks_body, r"\d+\.\d+")
    spike_blocks = parse_checkbox_blocks(tasks_body, r"SPIKE-\d{3}")

    des_to_req: dict[str, list[str]] = {identifier: [] for identifier in design_ids}
    req_to_task: dict[str, list[str]] = {identifier: [] for identifier in requirement_ids}

    for block in requirement_blocks:
        for design_id in extract_design_links(block.text):
            if design_id in des_to_req and block.identifier not in des_to_req[design_id]:
                des_to_req[design_id].append(block.identifier)

    for block in task_blocks:
        for requirement_id in extract_requirement_links(block.text):
            if requirement_id in req_to_task and block.identifier not in req_to_task[requirement_id]:
                req_to_task[requirement_id].append(block.identifier)

    critical_blockers = [
        item for item in extract_decision_needed_items(design_body) if item[0] == "critical"
    ]
    tasks_blocked = "blocked" in extract_section(tasks_body, "Gating Status").lower()

    print(f"Spec: {design_frontmatter.get('scope', spec_dir.name)}")
    print(f"Status: {design_frontmatter.get('status', 'unknown')}")
    print(f"Risk level: {design_frontmatter.get('risk_level', 'unknown')}")
    print(f"Blocking decisions: {len(critical_blockers)}")
    print(f"Design decisions: {len(design_ids)}")
    print(f"Requirements: {len(requirement_ids)}")
    print(f"Implementation tasks: {len(task_blocks)}")
    print(f"Blocking spikes: {len(spike_blocks)}")
    print("")
    print("DES -> REQ")
    for design_id in design_ids:
        linked = ", ".join(des_to_req.get(design_id, [])) or "UNMAPPED"
        print(f"- {design_id}: {linked}")
    print("")
    print("REQ -> TASK")
    for requirement_id in requirement_ids:
        linked = ", ".join(req_to_task.get(requirement_id, [])) or "UNMAPPED"
        print(f"- {requirement_id}: {linked}")

    uncovered_des = [identifier for identifier, linked in des_to_req.items() if not linked]
    uncovered_req = [identifier for identifier, linked in req_to_task.items() if not linked]
    if uncovered_des or uncovered_req:
        print("")
        if uncovered_des:
            print("Uncovered design decisions:")
            for identifier in uncovered_des:
                print(f"- {identifier}")
        if uncovered_req:
            print("Uncovered requirements:")
            for identifier in uncovered_req:
                print(f"- {identifier}")
        if args.strict and (uncovered_des or (uncovered_req and not tasks_blocked)):
            return 1
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
