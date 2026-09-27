# PER_democratic_promise_dlc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PER_democratic_promise_dlc"))
        n2["PER_empower_the_shah_dlc"]
        n3["PER_falsify_elections_dlc"]
    end
    subgraph tier_1["Tier 1"]
        n4["PER_land_reforms_cw_dlc"]
        n5["PER_reform_the_administration_cw_dlc"]
    end
    subgraph tier_2["Tier 2"]
        n6["PER_nationalize_iranian_oil_dlc"]
        n7["PER_the_seven_year_plan_dlc"]
    end
    subgraph tier_3["Tier 3"]
        n8["PER_economy_without_oil_dlc"]
        n9["PER_undermine_the_shah_dlc"]
    end
    subgraph tier_4["Tier 4"]
        n10{"PER_alliance_with_the_ussr_dlc"}
        n11{"PER_compromise_with_britain_dlc"}
        n12{"PER_request_american_support_dlc"}
    end
    subgraph tier_5["Tier 5"]
        n13["PER_entrench_mosaddegh_dlc"]
        n14["PER_found_SAVAK_dlc"]
    end
    n9 --> n10
    n5 --> n10
    n9 --> n11
    n6 --> n8
    n7 --> n8
    n12 --> n13
    n11 --> n13
    n10 --> n13
    n12 --> n14
    n11 --> n14
    n1 --> n4
    n3 --> n4
    n5 --> n6
    n2 --> n6
    n1 --> n5
    n9 --> n12
    n2 --> n7
    n5 --> n7
    n6 --> n9
    n2 --> n9
    n1 x--x n3
    n13 x--x n14
```

# PER_establish_airforce

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15(("PER_establish_airforce"))
        n16["PER_import_rocketry"]
    end
    subgraph tier_1["Tier 1"]
        n17["PER_construct_air_bases"]
        n18{"PER_pilot_training"}
    end
    subgraph tier_2["Tier 2"]
        n19["PER_anti_air_research"]
        n20["PER_luftwaffe_planes"]
        n21["PER_raf_planes"]
    end
    subgraph tier_3["Tier 3"]
        n22{"PER_anti_air_development"}
        n23{"PER_establish_air_academy"}
        n24["PER_own_plane_designs"]
    end
    subgraph tier_4["Tier 4"]
        n25["PER_air_superiority"]
        n26["PER_battlefield_support"]
        n27["PER_legacy_of_gilani"]
        n28["PER_strategic_bombing"]
    end
    subgraph tier_5["Tier 5"]
        n29["PER_negotiate_with_america"]
        n30["PER_perfect_iranian_airforce"]
    end
    subgraph tier_6["Tier 6"]
        n31["PER_establish_nuclear_program"]
    end
    n23 --> n25
    n22 --> n25
    n19 --> n22
    n17 --> n19
    n23 --> n26
    n15 --> n17
    n20 --> n23
    n21 --> n23
    n29 --> n31
    n23 --> n27
    n18 --> n20
    n16 --> n29
    n28 --> n29
    n20 --> n24
    n21 --> n24
    n25 --> n30
    n28 --> n30
    n26 --> n30
    n15 --> n18
    n18 --> n21
    n23 --> n28
    n25 x--x n26
    n25 x--x n28
    n26 x--x n28
    n20 x--x n21
```

# PER_establish_the_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n32(("PER_establish_the_navy"))
    end
    subgraph tier_1["Tier 1"]
        n33{"PER_construct_naval_bases"}
        n34{"PER_officers_to_italy"}
    end
    subgraph tier_2["Tier 2"]
        n35["PER_bolster_the_caspian"]
        n36["PER_coastal_defense_initiative"]
        n37["PER_persian_gulf_fleet"]
    end
    subgraph tier_3["Tier 3"]
        n38["PER_purchase_foreign_ships"]
    end
    subgraph tier_4["Tier 4"]
        n39["PER_found_iranian_shipyards"]
    end
    subgraph tier_5["Tier 5"]
        n40{"PER_expand_dockyards"}
    end
    subgraph tier_6["Tier 6"]
        n41["PER_expert_raiders"]
        n42["PER_merchant_navy"]
    end
    n33 --> n35
    n34 --> n35
    n33 --> n36
    n32 --> n33
    n39 --> n40
    n40 --> n41
    n38 --> n39
    n40 --> n42
    n32 --> n34
    n34 --> n37
    n33 --> n37
    n35 --> n38
    n37 --> n38
    n35 x--x n37
    n41 x--x n42
