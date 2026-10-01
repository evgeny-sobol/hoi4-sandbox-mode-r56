<!-- source: 30b21a63f24905be2334f85364030e2a74f8a51f -->
# Scenarios - RU

Сценарий - это кризисная арка на всю сессию, которую ведет **директор**: фоновая система, выбирающая на старте один правдоподобный конфликт и толкающая к нему ИИ бонусами и скриптованными кризисами, пока не грянет большая война. Война - это суть. В каких-то сессиях игрок в нее вступает; в каких-то - сидит в стороне; тихих сессий не бывает.

Сценарии - это **не**:
- Скриптованные объявления войны. Директор сам войну не объявляет и `start_civil_war` никогда не зовет; он меняет только веса, rivalry, Honor-экспозицию и стреляет кризисными ивентами. Курок спускает ИИ.
- Рельсы. Фиксированных дат объявлений нет, вынужденных мирных сделок нет, телепортов дивизий нет.
- Система, целящаяся в игрока. Челлендж фоновый: война где-то в мире, а не нацелена на тег игрока.
- Гражданские войны (`docs/gdd/Civil Wars.md`). Войны сценариев - международные. Счетчик и кап гражданских войн директор не трогает.

Sandbox-only: все правила ниже работают под `is_sandbox_mode_on()`. Исторический режим не меняется.

## Why this is needed - RU

Сессии observer скучные: страны редко начинают войны и еще реже вступают друг за друга. Диагноз (GDD плюс исходники, сентябрь 2026):

1. Исторический движок войн ушел без замены. Все ванильные strategy plans абортятся в sandbox; war-фокусы весят 40 как промышленность и режутся дальше через war support (примерно x0.5 в 1936). (`docs/gdd/National Focuses.md`, "Basic modifiers"; `common/ai_strategy_plans/*.include`.)
2. Honor-гейты плюс betrayal-вес блокируют войны на друзей: на старте большинство лидеров не может тронуть союзника, а honorable-ИИ почти никогда не берет betrayal-фокус. (`docs/gdd/Honor System.md`, "Gating betrayal focuses by band", "AI weighting".)
3. Порог Feud: планы `conquer` / `prepare_for_war` существуют только при `rivalry >= 75`, слоты стартуют с 50 и гниют без подпитки. (`docs/gdd/Rivals System.md`, "AI strategies", "Rivalry changes".)
4. Фрагментированные альянсы: rival-гейтнутая кооперация плюс `alliance -200` означают меньше фракций и меньше каскадов через призыв к оружию, хотя Honor платит за вступление. (`docs/gdd/Rivals System.md`, "National focuses"; `docs/gdd/Honor System.md`, "Honor gains".)
5. Ложный след исключен: кап гражданских войн международные войны не трогает.

Чинить каждый гейт по отдельности - вернуть шум, а не драму. Директор чинит форму сессии: один выбранный конфликт, эскалация по расписанию, на практике гарантированно.

## Design goals - RU

1. В каждой сессии большая война. "Гарантированность" доставляется эскалационной лестницей, а не форсированными объявлениями.
2. Челлендж фоновый: война сценария где-то; игрок может вступать или сидеть в стороне.
3. Только правдоподобные арки: исторические и could-have-happened. Шут-арок в v1 нет.
4. Директор использует только бонусы и кризисы. Если войну нельзя заработать рычагами, неправа арка, а не правило.
5. Общая механика, пер-модный контент: один движок директора, раздельные actor/event/focus id для ваниллы и Rt56.
6. Верифицируемость как у гражданских войн: log-first приемка на observer-сессиях (`#sandbox`-телеметрия).

## Model - RU

### Arc (generator-ready schema) - RU

Контент - фиксированные авторские арки, но каждая арка пишется как данные по одной схеме, чтобы генератор мог потом рандомизировать поверх. Доказательство "generator-ready" - вторая арка: если ей нужна новая механика, чинить схему, а не арку.

```yaml
arc:
  id: axis_expansion
  plausibility: historical      # historical | plausible
  actors:
    aggressors: [GER]
    joiners: { select: top_n_by_scorer, n: 2, scorer: scenario_join_scorer }
    targets: [CZE, POL]
  ladder:                       # calendar phases, "Escalation ladder"
    - { phase: smolder, from: 1936.1.1 }
    - { phase: crises,  from: 1937.1.1 }
    - { phase: peak,    from: 1938.1.1 }
  levers:                       # "Levers", global plus per-phase parameters
    rivalry_seed / honor_exemptions / war_support / focus_weights / join
  crises: [...]                 # scripted events per phase
  end: stand_down_to_support    # "Lifecycle"
  derail: abort_and_repick      # "Lifecycle"
  content_refs:                 # per-mod ids, "Per-mod content"
    vanilla: [...]  r56: [...]
```

### Selection - RU

Одна арка на сессию, выбирается на старте взвешенным рандомом из подходящих арок. Пригодность - это plausibility плюс sanity (акторы существуют на карте). Пик - сюрприз в игре: он логируется (`sc_pick`), но ни UI, ни ивент, ни тултип выбранную арку не называют. Сам пул виден (pinning game rule перечисляет опции); `game.log` вне полосы, как `cw_`-телеметрия.

Пул v2 держит шесть арок (Axis плюс пять новых) с равными весами. Game rule пинит фиксированный сценарий для реплеев и тестов; pin-опции существуют только для implemented арок и растут с пулом. Пин перекрывает случайный пик и означает строгую изоляцию: пикатированная сессия никогда не перевыбирает (дерайльнутый пин тихо гаснет). В случайных сессиях derail перевыбирает следующую подходящую еще не дерайлившуюся арку (`sc_derail` + `sc_repick` + новый `sc_pick`); дерайльнутая арка в той же сессии в пул не возвращается. Перевыбранная арка прогоняет лестницу со smolder, сжатую календарем (поздние репики бьют crises и peak на соседних тиках).

### Escalation ladder - RU

