# 17: Italian Mediterranean empire arc (TUR/ROM or FRA/ENG)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for Italy's Mediterranean empire branch. Targets variant A (TUR, ROM), variant B (FRA, ENG), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `ITA_a_time_for_war` / `ITA_claims_on_turkey_bba` / `ITA_all_roads_lead_to_rome` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct pair, ladder fires.
- [ ] Crisis/ultimatums for the chosen variant; derail on gone/neutralized targets.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
