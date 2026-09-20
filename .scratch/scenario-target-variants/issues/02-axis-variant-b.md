# 02: Axis arc variant B (FRA/ENG)

**What to build:** the second target variant for the existing Axis arc. Variant A stays (CZE, POL); variant B is (FRA, ENG), rolled 50/50 at pick. Crises, peak ultimatums, derail and telemetry work identically on B.

**Blocked by:** 01 (target-array engine).

**Status:** ready-for-agent

- [ ] Pinned observer with forced variant B shows `sc_pick axis_expansion variant=b` and only FRA/ENG in `sc_seed`/`sc_target`.
- [ ] Both ultimatum events fire on the B pair; derail follows FRA/ENG.
- [ ] No scenario-attributable `error.log` lines; HSL compile clean.