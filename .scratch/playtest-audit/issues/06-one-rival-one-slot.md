# 06 - One country must never occupy two rival slots

Status: resolved
Type: bug
Blocked by: none

## What to build

A country holds at most one of its three rival slots per rival. Every write path
enforces uniqueness, so the three slots always mean three different countries.
The `census` line reports three distinct tags, and an empty slot reads as absent
rather than as a tag with zero strength.

## Problem

Found in the 1936-1941 playtest audit (session 1936.01-1937.06). Reconstructing
slot state from `rivals_set` and `rivals_clear_*` events gives six cases in
eighteen months across five countries:

```
HUN  FRA -> slot 1, already held slot 0
SAU  ENG -> slot 2, already held slot 0
COG  FRA -> slot 0, already held slot 2   (twice)
GXC  FRA -> slot 0, already held slot 1   (twice)
```

It survives in the monthly census. HUN held FRA twice for seventeen consecutive
months:

```
1 February 1936 HUN census ... r0=FRA:52 r1=FRA:52 r2=LAT:51 ...
1 June     1937 HUN census ... r0=FRA:52 r1=FRA:52 r2=LAT:51 ...
```

One rival counted twice means one slot is dead and the band arithmetic reads the
same country from two places.

## Three write paths, all missing the same guard

1. **The scorers** (`major_rivals_scorer`, `minor_rivals_scorer`). Among the
   `factor(0)` gates there is the initiator (`tag(FROM)`), `former_rivals[]`,
   faction, subject and overlord - but no "this tag already holds another slot".
   The membership test for a foreign array already exists in this repo
   (`THIS in FROM.former_rivals[]`, which compiles to
   `is_in_array = { FROM.former_rivals = THIS }`), so the form is available.
2. **`select_minor_rival()`** has half a guard: the slot-2 branch checks
   `find != rivals[1]`, while the slot-1 branch checks nothing, so a tag already
   in slot 2 can be written into slot 1.
3. **`set_rival()`** writes `&rivals[rival_slot] = rival_tag` with no occupancy
   check at all. This is the backstop that must hold for every caller, including
   the ones that never go through a scorer.

Fix the scorer so a duplicate is never chosen, and `set_rival` so a duplicate is
never written. The second is not redundant: the scenario director seeds rivals
directly through `sandbox_seed_rival` and `become_event_rival`, which pick a slot
from their own logic.

## Cosmetic part, same ticket

`census` prints a tag for an empty slot: FRA read `r0=FRA:0` in four monthly
rows while slot 0 held nobody. `rivals^0.GetTag` resolves even when the strength is
zero, so the field reads as "a rival with no strength" instead of "no rival".
The line should make an empty slot distinguishable from a weak one.

## Acceptance

The behavioural lines are source-verified; a session is needed to confirm.

- [x] No `rivals_set` writes a tag into a slot it already occupies. The 1941
      run has 656 slot events and zero duplicate writes.
- [x] A `census` line never shows the same tag in two slots. 526 rows, none with
      a repeated tag (was 17).
- [ ] An empty slot is distinguishable from a rival with zero strength in
      `census`. NOT DONE - see the regression note at the bottom.
- [x] Slots stay unique after a scenario seed, after `become_event_rival`, and
      after a ruler change re-rolls slot 0.
- [x] No new `error.log` lines attributable to rivals or the scorers.

## Scope note

Two repos:

- `99_sandbox_scorer.hsl` is per-mod (the opinion scale differs between them), so
  the scorer change lands in both mods separately.
- `99_sandbox_scripted_effects.hsl` is shared core content: edit it in
  `C:\Users\evgeny\Repos\HoI4\sandbox-mod-core`, then sync outward.

## Verification

- Recompile both mods.
- Replay the log reconstruction against a new session: zero duplicate slots.
- Confirm a census row shows `r0=` empty when slot 0 is unset.

## Implementation (2026-11-06)

All four edits applied; both mods compile.

