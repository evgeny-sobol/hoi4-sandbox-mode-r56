# INS_defenders_of_homeland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"INS_defenders_of_homeland"}
        n2["INS_resist_occupation"]
        n3["INS_underground_revolution"]
    end
    subgraph tier_1["Tier 1"]
        n4["INS_embrace_co_prosp_sphere"]
        n5["INS_japanese_resource_infrastructure"]
        n6["INS_seize_oppurtunity"]
    end
    subgraph tier_2["Tier 2"]
        n7["INS_japanese_army_training"]
        n8["INS_the_declaration_of_independence"]
    end
    subgraph tier_3["Tier 3"]
        n9{"INS_just_a_fisherman"}
        n10["INS_laskar_rakjat"]
        n11{"INS_political_stabilization"}
        n12{"INS_the_peoples_security_army"}
    end
    subgraph tier_4["Tier 4"]
        n13["INS_a_cheap_navy"]
        n14["INS_assist_the_pemuda"]
        n15["INS_commander_oerip"]
        n16["INS_commander_sudirman"]
        n17["INS_darul_islam_focus"]
        n18["INS_deploy_the_kris"]
        n19["INS_divert_army_funds_to_navy"]
        n20{"INS_guided_democracy"}
        n21["INS_integrate_sarekat_islam"]
        n22["INS_nationalize"]
        n23["INS_recognize_moestopos_batallion"]
        n24["INS_restore_order"]
        n25["INS_secularism"]
        n26{"INS_subsidize_laskar_armament"}
        n27["INS_support_tan_malakas_coup"]
        n28["INS_unity_in_diversity"]
        n29["INS_utilize_tan_malakas_militia"]
        n30{"INS_vice_presidential_edict"}
    end
    subgraph tier_5["Tier 5"]
        n31["INS_admiral_mas_pardi"]
        n32["INS_agrarian_reform"]
        n33["INS_arm_the_revolutionaries"]
        n34{"INS_centralization"}
        n35["INS_continue_hybrid_politics"]
        n36["INS_develop_a_functioning_airforce"]
        n37["INS_dissolve_national_party"]
        n38["INS_guerilla_industry"]
        n39["INS_increase_laskar_funding"]
        n40{"INS_indonesian_assault_doctrine"}
        n41["INS_indonesian_naval_doctrine"]
        n42["INS_local_autonomy"]
        n43["INS_local_cooperatives"]
        n44["INS_local_unity"]
        n45["INS_organize_jakarta_pemuda"]
        n46{"INS_pacific_revolution"}
        n47["INS_railway_youth_force"]
        n48["INS_soviet_aid"]
        n49["INS_sudirmans_promotion"]
    end
    subgraph tier_6["Tier 6"]
        n50["INS_abolish_national_committee"]
        n51["INS_acquire_modern_blueprints"]
        n52["INS_akademi_angkatan_laut"]
        n53["INS_arm_the_youth"]
        n54["INS_domestic_shipbuilding"]
        n55["INS_education_subsidies"]
        n56{"INS_fair_election"}
        n57["INS_land_reform"]
        n58{"INS_musso_ascends"}
        n59["INS_purge_oppurtunists"]
        n60["INS_quality_over_quantity"]
        n61["INS_sukarno_retakeover"]
        n62["INS_the_co_prosperity_sphere"]
        n63["INS_the_three_year_plan"]
        n64["INS_tighter_tkr_integration"]
        n65["INS_union_of_ins_states"]
        n66["INS_womens_sufferage"]
    end
    subgraph tier_7["Tier 7"]
        n67["INS_arm_the_students"]
        n68["INS_divert_javanese_education_funding_the_east"]
        n69["INS_enact_militarism"]
        n70["INS_guided_economy"]
        n71["INS_indonesian_inter_province_trade_agreement"]
        n72["INS_minimum_program"]
        n73["INS_pan_asian_union"]
        n74["INS_pancasila_achieved"]
        n75["INS_prime_minister_hatta"]
        n76["INS_prime_minister_sjarifuddin"]
        n77["INS_rapid_mobilization"]
        n78["INS_realign_export_markets"]
        n79["INS_shining_from_the_periphery"]
        n80["INS_sjahrirs_continued_tenure"]
        n81["INS_strengthen_ins_jap_trade"]
        n82["INS_the_maphilindo_speech"]
        n83["INS_united_against_japan"]
        n84["INS_utilize_comintern_connections"]
        n85["INS_women_in_military"]
    end
    subgraph tier_8["Tier 8"]
        n86["INS_concessions_to_communists"]
        n87["INS_destroy_pacific_colonialism"]
        n88["INS_eastern_universities"]
        n89["INS_expanding_the_union"]
        n90["INS_federation_of_aslia"]
        n91["INS_hatta_focus_2"]
        n92["INS_japanese_military_lessons"]
        n93["INS_mixed_economy_system"]
        n94["INS_pan_economic_area"]
        n95["INS_pledge_to_allies"]
        n96["INS_reform_education_system"]
        n97["INS_revolutionary_economic_cooperation"]
        n98["INS_seek_recognition_of_mal_claims"]
        n99["INS_sjarifuddin_focus_2"]
        n100["INS_soviet_economic_integration"]
        n101["INS_sukarnos_industrialization"]
        n102["INS_the_timor_issue"]
    end
    subgraph tier_9["Tier 9"]
        n103["INS_all_toward_the_war_effort"]
        n104["INS_attack_philippines"]
        n105["INS_demand_northern_malay"]
        n106["INS_hatta_princely_advisors"]
        n107["INS_reform_education_system_2"]
        n108["INS_social_democracy"]
        n109["INS_sukarnos_industrialization2"]
        n110["INS_three_year_plan"]
    end
    subgraph tier_10["Tier 10"]
        n111["INS_siam_agreement"]
    end
    n9 --> n13
    n34 --> n50
    n41 --> n51
    n13 --> n31
    n19 --> n31
    n27 --> n32
    n31 --> n52
    n101 --> n103
    n16 --> n33
    n53 --> n67
    n33 --> n53
    n10 --> n14
    n98 --> n104
    n20 --> n34
    n12 --> n15
    n12 --> n16
    n76 --> n86
    n30 --> n35
    n10 --> n17
    n98 --> n105
    n10 --> n18
    n74 --> n87
    n26 --> n36
    n30 --> n37
    n9 --> n19
    n63 --> n68
    n41 --> n54
    n68 --> n88
    n44 --> n55
    n37 --> n55
    n1 --> n4
    n62 --> n69
    n71 --> n89
    n37 --> n56
    n82 --> n90
    n73 --> n90
    n16 --> n38
    n15 --> n38
    n11 --> n20
    n50 --> n70
    n35 --> n70
    n75 --> n91
    n91 --> n106
    n26 --> n39
    n15 --> n40
    n65 --> n71
    n19 --> n41
    n11 --> n21
    n5 --> n7
    n69 --> n92
    n81 --> n92
    n1 --> n5
    n8 --> n9
    n43 --> n57
    n8 --> n10
    n20 --> n42
    n30 --> n43
    n30 --> n44
    n59 --> n72
    n80 --> n93
    n46 --> n58
    n11 --> n22
    n14 --> n45
    n27 --> n46
    n59 --> n73
    n73 --> n94
    n50 --> n74
    n80 --> n95
    n75 --> n95
    n8 --> n11
    n56 --> n75
    n56 --> n76
    n46 --> n59
    n40 --> n60
    n14 --> n47
    n50 --> n77
    n62 --> n77
    n63 --> n78
    n10 --> n23
    n70 --> n96
    n96 --> n107
    n11 --> n24
    n84 --> n97
    n83 --> n97
    n11 --> n25
    n81 --> n98
    n1 --> n6
    n57 --> n79
    n105 --> n111
    n56 --> n80
    n76 --> n99
    n93 --> n108
    n27 --> n48
    n84 --> n100
    n62 --> n81
    n10 --> n26
    n16 --> n49
    n35 --> n61
    n77 --> n101
    n81 --> n101
    n101 --> n109
    n11 --> n27
    n34 --> n62
    n3 --> n8
    n6 --> n8
    n59 --> n82
    n8 --> n12
    n32 --> n63
    n80 --> n102
    n76 --> n102
    n96 --> n110
    n75 --> n110
    n40 --> n64
    n42 --> n65
    n58 --> n83
    n11 --> n28
    n58 --> n84
    n10 --> n29
    n11 --> n30
    n66 --> n85
    n37 --> n66
    n35 --> n66
    n13 x--x n19
    n50 x--x n62
    n34 x--x n42
    n15 x--x n16
    n35 x--x n37
    n1 x--x n2
    n36 x--x n39
    n4 x--x n6
    n20 x--x n27
    n20 x--x n30
    n21 x--x n25
    n58 x--x n59
    n75 x--x n76
    n75 x--x n80
    n76 x--x n80
    n60 x--x n64
    n27 x--x n30
    n83 x--x n84
