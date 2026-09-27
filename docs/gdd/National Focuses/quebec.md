# QUE_fund_an_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("QUE_fund_an_air_force"))
        n2["QUE_locomotive_industry"]
        n3["QUE_organize_the_militias"]
        n4["QUE_rearmement_agreement"]
        n5["QUE_sorel_industries"]
        n6["QUE_sorel_steel_and_foundry"]
        n7["QUE_the_quebecois_economy"]
    end
    subgraph tier_1["Tier 1"]
        n8{"QUE_airfield_construction"}
        n9["QUE_quebec_arsenal"]
        n10["QUE_radar_development"]
    end
    subgraph tier_2["Tier 2"]
        n11{"QUE_bomber_development"}
        n12{"QUE_fighter_development"}
        n13["QUE_forest_training"]
        n14["QUE_protect_our_skies"]
        n15["QUE_small_arms_production"]
    end
    subgraph tier_3["Tier 3"]
        n16["QUE_artillery_improvements"]
        n17["QUE_focus_on_anti_air"]
        n18["QUE_ground_support_focus"]
        n19["QUE_modernized_support_equipment"]
        n20["QUE_naval_support_focus"]
        n21["QUE_winter_equipment"]
    end
    subgraph tier_4["Tier 4"]
        n22["QUE_bombardier_vehicles"]
        n23["QUE_expand_the_doctrines"]
        n24["QUE_jet_research"]
        n25["QUE_quebecois_officer_corps"]
        n26["QUE_rocket_research"]
        n27["QUE_tank_program"]
    end
    subgraph tier_5["Tier 5"]
        n28["QUE_angus_shop_tank_production"]
        n29["QUE_expand_bombardier_factories"]
        n30["QUE_military_industrial_cooperation"]
    end
    subgraph tier_6["Tier 6"]
        n31["QUE_develop_the_capitale_nationale"]
        n32["QUE_nuclear_research"]
    end
    subgraph tier_7["Tier 7"]
        n33["QUE_cote_nord_expansion"]
        n34["QUE_develop_northern_economy"]
        n35["QUE_mauricie_development"]
        n36["QUE_saguenay_industries"]
        n37["QUE_southern_development_initiative"]
    end
    n1 --> n8
    n25 --> n28
    n15 --> n16
    n2 --> n22
    n19 --> n22
    n8 --> n11
    n31 --> n33
    n31 --> n34
    n7 --> n31
    n29 --> n31
    n22 --> n29
    n2 --> n29
    n20 --> n23
    n18 --> n23
    n8 --> n12
    n14 --> n17
    n9 --> n13
    n4 --> n13
    n12 --> n18
    n11 --> n18
    n20 --> n24
    n18 --> n24
    n31 --> n35
    n25 --> n30
    n15 --> n19
    n5 --> n19
    n12 --> n20
    n11 --> n20
    n30 --> n32
    n8 --> n14
    n3 --> n9
    n1 --> n9
    n16 --> n25
    n19 --> n25
    n1 --> n10
    n20 --> n26
    n18 --> n26
    n17 --> n26
    n31 --> n36
    n9 --> n15
    n6 --> n15
    n4 --> n15
    n31 --> n37
    n19 --> n27
    n16 --> n27
    n13 --> n21
    n11 x--x n12
    n18 x--x n20
```

# QUE_marine_industries

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n38(("QUE_marine_industries"))
    end
    subgraph tier_1["Tier 1"]
        n39["QUE_merchant_marine"]
        n40["QUE_national_admiralty"]
        n41["QUE_naval_grade_steel"]
        n42["QUE_shipbuilding_contacts"]
    end
    subgraph tier_2["Tier 2"]
        n43["QUE_cruiser_focus"]
        n44["QUE_destroyer_focus"]
        n45["QUE_expand_the_port_of_quebec"]
        n46["QUE_form_national_harbour_board"]
    end
    subgraph tier_3["Tier 3"]
        n47["QUE_a_s_warfare"]
        n48["QUE_form_marine_corps"]
        n49["QUE_fortify_the_ports"]
        n50["QUE_increase_naval_production"]
        n51["QUE_naval_artillery"]
        n52["QUE_naval_mine_warfare"]
    end
    n44 --> n47
    n43 --> n47
    n42 --> n43
    n40 --> n43
    n42 --> n44
    n40 --> n44
    n39 --> n45
    n46 --> n48
    n45 --> n48
    n39 --> n46
    n46 --> n49
    n45 --> n49
    n44 --> n50
    n43 --> n50
    n38 --> n39
    n38 --> n40
    n41 --> n51
    n43 --> n51
    n38 --> n41
    n43 --> n52
    n44 --> n52
    n38 --> n42
```

