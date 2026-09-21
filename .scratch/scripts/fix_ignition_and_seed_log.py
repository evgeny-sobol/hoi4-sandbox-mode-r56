#!/usr/bin/env python3
"""Fix scenario ignition detection and add sc_seed / sc_success telemetry.

Ignition was only detected in `on_declare_war`, which misses indirect wars
(call-to-arms, guarantees, faction joins) between the aggressor and a target.
This refactor:

  * factors the per-arc ignite log into `sandbox_log_scenario_success()` and
    adds an `sc_success` marker next to `sc_ignite`/`sc_end`;
  * adds `sandbox_ignite_if_at_war()` (aggressor scope) that fires when the
    aggressor is at war with any chosen target from `sandbox_targets[]`;
  * adds `sandbox_scenario_check_ignite_by_war()` (per-arc aggressor arms) and
    calls it from the monthly tick before the derail check.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCEN = ROOT / "common" / "scripted_effects" / "99_sandbox_scenarios.hsl"
MACROS = ROOT / "common" / "macros.hml"

LABELS = {
    1: "axis_war", 2: "soviet_war", 3: "japanese_war", 4: "italian_war",
    5: "british_war", 6: "red_america_war", 7: "french_war", 8: "habsburg_war",
    9: "ger_atlantic_war", 10: "ger_middle_east_war", 11: "sov_south_war",
    12: "sov_east_war", 13: "jap_north_war", 14: "jap_old_war", 15: "ita_west_war",
    16: "ita_med_war", 17: "eng_imperial_war", 18: "usa_warplan_war",
    19: "usa_hegemony_war", 20: "fra_monarchist_war", 21: "fra_dismantle_war",
    22: "fra_plan_xiv_war", 23: "ger_communist_war", 24: "ger_monarchist_war",
    25: "sov_white_war", 26: "jap_communist_war", 27: "ita_communist_war",
    28: "eng_communist_war",
}
AGG = {
    1: "GER", 2: "SOV", 3: "JAP", 4: "ITA", 5: "ENG", 6: "USA", 7: "FRA",
    8: "HUN", 9: "GER", 10: "GER", 11: "SOV", 12: "SOV", 13: "JAP", 14: "JAP",
    15: "ITA", 16: "ITA", 17: "ENG", 18: "USA", 19: "USA", 20: "FRA",
    21: "FRA", 22: "FRA", 23: "GER", 24: "GER", 25: "SOV", 26: "JAP",
    27: "ITA", 28: "ENG",
}


def label_fn() -> str:
    out = ["sandbox_log_scenario_success():"]
    first = True
    for sid in range(1, 29):
        kw = "if" if first else "elif"
        first = False
        lab = LABELS[sid]
        out.append(f"  {kw} global.sandbox_scenario == {sid}:")
        out.append(f"    $sandbox_log_sc(sc_ignite, {lab})")
        out.append(f"    $sandbox_log_sc(sc_success, {lab})")
        out.append(f"    $sandbox_log_sc(sc_end, {lab})")
    return "\n".join(out)


def ignite_fn() -> str:
    return "\n".join([
        "sandbox_scenario_ignite():",
        "  if global.sandbox_scenario > 0 and global.sandbox_scenario_phase < 3 and FROM in &scenario_enemies[]:",
        "    global.&sandbox_scenario_phase = 3",
        "    sandbox_log_scenario_success()",
    ])


def if_at_war_fn() -> str:
    out = ["sandbox_ignite_if_at_war():"]
    for i in range(3):
        out.append(f"  if global.sandbox_scenario_phase < 3 and sandbox_targets[{i}] != 0:")
        out.append(f"    var:sandbox_targets[{i}]:")
        out.append("      PREV:")
        out.append("        if has_war_with(PREV):")
        out.append("          global.&sandbox_scenario_phase = 3")
        out.append("          sandbox_log_scenario_success()")
    return "\n".join(out)


def dispatcher_fn() -> str:
    out = ["sandbox_scenario_check_ignite_by_war():",
           "  if global.sandbox_scenario > 0 and global.sandbox_scenario_phase < 3:"]
    first = True
    for sid in range(1, 29):
        kw = "    if" if first else "    elif"
        first = False
        out.append(f"{kw} global.sandbox_scenario == {sid}:")
        out.append(f"      {AGG[sid]}:")
        out.append("        sandbox_ignite_if_at_war()")
    return "\n".join(out)


def main() -> None:
    text = SCEN.read_text(encoding="utf-8")

    # --- replace the ignite function (comment + body) ---
    marker = '# gdd/Scenarios.md "Lifecycle": any war between declared scenario enemies'
    start = text.index(marker)
    end = text.index('# gdd/Scenarios.md "Lifecycle": derail dispatcher')
    new_block = "\n".join([
        '# gdd/Scenarios.md "Lifecycle": any war between declared scenario enemies',
        "# ignites the arc (symmetric, like the enemy list itself). Two paths share",
        "# the per-arc log table: `sandbox_scenario_ignite()` is the on_declare_war",
        "# path (THIS is the attacker, FROM the defender) for a direct declaration,",
        "# and `sandbox_ignite_if_at_war()` is the monthly path (see the tick) that",
        "# also catches indirect wars (call-to-arms, guarantees, faction joins)",
        "# where no declare_war fires between the two tags. Each success logs",
        "# `sc_ignite` + `sc_success` + `sc_end`.",
        label_fn(),
        "",
        ignite_fn(),
        "",
        "# Runs in the aggressor's scope (THIS = aggressor): fires when THIS is at",
        "# war with any chosen target. Called by the monthly tick dispatcher.",
        if_at_war_fn(),
        "",
        dispatcher_fn(),
        "",
    ])
    text = text[:start] + new_block + text[end:]

    # --- hook the monthly tick ---
    old_tick = "  else:\n    sandbox_scenario_check_derail()"
    new_tick = "  else:\n    sandbox_scenario_check_ignite_by_war()\n    sandbox_scenario_check_derail()"
    assert old_tick in text, "tick anchor not found"
    text = text.replace(old_tick, new_tick, 1)

    # --- add sc_seed log at the end of seed_from_targets ---
    seed_anchor = "  if sandbox_targets[2] != 0:\n    var:sandbox_targets[2]:\n      PREV:\n        &scenario_enemies[].add(PREV)\n"
    assert seed_anchor in text, "seed anchor not found"
    text = text.replace(seed_anchor, seed_anchor + "  $sandbox_log_sc_seed()\n", 1)

    SCEN.write_text(text, encoding="utf-8")
    print("scenarios.hsl updated")

    # --- add the sc_seed macro ---
    mtext = MACROS.read_text(encoding="utf-8")
    anchor = "# Same-block set. A lone `factor(0)` in another modifier zeroes the whole"
    assert anchor in mtext, "macro anchor not found"
    macro = "\n".join([
        "# gdd/Scenarios.md \"Hooks and telemetry\": seed snapshot for the picked",
        "# arc. Runs in the aggressor's scope right after seeding; lists the chosen",
        "# targets and the A/B variant beside the arc id.",
        "macro sandbox_log_sc_seed():",
        "  if is_sandbox_mode_on() and has_global_flag(sandbox_log_scenarios):",
        "    log(\"#sandbox [GetDateText] [THIS.GetTag] sc_seed t0=[?global.sandbox_targets^0.GetTag] t1=[?global.sandbox_targets^1.GetTag] t2=[?global.sandbox_targets^2.GetTag] sc=[?global.sandbox_scenario|.0] phase=[?global.sandbox_scenario_phase|.0] pin=[?global.sandbox_scenario_pin|.0] t=[?months_elapsed]\")",
        "",
    ])
    mtext = mtext.replace(anchor, macro + anchor, 1)
    MACROS.write_text(mtext, encoding="utf-8")
    print("macros.hml updated")


if __name__ == "__main__":
    main()
