# r56_CAN_army_modernisation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("r56_CAN_army_modernisation"))
    end
    subgraph tier_1["Tier 1"]
        n2["r56_CAN_cmp_truck"]
        n3["r56_CAN_increase_budget"]
        n4["r56_can_rifle_association"]
    end
    subgraph tier_2["Tier 2"]
        n5["r56_CAN_british_designs"]
        n6["r56_CAN_increase_budget_more"]
        n7["r56_CAN_valentine_tank"]
    end
    subgraph tier_3["Tier 3"]
        n8["r56_CAN_canadian_armoured_corps"]
        n9["r56_CAN_retool_angus_shops"]
        n10["r56_CAN_royal_canadian_artillery"]
        n11["r56_CAN_walkie_talkie"]
    end
    subgraph tier_4["Tier 4"]
        n12["r56_CAN_kangaroo"]
        n13["r56_CAN_royal_canadian_corps_of_signals"]
        n14["r56_CAN_small_arms_limited"]
        n15["r56_CAN_the_ram"]
    end
    subgraph tier_5["Tier 5"]
        n16["r56_CAN_camp_borden"]
        n17["r56_CAN_land_mattress"]
        n18["r56_CAN_the_grizzly"]
    end
    n3 --> n5
    n14 --> n16
    n7 --> n8
    n1 --> n2
    n1 --> n3
    n3 --> n6
    n8 --> n12
    n14 --> n17
    n7 --> n9
    n5 --> n10
    n11 --> n13
    n10 --> n14
    n8 --> n14
    n12 --> n18
    n15 --> n18
    n8 --> n15
    n2 --> n7
    n5 --> n11
    n1 --> n4
```

# r56_CAN_depression_recovery

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19(("r56_CAN_depression_recovery"))
        n20["r56_CAN_modernize_industry"]
        n21["r56_CAN_replace_men_in_the_industry"]
    end
    subgraph tier_1["Tier 1"]
        n22["r56_CAN_dollar_a_year_men"]
        n23["r56_CAN_national_housing_act"]
        n24["r56_CAN_shutdown_relief_camps"]
        n25["r56_CAN_wheat_board"]
    end
    subgraph tier_2["Tier 2"]
        n26["r56_CAN_bank_of_canada"]
        n27["r56_CAN_canadian_pacific_railways"]
        n28["r56_CAN_cbc_focus"]
        n29["r56_CAN_debt_adjustment_act"]
        n30["r56_CAN_enlist_the_unemployed"]
        n31["r56_CAN_sorel_steel_and_foundry"]
    end
    subgraph tier_3["Tier 3"]
        n32["r56_CAN_alcan"]
        n33["r56_CAN_john_inglis_company"]
        n34["r56_CAN_national_railway"]
        n35["r56_CAN_national_steel_car"]
        n36["r56_CAN_sorel_industries"]
        n37["r56_CAN_war_economy"]
    end
    subgraph tier_4["Tier 4"]
        n38["r56_CAN_imperial_oil_focus"]
        n39["r56_CAN_research_grants"]
        n40["r56_CAN_resources_for_war_effort"]
        n41["r56_CAN_uranium_mining"]
    end
    subgraph tier_5["Tier 5"]
        n42["r56_CAN_establish_the_polymer_corporation"]
    end
    n26 --> n32
    n22 --> n26
    n22 --> n27
    n22 --> n28
    n23 --> n29
    n25 --> n29
    n19 --> n22
    n20 --> n22
    n23 --> n30
    n25 --> n30
    n24 --> n30
    n38 --> n42
    n32 --> n38
    n27 --> n33
    n19 --> n23
    n26 --> n34
    n27 --> n35
    n33 --> n39
    n34 --> n39
    n32 --> n40
    n37 --> n40
    n19 --> n24
    n31 --> n36
    n22 --> n31
    n32 --> n41
    n30 --> n37
    n21 --> n37
    n20 --> n25
    n19 --> n25
```

