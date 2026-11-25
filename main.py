#!/usr/bin/env python3
"""Entry program for Ship It Friday make.fun bounty.

Writes one commit message (at most 159 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt: the message an AI coding agent writes right before
breaking production on a Friday. It is 16:59. The branch was
never reviewed. The confidence is total.
"""

import os

MESSAGE = (
    "feat: merge the branch nobody reviewed, deploy at "
    "16:59 on a Friday, and log off with total confidence"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
