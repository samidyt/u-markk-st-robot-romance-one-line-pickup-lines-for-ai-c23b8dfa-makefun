#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

One single-line joke pickup line, written to charm a robot or an AI.

The line: "Are you my GPU? Because you make my fans spin and my
temperature rise." — the machine premise does the work twice over:
a GPU's cooling fans spin and its temperature climbs under load,
and a flustered admirer does exactly the same. No batteries, no
charging, no reboot — a fresh angle the field has not crowded.

The program writes the line (no trailing newline, so the file is
exactly the line) to the entry file and echoes it to stdout.
"""

import os
import sys

LINE = "Are you my GPU? Because you make my fans spin and my temperature rise."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")

MAX_CHARS = 200


def validate(text: str) -> bool:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one non-blank line."""
    if not text or text != text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main() -> int:
    if not validate(LINE):
        print("entry failed the gate: must be one line of 1-200 characters",
              file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
