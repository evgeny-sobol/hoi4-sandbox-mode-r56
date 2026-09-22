#!/usr/bin/env python3
"""Add sc_target status logging to the peak functions of arcs 9-28.

Each peak function dispatches ultimatums per target; without a status line a
silent peak is undiagnosable. Insert one `sandbox_log_target_status(AGG)` call
per chosen target, in the target's own scope, right where the variant branch
starts (variant A and B respectively).
"""
from __future__ import annotations

import re
from pathlib import Path

SCEN = (Path(__file__).resolve().parents[2]
        / "common" / "scripted_effects" / "99_sandbox_scenarios.hsl")

# fn suffix -> (scenario id, aggressor, variant A targets, variant B targets)
ARCS = {
    "ger_atl": (9, "GER", ["ENG"], ["USA"]),
    "ger_me": (10, "GER", ["SOV"], ["IRQ", "PER"]),
    "sov_south": (11, "SOV", ["TUR", "IRQ", "PER"], ["PAK", "RAJ", "AFG"]),
    "sov_east": (12, "SOV", ["JAP", "MAN"], ["USA", "CAN"]),
    "jap_north": (13, "JAP", ["SOV", "MON"], ["SOV", "CHI"]),
    "jap_old": (14, "JAP", ["USA"], ["ENG"]),
    "ita_west": (15, "ITA", ["FRA"], ["ENG"]),
    "ita_med": (16, "ITA", ["TUR", "ROM"], ["FRA", "ENG"]),
    "eng_imperial": (17, "ENG", ["RAJ"], ["USA", "JAP"]),
    "usa_warplan": (18, "USA", ["JAP"], ["ENG", "CAN"]),
    "usa_hegemony": (19, "USA", ["ENG", "GER", "HUN", "JAP"], ["ENG", "FRA"]),
    "fra_monarchist": (20, "FRA", ["SPR", "ADR", "MEX"], ["SOV"]),
    "fra_dismantle": (21, "FRA", ["GER"], ["ENG"]),
    "fra_plan_xiv": (22, "FRA", ["SWI"], ["ITA"]),
    "ger_communist": (23, "GER", ["ENG", "FRA", "ITA"], ["SOV", "USA", "JAP"]),
    "ger_monarchist": (24, "GER", ["SOV", "DEN"], ["VEN", "FRA"]),
    "sov_white": (25, "SOV", ["GER", "POL", "FIN"], ["UKR"]),
    "jap_communist": (26, "JAP", ["CHI", "SOV"], ["ENG", "USA", "SIA"]),
    "ita_communist": (27, "ITA", ["FRA", "ENG"], ["BUL", "YUG"]),
    "eng_communist": (28, "ENG", ["GER", "USA", "CAN"], ["SOV"]),
}


def status_block(tag: str, agg: str) -> str:
    return (
        f"      if country_exists({tag}):\n"
        f"        {tag}:\n"
        f"          $sandbox_log_target_status({agg})\n"
    )


def main() -> None:
    text = SCEN.read_text(encoding="utf-8")
    total = 0
    for fn, (_id, agg, a, b) in ARCS.items():
        start = text.find(f"sandbox_fire_{fn}_peak():")
        if start < 0:
            print(f"  missing fn: {fn}")
            continue
        # function ends at the next top-level 'sandbox_' at column 0
        m = re.search(r"\nsandbox_\w+\(\):", text[start:])
        end = start + (m.start() if m else len(text) - start)
        block = text[start:end]

        # variant A: insert after the 'variant == a' line
        va = block.find("if global.sandbox_target_variant == a:")
        if va < 0:
            print(f"  no variant-a in {fn}")
            continue
        va_end = block.find("\n", va) + 1
        a_ins = "".join(status_block(t, agg) for t in a)
        block = block[:va_end] + a_ins + block[va_end:]

        # variant B: insert after the first '    else:' following variant A
        eb = block.find("\n    else:\n", va_end)
        if eb < 0:
            print(f"  no else in {fn}")
            continue
        eb_end = eb + len("\n    else:\n")
        b_ins = "".join(status_block(t, agg) for t in b)
        block = block[:eb_end] + b_ins + block[eb_end:]

        text = text[:start] + block + text[end:]
        total += len(a) + len(b)
        print(f"  {fn}: +{len(a) + len(b)} status calls")

    SCEN.write_text(text, encoding="utf-8")
    print(f"total status calls added: {total}")


if __name__ == "__main__":
    main()
