#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POLICY_PACKS_DIR = ROOT / "references" / "policy-packs"


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap spec-driven development assets into a target repo.")
    parser.add_argument("--repo-root", required=True, help="Target repository root")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--seed-house-patterns", action="store_true", help="Create .spec/_shared/house-patterns.md")
    parser.add_argument("--policy-pack", action="append", default=[], help="Policy pack slug to seed into house-patterns")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    shared_dir = repo_root / ".spec" / "_shared"
    tools_root = shared_dir / "spec-tools"
    tools_dir = tools_root / "scripts"
    policy_pack_dir = shared_dir / "policy-packs"
    workflow_dir = repo_root / ".github" / "workflows"
    shared_dir.mkdir(parents=True, exist_ok=True)
    tools_root.mkdir(parents=True, exist_ok=True)
    tools_dir.mkdir(parents=True, exist_ok=True)
    policy_pack_dir.mkdir(parents=True, exist_ok=True)
    workflow_dir.mkdir(parents=True, exist_ok=True)

    copy_file(
        ROOT / "references" / "repo-profile-template.md",
        shared_dir / "repo-profile.md",
        args.force,
    )
    copy_file(
        ROOT / "assets" / "github-actions-spec-lint.yml",
        workflow_dir / "spec-validation.yml",
        args.force,
    )
    copy_scripts(ROOT / "scripts", tools_dir, args.force)
    copy_policy_packs(policy_pack_dir, args.policy_pack, args.force)

    if args.seed_house_patterns:
        content = build_house_patterns(args.policy_pack)
        write_file(shared_dir / "house-patterns.md", content, args.force)

    print(f"Bootstrapped spec assets into {repo_root}")
    return 0


def build_house_patterns(policy_packs: list[str]) -> str:
    lines = [
        "# House Patterns",
        "",
        "Use this file to document repo-specific architecture and implementation patterns that specs should prefer.",
        "",
        "## Policy Packs",
    ]
    if policy_packs:
        for pack in policy_packs:
            lines.append(f"- Load `.spec/_shared/policy-packs/{pack}.md` when the change matches that stack or domain.")
    else:
        lines.append("- Add repo-relevant policy pack references here.")
    lines.extend(
        [
            "",
            "## Local Conventions",
            "- Document preferred abstractions, naming, testing, migration, rollout, and observability patterns here.",
        ]
    )
    return "\n".join(lines) + "\n"


def copy_file(source: Path, destination: Path, force: bool) -> None:
    content = source.read_text(encoding="utf-8")
    write_file(destination, content, force)


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.write_text(content, encoding="utf-8")


def copy_scripts(source_dir: Path, destination_dir: Path, force: bool) -> None:
    for source in source_dir.glob("*.py"):
        copy_file(source, destination_dir / source.name, force)


def copy_policy_packs(destination_dir: Path, policy_packs: list[str], force: bool) -> None:
    for pack in policy_packs:
        source = POLICY_PACKS_DIR / f"{pack}.md"
        if not source.exists():
            raise SystemExit(f"Unknown policy pack: {pack}")
        copy_file(source, destination_dir / source.name, force)


if __name__ == "__main__":
    raise SystemExit(main())
