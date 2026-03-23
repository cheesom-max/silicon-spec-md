#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_TAXONOMY_TERMS = [
    "Layer 1",
    "Layer 2",
    "04-spec.md",
    "concept.md",
    "how-to.md",
    "reference.md",
    "examples.md",
    "changes.md",
    "known-issues.md",
]


def main() -> int:
    failures: list[str] = []

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    map_doc = (ROOT / "docs/00-README.md").read_text(encoding="utf-8")

    for term in REQUIRED_TAXONOMY_TERMS:
        if term not in readme:
            failures.append(f"README.md: missing taxonomy term '{term}'")

    if "## Layered Taxonomy Model" not in map_doc:
        failures.append("docs/00-README.md: missing '## Layered Taxonomy Model'")

    if "docs/04-features/<feature>/" not in map_doc:
        failures.append("docs/00-README.md: missing feature package taxonomy path")

    if failures:
        print(f"FAIL: {len(failures)} failures")
        for item in failures:
            print(f"- {item}")
        return 1

    print("PASS: 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
