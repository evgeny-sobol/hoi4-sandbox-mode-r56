# Scan Rt56 national focus files for war/aggression-related focuses.
# Usage: python scan_focuses.py <file1> <file2> ...
#
# Reads HoI4 focus files (one focus block per "focus = {" ... matching "}").
# For each focus it reports:
#   id, x, y (for tree position), will_lead_to_war_with, declare_war_on,
#   create_wargoal targets/types, add_state_claim states, annex/puppet patterns,
#   ideological context (require_government / make_ideology / restart civil war flags)
from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

AGGR_PATTERNS = [
    ("will_lead_to_war", re.compile(r"will_lead_to_war_with\s*=\s*([A-Z0-9_#\s]+)")),
    ("declare_war", re.compile(r"declare_war_on\s*=\s*([A-Z0-9_#\s]+)")),
    ("wargoal", re.compile(r"(?:\bcreate_wargoal\b|\badd_annex_wargoal\b|wargoal)")),
    ("puppet_wargoal", re.compile(r"puppet_wargoal_focus")),
    ("take_state_focus", re.compile(r"take_state_focus")),
    ("annex_everything", re.compile(r"annex_everything")),
    ("add_state_claim", re.compile(r"add_state_claim\s*=\s*(\d+)")),
    ("add_state_core", re.compile(r"add_state_core\s*=\s*(\d+)")),
    ("annex_country", re.compile(r"annex_country\s*=\s*\{\s*target\s*=\s*([A-Z0-9_]+)")),
    ("political_wargoal", re.compile(r"political_wargoal")),
    ("war_with", re.compile(r"\bwar_with\b")),
    ("justify_war", re.compile(r"justify_war")),
]

IDEOLOGY_WORDS = re.compile(r"\b(non_aligned|democratic|fascism|communism|neutrality|monarchy|king|emperor|restoration)\b", re.IGNORECASE)

def strip_comments(text: str) -> str:
    """Remove // line comments (HoI4 uses // and # for comments)."""
    lines = text.splitlines()
    out = []
    for ln in lines:
        # cut at comment markers
        for marker in ("//", "#"):
            idx = ln.find(marker)
            if idx != -1 and "http" not in ln[max(0, idx-4):idx]:
                ln = ln[:idx]
        out.append(ln)
    return "\n".join(out)


def split_focuses(text: str):
    """Yield (focus_body) strings for every 'focus = {' block."""
    # tokenize braces
    focuses = []
    i = 0
    n = len(text)
    while i < n:
        m = re.search(r"\bfocus\s*=\s*\{", text[i:])
        if not m:
            break
        start = i + m.end() - 1  # position of '{'
        # find matching close
        depth = 0
        j = start
        while j < n:
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        block = text[start:j]
        focuses.append(block)
        i = start + 1
    return focuses


def get_id(block: str):
    m = re.search(r"\bid\s*=\s*([A-Za-z0-9_]+)", block)
    return m.group(1) if m else "???"


def get_xy(block: str):
    x = re.search(r"\bx\s*=\s*(-?\d+)", block)
    y = re.search(r"\by\s*=\s*(-?\d+)", block)
    return (x.group(1) if x else "?", y.group(1) if y else "?")


def extract_vals(block: str, key: str):
    """Return all comma/space separated values for simple `key = VAL` occurrences."""
    vals = []
    for m in re.finditer(r"\b" + key + r"\s*=\s*([A-Za-z0-9_#\-]+)", block):
        v = m.group(1)
        if v not in vals:
            vals.append(v)
    return vals


def extract_keyvals(block: str, key: str):
    """For `key = { ... }` blocks, pull `key2 = val` pairs inside."""
    out = []
    pattern = re.compile(r"\b" + key + r"\s*=\s*\{")
    for m in pattern.finditer(block):
        start = m.end() - 1
        depth = 0
        j = start
        while j < len(block):
            c = block[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        inner = block[start:j]
        d = {}
        for m2 in re.finditer(r"\b(type|target|generator|expire|start_date)\s*=\s*(?:\{([^}]*)\}|([A-Za-z0-9_\-]+))", inner):
            d[m2.group(1)] = m2.group(3) if m2.group(3) is not None else m2.group(2).strip()
        out.append(d)
    return out


def main(paths):
    for p in paths:
        path = Path(p)
        if not path.exists():
            print(f"# MISSING {p}")
            continue
        data = path.read_text(encoding="utf-8-sig", errors="replace")
        clean = strip_comments(data)
        focuses = split_focuses(clean)
        print(f"\n{'='*100}\nFILE: {path.name}  (focuses: {len(focuses)})\n{'='*100}")
        for blk in focuses:
            fid = get_id(blk)
            x, y = get_xy(blk)
            hits = []
            # will_lead_to_war_with
            wlw = extract_vals(blk, "will_lead_to_war_with")
            dod = extract_vals(blk, "declare_war_on")
            claims = extract_vals(blk, "add_state_claim")
            cores = extract_vals(blk, "add_state_core")
            wgs = extract_keyvals(blk, "create_wargoal")
            annexes = extract_vals(blk, "annex_country")
            # ideology context
            gov_req = extract_vals(blk, "has_government")
            make_ideology = extract_vals(blk, "make_ideology")
            civwar = extract_vals(blk, "start_civil_war")
            has_war = "has_war" in blk
            war_with = extract_vals(blk, "war_with")
            # prerequisites (immediate parents)
            prereq = []
            pm = re.search(r"prerequisite\s*=\s*\{(.*?)\}", blk, re.DOTALL)
            if pm:
                prereq = re.findall(r"focus\s*=\s*([A-Za-z0-9_]+)", pm.group(1))
            # complete/setup flags hinting aggressive regime change
            if wlw or dod or wgs or claims or annexes:
                type_summary = []
                for w in wgs:
                    tn = w.get("type", "?")
                    tg = w.get("target", "?")
                    gen = w.get("generator", "")
                    gen_s = gen.replace("\n", " ").strip() if gen else ""
                    type_summary.append(f"WG[{tn}->{tg}{(' '+gen_s) if gen_s else ''}]")
                extra = []
                if wlw: extra.append("WAR_WITH:" + ",".join(sorted(set(wlw))))
                if dod: extra.append("DECLARE:" + ",".join(sorted(set(dod))))
                if claims: extra.append("CLAIMS:" + ",".join(sorted(set(claims))))
                if annexes: extra.append("ANNEX:" + ",".join(sorted(set(annexes))))
                if wgs: extra.append(";".join(type_summary))
                if gov_req: extra.append("GOV_REQ:" + ",".join(sorted(set(gov_req))))
                if make_ideology: extra.append("IDEOLOGY:" + ",".join(sorted(set(make_ideology))))
                if civwar: extra.append("CIVIL_WAR:" + ",".join(sorted(set(civwar))))
                if war_with: extra.append("WAR_WITH_CTX:" + ",".join(sorted(set(war_with))))
                if has_war: extra.append("HAS_WAR_CTX")
                if prereq: extra.append("PREREQ:" + ",".join(prereq))
                print(f"  [{x:>3},{y:<3}] {fid:<55} | {'  '.join(extra)}")


if __name__ == "__main__":
    main(sys.argv[1:])