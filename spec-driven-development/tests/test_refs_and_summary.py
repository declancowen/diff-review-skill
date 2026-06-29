from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
EXAMPLE = ROOT / "references" / "example-spec" / ".spec" / "request-id-propagation"
BLOCKED_EXAMPLE = ROOT / "references" / "example-spec" / ".spec" / "public-api-versioning-blocked"


def run_script(script: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
        text=True,
        capture_output=True,
        check=False,
    )


class ReferenceAndSummaryTests(unittest.TestCase):
    def test_check_code_refs_validates_anchor_symbol_and_minimum_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            spec_dir = repo_root / ".spec" / "ref-check"
            (repo_root / "docs").mkdir(parents=True)
            (repo_root / "src").mkdir(parents=True)
            spec_dir.mkdir(parents=True)

            (repo_root / "docs" / "guide.md").write_text("# Guide\n\n## Usage Notes\n")
            (repo_root / "src" / "service.ts").write_text("export function buildThing() {}\n")

            frontmatter = """---
title: Ref Check
scope: ref-check
status: draft
repo_root: REPO_ROOT
change_class: feature
risk_level: low
owner: platform
reviewers: alice
approvers: bob
implementation_owner: platform
operations_owner: not-applicable
last_updated: 2026-04-22
---
""".replace("REPO_ROOT", str(repo_root))

            design = frontmatter + """
# Design Document: Ref Check

See [guide](docs/guide.md#usage-notes), `src/service.ts::buildThing`, and `src/service.ts`.
"""
            requirements = frontmatter + """
# Requirements Document: Ref Check

`src/service.ts`
"""
            tasks = frontmatter + """
# Task Plan: Ref Check

`docs/guide.md`
"""
            (spec_dir / "design.md").write_text(design)
            (spec_dir / "requirements.md").write_text(requirements)
            (spec_dir / "tasks.md").write_text(tasks)

            result = run_script(
                "check_code_refs.py",
                "--spec-dir",
                str(spec_dir),
                "--min-path-refs",
                "2",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Concrete repo path references: 2", result.stdout)

    def test_check_code_refs_rejects_non_symbol_substring_reference(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            spec_dir = repo_root / ".spec" / "bad-ref"
            (repo_root / "src").mkdir(parents=True)
            spec_dir.mkdir(parents=True)

            (repo_root / "src" / "service.ts").write_text(
                'export function buildThing() { const note = "thing"; return note; }\n'
            )

            frontmatter = """---
title: Bad Ref
scope: bad-ref
status: draft
repo_root: REPO_ROOT
change_class: feature
risk_level: low
owner: platform
reviewers: alice
approvers: bob
implementation_owner: platform
operations_owner: not-applicable
last_updated: 2026-04-22
---
""".replace("REPO_ROOT", str(repo_root))

            for name in ("design.md", "requirements.md", "tasks.md"):
                (spec_dir / name).write_text(frontmatter + "\n`src/service.ts::thing`\n")

            result = run_script("check_code_refs.py", "--spec-dir", str(spec_dir))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("references missing symbol", result.stdout)

    def test_spec_summary_writes_summary_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            spec_dir = Path(tmp) / "request-id-propagation"
            shutil.copytree(EXAMPLE, spec_dir)
            result = run_script("spec_summary.py", "--spec-dir", str(spec_dir), "--write")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            summary = (spec_dir / "summary.md").read_text()
            self.assertIn("# Spec Summary: Request ID Propagation Across API and Worker Flows", summary)
            self.assertIn("Blocking decisions", summary)

    def test_spec_summary_can_emit_pr_comment(self) -> None:
        result = run_script("spec_summary.py", "--spec-dir", str(EXAMPLE), "--format", "pr-comment")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("## Spec Review Snapshot: Request ID Propagation Across API and Worker Flows", result.stdout)
        self.assertIn("Traceability:", result.stdout)

    def test_traceability_strict_allows_blocked_spec_without_tasks(self) -> None:
        result = run_script("traceability_report.py", "--spec-dir", str(BLOCKED_EXAMPLE), "--strict")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Blocking decisions: 1", result.stdout)


if __name__ == "__main__":
    unittest.main()
