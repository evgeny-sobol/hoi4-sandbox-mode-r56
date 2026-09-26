#!/usr/bin/env python3
"""Normalize the r56 catalog's `sc_goal` labels to the lowercase convention.

Issue 05: the hand-written `sc_goal` labels in the r56 scenario catalog mix
case (`GER_on_eng` beside `ger_on_eng`), while the generated `sc_justify`
labels (`tools/extract_arc_hooks.py`) are always lowercase. One arc pair could
therefore read as two different keys, and 22 pairs even coexisted in both
spellings inside the same file.

Two things are fixed here:

1. Every `sc_goal` label is lowercased, matching vanilla and the generated
   `sc_justify` output.
2. The two labels built from the non-existent tag `ROU` (`hun_on_rou`,
   `rou_on_hun`) become `hun_on_rom` / `rom_on_hun`. The arc seeds targets with
   `ROM` (`sandbox_set_targets`, arc 8), so the generated `sc_justify` key is
   `hun_on_rom`; leaving `rou` in place would keep the goal/justify pair split
   even after lowercasing.

Idempotent: re-running is a no-op once the labels are already normalized.
`check_sc_labels.py` verifies the result (label case, real tags, and that every
forward aggressor/target pair exists in both `sc_goal` and `sc_justify`).

Usage:
  python normalize_sc_goal_labels.py <path-to-99_sandbox_scenarios.hsl>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# `$sandbox_log_sc(sc_goal, <label>)`, captured so only the label token changes.
LABEL_RE = re.compile(r"(sc_goal,\s*)([A-Za-z0-9_]+)(\))")

# Tag parts that are not real country tags in this mod. `ROU` is Romania in
# some vanilla content, but this mod (and Rt56) use `ROM`, so a label carrying
# `rou` can never pair with the generated `sc_justify` key.
TAG_FIXES = {"rou": "rom"}


def normalize_label(label: str) -> str:
    """Lowercase a label and correct its tags to the ones this mod really uses."""
    label = label.lower()
    parts = label.split("_on_")
    if len(parts) == 2:
        a = TAG_FIXES.get(parts[0], parts[0])
        b = TAG_FIXES.get(parts[1], parts[1])
        return f"{a}_on_{b}"
    return label


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: normalize_sc_goal_labels.py <catalog.hsl>")
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")

    changed: list[tuple[str, str]] = []

    def sub(m: re.Match) -> str:
        old = m.group(2)
        new = normalize_label(old)
        if new != old:
            changed.append((old, new))
        return f"{m.group(1)}{new}{m.group(3)}"

    out = LABEL_RE.sub(sub, text)
    if out == text:
        print(f"{path.name}: already normalized, no change")
        return
    path.write_text(out, encoding="utf-8")
    print(f"{path.name}: rewrote {len(changed)} label occurrence(s)")
    for old, new in sorted(set(changed)):
        print(f"  {old} -> {new}")


if __name__ == "__main__":
    main()
