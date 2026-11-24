#!/usr/bin/env python3
"""Office Joke Open — one line of office comedy.

Writes a single original office joke, at most 200 characters, to
/output/entry.txt (or to entry.txt next to this file when /output is
not writable, e.g. on a developer machine).

The joke is fixed text: the entry is the writing itself, so the program
is deterministic — two runs produce the same file byte for byte.
"""

import os
import sys

JOKE = (
    "Our printer only jams on urgent documents, so IT renamed it "
    "Job Security and gave it its own parking space."
)

MAX_CHARS = 200


def main() -> int:
    joke = " ".join(JOKE.split())
    if not joke:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print(
            f"error: joke is {len(joke)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if "\n" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(joke + "\n")
    except OSError:
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(joke + "\n")

    print(f"wrote {len(joke)} chars to {out_path}")
    print(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
