# Road to 56 fork

This repository is the Sandbox companion for **The Road to 56**, not a vanilla overlay. Honor, Tyranny, and Rivals follow the existing documents in this folder. Do not invent new Honor/Tyranny numbers for Rt56.

Launcher name: `Sandbox Mode Overhaul for The Road to 56`. Depend on the exact string `The Road to 56`. Do not enable vanilla Sandbox Mode Overhaul at the same time.

## Compile and overlay

Compile this folder as `target_dir` against the subscribed workshop copy `C:\Games\Steam\steamapps\workshop\content\394360\820260968` as `vanilla_root`. That workshop tree is read-only.

Unique `99_sandbox_*` names **add** files. A compiled `.include` whose relative path already exists in Rt56 (for example `common/national_focus/germany.txt`) is allowed: the output is the full Rt56 file plus splices, and that replacement is how the overlay attaches. Do not emit a same-path file that was not produced from an `.include` against the workshop copy.

Do not copy `_sandbox` `.include` files until each one is remapped to an Rt56 filename and token set. Missing focus IDs fail the compile (`Block path segment not found`).

## National Focuses

`gdd/National Focuses.md` is the target design. Rt56 trees are overlaid with `.include` files that mirror workshop filenames (`germany.include` → workshop `germany.txt`, `r56_spain.include`, game-rule trees such as `GER_focus_tree_selection` / `R56_TREE` vs `STANDARD_TREE`).

`.scratch/scripts/generate_focus_includes.py` rebuilds every Rt56 focus include. It keeps the first-pass splices and then, for IDs that still exist in Rt56, copies the matching `_sandbox` extras (party shares, Honor/rival `available`, Tyranny completion, MIC, `$crossroad_modifier`, CW-root weights). Heuristics fill the rest:

- `$ai_sandbox_modifier()` on every id'd focus (create `ai_will_do` when the Rt56 focus has none); skip it when a copied extra already uses `$ai_sandbox_set`
- `$root_modifier()` when the focus has no `prerequisite` block
- `$ai_civil_war_ignition_modifier()` and `sandbox_civil_war_cap_reached` when the focus body contains `start_civil_war`
- `$sandbox_log_cw_ignition` / `$sandbox_log_cw_root` on those completion rewards (and on the extra event-queued POR/LIT ignition IDs)
- `$ai_civil_war_root_modifier()` on the exclusive ancestor of an ignition focus (not the ignition itself; skip lesson/interven/volunteer IDs)
- `$crossroad_modifier(N)` on concurrent optional exclusive groups that are not political, party-gated, `has_government`-split, or already party/Tyranny/crossroad weighted
- `$ai_mic_modifier()` on `FOCUS_FILTER_INDUSTRY` focuses that are not political
- Honor/rival AI and `available` gates from `create_wargoal` / `declare_war_on` / `add_to_faction` (no rival `available` gate when there are 3+ war targets)
- `$ai_high_tyranny_tilt()` on coup/seize-power IDs; `is_liberal_leader(no)` on purge/secret-police IDs

Do not copy a vanilla include block whose focus ID is absent from Rt56. Country weekly Honor target arrays come from copied `99_sandbox_<TAG>_on_actions.hsl` / `99_sandbox_<TAG>_scripted_effects.hsl` (AFG, CHI, CHL, COG, ENG, EST, GER, HOL, HUN, JAP, NOR, POL, SOV, SPR, USA).

Rt56 keeps the four vanilla parties. `japan_militarism_ideology` exists and still scales MIC with world tension.

## Civil Wars

The global counter `sandbox_civil_war_count` and the cap of 3 distinct `original_tag`s (`gdd/Civil Wars.md`) run in this fork. Event/mission/decision/BoP overlays delay fuses; they do not delete `start_civil_war` payloads. Player-started wars stay unrestricted.

Vanilla fuse includes from `_sandbox` are copied when the matching workshop `.txt` exists (`.scratch/scripts/copy_cw_fuse_includes.py`). `Spain.include` drops `spain.10` (deleted in Rt56 `Spain.txt`). Workshop-missing files cannot be spliced (vanilla fall-through at runtime): `events/NSB_Estonia`, `events/NSB_Lithuania`, `common/decisions/EST`, `common/scripted_effects/BLT_scripted_effects`, `common/bop/ITA`. ITA still uses event `BBA_italy_civil_war.1` `+trigger` plus weekly retry. `EST_events.7` weekly retry is a no-op unless `EST_vapsid_takeover` is set (Rt56 `estonia.txt` does not set that flag).

`gdd/Civil Wars.md` acceptance greps still apply. In this fork the first `#sandbox` line is `Mode Overhaul for The Road to 56 v0.1.0`. Spain 1936 is `cw_event spain.1` / `lar_spain.2` (no `spain.10`). First delivery of a gated event logs `cw_event` even when weekly retry is not the caller (ITA BoP `on_activate`, NSB hours=1, Cedillo `mexico.1`, `bftb_greece.105` / `.218`). Pattern B skips stay silent; the war option logs when taken. Mission timeouts that start a war inline (`POL_peasants_strike`, `AST_veterans_revolt`, `on_daily_AST`) log `cw_event` on fire so a free-slot war is not mistaken for an ungated fuse.

Rt56-only fuses (Patterns A–D, same helpers as vanilla):

- Events: `sfl.1` (Pattern A), `greece.81.b` / `r56.ger.39.b` / `new_ger.90.b` / `MAN_56_event.13.a` / `r56_paraguay.2.a` / `peru.3.c` (Pattern B), `new_ger.1` / `new_ger.29` / `MAN_56_event.3` / `lithuania.16` / `lithuania.109` / `peru.8` / `peru.55` / `portugal.44` / `portugal.45` / `prc.105` / `rt56.rom_general_election.5` / `rt56.rom_communist_takeover.3` (`+trigger`)
- Decisions/missions: `AFG_march_on_tehran`, `AFG_the_internal_crisis_mission`, `GER_freikorps_riots`, `EGY_impending_nationalist_uprising`, `LIT_communist_revolution_uprising_mission` (weekly `+8` days); Pattern D on `den_the_second_german_revolution`, AST `start_indonesian_uprising` / `start_malayan_uprising`, and the three Valkyrie decisions that queue `new_ger.1`
- BoP: `AFG_total_government_influence` `on_activate` plus weekly retry of the same payload
- Focus ignition added on `POR_ally_anti_colonial_resistance`, `POR_center_stage_against_communism`, `POR_avenge_the_1821_disaster`, `LIT_launch_the_revolution` (those rewards queue CW events rather than calling `start_civil_war` in the focus)

Do not overlay `political.21/22/23`. Spy operations stay out of scope. Residual holes: `peru.49` / `.50` / `.51` (`fire_only_once` from untagged callers), `portugal.60` (POR lights a war in BRA; ignition is on `POR_avenge_the_1821_disaster`), and vanilla DLC fuses that `_sandbox` also left untagged (`stability.3`, `britain.23`, and similar).
