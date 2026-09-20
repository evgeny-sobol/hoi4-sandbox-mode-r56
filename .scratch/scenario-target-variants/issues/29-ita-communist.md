# 29: Communist Italy arc (FRA/ENG or BUL/YUG)

**What to build:** a new flip arc for the communist Italian branch (`ITA_pugno_alzato`; gate: Italy communist by crises). Targets variant A (FRA, ENG), variant B (BUL, YUG), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `ITA_pugno_alzato` / `ITA_the_enemies_of_capitalism` / `ITA_liberate_the_workers_of_africa` with `$ai_scenario_focus_boost()`.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `italy_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.