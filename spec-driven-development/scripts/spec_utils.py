#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FRONTMATTER_KEYS = (
    "title",
    "scope",
    "status",
    "repo_root",
    "change_class",
    "risk_level",
    "owner",
    "reviewers",
    "approvers",
    "implementation_owner",
    "operations_owner",
    "last_updated",
)

FRONTMATTER_CONSISTENT_KEYS = (
    "title",
    "scope",
    "status",
    "repo_root",
    "change_class",
    "risk_level",
    "owner",
    "reviewers",
    "approvers",
    "implementation_owner",
    "operations_owner",
)

ALLOWED_STATUS_VALUES = {
    "draft",
    "discovery-blocked",
    "design-ready",
    "requirements-ready",
    "implementation-ready",
    "superseded",
}

ALLOWED_CHANGE_CLASSES = {
    "feature",
    "refactor",
    "migration",
    "integration",
    "platform",
    "security",
    "ops",
    "bugfix",
    "audit-remediation",
    "architecture-transition",
    "quality-gate",
}

ALLOWED_RISK_LEVELS = {"low", "medium", "high", "critical"}

DESIGN_REQUIRED_H2 = (
    "Summary",
    "Scope Statement",
    "Original Plan Alignment Audit",
    "Repository Discovery Summary",
    "Problem Statement and Context",
    "Current-State Analysis",
    "Target-State Architecture",
    "Goals",
    "Non-Goals",
    "Confirmed Facts",
    "Assumptions",
    "Open Questions",
    "Decision Needed",
    "Proposed Design",
    "Impacted Surfaces Matrix",
    "Change Impact Map",
    "Invariants and Forbidden Outcomes",
    "Compatibility Matrix",
    "Contract Examples and Before/After Payloads",
    "Cross-Cutting Applicability Matrix",
    "Success Metrics and Numeric NFR Targets",
    "Decision Register",
    "Risk Register",
    "Test Impact Matrix",
    "Validation Strategy",
    "Post-Design Review",
    "Rollout, Abort, and Reversal",
    "Forbidden Shortcuts and Guardrails",
    "Alternatives Considered",
    "Residual Risks",
)

REQUIREMENTS_REQUIRED_H2 = (
    "Source Artifacts",
    "Scope Statement",
    "Upstream Alignment Audit",
    "Cross-Cutting Coverage",
    "Requirements",
    "Traceability Matrix",
)

TASKS_REQUIRED_H2 = (
    "Source Artifacts",
    "Gating Status",
    "Execution Status Summary",
    "Sequencing Notes",
    "Implementation Authority And Review Loop",
    "Blocking Work",
    "Tasks",
    "Post-Deploy Verification",
    "Traceability Matrix",
    "Coverage Checklist",
)

DISCOVERY_SUBHEADINGS = (
    "Repo Root",
    "Repo-Specific Profile and House Patterns",
    "Entry Points and Execution Path",
    "Confirmed Code and Runtime Facts",
    "Related Code and Pattern Inventory",
    "Adjacent Pattern Comparison",
    "Blast Radius Review",
    "Recent Related Repository History",
    "Impacted Boundaries and Adjacent Systems",
    "Data, Contracts, and Config Surfaces",
    "Existing Tests and Operational Signals",
    "Static Analyzer and Audit Evidence",
)

IMPACT_SURFACE_TERMS = (
    "UI:",
    "API:",
    "Domain logic:",
    "Persistence:",
    "Integrations:",
    "Auth:",
    "Infra:",
    "Telemetry:",
    "Tests:",
    "Docs:",
)

CHANGE_IMPACT_TERMS = (
    "Direct impact:",
    "Indirect impact:",
    "Unchanged but risk-adjacent areas:",
)

COMPATIBILITY_TERMS = (
    "Public API:",
    "Internal API:",
    "Data schema:",
    "Events:",
    "Cache keys:",
    "Config:",
    "External consumers:",
    "Rollback compatibility:",
)

CROSS_CUTTING_TERMS = (
    "Security:",
    "Privacy:",
    "Performance:",
    "Resilience:",
    "Migration:",
    "Observability:",
    "Supportability:",
    "Backward compatibility:",
)

CONTRACT_EXAMPLE_TERMS = (
    "Request examples:",
    "Response examples:",
    "Event or message examples:",
    "Before/after comparisons:",
)

NFR_TARGET_TERMS = (
    "Latency targets:",
    "Throughput or concurrency targets:",
    "Error-rate or availability targets:",
    "Timeout, retry, or queue-depth limits:",
)

TEST_IMPACT_TERMS = (
    "Existing tests to update:",
    "New tests required:",
    "Compatibility tests:",
    "Rollback-safety tests:",
)

EXECUTION_STATUS_TERMS = (
    "To do:",
    "In progress:",
    "Completed:",
    "Deferred:",
    "Blocked:",
)

