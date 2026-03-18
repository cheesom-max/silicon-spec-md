#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Usage Order",
    "## Intended Audience",
    "## Out of Scope",
    "## Canonical Scope",
    "## Last Updated When",
    "## Canonical Links",
]

REQUIRED_METADATA_KEYS = (
    "doc_type",
    "status",
    "owner",
    "audience",
    "last_reviewed",
    "canonical",
    "supersedes",
)

TEMPLATE_DOCS = {
    "docs/06-adrs/06-ADR-0000-template.md",
    "docs/07-runbooks/07-template.md",
}


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}, text

    metadata: dict[str, str] = {}
    end_index = -1
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    if end_index == -1:
        return {}, text

    body = "\n".join(lines[end_index + 1 :])
    return metadata, body


def is_substantive_doc(rel_path: str) -> bool:
    if rel_path in TEMPLATE_DOCS:
        return False
    if rel_path.startswith("docs/04-features/04-_template/"):
        return False
    return True


def main() -> int:
    failures: list[str] = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel_path = path.relative_to(ROOT).as_posix()
        if not is_substantive_doc(rel_path):
            continue

        text = path.read_text(encoding="utf-8")
        metadata, body = parse_front_matter(text)
        if not metadata:
            failures.append(f"{rel_path}: missing YAML front matter")
            continue

        missing_metadata = [key for key in REQUIRED_METADATA_KEYS if key not in metadata]
        if missing_metadata:
            failures.append(f"{rel_path}: missing metadata keys {', '.join(missing_metadata)}")

        body_lines = [line.strip() for line in body.splitlines()]
        for section in REQUIRED_SECTIONS:
            occurrences = sum(1 for line in body_lines if line == section)
            if occurrences == 0:
                failures.append(f"{rel_path}: missing required section '{section}'")
            elif occurrences > 1:
                failures.append(f"{rel_path}: duplicated required section '{section}'")

    if failures:
        print(f"FAIL: {len(failures)} failures")
        for item in failures:
            print(f"- {item}")
        return 1

    print("PASS: 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
