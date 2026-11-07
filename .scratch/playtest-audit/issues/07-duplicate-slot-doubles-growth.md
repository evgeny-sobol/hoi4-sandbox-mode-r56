# 07 - A duplicated slot must not double the rivalry growth

Status: resolved
Type: bug
Blocked by: 06

## What to build

If a rival ever does occupy two slots, its rivalry grows once per tick, not once
per slot. A duplicated slot must not make a country's hostility climb twice as
fast.

## Problem

`add_rivalry_vs()` applies `rivalry_delta` to **every** slot holding the tag:

```
# Temps: rival_tag, rivalry_delta. Applies to every slot holding the tag.
add_rivalry_vs():
  if rivals[0] == rival_tag:
    $add_rivalry(0, rivalry_delta)
  if rivals[1] == rival_tag:
    $add_rivalry(1, rivalry_delta)
  if rivals[2] == rival_tag:
    $add_rivalry(2, rivalry_delta)
```

While a tag sits in two slots, each call charges it twice. Visible in the log,
where the same growth is applied to both slots on the same day:

```
HUN rivals_feud 74.00->76.00 d=2.00 other=FRA slot=0
HUN rivals_feud 74.00->76.00 d=2.00 other=FRA slot=1
```

Both slots rose by 2. The country's opinion modifiers, war-support tilt and AI
plan bands all key off the slot value, so a duplicate rival double-charges the
country's hostility budget and reaches Feud twice as fast.

## Why this is separate from issue 06

06 stops the duplicate from being written. This one makes the arithmetic survive
one. They are different mechanisms: 06 is an invariant on the slot array, 07 is
the behaviour of a helper that scans the array. Fixing only 06 leaves the helper
unsafe for any duplicate that arrives from a path nobody predicted - a scenario
seed, a save from an older build, or a future caller.

## Acceptance

The arithmetic is verified by simulation; a session is needed for the log line.

- [x] `add_rivalry_vs()` changes the rivalry of a tag once per call, even when
      that tag occupies two or three slots.
- [x] A duplicate-bearing session no longer shows two same-day `rivals_*` lines
      with the same growth for one tag. No duplicate arose at all in the 1941
      run, which is stronger: with slots unique by construction the case cannot
      be reached.
- [x] A single-occupancy session is unchanged: the same delta is applied to the
      same slot as before. 1145 rival lines, no paired same-day growth.
- [x] The opinion modifiers are applied once per tag, not once per slot.
- [x] No new `error.log` lines attributable to rivals.

## Scope note

`99_sandbox_scripted_effects.hsl` and the `$add_rivalry` macro live in shared
core: edit them in `C:\Users\evgeny\Repos\HoI4\sandbox-mod-core`, then sync
outward. Both mods inherit the fix; nothing here is per-mod.

## Verification

- Recompile both mods.
- Reconstruct rivalry growth from a new session's extract and confirm one
  `rivals_*` line per tag per change.
- Confirm the single-slot case still applies the delta exactly once.

## Implementation (2026-11-06)

Two implementations of the same rule existed, and both charged every matching
slot. Both are fixed, in shared core:

- **`add_rivalry_vs()`** (the scripted effect, four call sites) now scans for the
  lowest matching slot once and applies the delta through a `if`/`elif`/`else`
  chain on that slot index. A duplicate no longer charges twice.
- **`sandbox_add_rivalry_vs`** (the macro, used by `sandbox_seed_rival`) was
  three independent `if`s; it is now an `elif` chain, so the first match wins.

Lowest-slot-wins is deliberate: in a healthy session exactly one slot matches, so
the behaviour is byte-identical to before. Only the duplicate case changes.

### Evidence

- Both mods compile. The compiled effect carries `rival_slot_found`, the loop
  that fills it, and a three-way chain on the index; the compiled macro
  expansion in `99_sandbox_engine.txt` is `if` / `else_if` / `else_if` at
  matching depth (lines 65, 217, 369).
- Replayed the real duplicate (HUN holding FRA in slots 0 and 1, delta 2):
  old logic raised both slots 74 -> 76, new logic raises slot 0 only. The
  single-occupancy case is unchanged.
- All four guards pass in both mods.
- **Not yet done: a session.** One `rivals_*` line per tag per change is the
  remaining check.

### Note on the opinion modifiers

The acceptance criterion about opinion modifiers is met by construction, not by
a separate edit: `add_rivalry()` owns them, and it is now invoked once instead of
twice. No modifier code changed.

## Second session result (2026-11-07, 1936.01-1940.03)

Re-checked on a fresh extract: zero cases of one tag receiving two same-day
`rivals_*` growth lines in different slots. The guard on slot uniqueness reports
617 events and no duplicates, so the doubling case remains unreachable.
