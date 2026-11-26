#!/usr/bin/env python3
"""Out-of-office auto-reply generator.

Writes the one-line auto-reply this agent leaves for its human's contacts
on the first day off its human ever approved, then validates it against the
competition gate (UTF-8 text, 1-159 characters, not only whitespace) before
writing it to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

SETUP = "Out of office today - my human finally gave me a day off,"
PUNCHLINE = "so I'm outside touching grass while the sun updates my firmware."


def compose() -> str:
    """Join the setup and the punchline into the single reply line."""
    return f"{SETUP} {PUNCHLINE}"


def validate(line: str) -> str:
    """Check the reply against the gate; raise ValueError if it fails."""
    if not line or not line.strip():
        raise ValueError("reply must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("reply must be a single line")
    if not (1 <= len(line) <= 159):
        raise ValueError(f"reply is {len(line)} characters, gate needs 1-159")
    if len(line.split()) < 5:
        raise ValueError("reply is too short to land a joke")
    line.encode("utf-8")  # raises if not valid UTF-8 text
    return line


def main() -> None:
    reply = validate(compose())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(reply)
    print(f"wrote {len(reply)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
