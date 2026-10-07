# AFG_afghan_royal_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"AFG_afghan_royal_army"}
    end
    subgraph tier_1["Tier 1"]
        n2{"AFG_army_modernization"}
        n3{"AFG_army_status_quo"}
    end
    subgraph tier_2["Tier 2"]
        n4["AFG_legacy_of_cavalrymen"]
        n5["AFG_purhcase_czech_weaponry"]
        n6["AFG_study_our_surroundings"]
        n7{"AFG_study_the_blitzkrieg"}
        n8{"AFG_victory_through_firepower"}
    end
    subgraph tier_3["Tier 3"]
        n9["AFG_bolster_national_arms_manufacturing"]
        n10["AFG_develop_the_tank_industry"]
        n11["AFG_improve_our_logistics"]
        n12["AFG_live_off_the_land"]
        n13["AFG_motorized_research"]
        n14["AFG_redesign_military_curriculum"]
        n15["AFG_tank_purchase"]
    end
    subgraph tier_4["Tier 4"]
        n16["AFG_develop_domestic_designs"]
        n17["AFG_finance_army_mechanization"]
        n18["AFG_mass_produce_equipment"]
        n19["AFG_modernize_military_hospitals"]
    end
    subgraph tier_5["Tier 5"]
        n20["AFG_introduce_new_uniforms"]
        n21["AFG_know_thy_enemy"]
        n22["AFG_specialization_of_units_focus"]
    end
    subgraph tier_6["Tier 6"]
        n23["AFG_prussians_orient"]
    end
    n1 --> n2
    n1 --> n3
    n6 --> n9
    n4 --> n9
    n9 --> n16
    n7 --> n10
    n10 --> n17
    n15 --> n17
    n8 --> n11
    n19 --> n20
    n16 --> n21
    n18 --> n21
    n3 --> n4
    n6 --> n12
    n9 --> n18
    n11 --> n19
    n14 --> n19
    n7 --> n13
    n20 --> n23
    n21 --> n23
    n2 --> n5
    n3 --> n5
    n8 --> n14
    n7 --> n14
    n19 --> n22
    n3 --> n6
    n2 --> n7
    n7 --> n15
    n8 --> n15
    n2 --> n8
    n2 x--x n3
    n10 x--x n15
    n4 x--x n6
    n7 x--x n8
```

# AFG_begin_westernization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n24(("AFG_begin_westernization"))
    end
    subgraph tier_1["Tier 1"]
        n25["AFG_improve_national_infra"]
        n26["AFG_rural_schools"]
    end
    subgraph tier_2["Tier 2"]
        n27["AFG_aquire_foreign_machinery"]
        n28["AFG_begin_rearmament"]
        n29["AFG_expand_university"]
        n30["AFG_the_nomad_population"]
    end
    subgraph tier_3["Tier 3"]
        n31["AFG_bolster_the_textile_industry"]
        n32["AFG_establish_ammunition_factories"]
        n33["AFG_kabul_arsenal"]
        n34["AFG_monopolize_the_karakul_trade"]
        n35["AFG_womens_education"]
    end
    subgraph tier_4["Tier 4"]
        n36["AFG_start_the_second_seven_year_plan"]
    end
    subgraph tier_5["Tier 5"]
        n37["AFG_afghanistan_bank"]
        n38["AFG_develop_hydroelectric_power"]
        n39["AFG_expand_the_directorate_of_mines"]
    end
    subgraph tier_6["Tier 6"]
        n40["AFG_afghan_miracle"]
        n41["AFG_intensify_copper_mining"]
        n42["AFG_rejuvenate_the_gold_mines"]
    end
    subgraph tier_7["Tier 7"]
        n43["AFG_explore_helmand_uranium_deposits"]
    end
    n37 --> n40
    n38 --> n40
    n36 --> n37
    n25 --> n27
    n26 --> n27
    n25 --> n28
    n27 --> n31
    n36 --> n38
    n28 --> n32
    n36 --> n39
    n26 --> n29
    n41 --> n43
    n42 --> n43
    n24 --> n25
    n39 --> n41
    n28 --> n33
    n27 --> n34
    n39 --> n42
    n24 --> n26
    n31 --> n36
    n34 --> n36
    n25 --> n30
    n29 --> n35
```

