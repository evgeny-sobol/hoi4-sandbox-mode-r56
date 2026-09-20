#!/usr/bin/env python3
"""Generate national_focus .include files for the Rt56 sandbox fork.

gdd/National Focuses.md + gdd/Road to 56.md:
  * $ai_sandbox_modifier() on every id'd focus
  * $root_modifier() when there is no prerequisite
  * civil-war ignition + cap when the body contains start_civil_war
  * vanilla-include extras (party shares, Honor/rival gates, MIC, tyranny, CW roots)
    for IDs that still exist in Rt56
  * $sandbox_log_cw_ignition / $sandbox_log_cw_root on ignition and CW-root completion
    so game.log can tick gdd/Civil Wars.md
  * $crossroad_modifier(N) on optional exclusive groups
  * $ai_mic_modifier() on non-political industry focuses
  * $ai_civil_war_root_modifier() on exclusive ancestors of ignition focuses
  * Honor/rival AI + available for create_wargoal / declare_war / add_to_faction

Usage:
    python generate_focus_includes.py
"""

from __future__ import annotations

import os
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

RT56_FOCUS = Path(
    r"C:\Games\Steam\steamapps\workshop\content\394360\820260968\common\national_focus"
)
VANILLA_INCLUDES = Path(
    os.path.expandvars(r"%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox\common\national_focus")
)
VANILLA_MOD = Path(
    os.path.expandvars(r"%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox")
)
OUT_DIR = Path(
    os.path.expandvars(r"%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56\common\national_focus")
)
R56_MOD = Path(
    os.path.expandvars(r"%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56")
)

_WORD_CHARS = set(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
)
INDENT = "  "
FOCUS_HDR = re.compile(
    r"^(\s*)(focus|shared_focus|joint_focus)\[id = ([^\]]+)\]:\s*$"
)
TAG_RE = re.compile(r"^[A-Z][A-Z0-9]{2,}$")
ALIASES = {
    "SPA", "SPB", "SPC", "SPD", "VIC", "SOU", "SOB", "SOS", "SOT", "SOP",
    "BUF", "BUZ", "FGR", "FNO", "MOT", "RDS", "RSI", "SB1", "SB2", "SB3", "SB4",
}
PARTY_MARKERS = (
    "mtth:democracy_factor",
    "mtth:monarchy_factor",
    "mtth:communism_factor",
    "mtth:fascism_factor",
)
SKIP_MOD_MARKERS = (
    "$ai_sandbox_modifier()",
    "$root_modifier()",
    "$ai_civil_war_ignition_modifier()",
    "sandbox_civil_war_cap_reached()",
)
INTERVENTION_MARK = ("lesson", "interven", "volunteer")
UNCONST_MARK = (
    "seize_power", "coup", "ban_the_party", "suspend_election",
    "military_coup", "overthrow",
)
PURGE_MARK = ("_purge", "secret_police", "nkvd", "gestapo")
COUNTRY_TAGS = (
    "AFG", "CHI", "CHL", "COG", "ENG", "EST", "GER", "HOL", "HUN",
    "JAP", "NOR", "POL", "SOV", "SPR", "USA",
)
# Queues a CW event instead of calling start_civil_war in the focus body.
EXTRA_IGNITION_IDS = {
    "POR_ally_anti_colonial_resistance",
    "POR_center_stage_against_communism",
    "POR_avenge_the_1821_disaster",
    "LIT_launch_the_revolution",
}


def _is_word_char(text, i):
    return 0 <= i < len(text) and text[i] in _WORD_CHARS


def _skip_string(text, i):
    i += 1
    n = len(text)
    while i < n:
        if text[i] == '"':
            return i + 1
        i += 1
    return i


def _skip_comment(text, i):
    n = len(text)
    while i < n and text[i] != "\n":
        i += 1
    return i


def _match_closing_brace(text, open_pos):
    depth = 1
    i = open_pos
    n = len(text)
    while i < n:
        c = text[i]
        if c == "#":
            i = _skip_comment(text, i)
        elif c == '"':
            i = _skip_string(text, i)
        elif c == "{":
            depth += 1
            i += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
            i += 1
        else:
            i += 1
    raise ValueError("Unbalanced braces: no matching '}' found")


