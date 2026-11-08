# 04 - Repick eligibility ignores war state and delivers a spent arc

Status: ready-for-human
Type: bug
Blocked by: 01

## What to build

A repicked arc costs at least one month of play before it can ignite, so the
session gets a ladder rather than an instant `sc_ignite`.

## Problem

Every generated `eligible()` tests `country_exists` and nothing else, in both the
initial pick and the repick:

```
gen_napoleonic_france_scenario_eligible():
  if country_exists(FRA):
    eligible[].add(5)
```

`sandbox_scenario_maybe_repick()` builds the repick pool from the same predicate
plus the never-derailed check. Neither asks whether the aggressor is already at
war with the targets it is about to declare.

Observed in the 1936-1941 session: after the arc-5 `peak_timeout` the repick drew
arc 1 variant `b` (targets FRA and ENG) while GER was already at war with FRA.
The ignite check fired on the very next monthly tick and the arc was over before
it was played:

```
1939.07.01 HAI sc_repick nazi_germany / sc_pick / sc_phase smolder / sc_variant b
1939.08.01 GER sc_ignite  nazi_germany_war sc=1 phase=3 t=43
1939.08.01 GER sc_success nazi_germany_war sc=1 phase=3 t=43
1939.08.01 GER sc_end     nazi_germany_war sc=1 phase=3 t=43
```

One month from pick to success. The derailed-arc bookkeeping also consumed arc 1
for the rest of the session on a war that predated the pick.

## Why it matters

The GDD lifecycle exists so an arc smolders, then applies pressure through
crises and peak, then ignites. An arc that is already at war on the tick after
its pick skips every rung and still costs the session an arc from the
never-derailed pool. The observed session had six arcs available and burned a
second one this way.

## Fix shape

Add a war-state filter to the eligibility predicate used by both the initial
pick and the repick: an arc is not eligible when its aggressor is already at war
with any of its declared targets for the live variant. Keep the arc in the pool
for later rather than treating it as derailed.

Note the dependency: this only becomes observable once issue 01 makes repicks
happen at all. Landing 04 before 01 would be untestable.

## Acceptance

The session lines need a game run; the code and artifacts are verified.

- [ ] A repick never draws an arc whose aggressor is already at war with a
      declared target of the live variant.
- [x] The same filter applies to the initial pick at `on_startup`.
- [x] A skipped arc stays eligible for a later repick; it is not appended to
      `sandbox_derailed_arcs[]`.
- [x] A repick with every arc filtered out sets the phase-3 quiet state and logs
      `sc_repick none_eligible` rather than drawing anyway.
- [x] At least one session shows a repicked arc surviving more than one month
      before ignition or derail. The 1938 repick to `fascist_italy` lived twenty
      months: smolder on 1 July 1938, crises on 1 July 1939, still running and at
      war=0.00 when the session ended in March 1940. Compare the failure this
      ticket fixed, where a repicked arc ignited a month after the pick.
- [x] No new `error.log` lines attributable to scenario files. Zero `99_sandbox_scenarios` lines in 1433 error lines across the 1936-1940 run.

## Out of scope

- Whether an arc that ignites fast is itself acceptable when the war is declared
  *after* the pick. This ticket only rejects wars that already exist.

## Verification

- Recompile after the `.hsl` change.
- Re-extract and confirm no `sc_pick` / `sc_ignite` pair sits one month apart
  with a war that predates the pick.

## Implementation (2026-11-06)

Strict form, chosen by the operator after the first pass: the aggressor must not
be at war with **any** declared target of **any** variant.

- `render_pick()` in `core/tools/build_scenario_catalog.py` builds one `if` gate
  per arc: `country_exists(<aggr>) and <aggr>->is_ai(yes) and not
  <aggr>->has_war_with(<target>)` repeated over the union of every declared
  target across variants.
- The seven hand-written repick arms in each mod's `99_sandbox_scenarios.hsl`
  carry the same gate. A skipped arc never reaches
  `sandbox_derailed_arcs[]`, so it returns to the pool on a later repick.
- `render_roll_variant()` is back to the plain roll: with a strict eligibility
  gate every variant of a drawable arc is unpressed by construction, so a war
  filter there would be dead code that silently diverges from the rule.
- `docs/gdd/Scenarios.md` "Selection" documents the strict rule and the
  `and`-chaining requirement.
- `check_repick_gate.py` audits it: the war test must sit on the eligibility
  `if` line (not in the body), must name the arc's own aggressor, and the body
  must carry no stray condition.

### The compile trap that drove the final shape

Writing the war tests as separate body lines, or as an `and OR:` suffix, both
produce broken output:

* `and OR:` leaves a bare `OR` inside `limit` with its branches after the block.
* A body-level `not X` - even as a `NOT:` sub-block - is emitted OUTSIDE
  `limit`, where it is evaluated as a standalone expression and gates nothing.

Only `and`-chaining on the `if` line puts every check inside `limit`. Verified
against compiled output, not assumed: the first two shapes were compiled and
read before being discarded.

### Evidence

- `build_scenario_catalog.py` from the authoritative core repo rebuilt both
  mods; `--check` reports `7 spec(s), artifacts in sync` for both.
- Both mods compile. Compiled `gen_<arc>_scenario_eligible()` and the compiled
  repick arms carry every war test inside `limit`.
- `check_repick_gate.py` was negative-tested three ways, each caught: a
  body-line war test, dropping the war test entirely, and stripping the tests
  from a generated gate. All reverted.
- All seven guards pass in both mods.
- **Not yet done: a game run.** The two session-side criteria need one.

## Session attempt (2026-11-07, 1936.01-1941.01)

Not exercised: the criteria this ticket gates did not come up in the run.

Two arcs were drawn and both were legal at their pick moment: arc 1 in 1936 at
game start, arc 4 in January 1940 after arc 1 timed out, with SOV not yet at war
with POL or ROM. No pick landed on an arc whose aggressor was already at war, so
the filter was never asked to reject anything.

## Session result (2026-11-07, 1936.01-1940.03)

The repicked arc survived, which is the behaviour this ticket is for:

```
 1 July 1938  HAI sc_repick fascist_italy sc=2 phase=0
 1 July 1938  HAI sc_pick   fascist_italy sc=2 phase=0
 1 July 1939  HAI sc_phase  crises sc=2 phase=1
 1 March 1940 ITA census   ... war=0.00    (still alive at session end)
```

Twenty months from pick to the end of the log, and ITA stayed out of any war
against its declared targets YUG and SWI throughout. The failure this ticket
fixed was the opposite shape: a repick in July, an ignition in August, one slot
of the pool burned.

Still unchecked: no pick landed on an arc whose aggressor was already at war, so
the filter was never observed rejecting anything. That needs a session where a
major is already fighting when an arc ends.
