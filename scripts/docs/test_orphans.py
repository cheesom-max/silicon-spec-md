#!/usr/bin/env python3
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"
PATH_PATTERN = re.compile(r"(?<![A-Za-z0-9_./-])(docs/[A-Za-z0-9_./<>-]+\.md)")


def main() -> int:
    failures: list[str] = []

    doc_files = sorted(DOCS_DIR.rglob("*.md"))
    incoming: dict[str, int] = {
        doc.relative_to(ROOT).as_posix(): 0 for doc in doc_files
    }

    for source in doc_files:
        source_rel = source.relative_to(ROOT).as_posix()
        text = source.read_text(encoding="utf-8")
        for m in PATH_PATTERN.finditer(text):
            target = m.group(1)
            if "<" in target or ">" in target:
                continue
            if target == source_rel:
                continue
            if target in incoming:
                incoming[target] += 1

    for rel_path, count in incoming.items():
        if rel_path == "docs/00-README.md":
            continue
        if count == 0:
            failures.append(f"{rel_path}: orphaned (no inbound docs references)")

    if failures:
        print(f"FAIL: {len(failures)} failures")
        for item in failures:
            print(f"- {item}")
        return 1

    print("PASS: 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