```

# PER_falsify_elections_dlc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["PER_democratic_promise_dlc"]
        n3(("PER_falsify_elections_dlc"))
        n5["PER_reform_the_administration_cw_dlc"]
    end
    subgraph tier_1["Tier 1"]
        n2["PER_empower_the_shah_dlc"]
        n4["PER_land_reforms_cw_dlc"]
    end
    subgraph tier_2["Tier 2"]
        n6["PER_nationalize_iranian_oil_dlc"]
        n7["PER_the_seven_year_plan_dlc"]
    end
    subgraph tier_3["Tier 3"]
        n8["PER_economy_without_oil_dlc"]
        n9["PER_undermine_the_shah_dlc"]
    end
    subgraph tier_4["Tier 4"]
        n10{"PER_alliance_with_the_ussr_dlc"}
        n11{"PER_compromise_with_britain_dlc"}
        n12{"PER_request_american_support_dlc"}
    end
    subgraph tier_5["Tier 5"]
        n13["PER_entrench_mosaddegh_dlc"]
        n14["PER_found_SAVAK_dlc"]
    end
    n9 --> n10
    n5 --> n10
    n9 --> n11
    n6 --> n8
    n7 --> n8
    n3 --> n2
    n12 --> n13
    n11 --> n13
    n10 --> n13
    n12 --> n14
    n11 --> n14
    n1 --> n4
    n3 --> n4
    n5 --> n6
    n2 --> n6
    n9 --> n12
    n2 --> n7
    n5 --> n7
    n6 --> n9
    n2 --> n9
    n1 x--x n3
    n13 x--x n14
```

# PER_fight_for_iran

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n43{"PER_fight_for_iran"}
    end
    subgraph tier_1["Tier 1"]
        n44{"PER_dig_and_defend"}
        n45{"PER_force_them_back"}
    end
    subgraph tier_2["Tier 2"]
        n46{"PER_capital_protect"}
        n47{"PER_push_to_deserts"}
        n48{"PER_push_to_mountains"}
        n49{"PER_secure_coastline"}
    end
    subgraph tier_3["Tier 3"]
        n50["PER_demand_war_reparations"]
        n51["PER_force_white_peace"]
        n52["PER_push_negotiations"]
        n53["PER_swear_fealty"]
    end
    subgraph tier_4["Tier 4"]
        n54{"PER_rebuilding_iran"}
    end
    subgraph tier_5["Tier 5"]
        n55["PER_azadi"]
        n56["PER_declare_loyalty_to_britain"]
    end
    subgraph tier_6["Tier 6"]
        n57["PER_invite_british_investors"]
        n58["PER_rally_bakhtiari_and_qashqai"]
        n59["PER_reinforce_iranian_identity"]
        n60["PER_reinstate_qajars"]
        n61["PER_request_british_equipment"]
    end
    subgraph tier_7["Tier 7"]
        n62["PER_iran_for_iranians"]
        n63["PER_our_place_in_empire"]
    end
    subgraph tier_8["Tier 8"]
        n64["PER_consolidate_british_territory"]
        n65["PER_retake_north_iran"]
    end
    n54 --> n55
    n44 --> n46
    n62 --> n64
    n54 --> n56
    n47 --> n50
    n48 --> n50
    n43 --> n44
    n43 --> n45
    n47 --> n51
    n48 --> n51
    n56 --> n57
    n58 --> n62
    n59 --> n62
    n61 --> n63
    n57 --> n63
    n46 --> n52
    n49 --> n52
    n45 --> n47
    n45 --> n48
    n55 --> n58
    n53 --> n54
    n55 --> n59
    n56 --> n60
    n56 --> n61
    n63 --> n65
    n62 --> n65
    n44 --> n49
    n46 --> n53
    n49 --> n53
    n55 x--x n56
    n46 x--x n49
    n50 x--x n51
    n44 x--x n45
    n52 x--x n53
    n47 x--x n48
