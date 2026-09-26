# 14: Japanese northern push arc (SOV/MON or SOV/CHI)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for the Japanese northern (hokushin-ron) branch. Targets variant A (SOV, MON), variant B (SOV, CHI), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `JAP_hokushin_ron` / `JAP_sea_establish_the_northern_resource_area` / `JAP_strike_the_soviets` / `JAP_preemptive_strike_soviet` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct pair, ladder fires.
- [ ] Crisis/ultimatums for the chosen variant; derail on gone/neutralized targets.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
