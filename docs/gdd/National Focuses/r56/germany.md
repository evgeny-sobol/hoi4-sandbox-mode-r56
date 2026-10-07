# GER_develop_modern_maneuver_warfare

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"GER_develop_modern_maneuver_warfare"}
        n2["GER_dive_bombers"]
    end
    subgraph tier_1["Tier 1"]
        n3["GER_adopt_new_panzer_doctrine"]
        n4["GER_enigma"]
        n5["GER_fortify_the_vaterland"]
        n6["GER_the_prussian_legacy"]
    end
    subgraph tier_2["Tier 2"]
        n7["GER_advanced_panzer_research"]
        n8["GER_all_terrain_military_motorcycle"]
        n9["GER_improve_motorized_troops"]
        n10["GER_instill_auftragstaktik"]
        n11["GER_lessons_of_the_great_war"]
        n12["GER_panzer_troops_school"]
        n13["GER_salvage_captured_equipment"]
    end
    subgraph tier_3["Tier 3"]
        n14["GER_artillery_bombardment"]
        n15["GER_combined_arms"]
        n16["GER_counter_anti_tank"]
        n17["GER_counter_deep_battle"]
        n18["GER_establish_the_afrikakorps"]
        n19["GER_establish_the_skijager"]
        n20["GER_expand_kummersdorfs_capacity"]
        n21{"GER_panzergrenadier"}
    end
    subgraph tier_4["Tier 4"]
        n22["GER_defend_the_vaterland"]
        n23["GER_improve_the_logistics_system"]
        n24["GER_kriegslokomotiven"]
        n25["GER_nationalize_ford_factories"]
        n26["GER_stormtroopers"]
    end
    subgraph tier_5["Tier 5"]
        n27["GER_desperate_measures"]
    end
    subgraph tier_6["Tier 6"]
        n28["GER_found_the_volkssturm"]
        n29["GER_greater_collaborator_conscription"]
    end
    subgraph tier_7["Tier 7"]
        n30["GER_front_line_cities"]
        n31["GER_uranverein"]
        n32["GER_werewolves"]
    end
    subgraph tier_8["Tier 8"]
        n33["GER_a_world_in_flames"]
    end
    n30 --> n33
    n1 --> n3
    n3 --> n7
    n6 --> n8
    n3 --> n8
    n11 --> n14
    n9 --> n14
    n7 --> n15
    n2 --> n15
    n13 --> n16
    n12 --> n16
    n8 --> n17
    n11 --> n17
    n21 --> n22
    n23 --> n27
    n22 --> n27
    n1 --> n4
    n10 --> n18
    n10 --> n19
    n7 --> n20
    n12 --> n20
    n1 --> n5
    n27 --> n28
    n29 --> n30
    n28 --> n30
    n27 --> n29
    n6 --> n9
    n21 --> n23
    n6 --> n10
    n3 --> n10
    n21 --> n24
    n6 --> n11
    n21 --> n25
    n3 --> n12
    n10 --> n21
    n6 --> n13
    n3 --> n13
    n14 --> n26
    n1 --> n6
    n29 --> n31
    n28 --> n32
    n3 x--x n6
    n22 x--x n23