```

# PER_modernizing_iran

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n66(("PER_modernizing_iran"))
    end
    subgraph tier_1["Tier 1"]
        n67["PER_adult_literacy"]
        n68["PER_rapid_industrialization"]
        n69["PER_trans_iranian_railway"]
        n70["PER_white_revolution"]
    end
    subgraph tier_2["Tier 2"]
        n71["PER_develop_oil_fields"]
        n72{"PER_expand_tabriz_masshad"}
        n73{"PER_expand_tehran_abbas"}
        n74{"PER_expand_tehran_emam"}
        n75["PER_national_bank"]
        n76{"PER_national_museum"}
        n77["PER_tehran_power_plant"]
    end
    subgraph tier_3["Tier 3"]
        n78["PER_abolish_feudalism"]
        n79["PER_develop_cities"]
        n80{"PER_form_oil_company"}
        n81["PER_price_stabilization"]
        n82["PER_shiraz_university"]
        n83["PER_trains_from_britain"]
        n84["PER_trains_from_germany"]
        n85["PER_university_of_isfahan"]
    end
    subgraph tier_4["Tier 4"]
        n86["PER_educational_reforms"]
        n87["PER_feat_of_engineering"]
        n88["PER_food_for_all"]
        n89["PER_metropolitan_iran"]
        n90["PER_oil_baron"]
        n91["PER_profit_from_war"]
        n92["PER_women_vote"]
    end
    subgraph tier_5["Tier 5"]
        n93["PER_a_modern_iran"]
    end
    n91 --> n93
    n90 --> n93
    n89 --> n93
    n88 --> n93
    n92 --> n93
    n87 --> n93
    n86 --> n93
    n75 --> n78
    n66 --> n67
    n77 --> n79
    n68 --> n71
    n85 --> n86
    n82 --> n86
    n69 --> n72
    n69 --> n73
    n69 --> n74
    n83 --> n87
    n84 --> n87
    n81 --> n88
    n78 --> n88
    n71 --> n80
    n79 --> n89
    n70 --> n75
    n67 --> n76
    n80 --> n90
    n75 --> n81
    n80 --> n91
    n66 --> n68
    n76 --> n82
    n68 --> n77
    n72 --> n83
    n74 --> n83
    n73 --> n83
    n72 --> n84
    n74 --> n84
    n73 --> n84
    n66 --> n69
    n76 --> n85
    n66 --> n70
    n81 --> n92
    n78 --> n92
    n90 x--x n91
    n82 x--x n85
    n83 x--x n84
```

