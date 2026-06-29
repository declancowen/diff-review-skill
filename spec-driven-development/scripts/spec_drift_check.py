#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from spec_utils import (
    extract_block_field,
    extract_requirement_links,
    extract_section,
    iter_local_references,
    match_changed_path_to_reference,
    parse_checkbox_blocks,
    parse_frontmatter,
    read_text,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare changed files against spec coverage to detect drift.")
    parser.add_argument("--spec-dir", required=True, help="Path to .spec/<scope>")
    parser.add_argument("--repo-root", help="Override repo root instead of using design.md frontmatter")
    parser.add_argument("--diff-base", help="Git diff base to compare against HEAD, e.g. origin/main")
    parser.add_argument("--changed-file", action="append", default=[], help="Repo-relative changed file")
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
    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path(design_frontmatter.get("repo_root", ""))

    changed_files = [path.strip().lstrip("/") for path in args.changed_file if path.strip()]
    if not changed_files and args.diff_base:
        changed_files = git_changed_files(repo_root, args.diff_base)
    if not changed_files:
        print("ERROR: Provide --changed-file entries or --diff-base.")
        return 1

    changed_files = [path for path in changed_files if not path.startswith(".spec/")]
    if not changed_files:
        print("No code changes to evaluate for spec drift.")
        return 0

    impacted_refs = extract_repo_refs_from_text(
        "\n".join(
            [
                extract_section(design_body, "Repository Discovery Summary"),
                extract_section(design_body, "Impacted Surfaces Matrix"),
                extract_section(design_body, "Change Impact Map"),
            ]
        )
    )
    task_blocks = parse_checkbox_blocks(tasks_body, r"\d+\.\d+")
    task_refs = {
        block.identifier: extract_repo_refs_from_text(extract_block_field(block.text, "Likely areas"))
        for block in task_blocks
    }
    task_requirements = {
        block.identifier: extract_requirement_links(block.text)
        for block in task_blocks
    }

    covered_changed: dict[str, list[str]] = {}
    touched_requirements: set[str] = set()
    all_expected_refs = sorted(set(impacted_refs) | {ref for refs in task_refs.values() for ref in refs})

    for changed in changed_files:
        matches: list[str] = []
        for ref in impacted_refs:
            if match_changed_path_to_reference(changed, ref):
                matches.append(f"design:{ref}")
        for task_id, refs in task_refs.items():
            for ref in refs:
                if match_changed_path_to_reference(changed, ref):
                    matches.append(f"task {task_id}:{ref}")
                    touched_requirements.update(task_requirements.get(task_id, []))
        if matches:
            covered_changed[changed] = matches

    unexpected = [path for path in changed_files if path not in covered_changed]
    untouched_expected = [ref for ref in all_expected_refs if not any(match_changed_path_to_reference(changed, ref) for changed in changed_files)]

    print(f"Spec drift check: {spec_dir.name}")
    print(f"Changed files: {len(changed_files)}")
    print(f"Covered changed files: {len(covered_changed)}")
    print(f"Touched requirements: {', '.join(sorted(touched_requirements)) if touched_requirements else 'none'}")
    if unexpected:
        print("Unexpected changed files:")
        for path in unexpected:
            print(f"- {path}")
    if untouched_expected:
        print("Declared areas without changes in this diff:")
        for ref in untouched_expected:
            print(f"- {ref}")

    if unexpected or not touched_requirements:
        return 1
    return 0


def extract_repo_refs_from_text(text: str) -> list[str]:
    refs = []
    for ref in iter_local_references(text):
        if ref.path.startswith(".spec/") or ref.path.endswith("summary.md"):
            continue
        refs.append(ref.path.rstrip("/"))
    return sorted(set(refs))


def git_changed_files(repo_root: Path, diff_base: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{diff_base}...HEAD"],
        cwd=str(repo_root),
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or "git diff failed")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


if __name__ == "__main__":
    sys.exit(main())
