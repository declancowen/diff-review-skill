from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_script(script: str, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
        cwd=str(cwd or ROOT),
        text=True,
        capture_output=True,
        check=False,
    )


class OwnersBootstrapAndDriftTests(unittest.TestCase):
    def test_suggest_owners_from_codeowners(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            (repo_root / ".github").mkdir(parents=True)
            (repo_root / ".github" / "CODEOWNERS").write_text(
                "/src/api/ @api-team @platform-team\n"
                "/infra/ @sre-team\n"
            )
            result = run_script(
                "suggest_owners.py",
                "--repo-root",
                str(repo_root),
                "--path",
                "src/api/user.ts",
                "--path",
                "infra/deploy.yml",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual(data["implementation_owner"], "@api-team")
            self.assertEqual(data["operations_owner"], "@sre-team")
            self.assertIn("@platform-team", data["reviewers"])

    def test_bootstrap_repo_spec_installs_shared_assets(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            repo_root.mkdir()
            result = run_script(
                "bootstrap_spec_repo.py",
                "--repo-root",
                str(repo_root),
                "--seed-house-patterns",
                "--policy-pack",
                "nextjs-patterns",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue((repo_root / ".spec" / "_shared" / "repo-profile.md").exists())
            self.assertTrue((repo_root / ".github" / "workflows" / "spec-validation.yml").exists())
            self.assertTrue((repo_root / ".spec" / "_shared" / "spec-tools" / "scripts" / "lint_spec.py").exists())
            self.assertTrue((repo_root / ".spec" / "_shared" / "policy-packs" / "nextjs-patterns.md").exists())
            house_patterns = (repo_root / ".spec" / "_shared" / "house-patterns.md").read_text()
            workflow = (repo_root / ".github" / "workflows" / "spec-validation.yml").read_text()
            self.assertIn(".spec/_shared/policy-packs/nextjs-patterns.md", house_patterns)
            self.assertIn(".spec/_shared/spec-tools/scripts/lint_spec.py", workflow)

    def test_bootstrap_repo_rejects_unknown_policy_pack(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            repo_root.mkdir()
            result = run_script(
                "bootstrap_spec_repo.py",
                "--repo-root",
                str(repo_root),
                "--policy-pack",
                "unknown-pack",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unknown policy pack", result.stderr + result.stdout)

    def test_spec_drift_check_passes_when_changed_file_matches_task_area(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            spec_dir = repo_root / ".spec" / "demo"
            (repo_root / "src" / "api").mkdir(parents=True)
            spec_dir.mkdir(parents=True)
            (repo_root / "src" / "api" / "user.ts").write_text("export function loadUser() {}\n")

            frontmatter = """---
title: Demo
scope: demo
status: implementation-ready
repo_root: REPO_ROOT
change_class: feature
risk_level: medium
owner: platform
reviewers: alice
approvers: bob
implementation_owner: platform
operations_owner: not-applicable
last_updated: 2026-04-22
---
""".replace("REPO_ROOT", str(repo_root))

            design = frontmatter + """
# Design Document: Demo

## Repository Discovery Summary
### Repo Root
- `REPO_ROOT`
### Repo-Specific Profile and House Patterns
- Not applicable.
### Entry Points and Execution Path
- `src/api/user.ts`
### Confirmed Code and Runtime Facts
- `src/api/user.ts::loadUser`
### Related Code and Pattern Inventory
- `src/api/user.ts`
### Adjacent Pattern Comparison
- Existing pattern reused.
### Blast Radius Review
- `src/api`
### Recent Related Repository History
- None.
### Impacted Boundaries and Adjacent Systems
- `src/api/user.ts`
### Data, Contracts, and Config Surfaces
- Not applicable.
### Existing Tests and Operational Signals
- `src/api/user.ts`

## Problem Statement and Context
- Demo
## Current-State Analysis
- Demo
## Goals
- Demo
## Non-Goals
- Demo
## Confirmed Facts
- Demo
## Assumptions
- Demo
## Open Questions
- None.
## Decision Needed
- None.
## Proposed Design
### Solution Overview
- Demo
### End-to-End Flow
- Demo
### Component and Module Changes
#### UI or Client
- Not applicable.
#### API or Application Layer
- Demo
#### Domain or Business Logic
- Not applicable.
#### Data Model and Persistence
- Not applicable.
#### Integrations, Events, or Background Jobs
- Not applicable.
#### Security and Permissions
- Not applicable.
#### Performance and Scalability
- Not applicable.
#### Observability and Operations
- Not applicable.
## Impacted Surfaces Matrix
- UI: Not applicable.
- API: `src/api/user.ts`
- Domain logic: Not applicable.
- Persistence: Not applicable.
- Integrations: Not applicable.
- Auth: Not applicable.
- Infra: Not applicable.
- Telemetry: Not applicable.
- Tests: Not applicable.
- Docs: Not applicable.
## Change Impact Map
- Direct impact: `src/api/user.ts`
- Indirect impact: Not applicable.
- Unchanged but risk-adjacent areas: Not applicable.
## Invariants and Forbidden Outcomes
- Demo
## Compatibility Matrix
- Public API: Not applicable.
- Internal API: Not applicable.
- Data schema: Not applicable.
- Events: Not applicable.
- Cache keys: Not applicable.
- Config: Not applicable.
- External consumers: Not applicable.
- Rollback compatibility: Not applicable.
## Contract Examples and Before/After Payloads
- Request examples: Not applicable.
- Response examples: Not applicable.
- Event or message examples: Not applicable.
- Before/after comparisons: Not applicable.
## Cross-Cutting Applicability Matrix
- Security: Not applicable. Demo.
- Privacy: Not applicable. Demo.
- Performance: Not applicable. Demo.
- Resilience: Not applicable. Demo.
- Migration: Not applicable. Demo.
- Observability: Not applicable. Demo.
- Supportability: Not applicable. Demo.
- Backward compatibility: Not applicable. Demo.
## Success Metrics and Numeric NFR Targets
- Latency targets: Not applicable.
- Throughput or concurrency targets: Not applicable.
- Error-rate or availability targets: Not applicable.
- Timeout, retry, or queue-depth limits: Not applicable.
## Decision Register
### DES-001: Demo decision
- Context: Demo
- Decision: Demo
- Rationale: Demo
- Tradeoffs: Demo
- Affected surfaces: `src/api/user.ts`
## Risk Register
- Risk:
  - Impact: Demo
  - Mitigation: Demo
  - Residual risk: Demo
## Test Impact Matrix
- Existing tests to update: Not applicable.
- New tests required: Not applicable.
- Compatibility tests: Not applicable.
- Rollback-safety tests: Not applicable.
## Validation Strategy
- Demo
## Rollout, Abort, and Reversal
- Demo
## Forbidden Shortcuts and Guardrails
- Demo
## Alternatives Considered
- Alternative:
  - Why rejected: Demo
## Residual Risks
- Demo
""".replace("REPO_ROOT", str(repo_root))
            requirements = frontmatter + """
# Requirements Document: Demo
## Source Artifacts
- `.spec/demo/design.md`
## Scope Statement
- Demo
## Cross-Cutting Coverage
- Security: Not applicable. Demo.
- Privacy: Not applicable. Demo.
- Performance: Not applicable. Demo.
- Resilience: Not applicable. Demo.
- Migration: Not applicable. Demo.
- Observability: Not applicable. Demo.
- Supportability: Not applicable. Demo.
- Backward compatibility: Covered by `REQ-FUNC-001`
## Requirements
### REQ-FUNC-001: Demo requirement
Source Design Decisions:
- DES-001
Priority: High
Rationale:
- Demo
Requirement:
- THE system SHALL update the user API logic.
Verification Method:
- Demo
Risk if Unmet:
- Demo
Acceptance Criteria
1. Demo
Negative Cases
1. Demo
## Traceability Matrix
- DES-001 -> REQ-FUNC-001
"""
            tasks = frontmatter + """
# Task Plan: Demo
## Source Artifacts
- `.spec/demo/design.md`
- `.spec/demo/requirements.md`
## Gating Status
- Ready for implementation
- Blocking design decisions:
  - None
## Sequencing Notes
- Demo
## Blocking Work
- None.
## Tasks
- [ ] 1. API work
  - [ ] 1.1 Update user loader
    - Status: todo
    - Depends on: none
    - Likely areas: `src/api/user.ts`
    - Validation: Demo
    - Exit criteria: Demo
    - Rollback impact: Demo
    - Blocking unknowns: none
    - Pre-implementation context check: Demo
    - Test creation review: Demo
    - Slice review loop: Demo
    - Post-implementation review: Demo
    - Spec drift check: Demo
    - _Requirements: REQ-FUNC-001_
## Post-Deploy Verification
- Demo
## Traceability Matrix
- REQ-FUNC-001 -> 1.1
## Coverage Checklist
- Demo
"""
            (spec_dir / "design.md").write_text(design)
            (spec_dir / "requirements.md").write_text(requirements)
            (spec_dir / "tasks.md").write_text(tasks)

            result = run_script(
                "spec_drift_check.py",
                "--spec-dir",
                str(spec_dir),
                "--changed-file",
                "src/api/user.ts",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Touched requirements: REQ-FUNC-001", result.stdout)


if __name__ == "__main__":
    unittest.main()