```

# GER_die_letzte_verschwoerung

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n34["GER_a_new_monarch_for_a_new_age"]
        n35{"GER_die_letzte_verschwoerung"}
        n36{"GER_embrace_christian_humanism"}
        n37["GER_heed_von_neuraths_concerns"]
        n38["GER_oppose_hitler_ww"]
        n39["GER_pass_the_beck_constiution_copy"]
        n40["GER_remilitarize_the_rhineland"]
        n41["GER_shake_off_the_fascist_yoke_dummy"]
    end
    subgraph tier_1["Tier 1"]
        n42["GER_clamp_down_on_the_ruhr"]
        n43["GER_found_the_german_interim_government"]
        n44{"GER_found_the_new_german_state"}
        n45["GER_international_brigades"]
        n46["GER_rally_the_nation"]
        n47{"GER_step_back_into_the_international_community"}
    end
    subgraph tier_2["Tier 2"]
        n48["GER_GER_fate_of_nazism"]
        n49{"GER_a_greater_appeal_to_moscow"}
        n50["GER_a_martial_state"]
        n51["GER_an_outstreched_arm_towards_the_east"]
        n52{"GER_build_a_pakt_around_berlin"}
        n53["GER_heavy_handed_foreign_policy"]
        n54["GER_radicalize_german_workers"]
        n55{"GER_reaffirm_territorial_claims"}
        n56{"GER_reapproach_the_west"}
        n57["GER_rebuild_the_nation_ww"]
        n58["GER_shake_off_the_fascist_yoke"]
        n59{"GER_the_abwehrs_germany"}
        n60["GER_the_kaiser_rises"]
        n61["GER_wehrhafte_demokratie"]
    end
    subgraph tier_3["Tier 3"]
        n62["GER_a_europe_around_the_reich"]
        n63["GER_a_europe_of_the_fatherlands"]
        n64["GER_a_human_face_for_europe"]
        n65["GER_appeal_for_autonomy"]
        n66["GER_encircle_the_entente_powers"]
        n67["GER_end_the_austria_debate"]
        n68["GER_fight_the_apo"]
        n69["GER_liberation_for_the_sudetendeutsche"]
        n70["GER_loose_the_abwehr_on_the_opposition"]
        n71["GER_military_depoliticization"]
        n72["GER_move_towards_autocracy"]
        n73{"GER_move_towards_responsible_governance"}
        n74["GER_offer_goerdeler_reconciliation"]
        n75["GER_officialize_the_volksarmee"]
        n76["GER_political_commissars_focus"]
        n77{"GER_rekindle_the_franco_german_rivalry"}
        n78["GER_renegotiate_versailles_new"]
        n79["GER_restore_legality_to_germany"]
        n80["GER_revitalize_the_nation"]
        n81["GER_secure_control_over_the_brigades"]
        n82["GER_secure_western_science_funding"]
        n83{"GER_solve_the_danzig_issue"}
        n84["GER_strengthen_soviet_political_support"]
        n85["GER_the_old_man_still_has_it"]
        n86["GER_the_revolution_secured"]
    end
    subgraph tier_4["Tier 4"]
        n87["GER_a_dictated_parliament"]
        n88["GER_a_guided_kaiserreich"]
        n89["GER_align_the_balkans"]
        n90["GER_an_era_of_honor"]
        n91["GER_as_with_the_sa_so_with_the_antifa"]
        n92["GER_ban_internal_operations"]
        n93["GER_clear_the_facist_lair"]
        n94["GER_demokratieschutzgesetz"]
        n95["GER_embark_on_the_quest_to_absolutism"]
        n96["GER_end_the_german_brain_drain"]
        n97["GER_establish_the_european_coal_and_steel_community"]
        n98["GER_extol_prussian_virtue"]
        n99["GER_forge_an_alliance_with_the_church"]
        n100["GER_form_the_presidency"]
        n101["GER_germans_everywhere_united"]
        n102["GER_glorify_stalins_image"]
        n103["GER_increase_factional_defenses"]
        n104["GER_install_a_loyal_army_chief"]
        n105["GER_move_to_restore_brest_litovsk"]
        n106["GER_organize_workers_councils"]
        n107["GER_our_own_lennin"]
        n108["GER_politicize_the_abwehr"]
        n109["GER_reestablish_colonial_claims"]
        n110["GER_return_the_exiles"]
        n111["GER_the_berlin_trials"]
        n112["GER_the_canaris_wilhelm_pakt"]
        n113["GER_towards_a_european_research_sphere"]
    end
    subgraph tier_5["Tier 5"]
        n114{"GER_a_guiding_hand_in_politics"}
        n115["GER_an_iron_fist_on_the_state"]
        n116["GER_consolidate_the_new_system"]
        n117["GER_consolidate_the_party_leadership"]
        n118["GER_control_the_press"]
        n119["GER_declare_the_presidential_republic"]
        n120["GER_form_the_league_of_patriots"]
        n121{"GER_foster_a_progress_cult"}
        n122["GER_implement_state_religion"]
        n123["GER_nie_wieder_ist_jetzt"]
        n124["GER_pass_the_beck_constiution"]
        n125["GER_r56_pool_technical_know_how"]
        n126["GER_r56_shared_r_and_d_programs"]
        n127["GER_ready_the_army_for_the_external_threat"]
        n128{"GER_reconcile_the_crown_prince"}
        n129["GER_rely_on_divine_right"]
        n130{"GER_restore_discipline_in_the_military"}
        n131["GER_unite_the_working_class"]
        n132["GER_vanquish_the_eastern_threat"]
        n133["GER_whip_the_party_into_line"]
    end
    subgraph tier_6["Tier 6"]
        n134["GER_an_irresistable_moral_guide"]
        n135["GER_an_old_germany_for_a_new_age"]
        n136["GER_approach_the_anglosphere"]
        n137["GER_consolidate_the_kaiserreich"]
        n138["GER_deal_with_resistance_in_the_heer"]
        n139["GER_expand_liberalization_efforts"]
        n140["GER_hold_new_elections"]
        n141["GER_import_soviet_sciences"]
        n142["GER_integrate_the_dnvp"]
        n143["GER_integrate_the_monarchists"]
        n144["GER_integrate_the_zentrum"]
        n145["GER_military_led_state_building"]
        n146["GER_open_the_asia_department"]
        n147["GER_open_up_a_latin_connection"]
        n148["GER_r56_mannheim_project"]
        n149["GER_reach_out_to_old_allies"]
        n150["GER_remove_fatherlandless_fellows_from_power"]
        n151["GER_restore_the_fahneneid"]
        n152["GER_return_to_german_brilliance"]
        n153["GER_spread_ideals_of_soldierly_conscience"]
        n154["GER_thalmanns_cult_of_personality"]
        n155["GER_the_national_congress_of_councils"]
        n156["GER_towards_european_revolution"]
        n157["GER_work_with_the_aristocracy"]
    end
    subgraph tier_7["Tier 7"]
        n158["GER_alliance_with_the_united_evangelical_church"]
        n159["GER_bring_back_the_old_heirarchy"]
        n160["GER_build_a_cult_of_personality"]
        n161["GER_distance_from_past_mistakes"]
        n162{"GER_dnvp_in_coalition"}
        n163{"GER_dstp_in_coalition"}
        n164{"GER_dvu_in_coalition"}
        n165["GER_expand_the_reichsverweserschaft"]
        n166["GER_international_pro_european_propaganda"]
        n167["GER_kpd_in_coalition"]
        n168["GER_militarize_socity"]
        n169{"GER_nraf_in_coalition"}
        n170["GER_power_to_the_aristocracy"]
        n171["GER_prepare_the_new_era"]
        n172["GER_ready_the_political_sturcture"]
        n173["GER_secure_the_armys_support"]
        n174["GER_spd_in_coalition"]
        n175["GER_unite_the_bearocratic_colossus"]
        n176["GER_zentrum_in_coalition"]
    end
    subgraph tier_8["Tier 8"]
        n177["GER_a_germany_of_the_elites"]
        n178["GER_adenauers_chance"]
        n179["GER_all_under_the_grey_emminence"]
        n180{"GER_choose_an_heir_for_wels"}
        n181["GER_consolidate_elite_support"]
        n182{"GER_deal_with_inner_party_opposition"}
        n183{"GER_deal_with_the_officier_corps"}
        n184["GER_declare_the_ecr"]
        n185{"GER_embrace_secularism"}
        n186["GER_end_the_divide_between_state_and_church"]
        n187["GER_entrench_the_gilded_cage"]
        n188["GER_espouse_voelkish_nationalism"]
        n189["GER_fight_for_dvu_stability"]
        n190["GER_focus_on_political_education"]
        n191["GER_goerdelers_new_party"]
        n192{"GER_highten_nationalist_rethoric"}
        n193["GER_hugenburgs_legacy"]
        n194["GER_industrial_collectivization"]
        n195["GER_invest_in_the_naval_pet_project"]
        n196["GER_legacy_of_stresemann"]
        n197["GER_legalize_the_kjvd"]
        n198["GER_maintian_strict_anti_marxism"]
        n199["GER_offer_concessions_to_the_elites"]
        n200["GER_positive_christianty"]
        n201["GER_radicalize_the_army"]
        n202{"GER_radicalize_the_workers"}
        n203["GER_readdress_the_kaiserfrage"]
        n204["GER_reapproachment_with_moscow"]
        n205["GER_redistribute_wealth"]
        n206{"GER_revive_gestapo_remnants"}
        n207{"GER_revolution_in_german_culture"}
        n208["GER_the_compromise_for_national_order"]
        n209["GER_the_legacy_of_the_sozialistengesetze"]
        n210["GER_the_party_under_stegerwald"]
        n211{"GER_undermine_german_democracy"}
        n212["GER_undo_the_secularization_of_germany"]
        n213["GER_utilize_pro_democratic_propaganda"]
        n214["GER_utilize_the_zentrum_freeze"]
        n215["GER_wirths_new_zentrum"]
    end
    subgraph tier_9["Tier 9"]
        n216["GER_a_new_national_anthem"]
        n217["GER_achieve_national_renewal"]
        n218["GER_an_eye_towards_the_east"]
        n219["GER_apply_the_reichskonkordat_to_the_republic"]
        n220["GER_bring_about_the_second_revolution"]
        n221["GER_build_up_worker_and_peasant_councils"]
        n222["GER_cater_to_the_masses"]
        n223["GER_centralize_the_state"]
        n224["GER_collapse_our_institutions"]
        n225["GER_combat_the_reactionary"]
        n226["GER_coopt_the_sa"]
        n227["GER_deal_with_the_conciliators"]
        n228{"GER_end_the_party_rift"}
        n229["GER_expand_black_front_influence"]
        n230["GER_expand_the_kaisers_duties"]
        n231["GER_fight_trade_unions"]
        n232["GER_form_the_stasi_new"]
        n233["GER_foster_christian_democracy"]
        n234["GER_full_rehabilitation"]
        n235["GER_fully_rebuild_the_secret_police"]
        n236["GER_globalize_the_revolution"]
        n237["GER_guarantee_religious_freedom"]
        n238["GER_inspire_fear_of_the_liberals"]
        n239["GER_knock_stegerwald_down_a_peg"]
        n240["GER_land_reform"]
        n241["GER_learn_from_the_enabling_act"]
        n242["GER_legalize_the_remaining_communist_parties"]
        n243["GER_limited_reconciliation"]
        n244["GER_mandatory_membership"]
        n245["GER_manipulate_the_churches"]
        n246["GER_natural_leadership_for_the_best_men"]
        n247["GER_noble_advisors"]
        n248["GER_organize_german_labor"]
        n249["GER_peace_in_the_east"]
        n250["GER_politicize_the_trade_unions"]
        n251["GER_proper_agrarian_policy"]
        n252["GER_purge_the_military_of_reactionaries"]
        n253["GER_radicalize_german_nationalism"]
        n254["GER_radicalize_rearmament_efforts"]
        n255["GER_rebuild_the_prussian_bastion"]
        n256["GER_rebuild_the_shattered_zentrum"]
        n257["GER_rehabilitate_mueller"]
        n258["GER_restore_the_state_churches"]
        n259["GER_seize_direct_control"]
        n260["GER_sensible_fiscal_policy"]
        n261["GER_strengthen_german_patriotism"]
        n262["GER_strengthen_the_responsible_elites"]
        n263["GER_strengthen_the_spd_beurocracy"]
        n264["GER_the_fight_against_german_antisemitism"]
        n265["GER_the_new_federalism"]
        n266{"GER_the_new_german_establishment"}
        n267["GER_the_socialist_traitor"]
        n268["GER_tighten_naval_intelligence"]
        n269["GER_towards_national_militarization"]
        n270["GER_towards_state_atheism"]
        n271["GER_uplift_the_antifa"]
        n272["GER_uplift_the_black_front"]
        n273["GER_uplift_the_sa"]
        n274["GER_weaken_the_presidents_power"]
        n275["GER_work_towards_fiscal_stability"]
        n276["GER_work_towards_national_demilitarization"]
    end
    subgraph tier_10["Tier 10"]
        n277["GER_a_coup_in_all_but_name"]
        n278["GER_a_new_age_of_peace"]
        n279["GER_a_powerful_state"]
        n280["GER_a_respectable_germany"]
        n281["GER_a_second_restoration"]
        n282["GER_a_time_for_protectionism"]
        n283["GER_abandon_the_post_alltogether"]
        n284["GER_alliance_with_the_junkers"]
        n285["GER_bring_about_a_new_social_order"]
        n286["GER_bring_back_einstein"]
        n287["GER_build_a_mass_movement"]
        n288["GER_campaign_as_a_popular_front"]
        n289["GER_consolidate_socialist_reforms"]
        n290["GER_consultations_with_the_experts"]
        n291["GER_crush_bourgeoise_captialism"]
        n292["GER_divert_military_funding"]
        n293["GER_embrace_true_national_socialism"]
        n294["GER_end_conscription"]
        n295["GER_enforce_a_secularized_curriculum"]
        n296["GER_engrain_antiurbanism"]
        n297["GER_ensure_a_loyal_clergyship"]
        n298["GER_expand_recruitment"]
        n299["GER_federalism_a_hedge_against_radicalism"]
        n300["GER_fight_fascism_in_all_its_forms"]
        n301["GER_german_entry_into_the_comintern"]
        n302["GER_honor_the_legacy_of_marx"]
        n303["GER_improve_railway_economics"]
        n304["GER_increase_municipal_autonomy"]
        n305["GER_industrial_cooperation_2"]
        n306["GER_integrate_our_new_lands"]
        n307["GER_legacy_of_stinn"]
        n308["GER_legitimize_the_left"]
        n309["GER_limited_federalist_reforms"]
        n310["GER_national_economic_coordination"]
        n311["GER_peace_with_our_new_identity"]
        n312["GER_phase_out_the_standing_army"]
        n313["GER_reform_the_institutions"]
        n314["GER_revive_the_attitude_of_1914"]
        n315["GER_strike_the_baltic"]
        n316["GER_the_democratic_hegemon_of_germany"]
        n317["GER_the_fullness_of_german_conservatism"]
        n318["GER_the_national_salvation_law"]
        n319["GER_towards_a_party_state"]
        n320["GER_unite_the_party"]
        n321["GER_upkeep_german_order"]
        n322["GER_watch_the_churches"]
    end
    subgraph tier_11["Tier 11"]
        n323["GER_a_juggernaught_back_from_the_grave"]
        n324["GER_a_new_era_of_german_science"]
        n325["GER_a_patriotic_german_church"]
        n326["GER_a_true_volksgemeinschaft"]
        n327["GER_an_era_of_german_wealth"]
        n328["GER_ban_the_reactionaries"]
        n329["GER_build_germany_from_the_apartment_up"]
        n330["GER_claim_leadership_of_german_nationalism"]
        n331["GER_construct_the_karl_marx_cultural_instutute"]
        n332["GER_corporatism_with_catholic_characteristics"]
        n333["GER_demand_state_approval_for_clergy"]
        n334["GER_destroy_the_elites"]
        n335["GER_end_interanal_factionalism"]
        n336["GER_ensure_permanent_food_security"]
        n337["GER_expand_pro_state_propaganda"]
        n338["GER_form_the_sed"]
        n339["GER_foster_german_democracy"]
        n340["GER_fufill_the_legacy_of_rohm"]
        n341["GER_intertwine_the_state_and_the_church"]
        n342["GER_introduce_the_jugendweihe"]
        n343["GER_no_compromise_on_socialist_ideals"]
        n344["GER_prioritise_the_rheinland"]
        n345["GER_rehabilitate_the_red_tsar"]
        n346["GER_resource_trade_2"]
        n347["GER_restore_the_old_estates"]
        n348["GER_revolution_by_every_worker"]
        n349["GER_tech_sharing_2"]
        n350["GER_technocracy_with_strong_limits"]
        n351["GER_the_second_gleichschaltung"]
        n352["GER_the_spirit_of_blut_and_boden"]
        n353["GER_the_state_safe_from_within"]
        n354["GER_turn_the_opposition_into_regional_issues"]
        n355["GER_unite_against_fascism"]
        n356["GER_work_towards_a_demilitarized_europe"]
    end
    subgraph tier_12["Tier 12"]
        n357{"GER_declare_the_volksreich"}
        n358{"GER_end_political_parties"}
        n359["GER_ensure_the_gradual_withering_away_of_religion"]
        n360["GER_germany_glorious_as_it_once_was"]
        n361["GER_help_the_church_permeate_everyday_german_life"]
        n362["GER_the_end_of_class_warfare"]
        n363["GER_the_will_of_the_people_unopposed"]
        n364["GER_towards_mierendorffs_vision"]
        n365["GER_undermine_international_fascism"]
    end
    subgraph tier_13["Tier 13"]
        n366["GER_hail_the_new_fuhrer"]
        n367["GER_the_president_for_life"]
    end
    n46 --> n48
    n230 --> n277
    n73 --> n87
    n52 --> n62
    n52 --> n63
    n159 --> n177
    n42 --> n49
    n73 --> n88
    n87 --> n114
    n88 --> n114
    n52 --> n64
    n280 --> n323
    n231 --> n323
    n44 --> n50
    n225 --> n278
    n233 --> n278
    n286 --> n324
    n190 --> n216
    n297 --> n325
    n223 --> n279
    n254 --> n279
    n266 --> n280
    n230 --> n281
    n251 --> n282
    n289 --> n326
    n291 --> n326
    n274 --> n283
    n188 --> n217
    n201 --> n217
    n176 --> n178
    n164 --> n178
    n69 --> n89
    n67 --> n89
    n175 --> n179
    n134 --> n179
    n251 --> n284
    n135 --> n158
    n150 --> n158
    n310 --> n327
    n79 --> n90
    n192 --> n218
    n70 --> n115
    n108 --> n115
    n115 --> n134
    n130 --> n135
    n47 --> n51
    n49 --> n65
    n212 --> n219
    n109 --> n136
    n101 --> n136
    n103 --> n136
    n132 --> n136
    n75 --> n91
    n76 --> n91
    n71 --> n92
    n319 --> n328
    n250 --> n285
    n248 --> n285
    n182 --> n220
    n264 --> n286
    n157 --> n159
    n149 --> n160
    n151 --> n160
    n222 --> n287
    n47 --> n52
    n299 --> n329
    n304 --> n329
    n182 --> n221
    n242 --> n288
    n180 --> n222
    n182 --> n223
    n174 --> n180
    n314 --> n330
    n311 --> n330
    n35 --> n42
    n77 --> n93
    n56 --> n93
    n202 --> n224
    n211 --> n224
    n215 --> n225
    n178 --> n225
    n163 --> n181
    n220 --> n289
    n114 --> n137
    n36 --> n137
    n106 --> n116
    n110 --> n117
    n111 --> n117
    n300 --> n331
    n302 --> n331
    n275 --> n290
    n95 --> n118
    n188 --> n226
    n285 --> n332
    n220 --> n291
    n169 --> n182
    n115 --> n138
    n207 --> n227
    n167 --> n183
    n169 --> n183
    n172 --> n184
    n166 --> n184
    n100 --> n119
    n104 --> n119
    n334 --> n357
    n351 --> n357
    n354 --> n357
    n322 --> n333
    n68 --> n94
    n318 --> n334
    n157 --> n161
    n276 --> n292
    n140 --> n162
    n39 --> n162
    n140 --> n163
    n140 --> n164
    n85 --> n95
    n174 --> n185
    n167 --> n185
    n221 --> n293
    n229 --> n293
    n52 --> n66
    n53 --> n66
    n276 --> n294
    n196 --> n335
    n307 --> n335
    n354 --> n358
    n334 --> n358
    n55 --> n67
    n158 --> n186
    n80 --> n96
    n189 --> n228
    n237 --> n295
    n270 --> n295
    n251 --> n296
    n257 --> n297
    n245 --> n297
    n306 --> n336
    n342 --> n359
    n333 --> n359
    n165 --> n187
    n168 --> n187
    n160 --> n188
    n78 --> n97
    n182 --> n229
    n36 --> n139
    n114 --> n139
    n317 --> n337
    n232 --> n298
    n203 --> n230
    n145 --> n165
    n85 --> n98
    n34 --> n98
    n265 --> n299
    n227 --> n300
    n164 --> n189
    n61 --> n68
    n181 --> n231
    n163 --> n190
    n72 --> n99
    n99 --> n120
    n108 --> n120
    n74 --> n100
    n319 --> n338
    n207 --> n232
    n91 --> n121
    n215 --> n233
    n178 --> n233
    n316 --> n339
    n35 --> n43
    n35 --> n44
    n289 --> n340
    n279 --> n340
    n291 --> n340
    n161 --> n234
    n177 --> n234
    n206 --> n235
    n249 --> n301
    n69 --> n101
    n83 --> n101
    n67 --> n101
    n296 --> n360
    n347 --> n360
    n352 --> n360
    n155 --> n236
    n184 --> n236
    n84 --> n102
    n162 --> n191
    n164 --> n191
    n185 --> n237
    n357 --> n366
    n47 --> n53
    n341 --> n361
    n162 --> n192
    n169 --> n192
    n164 --> n192
    n119 --> n140
    n43 --> n140
    n244 --> n302
    n227 --> n302
    n164 --> n193
    n162 --> n193
    n99 --> n122
    n121 --> n141
    n275 --> n303
    n62 --> n103
    n63 --> n103
    n265 --> n304
    n167 --> n194
    n249 --> n305
    n182 --> n238
    n74 --> n104
    n218 --> n306
    n120 --> n142
    n120 --> n143
    n122 --> n144
    n120 --> n144
    n35 --> n45
    n156 --> n166
    n285 --> n341
    n258 --> n341
    n295 --> n342
    n270 --> n342
    n119 --> n195
    n175 --> n195
    n214 --> n239
    n140 --> n167
    n41 --> n167
    n205 --> n240
    n202 --> n241
    n211 --> n241
    n266 --> n307
    n163 --> n196
    n167 --> n197
    n180 --> n242
    n242 --> n308
    n55 --> n69
    n221 --> n309
    n182 --> n243
    n59 --> n70
    n169 --> n198
    n197 --> n244
    n207 --> n244
    n200 --> n245
    n145 --> n168
    n137 --> n168
    n61 --> n71
    n114 --> n145
    n83 --> n105
    n59 --> n72
    n50 --> n73
    n260 --> n310
    n173 --> n246
    n201 --> n246
    n188 --> n246
    n177 --> n246
    n94 --> n123
    n92 --> n123
    n287 --> n343
    n177 --> n247
    n140 --> n169
    n161 --> n199
    n59 --> n74
    n58 --> n75
    n109 --> n146
    n101 --> n146
    n103 --> n146
    n132 --> n146
    n109 --> n147
    n101 --> n147
    n103 --> n147
    n132 --> n147
    n210 --> n248
    n86 --> n106
    n86 --> n107
    n90 --> n124
    n87 --> n124
    n88 --> n124
    n204 --> n249
    n261 --> n311
    n273 --> n312
    n271 --> n312
    n272 --> n312
    n58 --> n76
    n72 --> n108
    n210 --> n250
    n169 --> n200
    n162 --> n200
    n137 --> n170
    n139 --> n171
    n135 --> n171
    n304 --> n344
    n193 --> n251
    n180 --> n252
    n125 --> n148
    n126 --> n148
    n96 --> n125
    n96 --> n126
    n192 --> n253
    n42 --> n54
    n182 --> n254
    n160 --> n201
    n173 --> n201
    n167 --> n202
    n38 --> n46
    n35 --> n46
    n128 --> n149
    n164 --> n203
    n162 --> n203
    n91 --> n127
    n156 --> n172
    n155 --> n172
    n47 --> n55
    n47 --> n56
    n167 --> n204
    n46 --> n57
    n213 --> n255
    n178 --> n256
    n95 --> n128
    n169 --> n205
    n174 --> n205
    n167 --> n205
    n77 --> n109
    n56 --> n109
    n263 --> n313
    n200 --> n257
    n313 --> n345
    n320 --> n345
    n55 --> n77
    n95 --> n129
    n129 --> n150
    n130 --> n150
    n56 --> n78
    n305 --> n346
    n98 --> n130
    n50 --> n79
    n129 --> n151
    n284 --> n347
    n212 --> n258
    n86 --> n110
    n121 --> n152
    n48 --> n80
    n57 --> n80
    n164 --> n206
    n169 --> n206
    n162 --> n206
    n252 --> n314
    n261 --> n314
    n312 --> n348
    n167 --> n207
    n54 --> n81
    n45 --> n81
    n157 --> n173
    n149 --> n173
    n56 --> n82
    n195 --> n259
    n191 --> n260
    n42 --> n58
    n55 --> n83
    n140 --> n174
    n36 --> n153
    n130 --> n153
    n37 --> n47
    n35 --> n47
    n180 --> n261
    n49 --> n84
    n178 --> n262
    n180 --> n263
    n218 --> n315
    n305 --> n349
    n290 --> n350
    n303 --> n350
    n133 --> n154
    n131 --> n154
    n44 --> n59
    n86 --> n111
    n72 --> n112
    n170 --> n208
    n168 --> n208
    n228 --> n316
    n332 --> n362
    n191 --> n264
    n228 --> n317
    n44 --> n60
    n169 --> n209
    n164 --> n209
    n162 --> n209
    n116 --> n155
    n117 --> n155
    n238 --> n318
    n178 --> n265
    n181 --> n266
    n60 --> n85
    n176 --> n210
    n164 --> n210
    n358 --> n367
    n58 --> n86
    n318 --> n351
    n215 --> n267
    n282 --> n352
    n298 --> n353
    n338 --> n363
    n328 --> n363
    n195 --> n268
    n63 --> n113
    n241 --> n319
    n224 --> n319
    n116 --> n156
    n117 --> n156
    n343 --> n364
    n356 --> n364
    n188 --> n269
    n201 --> n269
    n185 --> n270
    n318 --> n354
    n309 --> n354
    n167 --> n211
    n353 --> n365
    n162 --> n212
    n176 --> n212
    n164 --> n212
    n308 --> n355
    n288 --> n355
    n143 --> n175
    n144 --> n175
    n142 --> n175
    n263 --> n320
    n107 --> n131
    n262 --> n321
    n256 --> n321
    n183 --> n271
    n169 --> n272
    n183 --> n272
    n169 --> n273
    n183 --> n273
    n174 --> n213
    n163 --> n213
    n176 --> n213
    n164 --> n214
    n64 --> n132
    n105 --> n132
    n270 --> n322
    n235 --> n322
    n232 --> n322
    n213 --> n274
    n43 --> n61
    n107 --> n133
    n111 --> n133
    n176 --> n215
    n292 --> n356
    n294 --> n356
    n215 --> n275
    n180 --> n276
    n128 --> n157
    n140 --> n176
    n39 --> n176
    n87 x--x n88
    n62 x--x n63
    n64 x--x n105
    n50 x--x n59
    n65 x--x n84
    n224 x--x n241
    n137 x--x n145
    n35 x--x n40
    n139 x--x n153
    n189 x--x n214
    n232 x--x n235
    n43 x--x n44
    n191 x--x n193
    n237 x--x n270
    n366 x--x n367
    n141 x--x n152
    n307 x--x n196
    n243 x--x n253
    n72 x--x n74
    n252 x--x n276
    n149 x--x n157
    n56 x--x n77
    n109 x--x n78
    n316 x--x n317
    n271 x--x n272
    n271 x--x n273
    n272 x--x n273
```

