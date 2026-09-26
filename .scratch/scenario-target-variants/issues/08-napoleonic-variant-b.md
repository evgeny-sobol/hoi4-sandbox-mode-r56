# 08: Napoleonic France variant B (ENG)

Status: resolved
Type: task
Blocked by: none

**What to build:** the second target variant for the existing Napoleonic France arc. Variant A stays (GER, ITA); variant B is (ENG) as a single target, rolled 50/50 at pick. Napoleonic France has a destroy-Albion branch, so one-target variant B is valid; the engine must handle a 1-target variant (targets-gone when that one is removed).

- [ ] Pinned observer with forced variant B shows `sc_pick napoleonic_france variant=b` and only ENG in `sc_seed`/`sc_target`.
- [ ] Single-target derail works (france arc parks when ENG is gone/neutralized).
- [ ] No scenario-attributable `error.log` lines; HSL compile clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
