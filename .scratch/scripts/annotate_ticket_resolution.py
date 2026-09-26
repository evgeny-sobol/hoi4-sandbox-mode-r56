#!/usr/bin/env python3
"""Append a resolution note to each r56 ticket's `## Comments` section.

The tracker convention (docs/agents/issue-tracker.md) puts comments and
conversation history at the bottom of the file under `## Comments`. These
tickets had none; this adds one note recording how the status was decided.

Idempotent: a ticket that already carries the note is skipped.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R56 = Path(r"c:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56")
DIRS = [
    R56 / ".scratch/scenario-target-variants/issues",
    R56 / ".scratch/scenario-engine-regressions/issues",
]

NOTE = """## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
"""

MARKER = "Status normalized to `resolved`"


def main() -> None:
    changed = 0
    for d in DIRS:
        for p in sorted(d.glob("*.md")):
            text = p.read_text(encoding="utf-8")
            if MARKER in text:
                continue
            text = text.rstrip("\n") + "\n\n" + NOTE
            p.write_text(text, encoding="utf-8")
            changed += 1
    print(f"{changed} file(s) annotated")


if __name__ == "__main__":
    main()
