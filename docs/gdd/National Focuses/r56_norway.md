# NOR_air_bases

```mermaid
flowchart TD
    n1(("NOR_air_bases"))
    n2["NOR_army_wing"]
    n3["NOR_fortify_military_bases"]
    n4["NOR_light_fighters"]
    n5["NOR_medium_aircraft"]
    n6["NOR_merge_the_air_wings"]
    n7["NOR_navy_wing"]
    n8["NOR_resurrect_norsk_aeroplanfabrik"]
    n6 --> n3
    n6 --> n4
    n6 --> n5
    n1 --> n6
    n7 --> n6
    n2 --> n6
    n5 --> n8
```

# NOR_army

```mermaid
flowchart TD
    n9["NOR_a_serious_defense_budget"]
    n1["NOR_air_bases"]
    n10["NOR_armament_investments"]
    n11["NOR_armament_investments_2"]
    n12["NOR_armament_investments_3"]
    n13["NOR_armored_battalions"]
    n14(("NOR_army"))
    n2["NOR_army_wing"]
    n15["NOR_bicycle_battalions"]
    n16{"NOR_continued_motorization_efforts"}
    n17["NOR_encourage_recreational_shooting"]
    n18["NOR_equipment_effort"]
    n19["NOR_establish_heimevernet"]
    n20["NOR_expand_domestic_steel_production"]
    n3["NOR_fortify_military_bases"]
    n21["NOR_fund_the_rearmament"]
    n22["NOR_kongsberg_research"]
    n4["NOR_light_fighters"]
    n5["NOR_medium_aircraft"]
    n23["NOR_merge_jegerbataljonene"]
    n6["NOR_merge_the_air_wings"]
    n24["NOR_mountaineers"]
    n7["NOR_navy_wing"]
    n8["NOR_resurrect_norsk_aeroplanfabrik"]
    n25["NOR_ski_infantry"]
    n26["NOR_urban_defenses"]
    n21 --> n9
    n21 --> n10
    n10 --> n11
    n9 --> n12
    n11 --> n12
    n20 --> n12
    n16 --> n13
    n14 --> n2
    n16 --> n15
    n23 --> n16
    n24 --> n16
    n18 --> n17
    n14 --> n18
    n17 --> n19
    n26 --> n19
    n6 --> n3
    n14 --> n21
    n12 --> n22
    n6 --> n4
    n6 --> n5
    n25 --> n23
    n1 --> n6
    n7 --> n6
    n2 --> n6
    n25 --> n24
    n5 --> n8
    n14 --> n25
    n25 --> n26
    n18 --> n26
    n13 x--x n15
```

# NOR_de_norske_statsbaner

```mermaid
flowchart TD
    n9["NOR_a_serious_defense_budget"]
    n27["NOR_access_the_small_deposits"]
    n11["NOR_armament_investments_2"]
    n12["NOR_armament_investments_3"]
    n28(("NOR_de_norske_statsbaner"))
    n20["NOR_expand_domestic_steel_production"]
    n29["NOR_expanded_aluminium_production"]
    n30["NOR_invest_in_district_industries"]
    n22["NOR_kongsberg_research"]
    n31["NOR_nordlandsbanen"]
    n32["NOR_norsk_jernverk"]
    n33["NOR_nth"]
    n34["NOR_statmin"]
    n35["NOR_tungtvann"]
    n32 --> n27
    n9 --> n12
    n11 --> n12
    n20 --> n12
    n32 --> n20
    n12 --> n22
    n28 --> n31
    n28 --> n32
    n34 --> n33
    n29 --> n33
    n30 --> n33
    n20 --> n34
    n27 --> n34
    n33 --> n35
```

# NOR_encourage_fishing

```mermaid
flowchart TD
    n36["NOR_coastal_defense_specialization"]
    n37(("NOR_encourage_fishing"))
    n38["NOR_establish_nortraship"]
    n39["NOR_landing_crafts"]
    n40["NOR_naval_conferences"]
    n41["NOR_navy"]
    n42["NOR_nortraship_production_incentives"]
    n42 --> n36
    n37 --> n39
    n38 --> n39
    n36 --> n40
    n37 --> n42
    n41 --> n42
    n38 --> n42
```