ALLOWED_TASK_STATUSES = {
    "todo",
    "in-progress",
    "completed",
    "deferred",
    "blocked",
}

CRITICAL_DECISION_DOMAINS = {
    "auth",
    "data-model",
    "public-contract",
    "rollout",
}

VAGUE_REQUIREMENT_WORDS = {
    "support",
    "supports",
    "supported",
    "improve",
    "improves",
    "improved",
    "handle",
    "handles",
    "handled",
}

PATHLIKE_SUFFIXES = (
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".mjs",
    ".cjs",
    ".py",
    ".rb",
    ".go",
    ".java",
    ".kt",
    ".rs",
    ".sql",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".md",
    ".sh",
    ".graphql",
)


@dataclass
class Block:
    identifier: str
    text: str


@dataclass(frozen=True)
class LocalReference:
    raw: str
    path: str
    fragment: str = ""
    fragment_kind: str = ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    raw_frontmatter = parts[0].splitlines()[1:]
    body = parts[1]
    data: dict[str, str] = {}
    for line in raw_frontmatter:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def extract_h2_titles(text: str) -> set[str]:
    return {match.group(1).strip() for match in re.finditer(r"^##\s+(.+)$", text, re.M)}


def extract_section(text: str, title: str, level: int = 2) -> str:
    pattern = rf"^{'#' * level}\s+{re.escape(title)}\s*$\n(.*?)(?=^{'#' * level}\s+|^\#{{1,{level - 1}}}\s+|\Z)"
    match = re.search(pattern, text, re.M | re.S)
    return match.group(1).strip() if match else ""


def extract_heading_blocks(text: str, prefix: str) -> list[Block]:
    matches = list(re.finditer(rf"^###\s+({re.escape(prefix)}[A-Z0-9-]*\d{{3}}):\s+.+$", text, re.M))
    boundaries = [match.start() for match in re.finditer(r"^(?:##|###)\s+.+$", text, re.M)]
    boundaries.append(len(text))
    blocks: list[Block] = []
    for match in matches:
        start = match.start()
        end = next(boundary for boundary in boundaries if boundary > start)
        blocks.append(Block(identifier=match.group(1), text=text[start:end].strip()))
    return blocks


def extract_design_decision_ids(text: str) -> list[str]:
    return re.findall(r"^###\s+(DES-\d{3}):", text, re.M)


def extract_requirement_ids(text: str) -> list[str]:
    return re.findall(r"^###\s+(REQ-[A-Z]+-\d{3}):", text, re.M)


def parse_checkbox_blocks(text: str, id_pattern: str) -> list[Block]:
    lines = text.splitlines()
    blocks: list[Block] = []
    start_re = re.compile(rf"^(?P<indent>\s*)- \[[ xX]\] (?P<id>{id_pattern})\s+.+$")
    checkbox_re = re.compile(r"^(?P<indent>\s*)- \[[ xX]\] .+$")
    index = 0
    while index < len(lines):
        match = start_re.match(lines[index])
        if not match:
            index += 1
            continue
        start_indent = len(match.group("indent"))
        block_lines = [lines[index]]
        index += 1
        while index < len(lines):
            if re.match(r"^##\s+.+$", lines[index]):
                break
            next_checkbox = checkbox_re.match(lines[index])
            if next_checkbox and len(next_checkbox.group("indent")) <= start_indent:
                break
            block_lines.append(lines[index])
            index += 1
        blocks.append(Block(identifier=match.group("id"), text="\n".join(block_lines).strip()))
    return blocks


def checkbox_is_checked(block_text: str) -> bool:
    first_line = block_text.splitlines()[0] if block_text.splitlines() else ""
    return first_line.lstrip().startswith("- [x]") or first_line.lstrip().startswith("- [X]")


def extract_decision_needed_items(text: str) -> list[tuple[str, str, str]]:
    section = extract_section(text, "Decision Needed")
    results: list[tuple[str, str, str]] = []
    for line in section.splitlines():
        match = re.match(r"^- \[(critical|non-critical)\]\[([a-z-]+)\]\s+(.+)$", line.strip())
        if match:
            results.append((match.group(1), match.group(2), match.group(3)))
    return results


def extract_requirement_links(block_text: str) -> list[str]:
    return re.findall(r"(?<![A-Z0-9-])(REQ-[A-Z]+-\d{3})(?!\d)", block_text)


def extract_design_links(block_text: str) -> list[str]:
    return re.findall(r"(?<![A-Z0-9-])(DES-\d{3})(?!\d)", block_text)


def extract_block_field(block_text: str, label: str) -> str:
    for line in block_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            stripped = stripped[2:].strip()
        if stripped.startswith(label):
            return stripped.split(":", 1)[1].strip()
    return ""