# r56_CAN_emergency_assembly

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n43{"r56_CAN_emergency_assembly"}
        n44{"r56_CAN_forge_our_own_future"}
        n45["r56_CAN_shadow_factories"]
        n46["r56_CAN_trust_in_the_commonwealth"]
    end
    subgraph tier_1["Tier 1"]
        n47{"r56_CAN_a_new_constitution"}
        n48{"r56_CAN_alliance_with_america"}
        n49["r56_CAN_communism"]
        n50{"r56_CAN_fascism"}
        n51{"r56_CAN_post_colonial_rule"}
        n52["r56_CAN_secure_the_economy"]
    end
    subgraph tier_2["Tier 2"]
        n53["r56_CAN_an_independent_democracy"]
        n54["r56_CAN_anti_war_policy"]
        n55["r56_CAN_canadian_union_of_fascists"]
        n56["r56_CAN_defence_scheme_no2"]
        n57["r56_CAN_development_of_new_territories"]
        n58["r56_CAN_follow_american_interventionism"]
        n59["r56_CAN_follow_american_neutrality"]
        n60["r56_CAN_install_democracy_in_the_americas"]
        n61["r56_CAN_national_social_christian_party"]
        n62["r56_CAN_our_own_way"]
        n63["r56_CAN_permanent_joint_defence_board"]
    end
    subgraph tier_3["Tier 3"]
        n64["r56_CAN_a_one_party_state"]
        n65["r56_CAN_acquire_american_ships"]
        n66["r56_CAN_arcand_in_the_government"]
        n67["r56_CAN_arrest_the_anti_fascists"]
        n68{"r56_CAN_assert_canadian_involvment"}
        n69["r56_CAN_build_navy_for_defence"]
        n70["r56_CAN_first_special_service_force"]
        n71["r56_CAN_follow_mosleys_ideas"]
        n72["r56_CAN_form_a_canadian_red_guard"]
        n73["r56_CAN_form_the_blue_shirts"]
        n74["r56_CAN_get_ready_for_intervention"]
        n75["r56_CAN_independent_industry"]
        n76["r56_CAN_modernise_the_nation"]
        n77["r56_CAN_organize_the_trade_unions"]
        n78["r56_CAN_protect_the_coast"]
        n79["r56_CAN_reduce_the_tariffs"]
        n80{"r56_CAN_seek_closer_ties_to_germany"}
        n81["r56_CAN_strict_anti_communism"]
        n82{"r56_CAN_support_the_british_union_of_fascists"}
        n83["r56_CAN_the_canadian_fuhrer"]
        n84["r56_CAN_unite_the_fascist_parties"]
        n85["r56_CAN_young_communist_league_of_canada"]
    end
    subgraph tier_4["Tier 4"]
        n86["r56_CAN_abandon_anti_war_policy"]
        n87["r56_CAN_allow_free_access"]
        n88{"r56_CAN_anti_democracy"}
        n89["r56_CAN_ask_for_newfoundland_and_labrador_democratic"]
        n90["r56_CAN_canadian_nationalism"]
        n91{"r56_CAN_create_youth_wing"}
        n92["r56_CAN_frogmen_of_burma"]
        n93["r56_CAN_independent_military"]
        n94{"r56_CAN_join_the_axis"}
        n95{"r56_CAN_join_the_british"}
        n96["r56_CAN_new_deal"]
        n97["r56_CAN_public_ownership"]
        n98["r56_CAN_quell_quebec_nationalism"]
        n99{"r56_CAN_reenforce_the_commonwealth"}
        n100["r56_CAN_restrict_immigration"]
        n101["r56_CAN_restructure_the_government"]
        n102["r56_CAN_secure_american_democracy"]
        n103["r56_CAN_self_sufficiency"]
        n104{"r56_CAN_strenght_through_conquest"}
        n105["r56_CAN_the_canadian_youth_congress"]
        n106["r56_CAN_the_mac_paps"]
        n107["r56_CAN_west_coast_military_command"]
        n108["r56_CAN_workers_rights"]
    end
    subgraph tier_5["Tier 5"]
        n109["r56_CAN_a_united_canada"]
        n110["r56_CAN_ask_for_newfoundland_and_labrador"]
        n111["r56_CAN_fascist_corporatism"]
        n112{"r56_CAN_form_our_own_alliance"}
        n113["r56_CAN_fuel_the_arms_sector"]
        n114["r56_CAN_full_equality_for_women"]
        n115["r56_CAN_liberate_the_british_isles"]
        n116["r56_CAN_our_best_friend"]
        n117["r56_CAN_plebiscite_committees"]
        n118{"r56_CAN_repeal_the_padlock_law"}
        n119["r56_CAN_secure_greenland_and_iceland"]
        n120{"r56_CAN_support_the_soviets"}
        n121["r56_CAN_unemployment_insurance_scheme"]
        n122["r56_CAN_unite_with_the_french"]
    end
    subgraph tier_6["Tier 6"]
        n123["r56_CAN_arms_exports"]
        n124["r56_CAN_contact_the_synarchists"]
        n125["r56_CAN_defence_scheme_no1"]
        n126["r56_CAN_demand_newfoundland_and_labrador"]
        n127["r56_CAN_imprison_the_trotskyists"]
        n128["r56_CAN_intervene_ACW"]
        n129["r56_CAN_join_our_british_comrades"]
        n130["r56_CAN_join_the_communist_international"]
        n131["r56_CAN_strike_the_quebecois_anti_communists"]
    end
    subgraph tier_7["Tier 7"]
        n132["r56_CAN_destroy_imperialism"]
        n133["r56_CAN_send_weapons"]
        n134["r56_CAN_take_down_america"]
    end
    subgraph tier_8["Tier 8"]
        n135["r56_CAN_strike_britain"]
        n136["r56_CAN_strike_mexico"]
    end
    subgraph tier_9["Tier 9"]
        n137["r56_CAN_strike_america"]
    end
    n43 --> n47
    n61 --> n64
    n55 --> n64
    n98 --> n109
    n72 --> n86
    n56 --> n65
    n44 --> n48
    n43 --> n48
    n79 --> n87
    n47 --> n53
    n51 --> n53
    n64 --> n88
    n49 --> n54
    n55 --> n66
    n113 --> n123
    n61 --> n67
    n95 --> n110
    n68 --> n89
    n53 --> n68
    n59 --> n69
    n64 --> n90
    n50 --> n55
    n44 --> n49
    n43 --> n49
    n112 --> n124
    n73 --> n91
    n95 --> n125
    n112 --> n125
    n94 --> n125
    n48 --> n56
    n94 --> n126
    n112 --> n126
    n130 --> n132
    n129 --> n132
    n131 --> n132
    n127 --> n132
    n52 --> n57
    n44 --> n50
    n43 --> n50
    n101 --> n111
    n63 --> n70
    n45 --> n70
    n48 --> n58
    n48 --> n59
    n55 --> n71
    n54 --> n72
    n91 --> n112
    n88 --> n112
    n104 --> n112
    n61 --> n73
    n55 --> n73
    n70 --> n92
    n45 --> n92
    n68 --> n113
    n103 --> n113
    n71 --> n114
    n101 --> n114
    n58 --> n74
    n118 --> n127
    n53 --> n75
    n76 --> n93
    n48 --> n60
    n95 --> n128
    n112 --> n128
    n94 --> n128
    n120 --> n129
    n118 --> n129
    n80 --> n94
    n82 --> n95
    n120 --> n130
    n118 --> n130
    n99 --> n115
    n53 --> n76
    n50 --> n61
    n79 --> n96
    n54 --> n77
    n99 --> n116
    n51 --> n62
    n47 --> n62
    n46 --> n63
    n48 --> n63
    n86 --> n117
    n43 --> n51
    n60 --> n78
    n77 --> n97
    n84 --> n98
    n83 --> n98
    n58 --> n79
    n59 --> n79
    n68 --> n99
    n105 --> n118
    n84 --> n100
    n83 --> n100
    n71 --> n101
    n68 --> n102
    n95 --> n119
    n43 --> n52
    n61 --> n80
    n75 --> n103
    n128 --> n133
    n64 --> n104
    n55 --> n81
    n136 --> n137
    n132 --> n135
    n132 --> n136
    n118 --> n131
    n55 --> n82
    n86 --> n120
    n125 --> n134
    n61 --> n83
    n85 --> n105
    n72 --> n106
    n108 --> n121
    n97 --> n121
    n61 --> n84
    n99 --> n122
    n79 --> n107
    n77 --> n108
    n54 --> n85
    n48 x--x n49
    n48 x--x n50
    n53 x--x n62
    n55 x--x n61
    n49 x--x n50
    n125 x--x n128
    n58 x--x n59
    n112 x--x n94
    n112 x--x n95
    n129 x--x n130
    n116 x--x n102
