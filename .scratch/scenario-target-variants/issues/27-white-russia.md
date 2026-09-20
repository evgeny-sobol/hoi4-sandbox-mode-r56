# 27: White Russia arc (flip after civil war) (GER/POL/FIN or UKR/Baltic)

**What to build:** a new flip arc for the post-civil-war white/aggressive-monarchist Russia (same SOV tag, gate: SOV not communist by crises after the civil war). Targets rolled 50/50: variant A (GER, POL, FIN), variant B (UKR, Baltic). Arc data + crisis/ultimatum events, localisation, focus splices on `SOV_beaten_but_not_defeated` / `SOV_white_exiles` / `SOV_imperial_legacy` / `SOV_strike_the_eagle` with `$ai_scenario_focus_boost()`.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (SOV not communist by crises).
- [ ] Derail `soviet_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.