def normalize_task_status(value: str) -> str:
    normalized = value.strip().lower().replace("_", "-")
    aliases = {
        "to-do": "todo",
        "to do": "todo",
        "todo": "todo",
        "in-progress": "in-progress",
        "in progress": "in-progress",
        "wip": "in-progress",
        "done": "completed",
        "complete": "completed",
        "completed": "completed",
        "deferred": "deferred",
        "blocked": "blocked",
    }
    return aliases.get(normalized, normalized)


def parse_execution_status_summary(section_text: str) -> dict[str, list[str]]:
    label_map = {
        "to do": "todo",
        "in progress": "in-progress",
        "completed": "completed",
        "deferred": "deferred",
        "blocked": "blocked",
    }
    summary = {status: [] for status in label_map.values()}
    for line in section_text.splitlines():
        stripped = line.strip()
        match = re.match(r"^- ([A-Za-z ]+):\s*(.+)$", stripped)
        if not match:
            continue
        raw_label, raw_value = match.groups()
        key = label_map.get(raw_label.lower())
        if not key:
            continue
        if raw_value.strip().lower() == "none":
            continue
        summary[key] = re.findall(r"(SPIKE-\d{3}|\d+\.\d+)", raw_value)
    return summary


def parse_dependency_ids(value: str) -> list[str]:
    if not value or value.lower() == "none":
        return []
    return re.findall(r"(SPIKE-\d{3}|\d+\.\d+)", value)


def detect_vague_requirement_words(text: str) -> list[str]:
    lowered = text.lower()
    return sorted(word for word in VAGUE_REQUIREMENT_WORDS if re.search(rf"\b{word}\b", lowered))


def ensure_terms_present(section_text: str, terms: tuple[str, ...]) -> list[str]:
    return [term for term in terms if term not in section_text]


def normalize_link_target(target: str) -> str:
    value = target.strip().strip("<>").strip()
    if re.match(r"^[a-z]+://", value):
        return ""
    if value.startswith("#"):
        return ""
    if re.match(r"^[^/]+@[^/]+$", value):
        return ""
    if ":" in value and not value.startswith("/"):
        maybe_path, maybe_line = value.rsplit(":", 1)
        if maybe_line.isdigit():
            value = maybe_path
    elif value.count(":") > 1 and value.startswith("/"):
        maybe_path, maybe_line = value.rsplit(":", 1)
        if maybe_line.isdigit():
            value = maybe_path
    return value


def looks_like_code_path(token: str) -> bool:
    token = token.strip()
    if not token:
        return False
    if token.startswith(("DES-", "REQ-", "SPIKE-")):
        return False
    if "/" in token or token.startswith(".spec/") or token.startswith("./") or token.startswith("../"):
        return True
    return token.endswith(PATHLIKE_SUFFIXES)


def looks_like_directory_reference(path: str) -> bool:
    normalized = path.rstrip("/")
    return "." not in Path(normalized).name


def split_reference_target(raw_target: str) -> LocalReference | None:
    target = normalize_link_target(raw_target)
    if not target:
        return None
    fragment_kind = ""
    fragment = ""
    path = target
    if "::" in target:
        path, fragment = target.rsplit("::", 1)
        fragment_kind = "symbol"
    elif "#" in target:
        path, fragment = target.split("#", 1)
        fragment_kind = "anchor"
    if not looks_like_code_path(path):
        return None
    return LocalReference(raw=raw_target, path=path, fragment=fragment, fragment_kind=fragment_kind)


def iter_local_references(text: str) -> list[LocalReference]:
    refs: list[LocalReference] = []
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        ref = split_reference_target(match.group(1))
        if ref:
            refs.append(ref)
    for match in re.finditer(r"`([^`]+)`", text):
        candidate = match.group(1).strip()
        ref = split_reference_target(candidate)
        if ref:
            refs.append(ref)
    unique_refs: list[LocalReference] = []
    seen: set[tuple[str, str, str]] = set()
    for ref in refs:
        key = (ref.path, ref.fragment, ref.fragment_kind)
        if key not in seen:
            seen.add(key)
            unique_refs.append(ref)
    return unique_refs


def count_concrete_repo_references(text: str) -> int:
    refs = iter_local_references(text)
    unique_paths = {
        ref.path
        for ref in refs
        if not ref.path.startswith(".spec/") and not ref.path.endswith("summary.md")
    }
    return len(unique_paths)


def resolve_reference(repo_root: Path, ref: LocalReference) -> Path:
    ref_path = Path(ref.path)
    return ref_path if ref_path.is_absolute() else repo_root / ref_path


def match_changed_path_to_reference(changed_path: str, reference_path: str) -> bool:
    changed = changed_path.strip().strip("/")
    reference = reference_path.strip().strip("/")
    if not changed or not reference:
        return False
    if changed == reference:
        return True
    if looks_like_directory_reference(reference):
        return changed.startswith(reference + "/")
    return changed.startswith(reference.rstrip("/") + "/")


