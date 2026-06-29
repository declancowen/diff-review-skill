# CI Enforcement

Spec validation should not rely on author discipline alone.

## Recommended CI checks

Run these for any changed `.spec/**` directory:

```bash
python3 .spec/_shared/spec-tools/scripts/lint_spec.py --spec-dir <spec-dir>
python3 .spec/_shared/spec-tools/scripts/check_code_refs.py --spec-dir <spec-dir> --min-path-refs 8
python3 .spec/_shared/spec-tools/scripts/traceability_report.py --spec-dir <spec-dir> --strict
python3 .spec/_shared/spec-tools/scripts/spec_summary.py --spec-dir <spec-dir>
python3 .spec/_shared/spec-tools/scripts/spec_summary.py --spec-dir <spec-dir> --format pr-comment
```

Use [assets/github-actions-spec-lint.yml](../assets/github-actions-spec-lint.yml) as a starting point for GitHub Actions.

Install the repo-local validation runtime first:

```bash
python3 scripts/bootstrap_spec_repo.py --repo-root <repo-root> --seed-house-patterns
```

## Policy guidance

- Block merges when lint or traceability fails.
- Prefer summary output as an artifact or PR comment for reviewers.
- Prefer surfacing `pr-comment.md` in CI job summaries so reviewers see the spec snapshot without opening files manually.
- For code-bearing PRs, run `.spec/_shared/spec-tools/scripts/spec_drift_check.py` against the changed files to catch code that lands outside the declared spec surface.
- Re-run checks when any of `design.md`, `requirements.md`, or `tasks.md` changes.
