# 30: Communist Britain arc (GER/USA/CAN or SOV)

**What to build:** a new flip arc for the communist British branch (`ENG_soviet_cooperation` and the one-true-revolution line; gate: Britain communist by crises). Targets variant A (GER, USA, CAN), variant B (SOV), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `ENG_soviet_cooperation` / `ENG_the_one_true_revolution` / `ENG_liberate_the_home_of_marx` / `ENG_liberate_the_american_workers` with `$ai_scenario_focus_boost()`.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `britain_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.