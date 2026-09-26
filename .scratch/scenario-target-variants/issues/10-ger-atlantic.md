# 10: Germany Atlantic arc (ENG/USA)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for Germany's Atlantic / naval war branch. Targets variant A (ENG), variant B (USA), rolled 50/50. Requires the arc as data (aggressor, variants, block, key focuses) + its crisis/ultimatum events, localisation, and focus splices on `GER_crossing_the_atlantic` / `GER_atlantic_naval_bases` with `$ai_scenario_focus_boost()`. The pool gains the arc automatically.

- [ ] Pinned observer: `sc_pick <new id> variant=a|b`, correct pair in telemetry, smolder→crises→peak on schedule.
- [ ] Crisis events fire for the chosen variant; derail only when the target is gone/neutralized.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
