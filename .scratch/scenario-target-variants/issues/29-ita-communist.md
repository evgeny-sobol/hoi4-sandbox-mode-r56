# 29: Communist Italy arc (FRA/ENG or BUL/YUG)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new flip arc for the communist Italian branch (`ITA_pugno_alzato`; gate: Italy communist by crises). Targets variant A (FRA, ENG), variant B (BUL, YUG), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `ITA_pugno_alzato` / `ITA_the_enemies_of_capitalism` / `ITA_liberate_the_workers_of_africa` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (communism by crises).
- [ ] Derail `italy_not_communist` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
