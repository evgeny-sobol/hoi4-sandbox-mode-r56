# 08: Napoleonic France variant B (ENG)

**What to build:** the second target variant for the existing Napoleonic France arc. Variant A stays (GER, ITA); variant B is (ENG) as a single target, rolled 50/50 at pick. Napoleonic France has a destroy-Albion branch, so one-target variant B is valid; the engine must handle a 1-target variant (targets-gone when that one is removed).

**Blocked by:** 01 (target-array engine).

**Status:** ready-for-agent

- [ ] Pinned observer with forced variant B shows `sc_pick napoleonic_france variant=b` and only ENG in `sc_seed`/`sc_target`.
- [ ] Single-target derail works (france arc parks when ENG is gone/neutralized).
- [ ] No scenario-attributable `error.log` lines; HSL compile clean.