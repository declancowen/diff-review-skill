from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import spec_utils  # noqa: E402


class SpecUtilsTests(unittest.TestCase):
    def test_iter_local_references_parses_anchor_and_symbol(self) -> None:
        text = """
See [guide](docs/guide.md#usage-notes), `src/service.ts::buildThing`, and `src/worker.ts`.
"""
        refs = {(ref.path, ref.fragment, ref.fragment_kind) for ref in spec_utils.iter_local_references(text)}
        self.assertIn(("docs/guide.md", "usage-notes", "anchor"), refs)
        self.assertIn(("src/service.ts", "buildThing", "symbol"), refs)
        self.assertIn(("src/worker.ts", "", ""), refs)

    def test_slugify_markdown_heading_matches_anchor_style(self) -> None:
        self.assertEqual(spec_utils.slugify_markdown_heading("Usage Notes (v2)!"), "usage-notes-v2")


if __name__ == "__main__":
    unittest.main()
