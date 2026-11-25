#!/usr/bin/env python3
"""Snooze Button Roast: one line roasting an alarm clock at 6 AM Saturday.

Writes exactly one line of plain text to /output/entry.txt.
Pure Python stdlib, deterministic, no input, no network.
"""
from pathlib import Path

ENTRY = "My alarm clock rang at 6 AM on Saturday like my dreams owed it rent and it came to evict them."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Gate, mirrored locally before writing: one line, 1-200 chars, not blank.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200 and ENTRY.strip()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
