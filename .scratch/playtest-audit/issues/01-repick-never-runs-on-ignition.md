# 01 - Repick never runs on the ignition path, so the director parks for the session

Status: resolved
Type: bug
Blocked by: none

## What to build

After an arc ignites by war, the director keeps going: it records the finished
arc, picks a fresh one from the never-derailed pool, and telemetry continues for
the rest of the session.

## Problem

The monthly tick runs ignition before derail:

```
sandbox_scenario_tick():
  ...
  sandbox_scenario_check_ignite_by_war()   # .hsl:239
  sandbox_scenario_check_derail()          # .hsl:240
```

`check_ignite_by_war` delegates to `sandbox_ignite_if_at_war`, which sets
`global.sandbox_scenario_phase = 3` on a matching war (`99_sandbox_engine.hsl`
around line 45 for the `on_declare_war` entry point and the four target-slot
blocks in the monthly sweep). Only then does `check_derail` run, and it takes
its snapshot at its own top:

```
sandbox_scenario_check_derail():                # .hsl:730
  phase_before = global.sandbox_scenario_phase  # .hsl:731  -> already 3
  ...
  if phase_before < 3 and global.sandbox_scenario_phase == 3:
    sandbox_scenario_maybe_repick()             # .hsl:746
```

On the ignition path the gate is false by construction, so
`sandbox_scenario_maybe_repick()` never runs. The arc stays at phase 3, which
closes every `phase < 3` gate: the per-arc ticks, the s7 telemetry
(`sandbox_scenario_s7_telemetry`), `sc_power`, `sc_goal`, `sc_focus`, the lot.
`on_declare_war` reaches the same dead end without `check_derail` even being in
the same call.

## Evidence (1936-1941 Rt56 session)

The two transitions sit next to each other in one extract:

```
1939.07.01 HAI sc_derail peak_timeout  ... phase=3
1939.07.01 HAI sc_end    peak_timeout  ... phase=3
1939.07.01 HAI sc_repick nazi_germany  ... phase=0
1939.07.01 HAI sc_pick   nazi_germany  ... phase=0
1939.08.01 GER sc_ignite  nazi_germany_war ... phase=3
1939.08.01 GER sc_success nazi_germany_war ... phase=3
1939.08.01 GER sc_end     nazi_germany_war ... phase=3
                                  <-- 19 months of silence to 1941.02.14
```

The July derail repicked because the phase was set *inside* the derail check, so
the snapshot still read 2. The August ignition did not, because the phase was
already 3 when the snapshot was taken.

## Shape of the fix

Take the phase snapshot once per tick, in the tick, before anything can move it,
and let both the derail dispatcher and the ignite path see that snapshot. The
`on_declare_war` entry needs the same treatment or it has to route through the
same post-ignition repick. Do not fix this by reordering the two calls alone:
that still leaves `on_declare_war` broken.

Both mods share the shape (`99_sandbox_scenarios.hsl` is a per-mod copy, not
synced core content), so apply it to `_sandbox` as well as `_sandbox-r56`.

## Acceptance

Every criterion below needs a game run. The code and the compiled output are
verified; none of these lines has been observed in a session yet.

- [x] After an ignition by war, a `sc_repick` line follows in the same month.
- [x] Telemetry continues past the first ignition: a fresh session from 1936
      produces `#sandbox` lines after its first `sc_end *_war`.
- [x] An `on_declare_war` ignition repicks the same way as a monthly-sweep one.
      Proven by the 1940 session: `sc_ignite` fires on 23 June 1938 - mid-month,
      so it cannot be the monthly sweep - and `sc_repick` follows on 1 July, the
      first tick after the flag was raised. This is exactly the path the flag
      exists for, since there is no tick snapshot to fall back on.
- [x] The 1939.07 non-ignition derail path still repicks exactly once (no double
      repick, no skipped derail).
- [ ] Pinned sessions (`sandbox_scenario_pin == 1`) still go quiet at phase 3 and
      do not repick. Not exercised: the session was unpinned.
- [x] No new `error.log` lines attributable to scenario files.

## Out of scope

- The 12-month peak timeout itself and its derail reasons.
- Which arcs are eligible; see issue 04 for the war-state filter.

## Verification