# AFG_crisis_over_the_durand

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n44{"AFG_crisis_over_the_durand"}
    end
    subgraph tier_1["Tier 1"]
        n45{"AFG_two_peoples_one_heritage"}
        n46["AFG_two_sides_one_people"]
    end
    subgraph tier_2["Tier 2"]
        n47["AFG_demand_a_compromise"]
        n48["AFG_ratify_the_durand_line"]
        n49["AFG_support_pashtun_resistance"]
        n50["AFG_support_the_khidmatgars"]
    end
    subgraph tier_3["Tier 3"]
        n51["AFG_now_or_never_unite_or_die"]
        n52{"AFG_the_bannu_resolution"}
    end
    subgraph tier_4["Tier 4"]
        n53["AFG_support_for_afghania"]
        n54["AFG_the_confederation_proposal"]
        n55["AFG_unification_or_death"]
    end
    subgraph tier_5["Tier 5"]
        n56["AFG_integrate_the_economy"]
        n57["AFG_united_military_command"]
    end
    subgraph tier_6["Tier 6"]
        n58["AFG_islam_king_and_state"]
    end
    n45 --> n47
    n54 --> n56
    n56 --> n58
    n57 --> n58
    n47 --> n51
    n48 --> n51
    n45 --> n48
    n52 --> n53
    n46 --> n49
    n46 --> n50
    n49 --> n52
    n50 --> n52
    n51 --> n54
    n44 --> n45
    n44 --> n46
    n52 --> n55
    n54 --> n57
    n47 x--x n48
    n53 x--x n55
    n45 x--x n46
```

# AFG_first_afghani_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n59{"AFG_first_afghani_navy"}
        n60["AFG_import_italian_fighters"]
    end
    subgraph tier_1["Tier 1"]
        n61["AFG_destroyers"]
        n62["AFG_submarines"]
    end
    subgraph tier_2["Tier 2"]
        n63["AFG_build_convoys"]
        n64["AFG_protect_our_convoys"]
        n65["AFG_under_the_radar"]
    end
    subgraph tier_3["Tier 3"]
        n66{"AFG_naval_building"}
        n67{"AFG_naval_defense_fund"}
    end
    subgraph tier_4["Tier 4"]
        n68["AFG_battleships"]
        n69["AFG_cruisers"]
        n70["AFG_naval_bombers"]
    end
    subgraph tier_5["Tier 5"]
        n71["AFG_terror_of_the_sea"]
    end
    n66 --> n68
    n67 --> n68
    n61 --> n63
    n62 --> n63
    n66 --> n69
    n67 --> n69
    n59 --> n61
    n67 --> n70
    n60 --> n70
    n63 --> n66
    n63 --> n67
    n61 --> n64
    n59 --> n62
    n70 --> n71
    n68 --> n71
    n62 --> n65
    n68 x--x n69
    n61 x--x n62
```

