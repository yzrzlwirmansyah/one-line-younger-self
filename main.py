#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes the single line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

# The choice: the older self knows the six-minute boiler voicemail survives
# Dad, and that the ordinary, boring missed call will one day be the one
# he'd give anything to return. "While it's still boring" is the sting —
# the call you can still make is the one that feels like nothing.
ENTRY = (
    "After Dad dies, you'll keep his six-minute voicemail about the "
    "boiler; call him back while it's still boring."
)

MAX_CHARS = 200


def main() -> int:
    if not ENTRY.strip():
        print("error: entry is empty", file=sys.stderr)
        return 2
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 2
    if len(ENTRY) > MAX_CHARS:
        print(
            f"error: entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 2
    if "\r" in ENTRY or "\n" in ENTRY:
        print("error: entry must be a single line (no CR/LF)", file=sys.stderr)
        return 2

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the line is the whole entry.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
