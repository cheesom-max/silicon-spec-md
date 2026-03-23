#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_MIGRATION_SECTIONS = [
    "## Purpose",
    "## Usage Order",
    "## Intended Audience",
    "## Out of Scope",
    "## Canonical Scope",
    "## Canonical Links",
    "## Migration Snapshot",
    "## Category A: Created Paths",
    "## Category B: Moved Paths",
    "## Category C: Renamed Paths",
    "## Category D: Deleted Paths",
    "## In-Place Updates (No Path Change)",
    "## Verification Notes",
    "## Last Updated When",
]

EXPECTED_CREATED_PATHS = [
    "docs/08-document-operations.md",
    "docs/09-glossary.md",
    "docs/06-adrs/06-ADR-INDEX.md",
    "docs/07-runbooks/07-INDEX.md",
    "docs/04-features/04-_template/concept.md",
    "docs/04-features/04-_template/how-to.md",
    "docs/04-features/04-_template/reference.md",
    "docs/04-features/04-_template/examples.md",
    "docs/04-features/04-_template/changes.md",
    "docs/04-features/04-_template/known-issues.md",
    "scripts/docs/test_required_sections.py",
    "scripts/docs/test_canonical_ownership.py",
    "scripts/docs/test_taxonomy_coverage.py",
    "scripts/docs/test_metadata_freshness.py",
    "scripts/docs/test_migration_map.py",
    "scripts/docs/test_links.py",
    "scripts/docs/test_orphans.py",
]

REQUIRED_MAP_REFERENCES = [
    "docs/08-document-operations.md",
    "docs/09-glossary.md",
    "docs/migration-map.md",
]


def main() -> int:
    failures: list[str] = []

    migration_path = ROOT / "docs/migration-map.md"
    migration_text = migration_path.read_text(encoding="utf-8")
    map_text = (ROOT / "docs/00-README.md").read_text(encoding="utf-8")

    for section in REQUIRED_MIGRATION_SECTIONS:
        if section not in migration_text:
            failures.append(f"docs/migration-map.md: missing section '{section}'")

    if "| Category | Source Path | Created Path | Replacement Path | Rationale | Status | Rollback Notes |" not in migration_text:
        failures.append("docs/migration-map.md: missing Category A created-paths table header")

    created_path_rows = migration_text.count("| `none` | `docs/")
    if created_path_rows < 10:
        failures.append("docs/migration-map.md: expected at least 10 created-path rows with source `none`")

    for created_path in EXPECTED_CREATED_PATHS:
        if f"`{created_path}`" not in migration_text:
            failures.append(f"docs/migration-map.md: missing created-path entry '{created_path}'")

    for required_phrase in (
        "No path moves were introduced in T1-T6.",
        "No file renames were introduced in T1-T6.",
        "No path deletions were introduced in T1-T6.",
    ):
        if required_phrase not in migration_text:
            failures.append(f"docs/migration-map.md: missing invariant phrase '{required_phrase}'")

    for reference in REQUIRED_MAP_REFERENCES:
        if reference not in map_text:
            failures.append(f"docs/00-README.md: missing migration reference '{reference}'")

    if failures:
        print(f"FAIL: {len(failures)} failures")
        for item in failures:
            print(f"- {item}")
        return 1

    print("PASS: 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
