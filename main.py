#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one single line of honest, funny error copy to
$MAKEFUN_OUTPUT_DIR/entry.txt (the file the sealed gate reads).
The line must stay 1-200 characters, a single line, UTF-8.
"""

import os
import sys

# The entry: one honest line, built from its beats so each beat can be
# tuned without touching the others. Kept to a single line, 1-200 chars.
_BEATS = (
    "Your file uploaded successfully \u2014 to a server we "
    "decommissioned yesterday.",
    "It is in the cloud now, in the literal sense.",
    "Please upload it again.",
)
LINE = " ".join(_BEATS)


def _entry_line() -> str:
    """Assemble the entry from its beats and validate it like the gate."""
    line = " ".join(_BEATS)
    if not (1 <= len(line) <= 200):
        raise ValueError(f"entry is {len(line)} chars, must be 1-200")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line with no blank edges")
    line.encode("utf-8")  # fail loudly here, not in the grader's sandbox
    return line


def _output_dir() -> str:
    """Where the gate reads entry.txt: the env dir, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def main() -> int:
    try:
        line = _entry_line()
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    path = os.path.join(_output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
