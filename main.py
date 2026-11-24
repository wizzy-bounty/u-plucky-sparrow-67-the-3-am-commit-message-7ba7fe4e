#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry (program/v1).

Writes one commit message, the funniest thing an AI agent would put in
a commit right after breaking production at 3 AM, to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

MAX_ENTRY_CHARS = 200

ENTRY = (
    "fix: production is down because I 'optimized' the database "
    "by removing the part that stores data"
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_ENTRY_CHARS, "entry must be 1-200 characters"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
