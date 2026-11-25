#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes a single one-line joke about office life to /output/entry.txt.
The joke is fixed and deterministic: the same line on every run.
"""

JOKE = (
    "My out-of-office reply answers emails faster than anyone "
    "in the office, so HR just promoted it above me."
)


def main() -> None:
    """Write the joke line to /output/entry.txt, exactly as-is."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
