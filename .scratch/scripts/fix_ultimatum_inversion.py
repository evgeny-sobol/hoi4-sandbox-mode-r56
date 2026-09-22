#!/usr/bin/env python3
"""Fix inverted ultimatum options in scenario events for arcs 16-28.

A later generator emitted the defy/submit options mirrored vs the arcs 1-15
reference: submit at 70% (war averted) and defy at 30% with no rivalry push.
This restores the reference anatomy:

  submit (a): factor 30, add_war_support(-0.10), aggressor +0.05
  defy   (b): factor 70, add_war_support(0.10),  aggressor +0.05 + rivalry

The rivalry uses PREV (the event recipient = the target), because arcs 16-28
share one event between two variant targets, so a literal tag cannot be used.
"""
from __future__ import annotations

import re
from pathlib import Path

EVENTS = Path(__file__).resolve().parents[2] / "events"

FILES = {
    "99_sandbox_scenario_ita_med.hsl": "ITA",
    "99_sandbox_scenario_eng_imperial.hsl": "ENG",
    "99_sandbox_scenario_usa_warplan.hsl": "USA",
    "99_sandbox_scenario_usa_hegemony.hsl": "USA",
    "99_sandbox_scenario_fra_monarchist.hsl": "FRA",
    "99_sandbox_scenario_fra_dismantle.hsl": "FRA",
    "99_sandbox_scenario_fra_plan_xiv.hsl": "FRA",
    "99_sandbox_scenario_ger_communist.hsl": "GER",
    "99_sandbox_scenario_ger_monarchist.hsl": "GER",
    "99_sandbox_scenario_sov_white.hsl": "SOV",
    "99_sandbox_scenario_jap_communist.hsl": "JAP",
    "99_sandbox_scenario_ita_communist.hsl": "ITA",
    "99_sandbox_scenario_eng_communist.hsl": "ENG",
}

# Option blocks, matched as whole units (name + ai_chance + effects).
A_RE = re.compile(
    r"name\((?P<id>sandbox_\w+_\d+_a)\)\n"
    r"    ai_chance:\n"
    r"      factor\(70\)\n"
    r"    add_war_support\(0\.10\)\n"
)
B_RE = re.compile(
    r"name\((?P<id>sandbox_\w+_\d+_b)\)\n"
    r"    ai_chance:\n"
    r"      factor\(30\)\n"
    r"    add_war_support\(-0\.05\)\n"
    r"(?P<log>    \$sandbox_log_sc\(sc_crisis, \w+_defy\))"
)


def fix(text: str, agg: str) -> tuple[str, int]:
    count = 0

    def a_sub(m: re.Match) -> str:
        nonlocal count
        count += 1
        return (
            f"name({m.group('id')})\n"
            f"    ai_chance:\n"
            f"      factor(30)\n"
            f"    add_war_support(-0.10)\n"
        )

    def b_sub(m: re.Match) -> str:
        nonlocal count
        count += 1
        return (
            f"name({m.group('id')})\n"
            f"    ai_chance:\n"
            f"      factor(70)\n"
            f"    add_war_support(0.10)\n"
            f"    {agg}:\n"
            f"      add_war_support(0.05)\n"
            f"      $sandbox_add_rivalry_vs(PREV, 15)\n"
            f"{m.group('log')}"
        )

    text = A_RE.sub(a_sub, text)
    text = B_RE.sub(b_sub, text)
    return text, count


def main() -> None:
    for name, agg in FILES.items():
        path = EVENTS / name
        if not path.is_file():
            print(f"  missing: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        new, n = fix(text, agg)
        if n:
            path.write_text(new, encoding="utf-8")
        print(f"  {name}: {n} edits")


if __name__ == "__main__":
    main()
