# 02 - The pick can hand the arc to the human's own country

Status: resolved
Type: bug
Blocked by: none

## What to build

The director never makes the human player's country the aggressor of the drawn
arc. If the roll would land there, that arc is not eligible for this session, and
the human-aggressor peak arm is removed from the generated gate.

## Decision (variant a, accepted 2026-11-04)

Exclude the human's country from the pool, at both the initial pick and the
repick. The `is_ai(no)` peak arm becomes unreachable and is removed from the
builder. Recorded in `docs/adr/0009-human-aggressor-is-never-drawn.md`.

Rejected in the same round: (b) treat a human aggressor as a supported mode and
build a real pressure lever on a human, (c) exclude only when the human is not
also a target. (b) needs a lever the director does not have and no spec asks for;
(c) leaves the observed failure standable.

## Problem

Arc 5 (`napoleonic_france`, aggressor FRA) was drawn in the 1936-1941 Rt56
session while the human was playing France:

```
1936.01.01 HAI sc_pick napoleonic_france sc=5 phase=0 pin=0
1936.01.01 HAI sc_variant a          sc=5 phase=0 pin=0
```

`pin=0`, so this was the random roll, not a forced pin. The whole ladder then
depended on the human declaring: crises at 1937.03, peak at 1938.07, and the
12-month `peak_timeout` at 1939.07 with FRA holding live wargoals on HOL and LUX
that it never pressed. An entire arc's worth of session time produced no war.

Selection eligibility is `country_exists` only, for all six arcs:

```
gen_napoleonic_france_scenario_eligible():
  if country_exists(FRA):
    eligible[].add(5)
```

`country_exists` is true for a human-controlled country, so the human's own
nation enters the pool at equal weight with the five AI majors. The eligibility
block inside `sandbox_scenario_maybe_repick()` has the identical shape.

## Why it matters

`docs/gdd/Scenarios.md` design goal 2 says the director pushes AI, not the human:
"the player can join, meddle, or sit it out". An arc whose aggressor is the
player inverts that: the director stops driving anything and waits on the player
to press the wargoals it issued.

The generated peak gate also carries a human-aggressor arm for all six arcs
(`render_peak_gate()` in `core/tools/build_scenario_catalog.py`, the emitted
`elif <aggr>->is_ai(no):` at the peak rung; 13 such lines in the Rt56 generated
file):

```
elif GER->is_ai(no):
  global.&sandbox_scenario_phase = 2
  $sandbox_log_sc(sc_phase, peak)
  sandbox_fire_nazi_germany_peak()
```

That arm exists specifically to advance a human aggressor on schedule, which is
the untestable half-support the decision above closes. Removing it is part of
this ticket, not a follow-up: leaving it in place documents a path no session can
reach.

## Acceptance

Every behavioural line needs a game run; the code and artifacts are verified.

- [x] A session with the human on FRA never draws arc 5, and the same holds for
      every other arc whose aggressor the human controls. The 1936-1940 session
      was played as FRA: two arcs were drawn in fifty months, GER and ITA, and
      arc 5 (whose aggressor is FRA) never came up.
- [x] The repick pool (`sandbox_scenario_maybe_repick()`) applies the same rule
      as the initial pick; the human's country is excluded in both. All seven
      repick arms carry `is_ai(yes)`, and the 1938 repick went to ITA while FRA
      was the human.
- [ ] An all-human-majors start (no eligible arc) sets `sandbox_scenario = 0` and
      logs it rather than picking anyway. Not exercised: a country cannot hold
      all six aggressors at once, so this needs a contrived setup.
- [x] `render_peak_gate()` no longer emits an `is_ai(no)` arm; the generated
      `99_sandbox_scenarios_gen.*` carries none in either mod.
- [x] The `render_peak_gate()` docstring no longer describes human aggressors
      "proceeding on schedule", and `docs/gdd/Scenarios.md` "Peak" no longer
      lists the human arm among the three. The remaining two arms are the
      completed tail and the `peak_at_month + 12` fallback.
- [x] `build_scenario_catalog.py --check` passes in both mods.
- [x] No new `error.log` lines attributable to scenario files. Zero `99_sandbox_scenarios` lines in 1433 error lines across the 1936-1940 run.

## Scope note

Two different repos are involved:

- The eligibility predicates live in the per-mod `99_sandbox_scenarios.hsl` and
  the generated `99_sandbox_scenarios_gen.hsl`, so the filter lands in both
  `_sandbox` and `_sandbox-r56`.
- `render_peak_gate()` lives in `core/tools/build_scenario_catalog.py`, which is
  shared core: edit it in `C:\Users\evgeny\Repos\HoI4\sandbox-mod-core`, then sync
  outward (sync-core-first rule). Do not edit the synced copy under `core/`.