```

# r56_CAN_forge_our_own_future

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n43{"r56_CAN_emergency_assembly"}
        n44{"r56_CAN_forge_our_own_future"}
        n45["r56_CAN_shadow_factories"]
        n46["r56_CAN_trust_in_the_commonwealth"]
    end
    subgraph tier_1["Tier 1"]
        n48{"r56_CAN_alliance_with_america"}
        n49["r56_CAN_communism"]
        n50{"r56_CAN_fascism"}
    end
    subgraph tier_2["Tier 2"]
        n54["r56_CAN_anti_war_policy"]
        n55["r56_CAN_canadian_union_of_fascists"]
        n56["r56_CAN_defence_scheme_no2"]
        n58["r56_CAN_follow_american_interventionism"]
        n59["r56_CAN_follow_american_neutrality"]
        n60["r56_CAN_install_democracy_in_the_americas"]
        n61["r56_CAN_national_social_christian_party"]
        n63["r56_CAN_permanent_joint_defence_board"]
    end
    subgraph tier_3["Tier 3"]
        n64["r56_CAN_a_one_party_state"]
        n65["r56_CAN_acquire_american_ships"]
        n66["r56_CAN_arcand_in_the_government"]
        n67["r56_CAN_arrest_the_anti_fascists"]
        n69["r56_CAN_build_navy_for_defence"]
        n70["r56_CAN_first_special_service_force"]
        n71["r56_CAN_follow_mosleys_ideas"]
        n72["r56_CAN_form_a_canadian_red_guard"]
        n73["r56_CAN_form_the_blue_shirts"]
        n74["r56_CAN_get_ready_for_intervention"]
        n77["r56_CAN_organize_the_trade_unions"]
        n78["r56_CAN_protect_the_coast"]
        n79["r56_CAN_reduce_the_tariffs"]
        n80{"r56_CAN_seek_closer_ties_to_germany"}
        n81["r56_CAN_strict_anti_communism"]
        n82{"r56_CAN_support_the_british_union_of_fascists"}
        n83["r56_CAN_the_canadian_fuhrer"]
        n84["r56_CAN_unite_the_fascist_parties"]
        n85["r56_CAN_young_communist_league_of_canada"]
    end
    subgraph tier_4["Tier 4"]
        n86["r56_CAN_abandon_anti_war_policy"]
        n87["r56_CAN_allow_free_access"]
        n88{"r56_CAN_anti_democracy"}
        n90["r56_CAN_canadian_nationalism"]
        n91{"r56_CAN_create_youth_wing"}
        n92["r56_CAN_frogmen_of_burma"]
        n94{"r56_CAN_join_the_axis"}
        n95{"r56_CAN_join_the_british"}
        n96["r56_CAN_new_deal"]
        n97["r56_CAN_public_ownership"]
        n98["r56_CAN_quell_quebec_nationalism"]
        n100["r56_CAN_restrict_immigration"]
        n101["r56_CAN_restructure_the_government"]
        n104{"r56_CAN_strenght_through_conquest"}
        n105["r56_CAN_the_canadian_youth_congress"]
        n106["r56_CAN_the_mac_paps"]
        n107["r56_CAN_west_coast_military_command"]
        n108["r56_CAN_workers_rights"]
    end
    subgraph tier_5["Tier 5"]
        n109["r56_CAN_a_united_canada"]
        n110["r56_CAN_ask_for_newfoundland_and_labrador"]
        n111["r56_CAN_fascist_corporatism"]
        n112{"r56_CAN_form_our_own_alliance"}
        n114["r56_CAN_full_equality_for_women"]
        n117["r56_CAN_plebiscite_committees"]
        n118{"r56_CAN_repeal_the_padlock_law"}
        n119["r56_CAN_secure_greenland_and_iceland"]
        n120{"r56_CAN_support_the_soviets"}
        n121["r56_CAN_unemployment_insurance_scheme"]
    end
    subgraph tier_6["Tier 6"]
        n124["r56_CAN_contact_the_synarchists"]
        n125["r56_CAN_defence_scheme_no1"]
        n126["r56_CAN_demand_newfoundland_and_labrador"]
        n127["r56_CAN_imprison_the_trotskyists"]
        n128["r56_CAN_intervene_ACW"]
        n129["r56_CAN_join_our_british_comrades"]
        n130["r56_CAN_join_the_communist_international"]
        n131["r56_CAN_strike_the_quebecois_anti_communists"]
    end
    subgraph tier_7["Tier 7"]
        n132["r56_CAN_destroy_imperialism"]
        n133["r56_CAN_send_weapons"]
        n134["r56_CAN_take_down_america"]
    end
    subgraph tier_8["Tier 8"]
        n135["r56_CAN_strike_britain"]
        n136["r56_CAN_strike_mexico"]
    end
    subgraph tier_9["Tier 9"]
        n137["r56_CAN_strike_america"]
    end
    n61 --> n64
    n55 --> n64
    n98 --> n109
    n72 --> n86
    n56 --> n65
    n44 --> n48
    n43 --> n48
    n79 --> n87
    n64 --> n88
    n49 --> n54
    n55 --> n66
    n61 --> n67
    n95 --> n110
    n59 --> n69
    n64 --> n90
    n50 --> n55
    n44 --> n49
    n43 --> n49
    n112 --> n124
    n73 --> n91
    n95 --> n125
    n112 --> n125
    n94 --> n125
    n48 --> n56
    n94 --> n126
    n112 --> n126
    n130 --> n132
    n129 --> n132
    n131 --> n132
    n127 --> n132
    n44 --> n50
    n43 --> n50
    n101 --> n111
    n63 --> n70
    n45 --> n70
    n48 --> n58
    n48 --> n59
    n55 --> n71
    n54 --> n72
    n91 --> n112
    n88 --> n112
    n104 --> n112
    n61 --> n73
    n55 --> n73
    n70 --> n92
    n45 --> n92
    n71 --> n114
    n101 --> n114
    n58 --> n74
    n118 --> n127
    n48 --> n60
    n95 --> n128
    n112 --> n128
    n94 --> n128
    n120 --> n129
    n118 --> n129
    n80 --> n94
    n82 --> n95
    n120 --> n130
    n118 --> n130
    n50 --> n61
    n79 --> n96
    n54 --> n77
    n46 --> n63
    n48 --> n63
    n86 --> n117
    n60 --> n78
    n77 --> n97
    n84 --> n98
    n83 --> n98
    n58 --> n79
    n59 --> n79
    n105 --> n118
    n84 --> n100
    n83 --> n100
    n71 --> n101
    n95 --> n119
    n61 --> n80
    n128 --> n133
    n64 --> n104
    n55 --> n81
    n136 --> n137
    n132 --> n135
    n132 --> n136
    n118 --> n131
    n55 --> n82
    n86 --> n120
    n125 --> n134
    n61 --> n83
    n85 --> n105
    n72 --> n106
    n108 --> n121
    n97 --> n121
    n61 --> n84
    n79 --> n107
    n77 --> n108
    n54 --> n85
    n48 x--x n49
    n48 x--x n50
    n55 x--x n61
    n49 x--x n50
    n125 x--x n128
    n58 x--x n59
    n44 x--x n46
    n112 x--x n94
    n112 x--x n95
    n129 x--x n130
```

