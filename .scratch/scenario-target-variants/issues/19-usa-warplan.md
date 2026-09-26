# 19: USA War Plan arc (JAP or ENG/CAN)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for the American War Plan branch (Pacific / anti-imperial). Targets variant A (JAP), variant B (ENG, CAN), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `USA_war_plan_orange` / `USA_war_plan_black` / `USA_defense_of_the_pacific` / `USA_intervention_in_europe` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct target(s), ladder fires.
- [ ] Single/pair target variants handled; derail on gone/neutralized targets.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
