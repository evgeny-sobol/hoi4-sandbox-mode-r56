# 01: Port the scenario-engine regressions fixes into the Rt56 overlay

Status: resolved
Type: bug
Blocked by: none

**What to build:** the Rt56 side of the four regressions found in the `_sandbox` v0.2.0 session
(see `_sandbox/.scratch/scenario-engine-regressions/`). Two of them hit this mod directly; two
are core-side changes this mod inherits through the sync. The `_sandbox` sides are resolved
(core `b7d9cd1`, `929464f`, `7336310`), so this port is unblocked and done.

## Hits this mod directly

- **Arc hooks in the wrong directory.** `common/on_actions/99_sandbox_arc_hooks.hsl` is parsed
  as an on_actions file and rejected, so all four `sandbox_arc_*` calls in the shared skeleton
  resolve to nothing. This mod is the one that actually pays for it: its
  `sandbox_arc_on_weekly()` calls `sandbox_retry_afg_bop_civil_war_fuse()`, which is therefore
  orphaned, and `sandbox_arc_tick_hosts()` carries the FRA/HUN tick-host fallback. Both are
  dead. `error.log:7-10` and `11-26` are from the vanilla mod in this session, but the same
  generated file has the same shape here.
- **R56-only content must move in, not out.** After `_sandbox` issue 03, core keeps only the 23
  vanilla `sandbox_delay_capped_cw_missions()` entries. This mod must gain its own per-mod
  hook with the five R56-only missions (`AFG_march_on_tehran`,
  `AFG_the_internal_crisis_mission`, `GER_freikorps_riots`, `EGY_impending_nationalist_uprising`,
  `LIT_communist_revolution_uprising_mission`), plus `sandbox_afg_bop_cw_fuse_ready` and
  `sandbox_retry_afg_bop_civil_war_fuse`. All of these validate here - Rt56 defines them
  (`common/decisions/r56_AFG.txt:3189`, `:6805`) - and must keep working. Done in core
  `7336310`: this mod's `99_sandbox_scenarios.hsl` now defines
  `sandbox_delay_capped_cw_missions_mod()` with the five missions and carries
  `sandbox_retry_afg_bop_civil_war_fuse`, and `99_sandbox_scenario_triggers.hsl` carries
  `sandbox_afg_bop_cw_fuse_ready`. Both compile; `sandbox_arc_on_weekly` still reaches the
  retry.

## Picked up from the sync

- **`$add_honor` / `$add_tyranny` math.** The macros are core (`common/macros.hml`), so this
  mod gets the `add_to_variable` + `clamp_variable` rewrite for free. Do not edit the synced
  copy. Done: core `929464f` synced outward, `common/macros.hml` here matches core, and this
  mod's `99_sandbox_on_actions.txt` now has 20 `clamp_variable` blocks and zero `value = {`
  accumulators.

## Acceptance

- [ ] No `99_sandbox_arc_hooks` file remains under `common/on_actions/`; the four
      `sandbox_arc_*` calls validate; `sandbox_retry_afg_bop_civil_war_fuse` is reachable from
      `on_weekly` again.
- [ ] The five R56-only missions and the AFG BoP trigger validate here, and `_sandbox` (vanilla)
      no longer references them.
- [ ] `python core/tools/sync_core.py --check` reports `drifted=0` for both mods.
- [ ] Compiled against the Rt56 workshop copy; no `error.log` lines attributable to scenario
      files.

## Comments

Status normalized to `resolved` (Sep 2026) against a code audit, not an observer run: the ticket
was authored `ready-for-agent` and implemented in bulk in `ad10adf` ("Add scenario director with
28 arcs, focus-path docs, and .scratch script layout"). The audit confirmed, per ticket, the arc
in `sandbox_set_targets()` with the variants this ticket names, its event file and localisation
keys, and (for flip/imperial tickets) the `$sandbox_check_flip_gate*` macros. The observer-session
acceptance checks above remain unchecked: they need a game run, not code.