## Out of scope

- Whether a human can be a declared *target* of an AI aggressor. That is the
  intended pressure direction and stays.

## Verification

- Recompile after the `.hsl` change (compile-after-hsl rule, both mods).
- Run a session as France: `sc_pick` must name a different arc, and FRA must not
  appear as the drawn aggressor.
- `grep -c "is_ai(no)"` over both generated `99_sandbox_scenarios_gen.hsl` files
  must be 0 for the peak gate.
- Re-run `build_scenario_catalog.py --check` in both mods.

## Implementation (2026-11-06)

Applied to both mods; two repos are in scope.

- `render_pick()` in `core/tools/build_scenario_catalog.py` now emits
  `if country_exists(<aggr>) and <aggr>->is_ai(yes):`, so the generated
  `gen_<arc>_scenario_eligible()` carries the filter for all seven arcs.
- `render_peak_gate()` in the same file loses its `elif <aggr>->is_ai(no):` arm,
  and its docstring loses the sentence about human aggressors proceeding on
  schedule. Two arms remain: the completed path tail and `peak_at_month + 12`.
- `sandbox_scenario_maybe_repick()` in each mod's `99_sandbox_scenarios.hsl` is
  hand-written, so its seven arms were edited directly to the same predicate.
- `docs/gdd/Scenarios.md` in both mods: "Selection" states that a human
  aggressor is never drawn (ADR-0009) and names the predicate; "Peak gating"
  drops the human arm from three to two and says why.
- `check_repick_gate.py` grew a human-aggressor audit: the generated
  `eligible()` functions carry the filter, the hand-written repick arms carry it,
  and no generated `*_scenario_tick()` carries an `is_ai(no)` arm.

Evidence, all source-side:

- `build_scenario_catalog.py` run from the authoritative core repo rebuilt both
  mods (7 specs each); `--check` then reports `7 spec(s), artifacts in sync` for
  both.
- Compiled output carries `is_ai = yes` six times and `is_ai = no` zero times in
  each mod's `99_sandbox_scenarios_gen.txt`. Both mods compile clean.
- `check_repick_gate.py`, `check_pick_gate.py`, `check_derail_arms.py` and
  `check_if_else.py` report 0 problems in both mods.
- The new audit was negative-tested three ways, each caught: stripping `is_ai`
  from a generated eligibility line, restoring an `is_ai(no)` peak arm, and
  stripping `is_ai` from a hand-written repick arm. All three were reverted and
  the guard is clean again.
- Found in passing: `check_pick_gate.py` is vacuous on the new shape. It reads
  only the hand-written catalog, where `eligible[].add` no longer appears, so it
  `continue`s through every arc. Confirmed by breaking a generated eligibility
  line and watching it still report 0. Left alone because the generated file is
  git-ignored; the new audit covers the invariant instead.
- **Not yet done: a game run.** The three behavioural criteria need a session
  with the human on a major's tag.

## Side effect to know about

`build_scenario_catalog.py` refuses to build when an aggressor's focus graph is
older than its specs. In `_sandbox` every spec was 10-30 ms newer than its graph
from a single checkout, so the guard fired on sub-second ordering rather than on
real staleness (both sides are git-clean). The seven graph files were `os.utime`d
forward, content untouched, to restore the intended "graph exported before spec
authored" ordering. If a future checkout reproduces this, do the same - never
edit the specs to be older.

## Session attempt (2026-11-07, 1936.01-1941.01)

Not exercised: the criteria this ticket gates did not come up in the run.

The run was `-hands_off`, so the human country was Haiti. The two arcs drawn had
GER and SOV as aggressors, so the "human is the aggressor" case never arose. The
filter is in the built code and the two drawn arcs are both AI, which is
consistent with the fix but does not prove it.

## Session result (2026-11-07, played as FRA)

This is the first run where the human actually controlled an arc aggressor's
country, so the filter was testable for real rather than by inspection.

Two arcs were drawn across fifty months: `nazi_germany` (GER) in 1936 and
`fascist_italy` (ITA) in the 1938 repick. Arc 5 is the one whose aggressor is
FRA, and it never appeared. The repick arm for arc 5 carries the same gate as the
other six:

```
if country_exists(FRA) and FRA->is_ai(yes) and 5 not in global.sandbox_derailed_arcs[] ...
```

Before the fix this ticket's premise was real: the 1936-1941 run had arc 5 handed
to a human FRA, which then parked on the peak timeout with live wargoals nobody
could press.

Remaining unchecked: the all-human-majors case, which cannot happen in a real
session because one country cannot be the aggressor of all six arcs.
