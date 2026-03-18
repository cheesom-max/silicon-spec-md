#!/usr/bin/env python3
from __future__ import annotations

from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"

REQUIRED_SCHEMA_TOKENS = [
    "YAML front matter",
    "doc_type",
    "status",
    "owner",
    "audience",
    "last_reviewed",
    "canonical",
    "supersedes",
    "substantive",
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


def parse_front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}
    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def is_substantive_doc(rel_path: str) -> bool:
    if rel_path in TEMPLATE_DOCS:
        return False
    if rel_path.startswith("docs/04-features/04-_template/"):
        return False
    return True


def allowed_age_days(doc_type: str, status: str) -> int | None:
    if status == "archived":
        return None
    if status == "deprecated":
        return 30
    if doc_type == "governance" and status == "active":
        return 30
    if doc_type == "governance" and status == "draft":
        return 14
    if doc_type == "feature-spec" and status == "active":
        return 30
    if doc_type == "feature-spec" and status == "draft":
        return 14
    if doc_type == "adr" and status == "active":
        return 60
    if doc_type == "adr" and status == "draft":
        return 30
    if doc_type == "runbook" and status == "active":
        return 30
    if doc_type == "runbook" and status == "draft":
        return 14
    if doc_type == "reference" and status == "active":
        return 60
    if doc_type == "reference" and status == "draft":
        return 30
    return None


def main() -> int:
    failures: list[str] = []

    rules_text = (ROOT / "docs/03-engineering-rules.md").read_text(encoding="utf-8")
    for token in REQUIRED_SCHEMA_TOKENS:
        if token not in rules_text:
            failures.append(f"docs/03-engineering-rules.md: missing metadata rule token '{token}'")

    today = date.today()
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if not is_substantive_doc(rel):
            continue

        metadata = parse_front_matter(path.read_text(encoding="utf-8"))
        if not metadata:
            failures.append(f"{rel}: missing YAML front matter")
            continue

        missing = [k for k in REQUIRED_METADATA_KEYS if k not in metadata]
        if missing:
            failures.append(f"{rel}: missing metadata keys {', '.join(missing)}")
            continue

        if metadata["canonical"] not in {"true", "false"}:
            failures.append(f"{rel}: invalid canonical value '{metadata['canonical']}' (expected true or false)")

        if not metadata["supersedes"]:
            failures.append(f"{rel}: supersedes must not be empty")

        try:
            reviewed = datetime.strptime(metadata["last_reviewed"], "%Y-%m-%d").date()
        except ValueError:
            failures.append(f"{rel}: invalid last_reviewed date '{metadata['last_reviewed']}' (expected YYYY-MM-DD)")
            continue

        limit = allowed_age_days(metadata["doc_type"], metadata["status"])
        if limit is None:
            continue

        age = (today - reviewed).days
        if age > limit:
            failures.append(
                f"{rel}: last_reviewed is stale ({age} days old, limit {limit} days for {metadata['doc_type']}/{metadata['status']})"
            )

    if failures:
        print(f"FAIL: {len(failures)} failures")
        for item in failures:
            print(f"- {item}")
        return 1

    print("PASS: 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
