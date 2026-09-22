# 04: Japanese arc variant B (BRM/INS/MAL)

**What to build:** the second target variant for the existing Japanese arc. Variant A stays (CHI, PHI); variant B is (BRM, INS, MAL), rolled 50/50 at pick. Crises, peak ultimatums, derail and telemetry work identically on B.

**Blocked by:** 01 (target-array engine).

**Status:** ready-for-agent

- [ ] Pinned observer with forced variant B shows `sc_pick japanese_expansion variant=b` and only BRM/INS/MAL in `sc_seed`/`sc_target`.
- [ ] Three targets must not break the two-letter join/target pattern: derail/peak handle a 3-target variant (targets-gone requires all three removed).
- [ ] No scenario-attributable `error.log` lines; HSL compile clean.