# PER_rally_the_reformers

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n94(("PER_rally_the_reformers"))
        n95["PER_the_pahlavi_imperium"]
    end
    subgraph tier_1["Tier 1"]
        n96{"PER_propagate_political_literature"}
        n97{"PER_stage_mass_protests"}
    end
    subgraph tier_2["Tier 2"]
        n98["PER_iranian_culture"]
        n99{"PER_rally_behind_mosaddegh"}
        n100["PER_united_progressive_parties"]
    end
    subgraph tier_3["Tier 3"]
        n101["PER_constitutional_monarchy"]
        n102["PER_embrace_national_front"]
        n103["PER_form_sumka"]
        n104{"PER_reach_to_seperatists"}
    end
    subgraph tier_4["Tier 4"]
        n105["PER_ally_the_bazaari"]
        n106["PER_brown_shirts"]
        n107["PER_elevate_the_iran_party"]
        n108["PER_force_abdication"]
        n109{"PER_promise_clergy_power"}
        n110["PER_strengthen_iranian_parliament"]
        n111["PER_strengthen_the_tudeh"]
    end
    subgraph tier_5["Tier 5"]
        n112{"PER_free_elections"}
        n113["PER_iranian_revolutionary_vanguard"]
        n114["PER_iranian_socialist_revolution"]
        n115["PER_march_on_saadabad"]
    end
    subgraph tier_6["Tier 6"]
        n116["PER_appease_the_seperatists"]
        n117["PER_continue_westernization"]
        n118["PER_finding_a_shah"]
        n119["PER_iranian_socialism"]
        n120["PER_islamic_restoration"]
        n121["PER_one_for_all_all_for_one"]
        n122["PER_roll_back_reforms"]
        n123["PER_soviet_alignment"]
    end
    subgraph tier_7["Tier 7"]
        n124["PER_ally_bazaari"]
        n125["PER_communist_education_reform"]
        n126["PER_communist_industrialization"]
        n127["PER_communist_propaganda"]
        n128["PER_entice_foreign_investment"]
        n129{"PER_fascist_secularism"}
        n130{"PER_form_savama"}
        n131["PER_industrial_aid"]
        n132["PER_iranian_industrialization"]
        n133{"PER_pan_iranianism"}
        n134["PER_royal_college_funding"]
        n135["PER_secularize_the_state"]
    end
    subgraph tier_8["Tier 8"]
        n136{"PER_expand_oil_production"}
        n137["PER_fascist_reach_out_to_germany"]
        n138["PER_fascist_reach_out_to_japan"]
        n139["PER_increase_faculty_staffing_budget"]
        n140["PER_invest_in_univerity_facilities"]
        n141["PER_iran_first"]
        n142["PER_islamic_revolution"]
        n143["PER_land_reform"]
        n144["PER_reject_foreign_dominance"]
        n145["PER_soviet_iranian_oil_collaboration"]
        n146["PER_the_new_economy"]
    end
    subgraph tier_9["Tier 9"]
        n147["PER_comintern_research_collaboration"]
        n148["PER_fascist_attack_turkey"]
        n149["PER_increase_oil_sales"]
        n150["PER_intervene_in_central_asia"]
        n151["PER_intervention_in_iraq"]
        n152["PER_nationalize_oil_fields"]
        n153["PER_oil_and_rubber_industry"]
        n154["PER_workers_army"]
    end
    subgraph tier_10["Tier 10"]
        n155["PER_crush_saudi_arabia"]
        n156["PER_fascist_attack_afghanistan"]
        n157["PER_international_solidarity"]
        n158["PER_iranian_nuclear_program"]
        n159["PER_islamic_solidarity"]
        n160["PER_request_membership_allies"]
        n161["PER_the_peoples_airforce"]
        n162["PER_the_peoples_navy"]
    end
    subgraph tier_11["Tier 11"]
        n163["PER_communist_afghanistan_intervention"]
        n164["PER_communist_air_defense"]
        n165["PER_communist_basic_plane_design"]
        n166["PER_communist_destabilize_iraq"]
        n167["PER_communist_naval_designs"]
        n168["PER_communist_shore_defense"]
        n169["PER_proclaim_greater_iran"]
        n170["PER_secure_afghanistan"]
        n171["PER_secure_iraq"]
    end
    subgraph tier_12["Tier 12"]
        n172["PER_challenge_the_royal_navy"]
        n173["PER_communist_liberate_pashtuns"]
        n174["PER_communist_naval_bomber_design"]
        n175["PER_communist_submarine_design"]
        n176["PER_curtail_pan_arabism"]
        n177["PER_eastern_expansion"]
        n178["PER_post_war_spoils"]
        n179["PER_revolution_in_the_gulf"]
        n180["PER_there_can_be_only_one"]
    end
    subgraph tier_13["Tier 13"]
        n181["PER_hormuz_crisis"]
    end
    subgraph tier_14["Tier 14"]
        n182["PER_communist_gulf_hegemony"]
    end
    n120 --> n124
    n103 --> n105
    n114 --> n116
    n103 --> n106
    n165 --> n172
    n167 --> n172
    n145 --> n147
    n143 --> n147
    n157 --> n163
    n161 --> n164
    n161 --> n165
    n157 --> n166
    n119 --> n125
    n123 --> n125
    n181 --> n182
    n119 --> n126
    n123 --> n126
    n163 --> n173
    n165 --> n174
    n162 --> n167
    n119 --> n127
    n123 --> n127
    n162 --> n168
    n167 --> n175
    n99 --> n101
    n112 --> n117
    n148 --> n155
    n169 --> n176
    n169 --> n177
    n104 --> n107
    n99 --> n102
    n117 --> n128
    n124 --> n136
    n128 --> n136
    n151 --> n156
    n137 --> n148
    n138 --> n148
    n141 --> n148
    n130 --> n137
    n133 --> n137
    n129 --> n138
    n133 --> n138
    n122 --> n129
    n118 --> n129
    n115 --> n118
    n105 --> n118
    n102 --> n108
    n122 --> n130
    n118 --> n130
    n98 --> n103
    n108 --> n112
    n110 --> n112
    n179 --> n181
    n134 --> n139
    n128 --> n139
    n136 --> n149
    n123 --> n131
    n146 --> n157
    n152 --> n157
    n141 --> n150
    n138 --> n150
    n137 --> n150
    n137 --> n151
    n138 --> n151
    n141 --> n151
    n134 --> n140
    n128 --> n140
    n130 --> n141
    n133 --> n141
    n97 --> n98
    n96 --> n98
    n119 --> n132
    n147 --> n158
    n107 --> n113
    n114 --> n119
    n107 --> n119
    n111 --> n114
    n107 --> n114
    n112 --> n120
    n109 --> n120
    n124 --> n142
    n152 --> n159
    n131 --> n143
    n106 --> n115
    n105 --> n115
    n136 --> n152
    n146 --> n153
    n113 --> n121
    n122 --> n133
    n118 --> n133
    n171 --> n178
    n170 --> n178
    n150 --> n169
    n155 --> n169
    n156 --> n169
    n101 --> n109
    n94 --> n96
    n97 --> n99
    n96 --> n99
    n100 --> n104
    n126 --> n144
    n132 --> n144
    n149 --> n160
    n166 --> n179
    n163 --> n179
    n115 --> n122
    n120 --> n134
    n117 --> n134
    n117 --> n135
    n160 --> n170
    n160 --> n171
    n114 --> n123
    n111 --> n123
    n131 --> n145
    n94 --> n97
    n101 --> n110
    n104 --> n111
    n125 --> n146
    n127 --> n146
    n126 --> n146
    n154 --> n161
    n154 --> n162
    n169 --> n180
    n97 --> n100
    n96 --> n100
    n146 --> n154
    n101 x--x n102
    n117 x--x n120
    n107 x--x n111
    n137 x--x n138
    n137 x--x n141
    n138 x--x n141
    n149 x--x n152
    n98 x--x n99
    n98 x--x n100
    n99 x--x n100
    n94 x--x n95