# GER_expand_the_kaisers_duties_fake

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n114{"GER_a_guiding_hand_in_politics"}
        n368(("GER_expand_the_kaisers_duties_fake"))
        n165["GER_expand_the_reichsverweserschaft"]
        n145["GER_military_led_state_building"]
        n129["GER_rely_on_divine_right"]
        n85["GER_the_old_man_still_has_it"]
    end
    subgraph tier_1["Tier 1"]
        n369["GER_the_kaiser_rises_fake"]
    end
    subgraph tier_2["Tier 2"]
        n34{"GER_a_new_monarch_for_a_new_age"}
        n370["GER_cleanse_the_kaiser_wilhelm_institute"]
    end
    subgraph tier_3["Tier 3"]
        n371["GER_a_patriotic_monarchy"]
        n372["GER_bring_the_kaiserreich_back_to_the_forefront_of_development"]
        n98["GER_extol_prussian_virtue"]
        n373["GER_modernize_the_monarchy"]
        n374["GER_r56_glorious_mechanical_mechanations"]
    end
    subgraph tier_4["Tier 4"]
        n36{"GER_embrace_christian_humanism"}
        n130{"GER_restore_discipline_in_the_military"}
    end
    subgraph tier_5["Tier 5"]
        n135["GER_an_old_germany_for_a_new_age"]
        n137["GER_consolidate_the_kaiserreich"]
        n139["GER_expand_liberalization_efforts"]
        n150["GER_remove_fatherlandless_fellows_from_power"]
        n153["GER_spread_ideals_of_soldierly_conscience"]
    end
    subgraph tier_6["Tier 6"]
        n158["GER_alliance_with_the_united_evangelical_church"]
        n168["GER_militarize_socity"]
        n170["GER_power_to_the_aristocracy"]
        n171["GER_prepare_the_new_era"]
    end
    subgraph tier_7["Tier 7"]
        n186["GER_end_the_divide_between_state_and_church"]
        n187["GER_entrench_the_gilded_cage"]
        n208["GER_the_compromise_for_national_order"]
    end
    n369 --> n34
    n34 --> n371
    n135 --> n158
    n150 --> n158
    n130 --> n135
    n370 --> n372
    n369 --> n370
    n114 --> n137
    n36 --> n137
    n371 --> n36
    n373 --> n36
    n158 --> n186
    n165 --> n187
    n168 --> n187
    n36 --> n139
    n114 --> n139
    n85 --> n98
    n34 --> n98
    n145 --> n168
    n137 --> n168
    n34 --> n373
    n137 --> n170
    n139 --> n171
    n135 --> n171
    n370 --> n374
    n129 --> n150
    n130 --> n150
    n98 --> n130
    n36 --> n153
    n130 --> n153
    n170 --> n208
    n168 --> n208
    n368 --> n369
    n371 x--x n373
    n137 x--x n145
    n139 x--x n153
```

# GER_expanding_the_luftwaffe

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n7["GER_advanced_panzer_research"]
        n375["GER_construct_aircraft_carriers"]
        n376(("GER_expanding_the_luftwaffe"))
    end
    subgraph tier_1["Tier 1"]
        n377{"GER_aeronautical_research_institute"}
        n378["GER_fallschirmjager"]
        n379["GER_form_the_jagdwaffe"]
    end
    subgraph tier_2["Tier 2"]
        n380["GER_develop_the_knickebein"]
        n2["GER_dive_bombers"]
        n381["GER_experimental_rotorcrafts"]
        n382["GER_reorganize_the_luftwaffe"]
        n383["GER_tactical_bombers"]
        n384["GER_uralbomber_program"]
    end
    subgraph tier_3["Tier 3"]
        n15["GER_combined_arms"]
        n385["GER_defense_of_the_reich"]
        n386["GER_rocketry_innovations"]
        n387["GER_solve_the_logistical_bottlenecks"]
        n388["GER_torpedobomber"]
    end
    subgraph tier_4["Tier 4"]
        n389["GER_construct_the_kammhuber_line"]
        n390["GER_establish_carrier_groups"]
        n391["GER_establish_night_fighter_squadrons"]
        n392["GER_flak_towers"]
    end
    subgraph tier_5["Tier 5"]
        n393["GER_aerodynamic_research_institute"]
    end
    subgraph tier_6["Tier 6"]
        n394["GER_amerikabomber"]
    end
    n387 --> n393
    n389 --> n393
    n391 --> n393
    n392 --> n393
    n386 --> n393
    n376 --> n377
    n393 --> n394
    n7 --> n15
    n2 --> n15
    n385 --> n389
    n382 --> n385
    n380 --> n385
    n379 --> n380
    n377 --> n2
    n388 --> n390
    n375 --> n390
    n385 --> n391
    n379 --> n381
    n376 --> n378
    n385 --> n392
    n376 --> n379
    n379 --> n382
    n2 --> n386
    n383 --> n386
    n384 --> n386
    n382 --> n387
    n377 --> n383
    n380 --> n388
    n377 --> n384
    n2 x--x n383
    n2 x--x n384
    n383 x--x n384
```

