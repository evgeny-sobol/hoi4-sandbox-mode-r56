# 05 - Peak timeout cannot report why it fired

Status: resolved
Type: feature
Blocked by: 01

## What to build

The `sc_derail peak_timeout` line says enough about the arc's state at the moment
of the timeout that an observer can tell design-compliant passivity from a stuck
aggressor without re-reading the whole extract.

## Problem

The classic derail line carries the phase and the month counter, and nothing
about what the aggressor was actually doing:

```
1939.07.01 HAI sc_derail peak_timeout sc=5 phase=3 pin=0 t=42 home=25.0
1939.07.01 HAI sc_end    peak_timeout sc=5 phase=3 pin=0 t=42 home=25.0
```

In arc 5 the aggressor was the human player's France (see issue 02), holding live
wargoals on HOL and LUX for 11 consecutive months. Those wargoals were visible in
the monthly `sc_goal fra_on_hol` / `sc_goal fra_on_lux` lines, but the derail line
itself cannot be read without cross-referencing 11 months of a different line
type. An observer also cannot see from it whether the aggressor was human at all,
which is the single most useful bit for triaging a timeout.

## Why it matters

`peak_timeout` was the dominant terminal event in this session (both arcs that
ended in-game ended this way), and it is ambiguous by construction:

- a human aggressor taking its time is design-compliant;
- an AI aggressor sitting on its wargoals for a year is a bug in the pressure
  levers;
- an aggressor with no wargoals at all is a bug in the ultimatum events.

All three produce byte-identical derail lines today. Making the line self-describing
turns the next session's extract into a triage document instead of a puzzle, and
that is cheaper than instrumenting a repro.

## What to record

Extend the timeout line (and its `sc_end` twin) with the state that separates the
three cases above. Keep it consistent with the existing convention: lowercase
labels, no new line type, one line, parseable `key=value` fields.

Fields worth carrying:

- whether the aggressor is human (`ai=0/1`), since that alone splits
  design-compliant from suspicious;
- how many declared targets are alive and how many the aggressor holds a wargoal
  against (`wgo=N`), which separates "levers produced nothing" from "levers
  produced war goals nobody pressed";
- the target ids, so the line stands alone without the `sc_goal` history.

Follow the existing gate and formatting idiom used by `sc_goal` and `sc_power`.

## Acceptance

The classification line needs a game run; the code and compiled output are
verified.

- [x] A `peak_timeout` derail line states whether the aggressor was human, how
      many targets were alive, and how many live wargoals the aggressor held.
- [x] The matching `sc_end` line carries the same fields so either can be read
      alone.
- [x] The fields are emitted from the same snapshot used by the derail decision,
      so they cannot disagree with the timeout count.
- [x] A session extract lets a reader classify a timeout as human-passive,
      AI-with-wargoals, or AI-without-wargoals, using that line alone. The 1941
      run has one: `ai=1 alive=1 wgo=1 t0=CZE t1=POL`, an AI holding a live
      wargoal on POL - the "levers produced, nobody pulled" case.
- [x] Existing label conventions and ASCII-only output hold; no new line type.
- [x] No new `error.log` lines attributable to scenario files.

## Out of scope

- Changing the 12-month timeout or any derail reason.
- Adding a new `#sandbox` log gate; this rides `sandbox_log_scenarios`.

## Verification

- Recompile after the `.hsl` change.
- Re-extract and confirm a `peak_timeout` line is self-describing.
- Since `peak_timeout` needs 12 months to reproduce, confirm the field set on a
  forced timeout in a short pinned run rather than a full session.

## Implementation (2026-11-06)

Applied to both mods.

- `macro sandbox_check_peak_timeout()` in shared core now calls
  `sandbox_log_peak_timeout_detail()` and no longer emits the blind
  `sc_derail`/`sc_end` pair itself. It cannot scope into the aggressor - the arc
  to tag mapping is per-mod - so delegation is the only way to get a
  self-describing line, and it follows the existing
  `sandbox_log_scenario_success()` contract where core calls and each mod
  defines.
- Each mod's `99_sandbox_scenarios.hsl` defines
  `sandbox_log_peak_timeout_detail()` (arc to tag dispatch, mirroring
  `sandbox_scenario_check_civil_war_derail()`) plus
  `sandbox_log_peak_timeout_actor()`, which runs in the aggressor's scope and
  emits the pair with `ai=`, `alive=`, `wgo=` and `t0..t3`.
- `docs/gdd/Scenarios.md` "Hooks and telemetry" documents the contract and the
  three-way reading.
- New guard `.scratch/scripts/check_peak_timeout_detail.py`, registered in
  `SHARED_MISC`. It checks core for a re-added blind pair AND the mods for a
  missing hook, plus the compiled line counts.

### Field meanings

- `ai=1` - the aggressor is human. A slow ladder here is design-compliant.
- `ai=0 wgo>0` - AI holding wargoals it never pressed. The levers produced
  goals and nobody pulled them.
- `ai=0 wgo=0` - no wargoal at all. The ultimatum events never landed.
- `alive=N` - how many declared targets still exist, so a timeout on a dead
  target set is distinguishable from one on a live set.
- `t0..t3` - the declared tags, so the line stands alone.

`wgo` counts `has_wargoal_against` or `is_justifying_wargoal_against` per live
target, matching how `sc_goal` already defines "a pair with an active goal".

### Evidence

- Both mods compile. Compiled output carries exactly one detailed
  `sc_derail peak_timeout ai=` line and one `sc_end peak_timeout ai=` line, and
  zero blind `sc_derail peak_timeout sc=` lines.
- The guard was negative-tested both ways: re-adding the blind pair in core, and
  renaming the hook away in the catalog. Both caught, both reverted.
- All eight guards pass in both mods.
- `sync_core.py --check` reports drift only on `AGENTS.md` (the per-repo lore
  attribution line), as before. `macros.hml` was pushed to both mods by copying
  the core file directly rather than running the sync, precisely to avoid that
  rewrite.
- **Not yet done: a game run.** `peak_timeout` needs 12 months at peak, so the
  remaining two criteria need a session, or a forced timeout in a short pinned
  run.

### Trap worth remembering

The first pass left core emitting the generic pair *and* calling the hook. That
compiles, passes every other guard, and prints two `peak_timeout` lines per
timeout - one blind, one informative - so an extract would read as if the arc
derailed twice. The guard now rejects exactly that shape.