# NOR_establish_nortraship

```mermaid
flowchart TD
    n36["NOR_coastal_defense_specialization"]
    n37["NOR_encourage_fishing"]
    n38(("NOR_establish_nortraship"))
    n39["NOR_landing_crafts"]
    n40["NOR_naval_conferences"]
    n41["NOR_navy"]
    n42["NOR_nortraship_production_incentives"]
    n42 --> n36
    n37 --> n39
    n38 --> n39
    n36 --> n40
    n37 --> n42
    n41 --> n42
    n38 --> n42
```

# NOR_lumber_industries

```mermaid
flowchart TD
    n29["NOR_expanded_aluminium_production"]
    n30["NOR_invest_in_district_industries"]
    n43(("NOR_lumber_industries"))
    n33["NOR_nth"]
    n34["NOR_statmin"]
    n35["NOR_tungtvann"]
    n43 --> n30
    n34 --> n33
    n29 --> n33
    n30 --> n33
    n33 --> n35
```

# NOR_navy

```mermaid
flowchart TD
    n1["NOR_air_bases"]
    n2["NOR_army_wing"]
    n44["NOR_capital_ships"]
    n45["NOR_carriers"]
    n36["NOR_coastal_defense_specialization"]
    n46["NOR_develop_naval_tactics"]
    n37["NOR_encourage_fishing"]
    n47["NOR_escorts"]
    n38["NOR_establish_nortraship"]
    n3["NOR_fortify_military_bases"]
    n4["NOR_light_fighters"]
    n5["NOR_medium_aircraft"]
    n6["NOR_merge_the_air_wings"]
    n40["NOR_naval_conferences"]
    n48["NOR_naval_equipment"]
    n41(("NOR_navy"))
    n7["NOR_navy_wing"]
    n42["NOR_nortraship_production_incentives"]
    n8["NOR_resurrect_norsk_aeroplanfabrik"]
    n49["NOR_submarines"]
    n47 --> n44
    n46 --> n44
    n46 --> n45
    n7 --> n45
    n42 --> n36
    n41 --> n46
    n41 --> n47
    n6 --> n3
    n6 --> n4
    n6 --> n5
    n1 --> n6
    n7 --> n6
    n2 --> n6
    n36 --> n40
    n44 --> n48
    n45 --> n48
    n41 --> n7
    n37 --> n42
    n41 --> n42
    n38 --> n42
    n5 --> n8
    n47 --> n49
```

# NOR_norsk_hydro_focus

```mermaid
flowchart TD
    n29["NOR_expanded_aluminium_production"]
    n50["NOR_hydroelectric_power_generation"]
    n30["NOR_invest_in_district_industries"]
    n51(("NOR_norsk_hydro_focus"))
    n33["NOR_nth"]
    n34["NOR_statmin"]
    n35["NOR_tungtvann"]
    n50 --> n29
    n51 --> n50
    n34 --> n33
    n29 --> n33
    n30 --> n33
    n33 --> n35
```

# NOR_til_dovre_faller