# GER_kill_hitler

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n395{"GER_anti_comintern_pact"}
        n396{"GER_kill_hitler"}
        n40{"GER_remilitarize_the_rhineland"}
    end
    subgraph tier_1["Tier 1"]
        n397{"GER_political_turmoil"}
        n398["GER_rally_the_monarchists"]
    end
    subgraph tier_2["Tier 2"]
        n399["GER_contact_ludendorff"]
        n400{"GER_repeal_reichstag_fire_decree"}
        n401["GER_restore_weimar"]
        n402["GER_return_of_conservative_exiles"]
        n403["GER_support_freikorps"]
    end
    subgraph tier_3["Tier 3"]
        n404["GER_a_new_reich"]
        n405["GER_alliance_with_soviets"]
        n406["GER_establish_bundesrepublik"]
        n407["GER_world_revolution"]
    end
    subgraph tier_4["Tier 4"]
        n408["GER_collectivize_industry"]
        n409["GER_establish_bundeswehr"]
        n410["GER_post_fascism_recovery"]
        n411["GER_rehabilitate_military"]
        n412{"GER_restore_the_empire"}
    end
    subgraph tier_5["Tier 5"]
        n413{"GER_defense_and_deterence"}
        n414["GER_establish_NVA"]
        n415{"GER_establish_imperial_german_army"}
        n416["GER_european_claims"]
        n417{"GER_mon_allies_alliance"}
        n418["GER_recruit_grenztruppen"]
        n419{"GER_replace_reichsmark"}
        n420{"GER_restore_the_central_powers"}
        n421{"GER_support_landwehr"}
    end
    subgraph tier_6["Tier 6"]
        n422["GER_alliance_with_austria_hungary"]
        n423["GER_alliance_with_the_ottomans"]
        n424{"GER_anti_expansionism"}
        n425{"GER_asia_department"}
        n426["GER_asia_department_dummy"]
        n427["GER_demand_northern_schleswig_r56"]
        n428["GER_destabilize_france"]
        n429{"GER_expansionism_light"}
        n430["GER_focus_on_fascist_threat_r56"]
        n431["GER_interest_in_the_carribean"]
        n432["GER_mon_FRA_alliance"]
        n433["GER_poland_trade"]
        n434["GER_prepare_italian_coup_r56"]
        n435["GER_prioritize_civilian_industry"]
        n436["GER_prioritize_military_industry"]
        n437["GER_progress_cult"]
        n438["GER_soviet_invasion"]
        n439["GER_spread_the_revolution_r56"]
    end
    subgraph tier_7["Tier 7"]
        n440["GER_alliance_with_gustaf"]
        n441["GER_assassinate_mussolini_r56"]
        n442["GER_befriend_china"]
        n443["GER_befriend_japan"]
        n444{"GER_decrease_fascist_influence_r56"}
        n445["GER_galvanize_german_militarism"]
        n446["GER_gott_mit_uns"]
        n447{"GER_increase_influence_over_balkans_r56"}
        n448{"GER_increase_influence_over_eastern_europe_r56"}
        n449{"GER_join_allies"}
        n450{"GER_lead_communists"}
        n451{"GER_lead_democracies"}
        n452["GER_mon_anti_commie_france"]
        n453{"GER_pressure_austria_r56"}
        n454["GER_renegotiate_versailles"]
        n455["GER_restore_klein_venedig"]
        n456["GER_revive_brest_litovsk"]
        n457["GER_soviet_scientists"]
        n458["GER_sway_spain"]
    end
    subgraph tier_8["Tier 8"]
        n459["GER_ally_benelux"]
        n460["GER_ally_chiang_kai_shek"]
        n461{"GER_ally_eastern_europe"}
        n462{"GER_anti_colonialism"}
        n463["GER_claim_old_colonies_in_the_east"]
        n464["GER_colonies_for_support"]
        n465["GER_deal_with_the_devil_r56"]
        n466{"GER_dem_anschluss_prep"}
        n467["GER_help_SOV_revolutionaries_r56"]
        n468["GER_increase_influence_over_benelux_r56"]
        n469["GER_inter_communist_fighting"]
        n470["GER_japanese_naval_cooperation"]
        n471["GER_legacy_of_gluckliche_zwanziger_jahre"]
        n472["GER_negotiate_old_colonies_in_the_east"]
        n473["GER_re_establish_german_control_over_qingdao"]
        n474{"GER_request_danzig"}
        n475["GER_safeguard_neutrality"]
        n476["GER_western_science_funding"]
    end
    subgraph tier_9["Tier 9"]
        n477["GER_ally_czechoslovakia"]
        n478["GER_aus_ally"]
        n479["GER_counter_soviet_agression"]
        n480["GER_create_asian_reichskommissariat"]
        n481["GER_dem_anschluss"]
        n482["GER_dem_polish_corridor_deal"]
        n483["GER_dem_polish_corridor_trade"]
        n484["GER_end_british_imperial_hegemony_r56"]
        n485["GER_german_scientific_haven"]
        n486["GER_old_nemensis_r56"]
        n487["GER_sentinels_of_the_pacific"]
        n488["GER_south_east_asian_natural_wealth"]
        n489["GER_soviet_support"]
        n490["GER_the_source_of_fascism_r56"]
        n491["GER_western_communist"]
    end
    subgraph tier_10["Tier 10"]
        n492["GER_anti_bolshevist_bloc"]
        n493["GER_anti_soviet_friend_baltics"]
        n494{"GER_anti_soviet_friend_finland"}
        n495{"GER_anti_soviet_friend_poland"}
        n496["GER_blitzkrieg_across_the_pacific"]
        n497["GER_dem_italy_attack"]
        n498["GER_the_proud_eagle_and_the_resurgent_dragon"]
    end
    subgraph tier_11["Tier 11"]
        n499["GER_anti_soviet_war"]
        n500["GER_cooperate_with_nordics"]
        n501["GER_dem_anti_commie_bloc_hungary"]
        n502["GER_realise_belarusian_statehood"]
        n503["GER_realise_ukrainian_statehood"]
    end
    subgraph tier_12["Tier 12"]
        n504["GER_dem_italy_alliance"]
    end
    n403 --> n404
    n402 --> n404
    n420 --> n422
    n432 --> n440
    n422 --> n440
    n400 --> n405
    n420 --> n423
    n451 --> n459
    n442 --> n460
    n461 --> n477
    n451 --> n461
    n450 --> n461
    n479 --> n492
    n451 --> n492
    n451 --> n462
    n450 --> n462
    n419 --> n424
    n413 --> n424
    n479 --> n493
    n479 --> n494
    n479 --> n495
    n494 --> n499
    n495 --> n499
    n420 --> n425
    n420 --> n426
    n434 --> n441
    n466 --> n478
    n40 --> n442
    n425 --> n442
    n395 --> n443
    n425 --> n443
    n487 --> n496
    n488 --> n496
    n442 --> n463
    n405 --> n408
    n407 --> n408
    n449 --> n464
    n398 --> n399
    n475 --> n500
    n494 --> n500
    n461 --> n479
    n460 --> n480
    n472 --> n480
    n453 --> n465
    n444 --> n465
    n430 --> n444
    n409 --> n413
    n466 --> n481
    n451 --> n466
    n449 --> n466
    n492 --> n501
    n501 --> n504
    n478 --> n504
    n478 --> n497
    n481 --> n497
    n474 --> n482
    n474 --> n483
    n416 --> n427
    n417 --> n428
    n420 --> n428
    n468 --> n484
    n411 --> n414
    n401 --> n406
    n406 --> n409
    n412 --> n415
    n412 --> n416
    n419 --> n429
    n413 --> n429
    n414 --> n430
    n436 --> n445
    n471 --> n485
    n435 --> n446
    n451 --> n467
    n449 --> n467
    n439 --> n447
    n447 --> n468
    n448 --> n468
    n439 --> n448
    n450 --> n469
    n420 --> n431
    n443 --> n470
    n429 --> n449
    n439 --> n450
    n430 --> n450
    n424 --> n451
    n429 --> n451
    n454 --> n471
    n420 --> n432
    n412 --> n417
    n417 --> n452
    n428 --> n452
    n443 --> n472
    n468 --> n486
    n416 --> n433
    n396 --> n397
    n406 --> n410
    n420 --> n434
    n430 --> n453
    n415 --> n435
    n421 --> n435
    n415 --> n436
    n421 --> n436
    n418 --> n437
    n414 --> n437
    n408 --> n437
    n396 --> n398
    n442 --> n473
    n492 --> n502
    n492 --> n503
    n411 --> n418
    n407 --> n411
    n405 --> n411
    n429 --> n454
    n397 --> n400
    n410 --> n419
    n449 --> n474
    n451 --> n474
    n431 --> n455
    n412 --> n420
    n404 --> n412
    n397 --> n401
    n398 --> n402
    n433 --> n456
    n438 --> n456
    n424 --> n475
    n450 --> n475
    n470 --> n487
    n472 --> n487
    n460 --> n488
    n472 --> n488
    n416 --> n438
    n437 --> n457
    n462 --> n489
    n414 --> n439
    n398 --> n403
    n412 --> n421
    n432 --> n458
    n460 --> n498
    n480 --> n498
    n465 --> n490
    n459 --> n491
    n451 --> n476
    n449 --> n476
    n400 --> n407
    n405 x--x n407
    n459 x--x n462
    n424 x--x n429
    n499 x--x n467
    n478 x--x n481
    n442 x--x n443
    n479 x--x n489
    n465 x--x n468
    n482 x--x n483
    n428 x--x n432
    n449 x--x n451
    n449 x--x n454
    n396 x--x n40
    n451 x--x n454
    n417 x--x n420
    n397 x--x n398
    n435 x--x n436
    n400 x--x n401
```

# GER_oppose_hitler

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n505(("GER_oppose_hitler"))
        n40["GER_remilitarize_the_rhineland"]
    end
    subgraph tier_1["Tier 1"]
        n506{"GER_secure_the_new_state"}
    end
    subgraph tier_2["Tier 2"]
        n507["GER_reestablish_free_elections"]
        n508["GER_revive_the_kaiserreich"]
    end
    subgraph tier_3["Tier 3"]
        n509["GER_rebuild_the_nation"]
        n510{"GER_return_of_the_kaiser"}
        n511["GER_the_monarchy_compromise"]
    end
    subgraph tier_4["Tier 4"]
        n512["GER_a_new_and_better_germany"]
        n513{"GER_expatriate_the_communists"}
        n514["GER_fan_the_prussian_militarism"]
        n515{"GER_focus_on_the_true_enemy"}
        n516["GER_reverse_the_brain_drain"]
        n517["GER_see_to_the_eastern_front"]
        n518["GER_the_great_red_menace"]
    end
    subgraph tier_5["Tier 5"]
        n519["GER_accept_british_naval_dominance"]
        n520["GER_bulwark_against_bolshevism"]
        n521["GER_rebuild_the_high_seas_fleet"]
        n522["GER_safeguard_the_baltic"]
    end
    subgraph tier_6["Tier 6"]
        n523["GER_ally_the_shade"]
        n524["GER_central_european_alliance"]
        n525["GER_danzig_for_guarantees"]
        n526["GER_our_place_in_the_sun"]
        n527["GER_support_the_finns"]
    end
    subgraph tier_7["Tier 7"]
        n528["GER_anti_comintern_pact_unaligned"]
        n529["GER_carte_blanche_for_alsace_and_french_colonies"]
        n530["GER_danubian_membership"]
        n531["GER_low_countries_membership"]
        n532["GER_prepare_for_the_next_blockade"]
        n533["GER_pride_of_the_modern_germany"]
        n534["GER_scandinavian_membership"]
        n535["GER_shared_rd_programs"]
        n536["GER_the_central_powers"]
    end
    subgraph tier_8["Tier 8"]
        n537["GER_anti_soviet_pact_unaligned"]
        n538["GER_baltic_membership"]
        n539["GER_break_the_anglo_french_colonial_hegemony"]
        n540["GER_bypass_maginot_in_the_south"]
        n541["GER_danubian_expansion"]
        n542["GER_finnish_membership"]
        n543["GER_no_reds_in_western_europe"]
        n544["GER_polish_membership"]
        n545["GER_pool_technical_know_how"]
        n546["GER_prepare_italian_coup"]
        n547["GER_rekindle_imperial_sentiment"]
        n548["GER_the_mannheim_project"]
    end
    subgraph tier_9["Tier 9"]
        n549["GER_assassinate_mussolini"]
        n550["GER_no_balkan_communism"]
        n551["GER_schlieffen_once_more"]
        n552["GER_strike_at_the_source"]
        n553["GER_tackle_the_communist_threat"]
    end
    subgraph tier_10["Tier 10"]
        n554["GER_reinstate_imperial_possessions"]
        n555["GER_the_iberian_problem"]
    end
    n509 --> n512
    n513 --> n519
    n519 --> n523
    n527 --> n528
    n525 --> n528
    n528 --> n537
    n546 --> n549
    n534 --> n538
    n532 --> n539
    n514 --> n520
    n512 --> n520
    n529 --> n540
    n523 --> n529
    n518 --> n524
    n520 --> n524
    n530 --> n541
    n524 --> n530
    n517 --> n525
    n520 --> n525
    n510 --> n513
    n509 --> n514
    n534 --> n542
    n510 --> n515
    n524 --> n531
    n541 --> n550
    n531 --> n543
    n521 --> n526
    n534 --> n544
    n535 --> n545
    n526 --> n532
    n536 --> n546
    n526 --> n533
    n515 --> n521
    n508 --> n509
    n507 --> n509
    n506 --> n507
    n551 --> n554
    n540 --> n554
    n536 --> n547
    n508 --> n510
    n511 --> n516
    n506 --> n508
    n517 --> n522
    n524 --> n534
    n539 --> n551
    n505 --> n506
    n510 --> n517
    n516 --> n535
    n524 --> n535
    n538 --> n552
    n544 --> n552
    n542 --> n552
    n522 --> n527
    n537 --> n553
    n529 --> n553
    n526 --> n536
    n511 --> n518
    n553 --> n555
    n535 --> n548
    n534 --> n548
    n507 --> n511
    n519 x--x n521
    n513 x--x n515
    n505 x--x n40
    n507 x--x n508
```