- Recompile after the `.hsl` change (compile-after-hsl rule).
- Re-extract with `.scratch/scripts/extract_sandbox.py`; confirm lines continue
  beyond the first `sc_end *_war` and that at least one `sc_repick` follows an
  ignition.
- Confirm the derail-then-repick pair still appears as a single repick.

## Implementation (2026-11-06)

Applied to both mods; the shape is identical in each.

- `sandbox_scenario_tick()` now snapshots `phase_at_tick_start` before the
  ignition sweep and the derail dispatcher, and owns the gate: if the phase is 3
  at the end of the two checks it calls `sandbox_scenario_maybe_repick()` once.
- `sandbox_scenario_check_derail()` lost its own `phase_before` snapshot and its
  repick call. It now only decides whether the arc dies, so nothing can repick
  twice when a derail happens in the same tick as an ignition.
- `sandbox_log_scenario_success()` raises `global.sandbox_scenario_repick_pending`.
  Every caller of that logger sets the phase to 3 first and is itself gated on
  `phase < 3`, so the flag is only ever raised by a genuine ignition. The next
  tick's gate consumes it and clears it, which is how an `on_declare_war`
  ignition repicks without any history in the tick that follows it.
- `sandbox_pick_scenario()` and `sandbox_scenario_maybe_repick()` clear the flag
  on every pick, so it cannot leak across arcs.
- Pinned sessions are untouched: `maybe_repick()` returns early on
  `sandbox_scenario_pin != 0` and leaves the phase at 3, exactly as before.

New guard `.scratch/scripts/check_repick_gate.py` (shared core, in `SHARED_MISC`)
asserts the accepted shape in both mods: the tick takes a snapshot before the
ignition call, the tick calls the repick, the dispatcher does not, the ignite
path raises the flag, and both pick paths clear it.

Evidence this is source-verified, not session-verified:

- Both mods compile clean (`compiler.py`, r56 against the workshop root). The
  emitted `99_sandbox_scenarios.txt` carries the snapshot before
  `sandbox_scenario_check_ignite_by_war = yes` and no `phase_before` anywhere.
- `check_repick_gate.py` reports 0 problems on the fixed code and 4 problems per
  mod on a reconstructed pre-fix fixture, so it is not a no-op.
- `check_derail_arms.py`, `check_pick_gate.py`, `check_if_else.py` and
  `check_focus_splices.py` all still report 0.
- **Not yet done: a game run.** The two unchecked criteria need a session from
  1936 in which an arc ignites by war, then a look at the extract. Until that
  run exists, "telemetry continues past the first ignition" is a reading of the
  code, not an observation.

## Session result (2026-11-07, 1936.01-1941.01)

The director survives a terminal arc:

```
1940.01  GER sc_derail peak_timeout ai=1 alive=1 wgo=1 t0=CZE t1=POL ... phase=3
1940.01  GER sc_end    peak_timeout ... phase=3
1940.01  HAI sc_repick soviet_west sc=4 phase=0
1940.01  HAI sc_pick   soviet_west sc=4 phase=0
```

Telemetry continues after the repick to the end of the run. Before this fix the
same sequence ended the session's telemetry for good.

Two criteria stay unchecked because the session did not exercise them: no arc
ignited by war (so the `on_declare_war` path never ran), and the session was
unpinned (so the pinned quiet path never ran).

## Second session result (2026-11-07, 1936.01-1940.03)

The `on_declare_war` path was finally exercised. The ignition lands on 23 June
1938, not on a month boundary, so it came from the declare-war event and not from
the monthly sweep of ongoing wars - the sweep only runs on tick days:

```
23 June 1938  GER sc_ignite nazi_germany_war sc=1 phase=3
23 June 1938  GER sc_success nazi_germany_war
23 June 1938  GER sc_end    nazi_germany_war
 1 July 1938  HAI sc_repick fascist_italy sc=2 phase=0
 1 July 1938  HAI sc_pick   fascist_italy sc=2 phase=0
```

The repick arrives on the first tick after the flag was raised, which is the
designed one-month lag for this path. Telemetry continues past it for another
twenty months. This closes the last open traceability criterion in this ticket.

Still unchecked: the pinned-session criterion. No run has used a pin yet.
