# 30: Communist Britain arc (GER/USA/CAN or SOV)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new flip arc for the communist British branch (`ENG_soviet_cooperation` and the one-true-revolution line; gate: Britain communist by crises). Targets variant A (GER, USA, CAN), variant B (SOV), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `ENG_soviet_cooperation` / `ENG_the_one_true_revolution` / `ENG_liberate_the_home_of_marx` / `ENG_liberate_the_american_workers` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `britain_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