# r56_CAN_modernize_industry

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19["r56_CAN_depression_recovery"]
        n20(("r56_CAN_modernize_industry"))
        n23["r56_CAN_national_housing_act"]
        n21["r56_CAN_replace_men_in_the_industry"]
        n24["r56_CAN_shutdown_relief_camps"]
    end
    subgraph tier_1["Tier 1"]
        n22["r56_CAN_dollar_a_year_men"]
        n25["r56_CAN_wheat_board"]
    end
    subgraph tier_2["Tier 2"]
        n26["r56_CAN_bank_of_canada"]
        n27["r56_CAN_canadian_pacific_railways"]
        n28["r56_CAN_cbc_focus"]
        n29["r56_CAN_debt_adjustment_act"]
        n30["r56_CAN_enlist_the_unemployed"]
        n31["r56_CAN_sorel_steel_and_foundry"]
    end
    subgraph tier_3["Tier 3"]
        n32["r56_CAN_alcan"]
        n33["r56_CAN_john_inglis_company"]
        n34["r56_CAN_national_railway"]
        n35["r56_CAN_national_steel_car"]
        n36["r56_CAN_sorel_industries"]
        n37["r56_CAN_war_economy"]
    end
    subgraph tier_4["Tier 4"]
        n38["r56_CAN_imperial_oil_focus"]
        n39["r56_CAN_research_grants"]
        n40["r56_CAN_resources_for_war_effort"]
        n41["r56_CAN_uranium_mining"]
    end
    subgraph tier_5["Tier 5"]
        n42["r56_CAN_establish_the_polymer_corporation"]
    end
    n26 --> n32
    n22 --> n26
    n22 --> n27
    n22 --> n28
    n23 --> n29
    n25 --> n29
    n19 --> n22
    n20 --> n22
    n23 --> n30
    n25 --> n30
    n24 --> n30
    n38 --> n42
    n32 --> n38
    n27 --> n33
    n26 --> n34
    n27 --> n35
    n33 --> n39
    n34 --> n39
    n32 --> n40
    n37 --> n40
    n31 --> n36
    n22 --> n31
    n32 --> n41
    n30 --> n37
    n21 --> n37
    n20 --> n25
    n19 --> n25