def _iter_named_blocks(text, name, start, end):
    i = start
    depth = 0
    nlen = len(name)
    while i < end:
        c = text[i]
        if c == "#":
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if c == "{":
            depth += 1
            i += 1
            continue
        if c == "}":
            depth -= 1
            i += 1
            continue
        if (
            depth == 0
            and not _is_word_char(text, i - 1)
            and text.startswith(name, i)
            and not _is_word_char(text, i + nlen)
        ):
            j = i + nlen
            while j < end and text[j] in " \t\r\n":
                j += 1
            if j < end and text[j] == "=":
                j += 1
                while j < end and text[j] in " \t\r\n":
                    j += 1
                if j < end and text[j] == "{":
                    open_pos = j + 1
                    close_pos = _match_closing_brace(text, open_pos)
                    yield (open_pos, close_pos)
                    i = close_pos + 1
                    continue
            i = i + nlen
            continue
        i += 1


def _iter_named_blocks_any_depth(text, name, start, end):
    i = start
    nlen = len(name)
    while i < end:
        c = text[i]
        if c == "#":
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if (
            not _is_word_char(text, i - 1)
            and text.startswith(name, i)
            and not _is_word_char(text, i + nlen)
        ):
            j = i + nlen
            while j < end and text[j] in " \t\r\n":
                j += 1
            if j < end and text[j] == "=":
                j += 1
                while j < end and text[j] in " \t\r\n":
                    j += 1
                if j < end and text[j] == "{":
                    open_pos = j + 1
                    close_pos = _match_closing_brace(text, open_pos)
                    yield (open_pos, close_pos)
                    i = close_pos + 1
                    continue
            i = i + nlen
            continue
        i += 1


def _read_direct_scalar(text, open_pos, close_pos, key):
    i = open_pos
    depth = 0
    klen = len(key)
    while i < close_pos:
        c = text[i]
        if c == "#":
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if c == "{":
            depth += 1
            i += 1
            continue
        if c == "}":
            depth -= 1
            i += 1
            continue
        if (
            depth == 0
            and not _is_word_char(text, i - 1)
            and text.startswith(key, i)
            and not _is_word_char(text, i + klen)
        ):
            j = i + klen
            while j < close_pos and text[j] in " \t\r\n":
                j += 1
            if j < close_pos and text[j] == "=":
                j += 1
                while j < close_pos and text[j] in " \t\r\n":
                    j += 1
                if j < close_pos and text[j] == "{":
                    i = _match_closing_brace(text, j + 1) + 1
                    continue
                if j < close_pos and text[j] == '"':
                    endq = _skip_string(text, j)
                    return text[j:endq].strip('"')
                k = j
                while k < close_pos and text[k] not in " \t\r\n}#":
                    k += 1
                return text[j:k]
            i = i + klen
            continue
        i += 1
    return None


def _read_all_direct_scalars(text, open_pos, close_pos, key):
    values = []
    i = open_pos
    depth = 0
    klen = len(key)
    while i < close_pos:
        c = text[i]
        if c == "#":
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if c == "{":
            depth += 1
            i += 1
            continue
        if c == "}":
            depth -= 1
            i += 1
            continue
        if (
            depth == 0
            and not _is_word_char(text, i - 1)
            and text.startswith(key, i)
            and not _is_word_char(text, i + klen)
        ):
            j = i + klen
            while j < close_pos and text[j] in " \t\r\n":
                j += 1
            if j < close_pos and text[j] == "=":
                j += 1
                while j < close_pos and text[j] in " \t\r\n":
                    j += 1
                if j < close_pos and text[j] == "{":
                    i = _match_closing_brace(text, j + 1) + 1
                    continue
                if j < close_pos and text[j] == '"':
                    endq = _skip_string(text, j)
                    values.append(text[j:endq].strip('"'))
                    i = endq
                    continue
                k = j
                while k < close_pos and text[k] not in " \t\r\n}#":
                    k += 1
                values.append(text[j:k])
                i = k
                continue
            i = i + klen
            continue
        i += 1
    return values


def _has_direct_block(text, open_pos, close_pos, key):
    for _ in _iter_named_blocks(text, key, open_pos, close_pos):
        return True
    return False


def _has_injectable_block(text, open_pos, close_pos, key):
    for _op, cl in _iter_named_blocks(text, key, open_pos, close_pos):
        line_start = text.rfind("\n", 0, cl) + 1
        return text[line_start:cl].strip() == ""
    return False