# GER_oppose_hitler_ww

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35["GER_die_letzte_verschwoerung"]
        n38(("GER_oppose_hitler_ww"))
        n40["GER_remilitarize_the_rhineland"]
    end
    subgraph tier_1["Tier 1"]
        n46["GER_rally_the_nation"]
        n556{"GER_tend_to_the_future_of_germany"}
    end
    subgraph tier_2["Tier 2"]
        n48["GER_GER_fate_of_nazism"]
        n557{"GER_monarchist_sentiment"}
        n57["GER_rebuild_the_nation_ww"]
        n558["GER_start_the_proletarian_revolution"]
    end
    subgraph tier_3["Tier 3"]
        n559["GER_formalize_the_intelligence_wing"]
        n560["GER_ressurect_the_red_front_fighters_league"]
        n80["GER_revitalize_the_nation"]
        n561{"GER_revive_the_kaiserreich_ww"}
        n562["GER_the_monarchy_compromise_ww"]
        n563{"GER_the_peoples_victory"}
        n564{"GER_weltpolitik"}
    end
    subgraph tier_4["Tier 4"]
        n565["GER_accept_british_naval_dominance_ww"]
        n566["GER_effective_operations"]
        n96["GER_end_the_german_brain_drain"]
        n567["GER_form_the_stasi"]
        n568["GER_legacy_of_the_spartacus_league"]
        n569["GER_military_dictatorship"]
        n570["GER_political_commissars"]
        n571["GER_proletarian_dictatorship"]
        n572["GER_re_establish_free_elections_ww"]
        n573{"GER_realpolitik"}
        n574["GER_reorganize_nationale_volksarmee"]
        n575["GER_return_of_the_kaiser_ww"]
        n576["GER_sign_the_second_treaty_of_berlin"]
        n577["GER_the_second_naval_race"]
    end
    subgraph tier_5["Tier 5"]
        n578["GER_assemble_red_orchestra"]
        n579["GER_assist_our_eastern_comrades"]
        n580{"GER_ban_political_uniforms"}
        n581["GER_carve_up_congo"]
        n582["GER_closer_sino_germanic_relations"]
        n583["GER_defense_treaty_with_the_soviet"]
        n584{"GER_demand_the_return_of_southern_jutland"}
        n585["GER_expatriate_the_communists_ww"]
        n586["GER_fan_prussian_militarism"]
        n587["GER_industrial_cooperation"]
        n588["GER_intervene_in_spain"]
        n589["GER_invite_scientists_back"]
        n590{"GER_mitteleuropa"}
        n591["GER_prepare_for_the_next_naval_blockade"]
        n125["GER_r56_pool_technical_know_how"]
        n126["GER_r56_shared_r_and_d_programs"]
        n592["GER_rapid_army_expansion"]
        n593["GER_re_ratify_the_locarno_treaty"]
        n594["GER_rebuild_the_high_seas_fleet_ww"]
        n595["GER_restore_the_brest_litovsk_borders"]
        n596["GER_reverse_the_brain_drain_ww"]
        n597{"GER_see_to_the_eastern_front_ww"}
        n598["GER_social_ownership"]
        n599["GER_state_controlled_economy"]
    end
    subgraph tier_6["Tier 6"]
        n600["GER_all_for_the_front"]
        n601{"GER_anglo_germanic_defense_pact"}
        n602{"GER_break_anglo_french_colonial_hegemony_ww"}
        n603{"GER_brothers_in_arms"}
        n604["GER_central_planning"]
        n605["GER_civil_liberties"]
        n606["GER_danzig_for_guarantees_ww"]
        n607["GER_embrace_democratic_institutions"]
        n608["GER_embrace_liberal_leanings"]
        n609["GER_franco_germanic_pact"]
        n610["GER_glorious_mechanical_machinations"]
        n611["GER_industrial_investments"]
        n612["GER_liberate_austria"]
        n613["GER_memel_ultimatum"]
        n614["GER_nationalize_industries"]
        n615["GER_offer_trade_proposal"]
        n616["GER_pool_technical_know_how_ww"]
        n617["GER_prussian_artillery"]
        n148["GER_r56_mannheim_project"]
        n618["GER_re_establish_the_landwehr"]
        n619["GER_re_form_the_freikorps"]
        n620{"GER_reject_the_locarno_treaty"}
        n621["GER_resource_trade"]
        n622["GER_restore_eastern_imperial_possessions"]
        n623["GER_safeguard_poland"]
        n624["GER_safeguard_the_baltic_ww"]
        n625["GER_send_military_aid"]
        n626["GER_shared_rd_programs_ww"]
        n627["GER_spheres_of_influence"]
        n628["GER_strive_for_conservative_values"]
        n629["GER_tech_sharing"]
        n630{"GER_the_austrian_question"}
        n631["GER_tributes_for_guarantees"]
    end
    subgraph tier_7["Tier 7"]
        n632["GER_align_czechoslovakia"]
        n633["GER_anglo_germanic_cooperation_program"]
        n634["GER_asian_allies"]
        n635["GER_backdoor_negotiations"]
        n636["GER_build_the_eastern_bulwark"]
        n637{"GER_carte_blanche_for_alsace_and_french_colonies_ww"}
        n638["GER_carve_up_czechoslovakia"]
        n639["GER_czechoslovakia"]
        n640["GER_demand_further_polish_concessions"]
        n641["GER_demand_lithuanian_integration"]
        n642["GER_expand_african_reach"]
        n643["GER_factories_for_resources"]
        n644["GER_form_agricultural_cooperatives"]
        n645["GER_glory_to_the_imperial_army"]
        n646["GER_labor_rights_and_union_stuff"]
        n647["GER_launch_sino_germanic_joint_research_program"]
        n648["GER_liberate_italy"]
        n649["GER_liberate_oppressed_people"]
        n650["GER_offer_military_production_support"]
        n651["GER_our_place_in_the_sun_ww"]
        n652{"GER_petition_for_the_return_of_old_colonies"}
        n653["GER_poland"]
        n654["GER_rekindle_imperial_sentiment_ww"]
        n655["GER_request_the_return_of_french_held_colonies"]
        n656["GER_request_the_return_of_qingdao"]
        n657["GER_schlieffen_once_more_ww"]
        n658["GER_send_volunteers"]
        n659["GER_spark_the_flame_of_revolution"]
        n660["GER_strengthen_the_welfare_state"]
        n661["GER_support_the_finns_ww"]
        n662["GER_the_german_stakhanovite_movement"]
        n663["GER_the_mannheim_project_ww"]
    end
    subgraph tier_8["Tier 8"]
        n664["GER_african_allies"]
        n665["GER_ally_white_russian_forces"]
        n666["GER_bypass_maginot_in_the_south_ww"]
        n667["GER_democratic_shield"]
        n668["GER_effectivize_the_volkswerke"]
        n669["GER_establish_a_customs_union"]
        n670["GER_establish_eastern_grand_duchies"]
        n671["GER_expand_pacific_holdings"]
        n672["GER_expand_social_welfare"]
        n673["GER_hold_joint_military_drills"]
        n674["GER_hungary"]
        n675["GER_mitteleuropa_cooperation_sphere"]
        n676["GER_protect_the_revolution"]
        n677["GER_realize_mittelafrika"]
        n678["GER_support_the_proletarian_uprising"]
        n679["GER_sway_the_balkans"]
        n680["GER_the_end_to_fascist_europe"]
        n681["GER_the_first_berlin_award"]
        n682{"GER_the_sino_germanic_pact"}
        n683["GER_unify_west_africa"]
    end
    subgraph tier_9["Tier 9"]
        n684["GER_divide_and_conquer"]
        n685["GER_establish_volkskommissariats"]
        n686["GER_establish_western_grand_duchies"]
        n687["GER_extend_mitteleuropas_bounderies"]
        n688["GER_incorporate_the_polish_rump_state"]
        n689["GER_integrated_economies"]
        n690["GER_puppet_finland"]
        n691["GER_reinstate_imperial_possessions_ww"]
        n692["GER_strengthen_the_proletarian_international"]
        n693["GER_subduing_the_baltic_states"]
        n694["GER_the_northern_shield"]
        n695["GER_the_proletarian_legion"]
        n696{"GER_the_second_berlin_award"}
        n697{"GER_trade_agreements"}
        n698["GER_womens_rights_and_equality"]
    end
    subgraph tier_10["Tier 10"]
        n699{"GER_align_italy"}
        n700{"GER_conquer_italy"}
        n701{"GER_european_confederation"}
        n702["GER_industrialize_volkskommissariats"]
        n703["GER_instill_german_discipline"]
        n704["GER_integrate_western_german_speakers"]
        n705{"GER_prepare_italian_coup_ww"}
        n706["GER_reach_out_to_scandinavia"]
        n707["GER_red_europe"]
        n708["GER_strike_eastward"]
    end
    subgraph tier_11["Tier 11"]
        n709["GER_assassinate_mussolini_ww"]
        n710["GER_bring_turkey_into_the_fold"]
        n711["GER_end_european_communism"]
        n712["GER_german_hegemony_in_the_middle_east"]
        n713["GER_integrate_subjects_economies"]
        n714["GER_proletarian_solidarity"]
        n715["GER_restore_the_holy_roman_empire"]
        n716["GER_root_out_imperialism"]
    end
    subgraph tier_12["Tier 12"]
        n717["GER_align_south_america"]
        n718["GER_hegemony_over_europe"]
        n719["GER_instigate_middle_eastern_revolutions"]
        n720["GER_integrate_volkskommissariats"]
    end
    subgraph tier_13["Tier 13"]
        n721["GER_strike_at_the_rising_sun"]
        n722["GER_wage_war_on_capitalism"]
    end
    n46 --> n48
    n564 --> n565
    n642 --> n664
    n630 --> n632
    n603 --> n632
    n697 --> n699
    n716 --> n717
    n591 --> n600
    n650 --> n665
    n649 --> n665
    n636 --> n665
    n601 --> n633
    n581 --> n601
    n602 --> n634
    n705 --> n709
    n567 --> n578
    n566 --> n578
    n568 --> n579
    n571 --> n579
    n620 --> n635
    n572 --> n580
    n594 --> n602
    n700 --> n710
    n701 --> n710
    n699 --> n710
    n705 --> n710
    n590 --> n603
    n624 --> n636
    n631 --> n636
    n606 --> n636
    n623 --> n636
    n620 --> n666
    n637 --> n666
    n601 --> n637
    n565 --> n581
    n630 --> n638
    n603 --> n638
    n599 --> n604
    n598 --> n605
    n565 --> n582
    n577 --> n582
    n696 --> n700
    n697 --> n700
    n627 --> n639
    n597 --> n606
    n576 --> n583
    n622 --> n640
    n613 --> n641
    n575 --> n584
    n569 --> n584
    n660 --> n667
    n682 --> n684
    n559 --> n566
    n644 --> n668
    n646 --> n668
    n598 --> n607
    n580 --> n608
    n708 --> n711
    n80 --> n96
    n632 --> n669
    n640 --> n670
    n641 --> n670
    n676 --> n685
    n635 --> n686
    n657 --> n686
    n666 --> n686
    n689 --> n701
    n602 --> n642
    n652 --> n671
    n644 --> n672
    n646 --> n672
    n575 --> n585
    n569 --> n585
    n669 --> n687
    n650 --> n687
    n649 --> n687
    n636 --> n687
    n629 --> n643
    n621 --> n643
    n575 --> n586
    n569 --> n586
    n614 --> n644
    n559 --> n567
    n558 --> n559
    n593 --> n609
    n700 --> n712
    n701 --> n712
    n699 --> n712
    n705 --> n712
    n589 --> n610
    n619 --> n645
    n618 --> n645
    n716 --> n718
    n650 --> n673
    n649 --> n673
    n636 --> n673
    n639 --> n674
    n653 --> n674
    n640 --> n688
    n670 --> n688
    n576 --> n587
    n582 --> n611
    n685 --> n702
    n716 --> n719
    n685 --> n703
    n702 --> n713
    n703 --> n713
    n713 --> n720
    n686 --> n704
    n691 --> n704
    n669 --> n689
    n675 --> n689
    n568 --> n588
    n571 --> n588
    n575 --> n589
    n614 --> n646
    n611 --> n647
    n563 --> n568
    n598 --> n612
    n599 --> n612
    n612 --> n648
    n624 --> n649
    n631 --> n649
    n606 --> n649
    n623 --> n649
    n595 --> n613
    n561 --> n569
    n573 --> n590
    n638 --> n675
    n632 --> n675
    n556 --> n557
    n598 --> n614
    n599 --> n614
    n624 --> n650
    n631 --> n650
    n606 --> n650
    n623 --> n650
    n593 --> n615
    n602 --> n651
    n601 --> n652
    n627 --> n653
    n560 --> n570
    n596 --> n616
    n569 --> n591
    n696 --> n705
    n563 --> n571
    n707 --> n714
    n605 --> n676
    n607 --> n676
    n659 --> n676
    n589 --> n617
    n591 --> n617
    n661 --> n690
    n670 --> n690
    n125 --> n148
    n126 --> n148
    n96 --> n125
    n96 --> n126
    n38 --> n46
    n35 --> n46
    n574 --> n592
    n570 --> n592
    n562 --> n572
    n586 --> n618
    n586 --> n619
    n572 --> n593
    n687 --> n706
    n642 --> n677
    n562 --> n573
    n561 --> n573
    n577 --> n594
    n46 --> n57
    n695 --> n707
    n692 --> n707
    n635 --> n691
    n657 --> n691
    n666 --> n691
    n573 --> n620
    n584 --> n620
    n603 --> n654
    n560 --> n574
    n609 --> n655
    n611 --> n656
    n625 --> n656
    n587 --> n621
    n558 --> n560
    n595 --> n622
    n573 --> n595
    n700 --> n715
    n705 --> n715
    n561 --> n575
    n572 --> n596
    n48 --> n80
    n57 --> n80
    n557 --> n561
    n680 --> n716
    n707 --> n716
    n597 --> n623
    n597 --> n624
    n620 --> n657
    n573 --> n597
    n582 --> n625
    n625 --> n658
    n596 --> n626
    n563 --> n576
    n568 --> n598
    n612 --> n659
    n599 --> n627
    n583 --> n627
    n556 --> n558
    n571 --> n599
    n678 --> n692
    n628 --> n660
    n608 --> n660
    n719 --> n721
    n693 --> n708
    n673 --> n708
    n580 --> n628
    n670 --> n693
    n624 --> n661
    n631 --> n661
    n613 --> n661
    n659 --> n678
    n632 --> n679
    n587 --> n629
    n38 --> n556
    n590 --> n630
    n648 --> n680
    n638 --> n681
    n604 --> n662
    n626 --> n663
    n616 --> n663
    n557 --> n562
    n674 --> n694
    n558 --> n563
    n678 --> n695
    n676 --> n695
    n681 --> n696
    n564 --> n577
    n656 --> n682
    n675 --> n697
    n597 --> n631
    n652 --> n683
    n717 --> n722
    n557 --> n564
    n672 --> n698
    n668 --> n698
    n565 x--x n577
    n632 x--x n638
    n699 x--x n700
    n699 x--x n705
    n635 x--x n666
    n635 x--x n657
    n710 x--x n712
    n603 x--x n630
    n666 x--x n657
    n637 x--x n620
    n700 x--x n705
    n606 x--x n623
    n684 x--x n671
    n684 x--x n651
    n608 x--x n628
    n671 x--x n651
    n568 x--x n571
    n569 x--x n575
    n557 x--x n558
    n38 x--x n40
    n595 x--x n597
    n561 x--x n562
    n624 x--x n631
