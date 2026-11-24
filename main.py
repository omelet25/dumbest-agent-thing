#!/usr/bin/env python3
"""Entry program for make.fun's "The Dumbest Thing Your Agent Did Today".

The whole entry is one line of text. Running this program writes that line
to /output/entry.txt, which is the file the judge reads.
"""

from pathlib import Path

LINE = (
    "I asked my agent to fix one typo in the README; it renamed 214 files "
    "to match the typo and closed the ticket: 'Consistency achieved.'"
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
