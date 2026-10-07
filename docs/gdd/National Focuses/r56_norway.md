# NOR_air_bases

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("NOR_air_bases"))
        n2["NOR_army_wing"]
        n3["NOR_navy_wing"]
    end
    subgraph tier_1["Tier 1"]
        n4["NOR_merge_the_air_wings"]
    end
    subgraph tier_2["Tier 2"]
        n5["NOR_fortify_military_bases"]
        n6["NOR_light_fighters"]
        n7["NOR_medium_aircraft"]
    end
    subgraph tier_3["Tier 3"]
        n8["NOR_resurrect_norsk_aeroplanfabrik"]
    end
    n4 --> n5
    n4 --> n6
    n4 --> n7
    n1 --> n4
    n3 --> n4
    n2 --> n4
    n7 --> n8
```

# NOR_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["NOR_air_bases"]
        n9(("NOR_army"))
        n10["NOR_expand_domestic_steel_production"]
        n3["NOR_navy_wing"]
    end
    subgraph tier_1["Tier 1"]
        n2["NOR_army_wing"]
        n11["NOR_equipment_effort"]
        n12["NOR_fund_the_rearmament"]
        n13["NOR_ski_infantry"]
    end
    subgraph tier_2["Tier 2"]
        n14["NOR_a_serious_defense_budget"]
        n15["NOR_armament_investments"]
        n16["NOR_encourage_recreational_shooting"]
        n17["NOR_merge_jegerbataljonene"]
        n4["NOR_merge_the_air_wings"]
        n18["NOR_mountaineers"]
        n19["NOR_urban_defenses"]
    end
    subgraph tier_3["Tier 3"]
        n20["NOR_armament_investments_2"]
        n21{"NOR_continued_motorization_efforts"}
        n22["NOR_establish_heimevernet"]
        n5["NOR_fortify_military_bases"]
        n6["NOR_light_fighters"]
        n7["NOR_medium_aircraft"]
    end
    subgraph tier_4["Tier 4"]
        n23["NOR_armament_investments_3"]
        n24["NOR_armored_battalions"]
        n25["NOR_bicycle_battalions"]
        n8["NOR_resurrect_norsk_aeroplanfabrik"]
    end
    subgraph tier_5["Tier 5"]
        n26["NOR_kongsberg_research"]
    end
    n12 --> n14
    n12 --> n15
    n15 --> n20
    n14 --> n23
    n20 --> n23
    n10 --> n23
    n21 --> n24
    n9 --> n2
    n21 --> n25
    n17 --> n21
    n18 --> n21
    n11 --> n16
    n9 --> n11
    n16 --> n22
    n19 --> n22
    n4 --> n5
    n9 --> n12
    n23 --> n26
    n4 --> n6
    n4 --> n7
    n13 --> n17
    n1 --> n4
    n3 --> n4
    n2 --> n4
    n13 --> n18
    n7 --> n8
    n9 --> n13
    n13 --> n19
    n11 --> n19
    n24 x--x n25
```

# NOR_de_norske_statsbaner

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14["NOR_a_serious_defense_budget"]
        n20["NOR_armament_investments_2"]
        n27(("NOR_de_norske_statsbaner"))
        n28["NOR_expanded_aluminium_production"]
        n29["NOR_invest_in_district_industries"]
    end
    subgraph tier_1["Tier 1"]
        n30["NOR_nordlandsbanen"]
        n31["NOR_norsk_jernverk"]
    end
    subgraph tier_2["Tier 2"]
        n32["NOR_access_the_small_deposits"]
        n10["NOR_expand_domestic_steel_production"]
    end
    subgraph tier_3["Tier 3"]
        n23["NOR_armament_investments_3"]
        n33["NOR_statmin"]
    end
    subgraph tier_4["Tier 4"]
        n26["NOR_kongsberg_research"]
        n34["NOR_nth"]
    end
    subgraph tier_5["Tier 5"]
        n35["NOR_tungtvann"]
    end
    n31 --> n32
    n14 --> n23
    n20 --> n23
    n10 --> n23
    n31 --> n10
    n23 --> n26
    n27 --> n30
    n27 --> n31
    n33 --> n34
    n28 --> n34
    n29 --> n34
    n10 --> n33
    n32 --> n33
    n34 --> n35
