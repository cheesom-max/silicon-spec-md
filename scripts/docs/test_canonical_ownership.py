#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

CANONICAL_MAP = {
    "Product intent": "docs/01-product.md",
    "System shape": "docs/02-system-architecture.md",
    "Repository-wide engineering rules": "docs/03-engineering-rules.md",
    "Feature behavior and acceptance criteria": "docs/04-features/<feature>/04-spec.md",
    "Documentation operations model": "docs/08-document-operations.md",
    "Architectural decisions": "docs/06-adrs/06-ADR-xxxx-title.md",
    "Operational response": "docs/07-runbooks/07-<name>.md",
    "Test expectations": "docs/05-test-strategy.md",
}

OWNER_DOCS = [
    "docs/01-product.md",
    "docs/02-system-architecture.md",
    "docs/03-engineering-rules.md",
    "docs/05-test-strategy.md",
    "docs/08-document-operations.md",
]


def main() -> int:
    failures: list[str] = []

    map_path = ROOT / "docs/00-README.md"
    map_text = map_path.read_text(encoding="utf-8")
    for concern, canonical_path in CANONICAL_MAP.items():
        if concern not in map_text:
            failures.append(f"docs/00-README.md: missing concern row '{concern}'")
        if canonical_path not in map_text:
            failures.append(f"docs/00-README.md: missing canonical path '{canonical_path}'")

    for rel_path in OWNER_DOCS:
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        if "## Canonical Scope" not in text:
            failures.append(f"{rel_path}: missing '## Canonical Scope'")
        if "## Canonical Links" not in text:
            failures.append(f"{rel_path}: missing '## Canonical Links'")

    if failures:
        print(f"FAIL: {len(failures)} failures")
        for item in failures:
            print(f"- {item}")
        return 1

    print("PASS: 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