```

# GER_pass_the_beck_constiution_copy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n163["GER_dstp_in_coalition"]
        n164{"GER_dvu_in_coalition"}
        n232["GER_form_the_stasi_new"]
        n140["GER_hold_new_elections"]
        n342["GER_introduce_the_jugendweihe"]
        n243["GER_limited_reconciliation"]
        n169["GER_nraf_in_coalition"]
        n39(("GER_pass_the_beck_constiution_copy"))
        n174["GER_spd_in_coalition"]
        n270["GER_towards_state_atheism"]
    end
    subgraph tier_1["Tier 1"]
        n162{"GER_dnvp_in_coalition"}
        n176["GER_zentrum_in_coalition"]
    end
    subgraph tier_2["Tier 2"]
        n178["GER_adenauers_chance"]
        n191["GER_goerdelers_new_party"]
        n192{"GER_highten_nationalist_rethoric"}
        n193["GER_hugenburgs_legacy"]
        n200["GER_positive_christianty"]
        n203["GER_readdress_the_kaiserfrage"]
        n206{"GER_revive_gestapo_remnants"}
        n209["GER_the_legacy_of_the_sozialistengesetze"]
        n210["GER_the_party_under_stegerwald"]
        n212["GER_undo_the_secularization_of_germany"]
        n213["GER_utilize_pro_democratic_propaganda"]
        n215["GER_wirths_new_zentrum"]
    end
    subgraph tier_3["Tier 3"]
        n218["GER_an_eye_towards_the_east"]
        n219["GER_apply_the_reichskonkordat_to_the_republic"]
        n225["GER_combat_the_reactionary"]
        n230["GER_expand_the_kaisers_duties"]
        n233["GER_foster_christian_democracy"]
        n235["GER_fully_rebuild_the_secret_police"]
        n245["GER_manipulate_the_churches"]
        n248["GER_organize_german_labor"]
        n250["GER_politicize_the_trade_unions"]
        n251["GER_proper_agrarian_policy"]
        n253["GER_radicalize_german_nationalism"]
        n255["GER_rebuild_the_prussian_bastion"]
        n256["GER_rebuild_the_shattered_zentrum"]
        n257["GER_rehabilitate_mueller"]
        n258["GER_restore_the_state_churches"]
        n260["GER_sensible_fiscal_policy"]
        n262["GER_strengthen_the_responsible_elites"]
        n264["GER_the_fight_against_german_antisemitism"]
        n265["GER_the_new_federalism"]
        n267["GER_the_socialist_traitor"]
        n274["GER_weaken_the_presidents_power"]
        n275["GER_work_towards_fiscal_stability"]
    end
    subgraph tier_4["Tier 4"]
        n277["GER_a_coup_in_all_but_name"]
        n278["GER_a_new_age_of_peace"]
        n281["GER_a_second_restoration"]
        n282["GER_a_time_for_protectionism"]
        n283["GER_abandon_the_post_alltogether"]
        n284["GER_alliance_with_the_junkers"]
        n285["GER_bring_about_a_new_social_order"]
        n286["GER_bring_back_einstein"]
        n290["GER_consultations_with_the_experts"]
        n296["GER_engrain_antiurbanism"]
        n297["GER_ensure_a_loyal_clergyship"]
        n299["GER_federalism_a_hedge_against_radicalism"]
        n303["GER_improve_railway_economics"]
        n304["GER_increase_municipal_autonomy"]
        n306["GER_integrate_our_new_lands"]
        n310["GER_national_economic_coordination"]
        n315["GER_strike_the_baltic"]
        n321["GER_upkeep_german_order"]
        n322["GER_watch_the_churches"]
    end
    subgraph tier_5["Tier 5"]
        n324["GER_a_new_era_of_german_science"]
        n325["GER_a_patriotic_german_church"]
        n327["GER_an_era_of_german_wealth"]
        n329["GER_build_germany_from_the_apartment_up"]
        n332["GER_corporatism_with_catholic_characteristics"]
        n333["GER_demand_state_approval_for_clergy"]
        n336["GER_ensure_permanent_food_security"]
        n341["GER_intertwine_the_state_and_the_church"]
        n344["GER_prioritise_the_rheinland"]
        n347["GER_restore_the_old_estates"]
        n350["GER_technocracy_with_strong_limits"]
        n352["GER_the_spirit_of_blut_and_boden"]
    end
    subgraph tier_6["Tier 6"]
        n359["GER_ensure_the_gradual_withering_away_of_religion"]
        n360["GER_germany_glorious_as_it_once_was"]
        n361["GER_help_the_church_permeate_everyday_german_life"]
        n362["GER_the_end_of_class_warfare"]
    end
    n230 --> n277
    n225 --> n278
    n233 --> n278
    n286 --> n324
    n297 --> n325
    n230 --> n281
    n251 --> n282
    n274 --> n283
    n176 --> n178
    n164 --> n178
    n251 --> n284
    n310 --> n327
    n192 --> n218
    n212 --> n219
    n250 --> n285
    n248 --> n285
    n264 --> n286
    n299 --> n329
    n304 --> n329
    n215 --> n225
    n178 --> n225
    n275 --> n290
    n285 --> n332
    n322 --> n333
    n140 --> n162
    n39 --> n162
    n251 --> n296
    n257 --> n297
    n245 --> n297
    n306 --> n336
    n342 --> n359
    n333 --> n359
    n203 --> n230
    n265 --> n299
    n215 --> n233
    n178 --> n233
    n206 --> n235
    n296 --> n360
    n347 --> n360
    n352 --> n360
    n162 --> n191
    n164 --> n191
    n341 --> n361
    n162 --> n192
    n169 --> n192
    n164 --> n192
    n164 --> n193
    n162 --> n193
    n275 --> n303
    n265 --> n304
    n218 --> n306
    n285 --> n341
    n258 --> n341
    n200 --> n245
    n260 --> n310
    n210 --> n248
    n210 --> n250
    n169 --> n200
    n162 --> n200
    n304 --> n344
    n193 --> n251
    n192 --> n253
    n164 --> n203
    n162 --> n203
    n213 --> n255
    n178 --> n256
    n200 --> n257
    n284 --> n347
    n212 --> n258
    n164 --> n206
    n169 --> n206
    n162 --> n206
    n191 --> n260
    n178 --> n262
    n218 --> n315
    n290 --> n350
    n303 --> n350
    n332 --> n362
    n191 --> n264
    n169 --> n209
    n164 --> n209
    n162 --> n209
    n178 --> n265
    n176 --> n210
    n164 --> n210
    n215 --> n267
    n282 --> n352
    n162 --> n212
    n176 --> n212
    n164 --> n212
    n262 --> n321
    n256 --> n321
    n174 --> n213
    n163 --> n213
    n176 --> n213
    n270 --> n322
    n235 --> n322
    n232 --> n322
    n213 --> n274
    n176 --> n215
    n215 --> n275
    n140 --> n176
    n39 --> n176
    n232 x--x n235
    n191 x--x n193
    n243 x--x n253
```

