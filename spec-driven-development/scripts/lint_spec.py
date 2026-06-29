#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from spec_utils import (
    ALLOWED_TASK_STATUSES,
    CHANGE_IMPACT_TERMS,
    COMPATIBILITY_TERMS,
    CONTRACT_EXAMPLE_TERMS,
    CRITICAL_DECISION_DOMAINS,
    CROSS_CUTTING_TERMS,
    DESIGN_REQUIRED_H2,
    DISCOVERY_SUBHEADINGS,
    EXECUTION_STATUS_TERMS,
    FRONTMATTER_CONSISTENT_KEYS,
    IMPACT_SURFACE_TERMS,
    NFR_TARGET_TERMS,
    REQUIREMENTS_REQUIRED_H2,
    TASKS_REQUIRED_H2,
    TEST_IMPACT_TERMS,
    checkbox_is_checked,
    detect_vague_requirement_words,
    ensure_terms_present,
    extract_block_field,
    extract_decision_needed_items,
    extract_design_decision_ids,
    extract_design_links,
    extract_h2_titles,
    extract_heading_blocks,
    extract_requirement_ids,
    extract_requirement_links,
    extract_section,
    has_numeric_content,
    parse_checkbox_blocks,
    parse_dependency_ids,
    parse_execution_status_summary,
    parse_frontmatter,
    read_text,
    normalize_task_status,
    validate_frontmatter_fields,
    validate_frontmatter_values,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a spec package for structure and traceability.")
    parser.add_argument("--spec-dir", required=True, help="Path to .spec/<scope>")
    args = parser.parse_args()

    spec_dir = Path(args.spec_dir).resolve()
    design_path = spec_dir / "design.md"
    requirements_path = spec_dir / "requirements.md"
    tasks_path = spec_dir / "tasks.md"

    errors: list[str] = []

    for path in (design_path, requirements_path, tasks_path):
        if not path.exists():
            errors.append(f"Missing required file: {path}")

    if errors:
        return fail(errors)

    design_frontmatter, design_body = parse_frontmatter(read_text(design_path))
    requirements_frontmatter, requirements_body = parse_frontmatter(read_text(requirements_path))
    tasks_frontmatter, tasks_body = parse_frontmatter(read_text(tasks_path))

    frontmatters = (
        (design_path, design_frontmatter),
        (requirements_path, requirements_frontmatter),
        (tasks_path, tasks_frontmatter),
    )
    for path, frontmatter in frontmatters:
        missing = validate_frontmatter_fields(frontmatter)
        if missing:
            errors.append(f"{path.name} missing frontmatter keys: {', '.join(missing)}")
        invalid = validate_frontmatter_values(frontmatter)
        if invalid:
            errors.append(f"{path.name} has invalid frontmatter values: {', '.join(invalid)}")

    for key in FRONTMATTER_CONSISTENT_KEYS:
        values = {frontmatter.get(key) for _, frontmatter in frontmatters}
        if len(values) > 1:
            errors.append(f"Frontmatter {key} values differ across spec files.")

    design_headings = extract_h2_titles(design_body)
    requirements_headings = extract_h2_titles(requirements_body)
    tasks_headings = extract_h2_titles(tasks_body)

    for heading in DESIGN_REQUIRED_H2:
        if heading not in design_headings:
            errors.append(f"design.md missing required section: {heading}")
    for heading in REQUIREMENTS_REQUIRED_H2:
        if heading not in requirements_headings:
            errors.append(f"requirements.md missing required section: {heading}")
    for heading in TASKS_REQUIRED_H2:
        if heading not in tasks_headings:
            errors.append(f"tasks.md missing required section: {heading}")

    discovery_text = extract_section(design_body, "Repository Discovery Summary")
    for heading in DISCOVERY_SUBHEADINGS:
        if heading not in discovery_text:
            errors.append(f"design.md Repository Discovery Summary missing subsection: {heading}")

    section_term_groups = (
        ("Impacted Surfaces Matrix", IMPACT_SURFACE_TERMS),
        ("Change Impact Map", CHANGE_IMPACT_TERMS),
        ("Compatibility Matrix", COMPATIBILITY_TERMS),
        ("Contract Examples and Before/After Payloads", CONTRACT_EXAMPLE_TERMS),
        ("Cross-Cutting Applicability Matrix", CROSS_CUTTING_TERMS),
        ("Success Metrics and Numeric NFR Targets", NFR_TARGET_TERMS),
        ("Test Impact Matrix", TEST_IMPACT_TERMS),
    )
    for section_name, terms in section_term_groups:
        missing = ensure_terms_present(extract_section(design_body, section_name), terms)
        if missing:
            errors.append(f"design.md {section_name} missing entries: {', '.join(missing)}")

    missing_cross_cutting = ensure_terms_present(
        extract_section(requirements_body, "Cross-Cutting Coverage"),
        CROSS_CUTTING_TERMS,
    )
    if missing_cross_cutting:
        errors.append(
            "requirements.md Cross-Cutting Coverage missing entries: "
            + ", ".join(missing_cross_cutting)
        )

    missing_execution_terms = ensure_terms_present(
        extract_section(tasks_body, "Execution Status Summary"),
        EXECUTION_STATUS_TERMS,
    )
    if missing_execution_terms:
        errors.append(
            "tasks.md Execution Status Summary missing entries: "
            + ", ".join(missing_execution_terms)
        )

    design_ids = extract_design_decision_ids(design_body)
    if not design_ids:
        errors.append("design.md contains no DES-* entries in the Decision Register.")
    if len(set(design_ids)) != len(design_ids):
        errors.append("design.md contains duplicate DES-* IDs.")

    requirement_blocks = extract_heading_blocks(requirements_body, "REQ-")
    requirement_ids = extract_requirement_ids(requirements_body)
    if not requirement_blocks:
        errors.append("requirements.md contains no REQ-* blocks.")
    if len(set(requirement_ids)) != len(requirement_ids):
        errors.append("requirements.md contains duplicate REQ-* IDs.")

    des_to_req: dict[str, set[str]] = {identifier: set() for identifier in design_ids}
    for block in requirement_blocks:
        required_markers = [
            "Source Design Decisions:",
            "Priority:",
            "Rationale:",
            "Requirement:",
            "Verification Method:",
            "Risk if Unmet:",
            "Acceptance Criteria",
            "Negative Cases",
        ]
        if block.identifier.startswith("REQ-NFR-"):
            required_markers.append("Target Metrics:")
        for marker in required_markers:
            if marker not in block.text:
                errors.append(f"{block.identifier} missing required field or section: {marker}")
        linked_des = extract_design_links(block.text)
        if not linked_des:
            errors.append(f"{block.identifier} does not cite any DES-* IDs.")
        for linked in linked_des:
            if linked not in des_to_req:
                errors.append(f"{block.identifier} cites unknown design decision: {linked}")
            else:
                des_to_req[linked].add(block.identifier)

        requirement_text = block.text
        if "Requirement:" in block.text and "Verification Method:" in block.text:
            requirement_text = block.text.split("Requirement:", 1)[1].split("Verification Method:", 1)[0]
        vague_words = detect_vague_requirement_words(requirement_text)
        if vague_words:
            errors.append(
                f"{block.identifier} uses vague requirement wording: {', '.join(vague_words)}"
            )
        if block.identifier.startswith("REQ-NFR-"):
            target_metrics = extract_block_field(block.text, "Target Metrics")
            if target_metrics and "not applicable" not in target_metrics.lower() and not has_numeric_content(
                target_metrics
            ):
                errors.append(f"{block.identifier} Target Metrics must include numeric targets or an explicit not-applicable reason.")

    for design_id, linked_reqs in des_to_req.items():
        if not linked_reqs:
            errors.append(f"{design_id} is not referenced by any requirement.")

    gating_status = extract_section(tasks_body, "Gating Status")
    tasks_blocked = "blocked" in gating_status.lower()
    package_status = design_frontmatter.get("status", "")
    critical_decisions = [
        item for item in extract_decision_needed_items(design_body) if item[0] == "critical"
    ]
    critical_blockers = [item for item in critical_decisions if item[1] in CRITICAL_DECISION_DOMAINS]

    if critical_blockers and not tasks_blocked:
        errors.append(
            "tasks.md must be blocked while critical Decision Needed items remain in auth, "
            "data-model, public-contract, or rollout."
        )
    if tasks_blocked and package_status == "implementation-ready":
        errors.append("Blocked specs may not use status implementation-ready.")

    task_blocks = parse_checkbox_blocks(tasks_body, r"\d+\.\d+")
    spike_blocks = parse_checkbox_blocks(tasks_body, r"SPIKE-\d{3}")
    execution_summary = parse_execution_status_summary(
        extract_section(tasks_body, "Execution Status Summary")
    )

    if tasks_blocked and task_blocks:
        errors.append("tasks.md contains implementation tasks even though Gating Status is blocked.")
    if not tasks_blocked and not task_blocks:
        errors.append("tasks.md is ready but contains no implementation task blocks.")

    req_to_tasks: dict[str, set[str]] = {identifier: set() for identifier in requirement_ids}
    all_task_ids = {block.identifier for block in task_blocks} | {block.identifier for block in spike_blocks}
    dependency_graph: dict[str, list[str]] = {}
    task_statuses: dict[str, str] = {}

    for block in task_blocks:
        for marker in (
            "Status:",
            "Depends on:",
            "Likely areas:",
            "Validation:",
            "Exit criteria:",
            "Rollback impact:",
            "Blocking unknowns:",
            "Pre-implementation context check:",
            "Test creation review:",
            "Slice review loop:",
            "Post-implementation review:",
            "Spec drift check:",
            "_Requirements:",
        ):
            if marker not in block.text:
                errors.append(f"Task {block.identifier} missing required field: {marker}")
        status = normalize_task_status(extract_block_field(block.text, "Status"))
        if status not in ALLOWED_TASK_STATUSES:
            errors.append(f"Task {block.identifier} has invalid Status: {status or 'missing'}")
        else:
            task_statuses[block.identifier] = status
            if checkbox_is_checked(block.text) and status != "completed":
                errors.append(
                    f"Task {block.identifier} is checked but Status is {status}; checked tasks must be completed."
                )
            if not checkbox_is_checked(block.text) and status == "completed":
                errors.append(
                    f"Task {block.identifier} has Status completed but is not checked."
                )
        linked_reqs = extract_requirement_links(block.text)
        if not linked_reqs:
            errors.append(f"Task {block.identifier} cites no REQ-* IDs.")
        for linked in linked_reqs:
            if linked not in req_to_tasks:
                errors.append(f"Task {block.identifier} cites unknown requirement: {linked}")
            else:
                req_to_tasks[linked].add(block.identifier)
        dependencies = parse_dependency_ids(extract_block_field(block.text, "Depends on"))
        dependency_graph[block.identifier] = dependencies
        for dependency in dependencies:
            if dependency not in all_task_ids:
                errors.append(f"Task {block.identifier} depends on unknown task: {dependency}")

    for block in spike_blocks:
        for marker in ("Status:", "Blocks:", "Likely areas:", "Validation:", "Exit criteria:"):
            if marker not in block.text:
                errors.append(f"Blocking spike {block.identifier} missing required field: {marker}")
        status = normalize_task_status(extract_block_field(block.text, "Status"))
        if status not in ALLOWED_TASK_STATUSES:
            errors.append(f"Blocking spike {block.identifier} has invalid Status: {status or 'missing'}")
        else:
            task_statuses[block.identifier] = status
            if checkbox_is_checked(block.text) and status != "completed":
                errors.append(
                    f"Blocking spike {block.identifier} is checked but Status is {status}; checked tasks must be completed."
                )
            if not checkbox_is_checked(block.text) and status == "completed":
                errors.append(
                    f"Blocking spike {block.identifier} has Status completed but is not checked."
                )
        dependency_graph[block.identifier] = []

    seen_in_summary: set[str] = set()
    for status, ids in execution_summary.items():
        for identifier in ids:
            if identifier not in all_task_ids:
                errors.append(
                    f"Execution Status Summary references unknown task or spike: {identifier}"
                )
                continue
            if identifier in seen_in_summary:
                errors.append(f"Execution Status Summary references {identifier} more than once.")
                continue
            seen_in_summary.add(identifier)
            if task_statuses.get(identifier) != status:
                errors.append(
                    f"Execution Status Summary lists {identifier} as {status}, but its block Status is {task_statuses.get(identifier, 'missing')}."
                )

    untracked = sorted(all_task_ids - seen_in_summary)
    if untracked:
        errors.append(
            "Execution Status Summary does not track these tasks or spikes: "
            + ", ".join(untracked)
        )

    cycle = detect_cycle(dependency_graph)
    if cycle:
        errors.append("Task dependency graph contains a cycle: " + " -> ".join(cycle))

    if not tasks_blocked:
        for requirement_id, linked_tasks in req_to_tasks.items():
            if not linked_tasks:
                errors.append(f"{requirement_id} is not covered by any implementation task.")

    if errors:
        return fail(errors)

    print(f"Spec lint passed: {spec_dir}")
    print(f"Design decisions: {len(design_ids)}")
    print(f"Requirements: {len(requirement_ids)}")
    print(f"Implementation tasks: {len(task_blocks)}")
    print(f"Blocking spikes: {len(spike_blocks)}")
    return 0


def detect_cycle(graph: dict[str, list[str]]) -> list[str]:
    visited: set[str] = set()
    stack: set[str] = set()
    path: list[str] = []

    def visit(node: str) -> list[str]:
        if node in stack:
            cycle_start = path.index(node)
            return path[cycle_start:] + [node]
        if node in visited:
            return []
        visited.add(node)
        stack.add(node)
        path.append(node)
        for neighbor in graph.get(node, []):
            cycle = visit(neighbor)
            if cycle:
                return cycle
        path.pop()
        stack.remove(node)
        return []

    for node in graph:
        cycle = visit(node)
        if cycle:
            return cycle
    return []


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
