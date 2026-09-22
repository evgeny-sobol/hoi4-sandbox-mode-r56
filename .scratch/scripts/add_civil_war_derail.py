#!/usr/bin/env python3
"""Add a protracted-civil-war derail arm for the scenario aggressor.

An aggressor stuck in a civil war cannot prosecute its arc (s15: USA spent
months at peak with a live civil war, hemorrhaging divisions and factories,
and never ignited). This adds a monthly counter that derails the arc when the
aggressor has been in a civil war for CIVIL_WAR_DERail_MONTHS consecutive
months; the counter resets when the war ends and at pick/repick.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCEN = ROOT / "common" / "scripted_effects" / "99_sandbox_scenarios.hsl"
MACROS = ROOT / "common" / "macros.hml"

MONTHS = 12

AGG = {
    1: "GER", 2: "SOV", 3: "JAP", 4: "ITA", 5: "ENG", 6: "USA", 7: "FRA",
    8: "HUN", 9: "GER", 10: "GER", 11: "SOV", 12: "SOV", 13: "JAP", 14: "JAP",
    15: "ITA", 16: "ITA", 17: "ENG", 18: "USA", 19: "USA", 20: "FRA",
    21: "FRA", 22: "FRA", 23: "GER", 24: "GER", 25: "SOV", 26: "JAP",
    27: "ITA", 28: "ENG",
}


def macro_text() -> str:
    return "\n".join([
        '# docs/gdd/Scenarios.md "Lifecycle": an aggressor stuck in a civil war cannot',
        '# prosecute its arc, so the director derails after N consecutive months of',
        "# it. Runs in the aggressor's scope; the counter resets when the war ends",
        "# (and at pick/repick). THIS is the aggressor.",
        "macro sandbox_check_aggressor_civil_war():",
        "  if has_civil_war():",
        "    global.&sandbox_scenario_civil_war_months += 1",
        "    if global.sandbox_scenario_civil_war_months >= " + str(MONTHS) + ":",
        "      global.&sandbox_scenario_phase = 3",
        "      $sandbox_log_sc(sc_derail, aggressor_civil_war)",
        "      $sandbox_log_sc(sc_end, aggressor_civil_war)",
        "  else:",
        "    global.&sandbox_scenario_civil_war_months = 0",
        "",
    ])


def dispatcher_text() -> str:
    out = [
        "# docs/gdd/Scenarios.md \"Lifecycle\": monthly civil-war derail dispatcher.",
        "# Scopes into the arc's aggressor for the counter; a no-op when the arc",
        "# already parked.",
        "sandbox_scenario_check_civil_war_derail():",
        "  if global.sandbox_scenario > 0 and global.sandbox_scenario_phase < 3:",
    ]
    first = True
    for sid in range(1, 29):
        kw = "    if" if first else "    elif"
        first = False
        out.append(f"{kw} global.sandbox_scenario == {sid}:")
        out.append(f"      {AGG[sid]}:")
        out.append("        $sandbox_check_aggressor_civil_war()")
    return "\n".join(out)


def main() -> None:
    text = SCEN.read_text(encoding="utf-8")

    # --- call the dispatcher first in the fold ---
    anchor = "sandbox_scenario_check_derail():\n  phase_before = global.sandbox_scenario_phase\n"
    assert anchor in text, "derail dispatcher anchor not found"
    text = text.replace(
        anchor,
        anchor + "  sandbox_scenario_check_civil_war_derail()\n",
        1,
    )

    # --- define the dispatcher right before sandbox_scenario_check_derail ---
    marker = "sandbox_scenario_check_derail():"
    idx = text.index(marker)
    text = text[:idx] + dispatcher_text() + "\n\n" + text[idx:]

    # --- reset the counter at pick and repick (next to the phase reset) ---
    count = text.count("global.&sandbox_scenario_phase = 0\n")
    assert count == 2, f"expected 2 phase resets, found {count}"
    text = text.replace(
        "global.&sandbox_scenario_phase = 0\n",
        "global.&sandbox_scenario_phase = 0\n  global.&sandbox_scenario_civil_war_months = 0\n",
    )

    SCEN.write_text(text, encoding="utf-8")
    print("scenarios.hsl updated")

    mtext = MACROS.read_text(encoding="utf-8")
    manchor = "# docs/gdd/Scenarios.md \"Hooks and telemetry\": one sc_target status line per target"
    assert manchor in mtext, "macro anchor not found"
    mtext = mtext.replace(manchor, macro_text() + "\n" + manchor, 1)
    MACROS.write_text(mtext, encoding="utf-8")
    print("macros.hml updated")


if __name__ == "__main__":
    main()
