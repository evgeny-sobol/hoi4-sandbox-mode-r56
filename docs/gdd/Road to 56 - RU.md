<!-- source: 30b21a63f24905be2334f85364030e2a74f8a51f -->
# Road to 56 fork - RU

Этот репозиторий - Sandbox-компаньон для **The Road to 56**, а не ванильный оверлей. Honor, Tyranny и Rivals следуют существующим документам в этой папке. Не выдумывать новые Honor/Tyranny-числа для Rt56.

Launcher name: `Sandbox Mode Overhaul for The Road to 56`. Depend on the exact string `The Road to 56`. Не включать ванильный Sandbox Mode Overhaul одновременно.

## Compile and overlay - RU

Компилировать эту папку как `target_dir` против подписанной workshop-копии `C:\Games\Steam\steamapps\workshop\content\394360\820260968` как `vanilla_root`. Это workshop-дерево read-only.

Уникальные имена `99_sandbox_*` **добавляют** файлы. Скомпилированный `.include`, чей относительный путь уже есть в Rt56 (например `common/national_focus/germany.txt`), разрешен: вывод - это полный Rt56-файл плюс сплайсы, и эта замена - то, как аттачится оверлей. Не эмитить same-path файл, который не произведен из `.include` против workshop-копии.

Не копировать `_sandbox`-файлы `.include`, пока каждый не ремаплен на Rt56-имя файла и набор токенов. Отсутствующие focus ID валят компиляцию (`Block path segment not found`).

## National Focuses - RU

`docs/gdd/National Focuses.md` - целевой дизайн. Rt56-деревья оверлеятся `.include`-файлами, зеркалящими workshop-имена (`germany.include` -> workshop `germany.txt`, `r56_spain.include`, game-rule деревья вроде `GER_focus_tree_selection` / `R56_TREE` против `STANDARD_TREE`).

`.scratch/scripts/generate_focus_includes.py` перестраивает каждый Rt56 focus include. Он держит first-pass сплайсы, а затем для ID, все еще существующих в Rt56, копирует подходящие `_sandbox`-экстры (party shares, Honor/rival `available`, Tyranny completion, MIC, `$crossroad_modifier`, CW-root веса). Остальное добивают эвристики:

- `$ai_sandbox_modifier()` на каждый id'd фокус (создать `ai_will_do`, когда у Rt56-фокуса его нет); пропустить, когда скопированная экстра уже использует `$ai_sandbox_set`
- `$root_modifier()`, когда у фокуса нет блока `prerequisite`
- `$ai_civil_war_ignition_modifier()` и `sandbox_civil_war_cap_reached`, когда тело фокуса содержит `start_civil_war`
- `$sandbox_log_cw_ignition` / `$sandbox_log_cw_root` на эти completion rewards (и на extra event-queued POR/LIT ignition ID)
- `$ai_civil_war_root_modifier()` на exclusive ancestor ignition-фокуса (не сам ignition; пропустить lesson/interven/volunteer ID)
- `$crossroad_modifier(N)` на конкурентные опциональные эксклюзивные группы, которые не политические, не party-gated, не `has_government`-split и не взвешены party/Tyranny/crossroad
- `$ai_mic_modifier()` на фокусы `FOCUS_FILTER_INDUSTRY`, которые не политические
- Honor/rival AI и `available`-гейты из `create_wargoal` / `declare_war_on` / `add_to_faction` (без rival-`available`-гейта при 3+ war targets)
- `$ai_high_tyranny_tilt()` на coup/seize-power ID; `is_liberal_leader(no)` на purge/secret-police ID

Не копировать ванильный include-блок, чей focus ID отсутствует в Rt56. Country weekly Honor target arrays берутся из скопированных `99_sandbox_<TAG>_on_actions.hsl` / `99_sandbox_<TAG>_scripted_effects.hsl` (AFG, CHI, CHL, COG, ENG, EST, GER, HOL, HUN, JAP, NOR, POL, SOV, SPR, USA).

