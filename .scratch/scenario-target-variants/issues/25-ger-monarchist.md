# 25: Monarchist Germany (Kaiserreich) arc (SOV/DEN or VEN/FRA)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new flip/imperial arc for the monarchist German branch (`GER_restore_the_empire`; gate: Germany neutral/monarchy by crises). Targets variant A (SOV, DEN), variant B (VEN, FRA), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `GER_soviet_invasion` / `GER_restore_klein_venedig` / `GER_demand_northern_schleswig` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (neutrality/monarchy by crises).
- [ ] Derail `germany_not_neutral` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
