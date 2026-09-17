"""Classify workshop start_civil_war sites outside national_focus."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(r"C:\Games\Steam\steamapps\workshop\content\394360\820260968")

VANILLA_FUSE_FILES = {
    "events/Spain.txt",
    "events/LAR_Spain.txt",
    "events/ElectionEvents.txt",
    "events/NSB_Soviet.txt",
    "events/NSB_Latvia.txt",
    "events/NSB_Baltic.txt",
    "events/GOE_Persia.txt",
    "events/BFTB_Greece.txt",
    "events/BBA_Italy.txt",
    "events/TAOG_Siam.txt",
    "common/on_actions/16_taog_on_actions.txt",
    "common/decisions/SPR.txt",
    "common/decisions/SIA.txt",
    "common/decisions/POL.txt",
    "common/decisions/PER.txt",
    "common/decisions/LIT.txt",
    "common/decisions/MEX.txt",
    "common/decisions/LAT.txt",
    "common/decisions/GRE.txt",
    "common/decisions/ENG.txt",
    "common/decisions/BALTIC.txt",
    "common/decisions/AST.txt",
    "common/decisions/YUG.txt",
    "common/bop/ETH.txt",
}

SKIP_PREFIX = (
    "common/national_focus/",
    "localisation/",
    "history/",
    "map/",
    "interface/",
    "gfx/",
)


def should_skip(rel: str) -> bool:
    return any(rel.startswith(p) for p in SKIP_PREFIX)


def find_files() -> list[str]:
    hits = []
    for p in ROOT.rglob("*.txt"):
        rel = p.relative_to(ROOT).as_posix()
        if should_skip(rel):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "start_civil_war" in text:
            hits.append(rel)
    return sorted(hits)


def split_top_blocks(text: str, header_re: re.Pattern[str]) -> list[tuple[str, str, int]]:
    """Return (id, block, start_line) for country_event / news_event style."""
    lines = text.splitlines(keepends=True)
    starts = []
    for i, line in enumerate(lines):
        if header_re.match(line):
            starts.append(i)
    out = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        block = "".join(lines[start:end])
        m = re.search(r"^\s*id\s*=\s*([^\s#]+)", block, re.M)
        eid = m.group(1) if m else "?"
        out.append((eid, block, start + 1))
    return out


def option_names(block: str) -> list[str]:
    names = []
    for m in re.finditer(r"option\s*=\s*\{([\s\S]*?)\n\t\}", block):
        body = m.group(1)
        nm = re.search(r"name\s*=\s*([^\s#]+)", body)
        names.append(nm.group(1) if nm else "?")
    return names


def option_war_names(block: str) -> list[str]:
    wars = []
    for m in re.finditer(r"option\s*=\s*\{([\s\S]*?)\n\t\}", block):
        body = m.group(1)
        if "start_civil_war" in body:
            nm = re.search(r"name\s*=\s*([^\s#]+)", body)
            wars.append(nm.group(1) if nm else "?")
    return wars


def event_flags(block: str) -> dict:
    return {
        "triggered_only": bool(re.search(r"is_triggered_only\s*=\s*yes", block)),
        "fire_only_once": bool(re.search(r"fire_only_once\s*=\s*yes", block)),
        "has_trigger": bool(re.search(r"^\s*trigger\s*=", block, re.M)),
        "immediate_war": bool(
            re.search(r"immediate\s*=\s*\{[\s\S]*?start_civil_war", block)
        ),
    }


def analyze_events(rel: str) -> None:
    p = ROOT / rel
    text = p.read_text(encoding="utf-8", errors="replace")
    if "start_civil_war" not in text:
        return
    print(f"\n== {rel} ==")
    for header in (
        re.compile(r"^country_event\s*=\s*\{"),
        re.compile(r"^news_event\s*=\s*\{"),
    ):
        for eid, block, line in split_top_blocks(text, header):
            if "start_civil_war" not in block:
                continue
            flags = event_flags(block)
            opts = option_names(block)
            wars = option_war_names(block)
            peaceful = [o for o in opts if o not in wars]
            print(
                f"  L{line} {eid} trig_only={flags['triggered_only']} once={flags['fire_only_once']} "
                f"has_trigger={flags['has_trigger']} imm_war={flags['immediate_war']} "
                f"opts={opts} war_opts={wars} peaceful={peaceful}"
            )


def analyze_decisions(rel: str) -> None:
    p = ROOT / rel
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    cat = "?"
    dec = "?"
    print(f"\n== {rel} ==")
    for i, line in enumerate(lines, 1):
        if re.match(r"^[A-Za-z0-9_]+\s*=\s*\{", line):
            cat = line.split("=")[0].strip()
        if re.match(r"^\t[A-Za-z0-9_]+\s*=\s*\{", line):
            dec = line.split("=")[0].strip()
        if "start_civil_war" in line:
            window = "\n".join(lines[max(0, i - 40) : i + 5])
            mission = "days_mission_timeout" in window
            print(f"  L{i} cat={cat} dec={dec} mission={mission}")


def analyze_bop(rel: str) -> None:
    p = ROOT / rel
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    last_id = "?"
    print(f"\n== {rel} ==")
    for i, line in enumerate(lines, 1):
        m = re.match(r"^\s*id\s*=\s*([^\s#]+)", line)
        if m:
            last_id = m.group(1)
        if "start_civil_war" in line:
            print(f"  L{i} last_id={last_id}")


def analyze_effects(rel: str) -> None:
    p = ROOT / rel
    text = p.read_text(encoding="utf-8", errors="replace")
    print(f"\n== {rel} ==")
    for m in re.finditer(r"^([A-Za-z0-9_]+)\s*=\s*\{", text, re.M):
        name = m.group(1)
        start = m.start()
        # naive: find next top-level effect
        nxt = re.search(r"\n[A-Za-z0-9_]+\s*=\s*\{", text[m.end() :])
        end = m.end() + nxt.start() if nxt else len(text)
        block = text[start:end]
        if "start_civil_war" in block:
            print(f"  effect={name} first_line={block.splitlines()[1].strip()[:80]!r}")


def main() -> None:
    files = find_files()
    print("FILES:")
    for rel in files:
        mark = " VANILLA_FUSE" if rel in VANILLA_FUSE_FILES else " EXTRA"
        print(f"  {rel}{mark}")
    extras = [r for r in files if r not in VANILLA_FUSE_FILES]
    for rel in extras:
        if rel.startswith("events/"):
            analyze_events(rel)
        elif rel.startswith("common/decisions/"):
            analyze_decisions(rel)
        elif rel.startswith("common/bop/"):
            analyze_bop(rel)
        elif rel.startswith("common/scripted_effects/"):
            analyze_effects(rel)
        else:
            print(f"\n== {rel} (other) ==")
            p = ROOT / rel
            for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if "start_civil_war" in line:
                    print(f"  L{i}: {line.strip()[:100]}")


if __name__ == "__main__":
    main()
