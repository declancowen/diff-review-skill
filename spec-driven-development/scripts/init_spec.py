#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from textwrap import dedent

from owner_utils import infer_owners


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a spec package skeleton under .spec/<scope>.")
    parser.add_argument("--repo-root", required=True, help="Repository root that will own the spec package")
    parser.add_argument("--scope", required=True, help="Kebab-case spec scope name")
    parser.add_argument("--title", required=True, help="Human-readable spec title")
    parser.add_argument("--owner", default="unknown-owner", help="Owning team or person")
    parser.add_argument("--reviewers", default="unassigned", help="Comma-separated reviewers")
    parser.add_argument("--approvers", default="unassigned", help="Comma-separated approvers")
    parser.add_argument("--implementation-owner", default="unknown-owner", help="Implementation owner")
    parser.add_argument("--operations-owner", default="not-applicable", help="Operations owner or not-applicable")
    parser.add_argument("--touched-path", action="append", default=[], help="Repo-relative changed or intended paths for owner inference")
    parser.add_argument("--auto-owners", action="store_true", help="Infer reviewers and owners from CODEOWNERS using --touched-path")
    parser.add_argument(
        "--change-class",
        default="feature",
        choices=[
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
        ],
    )
    parser.add_argument(
        "--risk-level",
        default="medium",
        choices=["low", "medium", "high", "critical"],
    )
    parser.add_argument(
        "--status",
        default="draft",
        choices=[
            "draft",
            "discovery-blocked",
            "design-ready",
            "requirements-ready",
            "implementation-ready",
            "superseded",
        ],
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    spec_dir = repo_root / ".spec" / args.scope
    spec_dir.mkdir(parents=True, exist_ok=True)

    payload = {
        "title": args.title,
        "scope": args.scope,
        "status": args.status,
        "repo_root": str(repo_root),
        "change_class": args.change_class,
        "risk_level": args.risk_level,
        "owner": args.owner,
        "reviewers": args.reviewers,
        "approvers": args.approvers,
        "implementation_owner": args.implementation_owner,
        "operations_owner": args.operations_owner,
        "last_updated": date.today().isoformat(),
    }

    if args.auto_owners and args.touched_path:
        suggestions = infer_owners(repo_root, args.touched_path)
        if payload["reviewers"] == "unassigned":
            payload["reviewers"] = suggestions["reviewers"]
        if payload["approvers"] == "unassigned":
            payload["approvers"] = suggestions["approvers"]
        if payload["implementation_owner"] == "unknown-owner":
            payload["implementation_owner"] = suggestions["implementation_owner"]
        if payload["operations_owner"] == "not-applicable":
            payload["operations_owner"] = suggestions["operations_owner"]

    write_file(spec_dir / "design.md", build_design(payload), args.force)
    write_file(spec_dir / "requirements.md", build_requirements(payload), args.force)
    write_file(spec_dir / "tasks.md", build_tasks(payload), args.force)

    print(f"Initialized spec package at {spec_dir}")
    return 0


def frontmatter(payload: dict[str, str]) -> str:
    lines = ["---"]
    for key in (
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
    ):
        lines.append(f"{key}: {payload[key]}")
    lines.append("---")
    return "\n".join(lines)


def build_design(payload: dict[str, str]) -> str:
    return dedent(
        f"""{frontmatter(payload)}

        # Design Document: {payload["title"]}

        ## Summary
        - TODO

        ## Scope Statement
        - TODO

        ## Original Plan Alignment Audit
        - Original plan or prompt excerpts reviewed: TODO
        - Explicit requirements confirmed from the original plan: TODO
        - Plan items excluded or deferred, with reason: TODO
        - Gaps, contradictions, or stale assumptions found: TODO
        - Upstream artifact changes required before continuing: TODO
        - Architecture standards reviewed: TODO
        - Agent judgment or justified architecture-standard deviations: TODO
        - Post-design audit outcome: TODO

        ## Repository Discovery Summary

        ### Repo Root
        - `{payload["repo_root"]}`

        ### Repo-Specific Profile and House Patterns
        - TODO

        ### Entry Points and Execution Path
        - TODO

        ### Confirmed Code and Runtime Facts
        - TODO

        ### Related Code and Pattern Inventory
        - TODO

        ### Adjacent Pattern Comparison
        - TODO

        ### Blast Radius Review
        - TODO

        ### Recent Related Repository History
        - TODO

        ### Impacted Boundaries and Adjacent Systems
        - TODO

        ### Data, Contracts, and Config Surfaces
        - TODO

        ### Existing Tests and Operational Signals
        - TODO

        ### Static Analyzer and Audit Evidence
        - Relevant audit/review artifacts: TODO
        - Analyzer commands, HEAD, date, mode, scope, baseline/gate, and result: TODO
        - Gate versus advisory inventory distinction: TODO
        - CI parity and accepted-debt status: TODO

        ## Problem Statement and Context
        - TODO

        ## Current-State Analysis
        - TODO

        ## Target-State Architecture
        - Intended owner for each durable invariant: TODO
        - Dependency direction and public surfaces: TODO
        - Contracts, data ownership, async/reliability, and operational ownership: TODO
        - What must stop happening after the transition: TODO
        - Fitness functions that prove the target state is holding: TODO

        ## Goals
        - TODO

        ## Non-Goals
        - TODO

        ## Confirmed Facts
        - TODO

        ## Assumptions
        - TODO

        ## Open Questions
        - None.

        ## Decision Needed
        - None.

        ## Proposed Design

        ### Solution Overview
        - TODO

        ### Transition Plan From Current State
        - Containment gate: TODO
        - Safe implementation slices: TODO
        - Old bypasses or compatibility paths to remove: TODO
        - Baselines, suppressions, allowlists, or module-budget caps that remain temporarily: TODO
        - Revisit trigger for each accepted exception: TODO

        ### End-to-End Flow
        - TODO

        ### Component and Module Changes

        #### UI or Client
        - TODO

        #### API or Application Layer
        - TODO

        #### Domain or Business Logic
        - TODO

        #### Data Model and Persistence
        - TODO

        #### Integrations, Events, or Background Jobs
        - TODO

        #### Security and Permissions
        - TODO

        #### Performance and Scalability
        - TODO

        #### Observability and Operations
        - TODO

        ## Impacted Surfaces Matrix
        - UI: TODO
        - API: TODO
        - Domain logic: TODO
        - Persistence: TODO
        - Integrations: TODO
        - Auth: TODO
        - Infra: TODO
        - Telemetry: TODO
        - Tests: TODO
        - Docs: TODO

        ## Change Impact Map
        - Direct impact: TODO
        - Indirect impact: TODO
        - Unchanged but risk-adjacent areas: TODO

        ## Invariants and Forbidden Outcomes
        - TODO

        ## Compatibility Matrix
        - Public API: TODO
        - Internal API: TODO
        - Data schema: TODO
        - Events: TODO
        - Cache keys: TODO
        - Config: TODO
        - External consumers: TODO
        - Rollback compatibility: TODO

        ## Contract Examples and Before/After Payloads
        - Request examples: TODO
        - Response examples: TODO
        - Event or message examples: TODO
        - Before/after comparisons: TODO

        ## Cross-Cutting Applicability Matrix
        - Security: TODO
        - Privacy: TODO
        - Performance: TODO
        - Resilience: TODO
        - Migration: TODO
        - Observability: TODO
        - Supportability: TODO
        - Backward compatibility: TODO

        ## Success Metrics and Numeric NFR Targets
        - Latency targets: TODO
        - Throughput or concurrency targets: TODO
        - Error-rate or availability targets: TODO
        - Timeout, retry, or queue-depth limits: TODO

        ## Decision Register

        ### DES-001: TODO
        - Context: TODO
        - Current-state gap: TODO
        - Decision: TODO
        - Rationale: TODO
        - Tradeoffs: TODO
        - Affected surfaces: TODO
        - Fitness signal: TODO

        ## Risk Register
        - Risk:
          - Impact: TODO
          - Mitigation: TODO
          - Residual risk: TODO

        ## Test Impact Matrix
        - Existing tests to update: TODO
        - New tests required: TODO
        - Compatibility tests: TODO
        - Rollback-safety tests: TODO

        ## Validation Strategy
        - TODO

        ## Post-Design Review
        - Original plan coverage review: TODO
        - Repository evidence review: TODO
        - Architecture standards review: TODO
        - Requirements readiness: TODO
        - Required upstream changes before requirements authoring: TODO

        ## Rollout, Abort, and Reversal
        - TODO

        ## Forbidden Shortcuts and Guardrails
        - TODO

        ## Alternatives Considered
        - Alternative:
          - Why rejected: TODO

        ## Residual Risks
        - TODO
        """
    ).strip().replace("\n        ", "\n") + "\n"


def build_requirements(payload: dict[str, str]) -> str:
    return dedent(
        f"""{frontmatter(payload)}

        # Requirements Document: {payload["title"]}

        ## Source Artifacts
        - `.spec/{payload["scope"]}/design.md`

        ## Scope Statement
        - TODO

        ## Upstream Alignment Audit
        - Original plan requirements reviewed: TODO
        - Design decisions reviewed: TODO
        - Repository evidence and current tests reviewed: TODO
        - Architecture standards implications reviewed: TODO
        - Requirements added, changed, or rejected during audit: TODO
        - Design updates required before continuing: TODO
        - Agent judgment or justified architecture-standard deviations: TODO
        - Post-requirements audit outcome: TODO

        ## Cross-Cutting Coverage
        - Security: TODO
        - Privacy: TODO
        - Performance: TODO
        - Resilience: TODO
        - Migration: TODO
        - Architecture transition: TODO
        - Observability: TODO
        - Supportability: TODO
        - Backward compatibility: TODO

        ## Requirements

        ### REQ-FUNC-001: TODO
        Source Design Decisions:
        - DES-001

        Priority: High

        Rationale:
        - TODO

        Requirement:
        - THE system SHALL ...

        Verification Method:
        - TODO

        Risk if Unmet:
        - TODO

        Acceptance Criteria
        1. TODO

        Negative Cases
        1. TODO

        ### REQ-NFR-001: TODO
        Source Design Decisions:
        - DES-001

        Priority: Medium

        Rationale:
        - TODO

        Requirement:
        - THE system SHALL ...

        Target Metrics:
        - Not applicable with reason, or numeric target

        Verification Method:
        - TODO

        Risk if Unmet:
        - TODO

        Acceptance Criteria
        1. TODO

        Negative Cases
        1. TODO

        ## Traceability Matrix
        - DES-001 -> REQ-FUNC-001, REQ-NFR-001
        """
    ).strip().replace("\n        ", "\n") + "\n"


def build_tasks(payload: dict[str, str]) -> str:
    return dedent(
        f"""{frontmatter(payload)}

        # Task Plan: {payload["title"]}

        ## Source Artifacts
        - `.spec/{payload["scope"]}/design.md`
        - `.spec/{payload["scope"]}/requirements.md`

        ## Gating Status
        - Blocked
        - Blocking design decisions:
          - DES-001

        ## Execution Status Summary
        - To do: SPIKE-001
        - In progress: none
        - Completed: none
        - Deferred: none
        - Blocked: none

        ## Sequencing Notes
        - TODO

        ## Implementation Authority And Review Loop
        - The spec is guidance; the original user request is authoritative for the target outcome, architecture standards are the review lens for solution shape, and live code/current tests are authoritative for current reality.
        - Before each leaf task, read linked `DES-*` entries, linked `REQ-*` entries, the task entry, relevant code, and current tests.
        - During each leaf task, use architecture standards to shape every material design/code/test decision, not only the final review.
        - Treat a requirement slice as one leaf task or a small group of tightly coupled leaf tasks that completes one requirement or requirement cluster.
        - After each implementation slice, run focused validation, then run a deep diff-review scoped to that slice with architecture standards as the architecture lens.
        - If diff-review is unavailable, run an equivalent manual deep diff review and record the fallback.
        - Fix slice review findings, then run normal diff-review passes with architecture standards until the slice is clean before moving on.
        - Record every slice review and the final total-diff review in `.spec/{payload["scope"]}/reviews.md`.
        - After test creation, verify tests prove requirement behavior and relevant negative cases rather than implementation details.
        - If code reality and spec intent diverge, update `design.md`, then `requirements.md`, then `tasks.md` before continuing.
        - If the user corrects a generated artifact or says an item drifted, treat that correction as authoritative and refresh upstream spec artifacts before continuing.
        - The implementing agent may challenge a stale task or skill interpretation, but must document the rationale and update upstream artifacts before continuing.

        ## Blocking Work
        - [ ] SPIKE-001 Resolve the first blocking design decision
          - Status: todo
          - Blocks: DES-001
          - Likely areas: `path/to/code`, `path/to/test`
          - Validation: TODO
          - Exit criteria: decision recorded in `design.md`

        ## Tasks
        - No implementation tasks until the design is unblocked.

        ## Post-Deploy Verification
        - TODO

        ## Traceability Matrix
        - Add once implementation tasks exist.

        ## Coverage Checklist
        - Every `REQ-*` appears in at least one leaf task
        - No leaf task introduces scope absent from the requirements
        - Validation is included near risky changes
        - Rollout and rollback work is present when needed
        - Every leaf task includes pre-implementation context review, test creation review, slice review loop, post-implementation review, and spec drift check fields
        - `Depends on` references form a valid acyclic graph
        - Every leaf task and blocking spike appears exactly once in `Execution Status Summary`
        """
    ).strip().replace("\n        ", "\n") + "\n"


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