```

# PER_restructure_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n183(("PER_restructure_army"))
        n28["PER_strategic_bombing"]
    end
    subgraph tier_1["Tier 1"]
        n184["PER_expand_imperial_guard"]
        n185{"PER_expand_military_facilities"}
        n186{"PER_foreign_retraining"}
        n187["PER_special_units"]
    end
    subgraph tier_2["Tier 2"]
        n188["PER_bolster_infantry"]
        n189["PER_czech_tanks"]
        n190["PER_form_savak"]
        n191["PER_german_tanks"]
        n16["PER_import_rocketry"]
        n192["PER_special_forces_program"]
        n193["PER_swedish_artillery"]
    end
    subgraph tier_3["Tier 3"]
        n194["PER_cyrus_initiative"]
        n195["PER_develop_qorkhaneh"]
        n196["PER_establish_motor_arms"]
        n197["PER_expand_unique_unit"]
        n198["PER_fund_state_intelligence"]
        n199["PER_future_of_war"]
        n200["PER_increase_heavy_arms"]
        n29["PER_negotiate_with_america"]
        n201["PER_recruit_bakhtiari"]
        n202["PER_reverse_engineer_tanks"]
        n203["PER_transfer_officers_to_intelligence"]
    end
    subgraph tier_4["Tier 4"]
        n204{"PER_desert_training"}
        n31["PER_establish_nuclear_program"]
        n205["PER_establish_tehran_armor"]
        n206["PER_motorize_infantry"]
        n207["PER_our_own_artillery"]
        n208{"PER_train_tank_commanders"}
    end
    subgraph tier_5["Tier 5"]
        n209["PER_every_man_serves"]
        n210["PER_expand_tehran_armor"]
        n211["PER_military_excellency"]
    end
    n186 --> n188
    n16 --> n194
    n185 --> n189
    n195 --> n204
    n188 --> n195
    n193 --> n195
    n188 --> n196
    n29 --> n31
    n202 --> n205
    n204 --> n209
    n208 --> n209
    n183 --> n184
    n183 --> n185
    n205 --> n210
    n192 --> n197
    n183 --> n186
    n187 --> n190
    n190 --> n198
    n191 --> n199
    n189 --> n199
    n185 --> n191
    n187 --> n16
    n193 --> n200
    n204 --> n211
    n208 --> n211
    n196 --> n206
    n16 --> n29
    n28 --> n29
    n200 --> n207
    n192 --> n201
    n191 --> n202
    n189 --> n202
    n187 --> n192
    n183 --> n187
    n186 --> n193
    n199 --> n208
    n190 --> n203
    n188 x--x n193
    n189 x--x n191
    n209 x--x n211
```

