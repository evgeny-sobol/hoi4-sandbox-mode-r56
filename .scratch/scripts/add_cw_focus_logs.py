#!/usr/bin/env python3
"""Add cw_ignition / cw_root completion logs to existing focus includes.

Idempotent. generate_focus_includes.py emits the same tokens on a full regen.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

OUT_DIR = Path(
    os.path.expandvars(r"%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56\common\national_focus")
)

FOCUS_HDR = re.compile(
    r"^([ \t]*)(focus|shared_focus|joint_focus)\[id = ([^\]]+)\]:\s*$"
)
COMP_HDR = re.compile(r"^([ \t]*)(\+?completion_reward):\s*$")


def _indent_width(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _section_end(lines: list[str], start: int, end: int, col: int) -> int:
    j = start + 1
    while j < end:
        raw = lines[j]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            j += 1
            continue
        if _indent_width(raw) <= col:
            break
        j += 1
    return j


def _patch_block(lines: list[str], start: int, end: int, fid: str) -> tuple[list[str], int]:
    body = "".join(lines[start:end])
    logs: list[str] = []
    if "$ai_civil_war_ignition_modifier" in body and "sandbox_log_cw_ignition" not in body:
        logs.append(f"$sandbox_log_cw_ignition({fid})")
    if "$ai_civil_war_root_modifier" in body and "sandbox_log_cw_root" not in body:
        logs.append(f"$sandbox_log_cw_root({fid})")
    if not logs:
        return lines, 0

    hdr_indent = _indent_width(lines[start])
    child_indent = hdr_indent + 2
    log_indent = child_indent + 2

    comp_idx = None
    for i in range(start + 1, end):
        m = COMP_HDR.match(lines[i].rstrip("\n"))
        if m:
            comp_idx = i
            break

    insert: list[str] = [f"{' ' * log_indent}{log}\n" for log in logs]
    if comp_idx is not None:
        col = _indent_width(lines[comp_idx])
        j = _section_end(lines, comp_idx, end, col)
        lines[j:j] = insert
        return lines, len(logs)

    insert_at = end
    while insert_at > start + 1 and not lines[insert_at - 1].strip():
        insert_at -= 1
    block = [f"{' ' * child_indent}+completion_reward:\n", *insert]
    lines[insert_at:insert_at] = block
    return lines, len(logs)


def patch_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    headers: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = FOCUS_HDR.match(line.rstrip("\n"))
        if m:
            headers.append((i, m.group(3)))
    added = 0
    for n in range(len(headers) - 1, -1, -1):
        start, fid = headers[n]
        end = headers[n + 1][0] if n + 1 < len(headers) else len(lines)
        lines, n_add = _patch_block(lines, start, end, fid)
        added += n_add
    if added:
        path.write_text("".join(lines), encoding="utf-8", newline="\n")
    return added


def main() -> None:
    total_files = 0
    total_logs = 0
    for path in sorted(OUT_DIR.glob("*.include")):
        n = patch_file(path)
        if n:
            total_files += 1
            total_logs += n
            print(f"{path.name}: +{n}")
    print(f"files={total_files} logs={total_logs}")


if __name__ == "__main__":
    main()
