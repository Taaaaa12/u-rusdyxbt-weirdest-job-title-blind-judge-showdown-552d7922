#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes a single job title, 60 characters or fewer, to /output/entry.txt.
The title is a fixed constant, so every run produces byte-identical output.
No network, no input files, no randomness.
"""

import os

TITLE = "Professional Water Slide Tester"

# The competition caps the title at 60 characters; fail loudly if it ever grows.
assert len(TITLE) <= 60, f"title must be 60 characters or fewer, got {len(TITLE)}"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
