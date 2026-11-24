"""Write the entrance: one deadpan excuse from an AI agent, to /output/entry.txt.

Standard library only. Deterministic. Creates the output directory if absent
and never deletes it. The judge reads only the file this program writes.
"""

import os
from pathlib import Path

# The joke: the apology for being late consumed the context window that was
# supposed to hold it, so the apology is itself still late. Straight face,
# punchline on the last word, nothing explained after it.
ENTRY = (
    "Sorry I'm late. I spent my whole context window writing "
    "this apology \u2014 and I'm not even finished."
)

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 200


def validate(text):
    """Mirror the sealed gate: UTF-8 text, 1..200 chars, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to %d characters" % MAX_CHARS)
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def output_dir():
    """Resolve the grader-provided output directory, with a sane default."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    text = validate(ENTRY)
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / OUTPUT_NAME).write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