Rt56 держит четыре ванильные партии. `japan_militarism_ideology` существует и по-прежнему скалит MIC с world tension.

## Civil Wars - RU

Глобальный счетчик `sandbox_civil_war_count` и кап в 3 разных `original_tag` (`docs/gdd/Civil Wars.md`) работают в этом форке. Event/mission/decision/BoP-оверлеи задерживают запалы; они не удаляют `start_civil_war`-пейлоады. Войны, начатые игроком, без ограничений.

Ванильные fuse includes из `_sandbox` копируются, когда существует подходящий workshop-`.txt` (`.scratch/scripts/copy_cw_fuse_includes.py`). `Spain.include` дропает `spain.10` (удален в Rt56 `Spain.txt`). Workshop-missing файлы нельзя сплайсить (vanilla fall-through в рантайме): `events/NSB_Estonia`, `events/NSB_Lithuania`, `common/decisions/EST`, `common/scripted_effects/BLT_scripted_effects`, `common/bop/ITA`. ITA по-прежнему использует ивент `BBA_italy_civil_war.1` `+trigger` плюс недельный ретрай. Недельный ретрай `EST_events.7` - no-op, пока не стоит `EST_vapsid_takeover` (Rt56 `estonia.txt` этот флаг не ставит).

Приемочные грепы `docs/gdd/Civil Wars.md` по-прежнему применяются. В этом форке первая строка `#sandbox` - это `Mode Overhaul for The Road to 56 v0.1.0`. Испания 1936 - это `cw_event spain.1` / `lar_spain.2` (без `spain.10`). Первая доставка гейтнутого ивента логирует `cw_event`, даже когда недельный ретрай - не вызывающий (ITA BoP `on_activate`, NSB hours=1, Седильо `mexico.1`, `bftb_greece.105` / `.218`). Pattern B-скипы молчат; war-опция логирует когда взята. Таймауты миссий, начинающие войну инлайн (`POL_peasants_strike`, `AST_veterans_revolt`, `on_daily_AST`), логируют `cw_event` на выстреле, чтобы войну при свободном слоте не приняли за ungated fuse.

Rt56-only запалы (Patterns A-D, те же хелперы, что ванилла):

- Events: `sfl.1` (Pattern A), `greece.81.b` / `r56.ger.39.b` / `new_ger.90.b` / `MAN_56_event.13.a` / `r56_paraguay.2.a` / `peru.3.c` (Pattern B), `new_ger.1` / `new_ger.29` / `MAN_56_event.3` / `lithuania.16` / `lithuania.109` / `peru.8` / `peru.55` / `portugal.44` / `portugal.45` / `prc.105` / `rt56.rom_general_election.5` / `rt56.rom_communist_takeover.3` (`+trigger`)
- Decisions/missions: `AFG_march_on_tehran`, `AFG_the_internal_crisis_mission`, `GER_freikorps_riots`, `EGY_impending_nationalist_uprising`, `LIT_communist_revolution_uprising_mission` (недельные `+8` дней); Pattern D на `den_the_second_german_revolution`, AST `start_indonesian_uprising` / `start_malayan_uprising` и три решения Valkyrie, ставящие в очередь `new_ger.1`
- BoP: `AFG_total_government_influence` `on_activate` плюс недельный ретрай того же пейлоада
- Focus ignition добавлен на `POR_ally_anti_colonial_resistance`, `POR_center_stage_against_communism`, `POR_avenge_the_1821_disaster`, `LIT_launch_the_revolution` (эти награды ставят CW-ивенты в очередь, а не зовут `start_civil_war` в фокусе)

Не оверлеить `political.21/22/23`. Шпионские операции вне скоупа. Остаточные дыры: `peru.49` / `.50` / `.51` (`fire_only_once` от нетегированных вызывающих), `portugal.60` (POR зажигает войну в BRA; ignition на `POR_avenge_the_1821_disaster`) и ванильные DLC-запалы, которые `_sandbox` тоже оставил нетегированными (`stability.3`, `britain.23` и подобные).