```mermaid
flowchart TD
    n52["NOR_a_beacon_among_democracies"]
    n53["NOR_a_communist_alternative"]
    n54["NOR_a_deal_with_britain"]
    n55["NOR_a_deal_with_germany"]
    n56{"NOR_a_piece_in_the_greater_game"}
    n57["NOR_a_prosperous_kingdom"]
    n58{"NOR_affirm_constitutional_monarchy"}
    n59["NOR_allied_technology_sharing"]
    n60["NOR_american_military_support"]
    n61{"NOR_approach_denmark"}
    n62["NOR_approach_finland"]
    n63{"NOR_approach_sweden"}
    n64["NOR_armed_neutrality_once_more"]
    n65["NOR_at_any_cost"]
    n66{"NOR_baltic_anti-communist_league"}
    n67["NOR_baltic_league_deterrence"]
    n68["NOR_baltic_league_strikes_east"]
    n69["NOR_baltic_league_strikes_west"]
    n70["NOR_british_military_support"]
    n71{"NOR_change_starts_within"}
    n72["NOR_collectivism"]
    n73{"NOR_continuous_politics"}
    n74["NOR_delegate_control_of_the_merchant_fleet"]
    n75["NOR_demand_overseas_colonies"]
    n76["NOR_demand_russian_territories"]
    n77["NOR_demand_scottish_lands"]
    n78{"NOR_demand_the_northern_isles"}
    n79["NOR_develop_iceland"]
    n80["NOR_develop_the_faroes"]
    n81["NOR_develop_the_jarldom_of_orkney"]
    n82["NOR_develop_the_kingdom"]
    n83["NOR_end_foreign_influence"]
    n84["NOR_establish_a_secret_police"]
    n85["NOR_expand_allied_technology_sharing"]
    n86{"NOR_expand_german_technology_sharing"}
    n87["NOR_expand_nordic_technology_sharing"]
    n88["NOR_expand_soviet_technology_sharing"]
    n89["NOR_expand_the_intelligence_service"]
    n90{"NOR_festung_norwegen"}
    n91["NOR_folkearmeen"]
    n92["NOR_foreign_relations"]
    n93["NOR_fourth_brother"]
    n94["NOR_german_naval_coordination"]
    n95["NOR_german_puppet"]
    n96["NOR_german_technology_sharing"]
    n97["NOR_gutta_paa_skauen"]
    n98["NOR_heavy_industry_plan"]
    n99["NOR_hirden_paramilitary"]
    n100["NOR_icelandic-faroese_revolt"]
    n101["NOR_invite_finland"]
    n102["NOR_invite_terboven"]
    n103["NOR_join_axis"]
    n104["NOR_join_comintern"]
    n105["NOR_matters_of_practicality"]
    n106["NOR_matters_of_presentation"]
    n107{"NOR_motion_of_no_confidence"}
    n108["NOR_nordic_joint_defense_focus"]
    n109["NOR_nordic_technology_sharing"]
    n110{"NOR_north_atlantic_defense_focus"}
    n111["NOR_norway_first"]
    n112["NOR_perfect_state_propaganda"]
    n113{"NOR_pragmatic_diplomacy"}
    n114["NOR_prepare_the_proletariat_for_war"]
    n115["NOR_pressure_finland"]
    n116["NOR_reclaim_danish"]
    n117["NOR_reclaim_swedish"]
    n118{"NOR_reclaim_the_islands"}
    n119{"NOR_reclaim_the_mainland"}
    n120{"NOR_reject_constitutional_monarchy"}
    n121{"NOR_request_allied_favors"}
    n122["NOR_revise_the_treaty_of_kiel"]
    n123["NOR_rinnanbanden"]
    n124["NOR_saboteurs"]
    n125["NOR_secret_departments"]
    n126["NOR_seek_a_british_alliance"]
    n127["NOR_seek_american_support"]
    n128["NOR_soviet_technology_sharing"]
    n129["NOR_stand_against_communism"]
    n130["NOR_stand_against_fascism"]
    n131["NOR_subjugate_finland"]
    n132["NOR_support_neighbors"]
    n133{"NOR_support_radical_nationalism"}
    n134{"NOR_support_radical_socialism"}
    n135["NOR_take_no_sides"]
    n136{"NOR_the_british_empire"}
    n137["NOR_the_brotherhood_of_nations"]
    n138["NOR_the_dano-norwegian_deal"]
    n139{"NOR_the_european_policy"}
    n140["NOR_the_extent_of_power"]
    n141{"NOR_the_fennoscandian_deal"}
    n142{"NOR_the_german_kaiserreich"}
    n143["NOR_the_location_of_power"]
    n144{"NOR_the_nordic_policy"}
    n145["NOR_the_north_sea_deal"]
    n146["NOR_three_brothers"]
    n147{"NOR_til_dovre_faller"}
    n148["NOR_traditions_and_monarchy"]
    n149["NOR_traditions_worth_fighting_for"]
    n150["NOR_unite_the_scandinavian_workers"]
    n151["NOR_workers_war_economy"]
    n121 --> n52
    n134 --> n53
    n136 --> n54
    n142 --> n55
    n139 --> n56
    n149 --> n57
    n147 --> n58
    n126 --> n59
    n110 --> n60
    n144 --> n61
    n119 --> n62
    n63 --> n62
    n118 --> n63
    n61 --> n63
    n73 --> n64
    n71 --> n64
    n107 --> n64
    n90 --> n65
    n117 --> n65
    n56 --> n66
    n66 --> n67
    n66 --> n68
    n66 --> n69
    n110 --> n70
    n58 --> n71
    n134 --> n72
    n58 --> n73
    n126 --> n74
    n78 --> n75
    n86 --> n76
    n90 --> n76
    n78 --> n77
    n65 --> n78
    n100 --> n79
    n100 --> n80
    n79 --> n81
    n80 --> n81
    n148 --> n82
    n129 --> n83
    n130 --> n83
    n150 --> n84
    n59 --> n85
    n96 --> n86
    n109 --> n87
    n128 --> n88
    n125 --> n89
    n102 --> n90
    n72 --> n91
    n143 --> n92
    n140 --> n92
    n146 --> n93
    n86 --> n94
    n133 --> n95
    n103 --> n96
    n95 --> n96
    n132 --> n97
    n72 --> n98
    n133 --> n99
    n118 --> n100
    n93 --> n101
    n111 --> n102
    n103 --> n102
    n95 --> n102
    n133 --> n103
    n134 --> n104
    n149 --> n105
    n149 --> n106
    n58 --> n107
    n87 --> n108
    n101 --> n108
    n141 --> n108
    n146 --> n109
    n74 --> n110
    n133 --> n111
    n115 --> n112
    n84 --> n112
    n141 --> n113
    n53 --> n114
    n150 --> n115
    n103 --> n116
    n111 --> n116
    n116 --> n117
    n144 --> n118
    n118 --> n119
    n61 --> n119
    n147 --> n120
    n60 --> n121
    n70 --> n121
    n121 --> n122
    n99 --> n123
    n97 --> n124
    n84 --> n125
    n73 --> n126
    n71 --> n126
    n107 --> n126
    n141 --> n127
    n104 --> n128
    n113 --> n129
    n113 --> n130
    n119 --> n131
    n63 --> n131
    n58 --> n132
    n120 --> n133
    n120 --> n134
    n139 --> n135
    n56 --> n136
    n108 --> n137
    n146 --> n138
    n92 --> n139
    n105 --> n140
    n138 --> n141
    n56 --> n142
    n106 --> n143
    n92 --> n144
    n136 --> n145
    n142 --> n145
    n73 --> n146
    n71 --> n146
    n107 --> n146
    n147 --> n148
    n82 --> n149
    n91 --> n150
    n114 --> n151
    n91 --> n151
    n52 x--x n122
    n53 x--x n104
    n54 x--x n55
    n54 x--x n145
    n55 x--x n145
    n56 x--x n135
    n58 x--x n120
    n58 x--x n148
    n60 x--x n70
    n61 x--x n118
    n62 x--x n131
    n63 x--x n119
    n64 x--x n126
    n64 x--x n146
    n66 x--x n136
    n66 x--x n142
    n67 x--x n68
    n67 x--x n69
    n68 x--x n69
    n71 x--x n73
    n71 x--x n107
    n73 x--x n107
    n75 x--x n76
    n75 x--x n77
    n76 x--x n77
    n95 x--x n103
    n95 x--x n111
    n103 x--x n111
    n113 x--x n127
    n120 x--x n148
    n126 x--x n146
    n129 x--x n130
    n133 x--x n134
    n136 x--x n142
```