def _contains_token(text, open_pos, close_pos, token):
    i = open_pos
    nlen = len(token)
    while i < close_pos:
        c = text[i]
        if c == "#":
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if (
            not _is_word_char(text, i - 1)
            and text.startswith(token, i)
            and not _is_word_char(text, i + nlen)
        ):
            return True
        i += 1
    return False


def _indent_width(raw):
    return len(raw) - len(raw.lstrip(" \t"))


def _is_comment(line: str) -> bool:
    return line.lstrip().startswith("#")


def _dedent_lines(lines):
    nonempty = [l for l in lines if l.strip() and not _is_comment(l)]
    if not nonempty:
        return []
    base = min(_indent_width(l) for l in nonempty)
    out = []
    for l in lines:
        if not l.strip() or _is_comment(l):
            continue
        out.append(l[base:] if len(l) >= base else l.strip())
    return out


def _hsl_leaf(line: str) -> str:
    """Include '+' is only valid on headers (`+available:`). Strip it from HSL leaves."""
    stripped = line.lstrip()
    if stripped.startswith("+") and stripped[1:2].isalpha() and "(" in stripped:
        return stripped[1:]
    return stripped


@dataclass
class VanillaExtras:
    extra_mods: list[list[str]] = field(default_factory=list)
    available: list[str] | None = None
    completion: list[str] | None = None
    has_crossroad: bool = False
    has_mic: bool = False
    has_party: bool = False
    has_cw_root: bool = False
    has_tyranny: bool = False
    has_honor: bool = False
    has_sandbox_set: bool = False


@dataclass
class FocusInfo:
    fid: str
    kind: str
    tree_id: str | None
    open_pos: int
    close_pos: int
    has_awd: bool
    is_root: bool
    is_ignition: bool
    has_available: bool
    has_completion: bool
    exclusive: list[str]
    prereqs: list[str]
    filters: set[str]
    avail_text: str
    reward_text: str


def _parse_vanilla_body(body_lines: list[str]) -> VanillaExtras:
    extras = VanillaExtras()
    if not body_lines:
        return extras
    ded = _dedent_lines(body_lines)
    i = 0
    n = len(ded)

    def take_section(start, min_indent):
        j = start + 1
        chunk = []
        while j < n:
            line = ded[j]
            stripped = line.strip()
            if not stripped or _is_comment(line):
                j += 1
                continue
            if _indent_width(line) <= min_indent:
                break
            chunk.append(line)
            j += 1
        return _dedent_lines(chunk), j

    while i < n:
        line = ded[i]
        stripped = line.strip()
        col = _indent_width(line)
        if stripped in ("ai_will_do:", "+ai_will_do:"):
            inner, i = take_section(i, col)
            extras.extra_mods.extend(_split_modifiers(inner))
            continue
        if stripped in ("available:", "+available:"):
            extras.available, i = take_section(i, col)
            extras.has_honor = True
            continue
        if stripped in ("completion_reward:", "+completion_reward:"):
            extras.completion, i = take_section(i, col)
            continue
        i += 1

    kept = []
    for mod in extras.extra_mods:
        joined = "\n".join(mod)
        if any(m in joined for m in SKIP_MOD_MARKERS) and not any(
            x in joined for x in ("$ai_mic_modifier", "$crossroad_modifier", "$ai_civil_war_root",
                                  "$ai_cooperation", "$ai_antagonism", "$ai_betrayal",
                                  "$ai_rivalry", "$ai_war_support", "$ai_high_tyranny",
                                  "$ai_low_tyranny", "$ai_medium_tyranny")
        ) and not any(p in joined for p in PARTY_MARKERS):
            if "$ai_civil_war_ignition" in joined or "$ai_sandbox_modifier" in joined or "$root_modifier" in joined:
                continue
            if "sandbox_civil_war_cap_reached" in joined:
                continue
        if "$ai_sandbox_set" in joined:
            extras.has_sandbox_set = True
        if "$crossroad_modifier" in joined:
            extras.has_crossroad = True
        if "$ai_mic_modifier" in joined:
            extras.has_mic = True
        if any(p in joined for p in PARTY_MARKERS):
            extras.has_party = True
        if "$ai_civil_war_root_modifier" in joined:
            extras.has_cw_root = True
        if "tyranny" in joined:
            extras.has_tyranny = True
        if any(x in joined for x in ("$ai_cooperation", "$ai_antagonism", "$ai_betrayal", "$ai_rivalry", "not_rival")):
            extras.has_honor = True
        kept.append(mod)
    extras.extra_mods = kept
    if extras.completion and any("add_tyranny" in l or "tyranny" in l for l in extras.completion):
        extras.has_tyranny = True
    return extras


