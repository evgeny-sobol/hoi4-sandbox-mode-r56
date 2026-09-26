# 20: USA global hegemony arc (ENG/GER/HUN/JAP or hegemony)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for the American global-hegemony branch (`USA_end_monarchism` / `shatter_the_empires` / `global_hegemony`). Targets variant A (ENG, GER, HUN, JAP), variant B (hegemony set: pursue global objectives via `global_hegemony`). Rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, ladder fires.
- [ ] Derail on gone/neutralized targets; variant B (hegemony) tested for its own derail.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
