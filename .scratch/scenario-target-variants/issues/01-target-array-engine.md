# 01: Target-array engine

**What to build:** the per-session `sandbox_targets[]` array that every scenario mechanic reads. At pick (pinned or random), after an arc is chosen, the director rolls the A/B variant (50/50) for that arc and writes the two chosen target tags into `sandbox_targets[]`; `sc_pick` logs the variant. The existing eight arcs behave identically (variant A = their current pairs), but seed, crisis/peak fire, derail checks and telemetry now read the array instead of hard-coded pairs. Adds the generic seed helper and the generic derail arms for target-gone/neutralized.

**Blocked by:** None (can start immediately).

**Status:** ready-for-agent

- [ ] `sc_pick <arc> variant=a` for every existing arc 1-8 on a pinned observer; `sc_seed` and all `sc_target`/`sc_goal`/`sc_justify` lines name exactly the chosen pair.
- [ ] Roll path exists: forcing variant B on any arc changes the pair and telemetry follows.
- [ ] Derail still fires on the chosen pair only (targets-gone / neutralized keyed to `sandbox_targets[]`).
- [ ] No `error.log` lines attributable to scenario files; HSL compile clean.