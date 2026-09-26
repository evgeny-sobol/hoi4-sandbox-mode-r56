# 22: French dismantle-Germany / destroy-Albion arc (GER or ENG)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new historical arc for France's revanchist branch. Targets variant A (GER partition), variant B (ENG destroy Albion), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `FRA_dismantle_germany` / `FRA_crush_germany` / `FRA_destroy_albion` / `FRA_strike_empire` with `$ai_scenario_focus_boost()`.

- [ ] Pinned observer: `sc_pick` with variant, correct target, ladder fires.
- [ ] Single-target variant handled; derail on gone/neutralized target.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
