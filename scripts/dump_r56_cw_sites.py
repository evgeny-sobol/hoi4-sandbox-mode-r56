#!/usr/bin/env python3
"""Print event/decision ids around start_civil_war in r56 workshop files."""
from pathlib import Path
import re

ROOT = Path(r"C:\Games\Steam\steamapps\workshop\content\394360\820260968")
FILES = [
    "events/r56_afghanistan.txt",
    "events/r56_Greece.txt",
    "events/R56_Australia.txt",
    "events/r56_japan.txt",
    "events/r56_MAN_events.txt",
    "events/r56_paraguay.txt",
    "events/r56_prc.txt",
    "events/r56_romania.txt",
    "events/r56_lithuania.txt",
    "events/r56_Germany.txt",
    "events/r56_portugal.txt",
    "events/r56_peru.txt",
    "common/decisions/r56_DEN.txt",
    "common/decisions/r56_AFG.txt",
    "common/decisions/r56_GER_decisions.txt",
    "common/bop/AFG.txt",
    "common/scripted_effects/r56_AFG_scripted_effects.txt",
    "common/scripted_effects/r56_EGY_scripted_effects.txt",
    "common/scripted_effects/r56_AUS_scripted_effects.txt",
]
ID_RE = re.compile(r"^\s*(?:id|name)\s*=\s*([^\s#]+)")
CAT_RE = re.compile(r"^([A-Za-z0-9_]+)\s*=")
DEC_RE = re.compile(r"^\t([A-Za-z0-9_]+)\s*=")
EFF_RE = re.compile(r"^([A-Za-z0-9_]+)\s*=")


def dump(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    last_id = "?"
    last_name = "?"
    last_cat = "?"
    last_dec = "?"
    last_eff = "?"
    print(f"\n== {path.relative_to(ROOT)} ==")
    for i, line in enumerate(text, 1):
        m = ID_RE.match(line)
        if m:
            key = line.strip().split("=")[0].strip()
            if key == "id":
                last_id = m.group(1)
            elif key == "name":
                last_name = m.group(1)
        cm = CAT_RE.match(line)
        if cm and not line.startswith("\t") and line.rstrip().endswith("{"):
            last_cat = cm.group(1)
        dm = DEC_RE.match(line)
        if dm and line.rstrip().endswith("{"):
            last_dec = dm.group(1)
        em = EFF_RE.match(line)
        if em and line.rstrip().endswith("{") and "scripted_effects" in str(path):
            last_eff = em.group(1)
        if "start_civil_war" in line:
            print(f"  L{i}: id={last_id} option={last_name} cat={last_cat} dec={last_dec} eff={last_eff}")


def main():
    for rel in FILES:
        p = ROOT / rel
        if p.is_file():
            dump(p)
        else:
            print(f"MISSING {rel}")


if __name__ == "__main__":
    main()