# PER_the_pahlavi_imperium

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n94["PER_rally_the_reformers"]
        n95{"PER_the_pahlavi_imperium"}
    end
    subgraph tier_1["Tier 1"]
        n212{"PER_legacy_of_greatness"}
        n213["PER_stand_with_giants"]
    end
    subgraph tier_2["Tier 2"]
        n214["PER_assassinate_reza_shah"]
        n215["PER_assessing_the_opposition"]
        n216["PER_forced_secularization"]
        n217["PER_imperial_funded_universities"]
        n218["PER_increase_education_funding"]
        n219["PER_increase_military_funding"]
        n220["PER_persian_german_trade"]
        n221["PER_root_out_conspiracies"]
        n222["PER_trial_fifty_three"]
    end
    subgraph tier_3["Tier 3"]
        n223["PER_absolute_monarchy"]
        n224["PER_his_fathers_footsteps"]
        n225["PER_imperial_expansionism"]
        n226["PER_military_high_schools"]
        n227["PER_open_abadan"]
        n228["PER_royal_visit_germany"]
        n229["PER_the_unification_initiative"]
    end
    subgraph tier_4["Tier 4"]
        n230{"PER_clamp_azerbaijani_dissidence"}
        n231{"PER_clamp_kurdish_dissidence"}
        n232["PER_establish_special_unit"]
        n233["PER_first_iranian_empire"]
        n234["PER_tehran_moscow_pact"]
        n235["PER_third_persian_empire"]
        n236{"PER_wether_the_storm"}
    end
    subgraph tier_5["Tier 5"]
        n237{"PER_choose_a_shahbanu"}
        n238["PER_demand_afghan_territory"]
        n239["PER_demand_iraqi_territory"]
        n240["PER_question_of_resources"]
        n241["PER_revive_old_ways"]
        n242["PER_shahanshah"]
        n243["PER_stand_our_ground"]
        n244["PER_state_atheism"]
        n245{"PER_take_regional_tour"}
        n246["PER_venerate_islam"]
    end
    subgraph tier_6["Tier 6"]
        n247["PER_bolster_civilian_industry"]
        n248["PER_embrace_industrial_powers"]
        n249["PER_embrace_opulence"]
        n250["PER_emperor_for_people"]
        n251["PER_limit_foreign_influence"]
        n252["PER_plant_resistance_cells"]
        n253["PER_prepare_for_worst"]
        n254["PER_rally_ancient_history"]
        n255["PER_upscale_military_production"]
        n256["PER_war_plan_cambyses"]
        n257["PER_war_plan_darius"]
        n258["PER_war_plan_xerxes"]
    end
    subgraph tier_7["Tier 7"]
        n259["PER_demand_west_asia"]
        n260["PER_foothold_in_indus"]
        n261["PER_fund_imperial_excellency"]
        n262["PER_modernize_iran_economy"]
        n263["PER_path_through_iraq"]
        n264["PER_preemptive_strike"]
        n265["PER_preparatory_mobilization"]
        n266["PER_rebuild_persepolis"]
        n267["PER_reclaim_turkish_peninsula"]
        n268["PER_stand_with_germany"]
        n269["PER_subserviant_to_noone"]
        n270["PER_uphold_civil_rights"]
        n271["PER_usurp_afghanistan"]
    end
    subgraph tier_8["Tier 8"]
        n272["PER_align_with_axis"]
        n273["PER_clash_of_titans"]
        n274["PER_establish_northern_buffer_states"]
        n275["PER_invasion_of_india"]
        n276["PER_last_thousand_years"]
        n277["PER_march_to_nile"]
        n278["PER_reintegrate_anatolia"]
        n279["PER_we_will_survive"]
    end
    subgraph tier_9["Tier 9"]
        n280["PER_absorb_byzantines"]
        n281["PER_donate_oil_fields"]
        n282["PER_glory_of_cyrus"]
        n283["PER_spoils_of_war"]
        n284["PER_the_memphis_initiative"]
        n285["PER_we_survived"]
    end
    subgraph tier_10["Tier 10"]
        n286["PER_middle_east_protectorate"]
    end
    n221 --> n223
    n273 --> n280
    n268 --> n272
    n212 --> n214
    n212 --> n215
    n243 --> n247
    n235 --> n237
    n229 --> n230
    n229 --> n231
    n267 --> n273
    n234 --> n238
    n234 --> n239
    n256 --> n259
    n272 --> n281
    n245 --> n248
    n237 --> n249
    n237 --> n250
    n264 --> n274
    n225 --> n232
    n223 --> n233
    n257 --> n260
    n213 --> n216
    n212 --> n216
    n249 --> n261
    n275 --> n282
    n278 --> n282
    n277 --> n282
    n214 --> n224
    n215 --> n225
    n212 --> n217
    n213 --> n218
    n213 --> n219
    n260 --> n275
    n271 --> n275
    n269 --> n276
    n261 --> n276
    n270 --> n276
    n262 --> n276
    n95 --> n212
    n245 --> n251
    n263 --> n277
    n283 --> n286
    n219 --> n226
    n248 --> n262
    n218 --> n227
    n256 --> n263
    n213 --> n220
    n240 --> n252
    n252 --> n264
    n253 --> n264
    n255 --> n265
    n247 --> n265
    n240 --> n253
    n236 --> n240
    n242 --> n254
    n254 --> n266
    n258 --> n267
    n267 --> n278
    n230 --> n241
    n231 --> n241
    n212 --> n221
    n220 --> n228
    n235 --> n242
    n233 --> n242
    n272 --> n283
    n236 --> n243
    n248 --> n268
    n95 --> n213
    n230 --> n244
    n231 --> n244
    n251 --> n269
    n233 --> n245
    n225 --> n234
    n277 --> n284
    n215 --> n229
    n224 --> n235
    n213 --> n222
    n250 --> n270
    n243 --> n255
    n257 --> n271
    n230 --> n246
    n231 --> n246
    n239 --> n256
    n238 --> n256
    n239 --> n257
    n238 --> n257
    n239 --> n258
    n238 --> n258
    n279 --> n285
    n274 --> n285
    n265 --> n279
    n228 --> n236
    n226 --> n236
    n214 x--x n221
    n248 x--x n251
    n249 x--x n250
    n212 x--x n213
    n240 x--x n243
    n94 x--x n95
    n241 x--x n244
    n241 x--x n246
    n244 x--x n246
```
