# 28: Communist Japan arc (pan-Asian revolution) (CHI/SOV or ENG/USA/SEA)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new flip arc for the communist Japanese branch (`JAP_raise_the_red_flag_high`; gate: Japan communist by crises). Targets variant A (CHI, SOV), variant B (ENG, USA, SEA), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `JAP_put_an_end_to_chinese_feudalism` / `JAP_spread_the_revolutuon_south` / `JAP_free_asians_from_soviet_opression` / `JAP_go_after_the_capitalists` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `japan_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