Лестница заменяет форсирование. Три фазы на каждую арку (smolder / crises / peak), каждый ранг стреляет один раз (anti-spam правило). Лестница держится на peak, пока не грянет война, ограниченная **peak timeout**: арка, все еще на peak через 12 месяцев после входа, дерайлится (`peak_timeout`) и перевыбирается, потому что другого выхода у лестницы нет (observer-сессия на ванильном порту сидела на peak шесть лет). Дедлайн-запала, объявляющего войну по скрипту, нет (см. "Scenarios are not").

Даты пер-арочные (настроены под историю каждой арки); календарь Axis - шаблон:

| Arc | Smolder from | Crises from | Peak from |
|-----|------|------|------|
| 1 Axis | 1936.1.1 | 1937.1.1 | 1938.1.1 |
| 2 Soviet | 1936.1.1 | 1937.1.1 | 1938.1.1 |
| 3 Japanese | 1936.1.1 | 1937.6.1 | 1938.6.1 |
| 4 Italian | 1936.1.1 | 1937.6.1 | 1938.6.1 |
| 5 Fascist Britain | 1936.1.1 | 1937.1.1 | 1938.6.1 |
| 6 Red America | 1936.1.1 | 1937.1.1 | 1938.6.1 |
| 7 Napoleonic France | 1936.1.1 | 1937.6.1 | 1938.6.1 |
| 8 Habsburg restoration | 1936.1.1 | 1937.6.1 | 1938.6.1 |

- **Smolder**: rivalry-сидинг агрессоров против целей, Honor-исключения для пар сценария, war-focus веса. Тихое накопление, без кризисов.
- **Crises**: скриптованные кризисные ивенты (claims, incidents), war-support памп, join-рычаги для joiners. Мир замечает. Flip-арки (5-6) должны флипнуться к этой фазе или дерайлятся.
- **Peak**: ультиматумы, максимальное давление. Каждый peak оставляет 12-18 месяцев до пулового дедлайна 1940.

### Levers - RU

**Aggression** (закрывает диагнозы 1-3):
- Rivalry-сидинг и инъекции к Feud (`>= 75`) для агрессоров против целей через существующую slot-дисциплину (`$add_rivalry`, `set_rival`; `docs/gdd/Rivals System.md`). На Feud ИИ получает `conquer 100` / `prepare_for_war 100`, а antagonism-фокусы весят x3.
- Honor-исключения: каждая арка регистрирует declared scenario enemies на селекте (именованный парный список; представление - деталь реализации). Объявления войны между declared enemies пропускают betrayal-заряд в `on_declare_war` и проходят `can_PREV_get_wargoal_on_THIS`. Это узкий явный карв-аут: `docs/gdd/Honor System.md` ("Honor losses") нужен одной строкой про сценарное исключение. Исключение покрывает и гейт, и вес: declared enemies проходят `can_PREV_get_wargoal_on_THIS` и пропускают `$ai_betrayal_modifier_vs` (весовая половина отсутствовала до s8, когда day-1 SOV-FIN NAP занулил советский war-focus вес на весь 1936). Сама rivalry цену предательства по-прежнему никогда не снижает.
- War support акторам, компенсирующий системный antagonism-срез.
- Числа рычагов общие: каждая арка стартует с Axis-значений (seed 65, crisis-инъекция +10, ultimatum-defy инъекция +15, war-support гранты) и тюнится только по observer-логам. Никакого кабинетного пер-арочного баланса.

**Focus weights** (закрывает диагноз 1): толкать акторов к их war-фокусам через существующие antagonism/rivalry-модификаторы. Отдельный сценарный буст разрешен, только если Feud плюс исключения окажутся недостаточны в логах. s8 и s9 были тем случаем (Soviet QUIET: Feud 100, ноль `sc_focus` на военной ветке). Буст - общий `$ai_scenario_focus_boost()` (x5, только живой агрессор, лестница не кончена), сплайснутый на war-focus ветку арки; Arc 2 использует `SOV_beaten_but_not_defeated` плюс шесть `sc_focus` id. Вердикт s10: x5 fork-буст проиграл сталинской ветке baseline (`factor(1)` + `add(40)` + `communism_factor*2` против `5` + `(demo+mon+fasc)*2`); SOV перепрошел `SOV_the_path_of_marxism_leninism`, все шесть бустнутых фокусов остались недостижимы, ноль `sc_focus`. Поднятие fork-буста (или ретаргет развилки) - открытый вопрос v2; значение буста общее, пока логи не скажут иначе. Какую ветку фокусов толкает каждая арка, нарисовано Mermaid-диаграммой на арку в `docs/gdd/Scenarios Catalog.md` ("Focus paths per arc"; генерируется из `docs/gdd/National Focuses/*.md`).