```

# INS_recovering_from_the_great_depression

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n112{"INS_recovering_from_the_great_depression"}
    end
    subgraph tier_1["Tier 1"]
        n113{"INS_developing_java"}
        n114["INS_developing_sumatra"]
        n115["INS_first_come_first_serve"]
        n116{"INS_realign_supply_chains"}
        n117{"INS_the_bangka_project"}
    end
    subgraph tier_2["Tier 2"]
        n118["INS_all_cards_into_industry"]
        n119["INS_all_in_on_rubber"]
        n120["INS_aluminium_factory"]
        n121["INS_australian_contracts"]
        n122["INS_bauxite_export"]
        n123["INS_coopereate_with_chinese_businessmen"]
        n124["INS_develop_borneo"]
        n125["INS_develop_sulawesi"]
        n126["INS_expand_batavia_technical_institute"]
        n127["INS_fate_of_de_javasche_bank"]
        n128["INS_increased_trade_with_japan"]
        n129["INS_invite_foreign_companies"]
        n130["INS_not_industry"]
        n131["INS_prioritize_sugar_economy"]
        n132["INS_reallocate_rubber_industry_funding"]
        n133["INS_sumatra_railway"]
    end
    subgraph tier_3["Tier 3"]
        n134["INS_construction_focus"]
        n135["INS_finish_the_bauxite_project"]
        n136["INS_kalimantan_mic"]
        n137["INS_more_market_resources"]
        n138["INS_negotiate_new_contracts"]
        n139["INS_new_bauxite_routes"]
        n140["INS_pontianak_to_balikpapan"]
        n141["INS_quinine_export"]
        n142["INS_tin_mining"]
    end
    subgraph tier_4["Tier 4"]
        n143["INS_centralize_the_state"]
    end
    n113 --> n118
    n116 --> n119
    n117 --> n120
    n116 --> n121
    n115 --> n121
    n117 --> n122
    n133 --> n143
    n125 --> n143
    n140 --> n143
    n136 --> n143
    n126 --> n134
    n118 --> n134
    n130 --> n134
    n115 --> n123
    n114 --> n124
    n114 --> n125
    n112 --> n113
    n112 --> n114
    n113 --> n126
    n116 --> n127
    n122 --> n135
    n120 --> n135
    n112 --> n115
    n115 --> n128
    n116 --> n129
    n124 --> n136
    n131 --> n137
    n129 --> n138
    n119 --> n138
    n122 --> n139
    n113 --> n130
    n124 --> n140
    n115 --> n131
    n127 --> n141
    n112 --> n116
    n115 --> n132
    n114 --> n133
    n112 --> n117
    n127 --> n142
    n118 x--x n130
    n119 x--x n129
    n120 x--x n122
    n115 x--x n116
```