def _split_modifiers(lines: list[str]) -> list[list[str]]:
    mods = []
    i = 0
    n = len(lines)
    while i < n:
        stripped = lines[i].strip()
        if stripped in ("modifier:", "+modifier:"):
            col = _indent_width(lines[i])
            i += 1
            chunk = []
            while i < n:
                s = lines[i].strip()
                if s in ("modifier:", "+modifier:") and _indent_width(lines[i]) <= col:
                    break
                if s in ("available:", "+available:", "completion_reward:", "+completion_reward:") and _indent_width(lines[i]) <= col:
                    break
                chunk.append(lines[i])
                i += 1
            mods.append(_dedent_lines(chunk))
            continue
        i += 1
    return mods


def load_vanilla_extras() -> dict[str, VanillaExtras]:
    out: dict[str, VanillaExtras] = {}
    if not VANILLA_INCLUDES.is_dir():
        return out
    for path in VANILLA_INCLUDES.glob("*.include"):
        lines = path.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            m = FOCUS_HDR.match(lines[i])
            if not m:
                i += 1
                continue
            indent = len(m.group(1).replace("\t", "  "))
            fid = m.group(3)
            i += 1
            body = []
            while i < len(lines):
                raw = lines[i]
                hm = FOCUS_HDR.match(raw)
                if hm and len(hm.group(1).replace("\t", "  ")) <= indent:
                    break
                if raw.startswith("focus_tree["):
                    break
                body.append(raw)
                i += 1
            parsed = _parse_vanilla_body(body)
            if fid in out:
                if parsed.extra_mods or parsed.available or parsed.completion:
                    out[fid] = parsed
            else:
                out[fid] = parsed
    return out


def _filter_set(text, f_open, f_close):
    found = set()
    for op, cl in _iter_named_blocks(text, "search_filters", f_open, f_close):
        found.update(re.findall(r"FOCUS_FILTER_[A-Z_]+", text[op:cl]))
    return found


def _exclusive_ids(text, f_open, f_close):
    ids = []
    for op, cl in _iter_named_blocks(text, "mutually_exclusive", f_open, f_close):
        ids.extend(_read_all_direct_scalars(text, op, cl, "focus"))
    return ids


def _prereq_ids(text, f_open, f_close):
    ids = []
    for op, cl in _iter_named_blocks(text, "prerequisite", f_open, f_close):
        ids.extend(_read_all_direct_scalars(text, op, cl, "focus"))
    return ids


def collect_focuses(text) -> list[FocusInfo]:
    focuses: list[FocusInfo] = []
    for tree_open, tree_close in _iter_named_blocks(text, "focus_tree", 0, len(text)):
        tree_id = _read_direct_scalar(text, tree_open, tree_close, "id")
        for f_open, f_close in _iter_named_blocks(text, "focus", tree_open, tree_close):
            info = _focus_info(text, "focus", tree_id, f_open, f_close)
            if info:
                focuses.append(info)
    for kind in ("shared_focus", "joint_focus"):
        for f_open, f_close in _iter_named_blocks(text, kind, 0, len(text)):
            info = _focus_info(text, kind, None, f_open, f_close)
            if info:
                focuses.append(info)
    return focuses


