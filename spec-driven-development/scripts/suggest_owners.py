#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from owner_utils import infer_owners


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest spec owners from CODEOWNERS and touched paths.")
    parser.add_argument("--repo-root", required=True, help="Repository root")
    parser.add_argument("--path", action="append", dest="paths", default=[], help="Touched repo-relative path")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    suggestions = infer_owners(repo_root, args.paths)
    print(json.dumps(suggestions, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