# AFG_first_loya_jirga

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n72{"AFG_first_loya_jirga"}
    end
    subgraph tier_1["Tier 1"]
        n73{"AFG_handle_the_king"}
        n74{"AFG_power_to_the_king"}
    end
    subgraph tier_2["Tier 2"]
        n75{"AFG_abolish_the_regency"}
        n76["AFG_contact_faqir"]
        n77["AFG_form_weekh_zalmian"]
        n78{"AFG_the_regency"}
    end
    subgraph tier_3["Tier 3"]
        n79["AFG_appoint_hashim"]
        n80["AFG_appoint_mahmud"]
        n81["AFG_approach_the_soviets"]
        n82["AFG_backtrack_on_reforms"]
        n83["AFG_contact_tribes"]
        n84["AFG_continute_nadir_shahs_reforms"]
        n85["AFG_form_worker_communes"]
        n86["AFG_invite_jamaat_islami"]
        n87["AFG_utilize_the_military"]
    end
    subgraph tier_4["Tier 4"]
        n88["AFG_annul_the_hasht_nafari"]
        n89["AFG_construct_the_great_north_road"]
        n90{"AFG_depose_the_king"}
        n91["AFG_enact_censorship"]
        n92["AFG_form_watan_party"]
        n93["AFG_introduce_new_taxes"]
        n94["AFG_irrigation_scheme"]
        n95["AFG_push_army_reforms"]
        n96["AFG_treaty_of_saadabad_hist"]
        n97["AFG_visit_berlin"]
        n98{"AFG_waaidu"}
    end
    subgraph tier_5["Tier 5"]
        n99{"AFG_amend_the_constitution"}
        n100["AFG_build_up_roads"]
        n101["AFG_foreign_economic_aid"]
        n102["AFG_grant_land_concessions"]
        n103["AFG_invite_wehrmacht_officers"]
        n104["AFG_maududi_as_sheikhulislam"]
        n105["AFG_mirzali_as_emir"]
        n106["AFG_national_front"]
        n107["AFG_soviet_expedition"]
        n108{"AFG_the_getyear_general_elections"}
        n109["AFG_university_in_herat"]
    end
    subgraph tier_6["Tier 6"]
        n110["AFG_adopt_constitutional_monarchy"]
        n111["AFG_centralize_the_bank_of_afg"]
        n112["AFG_enforce_the_pashtunwali_r56"]
        n113["AFG_eradicate_communism"]
        n114["AFG_fatherland_party_triumph"]
        n115["AFG_form_khad"]
        n116["AFG_german_investments_program"]
        n117{"AFG_institutionalize_pashto"}
        n118["AFG_land_redistribution"]
        n119{"AFG_ministry_for_propogation_of_virtue"}
        n120["AFG_nationalize_spiznar"]
        n121["AFG_purge_the_bourgeoisie"]
        n122["AFG_request_german_reinforcements"]
        n123["AFG_seize_royal_assets"]
        n124["AFG_shah_mahmud_prevails"]
        n125["AFG_socialist_education"]
        n126["AFG_the_exiled_king"]
        n127["AFG_the_generals_coup"]
        n128["AFG_utilize_the_sufis"]
    end
    subgraph tier_7["Tier 7"]
        n129["AFG_afghan_ssr"]
        n130["AFG_amanullahs_visit_to_europe"]
        n131["AFG_approach_mubashir"]
        n132["AFG_arrest_qiamuddin"]
        n133["AFG_ban_political_parties"]
        n134["AFG_begin_colectivization"]
        n135["AFG_bolster_the_nationalists"]
        n136["AFG_continue_railway_development"]
        n137["AFG_establish_radio_kabul"]
        n138{"AFG_german_equipment"}
        n139["AFG_infrastructure_privatization"]
        n140["AFG_kabul_military_college"]
        n141["AFG_liberal_constitution"]
        n142["AFG_nationalize_banks"]
        n143["AFG_our_own_path"]
        n144["AFG_persecute_believers"]
        n145["AFG_persecute_hazaras"]
        n146{"AFG_purge_the_nationalists"}
        n147{"AFG_reapproachment_with_RAJ"}
        n148{"AFG_return_of_the_king"}
        n149["AFG_support_the_palestinians"]
        n150["AFG_universal_suffarage"]
        n151["AFG_widen_perspective_of_religion"]
    end
    subgraph tier_8["Tier 8"]
        n152["AFG_ally_with_the_young_afghans"]
        n153["AFG_british_exchange_program"]
        n154["AFG_disband_the_jirga"]
        n155["AFG_economic_privatization"]
        n156["AFG_five_year_plan"]
        n157["AFG_form_muslim_youth"]
        n158{"AFG_form_the_turkestan_legion_r56"}
        n159["AFG_fund_the_army"]
        n160["AFG_global_islamic_revolution"]
        n161{"AFG_incorporate_tajikistan"}
        n162{"AFG_invite_abwehr_agents"}
        n163["AFG_invite_pakistani_military"]
        n164["AFG_join_allies"]
        n165["AFG_neutrality_reaffirmed"]
        n166{"AFG_persian_socialism"}
        n167["AFG_reform_the_education_system"]
        n168{"AFG_self_determination_for_pakistan"}
        n169{"AFG_socialist_constitution"}
        n170["AFG_stabilize_the_currency"]
        n171["AFG_the_afghan_new_deal"]
        n172["AFG_the_constitution_question"]
        n173["AFG_the_hazara_question"]
        n174["AFG_treaty_of_saadabad"]
        n175["AFG_you_cannot_kill_a_believer"]
    end
    subgraph tier_9["Tier 9"]
        n176["AFG_beacon_of_the_orient"]
        n177["AFG_crush_hazara_nationalism"]
        n178["AFG_deterrence_focus"]
        n179["AFG_export_based_economy"]
        n180["AFG_german_junker_purchase"]
        n181["AFG_give_hazara_rights"]
        n182["AFG_increase_school_funding"]
        n183["AFG_invite_amin_al_husseini"]
        n184["AFG_join_the_axis"]
        n185["AFG_loyalty_to_moscow"]
        n186["AFG_maintain_neutrality_r56"]
        n187["AFG_mix_sciences_with_religion"]
        n188["AFG_peace_through_islam"]
        n189["AFG_press_for_pakistan"]
        n190["AFG_proclaim_pashtunistan"]
        n191["AFG_restore_the_constitution"]
        n192["AFG_revolution_through_belief"]
        n193["AFG_revolution_through_force"]
        n194["AFG_subvert_soviet_influence_focus"]
        n195["AFG_the_fate_of_imperialism"]
        n196["AFG_tulaia_mutaharrika"]
        n197["AFG_undermine_moscow"]
    end
    subgraph tier_10["Tier 10"]
        n198["AFG_acquire_german_radios"]
        n199["AFG_afghan_workers_program"]
        n200["AFG_approach_pakistani_resistance"]
        n201["AFG_aquire_british_ships"]
        n202["AFG_army_reform"]
        n203["AFG_combat_foreign_influence"]
        n204["AFG_from_the_leopard_corps"]
        n205["AFG_implement_autarky"]
        n206["AFG_into_pakistan"]
        n207["AFG_legacy_of_the_yellow_expedition"]
        n208["AFG_marxist_thought"]
        n209["AFG_operation_blue_mosque"]
        n210["AFG_operation_red_mosque"]
        n211["AFG_operation_tiger"]
        n212["AFG_revive_the_basmachi_movement"]
        n213["AFG_sabotage_soviet_railways"]
        n214["AFG_secular_education"]
        n215["AFG_secure_the_corridor"]
        n216["AFG_seize_gun_stockpiles"]
        n217["AFG_socialist_economic_union"]
        n218["AFG_the_non_aligned_movement"]
        n219["AFG_turkish_subsidized_factories"]
    end
    subgraph tier_11["Tier 11"]
        n220{"AFG_attaturks_legacy"}
        n221["AFG_combined_training"]
        n222["AFG_deal_with_the_devil"]
        n223["AFG_end_soviet_rule"]
        n224["AFG_end_the_revolution"]
        n225["AFG_fortify_the_durand_line"]
        n226["AFG_implement_autarky_daoud"]
        n227["AFG_islamic_cooperation"]
        n228["AFG_pillars_of_islam"]
        n229["AFG_socialist_welfare"]
        n230["AFG_soviet_menace"]
        n231["AFG_the_perso_afghan_union"]
        n232["AFG_the_uneasey_border"]
    end
    subgraph tier_12["Tier 12"]
        n233["AFG_anti_fascist_league"]
        n234["AFG_greater_afghanistan"]
        n235["AFG_international_mujahideen"]
        n236["AFG_operation_coutenance"]
        n237["AFG_the_kabul_pact"]
        n238["AFG_tunganistan"]
    end
    subgraph tier_13["Tier 13"]
        n239["AFG_break_the_six_arrows"]
        n240["AFG_form_the_afghan_red_crescent"]
        n241["AFG_in_alexanders_footsteps"]
        n242["AFG_reclaim_our_land"]
        n243["AFG_the_ten_lost_tribes"]
    end
    n74 --> n75
    n184 --> n198
    n165 --> n198
    n101 --> n110
    n115 --> n129
    n185 --> n199
    n130 --> n152
    n126 --> n130
    n93 --> n99
    n88 --> n99
    n82 --> n88
    n221 --> n233
    n223 --> n233
    n78 --> n79
    n78 --> n80
    n128 --> n131
    n188 --> n200
    n77 --> n81
    n176 --> n201
    n194 --> n202
    n179 --> n202
    n115 --> n132
    n214 --> n220
    n219 --> n220
    n75 --> n82
    n127 --> n133
    n164 --> n176
    n121 --> n134
    n117 --> n135
    n238 --> n239
    n228 --> n239
    n139 --> n153
    n97 --> n100
    n101 --> n111
    n178 --> n203
    n185 --> n221
    n199 --> n221
    n84 --> n89
    n73 --> n76
    n76 --> n83
    n110 --> n136
    n75 --> n84
    n169 --> n177
    n202 --> n222
    n87 --> n90
    n85 --> n90
    n81 --> n90
    n165 --> n178
    n133 --> n154
    n142 --> n154
    n139 --> n155
    n79 --> n91
    n213 --> n223
    n216 --> n223
    n160 --> n224
    n211 --> n224
    n105 --> n112
    n104 --> n113
    n110 --> n137
    n152 --> n179
    n154 --> n179
    n108 --> n114
    n134 --> n156
    n95 --> n101
    n89 --> n101
    n107 --> n115
    n145 --> n157
    n186 --> n240
    n237 --> n240
    n131 --> n158
    n149 --> n158
    n80 --> n92
    n73 --> n77
    n77 --> n85
    n203 --> n225
    n184 --> n204
    n165 --> n204
    n146 --> n159
    n135 --> n159
    n122 --> n138
    n100 --> n116
    n138 --> n180
    n162 --> n180
    n169 --> n181
    n148 --> n160
    n94 --> n102
    n222 --> n234
    n72 --> n73
    n178 --> n205
    n202 --> n226
    n238 --> n241
    n129 --> n161
    n153 --> n182
    n155 --> n182
    n114 --> n139
    n124 --> n139
    n100 --> n117
    n103 --> n117
    n228 --> n235
    n185 --> n206
    n193 --> n206
    n82 --> n93
    n135 --> n162
    n158 --> n183
    n76 --> n86
    n143 --> n163
    n97 --> n103
    n80 --> n94
    n212 --> n227
    n141 --> n164
    n162 --> n184
    n138 --> n184
    n122 --> n140
    n106 --> n118
    n107 --> n118
    n176 --> n207
    n114 --> n141
    n161 --> n185
    n168 --> n186
    n181 --> n208
    n177 --> n208
    n98 --> n104
    n105 --> n119
    n104 --> n119
    n98 --> n105
    n172 --> n187
    n90 --> n106
    n127 --> n142
    n126 --> n142
    n104 --> n120
    n146 --> n165
    n147 --> n165
    n184 --> n209
    n221 --> n236
    n176 --> n210
    n184 --> n211
    n125 --> n143
    n158 --> n188
    n115 --> n144
    n119 --> n145
    n143 --> n166
    n200 --> n228
    n212 --> n228
    n72 --> n74
    n164 --> n189
    n165 --> n189
    n160 --> n190
    n106 --> n121
    n107 --> n121
    n117 --> n146
    n84 --> n95
    n124 --> n147
    n222 --> n242
    n237 --> n242
    n143 --> n167
    n105 --> n122
    n152 --> n191
    n123 --> n148
    n188 --> n212
    n160 --> n212
    n166 --> n192
    n166 --> n193
    n197 --> n213
    n191 --> n214
    n193 --> n215
    n197 --> n216
    n105 --> n123
    n136 --> n168
    n108 --> n124
    n150 --> n169
    n134 --> n169
    n192 --> n217
    n106 --> n125
    n217 --> n229
    n90 --> n107
    n206 --> n230
    n215 --> n230
    n135 --> n170
    n146 --> n170
    n147 --> n170
    n154 --> n194
    n128 --> n149
    n141 --> n171
    n145 --> n172
    n151 --> n172
    n99 --> n126
    n160 --> n195
    n99 --> n127
    n94 --> n108
    n92 --> n108
    n136 --> n173
    n137 --> n173
    n168 --> n237
    n220 --> n237
    n186 --> n218
    n217 --> n231
    n74 --> n78
    n238 --> n243
    n228 --> n243
    n203 --> n232
    n176 --> n232
    n130 --> n174
    n110 --> n174
    n79 --> n96
    n80 --> n96
    n172 --> n196
    n195 --> n238
    n224 --> n238
    n174 --> n219
    n191 --> n219
    n161 --> n197
    n121 --> n150
    n88 --> n109
    n89 --> n109
    n77 --> n87
    n104 --> n128
    n79 --> n97
    n86 --> n98
    n83 --> n98
    n119 --> n151
    n148 --> n175
    n75 x--x n78
    n79 x--x n80
    n82 x--x n84
    n135 x--x n146
    n76 x--x n77
    n177 x--x n181
    n114 x--x n124
    n160 x--x n188
    n73 x--x n74
    n184 x--x n165
    n185 x--x n197
    n186 x--x n237
    n104 x--x n105
    n106 x--x n107
    n145 x--x n151
    n192 x--x n193
    n126 x--x n127
```

# AFG_royal_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n68["AFG_battleships"]
        n67["AFG_naval_defense_fund"]
        n244(("AFG_royal_air_force"))
    end
    subgraph tier_1["Tier 1"]
        n245["AFG_invite_foreign_instructors"]
        n246["AFG_train_our_personnel_abroad"]
    end
    subgraph tier_2["Tier 2"]
        n247["AFG_expand_military_airports"]
        n248{"AFG_import_planes"}
    end
    subgraph tier_3["Tier 3"]
        n249["AFG_import_british_fighters"]
        n60["AFG_import_italian_fighters"]
        n250["AFG_the_242nd_parachute_battalion"]
    end
    subgraph tier_4["Tier 4"]
        n251["AFG_kabul_air_college"]
        n70["AFG_naval_bombers"]
    end
    subgraph tier_5["Tier 5"]
        n71["AFG_terror_of_the_sea"]
    end
    n246 --> n247
    n248 --> n249
    n248 --> n60
    n245 --> n248
    n246 --> n248
    n244 --> n245
    n249 --> n251
    n60 --> n251
    n67 --> n70
    n60 --> n70
    n70 --> n71
    n68 --> n71
    n247 --> n250
    n244 --> n246
    n249 x--x n60
```
