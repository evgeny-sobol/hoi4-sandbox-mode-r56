# Scenarios

A scenario is a full-session crisis arc run by a **director**: a background system that picks one plausible conflict at startup and pushes the AI toward it with bonuses and scripted crises until a big war fires. The war is the point. Some sessions the player joins it; some sessions they sit it out; no session is quiet.

Scenarios are **not**:
- Scripted declarations of war. The director never declares war itself and never calls `start_civil_war`; it only changes weights, rivalry, Honor exposure, and fires crisis events. The AI pulls the trigger.
- A railroader. There are no fixed dates for declarations, no forced peace deals, no teleporting divisions.
- A player-targeting system. The challenge is ambient: the war is somewhere in the world, not aimed at the player's tag.
- Civil wars (`gdd/Civil Wars.md`). Scenario wars are international. The civil-war counter and cap are untouched by the director.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`. Historical mode is unchanged.

## Why this is needed

Observer sessions are boring: countries rarely start wars and even more rarely join each other. Diagnosis (GDDs plus sources, September 2026):

1. The historical engine of wars is gone with no replacement. All vanilla strategy plans abort in sandbox; war focuses weigh 40 like industry and are further cut by war support (about x0.5 in 1936). (`gdd/National Focuses.md`, "Basic modifiers"; `common/ai_strategy_plans/*.include`.)
2. Honor gates plus the betrayal weight block wars on friends: on startup most leaders cannot touch an ally, and honorable AI almost never takes a betrayal focus. (`gdd/Honor System.md`, "Gating betrayal focuses by band", "AI weighting".)
3. The Feud threshold: `conquer` / `prepare_for_war` plans exist only at `rivalry >= 75`, slots start at 50 and decay without fuel. (`gdd/Rivals System.md`, "AI strategies", "Rivalry changes".)
4. Fragmented alliances: rival-gated cooperation plus `alliance -200` means fewer factions and fewer cascades through call to arms, even though Honor pays for joining. (`gdd/Rivals System.md`, "National focuses"; `gdd/Honor System.md`, "Honor gains".)
5. False trail excluded: the civil-war cap does not touch international wars.

Fixing each gate in isolation restores noise, not drama. The director fixes the session shape instead: one picked conflict, escalated on a schedule, guaranteed in practice.

## Design goals

1. Every session has a big war. "Guaranteed" is delivered by an escalation ladder, not by forcing declarations.
2. The challenge is ambient: the scenario war is somewhere; the player may join or sit out.
3. Plausible arcs only: historical and could-have-happened. No joke arcs in v1.
4. The director uses bonuses and crises only. If a war cannot be earned with levers, the arc is wrong, not the rule.
5. Shared mechanics, per-mod content: one director engine, separate actor/event/focus ids for vanilla and Rt56.
6. Verifiable like civil wars: log-first acceptance on observer sessions (`#sandbox` telemetry).

## Model

### Arc (generator-ready schema)

Content is fixed authorial arcs, but every arc is written as data on one schema so a generator can later randomize over it. Proof of "generator-ready" is the second arc: if it needs new mechanics, fix the schema, not the arc.

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

### Selection

One arc per session, picked at startup by weighted random from eligible arcs. Eligibility is plausibility plus sanity (actors exist on the map). The pick is a surprise in-game: it is logged (`sc_pick`) but no UI, event, or tooltip names the picked arc. The pool itself is visible (the pinning game rule lists its options); `game.log` is out of band, same as `cw_` telemetry.

The v2 pool holds six arcs (Axis plus five new) with equal weights. A game rule pins a fixed scenario for replays and tests; pin options exist only for implemented arcs and grow with the pool. The pin overrides the random pick and means strict isolation: a pinned session never repicks (a derailed pin goes quiet). In random sessions a derail repicks the next eligible arc that has not derailed yet this session (`sc_derail` + `sc_repick` + a new `sc_pick`); a derailed arc never re-enters the pool in the same session. A repicked arc runs its ladder from smolder, compressed by the calendar (late repicks hit crises and peak on consecutive ticks).

### Escalation ladder

The ladder replaces forcing. Three phases for every arc (smolder / crises / peak), each rung firing once (the anti-spam rule). The ladder holds at peak until the war fires. There is no deadline fuse that declares war by script (see "Scenarios are not").

Dates are per arc (tuned to each arc's history); the Axis calendar is the template:

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

- **Smolder**: rivalry seeding for aggressors vs targets, Honor exemptions for scenario pairs, war-focus weights. Quiet buildup, no crises.
- **Crises**: scripted crisis events (claims, incidents), war-support pump, join levers for joiners. The world notices. Flip arcs (5-6) must have flipped by this phase or derail.
- **Peak**: ultimatums, maximum pressure. Every peak leaves 12-18 months before the pooled 1940 deadline.

### Levers

**Aggression** (addresses diagnosis 1-3):
- Rivalry seeding and injection toward Feud (`>= 75`) for aggressors vs targets, through the existing slot discipline (`$add_rivalry`, `set_rival`; `gdd/Rivals System.md`). At Feud the AI gets `conquer 100` / `prepare_for_war 100` and antagonism focuses weigh x3.
- Honor exemptions: each arc registers its declared scenario enemies at selection (a named pair list; representation is an implementation detail). War declarations between declared enemies skip the betrayal charge in `on_declare_war` and pass `can_PREV_get_wargoal_on_THIS`. This is a narrow, explicit carve-out: `gdd/Honor System.md` ("Honor losses") needs one line acknowledging the scenario exception. The exemption covers the gate and the weight alike: declared enemies pass `can_PREV_get_wargoal_on_THIS` and skip `$ai_betrayal_modifier_vs` (the weight half was missing until s8, when a day-1 SOV-FIN NAP zeroed the Soviet war-focus weight for all of 1936). Rivalry itself still never lowers betrayal cost.
- War support for actors, offsetting the systemic antagonism cut.
- Lever numbers are shared: every arc starts with the Axis values (seed 65, crisis injection +10, ultimatum-defy injection +15, war-support grants) and tunes only from observer logs. No armchair per-arc balancing.

**Focus weights** (addresses diagnosis 1): push actors toward their war focuses through the existing antagonism/rivalry modifiers. A scenario-specific boost is allowed only if Feud plus exemptions prove insufficient in logs. s8 and s9 were that case (Soviet QUIET: Feud 100, no `sc_focus` on the war branch). The boost is shared `$ai_scenario_focus_boost()` (x5, live aggressor only, ladder not ended) spliced onto the arc war-focus branch; Arc 2 uses `SOV_beaten_but_not_defeated` plus the six `sc_focus` ids. s10 verdict: the x5 fork boost lost to the Stalinist branch baseline (`factor(1)` + `add(40)` + `communism_factor*2` vs `5` + `(demo+mon+fasc)*2`); SOV re-ran `SOV_the_path_of_marxism_leninism`, all six boosted focuses stayed unreachable, zero `sc_focus`. Raising the fork boost (or retargeting the fork) is the open v2 question; boost value stays shared until logs say otherwise. Which focus branch each arc pushes is drawn as a Mermaid diagram per arc in `gdd/Scenarios Catalog.md` ("Focus paths per arc"; generated from `gdd/National Focuses/*.md`).

**Join levers** (addresses diagnosis 4): at peak, the two highest-scoring countries in an open pool get a faction invitation (`scenario_join_scorer`, top-2, one letter each, `sc_offer` per letter). One scorer for all arcs, no per-arc parameters and no guaranteed flavor joiners. No fixed tag list: eligibility is gated, not curated. A candidate scores zero (is skipped) if it is the aggressor, is human-ruled, is in a civil war, is at war with the aggressor, already sits in the aggressor's faction, is the aggressor's subject or overlord, or holds an enemy ideology toward the aggressor (`has_enemy_ideology`: same group or non-aligned on either side passes). Faction membership elsewhere is not a bar: a joiner that accepts leaves its old faction first (leave-then-join; a joiner that leads its own faction leaves it and leadership passes by game rules) and the exit carries no Honor charge (one-shot `sandbox_honor_skip_leave_faction`, same as a released nation). The score is strength plus goodwill in three staircases (thresholds stack; maxima 60/60/60, tunable): divisions (>10/+5, >30/+10, >60/+15, >100/+15, >150/+15), industry as total `num_factories` (>10/+10, >25/+15, >50/+20, >80/+15, snapshotted into `scenario_join_industry` before scoring), opinion toward the aggressor (>25/+10, >50/+20, >75/+30, <0/-10, <-50/-20). The bloc keeps its arc name (Axis, Comintern, Co-Prosperity, Mare Nostrum, New Empire, People's Internationale); post-join ideology flips are not tracked (once in, in).

**Crises**: scripted events per phase (claims, border incidents, ultimatums) that create cores, tension, and war support. Same anatomy for every arc: claims plus incidents in crises, ultimatums at peak. Crisis events are the only scenario content the player sees, and they never name the arc.

**Flips** (arcs 5-6 only, no new mechanics): the director pushes the flip through existing focus weights only. If the aggressor has not flipped by the crises phase, the arc derails (and repicks on random). A near-zero flip rate in logs is a measured fact for v3 flip levers, not a guess to pre-fix.

### Lifecycle

One arc per session. The arc ends at ignition: the moment its war fires, the ladder stands down and the director drops to light join support (join levers stay warm, no new crises, no new phases). Ignition is symmetric: a war in either direction between declared scenario enemies (the aggressor attacks the target, or the target attacks the aggressor) ends the arc.

Derail policy is abort and repick on random, abort and end when pinned. The arc is derailed when it can no longer fire: the aggressor no longer exists, capitulated, abandoned its arc ideology (Axis: Germany no longer fascist; Soviet: Russia no longer communist; Japanese: Japan democratic or communist; Italian: Italy no longer fascist; flip arcs: England / America not flipped by crises), or no viable target remains (each target is gone, is the aggressor's subject, or sits in the aggressor's faction - a neutralized target can never fight its overlord or bloc). Then `sc_derail` and `sc_end` are logged. On random the director repicks the next eligible never-derailed arc (`sc_repick` + a new `sc_pick`); when pinned it goes quiet: no further `sc_phase` or scenario crises. The guarantee in "Design goals" requires it: a dead arc must not mean a quiet session (on random).

### Plausibility

Historical arcs (Axis expansion) and could-have-happened arcs (communist America, fascist Britain). Bar for "plausible": a reader of the arc must be able to say which real 1930s tension it continues. Joke arcs are a separate future pack, never mixed into the v1 pool.

### Per-mod content

Shared: director tick, ladder engine, lever macros, selection, logging. Per mod: actor tags, focus and event ids, crisis events, localisation.

- v1: Rt56 Axis arc (parked Sep 2026 as good enough; history s3-s7 in the checklist).
- v2: five more arcs on Rt56, easy-to-hard: Soviet, Japanese, Italian, Fascist Britain, Red America. Each new arc ships with no new mechanics, macros, or hooks (review check per arc diff); if one needs any, the schema is wrong: fix the schema, do not accumulate per-arc code. All five v2 arcs are implemented (Soviet, Japanese, Italian, Fascist Britain, Red America). Arc 7 (Napoleonic France) covers the last classic major, and Arc 8 (Habsburg restoration) is the event-driven minor-led arc (Hungary restores the Dual Monarchy) added by request; both also shipped with no new mechanics. Arcs 9-15 (the extended catalog: GER Atlantic, GER Middle East, SOV South, SOV East, JAP North, JAP Old Oppressors, ITA West) generalize the target system further: every arc now rolls an A/B target variant at pick and reads all seeds, crises, ultimatums, derail checks, and telemetry from the shared `sandbox_targets[]` array plus `sandbox_target_variant`. The pool is now fifteen arcs, all implemented on Rt56 with no new mechanics (the target-variant system is the same engine, generalized).
- Then: vanilla port of the pool (content only, no mechanic changes).

### Hooks and telemetry

- Tick: `on_startup` (selection) plus `on_weekly` / `on_monthly` in `common/on_actions/99_sandbox_on_actions.hsl`, next to the civil-war retry and the monthly census.
- Reactions: `on_declare_war` (ignition and join detection), `on_capitulation` / `on_annex` (derail detection), `on_join_allies` / `on_join_faction` (joiner tracking).
- Telemetry mirrors the `cw_` conventions: `sc_pick`, `sc_variant`, `sc_phase`, `sc_seed`, `sc_crisis`, `sc_target`, `sc_power`, `sc_goal`, `sc_justify`, `sc_goal_end`, `sc_focus`, `sc_offer`, `sc_ignite`, `sc_join`, `sc_end`, `sc_derail`, `sc_repick`. At pick (and repick) the director rolls the A/B target variant and logs it as a separate `sc_variant a|b` line right after `sc_pick` (the picked pair itself is fixed by `sandbox_targets[]`). At peak each arc target logs one `sc_target` status line (`at_war` / `civil_war` / `subject` / `in_faction` / `open`, or `<tag>_gone` when the tag is missing), so a silent ultimatum arm stays diagnosable. Scenario war-focus branches log `sc_focus` on completion (Arc 2 branch spliced, 6 focuses; Arc 3 spliced, 2 focuses; Arc 4 spliced, 2 focuses; Arc 5 spliced, 3 focuses; Arc 6 spliced, 4 focuses; Arc 7 spliced, 6 focuses incl. the Bonapartist chain; Arc 8 spliced, 4 focuses; arcs 9-15 spliced, 5/5/6/3/3/2/2 focuses respectively, 26 in total). The s7 diagnostic package (read-only, behavior-neutral) is per-arc: monthly `sc_power` (divisions and factories per live arc actor), monthly `sc_goal` (held wargoals between the aggressor and its targets, positives only), daily `sc_justify` (aggressor justifying on a target), `sc_goal_end` (an arc actor's wargoal expired unused). Telemetry functions are shared with one arm per arc (schema-shaped, no per-arc telemetry files). A repick logs the chain `sc_derail` + `sc_end` + `sc_repick` + a new `sc_pick`. Census countries (`is_sandbox_census_country()`) carry the same coverage as other systems.

## Arc 1: Axis expansion (v1, parked)

Historical. Aggressor: GER (derail if no longer fascist). Joiners: open-pool top-2 at peak ("Join levers"). Targets: CZE, POL. Bloc: Axis. Ladder: the template calendar (smolder 36.1.1 / crises 37.1.1 / peak 38.1.1). Crisis content: Rhineland-style remilitarisation pressure, Sudeten-style claims, ultimatums at peak. Parked Sep 2026 as good enough (plays imperfectly, history s3-s7 in the checklist); per-mod `content_refs` carry the vanilla focus/event ids and the Rt56 ones separately.

## Arc 2: Soviet expansion (v2 first)

Historical. Aggressor: SOV (derail if no longer communist). Joiners: open-pool top-2, same scorer. Targets: POL, FIN (the partition of Poland, the Winter War). Bloc: Comintern. Ladder: the template calendar. Crisis content mirrors Axis anatomy with Soviet flavor: Eastern Poland and Karelia/Petsamo claims plus border incidents in crises, ultimatums to Warsaw and Helsinki at peak. Lever numbers are the Axis values.

## Arc 3: Japanese expansion (v2 second)

Historical. Aggressor: JAP (derail if democratic or communist - Japan starts on the non-aligned government, so neutrality and fascism both stay alive). Joiners: open-pool top-2, same scorer. Targets: CHI, PHI (Marco Polo Bridge; a strike on the Philippines cascades into the USA through the puppet and delivers the big war). Bloc: Co-Prosperity. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. Crisis content mirrors the other arcs with Japanese flavor: the China incident in crises, ultimatums to Nanjing and Manila at peak. War-focus branch: `JAP_reinforce_the_beijing_garrison` (China) and `JAP_strike_the_southern_road` (the south); `$ai_scenario_focus_boost()` also sits on the branch roots `JAP_revisit_the_thirteen_demands` and `JAP_occupy_siam`, so the boost is reachable even before the war focuses (the s10 lesson: a boost behind an unboosted fork is dead).

## Arc 4: Italian expansion (v2 third)

Historical. Aggressor: ITA (derail if no longer fascist - Italy starts fascist; neutrality/democracy/communism are all off-arc). Joiners: open-pool top-2, same scorer. Targets: YUG, GRE (historical claims; Albania-39 / Greece-40 run later than the Sudeten). Bloc: Mare Nostrum. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. Crisis content mirrors the other arcs with Italian flavor: the Adriatic incident in crises, ultimatums to Belgrade and Athens at peak. War-focus branch: `ITA_italys_destiny` (Balkan puppet-wargoals, including YUG and GRE) and `ITA_war_with_greece`; `$ai_scenario_focus_boost()` also sits on the branch roots `ITA_foreign_affairs`, `ITA_balkan_ambition`, and `ITA_ratify_the_stresa_front`, so the boost stays reachable ahead of the war focuses (Arc 3 lesson). `sc_focus` splices: `ITA_italys_destiny`, `ITA_war_with_greece`.

## Arc 5: Fascist Britain (v2 fourth)

Plausible. Aggressor: ENG (derail if not fascist by the crises phase; the flip is pushed through focus weights only). Joiners: open-pool top-2, same scorer. Targets: FRA, SOV (breaking the Entente, an anti-communist crusade). Bloc: New Empire. Ladder: smolder 36.1.1 / crises 37.1.1 / peak 38.6.1. Crisis content mirrors the other arcs with British flavor: the New Order incident in crises, ultimatums to Paris and Moscow at peak. Flip branch: `ENG_a_change_in_course` roots it; `$ai_scenario_focus_boost()` sits on `ENG_a_change_in_course` and `ENG_organize_the_blackshirts` so the flip branch wins the fork (s10 lesson). War-focus branch: `ENG_war_france` and `ENG_war_with_ussr` (plus roots `ENG_burn_french` and `ENG_embargo_ussr`), all with the boost. `sc_focus` splices: the flip `ENG_organize_the_blackshirts` and the two war focuses.

## Arc 6: Red America (v2 fifth, flip validation)

Plausible. Aggressor: USA (derail if not communist by the crises phase; the flip is pushed through focus weights only). Joiners: open-pool top-2, same scorer - the USSR is an emergent joiner (same ideology group passes the gate, Soviet strength all but guarantees a top-2 letter), not a guaranteed ally. Targets: CAN, JAP (both hemispheres: Canada pulls England through the dominion, Japan continues the Pacific rivalry under the red flag). Bloc: People's Internationale. Ladder: smolder 36.1.1 / crises 37.1.1 / peak 38.6.1. Crisis content mirrors the other arcs with American flavor: the World Revolution incident in crises, ultimatums to Ottawa and Tokyo at peak. Flip branch: the communist path roots at `USA_continue_the_new_deal`; `$ai_scenario_focus_boost()` sits on `USA_continue_the_new_deal` and the flip root `USA_suspend_the_presecution` so the red branch wins its fork (s10 lesson). War-focus branch: `USA_end_monarchism`, `USA_shatter_the_empires`, and `USA_us_ussr_economic_cooperation` (the SOV cooperation focus doubles as a joiner pull), all with the boost. `sc_focus` splices: the flip root and the three war focuses. If this arc needs any new mechanics, the schema is wrong: fix the schema, do not accumulate per-arc code (it did not need any - the flip validation is the proof).

## Arc 7: Napoleonic France (v2 sixth)

Historical. Aggressor: FRA (no ideology arm - France reaches the Bonapartist branch from a democratic or neutral government, so only gone/capitulated/targets derail). The last of the majors. Joiners: open-pool top-2, same scorer. Targets: GER, ITA (the Rhine and the Alps: France restores the Continental System, breaks Germany, and reclaims Savoy/Nice). Bloc: Continental System. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1 (late, matching the other late-Balkans arcs - France needs time to find the Bonapartist branch). Crisis content mirrors the other arcs with French flavor: the Rhine question in crises, ultimatums to Berlin and Rome at peak. War-focus branch: the Continental System root is `FRA_the_new_continental_system`; `$ai_scenario_focus_boost()` sits on it, on `FRA_crush_germany` (puppet wargoals on GER and Prussia), on `FRA_nothern_italy_claim` (Italy), **and on the whole Bonapartist chain** - `FRA_action_francaise`, `FRA_papal_rehabilitation`, `FRA_repeal_the_law_of_exile`, `FRA_brumaire_movement` - because in Rt56 the Bonapartist branch is hidden behind those focuses (mutually-exclusive with status-quo/radicalize/far-right), so the earlier boost-on-wars-only version never fired (s11: FRA went status-quo, zero `sc_focus`, no wargoals by t=24). `sc_focus` splices: the chain (4) + the Continental System root + the two war focuses. French flavor: the aggression is revanchist-imperial, not ideological - no flip, no ideological derail.

## Arc 8: Habsburg restoration (v2 seventh)

Historical. Aggressor: HUN (Hungary; derail when Hungary is gone, capitulated, both targets neutralized, or - the flip-style gate - Hungary never commits to the restoration path). Targets: CZE, ROU (the historic crown lands: Bohemia/Moravia and Transylvania). Joiners: open-pool top-2, same scorer (the Austro-Hungarian crown tier pulls the Danubian minors in). Bloc: Danubian Empire. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1 (late - Hungary needs to find the restoration branch first). Hungerian flavor: the revanchist Regency. The "restoration gate" replaces an ideology arm: Hungary must complete `HUN_proclaim_the_restoration_of_austria_hungary` (or the take-Austria-by-force path) by the crises phase, or the arc derails - no separate Dual Monarchy tag is created by the director (Rt56 forms Austria-Hungary by annexing Austria into Hungary, so Hungary itself is the aggressor). Crisis content mirrors the other arcs: the Habsburg question in crises, ultimatums to Prague and Bucharest at peak. War-focus branch: the restoration root `HUN_proclaim_the_restoration_of_austria_hungary` plus the claims `HUN_claim_transylvania`, `HUN_march_to_the_shore`, `HUN_claim_galicia`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 9: German Atlantic (v3 catalog)

Historical. Aggressor: GER (derail if no longer fascist). Joiners: open-pool top-2, same scorer. Variant targets: A = ENG, B = USA (the naval question: break the Anglo-American ring on the waves). Bloc: Atlantic. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. Crisis content mirrors the other arcs with German naval flavor: the Atlantic question in crises, ultimatums at peak to the A/B first target. War-focus branch: `GER_crossing_the_atlantic` and `GER_atlantic_naval_bases`, both with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 10: German Middle East (v3 catalog)

Historical. Aggressor: GER (derail if no longer fascist). Joiners: open-pool top-2, same scorer. Variant targets: A = SOV, B = IRQ, PER (the eastern question: the drive toward oil and the East). Bloc: Eastern. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `GER_influence_the_middle_east`, `GER_claim_old_colonies_in_the_east`, and `GER_wage_war_on_capitalism`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 11: Soviet South (v3 catalog)

Historical. Aggressor: SOV (derail if no longer communist). Joiners: open-pool top-2, same scorer. Variant targets: A = TUR, IRQ, PER, B = PAK, RAJ, AFG (the southern thrust: the warm seas and the Indian frontier). Bloc: Southern. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `SOV_the_last_break_southward`, `SOV_preemptive_invasion_of_iran`, and `SOV_into_the_plateau`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 12: Soviet East (v3 catalog)

Historical. Aggressor: SOV (derail if no longer communist). Joiners: open-pool top-2, same scorer. Variant targets: A = JAP, MAN, B = USA, CAN (the eastern frontier: reckoning with Japan or a trans-Pacific red drive). Bloc: Eastern. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `SOV_crush_our_eastern_rival`, `SOV_our_american_holding`, and `SOV_restore_the_old_eastern_empire`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 13: Japanese North (v3 catalog)

Historical. Aggressor: JAP (derail if democratic or communist). Joiners: open-pool top-2, same scorer. Variant targets: A = SOV, MON, B = SOV, CHI (the northern path: hokushin-ron against the Soviet Union and its satellites). Bloc: Northern. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `JAP_hokushin_ron`, `JAP_sea_establish_the_northern_resource_area`, and `JAP_strike_the_soviets`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 14: Japanese Old Oppressors (v3 catalog)

Historical. Aggressor: JAP (derail if democratic or communist). Joiners: open-pool top-2, same scorer. Variant targets: A = USA, B = ENG (strike the old oppressors: break the Anglo-American ring). Bloc: Anti-Oppressor. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `JAP_strike_the_old_oppressors` and `JAP_ultimate_deterrence`, both with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 15: Italian West (v3 catalog)

Historical. Aggressor: ITA (derail if no longer fascist). Joiners: open-pool top-2, same scorer. Variant targets: A = FRA, B = ENG (the western enemy: mastery of the western Mediterranean against France or England). Bloc: Western. Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `ITA_war_with_france`, `ITA_war_with_the_uk`, and `ITA_demand_ticino`, all with `$ai_scenario_focus_boost()` and `sc_focus`. Audit fix Sep 2026: arc 15 was missing from `sandbox_set_targets`, the derail dispatcher, `sandbox_seed_actors`, and the two `on_actions` telemetry arms (a copy-paste gap in the 14->16 range); all four were added, so the arc now seeds, derails and telemetries like the rest.

## Arc 16: Italian Mediterranean Empire (v4 catalog)

Historical. Aggressor: ITA (derail if no longer fascist). Joiners: open-pool top-2. Variant targets: A = TUR, ROM, B = FRA, ENG (restore the Roman sea from Anatolia to the west). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `ITA_a_time_for_war`, `ITA_claims_on_turkey_bba`, `ITA_all_roads_lead_to_rome`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 17: British Imperial Restoration (v4 catalog)

Imperial (gate: neutrality OR fascism by crises; derail `britain_not_imperial`). Aggressor: ENG. Variant targets: A = RAJ, B = USA, JAP (reunite the Empire under the Crown). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `ENG_reclaim_the_jewel_in_the_crown`, `ENG_bring_the_dominions_back_into_the_fold`, `ENG_unite_the_anglosphere`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 18: American War Plan (v4 catalog)

Historical. Aggressor: USA. Variant targets: A = JAP, B = ENG, CAN (the war plans: Pacific against Japan, Atlantic against the entente). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `USA_war_plan_orange`, `USA_war_plan_black`, `USA_defense_of_the_pacific`, `USA_intervention_in_europe`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 19: American Global Hegemony (v4 catalog)

Historical (no flip gate). Aggressor: USA. Variant targets: A = ENG, GER, HUN, JAP (the old imperial order), B = ENG, FRA (the open challenge). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `USA_global_hegemony` (plus the already-boosted `USA_end_monarchism` / `USA_shatter_the_empires`), all with `$ai_scenario_focus_boost()` and `sc_focus`. Variant A uses the 4-target derail arm.

## Arc 20: French Monarchist Revival (v4 catalog)

Imperial (gate: neutrality by crises; derail `france_not_neutral`). Aggressor: FRA. Variant targets: A = SPR, ADR, MEX (the Latin union), B = SOV (the second march on Moscow). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `FRA_secure_the_crown_of_spain`, `FRA_claim_the_andorran_throne`, `FRA_restore_the_mexican_monarchy`, `FRA_second_march_on_moscow`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 21: French Revenge (v4 catalog)

Historical. Aggressor: FRA. Variant targets: A = GER (partition), B = ENG (destroy Albion). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `FRA_dismantle_germany`, `FRA_crush_germany` (already boosted), `FRA_destroy_albion`, `FRA_strike_empire`, all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 22: French Plan XIV (v4 catalog)

Historical. Aggressor: FRA. Variant targets: A = SWI, B = ITA (the neutral border, Plan XIV). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `FRA_plan_xiv`, `FRA_return_to_dalmatia`, `FRA_nothern_italy_claim` (already boosted), all with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 23: Communist Germany (v4 catalog)

Flip (gate: communism by crises; derail `germany_not_communist`). Aggressor: GER. Variant targets: A = ENG, FRA, ITA (the world revolution westward), B = SOV, USA, JAP (eastward). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `GER_root_out_imperialism`, `GER_hegemony_over_europe`, `GER_wage_war_on_capitalism` (already boosted), `GER_strike_at_the_rising_sun`, with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 24: Monarchist Germany (v4 catalog)

Flip (gate: neutrality by crises; derail `germany_not_neutral`). Aggressor: GER. Variant targets: A = SOV, DEN, B = VEN, FRA (the Kaiserreich restoration). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `GER_soviet_invasion`, `GER_restore_klein_venedig` (the northern-Schleswig demand focus does not exist in Rt56 and is skipped), with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 25: White Russia (v4 catalog)

Flip (gate: SOV NOT communist by crises; derail `soviet_not_communist`, inverted gate). Aggressor: SOV (post-civil-war white Russia). Variant targets: A = GER, POL, FIN, B = UKR (the restored imperial borders). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `SOV_beaten_but_not_defeated` (already boosted), `SOV_white_exiles`, `SOV_imperial_legacy` (already boosted), `SOV_strike_the_eagle`, with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 26: Communist Japan (v4 catalog)

Flip (gate: communism by crises; derail `japan_not_communist`). Aggressor: JAP. Variant targets: A = CHI, SOV, B = ENG, USA, SIA (the pan-Asian revolution). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `JAP_put_an_end_to_chinese_feudalism`, `JAP_spread_the_revolutuon_south`, `JAP_free_asians_from_soviet_opression`, `JAP_go_after_the_capitalists`, with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 27: Communist Italy (v4 catalog)

Flip (gate: communism by crises; derail `italy_not_communist`). Aggressor: ITA. Variant targets: A = FRA, ENG, B = BUL, YUG (the red revolution in the West or the Balkans). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `ITA_pugno_alzato`, `ITA_the_enemies_of_capitalism`, `ITA_liberate_the_workers_of_africa`, with `$ai_scenario_focus_boost()` and `sc_focus`.

## Arc 28: Communist Britain (v4 catalog)

Flip (gate: communism by crises; derail `britain_not_communist`). Aggressor: ENG. Variant targets: A = GER, USA, CAN, B = SOV (the world revolution under the red flag). Ladder: smolder 36.1.1 / crises 37.6.1 / peak 38.6.1. War-focus branch: `ENG_soviet_cooperation`, `ENG_the_one_true_revolution`, `ENG_liberate_the_home_of_marx`, `ENG_liberate_the_american_workers`, with `$ai_scenario_focus_boost()` and `sc_focus`.

## Acceptance checklist

Log-first. Observer sandbox. Tick only when the grep holds (same discipline as `gdd/Civil Wars.md`).

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

## Out of scope for this iteration

- Scripted declarations of war by the director, under any name (fuses, deadlines, forced DOWs).
- Flip-assist levers for v2: arcs 5-6 flip through focus weights only (a near-zero flip rate in logs is the measured case for v3).
- Joke arcs and mixed plausibility pools.
- Player-facing scenario UI beyond the pinning game rule.
- Concurrent arcs (revisit after the v2 pool proves the single-arc loop).
- Scenario behaviour in historical mode: everything here is sandbox-only.
- Vanilla port mechanics changes: the port is content only.
- News events and notifications about director actions (the player sees crises, not the director).