def _focus_info(text, kind, tree_id, f_open, f_close) -> FocusInfo | None:
    fid = _read_direct_scalar(text, f_open, f_close, "id")
    if fid is None:
        return None
    avail = ""
    for op, cl in _iter_named_blocks(text, "available", f_open, f_close):
        avail = text[op:cl]
        break
    reward = ""
    for op, cl in _iter_named_blocks(text, "completion_reward", f_open, f_close):
        reward = text[op:cl]
        break
    return FocusInfo(
        fid=fid,
        kind=kind,
        tree_id=tree_id,
        open_pos=f_open,
        close_pos=f_close,
        has_awd=_has_injectable_block(text, f_open, f_close, "ai_will_do"),
        is_root=not _has_direct_block(text, f_open, f_close, "prerequisite"),
        is_ignition=_contains_token(text, f_open, f_close, "start_civil_war")
            or fid in EXTRA_IGNITION_IDS,
        has_available=_has_direct_block(text, f_open, f_close, "available"),
        has_completion=_has_direct_block(text, f_open, f_close, "completion_reward"),
        exclusive=_exclusive_ids(text, f_open, f_close),
        prereqs=_prereq_ids(text, f_open, f_close),
        filters=_filter_set(text, f_open, f_close),
        avail_text=avail,
        reward_text=reward,
    )