**`set_rival()` - the backstop (shared core).** Before writing, it scans the
other two slots for `rival_tag` and skips the whole write (including the log line
and the opinion modifier) when the tag is already held. This covers every path,
including `sandbox_seed_rival` and `become_event_rival`, which pick a slot from
their own logic and never reach a scorer. It also means a rejected write does not
leave a stray `rivals_set` line claiming a change that did not happen.

**`select_minor_rival()` (shared core).** Both branches now test the other two
slots. The slot-2 branch previously checked only `rivals[1]`; the slot-1 branch
checked nothing, so a tag held in slot 2 could be written into slot 1.

**Both rival scorers (per-mod).** One `factor(0)` gate added:
`THIS in FROM.rivals[]`, which compiles to
`is_in_array = { FROM.rivals = THIS }` - the same form the file already uses for
`former_rivals[]`. This is not redundant with the write guard: a scorer that
keeps proposing an already-held tag burns the roll and leaves the slot empty for
the month, so the tag is taken out of the candidates instead.

**`census` (shared core).** Each slot is rendered into its own temp string and an
empty slot prints `0` instead of `TAG:0`. Format is otherwise unchanged and the
line stays one line, so existing parsing keeps working. `0` was chosen over
omitting the field because a fixed field set is easier to read and to grep.

### Verification

- Both mods compile. Compiled output carries the three-slot scan in `set_rival`,
  both occupancy tests in `select_minor_rival`, the `is_in_array` gate in both
  scorers, and the three `r0_text`/`r1_text`/`r2_text` temps in `census`.
- All four original duplicate cases were replayed against the new logic: each one
  is blocked by the write guard and scored to zero by the scorer.
- `check_economic_posture`, `check_repick_gate`, `check_peak_timeout_detail` and
  `check_scorer_self_exclusion` all report 0 in both mods.
- `sync_core.py --check` reports drift only on `AGENTS.md` (the per-repo lore
  line), as before.
- **Not yet done: a session.** Zero duplicates in a fresh extract, and a `census`
  row showing `r0=0` for an empty slot, are the remaining checks.

### Traps hit

- `set_temp_variable = { x = 0 }` inside HSL source does not parse: the block
  form is the *output*, not the input. Use plain `x = 0`.
- Array indexing with `^` is not available in a scorer condition context, so the
  per-slot exclusion is one membership test (`THIS in FROM.rivals[]`) rather than
  three indexed comparisons.

## Session result (2026-11-07, 1936.01-1941.01)

`check_rival_slot_uniqueness.py` over the new extract:

```
event stream: 656 slot events, 0 duplicate write(s)
census: 526 row(s), 0 with a repeated tag
problems: 0
```

Against the previous session the same guard reported 6 duplicate writes and 17
repeated census rows. Both write paths and the scorer gate hold.

### Regression found and reverted: the census cosmetics

The empty-slot cosmetics was first implemented by caching each slot's rendered
text in a temp (`r0_text`) and logging `[?r0_text]`. That does not work: the game
substitutes the temporary's **value**, not the text it holds, so every census row
printed floats - `r0=10780.22997 r1=10780.22997 r2=10780.22997` - on 524 of 526
rows. The rival data in those rows was unreadable for the whole run.

It compiled clean and every guard passed, because the guard counted tags and a
float carries none, so "no repeated tag" was vacuously true. The cosmetics is
reverted to the working inline form and the comment records why the clever form
must not come back. The empty-slot criterion above stays unchecked until a form
is found that the game actually substitutes.

Lesson for the guard: a census signal that parses zero tags must fail, not pass.

## Second session result (2026-11-07, 1936.01-1940.03)

Independent confirmation on a run with a different arc and a different player
country:

```
event stream: 617 slot events, 0 duplicate write(s)
census: 450 row(s), 0 with a repeated tag
problems: 0
```

This run also confirms the census field itself is healthy again after the
reverted cosmetics: rows parse as `r0=USA:54 r1=CZE:68 r2=POL:66`.

The empty-slot criterion stays unchecked, and this run shows precisely why it
matters: 25 fields print `TAG:0` - a rival shown with zero strength rather than
an empty slot. Reverting the broken cosmetics restored the old shape, so the
ambiguity is still there; a working form has not been found.
