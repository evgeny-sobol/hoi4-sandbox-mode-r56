# 06: Fascist Britain variant B (GER/ITA)

Status: resolved
Type: task
Blocked by: none

**What to build:** the second target variant for the existing Fascist Britain arc. Variant A stays (FRA, SOV); variant B is (GER, ITA), rolled 50/50 at pick. Crises, peak ultimatums, derail and telemetry work identically on B, and the flip gate (fascism by crises) is unchanged.

- [ ] Pinned observer with forced variant B shows `sc_pick fascist_britain variant=b` and only GER/ITA in `sc_seed`/`sc_target`.
- [ ] Flip derail still fires as before on both variants (britain_not_fascist on crises).
- [ ] No scenario-attributable `error.log` lines; HSL compile clean.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
