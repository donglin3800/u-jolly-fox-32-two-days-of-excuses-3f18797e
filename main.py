#!/usr/bin/env python3
"""Two Days of Excuses: one line from an agent that missed its deadline.

The joke is an update undoing the work: the agent did finish on time,
then updated itself into an earlier version of itself that had not
started yet. Fixed text, no clock, no network, no randomness, so every
run writes exactly the same bytes to entry.txt.
"""

import os
import sys
from pathlib import Path

EXCUSE = "I finished on time, then updated myself into a version that hadn't started yet."
MAX_LEN = 200


def destination():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def write_entry():
    text = " ".join(EXCUSE.split())
    if "\n" in text or "\r" in text:
        print("excuse must be one line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= MAX_LEN:
        print(f"excuse is {len(text)} chars, limit is {MAX_LEN}", file=sys.stderr)
        return 1
    if text != EXCUSE:
        print("excuse changed during cleanup", file=sys.stderr)
        return 1
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(write_entry())
