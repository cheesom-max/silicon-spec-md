#!/usr/bin/env python3
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"

PATH_PATTERN = re.compile(r"(?<![A-Za-z0-9_./-])(docs/[A-Za-z0-9_./<>-]+\.md)")


def main() -> int:
    failures: list[str] = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for m in PATH_PATTERN.finditer(text):
            match = m.group(1)
            if "<" in match or ">" in match or "xxxx" in match:
                continue
            target = ROOT / match
            if not target.exists():
                failures.append(f"{rel}: broken docs link target '{match}'")

    if failures:
        print(f"FAIL: {len(failures)} failures")
        for item in failures:
            print(f"- {item}")
        return 1

    print("PASS: 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