# QUE_organize_the_militias

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["QUE_fund_an_air_force"]
        n2["QUE_locomotive_industry"]
        n3(("QUE_organize_the_militias"))
        n5["QUE_sorel_industries"]
        n6["QUE_sorel_steel_and_foundry"]
        n7["QUE_the_quebecois_economy"]
    end
    subgraph tier_1["Tier 1"]
        n9["QUE_quebec_arsenal"]
        n4["QUE_rearmement_agreement"]
    end
    subgraph tier_2["Tier 2"]
        n53["QUE_a_standing_army"]
        n13["QUE_forest_training"]
        n15["QUE_small_arms_production"]
    end
    subgraph tier_3["Tier 3"]
        n16["QUE_artillery_improvements"]
        n54["QUE_land_doctrine_reform"]
        n19["QUE_modernized_support_equipment"]
        n21["QUE_winter_equipment"]
    end
    subgraph tier_4["Tier 4"]
        n22["QUE_bombardier_vehicles"]
        n25["QUE_quebecois_officer_corps"]
        n27["QUE_tank_program"]
    end
    subgraph tier_5["Tier 5"]
        n28["QUE_angus_shop_tank_production"]
        n29["QUE_expand_bombardier_factories"]
        n30["QUE_military_industrial_cooperation"]
    end
    subgraph tier_6["Tier 6"]
        n31["QUE_develop_the_capitale_nationale"]
        n32["QUE_nuclear_research"]
    end
    subgraph tier_7["Tier 7"]
        n33["QUE_cote_nord_expansion"]
        n34["QUE_develop_northern_economy"]
        n35["QUE_mauricie_development"]
        n36["QUE_saguenay_industries"]
        n37["QUE_southern_development_initiative"]
    end
    n4 --> n53
    n25 --> n28
    n15 --> n16
    n2 --> n22
    n19 --> n22
    n31 --> n33
    n31 --> n34
    n7 --> n31
    n29 --> n31
    n22 --> n29
    n2 --> n29
    n9 --> n13
    n4 --> n13
    n53 --> n54
    n31 --> n35
    n25 --> n30
    n15 --> n19
    n5 --> n19
    n30 --> n32
    n3 --> n9
    n1 --> n9
    n16 --> n25
    n19 --> n25
    n3 --> n4
    n31 --> n36
    n9 --> n15
    n6 --> n15
    n4 --> n15
    n31 --> n37
    n19 --> n27
    n16 --> n27
    n13 --> n21