```

# r56_CAN_rebuilding_the_royal_canadian_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n138(("r56_CAN_rebuilding_the_royal_canadian_navy"))
    end
    subgraph tier_1["Tier 1"]
        n139["r56_CAN_focus_on_destroyers"]
        n140["r56_CAN_halifax_shipyards"]
    end
    subgraph tier_2["Tier 2"]
        n141["r56_CAN_expand_the_navy"]
        n142["r56_CAN_protect_atlantic_shipping"]
        n143["r56_CAN_sorel_shipyards"]
    end
    subgraph tier_3["Tier 3"]
        n144["r56_CAN_fight_the_uboats"]
        n145["r56_CAN_merchant_fleet"]
        n146["r56_CAN_reopen_toronto_shipyards"]
        n147["r56_CAN_sorel_industries_naval_artillery"]
        n148["r56_CAN_the_pacific_ocean"]
        n149["r56_CAN_wrens"]
    end
    subgraph tier_4["Tier 4"]
        n150["r56_CAN_degaussing"]
        n151["r56_CAN_invasion_transports"]
        n152["r56_CAN_rural_class_carriers"]
        n153["r56_CAN_ships_for_the_pacific"]
        n154["r56_CAN_sorel_naval_steel"]
    end
    subgraph tier_5["Tier 5"]
        n155["CAN_pykrete_carrier"]
    end
    n154 --> n155
    n144 --> n150
    n140 --> n141
    n139 --> n141
    n142 --> n144
    n138 --> n139
    n138 --> n140
    n148 --> n151
    n142 --> n145
    n139 --> n142
    n143 --> n146
    n148 --> n152
    n148 --> n153
    n143 --> n147
    n147 --> n154
    n140 --> n143
    n141 --> n148
    n141 --> n149
    n139 --> n149
```