def slugify_markdown_heading(heading: str) -> str:
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-")


def markdown_heading_anchors(text: str) -> set[str]:
    return {
        slugify_markdown_heading(match.group(2))
        for match in re.finditer(r"^(#{1,6})\s+(.+)$", text, re.M)
    }


def validate_frontmatter_fields(frontmatter: dict[str, str]) -> list[str]:
    return [key for key in REQUIRED_FRONTMATTER_KEYS if not frontmatter.get(key)]


def validate_frontmatter_values(frontmatter: dict[str, str]) -> list[str]:
    errors: list[str] = []
    status = frontmatter.get("status", "")
    change_class = frontmatter.get("change_class", "")
    risk_level = frontmatter.get("risk_level", "")
    if status and status not in ALLOWED_STATUS_VALUES:
        errors.append(f"invalid status: {status}")
    if change_class and change_class not in ALLOWED_CHANGE_CLASSES:
        errors.append(f"invalid change_class: {change_class}")
    if risk_level and risk_level not in ALLOWED_RISK_LEVELS:
        errors.append(f"invalid risk_level: {risk_level}")
    return errors


def has_numeric_content(text: str) -> bool:
    return bool(re.search(r"\d", text))


def symbol_exists_in_text(path: Path, text: str, symbol: str) -> bool:
    parts = [part for part in re.split(r"[.#]", symbol.strip()) if part]
    if not parts:
        return False
    suffix = path.suffix.lower()
    return all(_single_symbol_exists(suffix, text, part) for part in parts)


def _single_symbol_exists(suffix: str, text: str, symbol: str) -> bool:
    patterns = symbol_patterns_for_suffix(suffix, symbol)
    if not patterns:
        return bool(re.search(rf"\b{re.escape(symbol)}\b", text))
    return any(re.search(pattern, text, re.M | re.S | re.I) for pattern in patterns)


def symbol_patterns_for_suffix(suffix: str, symbol: str) -> list[str]:
    escaped = re.escape(symbol)
    if suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}:
        return [
            rf"\b(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s+{escaped}\b",
            rf"\b(?:export\s+)?class\s+{escaped}\b",
            rf"\b(?:export\s+)?interface\s+{escaped}\b",
            rf"\b(?:export\s+)?type\s+{escaped}\b",
            rf"\b(?:export\s+)?(?:const|let|var)\s+{escaped}\b",
            rf"\b{escaped}\s*:\s*(?:async\s*)?\(",
            rf"\b{escaped}\s*\(",
        ]
    if suffix == ".py":
        return [
            rf"^\s*(?:async\s+def|def)\s+{escaped}\b",
            rf"^\s*class\s+{escaped}\b",
            rf"^\s*{escaped}\s*=",
        ]
    if suffix == ".go":
        return [
            rf"\bfunc\s+(?:\([^)]*\)\s*)?{escaped}\b",
            rf"\btype\s+{escaped}\b",
            rf"\bvar\s+{escaped}\b",
            rf"\bconst\s+{escaped}\b",
        ]
    if suffix == ".rb":
        return [
            rf"^\s*def\s+{escaped}\b",
            rf"^\s*class\s+{escaped}\b",
            rf"^\s*module\s+{escaped}\b",
        ]
    if suffix == ".rs":
        return [
            rf"\bfn\s+{escaped}\b",
            rf"\bstruct\s+{escaped}\b",
            rf"\benum\s+{escaped}\b",
            rf"\btrait\s+{escaped}\b",
            rf"\bmod\s+{escaped}\b",
            rf"\b(?:const|static)\s+{escaped}\b",
        ]
    if suffix == ".java":
        return [
            rf"\b(?:class|interface|enum|record)\s+{escaped}\b",
            rf"(?:public|private|protected|static|final|abstract|\s)+[\w<>\[\], ?]+\s+{escaped}\s*\(",
        ]
    if suffix == ".kt":
        return [
            rf"\b(?:class|interface|object|data\s+class|enum\s+class)\s+{escaped}\b",
            rf"\bfun\s+{escaped}\b",
            rf"\b(?:val|var)\s+{escaped}\b",
        ]
    if suffix == ".sql":
        return [
            rf"\bCREATE\s+(?:OR\s+REPLACE\s+)?(?:TABLE|VIEW|FUNCTION|PROCEDURE|INDEX|TRIGGER)\s+{escaped}\b",
            rf"\bALTER\s+TABLE\s+{escaped}\b",
        ]
    if suffix in {".yaml", ".yml", ".json", ".toml"}:
        return [
            rf'["\']?{escaped}["\']?\s*:',
            rf"\b{escaped}\b",
        ]
    return []