**Join levers** (закрывает диагноз 4): на peak две топ-скорера из открытого пула получают приглашение во фракцию (`scenario_join_scorer`, top-2, по одному письму каждому, `sc_offer` на письмо). Один скорер на все арки, без пер-арочных параметров и без гарантированных flavor-джойнеров. Фиксированного списка тегов нет: пригодность гейтится, а не курируется. Кандидат скорит ноль (пропускается), если он агрессор, под игроком, в гражданской войне, в войне с агрессором, уже сидит во фракции агрессора, субъект или сюзерен агрессора, либо держит enemy ideology к агрессору (`has_enemy_ideology`: та же группа или non-aligned с любой стороны - pass). Членство в чужой фракции - не барьер: принявший джойнер сначала выходит из старой фракции (leave-then-join; джойнер, возглавляющий свою фракцию, выходит из нее и лидерство переходит по правилам игры) и выход не несет Honor-заряда (one-shot `sandbox_honor_skip_leave_faction`, как у релизнутой нации). Скор - сила плюс goodwill тремя лестницами (пороги складываются; максимумы 60/60/60, тюнабельны): дивизии (>10/+5, >30/+10, >60/+15, >100/+15, >150/+15), промышленность как total `num_factories` (>10/+10, >25/+15, >50/+20, >80/+15, снимается в `scenario_join_industry` до скоринга), opinion к агрессору (>25/+10, >50/+20, >75/+30, <0/-10, <-50/-20). Блок хранит имя арки (Axis, Comintern, Co-Prosperity, Mare Nostrum, New Empire, People's Internationale); пост-join флипы идеологии не трекаются (раз внутри - внутри).

**Crises**: скриптованные ивенты по фазам (claims, border incidents, ultimatums), создающие коры, tension и war support. Одна анатомия на каждую арку: claims плюс incidents в crises, ультиматумы на peak. Кризисные ивенты - единственный контент сценариев, который видит игрок, и они никогда не называют арку. Опции ультиматума - эталонная анатомия везде: **submit 30%** (war support -0.10, агрессору +0.05) и **defy 70%** (war support +0.10, агрессору +0.05 и `$sandbox_add_rivalry_vs(PREV, 15)`). Поздний генератор выпустил арки 16-28 отзеркаленными (submit 70% без rivalry-пуша), что фактически залочило эти арки в мир (s13: арка 16 на peak, оба ультиматума стрельнули, обе цели submitted); все 13 восстановлены к эталону. Арки 16-28 делят один ивент на обе variant-цели, так что их rivalry использует `PREV` (получателя ивента), а не литеральный тег.

**Flips** (только арки 5-6, без новой механики): директор толкает флип только существующими focus-весами. Если агрессор не флипнулся к фазе crises, арка дерайлится (и перевыбирается на random). Почти нулевой flip rate в логах - измеренный факт для v3 flip-рычагов, а не догадка под префикс. Гейт - два макроса (`$sandbox_check_flip_gate1` одна идеология, `$sandbox_check_flip_gate2` две для imperial neutrality-OR-fascism) плюс `$sandbox_check_flip_gate_inv` для пост-флип арок; сплит по арности, потому что параметры макросов текстово подставляются и один макрос с неиспользуемым слотом идеологии эмитил бы `has_government = 0` (s12 error.log).

### Lifecycle - RU

Одна арка на сессию. Арка кончается на ignition: в момент выстрела ее войны лестница сворачивается в поддержку и директор переходит на легкий join-саппорт (join-рычаги теплые, новых кризисов нет, новых фаз нет). Ignition симметричен: война в любую сторону между declared scenario enemies (агрессор атакует цель или цель атакует агрессора) кончает арку. Детектируется двумя путями, потому что война между двумя тегами - не всегда прямое объявление: `on_declare_war` ловит прямой случай, а месячный тик ловит любую идущую войну между агрессором и выбранной целью (`sandbox_scenario_check_ignite_by_war` -> `sandbox_ignite_if_at_war`). Путь тика закрывает s13-гэп: Axis против Britain в той сессии пришли через cascade призывов (отзывы гарантий плюс dominion `call_to_arms`), так что `declare_war` между GER и ENG ни разу не стрельнул и арка висела на peak посреди живой войны. Ignition логирует `sc_ignite` + `sc_success` + `sc_end` (маркер `sc_success` делает успешную арку грепабельной саму по себе).

Derail-политика: abort и repick на random, abort и конец на пине. Арка дерайлится, когда больше не может стрельнуть: агрессор больше не существует, капитулировал, бросил идеологию арки (Axis: Германия больше не фашистская; Soviet: Россия больше не коммунистическая; Japanese: Япония демократическая или коммунистическая; Italian: Италия больше не фашистская; flip-арки: Англия / Америка не флипнуты к crises), либо жизнеспособных целей не осталось (каждая цель gone, субъект агрессора или сидит в его фракции - нейтрализованная цель никогда не будет воевать со сюзереном или блоком). "Фракция агрессора" резолвится против тега агрессора арки явно, а не против скопа директора (`THIS`): цель, стартующая в чужой фракции цели (Rt56 кладет Монголию в советскую фракцию, что дерайлило Arc 13 на первом ходу в s12) - не нейтрализована. Четвертая рука покрывает **затяжную гражданскую войну**: агрессор, сидящий в гражданской войне 12 месяцев подряд, дерайлится (`aggressor_civil_war`), потому что страна, воюющая сама с собой, не может вести арку (s15: США просидели месяцы на peak в гражданской войне, теряя дивизии и фабрики, и так и не зажглись). Счетчик сбрасывается когда война кончается и на pick/repick. Пятая рука - **peak timeout**: арка, продержавшаяся на peak 12 месяцев без ignition, дерайлится (`peak_timeout`), потому что другого выхода у лестницы нет и зависшая арка сидела бы там вечно (итальянская арка ванильного порта парковалась на peak на шесть лет). Ее счетчик сбрасывается на pick/repick. Затем логируются `sc_derail` и `sc_end`. На random директор перевыбирает следующую подходящую никогда не дерайлившуюся арку (`sc_repick` + новый `sc_pick`); на пине тихо гаснет: никаких `sc_phase` и сценарных кризисов дальше. Гарантия из "Design goals" требует именно этого: мертвая арка не должна означать тихую сессию (на random).

### Plausibility - RU

Исторические арки (Axis expansion) и could-have-happened арки (communist America, fascist Britain). Планка "plausible": читатель арки должен уметь сказать, какое реальное напряжение 1930-х она продолжает. Шут-арки - отдельный будущий пак, никогда не мешаемый в пул v1.

### Per-mod content - RU

Общее: директорский тик, движок лестницы, рычаговые макросы, селекция, логирование. Пер-модное: теги акторов, id фокусов и ивентов, кризисные ивенты, локализация.

- v1: Rt56 Axis-арка (паркована Sep 2026 как good enough; история s3-s7 в чеклисте).
- v2: еще пять арок на Rt56, от легких к сложным: Soviet, Japanese, Italian, Fascist Britain, Red America. Каждая новая арка шипается без новой механики, макросов и хуков (ревью-чек на дифф арки); если какой-то понадобились - неправа схема: чинить схему, не копить пер-арочный код. Все пять v2-арок implemented (Soviet, Japanese, Italian, Fascist Britain, Red America). Arc 7 (Napoleonic France) закрывает последнего классического мажора, а Arc 8 (Habsburg restoration) - event-driven арка ведомого минора (Венгрия восстанавливает Двуединую монархию), добавленная по запросу; обе тоже шипнуты без новой механики. Арки 9-15 (расширенный каталог: GER Atlantic, GER Middle East, SOV South, SOV East, JAP North, JAP Old Oppressors, ITA West) дальше обобщают таргет-систему: каждая арка теперь роллит A/B target variant на пике и читает все сиды, кризисы, ультиматумы, derail-чеки и телеметрию из общего массива `sandbox_targets[]` плюс `sandbox_target_variant`. Пул теперь пятнадцать арок, все implemented на Rt56 без новой механики (target-variant система - тот же движок, обобщенный).
- Затем: ванильный порт пула (тот же движок, только content-portable арки; см. `docs/adr/0001-full-scenario-engine-in-vanilla-port.md`).

### Hooks and telemetry - RU

- Tick: `on_startup` (selection) плюс `on_weekly` / `on_monthly` в `common/on_actions/99_sandbox_on_actions.hsl`, рядом с civil-war ретраем и месячным census. `on_monthly` идет по странам, так что ladder tick должен стрелять ровно в одном хосте в месяц: он идет цепочкой хостов (GER, затем SOV, JAP, ITA, ENG, USA, FRA, HUN, каждый только если ранние хосты gone). HAI был изначальным единственным хостом; удаленный минор молча морозил каждую арку (s12), так что цепочка гарантирует, что директор переживает потерю любой single страны.
- Reactions: `on_declare_war` (ignition и join-детект), `on_capitulation` / `on_annex` (derail-детект), `on_join_allies` / `on_join_faction` (joiner-трекинг).
- Telemetry зеркалит `cw_`-конвенции: `sc_pick`, `sc_variant`, `sc_seed`, `sc_phase`, `sc_crisis`, `sc_target`, `sc_power`, `sc_goal`, `sc_justify`, `sc_goal_end`, `sc_focus`, `sc_offer`, `sc_ignite`, `sc_success`, `sc_join`, `sc_end`, `sc_derail`, `sc_repick`. На пике (и репике) директор роллит A/B target variant и логирует его отдельной строкой `sc_variant a|b` сразу после `sc_pick` (сама выбранная пара фиксирована массивом `sandbox_targets[]`); сидинг затем логирует `sc_seed` с выбранными целями (`t0`/`t1`/`t2`) из скопа агрессора. На peak каждая цель арки логирует одну статус-строку `sc_target` (`at_war` / `civil_war` / `subject` / `in_faction` / `open`, или `<tag>_gone` когда тег missing), чтобы молчаливая ultimatum-рука оставалась диагнозируемой; generic макрос `$sandbox_log_target_status(AGG)` покрывает арки 9-28 (арки 1-8 держат свои пер-арочные логгеры). Ветки scenario war-фокусов логируют `sc_focus` по завершении (ветка Arc 2 сплайснута, 6 фокусов; Arc 3 сплайснута, 2 фокуса; Arc 4 сплайснута, 2 фокуса; Arc 5 сплайснута, 3 фокуса; Arc 6 сплайснута, 4 фокуса; Arc 7 сплайснута, 6 фокусов вкл. Bonapartist chain; Arc 8 сплайснута, 4 фокуса; арки 9-15 сплайснуты, 5/5/6/3/3/2/2 фокусов соответственно, 26 total). s7 diagnostic package (read-only, behavior-neutral) пер-арочный: месячный `sc_power` (дивизии и фабрики на живого актора арки), месячный `sc_goal` (держимые варголы и активные justifications между агрессором и целями, только positives), месячный `sc_justify` (агрессор justifying на цель), `sc_goal_end` (варгол актора арки истек неиспользованным). Cadence rule: повторяющееся состояние сэмплируется monthly (`sc_power`, `sc_goal`, `sc_justify`); переход логируется когда случается (`sc_goal_end` на истечении варгола). Телеметрийные функции общие с одной рукой на арку (schema-shaped, без пер-арочных файлов телеметрии). Репик логирует цепочку `sc_derail` + `sc_end` + `sc_repick` + новый `sc_pick`. Census-страны (`is_sandbox_census_country()`) несут то же покрытие, что остальные системы.

**Telemetry label convention**: `sc_goal` и `sc_justify` несут по одной метке на пару агрессор/цель, всегда `<aggressor>_on_<target>` в **lowercase** (`ger_on_cze`, `hun_on_rom`). Каталог пишет оба набора меток руками в s7-телеметрии. Оба должны совпадать точно, иначе одна арка читается как два ключа при грепе сессии. `sc_goal` логирует варголы в **обе** стороны, так что держит и `<target>_on_<aggressor>`-метки (`cze_on_ger`); `sc_justify` покрывает только justifications агрессора. Каждый тег цели в метке должен быть реальным тегом, который сидит арка (`sandbox_set_targets`) - Румыния это `ROM`, никогда `ROU`.

## Arc 1: Axis expansion (v1, parked) - RU

Историческая. Агрессор: GER (derail если больше не фашистская). Joiners: open-pool top-2 на peak ("Join levers"). Цели: CZE, POL. Bloc: Axis. Лестница: шаблонный календарь (smolder 36.1.1 / crises 37.1.1 / peak 38.1.1). Кризисный контент: рейнское remilitarisation-давление, судетские claims, ультиматумы на peak. Паркована Sep 2026 как good enough (играет неидеально, история s3-s7 в чеклисте); пер-мод `content_refs` несут ванильные focus/event id и Rt56 отдельно.

## Arc 2: Soviet expansion (v2 first) - RU

Историческая. Агрессор: SOV (derail если больше не communist). Joiners: open-pool top-2, тот же скорер. Цели: POL, FIN (раздел Польши, Зимняя война). Bloc: Comintern. Лестница: шаблонный календарь. Кризисный контент зеркалит Axis-анатомию с советским flavor: claims Восточной Польши и Карелии/Петсамо плюс border incidents в crises, ультиматумы Варшаве и Хельсинки на peak. Числа рычагов - Axis-значения.

## Arc 3: Japanese expansion (v2 second) - RU

Историческая. Агрессор: JAP (derail если democratic или communist - Япония стартует на non-aligned правительстве, так что neutrality и fascism оба живы). Joiners: open-pool top-2, тот же скорер. Цели: CHI, PHI (Мост Марко Поло; удар по Филиппинам каскадит в США через марионетку и доставляет большую войну). Bloc: Co-Prosperity. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. Кризисный контент зеркалит остальные арки с японским flavor: China incident в crises, ультиматумы Нанкину и Маниле на peak. War-focus ветка: `JAP_reinforce_the_beijing_garrison` (Китай) и `JAP_strike_the_southern_road` (юг); `$ai_scenario_focus_boost()` сидит и на корнях ветки `JAP_revisit_the_thirteen_demands` и `JAP_occupy_siam`, так что буст достижим еще до war-фокусов (урок s10: буст за небустнутой развилкой мертв).

## Arc 4: Italian expansion (v2 third) - RU

Историческая. Агрессор: ITA (derail если больше не фашистская - Италия стартует фашистской; neutrality/democracy/communism все вне арки). Joiners: open-pool top-2, тот же скорер. Цели: YUG, GRE (исторические claims; Албания-39 / Греция-40 идут позже Судет). Bloc: Mare Nostrum. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. Кризисный контент зеркалит остальные арки с итальянским flavor: Адриатический инцидент в crises, ультиматумы Белграду и Афинам на peak. War-focus ветка: `ITA_italys_destiny` (балканские puppet-варголы, вкл. YUG и GRE) и `ITA_war_with_greece`; `$ai_scenario_focus_boost()` сидит и на корнях ветки `ITA_foreign_affairs`, `ITA_balkan_ambition` и `ITA_ratify_the_stresa_front`, так что буст достижим впереди war-фокусов (урок Arc 3). `sc_focus` сплайсы: `ITA_italys_destiny`, `ITA_war_with_greece`.

## Arc 5: Fascist Britain (v2 fourth) - RU

Plausible. Агрессор: ENG (derail если не фашистская к фазе crises; флип толкается только focus-весами). Joiners: open-pool top-2, тот же скорер. Цели: FRA, SOV (разрыв Антанты, антикоммунистический крестовый поход). Bloc: New Empire. Лестница: smolder 36.1.1 / crises 37.1.1 / peak 38.6.1. Кризисный контент зеркалит остальные арки с британским flavor: New Order incident в crises, ультиматумы Парижу и Москве на peak. Flip-ветка: `ENG_a_change_in_course` ее коренит; `$ai_scenario_focus_boost()` сидит на `ENG_a_change_in_course` и `ENG_organize_the_blackshirts`, чтобы flip-ветка выигрывала развилку (урок s10). War-focus ветка: `ENG_war_france` и `ENG_war_with_ussr` (плюс корни `ENG_burn_french` и `ENG_embargo_ussr`), все с бустом. `sc_focus` сплайсы: flip `ENG_organize_the_blackshirts` и два war-фокуса.

## Arc 6: Red America (v2 fifth, flip validation) - RU

Plausible. Агрессор: USA (derail если не communist к фазе crises; флип толкается только focus-весами). Joiners: open-pool top-2, тот же скорер - СССР emergent joiner (та же ideology group проходит гейт, советская сила почти гарантирует топ-2 письмо), а не гарантированный союзник. Цели: CAN, JAP (оба полушария: Канада тянет Англию через доминион, Япония продолжает тихоокеанское rivalry под красным флагом). Bloc: People's Internationale. Лестница: smolder 36.1.1 / crises 37.1.1 / peak 38.6.1. Кризисный контент зеркалит остальные арки с американским flavor: World Revolution incident в crises, ультиматумы Оттаве и Токио на peak. Flip-ветка: коммунистический путь коренится в `USA_continue_the_new_deal`; `$ai_scenario_focus_boost()` сидит на `USA_continue_the_new_deal` и flip-корне `USA_suspend_the_presecution`, чтобы красная ветка выигрывала свою развилку (урок s10). War-focus ветка: `USA_end_monarchism`, `USA_shatter_the_empires` и `USA_us_ussr_economic_cooperation` (SOV-cooperation фокус работает и как joiner-приманка), все с бустом. `sc_focus` сплайсы: flip-корень и три war-фокуса. Если этой арке понадобится новая механика - неправа схема: чинить схему, не копить пер-арочный код (не понадобилась - flip-валидация и есть доказательство).

## Arc 7: Napoleonic France (v2 sixth) - RU

Историческая. Агрессор: FRA (без ideology arm - Франция доходит до бонапартистской ветки из демократического или нейтрального правительства, так что только gone/capitulated/targets derail). Последний из мажоров. Joiners: open-pool top-2, тот же скорер. Цели: GER, ITA (Рейн и Альпы: Франция восстанавливает Континентальную систему, ломает Германию и возвращает Савойю/Ниццу). Bloc: Continental System. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1 (поздно, как остальные поздне-балканские арки - Франции нужно время найти бонапартистскую ветку). Кризисный контент зеркалит остальные арки с французским flavor: Рейнский вопрос в crises, ультиматумы Берлину и Риму на peak. War-focus ветка: корень Континентальной системы `FRA_the_new_continental_system`; `$ai_scenario_focus_boost()` сидит на нем, на `FRA_crush_germany` (puppet-варголы на GER и Пруссию), на `FRA_nothern_italy_claim` (Италия), **и на всей бонапартистской цепочке** - `FRA_action_francaise`, `FRA_papal_rehabilitation`, `FRA_repeal_the_law_of_exile`, `FRA_brumaire_movement` - потому что в Rt56 бонапартистская ветка спрятана за этими фокусами (mutually-exclusive со status-quo/radicalize/far-right), так что ранняя версия с бустом только на войнах никогда не стреляла (s11: FRA пошла status-quo, ноль `sc_focus`, ноль варголов к t=24). `sc_focus` сплайсы: цепочка (4) + корень Континентальной системы + два war-фокуса. Французский flavor: агрессия реваншистско-имперская, не идеологическая - без флипа, без идеологического derail.

## Arc 8: Habsburg restoration (v2 seventh) - RU

Историческая. Агрессор: HUN (Венгрия; derail когда Венгрия gone, капитулировала, обе цели нейтрализованы или - flip-style гейт - Венгрия так и не встала на restoration-путь). Цели: CZE, ROU (исторические коронные земли: Богемия/Моравия и Трансильвания). Joiners: open-pool top-2, тот же скорер (австро-венгерский crown tier тянет дунайских миноров). Bloc: Danubian Empire. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1 (поздно - Венгрии нужно сначала найти restoration-ветку). Hungerian flavor: реваншистское Регентство. "Restoration gate" заменяет ideology arm: Венгрия должна завершить `HUN_proclaim_the_restoration_of_austria_hungary` (или путь take-Austria-by-force) к фазе crises, иначе арка дерайлится - отдельный Dual Monarchy-тег директор не создает (Rt56 образует Австро-Венгрию аннексией Австрии в Венгрию, так что агрессор - сама Венгрия). Кризисный контент зеркалит остальные арки: Габсбургский вопрос в crises, ультиматумы Праге и Бухаресту на peak. War-focus ветка: restoration-корень `HUN_proclaim_the_restoration_of_austria_hungary` плюс claims `HUN_claim_transylvania`, `HUN_march_to_the_shore`, `HUN_claim_galicia`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 9: German Atlantic (v3 catalog) - RU

Историческая. Агрессор: GER (derail если больше не фашистская). Joiners: open-pool top-2, тот же скорер. Variant targets: A = ENG, B = USA (морской вопрос: взломать англо-американское кольцо на волнах). Bloc: Atlantic. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. Кризисный контент зеркалит остальные арки с германским морским flavor: Атлантический вопрос в crises, ультиматумы первой цели A/B на peak. War-focus ветка: `GER_crossing_the_atlantic` и `GER_atlantic_naval_bases`, обе с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 10: German Middle East (v3 catalog) - RU

Историческая. Агрессор: GER (derail если больше не фашистская). Joiners: open-pool top-2, тот же скорер. Variant targets: A = SOV, B = IRQ, PER (восточный вопрос: рывок к нефти и Востоку). Bloc: Eastern. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `GER_influence_the_middle_east`, `GER_claim_old_colonies_in_the_east` и `GER_wage_war_on_capitalism`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 11: Soviet South (v3 catalog) - RU

Историческая. Агрессор: SOV (derail если больше не communist). Joiners: open-pool top-2, тот же скорер. Variant targets: A = TUR, IRQ, PER, B = PAK, RAJ, AFG (южный thrust: теплые моря и индийский фронтир). Bloc: Southern. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `SOV_the_last_break_southward`, `SOV_preemptive_invasion_of_iran` и `SOV_into_the_plateau`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 12: Soviet East (v3 catalog) - RU

Историческая. Агрессор: SOV (derail если больше не communist). Joiners: open-pool top-2, тот же скорер. Variant targets: A = JAP, MAN, B = USA, CAN (восточный фронтир: расчет с Японией или trans-Pacific красный рывок). Bloc: Eastern. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `SOV_crush_our_eastern_rival`, `SOV_our_american_holding` и `SOV_restore_the_old_eastern_empire`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 13: Japanese North (v3 catalog) - RU

Историческая. Агрессор: JAP (derail если democratic или communist). Joiners: open-pool top-2, тот же скорер. Variant targets: A = SOV, MON, B = SOV, CHI (северный путь: hokushin-ron против Советского Союза и его сателлитов). Bloc: Northern. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `JAP_hokushin_ron`, `JAP_sea_establish_the_northern_resource_area` и `JAP_strike_the_soviets`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 14: Japanese Old Oppressors (v3 catalog) - RU

Историческая. Агрессор: JAP (derail если democratic или communist). Joiners: open-pool top-2, тот же скорер. Variant targets: A = USA, B = ENG (удар по старым угнетателям: взломать англо-американское кольцо). Bloc: Anti-Oppressor. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `JAP_strike_the_old_oppressors` и `JAP_ultimate_deterrence`, обе с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 15: Italian West (v3 catalog) - RU

Историческая. Агрессор: ITA (derail если больше не фашистская). Joiners: open-pool top-2, тот же скорер. Variant targets: A = FRA, B = ENG (западный враг: mastery западного Средиземноморья против Франции или Англии). Bloc: Western. Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `ITA_war_with_france`, `ITA_war_with_the_uk` и `ITA_demand_ticino`, все с `$ai_scenario_focus_boost()` и `sc_focus`. Audit-фикс Sep 2026: арка 15 отсутствовала в `sandbox_set_targets`, derail-диспетчере, `sandbox_seed_actors` и двух `on_actions`-телеметрийных руках (copy-paste гэп в диапазоне 14->16); все четыре добавлены, так что арка теперь сидится, дерайлится и телеметрится как остальные.

## Arc 16: Italian Mediterranean Empire (v4 catalog) - RU

Историческая. Агрессор: ITA (derail если больше не фашистская). Joiners: open-pool top-2. Variant targets: A = TUR, ROM, B = FRA, ENG (восстановить Римское море от Анатолии до запада). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `ITA_a_time_for_war`, `ITA_claims_on_turkey_bba`, `ITA_all_roads_lead_to_rome`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 17: British Imperial Restoration (v4 catalog) - RU

Imperial (gate: neutrality OR fascism к crises; derail `britain_not_imperial`). Агрессор: ENG. Variant targets: A = RAJ, B = USA, JAP (воссоединить Империю под Короной). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `ENG_reclaim_the_jewel_in_the_crown`, `ENG_bring_the_dominions_back_into_the_fold`, `ENG_unite_the_anglosphere`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 18: American War Plan (v4 catalog) - RU

Историческая. Агрессор: USA. Variant targets: A = JAP, B = ENG, CAN (war plans: Тихий против Японии, Атлантика против entente). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `USA_war_plan_orange`, `USA_war_plan_black`, `USA_defense_of_the_pacific`, `USA_intervention_in_europe`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 19: American Global Hegemony (v4 catalog) - RU

Историческая (без flip gate). Агрессор: USA. Variant targets: A = ENG, GER, HUN, JAP (старый имперский порядок), B = ENG, FRA (открытый вызов). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `USA_global_hegemony` (плюс уже бустнутые `USA_end_monarchism` / `USA_shatter_the_empires`), все с `$ai_scenario_focus_boost()` и `sc_focus`. Вариант A использует 4-target derail arm.

## Arc 20: French Monarchist Revival (v4 catalog) - RU

Imperial (gate: neutrality к crises; derail `france_not_neutral`). Агрессор: FRA. Variant targets: A = SPR, ADR, MEX (латинский союз), B = SOV (второй поход на Москву). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `FRA_secure_the_crown_of_spain`, `FRA_claim_the_andorran_throne`, `FRA_restore_the_mexican_monarchy`, `FRA_second_march_on_moscow`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 21: French Revenge (v4 catalog) - RU

Историческая. Агрессор: FRA. Variant targets: A = GER (partition), B = ENG (destroy Albion). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `FRA_dismantle_germany`, `FRA_crush_germany` (already boosted), `FRA_destroy_albion`, `FRA_strike_empire`, все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 22: French Plan XIV (v4 catalog) - RU

Историческая. Агрессор: FRA. Variant targets: A = SWI, B = ITA (нейтральная граница, Plan XIV). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `FRA_plan_xiv`, `FRA_return_to_dalmatia`, `FRA_nothern_italy_claim` (already boosted), все с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 23: Communist Germany (v4 catalog) - RU

Flip (gate: communism к crises; derail `germany_not_communist`). Агрессор: GER. Variant targets: A = ENG, FRA, ITA (мировая революция на запад), B = SOV, USA, JAP (на восток). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `GER_root_out_imperialism`, `GER_hegemony_over_europe`, `GER_wage_war_on_capitalism` (already boosted), `GER_strike_at_the_rising_sun`, с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 24: Monarchist Germany (v4 catalog) - RU

Flip (gate: neutrality к crises; derail `germany_not_neutral`). Агрессор: GER. Variant targets: A = SOV, DEN, B = VEN, FRA (реставрация Kaiserreich). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `GER_soviet_invasion`, `GER_restore_klein_venedig` (фокус требования северного Шлезвига в Rt56 отсутствует и скипается), с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 25: White Russia (v4 catalog) - RU

Flip (gate: SOV NOT communist к crises; derail `soviet_not_communist`, inverted gate). Агрессор: SOV (пост-гражданская белая Россия). Variant targets: A = GER, POL, FIN, B = UKR (восстановленные имперские границы). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `SOV_beaten_but_not_defeated` (already boosted), `SOV_white_exiles`, `SOV_imperial_legacy` (already boosted), `SOV_strike_the_eagle`, с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 26: Communist Japan (v4 catalog) - RU

Flip (gate: communism к crises; derail `japan_not_communist`). Агрессор: JAP. Variant targets: A = CHI, SOV, B = ENG, USA, SIA (паназиатская революция). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `JAP_put_an_end_to_chinese_feudalism`, `JAP_spread_the_revolutuon_south`, `JAP_free_asians_from_soviet_opression`, `JAP_go_after_the_capitalists`, с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 27: Communist Italy (v4 catalog) - RU

Flip (gate: communism к crises; derail `italy_not_communist`). Агрессор: ITA. Variant targets: A = FRA, ENG, B = BUL, YUG (красная революция на Западе или Балканах). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `ITA_pugno_alzato`, `ITA_the_enemies_of_capitalism`, `ITA_liberate_the_workers_of_africa`, с `$ai_scenario_focus_boost()` и `sc_focus`.

## Arc 28: Communist Britain (v4 catalog) - RU

Flip (gate: communism к crises; derail `britain_not_communist`). Агрессор: ENG. Variant targets: A = GER, USA, CAN, B = SOV (мировая революция под красным флагом). Лестница: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus ветка: `ENG_soviet_cooperation`, `ENG_the_one_true_revolution`, `ENG_liberate_the_home_of_marx`, `ENG_liberate_the_american_workers`, с `$ai_scenario_focus_boost()` и `sc_focus`.

## Acceptance checklist - RU

Log-first. Observer sandbox. Tick only when the grep holds (same discipline as `docs/gdd/Civil Wars.md`).

- [x] Startup: exactly one `sc_pick` naming one pool arc; no UI, event, or tooltip names the picked scenario (the game-rule options may list the pool; `game.log` is out of band).
- [x] Ladder phases logged on the picked arc's schedule in an idle observer session: `sc_phase smolder`, then `crises`, then `peak`; each rung once.
- [x] Aggressor rivalry vs targets seeded and rising for the picked arc (`sc_seed`, then `rivals_set` / Feud bands); Feud reached before peak.
- [ ] Pooled war bar: 5 random-pick observer sessions, `sc_ignite`-only from any arc by 1940 (post-repick ignitions count; non-scenario cascades do not). 4 of 5 must ignite. No scripted declaration exists in scenario files (review check, not a grep). Axis history (pre-pool window, kept for reference): s3/s4 ignited inverted (direction settled Sep 2026: inverted counts), s5 no scenario war by Oct 1939 (CZE puppeted by GER Feb 1938, POL ultimatum arm did not fire with POL alive - human-popup cause excluded, observer started on Ireland; civil-war tag-gap likely, TBD via target-status telemetry, GER fought only non-scenario wars); s6 QUIET (FAIL): no scenario war by Feb 1940 despite a perfect peak (sc_target open x2, both ultimatums fired, CHI+JAP joined); CZE alive at rivalry 100 for 25+ months, GER fought only non-scenario wars (FRA+X, then intermittent minors). Running 2/4 (s3/s4 inverted-ignited, s5/s6 quiet) - the 4-of-5 bar cannot pass on this window; counting decision Sep 2026: NEW SERIES from s7 (need 4/5 with fixes); s3-s6 kept as history. s7 QUIET (new series 0/1): no `sc_ignite` by Apr 1940; CZE neutralized pre-peak (Axis faction Aug 1937, GER subject by Jan 1938 - second puppet in a row after s5); POL open + rivalry 100 from Feb 1938 + defied ultimatum, never justified (`sc_justify`=0, `sc_goal`=0 across 51 months incl. 13 peaceful months with CZE:100 at 27 divs vs GER 67-106 - deterrence excluded); GER declared on USA (Jul 1938, distant random rival) instead and collected faction co-belligerencies (ITA Feb 1938, BEL, CHI, SAN, D15, CHL); the session still had a big non-scenario war (Axis vs ENG from Feb-Mar 1938) via cascade - the ambient goal was met by accident while the arc parked at peak 27 months.
- [ ] Per-arc gates: each new arc passes 3 pinned observer sessions with 2 of 3 `sc_ignite` by 1940 before the next arc starts. Soviet 0/2 (s8 QUIET: no `sc_ignite` by Oct 1944; SOV never justified on anyone in 105 months despite Feud 100 vs POL/FIN, Honor exemption, 232 div / 179 fab at Jan 1940 vs POL 81/61; FIN vanished Dec 1939 with no war/CW telemetry - likely Rt56 native content; SOV took a D08 civil-war split Jul 1941 and sat as a 240/16 rump; POL open all session, defied ultimatum, never attacked. s9 QUIET with the F1+F4 fixes active: ladder + peak all fired, JAP+ENG offered, JAP joined; zero `sc_focus` - SOV completed `SOV_the_path_of_marxism_leninism` (Mar 1936) again, so the whole white/imperial branch with the war focuses was unreachable; the x5 `beaten_but_not_defeated` boost lost the fork to the Stalinist branch's baseline `add(40)` + `communism_factor*2`; derail trigger left for later) Japanese 0/0 (implemented; not yet observed) Italian 0/0 (implemented; not yet observed) Fascist Britain 0/0 (implemented; not yet observed) Red America 0/0 (implemented; not yet observed) Napoleonic France 0/0 (implemented; not yet observed) Habsburg restoration 0/0 (implemented; not yet observed) GER Atlantic 0/0 (implemented; not yet observed) GER Middle East 0/0 (implemented; not yet observed) SOV South 0/0 (implemented; not yet observed) SOV East 0/0 (implemented; not yet observed) JAP North 0/0 (implemented; not yet observed) JAP Old Oppressors 0/0 (implemented; not yet observed) ITA West 0/0 (implemented; not yet observed) Arcs 16-28 0/0 per arc (implemented; not yet observed).
- [x] Joiners: one shared scorer, at most two `sc_offer` letters per arc at peak, and `sc_join` for each joiner before ignition or within 6 months after (faction, guarantee answered, or call to arms). Offer gates (enemy ideology, self, human, civil war, at-war, own faction, subject) are present in the scorer (review check, not a grep). (s5: offers to CHI + ROM, ROM faction-joined same tick, fought for the bloc Nov 1938; both recipients neutral/monarchist per observer; s7: offers CHI + ITA, both faction-joined same tick. Industry leg of the scorer was silently zero in s5-s7 (invalid `num_factories` token, always read 0 - fixed to `num_of_factories` after s7; s7 joins ran on divisions + opinion only); s8: offers FRA + SIK, SIK faction-joined same tick, FRA refused (no sc_join) - a microstate winning a top-2 slot shows the non-hostile gate empties the major pool for a communist aggressor (all democratic/fascist majors score 0).)
- [x] Derail: a dead arc (aggressor gone, capitulated, or off-ideology; no viable target remains - gone, subject of the aggressor, or in its faction) logs `sc_derail` + `sc_end` and either goes quiet when pinned (no further `sc_phase` or scenario crises) or repicks on random (next item). (Neutralized-target arm added Sep 2026; s7 partial test: single neutralization (CZE subject, POL viable) correctly did NOT derail - the arc held peak; s8: single FIN loss (vanished Dec 1939) correctly did NOT derail - POL viable, the arc held peak; s10: the both-gone arm finally fired - POL and FIN were annexed by third countries mid-1938 (no wars with SOV, no `cw_ignition` for either), arc derailed Jan 1939 `targets_gone`, pinned so it went quiet.)
- [ ] Repick: a derail on random logs `sc_derail` + `sc_end` + `sc_repick` + a new `sc_pick`, and the next eligible never-derailed arc runs its ladder from smolder; a derailed arc never re-enters the pool in the session.
- [x] One arc per session: never two `sc_pick` lines without `sc_end` or `sc_derail` between them.
- [x] After ignition: `sc_end`, no further `sc_phase` or scenario crises for that arc; join support may continue (`sc_join` allowed).
- [x] Game-rule pin: the pinned scenario runs and never repicks (s5+s6+s7 ran pinned Axis, s8 ran pinned Soviet with ladder + crises + offers all firing; pin options grow with implemented arcs).
- [ ] No-new-mechanics per arc: each v2 arc ships with no new mechanics, macros, or hooks (review check per arc diff). Soviet [ ] Japanese [x] Italian [x] Fascist Britain [x] Red America [x] Napoleonic France [x] Habsburg restoration [x] Arcs 9-15 [x] Arcs 16-28 [x] (the target-variant system and the generic flip/imperial gates are the same engine generalized; the 4-target derail arm is the same arm extended, no new mechanic). Each arc reuses the shared seed/join/tick/derail/telemetry engine and the shared `$ai_scenario_focus_boost()`; per-arc content is actor tags, crises + ultimatums, game-rule option, and focus splices (Arc 8's "restoration gate" is a flavor-renamed version of the flip gate, no new code path; arcs 17/20/23/24/25/26/27/28 use the shared `$sandbox_check_flip_gate` / `$sandbox_check_flip_gate_inv`).
- [x] No `error.log` lines attributable to scenario files (`99_sandbox_scenario*`, scenario crisis events). (s7: 4219 lines, zero sandbox/scenario refs - all vanilla/Rt56 load and UI noise; s8: zero sandbox/scenario refs.)
- [x] Civil wars unaffected: scenario wars are international and never move the civil-war counter; `cw_` logging in scenario sessions shows no scenario-attributed lines.

## Out of scope for this iteration - RU

- Scripted declarations of war by the director, under any name (fuses, deadlines, forced DOWs).
- Flip-assist levers for v2: arcs 5-6 flip through focus weights only (a near-zero flip rate in logs is the measured case for v3).
- Joke arcs and mixed plausibility pools.
- Player-facing scenario UI beyond the pinning game rule.
- Concurrent arcs (revisit after the v2 pool proves the single-arc loop).
- Scenario behaviour in historical mode: everything here is sandbox-only.
- Vanilla port mechanics changes: the port carries the whole engine and differs only in focus/event ids and pool composition (content-portable arcs only); see `docs/adr/0001-full-scenario-engine-in-vanilla-port.md`.
- News events and notifications about director actions (the player sees crises, not the director).