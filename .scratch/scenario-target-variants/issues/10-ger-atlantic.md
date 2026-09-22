# 10: Germany Atlantic arc (ENG/USA)

**What to build:** a new historical arc for Germany's Atlantic / naval war branch. Targets variant A (ENG), variant B (USA), rolled 50/50. Requires the arc as data (aggressor, variants, block, key focuses) + its crisis/ultimatum events, localisation, and focus splices on `GER_crossing_the_atlantic` / `GER_atlantic_naval_bases` with `$ai_scenario_focus_boost()`. The pool gains the arc automatically.

**Blocked by:** 01 (target-array engine).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick <new id> variant=a|b`, correct pair in telemetry, smolder→crises→peak on schedule.
- [ ] Crisis events fire for the chosen variant; derail only when the target is gone/neutralized.
- [ ] Focus splices compile; `error.log` clean.