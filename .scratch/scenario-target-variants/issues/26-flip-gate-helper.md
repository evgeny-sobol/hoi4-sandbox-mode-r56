# 26: Generic flip/imperial gate helper

**What to build:** a single shared derail arm for flip/imperial arcs, replacing the per-arc copies in arcs 5/6. Signature: given the aggressor tag and the required ideology (or `neutrality|fascism` for imperial), derail on crises if the aggressor is not on it. Arcs 5/6 migrate onto it; new flip/imperial arcs (9, 10, 13, 16, 18, 21, 23, 24, 25) reuse it.

**Blocked by:** 01 (target-array engine).

**Status:** ready-for-agent

- [ ] Arc 5 and 6 pinned observers still derail exactly as before (`britain_not_fascist`, `america_not_communist`) with the generic arm.
- [ ] One new flip arc (e.g. communist Germany) reuses it and derails correctly.
- [ ] HSL compile clean; no scenario-attributable `error.log` lines.