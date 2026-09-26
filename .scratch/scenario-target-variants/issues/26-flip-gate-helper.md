# 26: Generic flip/imperial gate helper

Status: resolved
Type: task
Blocked by: none

**What to build:** a single shared derail arm for flip/imperial arcs, replacing the per-arc copies in arcs 5/6. Signature: given the aggressor tag and the required ideology (or `neutrality|fascism` for imperial), derail on crises if the aggressor is not on it. Arcs 5/6 migrate onto it; new flip/imperial arcs (9, 10, 13, 16, 18, 21, 23, 24, 25) reuse it.

- [ ] Arc 5 and 6 pinned observers still derail exactly as before (`britain_not_fascist`, `america_not_communist`) with the generic arm.
- [ ] One new flip arc (e.g. communist Germany) reuses it and derails correctly.
- [ ] HSL compile clean; no scenario-attributable `error.log` lines.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
