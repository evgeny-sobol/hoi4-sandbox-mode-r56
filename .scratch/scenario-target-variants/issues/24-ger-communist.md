# 24: Communist Germany arc (world revolution) (ENG/FRA/ITA or SOV/USA/JAP)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new flip arc for the communist German branch (`GER_world_revolution`; gate: Germany communist by crises). Targets variant A (ENG, FRA, ITA), variant B (SOV, USA, JAP), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `GER_root_out_imperialism` / `GER_hegemony_over_europe` / `GER_wage_war_on_capitalism` / `GER_strike_at_the_rising_sun` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `germany_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
