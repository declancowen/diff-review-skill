from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
GOLDEN = ROOT / "tests" / "golden"
REQUEST_ID = ROOT / "references" / "example-spec" / ".spec" / "request-id-propagation"
BLOCKED = ROOT / "references" / "example-spec" / ".spec" / "public-api-versioning-blocked"
EXAMPLE_ROOT = ROOT / "references" / "example-spec" / ".spec"


def run_script(script: str, *args: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stdout + result.stderr)
    return normalize(result.stdout)


def normalize(text: str) -> str:
    return text.replace(str(ROOT), "<ROOT>").rstrip() + "\n"


class GoldenOutputTests(unittest.TestCase):
    def test_exemplar_spec_hashes(self) -> None:
        golden = json.loads((GOLDEN / "example_spec_hashes.json").read_text())
        current = {
            str(path.relative_to(EXAMPLE_ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(EXAMPLE_ROOT.rglob("*.md"))
        }
        self.assertEqual(current, golden)

    def test_request_id_lint_output(self) -> None:
        output = run_script("lint_spec.py", "--spec-dir", str(REQUEST_ID))
        golden = (GOLDEN / "request_id_lint.txt").read_text()
        self.assertEqual(output, golden)

    def test_blocked_traceability_output(self) -> None:
        output = run_script("traceability_report.py", "--spec-dir", str(BLOCKED), "--strict")
        golden = (GOLDEN / "blocked_traceability.txt").read_text()
        self.assertEqual(output, golden)

    def test_request_id_summary_output(self) -> None:
        output = run_script("spec_summary.py", "--spec-dir", str(REQUEST_ID))
        golden = (GOLDEN / "request_id_summary.txt").read_text()
        self.assertEqual(output, golden)

    def test_request_id_pr_comment_output(self) -> None:
        output = run_script("spec_summary.py", "--spec-dir", str(REQUEST_ID), "--format", "pr-comment")
        golden = (GOLDEN / "request_id_pr_comment.txt").read_text()
        self.assertEqual(output, golden)


if __name__ == "__main__":
    unittest.main()