# INS_resist_occupation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["INS_defenders_of_homeland"]
        n2(("INS_resist_occupation"))
    end
    subgraph tier_1["Tier 1"]
        n144["INS_east_indies_exile_government"]
        n145["INS_local_resistance"]
        n146["INS_silence_nationalists"]
    end
    subgraph tier_2["Tier 2"]
        n147["INS_establish_nefis"]
        n148["INS_stronghold_java"]
    end
    subgraph tier_3["Tier 3"]
        n149["INS_australian_weapons"]
        n150["INS_evacuate_soldiers_to_australia"]
    end
    n147 --> n149
    n2 --> n144
    n144 --> n147
    n147 --> n150
    n2 --> n145
    n2 --> n146
    n145 --> n148
    n1 x--x n2
```

# INS_the_jewel_in_the_crown

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n151{"INS_the_jewel_in_the_crown"}
        n3["INS_underground_revolution"]
    end
    subgraph tier_1["Tier 1"]
        n152["INS_governor_general_de_jonge"]
        n153["INS_governor_general_tjarda"]
        n154["INS_prepare_for_policy_shift"]
        n155["INS_prioritize_dutch_companies"]
        n156["INS_subsidize_local_business"]
    end
    subgraph tier_2["Tier 2"]
        n157["INS_economic_stabilization"]
        n158["INS_electrical_investments"]
        n159["INS_expand_batavia_med_school"]
        n160["INS_invest_in_batavian_education"]
    end
    subgraph tier_3["Tier 3"]
        n161{"INS_detangle_supply_chains"}
        n162["INS_javanese_education_investments"]
        n163["INS_reduce_land_taxes"]
        n164["INS_restore_order_in_indies"]
    end
    subgraph tier_4["Tier 4"]
        n165["INS_closer_economic_ties_to_netherlands"]
        n166["INS_prioritize_industrial_growth"]
    end
    n161 --> n165
    n157 --> n161
    n152 --> n157
    n153 --> n158
    n156 --> n159
    n155 --> n159
    n151 --> n152
    n151 --> n153
    n153 --> n160
    n160 --> n162
    n151 --> n154
    n151 --> n155
    n161 --> n166
    n158 --> n163
    n157 --> n164
    n151 --> n156
    n165 x--x n166
    n155 x--x n156
    n151 x--x n3
```

