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


def run_script(script: str, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
        cwd=str(cwd or ROOT),
        text=True,
        capture_output=True,
        check=False,
    )


class InitAndLintTests(unittest.TestCase):
    def test_init_spec_creates_extended_frontmatter_and_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            repo_root.mkdir()
            result = run_script(
                "init_spec.py",
                "--repo-root",
                str(repo_root),
                "--scope",
                "demo-change",
                "--title",
                "Demo Change",
                "--reviewers",
                "alice,bob",
                "--approvers",
                "carol",
                "--implementation-owner",
                "platform-team",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            design_text = (repo_root / ".spec" / "demo-change" / "design.md").read_text()
            tasks_text = (repo_root / ".spec" / "demo-change" / "tasks.md").read_text()
            self.assertIn("reviewers: alice,bob", design_text)
            self.assertIn("### Adjacent Pattern Comparison", design_text)
            self.assertIn("## Change Impact Map", design_text)
            self.assertIn("## Test Impact Matrix", design_text)
            self.assertIn("## Execution Status Summary", tasks_text)
            self.assertIn("- Status: todo", tasks_text)

    def test_lint_spec_passes_request_id_example(self) -> None:
        result = run_script("lint_spec.py", "--spec-dir", str(EXAMPLE))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_lint_spec_rejects_dependency_cycle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            spec_dir = Path(tmp) / "request-id-propagation"
            shutil.copytree(EXAMPLE, spec_dir)
            tasks_path = spec_dir / "tasks.md"
            tasks_text = tasks_path.read_text()
            tasks_text = tasks_text.replace("Depends on: none", "Depends on: 3.1", 1)
            tasks_path.write_text(tasks_text)
            result = run_script("lint_spec.py", "--spec-dir", str(spec_dir))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("contains a cycle", result.stdout)

    def test_lint_spec_rejects_status_summary_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            spec_dir = Path(tmp) / "request-id-propagation"
            shutil.copytree(EXAMPLE, spec_dir)
            tasks_path = spec_dir / "tasks.md"
            tasks_text = tasks_path.read_text()
            tasks_text = tasks_text.replace("- To do: 1.1, 2.1, 2.2, 3.1", "- To do: 2.1, 2.2, 3.1", 1)
            tasks_path.write_text(tasks_text)
            result = run_script("lint_spec.py", "--spec-dir", str(spec_dir))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Execution Status Summary does not track", result.stdout)


if __name__ == "__main__":
    unittest.main()
