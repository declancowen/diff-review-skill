#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from spec_utils import (
    FRONTMATTER_CONSISTENT_KEYS,
    iter_local_references,
    markdown_heading_anchors,
    parse_frontmatter,
    read_text,
    resolve_reference,
    symbol_exists_in_text,
    validate_frontmatter_fields,
    validate_frontmatter_values,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate local code and file references in a spec.")
    parser.add_argument("--spec-dir", required=True, help="Path to .spec/<scope>")
    parser.add_argument("--repo-root", help="Override repo root instead of using design.md frontmatter")
    parser.add_argument("--min-path-refs", type=int, default=0, help="Minimum number of concrete repo path references required across the package")
    args = parser.parse_args()

    spec_dir = Path(args.spec_dir).resolve()
    paths = [spec_dir / "design.md", spec_dir / "requirements.md", spec_dir / "tasks.md"]
    if not all(path.exists() for path in paths):
        for path in paths:
            if not path.exists():
                print(f"ERROR: Missing required file: {path}")
        return 1

    parsed = [(path, *parse_frontmatter(read_text(path))) for path in paths]
    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path(parsed[0][1].get("repo_root", ""))
    if not str(repo_root):
        print("ERROR: repo_root is missing. Pass --repo-root or add it to design.md frontmatter.")
        return 1

    errors: list[str] = []
    for path, frontmatter, _body in parsed:
        missing = validate_frontmatter_fields(frontmatter)
        if missing:
            errors.append(f"{path.name} missing frontmatter keys: {', '.join(missing)}")
        invalid = validate_frontmatter_values(frontmatter)
        if invalid:
            errors.append(f"{path.name} has invalid frontmatter values: {', '.join(invalid)}")

    for key in FRONTMATTER_CONSISTENT_KEYS:
        values = {frontmatter.get(key) for _, frontmatter, _ in parsed}
        if len(values) > 1:
            errors.append(f"Frontmatter {key} values differ across spec files.")

    concrete_ref_paths: set[str] = set()
    for path, _frontmatter, body in parsed:
        for ref in iter_local_references(body):
            if not ref.path.startswith(".spec/") and not ref.path.endswith("summary.md"):
                concrete_ref_paths.add(ref.path)
        for ref in iter_local_references(body):
            resolved = resolve_reference(repo_root, ref)
            if not resolved.exists():
                errors.append(f"{path.name} references missing path: {ref.path} -> {resolved}")
                continue
            if ref.fragment:
                target_text = read_text(resolved)
                if resolved.suffix == ".md" and ref.fragment_kind == "anchor":
                    anchors = markdown_heading_anchors(target_text)
                    if ref.fragment not in anchors:
                        errors.append(
                            f"{path.name} references missing markdown anchor: {ref.path}#{ref.fragment}"
                        )
                elif ref.fragment_kind == "symbol":
                    if not symbol_exists_in_text(resolved, target_text, ref.fragment):
                        errors.append(
                            f"{path.name} references missing symbol: {ref.path}::{ref.fragment}"
                        )
                else:
                    if ref.fragment not in target_text:
                        errors.append(
                            f"{path.name} references missing symbol or fragment text: {ref.path}::{ref.fragment}"
                        )

    total_concrete_refs = len(concrete_ref_paths)
    if total_concrete_refs < args.min_path_refs:
        errors.append(
            f"Spec references only {total_concrete_refs} concrete repo paths; expected at least {args.min_path_refs}."
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"All local references resolve under {repo_root}")
    print(f"Concrete repo path references: {total_concrete_refs}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
