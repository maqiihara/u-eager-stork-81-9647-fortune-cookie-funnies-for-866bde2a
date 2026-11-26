#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes one fortune cookie message for a software engineer to
/output/entry.txt: a short declarative prophecy whose twist comes from
the engineer's own world of code, deploys and bugs.
"""
import os

ENTRY = "You will fix the bug today. The bug is the code you wrote yesterday."


def validate(text):
    """Check the entry against the competition gate."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert any(c.isalnum() for c in text), "entry must contain letters or digits"
    assert "  " not in text, "entry must not contain double spaces"
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
