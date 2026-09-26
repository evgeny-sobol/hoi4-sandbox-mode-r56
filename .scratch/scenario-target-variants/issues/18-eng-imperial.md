# 18: British imperial restoration arc (RAJ/dominions or USA/JAP)

Status: resolved
Type: task
Blocked by: none

**What to build:** a new imperial arc for Britain's monarchist/imperial branch (`ENG_god_save_the_king`: gate neutrality/fascism). Targets variant A (RAJ, dominions), variant B (USA, JAP), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `ENG_reclaim_the_jewel_in_the_crown` / `ENG_bring_the_dominions_back_into_the_fold` / `ENG_unite_the_anglosphere` with `$ai_scenario_focus_boost()`.

**Note:** this is `imperial` type (gate neutrality OR fascism). It needs the flip-gate helper ticket before it can be tested; see blocked-by.

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (neutrality/fascism by crises).
- [ ] Derail `britain_not_imperial` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