# INS_underground_revolution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n6["INS_seize_oppurtunity"]
        n151["INS_the_jewel_in_the_crown"]
        n3(("INS_underground_revolution"))
    end
    subgraph tier_1["Tier 1"]
        n167["INS_infiltrate_the_army"]
        n168["INS_instigate_chaos_sulawesi"]
        n169["INS_prepare_raiding_bases"]
        n8["INS_the_declaration_of_independence"]
        n170["INS_volksraad_rumors"]
    end
    subgraph tier_2["Tier 2"]
        n171["INS_instigate_chaos_medan"]
        n9{"INS_just_a_fisherman"}
        n10["INS_laskar_rakjat"]
        n11{"INS_political_stabilization"}
        n172["INS_privately_owned_military_industry"]
        n173["INS_sleeper_informant_network"]
        n12{"INS_the_peoples_security_army"}
        n174["INS_tkr_steal_general"]
        n175["INS_tkr_supply"]
    end
    subgraph tier_3["Tier 3"]
        n13["INS_a_cheap_navy"]
        n14["INS_assist_the_pemuda"]
        n15["INS_commander_oerip"]
        n16["INS_commander_sudirman"]
        n17["INS_darul_islam_focus"]
        n18["INS_deploy_the_kris"]
        n19["INS_divert_army_funds_to_navy"]
        n20{"INS_guided_democracy"}
        n21["INS_integrate_sarekat_islam"]
        n22["INS_nationalize"]
        n23["INS_recognize_moestopos_batallion"]
        n24["INS_restore_order"]
        n25["INS_secularism"]
        n26{"INS_subsidize_laskar_armament"}
        n27["INS_support_tan_malakas_coup"]
        n28["INS_unity_in_diversity"]
        n29["INS_utilize_tan_malakas_militia"]
        n30{"INS_vice_presidential_edict"}
    end
    subgraph tier_4["Tier 4"]
        n31["INS_admiral_mas_pardi"]
        n32["INS_agrarian_reform"]
        n33["INS_arm_the_revolutionaries"]
        n34{"INS_centralization"}
        n35["INS_continue_hybrid_politics"]
        n36["INS_develop_a_functioning_airforce"]
        n37["INS_dissolve_national_party"]
        n38["INS_guerilla_industry"]
        n39["INS_increase_laskar_funding"]
        n40{"INS_indonesian_assault_doctrine"}
        n41["INS_indonesian_naval_doctrine"]
        n42["INS_local_autonomy"]
        n43["INS_local_cooperatives"]
        n44["INS_local_unity"]
        n45["INS_organize_jakarta_pemuda"]
        n46{"INS_pacific_revolution"}
        n47["INS_railway_youth_force"]
        n48["INS_soviet_aid"]
        n49["INS_sudirmans_promotion"]
    end
    subgraph tier_5["Tier 5"]
        n50["INS_abolish_national_committee"]
        n51["INS_acquire_modern_blueprints"]
        n52["INS_akademi_angkatan_laut"]
        n53["INS_arm_the_youth"]
        n54["INS_domestic_shipbuilding"]
        n55["INS_education_subsidies"]
        n56{"INS_fair_election"}
        n57["INS_land_reform"]
        n58{"INS_musso_ascends"}
        n59["INS_purge_oppurtunists"]
        n60["INS_quality_over_quantity"]
        n61["INS_sukarno_retakeover"]
        n62["INS_the_co_prosperity_sphere"]
        n63["INS_the_three_year_plan"]
        n64["INS_tighter_tkr_integration"]
        n65["INS_union_of_ins_states"]
        n66["INS_womens_sufferage"]
    end
    subgraph tier_6["Tier 6"]
        n67["INS_arm_the_students"]
        n68["INS_divert_javanese_education_funding_the_east"]
        n69["INS_enact_militarism"]
        n70["INS_guided_economy"]
        n71["INS_indonesian_inter_province_trade_agreement"]
        n72["INS_minimum_program"]
        n73["INS_pan_asian_union"]
        n74["INS_pancasila_achieved"]
        n75["INS_prime_minister_hatta"]
        n76["INS_prime_minister_sjarifuddin"]
        n77["INS_rapid_mobilization"]
        n78["INS_realign_export_markets"]
        n79["INS_shining_from_the_periphery"]
        n80["INS_sjahrirs_continued_tenure"]
        n81["INS_strengthen_ins_jap_trade"]
        n82["INS_the_maphilindo_speech"]
        n83["INS_united_against_japan"]
        n84["INS_utilize_comintern_connections"]
        n85["INS_women_in_military"]
    end
    subgraph tier_7["Tier 7"]
        n86["INS_concessions_to_communists"]
        n87["INS_destroy_pacific_colonialism"]
        n88["INS_eastern_universities"]
        n89["INS_expanding_the_union"]
        n90["INS_federation_of_aslia"]
        n91["INS_hatta_focus_2"]
        n92["INS_japanese_military_lessons"]
        n93["INS_mixed_economy_system"]
        n94["INS_pan_economic_area"]
        n95["INS_pledge_to_allies"]
        n96["INS_reform_education_system"]
        n97["INS_revolutionary_economic_cooperation"]
        n98["INS_seek_recognition_of_mal_claims"]
        n99["INS_sjarifuddin_focus_2"]
        n100["INS_soviet_economic_integration"]
        n101["INS_sukarnos_industrialization"]
        n102["INS_the_timor_issue"]
    end
    subgraph tier_8["Tier 8"]
        n103["INS_all_toward_the_war_effort"]
        n104["INS_attack_philippines"]
        n105["INS_demand_northern_malay"]
        n106["INS_hatta_princely_advisors"]
        n107["INS_reform_education_system_2"]
        n108["INS_social_democracy"]
        n109["INS_sukarnos_industrialization2"]
        n110["INS_three_year_plan"]
    end
    subgraph tier_9["Tier 9"]
        n111["INS_siam_agreement"]
    end
    n9 --> n13
    n34 --> n50
    n41 --> n51
    n13 --> n31
    n19 --> n31
    n27 --> n32
    n31 --> n52
    n101 --> n103
    n16 --> n33
    n53 --> n67
    n33 --> n53
    n10 --> n14
    n98 --> n104
    n20 --> n34
    n12 --> n15
    n12 --> n16
    n76 --> n86
    n30 --> n35
    n10 --> n17
    n98 --> n105
    n10 --> n18
    n74 --> n87
    n26 --> n36
    n30 --> n37
    n9 --> n19
    n63 --> n68
    n41 --> n54
    n68 --> n88
    n44 --> n55
    n37 --> n55
    n62 --> n69
    n71 --> n89
    n37 --> n56
    n82 --> n90
    n73 --> n90
    n16 --> n38
    n15 --> n38
    n11 --> n20
    n50 --> n70
    n35 --> n70
    n75 --> n91
    n91 --> n106
    n26 --> n39
    n15 --> n40
    n65 --> n71
    n19 --> n41
    n3 --> n167
    n168 --> n171
    n3 --> n168
    n11 --> n21
    n69 --> n92
    n81 --> n92
    n8 --> n9
    n43 --> n57
    n8 --> n10
    n20 --> n42
    n30 --> n43
    n30 --> n44
    n59 --> n72
    n80 --> n93
    n46 --> n58
    n11 --> n22
    n14 --> n45
    n27 --> n46
    n59 --> n73
    n73 --> n94
    n50 --> n74
    n80 --> n95
    n75 --> n95
    n8 --> n11
    n3 --> n169
    n56 --> n75
    n56 --> n76
    n167 --> n172
    n46 --> n59
    n40 --> n60
    n14 --> n47
    n50 --> n77
    n62 --> n77
    n63 --> n78
    n10 --> n23
    n70 --> n96
    n96 --> n107
    n11 --> n24
    n84 --> n97
    n83 --> n97
    n11 --> n25
    n81 --> n98
    n57 --> n79
    n105 --> n111
    n56 --> n80
    n76 --> n99
    n167 --> n173
    n93 --> n108
    n27 --> n48
    n84 --> n100
    n62 --> n81
    n10 --> n26
    n16 --> n49
    n35 --> n61
    n77 --> n101
    n81 --> n101
    n101 --> n109
    n11 --> n27
    n34 --> n62
    n3 --> n8
    n6 --> n8
    n59 --> n82
    n8 --> n12
    n32 --> n63
    n80 --> n102
    n76 --> n102
    n96 --> n110
    n75 --> n110
    n40 --> n64
    n167 --> n174
    n167 --> n175
    n42 --> n65
    n58 --> n83
    n11 --> n28
    n58 --> n84
    n10 --> n29
    n11 --> n30
    n3 --> n170
    n66 --> n85
    n37 --> n66
    n35 --> n66
    n13 x--x n19
    n50 x--x n62
    n34 x--x n42
    n15 x--x n16
    n35 x--x n37
    n36 x--x n39
    n20 x--x n27
    n20 x--x n30
    n21 x--x n25
    n58 x--x n59
    n75 x--x n76
    n75 x--x n80
    n76 x--x n80
    n60 x--x n64
    n27 x--x n30
    n151 x--x n3
    n83 x--x n84
```