# r56_CAN_start_the_expansion_of_the_rcaf

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n156(("r56_CAN_start_the_expansion_of_the_rcaf"))
    end
    subgraph tier_1["Tier 1"]
        n157["r56_CAN_appoint_air_chief"]
        n158["r56_CAN_eastern_air_command"]
        n159["r56_CAN_toronto_island_airport"]
        n160["r56_CAN_western_air_command"]
    end
    subgraph tier_2["Tier 2"]
        n161["r56_CAN_complete_separation_from_army"]
        n162["r56_CAN_hurricane"]
        n163["r56_CAN_rcaf_womens_division"]
        n164["r56_CAN_toronto_air_command"]
    end
    subgraph tier_3["Tier 3"]
        n165["r56_CAN_canadian_car_and_foundry"]
        n166["r56_CAN_rcaf_station_borden"]
    end
    subgraph tier_4["Tier 4"]
        n167["r56_CAN_fairchild_aircraft_company"]
        n168["r56_CAN_victory_aircraft_company"]
    end
    subgraph tier_5["Tier 5"]
        n169["r56_CAN_bomber_group_no_6"]
    end
    n156 --> n157
    n167 --> n169
    n168 --> n169
    n162 --> n165
    n157 --> n161
    n156 --> n158
    n165 --> n167
    n166 --> n167
    n160 --> n162
    n158 --> n162
    n163 --> n166
    n164 --> n166
    n160 --> n163
    n158 --> n163
    n159 --> n164
    n156 --> n159
    n165 --> n168
    n166 --> n168
    n156 --> n160