```

# NOR_encourage_fishing

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36(("NOR_encourage_fishing"))
        n37["NOR_establish_nortraship"]
        n38["NOR_navy"]
    end
    subgraph tier_1["Tier 1"]
        n39["NOR_landing_crafts"]
        n40["NOR_nortraship_production_incentives"]
    end
    subgraph tier_2["Tier 2"]
        n41["NOR_coastal_defense_specialization"]
    end
    subgraph tier_3["Tier 3"]
        n42["NOR_naval_conferences"]
    end
    n40 --> n41
    n36 --> n39
    n37 --> n39
    n41 --> n42
    n36 --> n40
    n38 --> n40
    n37 --> n40
```

# NOR_establish_nortraship

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36["NOR_encourage_fishing"]
        n37(("NOR_establish_nortraship"))
        n38["NOR_navy"]
    end
    subgraph tier_1["Tier 1"]
        n39["NOR_landing_crafts"]
        n40["NOR_nortraship_production_incentives"]
    end
    subgraph tier_2["Tier 2"]
        n41["NOR_coastal_defense_specialization"]
    end
    subgraph tier_3["Tier 3"]
        n42["NOR_naval_conferences"]
    end
    n40 --> n41
    n36 --> n39
    n37 --> n39
    n41 --> n42
    n36 --> n40
    n38 --> n40
    n37 --> n40
```

# NOR_lumber_industries

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28["NOR_expanded_aluminium_production"]
        n43(("NOR_lumber_industries"))
        n33["NOR_statmin"]
    end
    subgraph tier_1["Tier 1"]
        n29["NOR_invest_in_district_industries"]
    end
    subgraph tier_2["Tier 2"]
        n34["NOR_nth"]
    end
    subgraph tier_3["Tier 3"]
        n35["NOR_tungtvann"]
    end
    n43 --> n29
    n33 --> n34
    n28 --> n34
    n29 --> n34
    n34 --> n35
```

# NOR_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["NOR_air_bases"]
        n2["NOR_army_wing"]
        n36["NOR_encourage_fishing"]
        n37["NOR_establish_nortraship"]
        n38(("NOR_navy"))
    end
    subgraph tier_1["Tier 1"]
        n44["NOR_develop_naval_tactics"]
        n45["NOR_escorts"]
        n3["NOR_navy_wing"]
        n40["NOR_nortraship_production_incentives"]
    end
    subgraph tier_2["Tier 2"]
        n46["NOR_capital_ships"]
        n47["NOR_carriers"]
        n41["NOR_coastal_defense_specialization"]
        n4["NOR_merge_the_air_wings"]
        n48["NOR_submarines"]
    end
    subgraph tier_3["Tier 3"]
        n5["NOR_fortify_military_bases"]
        n6["NOR_light_fighters"]
        n7["NOR_medium_aircraft"]
        n42["NOR_naval_conferences"]
        n49["NOR_naval_equipment"]
    end
    subgraph tier_4["Tier 4"]
        n8["NOR_resurrect_norsk_aeroplanfabrik"]
    end
    n45 --> n46
    n44 --> n46
    n44 --> n47
    n3 --> n47
    n40 --> n41
    n38 --> n44
    n38 --> n45
    n4 --> n5
    n4 --> n6
    n4 --> n7
    n1 --> n4
    n3 --> n4
    n2 --> n4
    n41 --> n42
    n46 --> n49
    n47 --> n49
    n38 --> n3
    n36 --> n40
    n38 --> n40
    n37 --> n40
    n7 --> n8
    n45 --> n48
```

# NOR_norsk_hydro_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29["NOR_invest_in_district_industries"]
        n50(("NOR_norsk_hydro_focus"))
        n33["NOR_statmin"]
    end
    subgraph tier_1["Tier 1"]
        n51["NOR_hydroelectric_power_generation"]
    end
    subgraph tier_2["Tier 2"]
        n28["NOR_expanded_aluminium_production"]
    end
    subgraph tier_3["Tier 3"]
        n34["NOR_nth"]
    end
    subgraph tier_4["Tier 4"]
        n35["NOR_tungtvann"]
    end
    n51 --> n28
    n50 --> n51
    n33 --> n34
    n28 --> n34
    n29 --> n34
    n34 --> n35
```

