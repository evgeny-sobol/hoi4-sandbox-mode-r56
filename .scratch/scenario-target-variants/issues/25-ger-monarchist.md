# 25: Monarchist Germany (Kaiserreich) arc (SOV/DEN or VEN/FRA)

**What to build:** a new flip/imperial arc for the monarchist German branch (`GER_restore_the_empire`; gate: Germany neutral/monarchy by crises). Targets variant A (SOV, DEN), variant B (VEN, FRA), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `GER_soviet_invasion` / `GER_restore_klein_venedig` / `GER_demand_northern_schleswig` with `$ai_scenario_focus_boost()`.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (neutrality/monarchy by crises).
- [ ] Derail `germany_not_neutral` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.