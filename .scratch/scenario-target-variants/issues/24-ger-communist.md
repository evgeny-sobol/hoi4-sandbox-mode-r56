# 24: Communist Germany arc (world revolution) (ENG/FRA/ITA or SOV/USA/JAP)

**What to build:** a new flip arc for the communist German branch (`GER_world_revolution`; gate: Germany communist by crises). Targets variant A (ENG, FRA, ITA), variant B (SOV, USA, JAP), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `GER_root_out_imperialism` / `GER_hegemony_over_europe` / `GER_wage_war_on_capitalism` / `GER_strike_at_the_rising_sun` with `$ai_scenario_focus_boost()`.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `germany_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.