# 12: Soviet southern thrust arc (TUR/IRQ/PER or PAK/RAJ/AFG)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for the Soviet southern expansion. Targets variant A (TUR, IRQ, PER), variant B (PAK, RAJ, AFG), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `SOV_the_last_break_southward` / `SOV_preemptive_invasion_of_iran` / `SOV_into_the_plateau` with `$ai_scenario_focus_boost()`.

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
