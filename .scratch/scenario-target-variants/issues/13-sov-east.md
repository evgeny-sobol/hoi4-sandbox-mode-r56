# 13: Soviet eastern push arc (JAP/MAN or USA/CAN)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for the Soviet eastern expansion (Japan / Manchuria / Alaska). Targets variant A (JAP, MAN), variant B (USA, CAN), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `SOV_crush_our_eastern_rival` / `SOV_our_american_holding` / `SOV_restore_the_old_eastern_empire` with `$ai_scenario_focus_boost()`.

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