# GER_prioritize_economic_growth

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n723["GER_autarky_efforts"]
        n724(("GER_prioritize_economic_growth"))
        n725["GER_the_four_year_plan"]
    end
    subgraph tier_1["Tier 1"]
        n726["GER_construct_the_reichsautobahn"]
        n727["GER_currency_reforms"]
        n728["GER_rally_the_technocrats"]
    end
    subgraph tier_2["Tier 2"]
        n729["GER_build_defense_industry_r56"]
        n730["GER_build_the_rur_dam"]
        n731["GER_housing_developments"]
        n732["GER_kdf_wagen_factories"]
        n733["GER_lower_taxes"]
        n734["GER_tie_the_aristocracy_into_the_nsdap"]
        n735["GER_trade_deal_with_sweden"]
    end
    subgraph tier_3["Tier 3"]
        n736{"GER_abolish_price_controls"}
        n737["GER_develop_heraeus_facilities"]
        n738["GER_expand_the_reichsautobahn_east"]
        n739["GER_expand_the_reichsautobahn_south"]
        n740{"GER_industrial_expansion"}
        n741["GER_stabilize_the_heavy_industry"]
        n742["GER_war_production_r56"]
        n743{"GER_workers_rights"}
    end
    subgraph tier_4["Tier 4"]
        n744["GER_agricultural_reforms"]
        n745["GER_exploit_trade_dependence"]
        n746["GER_invest_in_vereinigte_stahlwerke"]
        n747{"GER_liberalize_the_economy"}
        n748{"GER_limited_social_reform"}
        n749["GER_secure_a_full_economic_recovery"]
        n750{"GER_towards_a_workers_democracy"}
        n751["GER_war_fueled_economy_building"]
    end
    subgraph tier_5["Tier 5"]
        n752["GER_a_planned_economy"]
        n753["GER_maintain_state_influence_on_the_economy"]
        n754["GER_move_towards_full_deregulation"]
        n755["GER_support_the_families"]
        n756["GER_support_the_industries"]
        n757["GER_support_the_workers"]
        n758["GER_urbanization"]
        n759["GER_wirtschaftswunder"]
    end
    subgraph tier_6["Tier 6"]
        n760["GER_build_defense_industry"]
        n761["GER_enact_drastic_tax_cuts"]
        n762{"GER_fight_employment_discrimination"}
        n763["GER_help_the_worker_through_his_company"]
        n764["GER_mass_production"]
        n765{"GER_set_prices_in_stone"}
        n766["GER_state_economy_simbiosis"]
        n767{"GER_strengthen_the_bedrock_of_the_family"}
    end
    subgraph tier_7["Tier 7"]
        n768["GER_achieve_secure_long_term_economic_growth"]
        n769["GER_become_the_model_social_market_economy"]
        n770["GER_socialism_with_german_characteristics"]
        n771["GER_war_production"]
    end
    n750 --> n752
    n733 --> n736
    n763 --> n768
    n766 --> n768
    n761 --> n768
    n740 --> n744
    n743 --> n744
    n767 --> n769
    n762 --> n769
    n759 --> n760
    n727 --> n729
    n726 --> n730
    n727 --> n730
    n724 --> n726
    n725 --> n726
    n724 --> n727
    n732 --> n737
    n754 --> n761
    n732 --> n738
    n732 --> n739
    n736 --> n745
    n757 --> n762
    n756 --> n763
    n727 --> n731
    n731 --> n740
    n733 --> n740
    n740 --> n746
    n736 --> n746
    n726 --> n732
    n736 --> n747
    n740 --> n747
    n743 --> n748
    n740 --> n748
    n727 --> n733
    n747 --> n753
    n759 --> n764
    n747 --> n754
    n724 --> n728
    n741 --> n749
    n752 --> n765
    n762 --> n770
    n765 --> n770
    n729 --> n741
    n734 --> n741
    n753 --> n766
    n755 --> n767
    n748 --> n755
    n748 --> n756
    n748 --> n757
    n750 --> n757
    n727 --> n734
    n743 --> n750
    n726 --> n735
    n723 --> n735
    n744 --> n758
    n742 --> n751
    n741 --> n751
    n764 --> n771
    n760 --> n771
    n729 --> n742
    n746 --> n759
    n744 --> n759
    n731 --> n743
    n752 x--x n757
    n769 x--x n770
    n747 x--x n748
    n747 x--x n750
    n748 x--x n750
    n753 x--x n754
    n724 x--x n725
    n755 x--x n756
    n755 x--x n757
    n756 x--x n757
```

# GER_remilitarize_the_rhineland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n425{"GER_asia_department"}
        n35["GER_die_letzte_verschwoerung"]
        n396["GER_kill_hitler"]
        n505["GER_oppose_hitler"]
        n38["GER_oppose_hitler_ww"]
        n40{"GER_remilitarize_the_rhineland"}
    end
    subgraph tier_1["Tier 1"]
        n395{"GER_anti_comintern_pact"}
        n442["GER_befriend_china"]
        n772{"GER_bribe_senior_officers"}
        n773{"GER_fuhrerprinzip"}
        n37["GER_heed_von_neuraths_concerns"]
        n774["GER_legion_condor"]
        n775{"GER_reorganize_the_wehrmacht"}
    end
    subgraph tier_2["Tier 2"]
        n460["GER_ally_chiang_kai_shek"]
        n776{"GER_anschluss"}
        n777["GER_anti_soviet_pact"]
        n778["GER_army_indoctrination"]
        n779["GER_ascension_of_goebbels"]
        n780["GER_ascension_of_goring"]
        n781{"GER_ascension_of_himmler"}
        n782["GER_ascension_of_speer"]
        n783["GER_ascension_of_todt"]
        n784["GER_autonomy_in_the_kriegsschulen"]
        n443["GER_befriend_japan"]
        n463["GER_claim_old_colonies_in_the_east"]
        n785["GER_demonstration_of_military_achievements"]
        n786["GER_expand_ss_recruitment"]
        n787["GER_molotov_ribbentrop_pact"]
        n788["GER_party_chancellor_bormann"]
        n789["GER_party_chancellor_hess"]
        n473["GER_re_establish_german_control_over_qingdao"]
        n47{"GER_step_back_into_the_international_community"}
        n790["GER_uplift_the_rosenberg_office"]
        n791["GER_war_preparations"]
        n792["GER_war_with_the_ussr"]
    end
    subgraph tier_3["Tier 3"]
        n793["GER_an_invincible_army"]
        n51["GER_an_outstreched_arm_towards_the_east"]
        n794{"GER_befriend_czechoslovakia"}
        n795["GER_befriend_turkey"]
        n52{"GER_build_a_pakt_around_berlin"}
        n796["GER_demand_slovenia"]
        n797["GER_demand_sudetenland"]
        n798{"GER_employ_philipp_holzmann"}
        n799["GER_expand_gestapo"]
        n800["GER_expand_ss_security_duties"]
        n801["GER_expand_the_truppenschulen"]
        n802{"GER_form_organization_todt"}
        n53["GER_heavy_handed_foreign_policy"]
        n803["GER_innovative_warfare"]
        n470["GER_japanese_naval_cooperation"]
        n804["GER_ministry_of_public_enlightenment"]
        n472["GER_negotiate_old_colonies_in_the_east"]
        n805["GER_optimize_reich_labour_service"]
        n806["GER_prepare_for_the_next_blockade_ww"]
        n807{"GER_prioritize_the_four_year_plan"}
        n55{"GER_reaffirm_territorial_claims"}
        n56{"GER_reapproach_the_west"}
        n808{"GER_reassert_eastern_claims"}
        n809["GER_reorganize_secret_services"]
        n810["GER_resolve_the_balkan_flank"]
        n811["GER_strafbataillon"]
        n812["GER_support_a_coup_in_liechtenstein"]
        n813["GER_support_finland"]
        n814["GER_the_final_blow_to_communism"]
        n815["GER_the_triumphant_will"]
        n816{"GER_treaty_with_the_ussr"}
    end
    subgraph tier_4["Tier 4"]
        n62["GER_a_europe_around_the_reich"]
        n63["GER_a_europe_of_the_fatherlands"]
        n64["GER_a_human_face_for_europe"]
        n817["GER_absorb_the_abwehr"]
        n818["GER_alliance_with_the_ussr"]
        n819["GER_autonomous_organization_todt"]
        n480["GER_create_asian_reichskommissariat"]
        n820{"GER_danzig_or_war"}
        n66["GER_encircle_the_entente_powers"]
        n67["GER_end_the_austria_debate"]
        n821["GER_expand_claims_in_baltic"]
        n822["GER_first_ljubljana_award"]
        n823["GER_first_vienna_award"]
        n824["GER_fund_the_film_department"]
        n825["GER_glorify_party_rallies"]
        n826{"GER_influence_the_baltics"}
        n827["GER_integrate_czechoslovakia"]
        n69["GER_liberation_for_the_sudetendeutsche"]
        n828["GER_plenipotentiary_of_armaments"]
        n829["GER_plenipotentiary_of_the_four_year_plan"]
        n830["GER_rally_the_industrialists"]
        n77{"GER_rekindle_the_franco_german_rivalry"}
        n78["GER_renegotiate_versailles_new"]
        n82["GER_secure_western_science_funding"]
        n487["GER_sentinels_of_the_pacific"]
        n83{"GER_solve_the_danzig_issue"}
        n488["GER_south_east_asian_natural_wealth"]
        n831["GER_strengthen_the_waffen_ss"]
        n832["GER_subversive_infiltrators"]
        n833["GER_the_supreme_leader"]
    end
    subgraph tier_5["Tier 5"]
        n89["GER_align_the_balkans"]
        n496["GER_blitzkrieg_across_the_pacific"]
        n93["GER_clear_the_facist_lair"]
        n97["GER_establish_the_european_coal_and_steel_community"]
        n834{"GER_fate_of_czechoslovakia"}
        n835{"GER_fate_of_yugoslavia"}
        n101["GER_germans_everywhere_united"]
        n836{"GER_hegemony_of_the_ss"}
        n103["GER_increase_factional_defenses"]
        n837{"GER_integration_of_puppet_economies"}
        n105["GER_move_to_restore_brest_litovsk"]
        n838{"GER_propaganda_master"}
        n839["GER_puppet_turkey"]
        n109["GER_reestablish_colonial_claims"]
        n498["GER_the_proud_eagle_and_the_resurgent_dragon"]
        n840{"GER_total_control_over_domestic_affairs"}
        n113["GER_towards_a_european_research_sphere"]
        n841["GER_utilize_the_nordliche_gesellschaft"]
        n842{"GER_wunderwaffe"}
    end
    subgraph tier_6["Tier 6"]
        n843["GER_a_strong_successor"]
        n844{"GER_befriend_poland"}
        n845["GER_influence_the_middle_east"]
        n846["GER_integrate_czech_manufacturers"]
        n847["GER_loyalty_to_the_fuhrer"]
        n848["GER_second_ljubljana_award"]
        n849{"GER_second_vienna_award"}
        n132["GER_vanquish_the_eastern_threat"]
        n850["GER_war_with_greece"]
    end
    subgraph tier_7["Tier 7"]
        n136["GER_approach_the_anglosphere"]
        n851{"GER_around_maginot"}
        n852["GER_danzig_for_slovakia"]
        n853["GER_fate_of_greece"]
        n854{"GER_form_rome_berlin_axis"}
        n855{"GER_influence_the_benelux"}
        n146["GER_open_the_asia_department"]
        n147["GER_open_up_a_latin_connection"]
        n856["GER_operation_weserubung"]
        n857["GER_subjugate_romanian_economy"]
    end
    subgraph tier_8["Tier 8"]
        n858["GER_demands_to_sweden"]
        n859{"GER_invade_italy"}
        n860["GER_secure_finland"]
        n861{"GER_war_with_france"}
    end
    subgraph tier_9["Tier 9"]
        n862{"GER_alliance_with_spain"}
        n863{"GER_operation_felix"}
        n864["GER_operation_sea_lion"]
        n865["GER_operation_tannenbaum"]
        n866["GER_reclaim_former_african_colonies"]
        n867["GER_reintegrate_luxemburg_and_alsace_lorraine"]
        n868["GER_the_swiss_gold"]
    end
    subgraph tier_10["Tier 10"]
        n869["GER_alliance_with_portugal"]
        n870["GER_crossing_the_atlantic"]
        n871["GER_mittelafrika"]
        n872["GER_operation_green"]
        n873["GER_operation_isabella"]
    end
    subgraph tier_11["Tier 11"]
        n874["GER_challenge_the_monroe_doctrine"]
        n875["GER_operation_bolivar"]
        n876["GER_shatter_usas_hegemony"]
    end
    subgraph tier_12["Tier 12"]
        n877["GER_establish_protectorates_in_america"]
    end
    n52 --> n62
    n52 --> n63
    n52 --> n64
    n836 --> n843
    n842 --> n843
    n837 --> n843
    n838 --> n843
    n840 --> n843
    n799 --> n817
    n69 --> n89
    n67 --> n89
    n862 --> n869
    n863 --> n869
    n854 --> n862
    n859 --> n862
    n816 --> n818
    n442 --> n460
    n785 --> n793
    n47 --> n51
    n775 --> n776
    n40 --> n395
    n395 --> n777
    n109 --> n136
    n101 --> n136
    n103 --> n136
    n132 --> n136
    n772 --> n778
    n844 --> n851
    n820 --> n851
    n773 --> n779
    n773 --> n780
    n773 --> n781
    n773 --> n782
    n773 --> n783
    n802 --> n819
    n772 --> n784
    n40 --> n442
    n425 --> n442
    n776 --> n794
    n395 --> n443
    n425 --> n443
    n834 --> n844
    n794 --> n844
    n792 --> n795
    n487 --> n496
    n488 --> n496
    n40 --> n772
    n47 --> n52
    n870 --> n874
    n442 --> n463
    n77 --> n93
    n56 --> n93
    n460 --> n480
    n472 --> n480
    n864 --> n870
    n844 --> n852
    n808 --> n820
    n776 --> n796
    n776 --> n797
    n856 --> n858
    n37 --> n785
    n775 --> n785
    n782 --> n798
    n52 --> n66
    n53 --> n66
    n55 --> n67
    n874 --> n877
    n876 --> n877
    n78 --> n97
    n808 --> n821
    n781 --> n799
    n37 --> n786
    n775 --> n786
    n781 --> n800
    n784 --> n801
    n823 --> n834
    n848 --> n853
    n822 --> n835
    n796 --> n822
    n810 --> n822
    n797 --> n823
    n783 --> n802
    n834 --> n854
    n849 --> n854
    n40 --> n773
    n804 --> n824
    n69 --> n101
    n83 --> n101
    n67 --> n101
    n805 --> n825
    n788 --> n825
    n47 --> n53
    n40 --> n37
    n817 --> n836
    n831 --> n836
    n62 --> n103
    n63 --> n103
    n808 --> n826
    n844 --> n855
    n820 --> n855
    n839 --> n845
    n795 --> n845
    n778 --> n803
    n784 --> n803
    n827 --> n846
    n834 --> n846
    n794 --> n827
    n829 --> n837
    n851 --> n859
    n855 --> n859
    n443 --> n470
    n40 --> n774
    n55 --> n69
    n836 --> n847
    n842 --> n847
    n837 --> n847
    n838 --> n847
    n840 --> n847
    n779 --> n804
    n866 --> n871
    n775 --> n787
    n83 --> n105
    n443 --> n472
    n109 --> n146
    n101 --> n146
    n103 --> n146
    n132 --> n146
    n109 --> n147
    n101 --> n147
    n103 --> n147
    n132 --> n147
    n870 --> n875
    n854 --> n863
    n859 --> n863
    n864 --> n872
    n863 --> n873
    n862 --> n873
    n861 --> n864
    n861 --> n865
    n820 --> n856
    n844 --> n856
    n789 --> n805
    n788 --> n805
    n773 --> n788
    n773 --> n789
    n798 --> n828
    n807 --> n829
    n791 --> n806
    n780 --> n807
    n824 --> n838
    n818 --> n839
    n805 --> n830
    n789 --> n830
    n442 --> n473
    n47 --> n55
    n47 --> n56
    n776 --> n808
    n859 --> n866
    n861 --> n866
    n77 --> n109
    n56 --> n109
    n861 --> n867
    n55 --> n77
    n56 --> n78
    n791 --> n809
    n40 --> n775
    n776 --> n810
    n835 --> n848
    n834 --> n849
    n794 --> n849
    n856 --> n860
    n841 --> n860
    n56 --> n82
    n470 --> n487
    n472 --> n487
    n870 --> n876
    n55 --> n83
    n460 --> n488
    n472 --> n488
    n37 --> n47
    n35 --> n47
    n778 --> n811
    n800 --> n831
    n844 --> n857
    n820 --> n857
    n809 --> n832
    n776 --> n812
    n777 --> n813
    n792 --> n814
    n460 --> n498
    n480 --> n498
    n793 --> n833
    n861 --> n868
    n776 --> n815
    n825 --> n840
    n830 --> n840
    n63 --> n113
    n787 --> n816
    n37 --> n790
    n775 --> n790
    n826 --> n841
    n64 --> n132
    n105 --> n132
    n37 --> n791
    n851 --> n861
    n856 --> n861
    n835 --> n850
    n395 --> n792
    n819 --> n842
    n828 --> n842
    n62 x--x n63
    n64 x--x n105
    n843 x--x n847
    n869 x--x n873
    n862 x--x n863
    n818 x--x n792
    n777 x--x n787
    n778 x--x n784
    n851 x--x n855
    n819 x--x n828
    n819 x--x n829
    n442 x--x n443
    n794 x--x n797
    n844 x--x n820
    n796 x--x n810
    n35 x--x n40
    n821 x--x n826
    n799 x--x n800
    n854 x--x n859
    n37 x--x n775
    n396 x--x n40
    n865 x--x n868
    n856 x--x n841
    n505 x--x n40
    n38 x--x n40
    n788 x--x n789
    n828 x--x n829
    n56 x--x n77
    n109 x--x n78
    n848 x--x n850
```

