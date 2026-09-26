#!/usr/bin/env python3
"""Bring the r56 ticket headers onto the documented tracker format.

`docs/agents/issue-tracker.md` says triage state is recorded as a plain
`Status:` line near the top of each issue file. The r56 tickets instead carry
bold `**Status:**` / `**Blocked by:**` fields buried in the body and have no
`Type:`. This rewrites the header to the flat form the other repo already uses:

    # NN: title

    Status: resolved
    Type: task
    Blocked by: none

    **What to build:** ...

Only the bold `**Blocked by:**` / `**Status:**` lines are removed from the body;
everything else is left byte-for-byte. Every blocker named by these tickets is
itself resolved, so `Blocked by` becomes `none` for all of them. Idempotent.

Usage:
  python normalize_ticket_headers.py <issues-dir> [--status resolved] [--type task]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BOLD_STATUS_RE = re.compile(r"^\s*\*\*Status:\*\*.*$")
BOLD_BLOCKED_RE = re.compile(r"^\s*\*\*Blocked by:\*\*.*$")
FLAT_STATUS_RE = re.compile(r"^Status:\s*\S+")


def normalize(path: Path, status: str, default_type: str) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if any(FLAT_STATUS_RE.match(l) for l in lines[:12]):
        print(f"  {path.name}: already normalized")
        return False
    if not any(BOLD_STATUS_RE.match(l) for l in lines):
        print(f"  {path.name}: no **Status:** line, skipped")
        return False

    body = [l for l in lines if not (BOLD_STATUS_RE.match(l) or BOLD_BLOCKED_RE.match(l))]
    # drop a run of blank lines left where the fields were
    cleaned: list[str] = []
    for l in body:
        if not l.strip() and cleaned and not cleaned[-1].strip():
            continue
        cleaned.append(l)

    title = cleaned[0].rstrip()
    rest = cleaned[1:]
    while rest and not rest[0].strip():
        rest.pop(0)

    out = [
        title,
        "",
        f"Status: {status}",
        f"Type: {default_type}",
        "Blocked by: none",
        "",
        *rest,
    ]
    path.write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8")
    print(f"  {path.name}: Status: {status}, Type: {default_type}")
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("issues_dir")
    ap.add_argument("--status", default="resolved")
    ap.add_argument("--type", dest="ticket_type", default="task")
    args = ap.parse_args()

    d = Path(args.issues_dir)
    if not d.is_dir():
        raise SystemExit(f"not a directory: {d}")
    changed = sum(normalize(p, args.status, args.ticket_type) for p in sorted(d.glob("*.md")))
    print(f"\n{changed} file(s) rewritten")


if __name__ == "__main__":
    main()
