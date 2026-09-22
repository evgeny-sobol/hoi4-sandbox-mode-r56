# 21: French monarchist arc (SPR/ADR/MEX or SOV)

**What to build:** a new imperial arc for France's legitimist/monarchist branch (`FRA_restore_ancient_reights`, gate neutrality). Targets variant A (SPR, ADR, MEX), variant B (SOV), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `FRA_secure_the_crown_of_spain` / `FRA_claim_the_andorran_throne` / `FRA_restore_the_mexican_monarchy` / `FRA_second_march_on_moscow` with `$ai_scenario_focus_boost()`.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (neutrality by crises).
- [ ] Derail `france_not_neutral` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.