# 21: French monarchist arc (SPR/ADR/MEX or SOV)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new imperial arc for France's legitimist/monarchist branch (`FRA_restore_ancient_reights`, gate neutrality). Targets variant A (SPR, ADR, MEX), variant B (SOV), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `FRA_secure_the_crown_of_spain` / `FRA_claim_the_andorran_throne` / `FRA_restore_the_mexican_monarchy` / `FRA_second_march_on_moscow` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (neutrality by crises).
- [ ] Derail `france_not_neutral` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