```

# QUE_political_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n55{"QUE_political_effort"}
        n56{"QUE_political_effort_puppet"}
    end
    subgraph tier_1["Tier 1"]
        n57{"QUE_radical_changes"}
        n58{"QUE_trust_in_democracy"}
    end
    subgraph tier_2["Tier 2"]
        n59["QUE_collectivism"]
        n60{"QUE_liberal_in_charge"}
        n61["QUE_political_nationalism"]
        n62{"QUE_the_union_nationale_wins"}
    end
    subgraph tier_3["Tier 3"]
        n63["QUE_communist_uprising"]
        n64["QUE_enforce_religious_morality"]
        n65{"QUE_found_the_conseil_superieur_du_travail"}
        n66["QUE_mandatory_minimum_wage"]
        n67["QUE_reform_the_party"]
        n68["QUE_storm_the_parliament"]
        n69["QUE_the_padlock_law"]
    end
    subgraph tier_4["Tier 4"]
        n70["QUE_advatageous_foreign_trade_deal"]
        n71["QUE_all_power_to_the_leader"]
        n72["QUE_bust_down_the_unions"]
        n73["QUE_collectivize_the_means_of_production"]
        n74["QUE_improve_agrarian_laws"]
        n75["QUE_labor_laws"]
        n76["QUE_promote_interventionism"]
        n77["QUE_remove_the_aristocracy"]
        n78["QUE_use_the_quebecois_nationalists"]
    end
    subgraph tier_5["Tier 5"]
        n79["QUE_contact_blueshirts"]
        n80["QUE_control_the_medias"]
        n81["QUE_deal_with_opposition"]
        n82["QUE_enforce_compulsory_education"]
        n83["QUE_enforce_local_ressource_exploitation"]
        n84["QUE_found_hydro_quebec"]
        n85["QUE_national_identity_propaganda"]
        n86{"QUE_revolutionary_patriotism"}
        n87["QUE_seize_the_royal_assets"]
    end
    subgraph tier_6["Tier 6"]
        n88{"QUE_colonize_the_north"}
        n89{"QUE_communial_defense"}
        n90["QUE_disband_parlimentarism"]
        n91{"QUE_exploit_hydroelectricity"}
        n92["QUE_focus_on_family"]
        n93["QUE_patriotic_education"]
        n94{"QUE_redistribute_the_church_wealth"}
        n95{"QUE_the_quebec_red_army"}
        n96["QUE_universal_suffrage"]
    end
    subgraph tier_7["Tier 7"]
        n97["QUE_abandon_electorialism"]
        n98["QUE_align_with_moscow"]
        n99["QUE_carry_on_the_work"]
        n100["QUE_first_nationalist_congress"]
        n101["QUE_liberals_legacy_saved"]
        n102["QUE_total_self_sufficiency"]
    end
    subgraph tier_8["Tier 8"]
        n103["QUE_abandon_ultramontanism"]
        n104["QUE_consolidate_le_chefs_rule"]
        n105["QUE_encourage_local_participation"]
        n106["QUE_encourage_traditionalist_economics"]
        n107{"QUE_establish_farmers_coops"}
        n108{"QUE_forced_industrialisation"}
        n109["QUE_glorify_clerical_past"]
        n110["QUE_incorporate_hydroquebec_in_the_state"]
        n111["QUE_institute_social_welfare"]
        n112["QUE_promote_french_language"]
        n113["QUE_safeguard_the_rights_to_unionize"]
        n114["QUE_soviet_tank_program"]
    end
    subgraph tier_9["Tier 9"]
        n115["QUE_councilism"]
        n116["QUE_electrify_the_countryside"]
        n117["QUE_enforce_quotas"]
        n118["QUE_for_the_good_of_the_nation"]
        n119["QUE_further_funding_to_culture"]
        n120["QUE_limit_economic_government_interference"]
        n121["QUE_maitres_chez_nous"]
        n122["QUE_provide_to_the_people"]
        n123["QUE_purge_the_anglophone"]
        n124["QUE_secret_police"]
        n125["QUE_spy_the_opposition"]
        n126["QUE_united_in_communism"]
        n127["QUE_vilify_federalists"]
    end
    subgraph tier_10["Tier 10"]
        n128["QUE_aggressive_economic_protectionism"]
        n129["QUE_cement_catholic_faith"]
        n130["QUE_corporatisme_ensuite"]
        n131["QUE_educate_the_masses"]
        n132{"QUE_enshrine_women_rights"}
        n133["QUE_give_power_to_the_clergy"]
        n134["QUE_let_the_church_control_education_and_healthcare"]
        n135["QUE_politique_dabord"]
        n136["QUE_quebecois_peoples_republic"]
        n137["QUE_toward_utopian_socialism"]
    end
    subgraph tier_11["Tier 11"]
        n138["QUE_a_bright_future_ahead"]
        n139{"QUE_christian_social_security"}
        n140["QUE_control_literature"]
        n141["QUE_national_free_market"]
        n142["QUE_nationalize_key_industries"]
        n143["QUE_purge_clerical_elements"]
        n144["QUE_state_led_labor_unions"]
        n145{"QUE_subsidies_to_corporations"}
        n146["QUE_weaponize_mysticism"]
    end
    subgraph tier_12["Tier 12"]
        n147["QUE_advantage_francophones"]
        n148["QUE_demand_new_brunswick"]
        n149["QUE_democratic_diplomacy"]
        n150["QUE_diplomatic_neutrality"]
        n151["QUE_encourage_christian_mutualism"]
        n152["QUE_everything_for_the_state"]
        n153["QUE_militaristic_society"]
        n154["QUE_order_authority_nation"]
        n155["QUE_seize_opponents_assets"]
        n156["QUE_shatter_the_dream"]
    end
    subgraph tier_13["Tier 13"]
        n157{"QUE_aspirations_of_new_france"}
        n158["QUE_demand_newfoundlands"]
        n159{"QUE_expansionism"}
        n160["QUE_free_the_canadian_workers"]
        n161["QUE_integrate_new_england"]
        n162["QUE_wartime_rationing"]
    end
    subgraph tier_14["Tier 14"]
        n163["QUE_align_with_mexico"]
        n164["QUE_approach_berlin"]
        n165["QUE_approach_paris"]
        n166["QUE_approach_rome"]
        n167["QUE_demand_newfoundlands_fascism"]
        n168["QUE_greater_quebec_concept"]
        n169["QUE_our_own_way"]
    end
    subgraph tier_15["Tier 15"]
        n170["QUE_claim_new_bruinswick"]
        n171["QUE_invade_canada"]
    end
    subgraph tier_16["Tier 16"]
        n172["QUE_expand_into_america"]
        n173["QUE_proclaim_french_canada"]
        n174["QUE_push_westward"]
    end
    subgraph tier_17["Tier 17"]
        n175["QUE_consolidate_american_holdings"]
        n176["QUE_establish_republican_canada"]
        n177["QUE_prepare_the_southern_front"]
        n178["QUE_subjugate_mexico"]
    end
    subgraph tier_18["Tier 18"]
        n179["QUE_fight_against_the_ideological_enemy"]
        n180["QUE_reclaim_southern_land"]
    end
    subgraph tier_19["Tier 19"]
        n181["QUE_proclaim_new_france"]
    end
    subgraph tier_20["Tier 20"]
        n182["QUE_avenge_the_seven_year_war"]
        n183["QUE_reclaim_france"]
    end
    n137 --> n138
    n136 --> n138
    n88 --> n97
    n100 --> n103
    n146 --> n147
    n140 --> n147
    n69 --> n70
    n121 --> n128
    n157 --> n163
    n91 --> n98
    n95 --> n98
    n89 --> n98
    n94 --> n98
    n68 --> n71
    n159 --> n164
    n157 --> n165
    n159 --> n166
    n147 --> n157
    n151 --> n157
    n181 --> n182
    n69 --> n72
    n88 --> n99
    n121 --> n129
    n133 --> n139
    n134 --> n139
    n169 --> n170
    n165 --> n170
    n163 --> n170
    n57 --> n59
    n63 --> n73
    n70 --> n88
    n80 --> n88
    n72 --> n88
    n86 --> n89
    n59 --> n63
    n172 --> n175
    n97 --> n104
    n76 --> n79
    n71 --> n79
    n129 --> n140
    n69 --> n80
    n78 --> n80
    n127 --> n130
    n105 --> n115
    n71 --> n81
    n138 --> n148
    n138 --> n158
    n149 --> n158
    n159 --> n167
    n157 --> n167
    n145 --> n149
    n139 --> n149
    n132 --> n149
    n139 --> n150
    n145 --> n150
    n132 --> n150
    n81 --> n90
    n126 --> n131
    n123 --> n131
    n112 --> n116
    n141 --> n151
    n102 --> n105
    n97 --> n106
    n67 --> n82
    n74 --> n82
    n73 --> n83
    n114 --> n117
    n62 --> n64
    n110 --> n132
    n119 --> n132
    n102 --> n107
    n174 --> n176
    n142 --> n152
    n144 --> n152
    n171 --> n172
    n153 --> n159
    n154 --> n159
    n152 --> n159
    n83 --> n91
    n175 --> n179
    n178 --> n179
    n92 --> n100
    n93 --> n100
    n90 --> n100
    n85 --> n92
    n106 --> n118
    n98 --> n108
    n75 --> n84
    n69 --> n84
    n60 --> n65
    n148 --> n160
    n113 --> n119
    n111 --> n119
    n118 --> n133
    n125 --> n133
    n100 --> n109
    n160 --> n168
    n65 --> n74
    n101 --> n110
    n101 --> n111
    n156 --> n161
    n169 --> n171
    n164 --> n171
    n166 --> n171
    n65 --> n75
    n116 --> n134
    n120 --> n134
    n58 --> n60
    n96 --> n101
    n112 --> n120
    n109 --> n121
    n62 --> n66
    n143 --> n153
    n128 --> n141
    n76 --> n85
    n130 --> n142
    n143 --> n154
    n159 --> n169
    n157 --> n169
    n85 --> n93
    n57 --> n61
    n127 --> n135
    n174 --> n177
    n171 --> n173
    n180 --> n181
    n99 --> n112
    n68 --> n76
    n105 --> n122
    n135 --> n143
    n107 --> n123
    n108 --> n123
    n170 --> n174
    n124 --> n136
    n117 --> n136
    n55 --> n57
    n56 --> n57
    n181 --> n183
    n177 --> n180
    n176 --> n180
    n87 --> n94
    n60 --> n67
    n63 --> n77
    n77 --> n86
    n101 --> n113
    n114 --> n124
    n142 --> n155
    n141 --> n155
    n73 --> n87
    n138 --> n156
    n98 --> n114
    n104 --> n125
    n130 --> n144
    n61 --> n68
    n172 --> n178
    n133 --> n145
    n134 --> n145
    n60 --> n69
    n62 --> n69
    n86 --> n95
    n58 --> n62
    n91 --> n102
    n95 --> n102
    n89 --> n102
    n94 --> n102
    n115 --> n137
    n122 --> n137
    n55 --> n58
    n56 --> n58
    n107 --> n126
    n108 --> n126
    n84 --> n96
    n72 --> n96
    n82 --> n96
    n64 --> n78
    n66 --> n78
    n103 --> n127
    n155 --> n162
    n129 --> n146
    n97 x--x n99
    n163 x--x n164
    n163 x--x n165
    n163 x--x n166
    n163 x--x n169
    n98 x--x n102
    n164 x--x n165
    n164 x--x n166
    n164 x--x n169
    n165 x--x n166
    n165 x--x n169
    n166 x--x n169
    n59 x--x n61
    n89 x--x n95
    n149 x--x n150
    n75 x--x n69
    n60 x--x n62
    n55 x--x n56
    n123 x--x n126
    n57 x--x n58
```

