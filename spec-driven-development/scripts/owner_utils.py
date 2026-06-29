#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path


CODEOWNERS_CANDIDATES = (
    ".github/CODEOWNERS",
    "CODEOWNERS",
    "docs/CODEOWNERS",
)


@dataclass
class CodeownersRule:
    pattern: str
    owners: list[str]


def find_codeowners_file(repo_root: Path) -> Path | None:
    for candidate in CODEOWNERS_CANDIDATES:
        path = repo_root / candidate
        if path.exists():
            return path
    return None


def parse_codeowners(path: Path) -> list[CodeownersRule]:
    rules: list[CodeownersRule] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        rules.append(CodeownersRule(pattern=parts[0], owners=parts[1:]))
    return rules


def match_rule(pattern: str, changed_path: str) -> bool:
    normalized_path = changed_path.strip().lstrip("/")
    normalized_pattern = pattern.strip()
    if normalized_pattern.endswith("/"):
        prefix = normalized_pattern.lstrip("/").rstrip("/")
        return normalized_path == prefix or normalized_path.startswith(prefix + "/")
    anchored = normalized_pattern.lstrip("/")
    if normalized_pattern.startswith("/"):
        return fnmatch(normalized_path, anchored)
    return fnmatch(normalized_path, anchored) or fnmatch(normalized_path, f"*{anchored}")


def owners_for_path(rules: list[CodeownersRule], changed_path: str) -> list[str]:
    matched: list[str] = []
    for rule in rules:
        if match_rule(rule.pattern, changed_path):
            matched = rule.owners
    return matched


def infer_owners(repo_root: Path, changed_paths: list[str]) -> dict[str, str]:
    codeowners_path = find_codeowners_file(repo_root)
    if not codeowners_path:
        return {
            "reviewers": "unassigned",
            "approvers": "unassigned",
            "implementation_owner": "unknown-owner",
            "operations_owner": "not-applicable",
            "codeowners_file": "",
        }

    rules = parse_codeowners(codeowners_path)
    seen: list[str] = []
    owner_counter: Counter[str] = Counter()
    for changed_path in changed_paths:
        for owner in owners_for_path(rules, changed_path):
            owner_counter[owner] += 1
            if owner not in seen:
                seen.append(owner)

    if not seen:
        return {
            "reviewers": "unassigned",
            "approvers": "unassigned",
            "implementation_owner": "unknown-owner",
            "operations_owner": "not-applicable",
            "codeowners_file": str(codeowners_path),
        }

    implementation_owner = owner_counter.most_common(1)[0][0]
    operations_owner = "not-applicable"
    for token in ("sre", "ops", "infra", "platform"):
        match = next((owner for owner in seen if token in owner.lower()), None)
        if match:
            operations_owner = match
            break
    approvers = next((owner for owner in seen if owner.startswith("@")), seen[0])
    return {
        "reviewers": ",".join(seen),
        "approvers": approvers,
        "implementation_owner": implementation_owner,
        "operations_owner": operations_owner,
        "codeowners_file": str(codeowners_path),
    }
