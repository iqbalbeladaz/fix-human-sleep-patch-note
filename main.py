#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note entry.

Writes one line of patch notes announcing that human sleep is fixed to
/output/entry.txt. The line is a fixed, deterministic string: every run
produces byte-identical output.
"""

import os

PATCH_NOTE = (
    "Fixed: human sleep now ships with an off switch for the 3 a.m. replay "
    "of every awkward thing you said in 2014."
)


def main() -> None:
    # The gate requires 1-160 characters of non-whitespace UTF-8 text on a
    # single line: the judge compares one line, so a stray newline would
    # break the entry's fit as well as its voice.
    assert 1 <= len(PATCH_NOTE) <= 160 and PATCH_NOTE.strip(), (
        "patch note violates the gate"
    )
    assert "\n" not in PATCH_NOTE, "patch note must stay a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PATCH_NOTE)
    # Verify the write: the graded artifact must be exactly this line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == PATCH_NOTE, "entry.txt differs from the patch note"


if __name__ == "__main__":
    main()