def _union_find(ids: list[str], edges: list[tuple[str, str]]) -> dict[str, set[str]]:
    parent = {i: i for i in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    known = set(ids)
    for a, b in edges:
        if a in known and b in known:
            union(a, b)
    groups: dict[str, set[str]] = {}
    for i in ids:
        groups.setdefault(find(i), set()).add(i)
    return {m: g for g in groups.values() for m in g}


def _is_intervention(fid: str) -> bool:
    low = fid.lower()
    return any(m in low for m in INTERVENTION_MARK)


def _party_gated(avail: str) -> bool:
    return bool(re.search(
        r"(democratic|communism|fascism|neutrality)\s*>\s*0\.5", avail
    ))


def _governments(avail: str) -> set[str]:
    found = set(re.findall(r"has_government\s*=\s*(\w+)", avail))
    found.update(re.findall(r"has_government\((\w+)\)", avail))
    return found


def _extract_effect_tags(text, f_open, f_close, effect_name) -> list[str]:
    tags = []
    for op, cl in _iter_named_blocks_any_depth(text, effect_name, f_open, f_close):
        for key in ("target", "target_country", "country"):
            val = _read_direct_scalar(text, op, cl, key)
            if val and TAG_RE.match(val):
                tags.append(val)
                break
    return tags


def _extract_scalar_tag(text, f_open, f_close, key) -> list[str]:
    tags = []
    for op, cl in _iter_named_blocks(text, "completion_reward", f_open, f_close):
        val = _read_direct_scalar(text, op, cl, key)
        if val and TAG_RE.match(val):
            tags.append(val)
        for aop, acl in _iter_named_blocks_any_depth(text, key, op, cl):
            inner = text[aop:acl].strip()
            if TAG_RE.match(inner):
                tags.append(inner)
    return tags


def _cw_roots(by_id: dict[str, FocusInfo]) -> set[str]:
    roots = set()

    def ancestors(fid: str) -> set[str]:
        seen = set()
        stack = list(by_id[fid].prereqs)
        while stack:
            cur = stack.pop()
            if cur in seen or cur not in by_id:
                continue
            seen.add(cur)
            stack.extend(by_id[cur].prereqs)
        return seen

    for fid, info in by_id.items():
        if not info.is_ignition or _is_intervention(fid):
            continue
        path = ancestors(fid) | {fid}
        cands = []
        for anc in path:
            if anc == fid or anc not in by_id:
                continue
            sibs = by_id[anc].exclusive
            if sibs and any(s not in path for s in sibs):
                cands.append(anc)
        if cands:
            roots.add(min(cands, key=lambda x: len(ancestors(x))))
    return roots


def _auto_diplomacy_mods(info: FocusInfo, text: str) -> tuple[list[list[str]], list[str] | None]:
    war_tags = _extract_effect_tags(text, info.open_pos, info.close_pos, "create_wargoal")
    war_tags += _extract_effect_tags(text, info.open_pos, info.close_pos, "declare_war_on")
    coop_tags = _extract_effect_tags(text, info.open_pos, info.close_pos, "diplomatic_relation")
    # add_to_faction is often a scalar
    for op, cl in _iter_named_blocks(text, "completion_reward", info.open_pos, info.close_pos):
        val = _read_direct_scalar(text, op, cl, "add_to_faction")
        if val and TAG_RE.match(val):
            coop_tags.append(val)
    war_tags = list(dict.fromkeys(war_tags))
    coop_tags = list(dict.fromkeys(t for t in coop_tags if t not in war_tags))
    mods: list[list[str]] = []
    available: list[str] | None = None
    if war_tags:
        mods.append(["$ai_war_support_modifier()"])
        if len(war_tags) == 1:
            tag = war_tags[0]
            mods.append([f"$ai_antagonism_modifier(${tag})"])
            mods.append([f"$ai_rivalry_modifier(${tag})"])
            mods.append([f"$ai_betrayal_modifier_vs(${tag})"])
            if tag in ALIASES:
                available = [f"$can_get_wargoal_on(${tag})"]
            else:
                available = [f"${tag}->can_PREV_get_wargoal_on_THIS()"]
        elif len(war_tags) == 2:
            a, b = war_tags
            mods.append([
                f"antagonism = 1 - ($opinion_factor(${a}) + $opinion_factor(${b})) / 2",
                "factor(antagonism)",
                "is_sandbox_mode_on()",
            ])
            mods.append([f"$ai_rivalry_modifier_max(${a}, ${b})"])
            mods.append([
                "$ai_betrayal_modifier()",
                "or:",
                f"  ${a}->is_friend_of_PREV()",
                f"  ${b}->is_friend_of_PREV()",
            ])
            available = [
                f"${a}->can_PREV_get_wargoal_on_THIS()",
                f"${b}->can_PREV_get_wargoal_on_THIS()",
            ]
        elif 3 <= len(war_tags) <= 6:
            terms = " + ".join(f"$opinion_factor(${t})" for t in war_tags)
            n = len(war_tags)
            mods.append([
                f"antagonism = 1 - ({terms}) / {n}",
                "factor(antagonism)",
                "is_sandbox_mode_on()",
            ])
            riv = ["rivalry_vs = 0"]
            riv.extend(f"$rivalry_vs_into(${t})" for t in war_tags)
            riv.extend(["f = 1 + rivalry_vs / 50", "factor(f)", "is_sandbox_mode_on()"])
            mods.append(riv)
            betr = ["$ai_betrayal_modifier()", "or:"]
            betr.extend(f"  ${t}->is_friend_of_PREV()" for t in war_tags)
            mods.append(betr)
            # GDD: 3+ invitees/targets get no rival available gate
            available = None
    elif coop_tags:
        if len(coop_tags) == 1:
            tag = coop_tags[0]
            mods.append([f"$ai_cooperation_modifier(${tag})"])
            mods.append([
                "factor(0)",
                f"${tag} in rivals[]",
                "is_sandbox_mode_on()",
            ])
            available = [f"$not_rival_of_PREV(${tag})"]
        elif 2 <= len(coop_tags) <= 3:
            terms = " + ".join(f"$opinion_factor(${t})" for t in coop_tags)
            n = len(coop_tags)
            mods.append([
                f"cooperation = 1 + ({terms}) / {n}",
                "factor(cooperation)",
                "is_sandbox_mode_on()",
            ])
            if n == 2:
                a, b = coop_tags
                mods.append([
                    "factor(0)",
                    "or:",
                    f"  ${a} in rivals[]",
                    f"  ${b} in rivals[]",
                    "is_sandbox_mode_on()",
                ])
                available = [
                    f"$not_rival_of_PREV(${a})",
                    f"$not_rival_of_PREV(${b})",
                ]
    return mods, available


def _emit_mod(lines, indent, has_awd, entries: list[str]):
    inner = INDENT * (indent + 1)
    body = INDENT * (indent + 2)
    header = f"{inner}+modifier:" if has_awd else f"{inner}modifier:"
    lines.append(header)
    for entry in entries:
        if entry.startswith("  ") or entry.startswith("\t"):
            # already relatively indented from or:/and: bodies
            rel = entry.replace("\t", INDENT)
            lines.append(f"{body}{rel.lstrip() if not rel.startswith(INDENT) else rel[len(INDENT):] if False else rel}")
            # keep relative indent: entry is "or:" or "  $TAG->..."
        else:
            lines.append(f"{body}{entry}")


def _emit_mod_fixed(lines, indent, has_awd, entries: list[str]):
    inner = INDENT * (indent + 1)
    body_col = indent + 2
    lines.append(f"{inner}+modifier:" if has_awd else f"{inner}modifier:")
    for entry in entries:
        if not entry.strip() or _is_comment(entry):
            continue
        raw = entry.replace("\t", INDENT)
        stripped = raw.lstrip(" ")
        extra = (len(raw) - len(stripped)) // 2
        lines.append(f"{INDENT * (body_col + extra)}{_hsl_leaf(stripped) if extra == 0 else stripped}")


def build_include(text, vanilla: dict[str, VanillaExtras], stats: dict) -> str | None:
    focuses = collect_focuses(text)
    if not focuses:
        return None
    by_id = {f.fid: f for f in focuses}
    edges = []
    for f in focuses:
        for other in f.exclusive:
            edges.append((f.fid, other))
    groups = _union_find(list(by_id), edges)
    cw_roots = _cw_roots(by_id)

    def component(fid: str) -> set[str]:
        return groups.get(fid, {fid})

    def allow_crossroad(fid: str) -> int | None:
        members = component(fid)
        if len(members) < 2:
            return None
        infos = [by_id[m] for m in members if m in by_id]
        if any("FOCUS_FILTER_POLITICAL" in i.filters or "FOCUS_FILTER_POLITICAL_CHARACTER" in i.filters for i in infos):
            return None
        if any(_party_gated(i.avail_text) for i in infos):
            return None
        govs = [_governments(i.avail_text) for i in infos]
        nonempty = [g for g in govs if g]
        if len(nonempty) >= 2 and any(a != b for a in nonempty for b in nonempty):
            return None
        for i in infos:
            vx = vanilla.get(i.fid)
            if vx and (vx.has_crossroad or vx.has_party or vx.has_tyranny):
                return None
        return len(members)

    lines: list[str] = []

    def emit_one(info: FocusInfo, indent: int):
        vx = vanilla.get(info.fid)
        n_cross = allow_crossroad(info.fid)
        lines.append("")
        lines.append(f"{INDENT * indent}{info.kind}[id = {info.fid}]:")
        wd = indent + 1
        has_awd = info.has_awd
        lines.append(f"{INDENT * wd}{'ai_will_do' if has_awd else '+ai_will_do'}:")

        def add(entries: list[str]):
            _emit_mod_fixed(lines, wd, has_awd, entries)
            stats["mods"] += 1

        if not (vx and vx.has_sandbox_set):
            add(["$ai_sandbox_modifier()"])
        if info.is_root:
            add(["$root_modifier()"])
        if info.is_ignition:
            add(["$ai_civil_war_ignition_modifier()"])
            add(["factor(0)", "sandbox_civil_war_cap_reached()"])
            stats["ignition"] += 1
        if info.fid in cw_roots and not (vx and vx.has_cw_root):
            add(["$ai_civil_war_root_modifier()"])
            stats["cw_root"] += 1
        if vx:
            for mod in vx.extra_mods:
                add(mod)
                stats["vanilla_extra"] += 1
        if n_cross and not (vx and vx.has_crossroad):
            add([f"$crossroad_modifier({n_cross})"])
            stats["crossroad"] += 1
        if (
            "FOCUS_FILTER_INDUSTRY" in info.filters
            and "FOCUS_FILTER_POLITICAL" not in info.filters
            and "FOCUS_FILTER_POLITICAL_CHARACTER" not in info.filters
            and not (vx and vx.has_mic)
        ):
            add(["$ai_mic_modifier()"])
            stats["mic"] += 1
        low = info.fid.lower()
        if any(m in low for m in UNCONST_MARK) and not (vx and vx.has_tyranny):
            add(["$ai_high_tyranny_tilt()"])
            stats["tyranny"] += 1
        if not (vx and vx.has_honor):
            auto_mods, auto_avail = _auto_diplomacy_mods(info, text)
            for mod in auto_mods:
                add(mod)
                stats["honor"] += 1
        else:
            auto_avail = None

        avail_lines = None
        if vx and vx.available:
            avail_lines = vx.available
        elif auto_avail:
            avail_lines = auto_avail
        if any(m in low for m in PURGE_MARK):
            extra_gate = "is_liberal_leader(no)"
            joined = "\n".join(avail_lines or [])
            if extra_gate not in joined:
                if avail_lines is None:
                    avail_lines = [extra_gate]
                else:
                    avail_lines = list(avail_lines) + [extra_gate]
            stats["purge_gate"] += 1
        if avail_lines:
            key = "available" if info.has_available else "+available"
            lines.append(f"{INDENT * wd}{key}:")
            for entry in avail_lines:
                if not entry.strip() or _is_comment(entry):
                    continue
                raw = entry.replace("\t", INDENT)
                stripped = raw.lstrip(" ")
                extra = (len(raw) - len(stripped)) // 2
                leaf = _hsl_leaf(stripped) if extra == 0 else stripped
                lines.append(f"{INDENT * (wd + 1 + extra)}{leaf}")
            stats["available"] += 1
        extra_cw_logs: list[str] = []
        joined_comp = "\n".join(vx.completion) if vx and vx.completion else ""
        if info.is_ignition and "sandbox_log_cw_ignition" not in joined_comp:
            extra_cw_logs.append(f"$sandbox_log_cw_ignition({info.fid})")
        if info.fid in cw_roots and "sandbox_log_cw_root" not in joined_comp:
            extra_cw_logs.append(f"$sandbox_log_cw_root({info.fid})")
        if vx and vx.completion:
            key = "completion_reward" if info.has_completion else "+completion_reward"
            lines.append(f"{INDENT * wd}{key}:")
            for entry in vx.completion:
                if not entry.strip() or _is_comment(entry):
                    continue
                raw = entry.replace("\t", INDENT)
                stripped = raw.lstrip(" ")
                extra = (len(raw) - len(stripped)) // 2
                lines.append(f"{INDENT * (wd + 1 + extra)}{stripped}")
            for log in extra_cw_logs:
                lines.append(f"{INDENT * (wd + 1)}{log}")
            stats["completion"] += 1
        elif extra_cw_logs:
            lines.append(f"{INDENT * wd}+completion_reward:")
            for log in extra_cw_logs:
                lines.append(f"{INDENT * (wd + 1)}{log}")
            stats["completion"] += 1

    emitted = False
    trees: dict[str, list[FocusInfo]] = {}
    shared: list[FocusInfo] = []
    for info in focuses:
        if info.tree_id:
            trees.setdefault(info.tree_id, []).append(info)
        else:
            shared.append(info)
    for tree_id, items in trees.items():
        if lines:
            lines.append("")
        lines.append(f"focus_tree[id = {tree_id}]:")
        for info in items:
            emit_one(info, 1)
        emitted = True
    if shared:
        if lines:
            lines.append("")
        for info in shared:
            emit_one(info, 0)
        emitted = True
    if not emitted:
        return None
    return "\n".join(lines) + "\n"


def copy_country_helpers():
    copied = 0
    for tag in COUNTRY_TAGS:
        for rel in (
            f"common/on_actions/99_sandbox_{tag}_on_actions.hsl",
            f"common/scripted_effects/99_sandbox_{tag}_scripted_effects.hsl",
        ):
            src = VANILLA_MOD / rel
            dst = R56_MOD / rel
            if src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                copied += 1
    return copied


def main():
    vanilla = load_vanilla_extras()
    helpers = copy_country_helpers()
    print(f"Vanilla extras loaded for {len(vanilla)} focus ids; copied {helpers} country helper files")
    if not RT56_FOCUS.is_dir():
        raise SystemExit(f"Rt56 national_focus not found: {RT56_FOCUS}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    generated = 0
    skipped = 0
    errors = []
    stats = {
        "mods": 0, "ignition": 0, "cw_root": 0, "vanilla_extra": 0,
        "crossroad": 0, "mic": 0, "tyranny": 0, "honor": 0,
        "purge_gate": 0, "available": 0, "completion": 0,
    }

    for src_path in sorted(RT56_FOCUS.glob("*.txt")):
        text = src_path.read_text(encoding="utf-8-sig")
        try:
            include_text = build_include(text, vanilla, stats)
        except ValueError as exc:
            errors.append(f"{src_path.name}: {exc}")
            continue
        if include_text is None:
            skipped += 1
            continue
        dst = OUT_DIR / (src_path.stem + ".include")
        dst.write_text(include_text, encoding="utf-8")
        generated += 1
        print(f"  {src_path.name} -> {dst.name}")

    print("-" * 50)
    print(f"Generated: {generated}; skipped: {skipped}")
    print("Stats:", stats)
    if errors:
        print("Errors:")
        for err in errors:
            print(f"  {err}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