```

# r56_CAN_strengthen_british_ties

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n170(("r56_CAN_strengthen_british_ties"))
        n171["r56_CAN_tizard_visit"]
        n46["r56_CAN_trust_in_the_commonwealth"]
    end
    subgraph tier_1["Tier 1"]
        n172["r56_CAN_british_ships"]
        n173["r56_CAN_commonwealth_air_training_plan"]
        n174["r56_CAN_governor_general_in_power"]
    end
    subgraph tier_2["Tier 2"]
        n175["r56_CAN_build_fighters_for_the_empire"]
        n176["r56_CAN_construct_the_cape_spear_forts"]
        n177["r56_CAN_empower_the_military_faction"]
        n178["r56_CAN_root_out_traitors"]
    end
    subgraph tier_3["Tier 3"]
        n179["r56_CAN_CAMP_X"]
        n180["r56_CAN_god_save_the_king"]
        n181["r56_CAN_integrate_the_canadian_cadet_corps"]
    end
    subgraph tier_4["Tier 4"]
        n182["r56_CAN_ask_for_newfoundland_and_labrador_gg"]
        n183["r56_CAN_hydra"]
        n184["r56_CAN_the_defense_of_canada"]
    end
    subgraph tier_5["Tier 5"]
        n185["r56_CAN_claims_on_america"]
        n186["r56_CAN_defence_scheme_no1_gg"]
        n187["r56_CAN_national_defense_funding"]
    end
    n176 --> n179
    n171 --> n179
    n180 --> n182
    n170 --> n172
    n173 --> n175
    n184 --> n185
    n46 --> n173
    n170 --> n173
    n172 --> n176
    n173 --> n176
    n184 --> n186
    n174 --> n177
    n177 --> n180
    n178 --> n180
    n170 --> n174
    n179 --> n183
    n177 --> n181
    n184 --> n187
    n174 --> n178
    n180 --> n184
```

# r56_CAN_suppress_the_separatists

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n188(("r56_CAN_suppress_the_separatists"))
    end
```

# r56_CAN_trust_in_the_commonwealth

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n48["r56_CAN_alliance_with_america"]
        n172["r56_CAN_british_ships"]
        n44["r56_CAN_forge_our_own_future"]
        n170["r56_CAN_strengthen_british_ties"]
        n46(("r56_CAN_trust_in_the_commonwealth"))
    end
    subgraph tier_1["Tier 1"]
        n173["r56_CAN_commonwealth_air_training_plan"]
        n63["r56_CAN_permanent_joint_defence_board"]
        n45["r56_CAN_shadow_factories"]
    end
    subgraph tier_2["Tier 2"]
        n175["r56_CAN_build_fighters_for_the_empire"]
        n176["r56_CAN_construct_the_cape_spear_forts"]
        n70["r56_CAN_first_special_service_force"]
        n189["r56_CAN_montreal_laboratory"]
        n171["r56_CAN_tizard_visit"]
    end
    subgraph tier_3["Tier 3"]
        n179["r56_CAN_CAMP_X"]
        n92["r56_CAN_frogmen_of_burma"]
    end
    subgraph tier_4["Tier 4"]
        n183["r56_CAN_hydra"]
    end
    n176 --> n179
    n171 --> n179
    n173 --> n175
    n46 --> n173
    n170 --> n173
    n172 --> n176
    n173 --> n176
    n63 --> n70
    n45 --> n70
    n70 --> n92
    n45 --> n92
    n179 --> n183
    n45 --> n189
    n46 --> n63
    n48 --> n63
    n46 --> n45
    n45 --> n171
    n44 x--x n46
```

# r56_CAN_war_measures_act

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n32["r56_CAN_alcan"]
        n30["r56_CAN_enlist_the_unemployed"]
        n190(("r56_CAN_war_measures_act"))
    end
    subgraph tier_1["Tier 1"]
        n191["r56_CAN_defence_of_canada_regulations"]
        n192["r56_CAN_nrma"]
        n193["r56_CAN_wartime_prices_and_trade_board"]
    end
    subgraph tier_2["Tier 2"]
        n194["r56_CAN_conscription_crisis"]
        n195["r56_CAN_department_of_munitions_and_supply"]
        n21["r56_CAN_replace_men_in_the_industry"]
    end
    subgraph tier_3["Tier 3"]
        n196["r56_CAN_bits_and_pieces_program"]
        n37["r56_CAN_war_economy"]
    end
    subgraph tier_4["Tier 4"]
        n197["r56_CAN_nrc_expansion"]
        n40["r56_CAN_resources_for_war_effort"]
    end
    n195 --> n196
    n193 --> n194
    n190 --> n191
    n192 --> n195
    n193 --> n195
    n196 --> n197
    n21 --> n197
    n190 --> n192
    n193 --> n21
    n32 --> n40
    n37 --> n40
    n30 --> n37
    n21 --> n37
    n190 --> n193
```
