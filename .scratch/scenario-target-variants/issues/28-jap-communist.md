# 28: Communist Japan arc (pan-Asian revolution) (CHI/SOV or ENG/USA/SEA)

**What to build:** a new flip arc for the communist Japanese branch (`JAP_raise_the_red_flag_high`; gate: Japan communist by crises). Targets variant A (CHI, SOV), variant B (ENG, USA, SEA), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `JAP_put_an_end_to_chinese_feudalism` / `JAP_spread_the_revolutuon_south` / `JAP_free_asians_from_soviet_opression` / `JAP_go_after_the_capitalists` with `$ai_scenario_focus_boost()`.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `japan_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.