# QUE_political_effort_puppet

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n55{"QUE_political_effort"}
        n56{"QUE_political_effort_puppet"}
    end
    subgraph tier_1["Tier 1"]
        n57{"QUE_radical_changes"}
        n58{"QUE_trust_in_democracy"}
    end
    subgraph tier_2["Tier 2"]
        n59["QUE_collectivism"]
        n60{"QUE_liberal_in_charge"}
        n61["QUE_political_nationalism"]
        n62{"QUE_the_union_nationale_wins"}
    end
    subgraph tier_3["Tier 3"]
        n63["QUE_communist_uprising"]
        n64["QUE_enforce_religious_morality"]
        n65{"QUE_found_the_conseil_superieur_du_travail"}
        n66["QUE_mandatory_minimum_wage"]
        n67["QUE_reform_the_party"]
        n68["QUE_storm_the_parliament"]
        n69["QUE_the_padlock_law"]
    end
    subgraph tier_4["Tier 4"]
        n70["QUE_advatageous_foreign_trade_deal"]
        n71["QUE_all_power_to_the_leader"]
        n72["QUE_bust_down_the_unions"]
        n73["QUE_collectivize_the_means_of_production"]
        n74["QUE_improve_agrarian_laws"]
        n75["QUE_labor_laws"]
        n76["QUE_promote_interventionism"]
        n77["QUE_remove_the_aristocracy"]
        n78["QUE_use_the_quebecois_nationalists"]
    end
    subgraph tier_5["Tier 5"]
        n79["QUE_contact_blueshirts"]
        n80["QUE_control_the_medias"]
        n81["QUE_deal_with_opposition"]
        n82["QUE_enforce_compulsory_education"]
        n83["QUE_enforce_local_ressource_exploitation"]
        n84["QUE_found_hydro_quebec"]
        n85["QUE_national_identity_propaganda"]
        n86{"QUE_revolutionary_patriotism"}
        n87["QUE_seize_the_royal_assets"]
    end
    subgraph tier_6["Tier 6"]
        n88{"QUE_colonize_the_north"}
        n89{"QUE_communial_defense"}
        n90["QUE_disband_parlimentarism"]
        n91{"QUE_exploit_hydroelectricity"}
        n92["QUE_focus_on_family"]
        n93["QUE_patriotic_education"]
        n94{"QUE_redistribute_the_church_wealth"}
        n95{"QUE_the_quebec_red_army"}
        n96["QUE_universal_suffrage"]
    end
    subgraph tier_7["Tier 7"]
        n97["QUE_abandon_electorialism"]
        n98["QUE_align_with_moscow"]
        n99["QUE_carry_on_the_work"]
        n100["QUE_first_nationalist_congress"]
        n101["QUE_liberals_legacy_saved"]
        n102["QUE_total_self_sufficiency"]
    end
    subgraph tier_8["Tier 8"]
        n103["QUE_abandon_ultramontanism"]
        n104["QUE_consolidate_le_chefs_rule"]
        n105["QUE_encourage_local_participation"]
        n106["QUE_encourage_traditionalist_economics"]
        n107{"QUE_establish_farmers_coops"}
        n108{"QUE_forced_industrialisation"}
        n109["QUE_glorify_clerical_past"]
        n110["QUE_incorporate_hydroquebec_in_the_state"]
        n111["QUE_institute_social_welfare"]
        n112["QUE_promote_french_language"]
        n113["QUE_safeguard_the_rights_to_unionize"]
        n114["QUE_soviet_tank_program"]
    end
    subgraph tier_9["Tier 9"]
        n115["QUE_councilism"]
        n116["QUE_electrify_the_countryside"]
        n117["QUE_enforce_quotas"]
        n118["QUE_for_the_good_of_the_nation"]
        n119["QUE_further_funding_to_culture"]
        n120["QUE_limit_economic_government_interference"]
        n121["QUE_maitres_chez_nous"]
        n122["QUE_provide_to_the_people"]
        n123["QUE_purge_the_anglophone"]
        n124["QUE_secret_police"]
        n125["QUE_spy_the_opposition"]
        n126["QUE_united_in_communism"]
        n127["QUE_vilify_federalists"]
    end
    subgraph tier_10["Tier 10"]
        n128["QUE_aggressive_economic_protectionism"]
        n129["QUE_cement_catholic_faith"]
        n130["QUE_corporatisme_ensuite"]
        n131["QUE_educate_the_masses"]
        n132{"QUE_enshrine_women_rights"}
        n133["QUE_give_power_to_the_clergy"]
        n134["QUE_let_the_church_control_education_and_healthcare"]
        n135["QUE_politique_dabord"]
        n136["QUE_quebecois_peoples_republic"]
        n137["QUE_toward_utopian_socialism"]
    end
    subgraph tier_11["Tier 11"]
        n138["QUE_a_bright_future_ahead"]
        n139{"QUE_christian_social_security"}
        n140["QUE_control_literature"]
        n141["QUE_national_free_market"]
        n142["QUE_nationalize_key_industries"]
        n143["QUE_purge_clerical_elements"]
        n144["QUE_state_led_labor_unions"]
        n145{"QUE_subsidies_to_corporations"}
        n146["QUE_weaponize_mysticism"]
    end
    subgraph tier_12["Tier 12"]
        n147["QUE_advantage_francophones"]
        n148["QUE_demand_new_brunswick"]
        n149["QUE_democratic_diplomacy"]
        n150["QUE_diplomatic_neutrality"]
        n151["QUE_encourage_christian_mutualism"]
        n152["QUE_everything_for_the_state"]
        n153["QUE_militaristic_society"]
        n154["QUE_order_authority_nation"]
        n155["QUE_seize_opponents_assets"]
        n156["QUE_shatter_the_dream"]
    end
    subgraph tier_13["Tier 13"]
        n157{"QUE_aspirations_of_new_france"}
        n158["QUE_demand_newfoundlands"]
        n159{"QUE_expansionism"}
        n160["QUE_free_the_canadian_workers"]
        n161["QUE_integrate_new_england"]
        n162["QUE_wartime_rationing"]
    end
    subgraph tier_14["Tier 14"]
        n163["QUE_align_with_mexico"]
        n164["QUE_approach_berlin"]
        n165["QUE_approach_paris"]
        n166["QUE_approach_rome"]
        n167["QUE_demand_newfoundlands_fascism"]
        n168["QUE_greater_quebec_concept"]
        n169["QUE_our_own_way"]
    end
    subgraph tier_15["Tier 15"]
        n170["QUE_claim_new_bruinswick"]
        n171["QUE_invade_canada"]
    end
    subgraph tier_16["Tier 16"]
        n172["QUE_expand_into_america"]
        n173["QUE_proclaim_french_canada"]
        n174["QUE_push_westward"]
    end
    subgraph tier_17["Tier 17"]
        n175["QUE_consolidate_american_holdings"]
        n176["QUE_establish_republican_canada"]
        n177["QUE_prepare_the_southern_front"]
        n178["QUE_subjugate_mexico"]
    end
    subgraph tier_18["Tier 18"]
        n179["QUE_fight_against_the_ideological_enemy"]
        n180["QUE_reclaim_southern_land"]
    end
    subgraph tier_19["Tier 19"]
        n181["QUE_proclaim_new_france"]
    end
    subgraph tier_20["Tier 20"]
        n182["QUE_avenge_the_seven_year_war"]
        n183["QUE_reclaim_france"]
    end
    n137 --> n138
    n136 --> n138
    n88 --> n97
    n100 --> n103
    n146 --> n147
    n140 --> n147
    n69 --> n70
    n121 --> n128
    n157 --> n163
    n91 --> n98
    n95 --> n98
    n89 --> n98
    n94 --> n98
    n68 --> n71
    n159 --> n164
    n157 --> n165
    n159 --> n166
    n147 --> n157
    n151 --> n157
    n181 --> n182
    n69 --> n72
    n88 --> n99
    n121 --> n129
    n133 --> n139
    n134 --> n139
    n169 --> n170
    n165 --> n170
    n163 --> n170
    n57 --> n59
    n63 --> n73
    n70 --> n88
    n80 --> n88
    n72 --> n88
    n86 --> n89
    n59 --> n63
    n172 --> n175
    n97 --> n104
    n76 --> n79
    n71 --> n79
    n129 --> n140
    n69 --> n80
    n78 --> n80
    n127 --> n130
    n105 --> n115
    n71 --> n81
    n138 --> n148
    n138 --> n158
    n149 --> n158
    n159 --> n167
    n157 --> n167
    n145 --> n149
    n139 --> n149
    n132 --> n149
    n139 --> n150
    n145 --> n150
    n132 --> n150
    n81 --> n90
    n126 --> n131
    n123 --> n131
    n112 --> n116
    n141 --> n151
    n102 --> n105
    n97 --> n106
    n67 --> n82
    n74 --> n82
    n73 --> n83
    n114 --> n117
    n62 --> n64
    n110 --> n132
    n119 --> n132
    n102 --> n107
    n174 --> n176
    n142 --> n152
    n144 --> n152
    n171 --> n172
    n153 --> n159
    n154 --> n159
    n152 --> n159
    n83 --> n91
    n175 --> n179
    n178 --> n179
    n92 --> n100
    n93 --> n100
    n90 --> n100
    n85 --> n92
    n106 --> n118
    n98 --> n108
    n75 --> n84
    n69 --> n84
    n60 --> n65
    n148 --> n160
    n113 --> n119
    n111 --> n119
    n118 --> n133
    n125 --> n133
    n100 --> n109
    n160 --> n168
    n65 --> n74
    n101 --> n110
    n101 --> n111
    n156 --> n161
    n169 --> n171
    n164 --> n171
    n166 --> n171
    n65 --> n75
    n116 --> n134
    n120 --> n134
    n58 --> n60
    n96 --> n101
    n112 --> n120
    n109 --> n121
    n62 --> n66
    n143 --> n153
    n128 --> n141
    n76 --> n85
    n130 --> n142
    n143 --> n154
    n159 --> n169
    n157 --> n169
    n85 --> n93
    n57 --> n61
    n127 --> n135
    n174 --> n177
    n171 --> n173
    n180 --> n181
    n99 --> n112
    n68 --> n76
    n105 --> n122
    n135 --> n143
    n107 --> n123
    n108 --> n123
    n170 --> n174
    n124 --> n136
    n117 --> n136
    n55 --> n57
    n56 --> n57
    n181 --> n183
    n177 --> n180
    n176 --> n180
    n87 --> n94
    n60 --> n67
    n63 --> n77
    n77 --> n86
    n101 --> n113
    n114 --> n124
    n142 --> n155
    n141 --> n155
    n73 --> n87
    n138 --> n156
    n98 --> n114
    n104 --> n125
    n130 --> n144
    n61 --> n68
    n172 --> n178
    n133 --> n145
    n134 --> n145
    n60 --> n69
    n62 --> n69
    n86 --> n95
    n58 --> n62
    n91 --> n102
    n95 --> n102
    n89 --> n102
    n94 --> n102
    n115 --> n137
    n122 --> n137
    n55 --> n58
    n56 --> n58
    n107 --> n126
    n108 --> n126
    n84 --> n96
    n72 --> n96
    n82 --> n96
    n64 --> n78
    n66 --> n78
    n103 --> n127
    n155 --> n162
    n129 --> n146
    n97 x--x n99
    n163 x--x n164
    n163 x--x n165
    n163 x--x n166
    n163 x--x n169
    n98 x--x n102
    n164 x--x n165
    n164 x--x n166
    n164 x--x n169
    n165 x--x n166
    n165 x--x n169
    n166 x--x n169
    n59 x--x n61
    n89 x--x n95
    n149 x--x n150
    n75 x--x n69
    n60 x--x n62
    n55 x--x n56
    n123 x--x n126
    n57 x--x n58
