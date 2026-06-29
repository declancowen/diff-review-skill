#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from spec_utils import (
    CROSS_CUTTING_TERMS,
    count_concrete_repo_references,
    extract_decision_needed_items,
    extract_block_field,
    extract_design_decision_ids,
    extract_requirement_ids,
    extract_section,
    normalize_task_status,
    parse_checkbox_blocks,
    parse_frontmatter,
    read_text,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Print or write a reviewer-oriented spec summary.")
    parser.add_argument("--spec-dir", required=True, help="Path to .spec/<scope>")
    parser.add_argument(
        "--format",
        choices=("summary", "pr-comment"),
        default="summary",
        help="Output as a full summary or compact PR comment",
    )
    parser.add_argument("--write", action="store_true", help="Write output into the spec directory")
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

    blocking_decisions = extract_decision_needed_items(design_body)
    critical_blockers = [item for item in blocking_decisions if item[0] == "critical"]
    des_count = len(extract_design_decision_ids(design_body))
    req_count = len(extract_requirement_ids(requirements_body))
    task_count = len(parse_checkbox_blocks(tasks_body, r"\d+\.\d+"))
    spike_count = len(parse_checkbox_blocks(tasks_body, r"SPIKE-\d{3}"))
    execution_counts = summarize_execution_statuses(tasks_body)
    concrete_refs = sum(
        count_concrete_repo_references(body) for body in (design_body, requirements_body, tasks_body)
    )

    cross_cutting = extract_section(requirements_body, "Cross-Cutting Coverage")
    not_applicable = [
        term.rstrip(":")
        for term in CROSS_CUTTING_TERMS
        if term in cross_cutting and "not applicable" in line_for_term(cross_cutting, term).lower()
    ]

    output = (
        build_pr_comment(
            design_frontmatter,
            len(critical_blockers),
            des_count,
            req_count,
            task_count,
            spike_count,
            execution_counts,
            concrete_refs,
            not_applicable,
        )
        if args.format == "pr-comment"
        else build_summary(
            design_frontmatter,
            len(critical_blockers),
            des_count,
            req_count,
            task_count,
            spike_count,
            execution_counts,
            concrete_refs,
            not_applicable,
        )
    )

    print(output)
    if args.write:
        filename = "pr-comment.md" if args.format == "pr-comment" else "summary.md"
        (spec_dir / filename).write_text(output + "\n", encoding="utf-8")
    return 0


def build_summary(
    frontmatter: dict[str, str],
    blocker_count: int,
    des_count: int,
    req_count: int,
    task_count: int,
    spike_count: int,
    execution_counts: dict[str, int],
    concrete_refs: int,
    not_applicable: list[str],
) -> str:
    return "\n".join(
        [
            f"# Spec Summary: {frontmatter.get('title', 'unknown')}",
            "",
            f"- Scope: `{frontmatter.get('scope', 'unknown')}`",
            f"- Status: `{frontmatter.get('status', 'unknown')}`",
            f"- Risk level: `{frontmatter.get('risk_level', 'unknown')}`",
            f"- Owner: `{frontmatter.get('owner', 'unknown')}`",
            f"- Implementation owner: `{frontmatter.get('implementation_owner', 'unknown')}`",
            f"- Operations owner: `{frontmatter.get('operations_owner', 'unknown')}`",
            f"- Blocking decisions: `{blocker_count}`",
            f"- Design decisions: `{des_count}`",
            f"- Requirements: `{req_count}`",
            f"- Implementation tasks: `{task_count}`",
            f"- Blocking spikes: `{spike_count}`",
            "- Execution status counts: "
            + f"`todo={execution_counts['todo']}`, "
            + f"`in-progress={execution_counts['in-progress']}`, "
            + f"`completed={execution_counts['completed']}`, "
            + f"`deferred={execution_counts['deferred']}`, "
            + f"`blocked={execution_counts['blocked']}`",
            f"- Concrete repo path references: `{concrete_refs}`",
            f"- Cross-cutting areas marked not applicable: `{', '.join(not_applicable) if not_applicable else 'none'}`",
        ]
    )


def build_pr_comment(
    frontmatter: dict[str, str],
    blocker_count: int,
    des_count: int,
    req_count: int,
    task_count: int,
    spike_count: int,
    execution_counts: dict[str, int],
    concrete_refs: int,
    not_applicable: list[str],
) -> str:
    status = frontmatter.get("status", "unknown")
    risk = frontmatter.get("risk_level", "unknown")
    title = frontmatter.get("title", "unknown")
    lines = [
        f"## Spec Review Snapshot: {title}",
        "",
        f"- Scope: `{frontmatter.get('scope', 'unknown')}`",
        f"- Status / Risk: `{status}` / `{risk}`",
        f"- Owners: `{frontmatter.get('implementation_owner', 'unknown')}` implementation, `{frontmatter.get('operations_owner', 'unknown')}` operations",
        f"- Traceability: `{des_count}` DES -> `{req_count}` REQ -> `{task_count}` implementation tasks (`{spike_count}` blocking spikes)",
        "- Execution: "
        + f"`{execution_counts['todo']}` todo / "
        + f"`{execution_counts['in-progress']}` in progress / "
        + f"`{execution_counts['completed']}` completed / "
        + f"`{execution_counts['deferred']}` deferred / "
        + f"`{execution_counts['blocked']}` blocked",
        f"- Blocking decisions: `{blocker_count}`",
        f"- Concrete repo refs: `{concrete_refs}`",
        f"- Cross-cutting marked not applicable: `{', '.join(not_applicable) if not_applicable else 'none'}`",
        "",
        "Review focus:",
        "- Confirm the related-code and blast-radius analysis matches the actual repo.",
        "- Confirm compatibility, rollback, and observability coverage are credible for the stated risk.",
        "- Confirm the task plan matches the intended implementation surface and sequencing.",
    ]
    return "\n".join(lines)


def line_for_term(section_text: str, term: str) -> str:
    for line in section_text.splitlines():
        if line.strip().startswith(f"- {term}"):
            return line
    return ""


def summarize_execution_statuses(tasks_body: str) -> dict[str, int]:
    counts = {status: 0 for status in ("todo", "in-progress", "completed", "deferred", "blocked")}
    blocks = parse_checkbox_blocks(tasks_body, r"\d+\.\d+") + parse_checkbox_blocks(
        tasks_body, r"SPIKE-\d{3}"
    )
    for block in blocks:
        status = normalize_task_status(extract_block_field(block.text, "Status"))
        if status in counts:
            counts[status] += 1
    return counts


if __name__ == "__main__":
    sys.exit(main())
