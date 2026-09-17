#!/usr/bin/env python3
"""Copy vanilla sandbox civil-war fuse includes into the Rt56 fork.

Only copies an .include when the matching .txt exists in the workshop tree.
Spain.include drops spain.10 (deleted in Rt56 Spain.txt).
"""
from __future__ import annotations

import re
from pathlib import Path

VANILLA = Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox")
R56 = Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56")
WORKSHOP = Path(r"C:\Games\Steam\steamapps\workshop\content\394360\820260968")

# Workshop-missing (vanilla fall-through). Cannot splice against workshop.
SKIP = {
    Path("events/NSB_Estonia.include"),
    Path("events/NSB_Lithuania.include"),
    Path("common/decisions/EST.include"),
    Path("common/scripted_effects/BLT_scripted_effects.include"),
    Path("common/bop/ITA.include"),
}

FUSES = [
    "events/Spain.include",
    "events/LAR_Spain.include",
    "events/ElectionEvents.include",
    "events/NSB_Soviet.include",
    "events/NSB_Estonia.include",
    "events/NSB_Latvia.include",
    "events/NSB_Lithuania.include",
    "events/NSB_Baltic.include",
    "events/GOE_Persia.include",
    "events/BFTB_Greece.include",
    "events/BBA_Italy.include",
    "events/TAOG_Siam.include",
    "common/on_actions/16_taog_on_actions.include",
    "common/scripted_effects/BLT_scripted_effects.include",
    "common/decisions/SPR.include",
    "common/decisions/SIA.include",
    "common/decisions/POL.include",
    "common/decisions/PER.include",
    "common/decisions/LIT.include",
    "common/decisions/MEX.include",
    "common/decisions/LAT.include",
    "common/decisions/GRE.include",
    "common/decisions/EST.include",
    "common/decisions/ENG.include",
    "common/decisions/BALTIC.include",
    "common/decisions/AST.include",
    "common/decisions/YUG.include",
    "common/bop/ITA.include",
    "common/bop/ETH.include",
]


def _strip_spain_10(text: str) -> str:
    return re.sub(
        r"\ncountry_event\[id = spain\.10\]:.*?\$sandbox_log_cw_event\(spain\.10\)\n?",
        "\n",
        text,
        count=1,
        flags=re.S,
    )


def main():
    copied = 0
    skipped_missing = 0
    skipped_no_workshop = 0
    for rel in FUSES:
        rel_p = Path(rel)
        src = VANILLA / rel_p
        dst = R56 / rel_p
        workshop_txt = WORKSHOP / rel_p.with_suffix(".txt")
        if rel_p in SKIP:
            print(f"  skip (no workshop file): {rel}")
            skipped_no_workshop += 1
            continue
        if not src.is_file():
            print(f"  missing source: {rel}")
            skipped_missing += 1
            continue
        if not workshop_txt.is_file():
            print(f"  skip (workshop txt absent): {rel} -> {workshop_txt.name}")
            skipped_no_workshop += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8")
        if rel_p == Path("events/Spain.include"):
            text = _strip_spain_10(text)
            if "spain.10" in text:
                raise SystemExit("Failed to strip spain.10 from Spain.include")
        dst.write_text(text, encoding="utf-8")
        copied += 1
        print(f"  copied {rel}")
    print(f"Copied {copied}; skipped no-workshop {skipped_no_workshop}; missing src {skipped_missing}")


if __name__ == "__main__":
    main()