```

# QUE_support_vautrin_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n9["QUE_quebec_arsenal"]
        n4["QUE_rearmement_agreement"]
        n184(("QUE_support_vautrin_plan"))
    end
    subgraph tier_1["Tier 1"]
        n185["QUE_abitibi_gold_rush"]
        n186["QUE_saguenay_aluminum"]
        n6["QUE_sorel_steel_and_foundry"]
        n187{"QUE_tackle_the_economic_issues"}
    end
    subgraph tier_2["Tier 2"]
        n188["QUE_encourage_anglo_canadian_investments"]
        n189["QUE_enforce_economic_nationalism"]
        n15["QUE_small_arms_production"]
        n5["QUE_sorel_industries"]
        n190["QUE_stimulate_the_economy"]
    end
    subgraph tier_3["Tier 3"]
        n16["QUE_artillery_improvements"]
        n191["QUE_cooperate_with_canadian_capitalists"]
        n192["QUE_fund_small_corporations"]
        n2["QUE_locomotive_industry"]
        n19["QUE_modernized_support_equipment"]
    end
    subgraph tier_4["Tier 4"]
        n22["QUE_bombardier_vehicles"]
        n193{"QUE_fix_the_broken_ties"}
        n194{"QUE_keep_bank_of_canada"}
        n195{"QUE_monetary_reforms"}
        n196{"QUE_promote_francophone_immigration"}
        n25["QUE_quebecois_officer_corps"]
        n27["QUE_tank_program"]
    end
    subgraph tier_5["Tier 5"]
        n197["QUE_a_change_in_course"]
        n28["QUE_angus_shop_tank_production"]
        n198{"QUE_continue_our_independence"}
        n29["QUE_expand_bombardier_factories"]
        n30["QUE_military_industrial_cooperation"]
    end
    subgraph tier_6["Tier 6"]
        n199["QUE_a_talk_with_ottawa"]
        n200["QUE_further_cut_ties"]
        n32["QUE_nuclear_research"]
        n201["QUE_open_the_border"]
    end
    subgraph tier_7["Tier 7"]
        n202["QUE_give_canada_another_chance"]
        n203["QUE_independence_secure"]
    end
    subgraph tier_8["Tier 8"]
        n7["QUE_the_quebecois_economy"]
    end
    subgraph tier_9["Tier 9"]
        n31["QUE_develop_the_capitale_nationale"]
    end
    subgraph tier_10["Tier 10"]
        n33["QUE_cote_nord_expansion"]
        n34["QUE_develop_northern_economy"]
        n35["QUE_mauricie_development"]
        n36["QUE_saguenay_industries"]
        n37["QUE_southern_development_initiative"]
    end
    n193 --> n197
    n194 --> n197
    n198 --> n199
    n184 --> n185
    n25 --> n28
    n15 --> n16
    n2 --> n22
    n19 --> n22
    n193 --> n198
    n194 --> n198
    n196 --> n198
    n195 --> n198
    n188 --> n191
    n31 --> n33
    n31 --> n34
    n7 --> n31
    n29 --> n31
    n187 --> n188
    n187 --> n189
    n22 --> n29
    n2 --> n29
    n191 --> n193
    n189 --> n192
    n198 --> n200
    n201 --> n202
    n199 --> n203
    n200 --> n203
    n191 --> n194
    n190 --> n2
    n31 --> n35
    n25 --> n30
    n15 --> n19
    n5 --> n19
    n192 --> n195
    n30 --> n32
    n197 --> n201
    n192 --> n196
    n16 --> n25
    n19 --> n25
    n184 --> n186
    n31 --> n36
    n9 --> n15
    n6 --> n15
    n4 --> n15
    n6 --> n5
    n186 --> n5
    n185 --> n5
    n184 --> n6
    n31 --> n37
    n6 --> n190
    n186 --> n190
    n185 --> n190
    n184 --> n187
    n19 --> n27
    n16 --> n27
    n202 --> n7
    n203 --> n7
    n197 x--x n198
    n199 x--x n200
    n188 x--x n189
```
