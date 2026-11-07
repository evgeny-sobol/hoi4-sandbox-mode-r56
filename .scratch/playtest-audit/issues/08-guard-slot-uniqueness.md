# 08 - Guard rival slot uniqueness from the extract

Status: resolved
Type: feature
Blocked by: 06

## What to build

A repo guard that reads a session extract and fails when one country holds the
same rival in two slots, so the regression from issue 06 is visible without
anyone re-deriving slot state by hand.

## Problem

There is no guard over the rivals system at all. Six duplicate-slot writes in
eighteen months went unnoticed for exactly that reason: the census line carried
the evidence (`r0=FRA:52 r1=FRA:52`) and nobody was comparing the two fields.

Finding them meant reconstructing slot state from the event stream:

- replay `rivals_set other=<tag> slot=<n>` into a per-country three-slot model;
- treat `rivals_clear_*` as freeing the slot only when the tag matches;
- flag a `rivals_set` whose tag already occupies a different slot.

That reconstruction is the guard. It needs no engine run beyond the extract.

## What the guard should report

- the country, the tag and the two slots, for each duplicate write;
- a count of countries whose monthly `census` shows a repeated tag, as a second
  independent signal (the event stream can be missing a write that predates the
  extract, the census cannot).

Both signals should print their own header so a clean run reads as clean rather
than as "the guard did not run".

## Acceptance

- [x] `.scratch/scripts/check_rival_slot_uniqueness.py` exists and is registered
      in `SHARED_MISC` so it syncs into both mods.
- [x] It takes an extract path argument and defaults to the standard logs
      location.
- [x] It reports duplicate writes from the event stream and repeated tags from
      `census`, with counts.
- [x] Run against the current extract it reports the six known cases, so it is
      not vacuous.
- [x] Run against a synthesised clean extract it reports zero.
- [x] Exit code is non-zero when anything is found.

## Out of scope

- Fixing the duplicates; that is issue 06.
- Guards over honor, tyranny or civil wars. Only the rivals slot invariant.

## Verification

- Run the guard against `logs/sandbox_extract.txt` from the 1936-1937 session and
  confirm it names HUN, SAU, COG and GXC.
- Hand-edit a copy of the extract to remove the duplicates and confirm zero.
- `python core/tools/sync_core.py --check` reports no drift for the new file.

## Implementation (2026-11-06)

`.scratch/scripts/check_rival_slot_uniqueness.py`, registered in `SHARED_MISC` so
it syncs into both mods. Two independent signals, each covering what the other
cannot:

- **Event stream** - replays `rivals_set` into a per-country three-slot model and
  flags a write whose tag already occupies another slot. A clear frees a slot
  only when it names the tag sitting there; a mismatch means the reconstruction
  is behind, not that the guard should invent a failure. This covers all 131
  countries that ever touch a slot in the sample extract.
- **`census`** - flags a row whose `rN=` fields repeat a tag. This covers only
  the nine major-country rows the trigger allows, but it observes state directly
  instead of reconstructing it, so it cannot drift.

That split is why both exist: the census caught HUN holding FRA twice for
seventeen months, and the event stream caught SAU, COG and GXC, which the census
never prints.

### Read the exit code correctly

This guard is a **session analysis**, not a repo-state check. Other guards exit 0
on a healthy checkout; this one exits 1 whenever the extract it reads contains a
duplicate. Running it against the current extract therefore exits 1 by design -
that is the finding, not a broken repo. Only after a session that includes the
issue-06 fix should it exit 0.

### Evidence

- Current extract: 528 slot events with 6 duplicate writes naming HUN, SAU, COG
  (twice) and GXC (twice), plus 153 census rows with 17 repeated-tag rows (all
  HUN/FRA). Exit 1.
- A synthesised clean extract (three distinct tags, a reroll that clears before
  rewriting, an empty slot printed as `0`): 5 events, 0 duplicates, 3 census rows,
  0 repeats. Exit 0.
- Each signal was tested alone: a duplicate write with a clean census is caught
  by the event scan, and a repeated census tag with a clean event stream is caught
  by the census scan. Neither is dead weight.
- Registered in `SHARED_MISC`; `sync_core.py --check` reports drift only on
  `AGENTS.md`, as before. The other four guards still pass in both mods.