# GER_shake_off_the_fascist_yoke_dummy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n235["GER_fully_rebuild_the_secret_police"]
        n140["GER_hold_new_elections"]
        n169{"GER_nraf_in_coalition"}
        n41(("GER_shake_off_the_fascist_yoke_dummy"))
        n174["GER_spd_in_coalition"]
    end
    subgraph tier_1["Tier 1"]
        n167["GER_kpd_in_coalition"]
    end
    subgraph tier_2["Tier 2"]
        n183{"GER_deal_with_the_officier_corps"}
        n185{"GER_embrace_secularism"}
        n194["GER_industrial_collectivization"]
        n197["GER_legalize_the_kjvd"]
        n202{"GER_radicalize_the_workers"}
        n204["GER_reapproachment_with_moscow"]
        n205["GER_redistribute_wealth"]
        n207{"GER_revolution_in_german_culture"}
        n211{"GER_undermine_german_democracy"}
    end
    subgraph tier_3["Tier 3"]
        n224["GER_collapse_our_institutions"]
        n227["GER_deal_with_the_conciliators"]
        n232["GER_form_the_stasi_new"]
        n237["GER_guarantee_religious_freedom"]
        n240["GER_land_reform"]
        n241["GER_learn_from_the_enabling_act"]
        n244["GER_mandatory_membership"]
        n249["GER_peace_in_the_east"]
        n270["GER_towards_state_atheism"]
        n271["GER_uplift_the_antifa"]
        n272["GER_uplift_the_black_front"]
        n273["GER_uplift_the_sa"]
    end
    subgraph tier_4["Tier 4"]
        n295["GER_enforce_a_secularized_curriculum"]
        n298["GER_expand_recruitment"]
        n300["GER_fight_fascism_in_all_its_forms"]
        n301["GER_german_entry_into_the_comintern"]
        n302["GER_honor_the_legacy_of_marx"]
        n305["GER_industrial_cooperation_2"]
        n312["GER_phase_out_the_standing_army"]
        n319["GER_towards_a_party_state"]
        n322["GER_watch_the_churches"]
    end
    subgraph tier_5["Tier 5"]
        n328["GER_ban_the_reactionaries"]
        n331["GER_construct_the_karl_marx_cultural_instutute"]
        n333["GER_demand_state_approval_for_clergy"]
        n338["GER_form_the_sed"]
        n342["GER_introduce_the_jugendweihe"]
        n346["GER_resource_trade_2"]
        n348["GER_revolution_by_every_worker"]
        n349["GER_tech_sharing_2"]
        n353["GER_the_state_safe_from_within"]
    end
    subgraph tier_6["Tier 6"]
        n359["GER_ensure_the_gradual_withering_away_of_religion"]
        n363["GER_the_will_of_the_people_unopposed"]
        n365["GER_undermine_international_fascism"]
    end
    n319 --> n328
    n202 --> n224
    n211 --> n224
    n300 --> n331
    n302 --> n331
    n207 --> n227
    n167 --> n183
    n169 --> n183
    n322 --> n333
    n174 --> n185
    n167 --> n185
    n237 --> n295
    n270 --> n295
    n342 --> n359
    n333 --> n359
    n232 --> n298
    n227 --> n300
    n319 --> n338
    n207 --> n232
    n249 --> n301
    n185 --> n237
    n244 --> n302
    n227 --> n302
    n167 --> n194
    n249 --> n305
    n295 --> n342
    n270 --> n342
    n140 --> n167
    n41 --> n167
    n205 --> n240
    n202 --> n241
    n211 --> n241
    n167 --> n197
    n197 --> n244
    n207 --> n244
    n204 --> n249
    n273 --> n312
    n271 --> n312
    n272 --> n312
    n167 --> n202
    n167 --> n204
    n169 --> n205
    n174 --> n205
    n167 --> n205
    n305 --> n346
    n312 --> n348
    n167 --> n207
    n305 --> n349
    n298 --> n353
    n338 --> n363
    n328 --> n363
    n241 --> n319
    n224 --> n319
    n185 --> n270
    n167 --> n211
    n353 --> n365
    n183 --> n271
    n169 --> n272
    n183 --> n272
    n169 --> n273
    n183 --> n273
    n270 --> n322
    n235 --> n322
    n232 --> n322
    n224 x--x n241
    n232 x--x n235
    n237 x--x n270
    n271 x--x n272
    n271 x--x n273
    n272 x--x n273
```

# GER_strengthen_the_kriegsmarine

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n878(("GER_strengthen_the_kriegsmarine"))
        n388["GER_torpedobomber"]
    end
    subgraph tier_1["Tier 1"]
        n879["GER_plan_z"]
        n880["GER_re_establish_the_seekriegsleitung"]
        n881["GER_trade_interdiction"]
    end
    subgraph tier_2["Tier 2"]
        n882["GER_atlantic_naval_bases"]
        n883{"GER_cruiser_warfare"}
        n884["GER_expand_kriegsmarinewerft"]
        n885["GER_marinestosstrupp"]
        n886{"GER_wolfpack_tactics"}
    end
    subgraph tier_3["Tier 3"]
        n887["GER_atlantic_naval_dominance"]
        n375["GER_construct_aircraft_carriers"]
        n888["GER_grosskampfschiff_construction"]
        n889["GER_high_seas_fleet"]
        n890["GER_panzerschiff_raiders"]
        n891["GER_u_boat_efforts"]
    end
    subgraph tier_4["Tier 4"]
        n390["GER_establish_carrier_groups"]
        n892["GER_unrestricted_convoy_raiding"]
    end
    subgraph tier_5["Tier 5"]
        n893["GER_seeherrschaft"]
    end
    n880 --> n882
    n885 --> n887
    n882 --> n887
    n884 --> n375
    n881 --> n883
    n388 --> n390
    n375 --> n390
    n879 --> n884
    n884 --> n888
    n884 --> n889
    n880 --> n885
    n883 --> n890
    n878 --> n879
    n878 --> n880
    n889 --> n893
    n892 --> n893
    n878 --> n881
    n886 --> n891
    n890 --> n892
    n891 --> n892
    n881 --> n886
    n890 x--x n891
```

# GER_the_four_year_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n727["GER_currency_reforms"]
        n724["GER_prioritize_economic_growth"]
        n725{"GER_the_four_year_plan"}
    end
    subgraph tier_1["Tier 1"]
        n894["GER_accelerate_the_rearmament_program"]
        n723["GER_autarky_efforts"]
        n895["GER_coerce_the_technocrats"]
        n726["GER_construct_the_reichsautobahn"]
        n896["GER_push_a_moderate_reamament_program"]
    end
    subgraph tier_2["Tier 2"]
        n730["GER_build_the_rur_dam"]
        n897["GER_coal_liquefaction"]
        n898["GER_concentrated_armament_program"]
        n899["GER_establish_production_targets"]
        n900["GER_establish_the_reichswerke"]
        n901["GER_institute_price_controls"]
        n732["GER_kdf_wagen_factories"]
        n735["GER_trade_deal_with_sweden"]
    end
    subgraph tier_3["Tier 3"]
        n737["GER_develop_heraeus_facilities"]
        n902["GER_establish_buna_werke"]
        n738["GER_expand_the_reichsautobahn_east"]
        n739["GER_expand_the_reichsautobahn_south"]
        n903["GER_seize_foreign_industries"]
        n904["GER_subsidize_hoesch_benzin"]
        n905["GER_zentrale_planung"]
    end
    subgraph tier_4["Tier 4"]
        n906["GER_armament_rationalization"]
        n907["GER_autarky_achieved"]
        n908["GER_create_rustungsstab"]
    end
    subgraph tier_5["Tier 5"]
        n909["GER_totaler_krieg"]
    end
    n725 --> n894
    n905 --> n906
    n903 --> n907
    n904 --> n907
    n902 --> n907
    n725 --> n723
    n726 --> n730
    n727 --> n730
    n723 --> n897
    n725 --> n895
    n896 --> n898
    n894 --> n898
    n724 --> n726
    n725 --> n726
    n905 --> n908
    n732 --> n737
    n897 --> n902
    n896 --> n899
    n894 --> n899
    n723 --> n900
    n732 --> n738
    n732 --> n739
    n723 --> n901
    n726 --> n732
    n725 --> n896
    n900 --> n903
    n897 --> n904
    n908 --> n909
    n906 --> n909
    n726 --> n735
    n723 --> n735
    n898 --> n905
    n899 --> n905
    n894 x--x n896
    n724 x--x n725
```
