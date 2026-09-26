# 27: White Russia arc (flip after civil war) (GER/POL/FIN or UKR/Baltic)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new flip arc for the post-civil-war white/aggressive-monarchist Russia (same SOV tag, gate: SOV not communist by crises after the civil war). Targets rolled 50/50: variant A (GER, POL, FIN), variant B (UKR, Baltic). Arc data + crisis/ultimatum events, localisation, focus splices on `SOV_beaten_but_not_defeated` / `SOV_white_exiles` / `SOV_imperial_legacy` / `SOV_strike_the_eagle` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (SOV not communist by crises).
- [ ] Derail `soviet_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