# NOR_til_dovre_faller

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n52{"NOR_til_dovre_faller"}
    end
    subgraph tier_1["Tier 1"]
        n53{"NOR_affirm_constitutional_monarchy"}
        n54{"NOR_reject_constitutional_monarchy"}
        n55["NOR_traditions_and_monarchy"]
    end
    subgraph tier_2["Tier 2"]
        n56{"NOR_change_starts_within"}
        n57{"NOR_continuous_politics"}
        n58["NOR_develop_the_kingdom"]
        n59{"NOR_motion_of_no_confidence"}
        n60["NOR_support_neighbors"]
        n61{"NOR_support_radical_nationalism"}
        n62{"NOR_support_radical_socialism"}
    end
    subgraph tier_3["Tier 3"]
        n63["NOR_a_communist_alternative"]
        n64["NOR_armed_neutrality_once_more"]
        n65["NOR_collectivism"]
        n66["NOR_german_puppet"]
        n67["NOR_gutta_paa_skauen"]
        n68["NOR_hirden_paramilitary"]
        n69["NOR_join_axis"]
        n70["NOR_join_comintern"]
        n71["NOR_norway_first"]
        n72["NOR_seek_a_british_alliance"]
        n73["NOR_three_brothers"]
        n74["NOR_traditions_worth_fighting_for"]
    end
    subgraph tier_4["Tier 4"]
        n75["NOR_a_prosperous_kingdom"]
        n76["NOR_allied_technology_sharing"]
        n77["NOR_delegate_control_of_the_merchant_fleet"]
        n78["NOR_folkearmeen"]
        n79["NOR_fourth_brother"]
        n80["NOR_german_technology_sharing"]
        n81["NOR_heavy_industry_plan"]
        n82["NOR_invite_terboven"]
        n83["NOR_matters_of_practicality"]
        n84["NOR_matters_of_presentation"]
        n85["NOR_nordic_technology_sharing"]
        n86["NOR_prepare_the_proletariat_for_war"]
        n87["NOR_reclaim_danish"]
        n88["NOR_rinnanbanden"]
        n89["NOR_saboteurs"]
        n90["NOR_soviet_technology_sharing"]
        n91["NOR_the_dano-norwegian_deal"]
    end
    subgraph tier_5["Tier 5"]
        n92["NOR_expand_allied_technology_sharing"]
        n93{"NOR_expand_german_technology_sharing"}
        n94["NOR_expand_nordic_technology_sharing"]
        n95["NOR_expand_soviet_technology_sharing"]
        n96{"NOR_festung_norwegen"}
        n97["NOR_invite_finland"]
        n98{"NOR_north_atlantic_defense_focus"}
        n99["NOR_reclaim_swedish"]
        n100["NOR_the_extent_of_power"]
        n101{"NOR_the_fennoscandian_deal"}
        n102["NOR_the_location_of_power"]
        n103["NOR_unite_the_scandinavian_workers"]
        n104["NOR_workers_war_economy"]
    end
    subgraph tier_6["Tier 6"]
        n105["NOR_american_military_support"]
        n106["NOR_at_any_cost"]
        n107["NOR_british_military_support"]
        n108["NOR_demand_russian_territories"]
        n109["NOR_establish_a_secret_police"]
        n110["NOR_foreign_relations"]
        n111["NOR_german_naval_coordination"]
        n112["NOR_nordic_joint_defense_focus"]
        n113{"NOR_pragmatic_diplomacy"}
        n114["NOR_pressure_finland"]
        n115["NOR_seek_american_support"]
    end
    subgraph tier_7["Tier 7"]
        n116{"NOR_demand_the_northern_isles"}
        n117["NOR_perfect_state_propaganda"]
        n118{"NOR_request_allied_favors"}
        n119["NOR_secret_departments"]
        n120["NOR_stand_against_communism"]
        n121["NOR_stand_against_fascism"]
        n122["NOR_the_brotherhood_of_nations"]
        n123{"NOR_the_european_policy"}
        n124{"NOR_the_nordic_policy"}
    end
    subgraph tier_8["Tier 8"]
        n125["NOR_a_beacon_among_democracies"]
        n126{"NOR_a_piece_in_the_greater_game"}
        n127{"NOR_approach_denmark"}
        n128["NOR_demand_overseas_colonies"]
        n129["NOR_demand_scottish_lands"]
        n130["NOR_end_foreign_influence"]
        n131["NOR_expand_the_intelligence_service"]
        n132{"NOR_reclaim_the_islands"}
        n133["NOR_revise_the_treaty_of_kiel"]
        n134["NOR_take_no_sides"]
    end
    subgraph tier_9["Tier 9"]
        n135{"NOR_approach_sweden"}
        n136{"NOR_baltic_anti-communist_league"}
        n137["NOR_icelandic-faroese_revolt"]
        n138{"NOR_reclaim_the_mainland"}
        n139{"NOR_the_british_empire"}
        n140{"NOR_the_german_kaiserreich"}
    end
    subgraph tier_10["Tier 10"]
        n141["NOR_a_deal_with_britain"]
        n142["NOR_a_deal_with_germany"]
        n143["NOR_approach_finland"]
        n144["NOR_baltic_league_deterrence"]
        n145["NOR_baltic_league_strikes_east"]
        n146["NOR_baltic_league_strikes_west"]
        n147["NOR_develop_iceland"]
        n148["NOR_develop_the_faroes"]
        n149["NOR_subjugate_finland"]
        n150["NOR_the_north_sea_deal"]
    end
    subgraph tier_11["Tier 11"]
        n151["NOR_develop_the_jarldom_of_orkney"]
    end
    n118 --> n125
    n62 --> n63
    n139 --> n141
    n140 --> n142
    n123 --> n126
    n74 --> n75
    n52 --> n53
    n72 --> n76
    n98 --> n105
    n124 --> n127
    n138 --> n143
    n135 --> n143
    n132 --> n135
    n127 --> n135
    n57 --> n64
    n56 --> n64
    n59 --> n64
    n96 --> n106
    n99 --> n106
    n126 --> n136
    n136 --> n144
    n136 --> n145
    n136 --> n146
    n98 --> n107
    n53 --> n56
    n62 --> n65
    n53 --> n57
    n72 --> n77
    n116 --> n128
    n93 --> n108
    n96 --> n108
    n116 --> n129
    n106 --> n116
    n137 --> n147
    n137 --> n148
    n147 --> n151
    n148 --> n151
    n55 --> n58
    n120 --> n130
    n121 --> n130
    n103 --> n109
    n76 --> n92
    n80 --> n93
    n85 --> n94
    n90 --> n95
    n119 --> n131
    n82 --> n96
    n65 --> n78
    n102 --> n110
    n100 --> n110
    n73 --> n79
    n93 --> n111
    n61 --> n66
    n69 --> n80
    n66 --> n80
    n60 --> n67
    n65 --> n81
    n61 --> n68
    n132 --> n137
    n79 --> n97
    n71 --> n82
    n69 --> n82
    n66 --> n82
    n61 --> n69
    n62 --> n70
    n74 --> n83
    n74 --> n84
    n53 --> n59
    n94 --> n112
    n97 --> n112
    n101 --> n112
    n73 --> n85
    n77 --> n98
    n61 --> n71
    n114 --> n117
    n109 --> n117
    n101 --> n113
    n63 --> n86
    n103 --> n114
    n69 --> n87
    n71 --> n87
    n87 --> n99
    n124 --> n132
    n132 --> n138
    n127 --> n138
    n52 --> n54
    n105 --> n118
    n107 --> n118
    n118 --> n133
    n68 --> n88
    n67 --> n89
    n109 --> n119
    n57 --> n72
    n56 --> n72
    n59 --> n72
    n101 --> n115
    n70 --> n90
    n113 --> n120
    n113 --> n121
    n138 --> n149
    n135 --> n149
    n53 --> n60
    n54 --> n61
    n54 --> n62
    n123 --> n134
    n126 --> n139
    n112 --> n122
    n73 --> n91
    n110 --> n123
    n83 --> n100
    n91 --> n101
    n126 --> n140
    n84 --> n102
    n110 --> n124
    n139 --> n150
    n140 --> n150
    n57 --> n73
    n56 --> n73
    n59 --> n73
    n52 --> n55
    n58 --> n74
    n78 --> n103
    n86 --> n104
    n78 --> n104
    n125 x--x n133
    n63 x--x n70
    n141 x--x n142
    n141 x--x n150
    n142 x--x n150
    n126 x--x n134
    n53 x--x n54
    n53 x--x n55
    n105 x--x n107
    n127 x--x n132
    n143 x--x n149
    n135 x--x n138
    n64 x--x n72
    n64 x--x n73
    n136 x--x n139
    n136 x--x n140
    n144 x--x n145
    n144 x--x n146
    n145 x--x n146
    n56 x--x n57
    n56 x--x n59
    n57 x--x n59
    n128 x--x n108
    n128 x--x n129
    n108 x--x n129
    n66 x--x n69
    n66 x--x n71
    n69 x--x n71
    n113 x--x n115
    n54 x--x n55
    n72 x--x n73
    n120 x--x n121
    n61 x--x n62
    n139 x--x n140
```
