#!/usr/bin/env python3
import sys
from pathlib import Path


def check_file(path: Path) -> list[tuple[int, str]]:
    """Return list of (line_number, message) violations for heading spacing.

    Rule: After any Markdown ATX heading line (starting with '#'), there must be
    exactly one blank line before the next non-blank content line.
    """
    violations: list[tuple[int, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if line.lstrip().startswith("#") and line.strip().startswith("#"):
            # It's a heading line if it begins with '#' ignoring leading spaces
            # (we don't validate valid ATX syntax beyond that).
            # Count consecutive blank lines following this heading.
            j = i + 1
            blanks = 0
            while j < n and lines[j].strip() == "":
                blanks += 1
                j += 1
            if j < n:  # only check when there's subsequent content
                if blanks == 0:
                    violations.append((i + 1, "Missing blank line after heading"))
                elif blanks > 1:
                    violations.append((i + 1, f"Too many blank lines after heading: {blanks}"))
        i += 1
    return violations


def main() -> int:
    base = Path("docs")
    if not base.exists():
        print("No docs/ directory found", file=sys.stderr)
        return 2
    failures = 0
    for md in base.rglob("*.md"):
        viols = check_file(md)
        if viols:
            failures += 1
            print(f"\n{md}")
            for ln, msg in viols:
                print(f"  L{ln}: {msg}")
    if failures:
        print(f"\nFound spacing issues in {failures} file(s).", file=sys.stderr)
        return 1
    print("All Markdown heading spacing checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

