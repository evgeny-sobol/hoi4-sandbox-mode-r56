# Scenario engine regressions (Rt56 overlay)

## Problem Statement

The `_sandbox` v0.2.0 session exposed four regressions introduced by the `6760a43` split of the
scenario engine into `sandbox-mod-core`. Full evidence is in
`_sandbox/.scratch/scenario-engine-regressions/spec.md`. Two of them cost this mod live
behaviour, and two are core-side changes this mod inherits through the sync.

1. **Arc hooks are compiled into `common/on_actions/`.** That directory is parsed as an
   on_actions file, so the effect definitions in `99_sandbox_arc_hooks.hsl` are rejected
   (`Unexpected token: sandbox_arc_*`) and every `sandbox_arc_*` call in the shared skeleton
   resolves to nothing. This mod loses two live hooks to it:
   `sandbox_arc_on_weekly` -> `sandbox_retry_afg_bop_civil_war_fuse()`, and
   `sandbox_arc_tick_hosts` -> the FRA/HUN tick-host fallback.
2. **R56-only content refs sit in the shared core.** Five `sandbox_delay_capped_cw_missions()`
   entries (`AFG_march_on_tehran`, `AFG_the_internal_crisis_mission`, `GER_freikorps_riots`,
   `EGY_impending_nationalist_uprising`, `LIT_communist_revolution_uprising_mission`), the
   `sandbox_afg_bop_cw_fuse_ready` trigger, and `sandbox_retry_afg_bop_civil_war_fuse` are
   R56-only and fail to validate in vanilla `_sandbox`. They must land here instead.
3. **`$add_honor` / `$add_tyranny` math fails inside `on_actions`** (core `common/macros.hml`):
   11 `script_math.cpp` errors and Honor/Tyranny silently reset to 0. Core-side fix; this mod
   inherits it and must not edit the synced copy.

## Solution

- Move the generated arc-hooks file from `common/on_actions/` to `common/scripted_effects/` in
  both mods, via `core/tools/extract_arc_hooks.py`; delete the stale
  `common/on_actions/99_sandbox_arc_hooks.txt`. This restores
  `sandbox_retry_afg_bop_civil_war_fuse` and the FRA/HUN tick-host fallback.
- After `_sandbox` issue 03 strips the R56-only refs from core, add them to this mod's per-mod
  catalogs (`common/scripted_effects/99_sandbox_scenarios.hsl`,
  `common/scripted_triggers/99_sandbox_scenario_triggers.hsl`) so they keep validating here.
  Rt56 defines all of them (`common/decisions/r56_AFG.txt:3189`, `:6805`).
- Take the `add_to_variable` + `clamp_variable` rewrite of the two macros from the sync; do not
  edit `common/macros.hml` here.

Ticket: `issues/01-port-sandbox-regression-fixes.md`.

## Verification

- `python core/tools/sync_core.py --check` -> `drifted=0` for both mods.
- Compile this mod against the Rt56 workshop copy (`394360/820260968`), read-only.
- Re-run a session: no scenario-attributable lines in `error.log`; `sc_goal_end` / `sc_justify`
  produce lines when a scenario runs; Honor/Tyranny events record real new values.
- Do not enable this mod together with vanilla Sandbox Mode Overhaul.
