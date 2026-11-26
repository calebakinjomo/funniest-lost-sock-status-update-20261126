#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun bounty entry.

Writes one status update (<= 120 characters) in the voice of a lost sock
to /output/entry.txt.

The joke: every lost-sock story blames the dryer. This sock flips it —
it was never eaten, it walked out, because its owner commits the one
unforgivable sock crime: socks with sandals. The punchline lands in the
last three words.
"""

import os

ENTRY = "I wasn't eaten by the dryer. I left. He wears socks with sandals. I have standards."
MAX_CHARS = 120


def validate(text: str) -> str:
    """Gate the line exactly the way the sealed scorer does: UTF-8 text,
    1 to 120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
