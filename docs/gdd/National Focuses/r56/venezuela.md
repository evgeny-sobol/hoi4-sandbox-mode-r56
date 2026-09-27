# VEN_a_seperate_branch

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("VEN_a_seperate_branch"))
        n2["VEN_acquire_czech_weaponry"]
        n3["VEN_expand_zulia_shipping"]
    end
    subgraph tier_1["Tier 1"]
        n4["VEN_el_libertador_air_base"]
        n5["VEN_fighter_development"]
    end
    subgraph tier_2["Tier 2"]
        n6["VEN_airforce_academy"]
        n7["VEN_naval_aircraft"]
        n8["VEN_purchase_british_aircraft"]
    end
    subgraph tier_3["Tier 3"]
        n9["VEN_bomber_production"]
        n10["VEN_radar_technologies"]
        n11["VEN_rocketry_experiments"]
    end
    n4 --> n6
    n5 --> n6
    n6 --> n9
    n1 --> n4
    n1 --> n5
    n3 --> n7
    n5 --> n7
    n5 --> n8
    n2 --> n8
    n6 --> n10
    n6 --> n11
```

# VEN_congress

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12{"VEN_congress"}
    end
    subgraph tier_1["Tier 1"]
        n13{"VEN_1935_elections"}
        n14["VEN_reorganize_the_ARDI"]
    end
    subgraph tier_2["Tier 2"]
        n15["VEN_barranquilla_plan"]
        n16["VEN_eleazar_contreras"]
        n17["VEN_generation_of_28"]
        n18["VEN_isaias_angarita"]
        n19["VEN_marcos_jimenez"]
        n20["VEN_new_republic"]
    end
    subgraph tier_3["Tier 3"]
        n21["VEN_crush_communists"]
        n22["VEN_depoliticize_the_army"]
        n23["VEN_enforce_army_loyalty"]
        n24["VEN_fate_of_jimenez"]
        n25["VEN_german_relations"]
        n26["VEN_health_and_social_assistance"]
        n27["VEN_labour_reforms"]
        n28["VEN_legalize_communism"]
        n29["VEN_miraflores_concessions"]
        n30["VEN_paramilitarism"]
        n31["VEN_protect_workers_rights"]
        n32{"VEN_rebellion"}
        n33["VEN_western_agreements"]
    end
    subgraph tier_4["Tier 4"]
        n34["VEN_DSN"]
        n35["VEN_abolish_death_penalty"]
        n36["VEN_american_student_exchange"]
        n37["VEN_arnoldo_gabaldon"]
        n38{"VEN_bolivarian_socialist_theory"}
        n39["VEN_cult_of_creole"]
        n40["VEN_enpower_the_pcv"]
        n41["VEN_german_advisors"]
        n42["VEN_german_oil_deal"]
        n43["VEN_housing_act"]
        n44["VEN_jewish_asylum"]
        n45["VEN_liberalize_oil_trade"]
        n46["VEN_military_youth"]
        n47["VEN_nationalize_the_banking_sector"]
        n48["VEN_presidential_amendment"]
        n49["VEN_promote_political_cooperation"]
        n50["VEN_reshuffle_of_general_staff"]
        n51{"VEN_suspend_elections"}
        n52["VEN_tax_reforms"]
    end
    subgraph tier_5["Tier 5"]
        n53{"VEN_allow_new_elections"}
        n54["VEN_amnesty_to_communists"]
        n55["VEN_arm_the_companies"]
        n56["VEN_central_university"]
        n57["VEN_communist_reforms"]
        n58{"VEN_constitute_womens_rights"}
        n59{"VEN_cult_of_personality"}
        n60["VEN_export_oil_aggressively"]
        n61{"VEN_institute_1936_constitution"}
        n62["VEN_military_colleges"]
        n63["VEN_privatize_oil"]
        n64["VEN_puntofijo_pact"]
        n65["VEN_purge_disloyal_officers"]
    end
    subgraph tier_6["Tier 6"]
        n66["VEN_50_50_oil_act"]
        n67["VEN_concessions_to_oil_unions"]
        n68["VEN_form_CPAI"]
        n69["VEN_join_allies"]
        n70{"VEN_join_axis"}
        n71["VEN_nationalist_education"]
        n72["VEN_neutrality_focus"]
        n73["VEN_oil_protection_squadrons"]
        n74["VEN_rebellion_recoverment_effots"]
        n75["VEN_seize_government_assets"]
        n76["VEN_seize_public_services"]
        n77["VEN_spanish_civil_war_involvement"]
        n78{"VEN_viva_venezuela"}
    end
    subgraph tier_7["Tier 7"]
        n79["VEN_assisted_oil_development"]
        n80{"VEN_by_any_means"}
        n81["VEN_food_importation"]
        n82["VEN_gran_colombia"]
        n83["VEN_national_literacy_programs"]
        n84{"VEN_oil_protection"}
        n85["VEN_peoples_university_of_venezuela"]
        n86["VEN_push_north"]
        n87["VEN_redistribution_of_wealth"]
        n88["VEN_tax_reforms_socialist"]
    end
    subgraph tier_8["Tier 8"]
        n89["VEN_annex_colombia"]
        n90["VEN_british_air_bases"]
        n91{"VEN_creole_indivisible"}
        n92["VEN_eliminating_the_competition"]
        n93["VEN_non_agression_colombia"]
        n94["VEN_prepare_amphibious_landings"]
        n95{"VEN_president_betancourts_legacy"}
        n96{"VEN_reorganization_of_congress"}
        n97["VEN_seize_curacao"]
        n98["VEN_zulia_line"]
    end
    subgraph tier_9["Tier 9"]
        n99["VEN_arms_protect_the_nation"]
        n100["VEN_attack_cuba"]
        n101["VEN_attack_ecuador"]
        n102["VEN_attack_hispaniola"]
        n103["VEN_attack_peru"]
        n104["VEN_demand_guyana"]
        n105["VEN_embargo_japan"]
        n106["VEN_foreign_expeditions"]
        n107["VEN_militarize_the_people"]
        n108["VEN_neutrality_focus2"]
        n109["VEN_seize_trinidad"]
        n110["VEN_under_soviet_dominion"]
        n111["VEN_venezuelan_fortress"]
        n112["VEN_venezuelan_way_of_communism"]
    end
    subgraph tier_10["Tier 10"]
        n113["VEN_anarchism_knows_no_borders"]
        n114{"VEN_anti_submarine"}
        n115["VEN_arms_protect_the_nation2"]
        n116["VEN_intergrate_caribbean"]
        n117["VEN_invite_polish_exiles"]
        n118["VEN_invite_soviet_officers"]
        n119["VEN_soviet_tank_factories"]
        n120["VEN_spread_the_south_american_revolution"]
        n121["VEN_strike_panama"]
    end
    subgraph tier_11["Tier 11"]
        n122["VEN_attack_germany"]
        n123["VEN_attack_japan"]
        n124["VEN_caribbean_naval_hub"]
        n125["VEN_introduce_political_commissars"]
        n126["VEN_latin_america_guardian"]
        n127["VEN_support_argentinian_revolution"]
        n128["VEN_support_brazillian_revolution"]
        n129["VEN_support_chilean_revolution"]
        n130["VEN_support_colombian_revolution"]
        n131["VEN_support_peruvian_revolution"]
        n132["VEN_unify_political_command"]
    end
    subgraph tier_12["Tier 12"]
        n133["VEN_bolivarian_development"]
        n134["VEN_connect_the_cities"]
        n135{"VEN_expand_gran_colombia"}
        n136["VEN_legacy_of_piracy"]
        n137["VEN_push_to_end_captalism"]
        n138["VEN_unify_bolivariana_army"]
        n139["VEN_unite_the_caribbean_under_venezuela"]
    end
    subgraph tier_13["Tier 13"]
        n140{"VEN_alliance_with_bolivia"}
        n141{"VEN_alliance_with_honduras"}
        n142["VEN_attack_america"]
        n143["VEN_attack_america_communist"]
        n144{"VEN_attack_bolivia"}
        n145["VEN_attack_britain"]
        n146{"VEN_attack_central_america"}
        n147["VEN_expand_ecuadorian_cocoa_fields"]
        n148["VEN_exploit_colombian_rubber"]
        n149["VEN_form_cuban_divisons"]
        n150["VEN_modern_pirate_navy"]
        n151["VEN_recruit_haitian_pilots"]
    end
    subgraph tier_14["Tier 14"]
        n152["VEN_alliance_with_mexico"]
        n153["VEN_alliance_with_south_south_america"]
        n154["VEN_attack_mexico"]
        n155["VEN_attack_south_south_america"]
    end
    subgraph tier_15["Tier 15"]
        n156["VEN_intervention_in_brazil"]
    end
    n12 --> n13
    n64 --> n66
    n54 --> n66
    n29 --> n34
    n22 --> n35
    n135 --> n140
    n135 --> n141
    n146 --> n152
    n141 --> n152
    n140 --> n153
    n144 --> n153
    n35 --> n53
    n52 --> n53
    n33 --> n36
    n38 --> n54
    n107 --> n113
    n82 --> n89
    n105 --> n114
    n106 --> n114
    n39 --> n55
    n93 --> n99
    n98 --> n99
    n108 --> n115
    n26 --> n37
    n69 --> n79
    n139 --> n142
    n137 --> n143
    n135 --> n144
    n137 --> n145
    n135 --> n146
    n94 --> n100
    n89 --> n101
    n114 --> n122
    n94 --> n102
    n114 --> n123
    n146 --> n154
    n141 --> n154
    n89 --> n103
    n140 --> n155
    n144 --> n155
    n14 --> n15
    n132 --> n133
    n32 --> n38
    n79 --> n90
    n81 --> n90
    n73 --> n80
    n76 --> n80
    n75 --> n80
    n116 --> n124
    n44 --> n56
    n37 --> n56
    n40 --> n57
    n57 --> n67
    n124 --> n134
    n43 --> n58
    n47 --> n58
    n49 --> n58
    n80 --> n91
    n19 --> n21
    n32 --> n39
    n46 --> n59
    n89 --> n104
    n20 --> n22
    n13 --> n16
    n80 --> n92
    n90 --> n105
    n19 --> n23
    n32 --> n40
    n133 --> n147
    n132 --> n135
    n133 --> n148
    n39 --> n60
    n18 --> n24
    n69 --> n81
    n90 --> n106
    n65 --> n68
    n134 --> n149
    n14 --> n17
    n25 --> n41
    n25 --> n42
    n16 --> n25
    n19 --> n25
    n70 --> n82
    n78 --> n82
    n16 --> n26
    n31 --> n43
    n48 --> n61
    n34 --> n61
    n50 --> n61
    n102 --> n116
    n109 --> n116
    n100 --> n116
    n155 --> n156
    n153 --> n156
    n152 --> n156
    n154 --> n156
    n119 --> n125
    n118 --> n125
    n108 --> n117
    n110 --> n118
    n13 --> n18
    n26 --> n44
    n58 --> n69
    n61 --> n69
    n53 --> n69
    n61 --> n70
    n58 --> n70
    n59 --> n70
    n20 --> n27
    n114 --> n126
    n124 --> n136
    n18 --> n28
    n22 --> n45
    n27 --> n45
    n13 --> n19
    n92 --> n107
    n51 --> n62
    n30 --> n46
    n23 --> n46
    n16 --> n29
    n136 --> n150
    n66 --> n83
    n62 --> n71
    n63 --> n71
    n31 --> n47
    n61 --> n72
    n58 --> n72
    n59 --> n72
    n53 --> n72
    n96 --> n108
    n95 --> n108
    n91 --> n108
    n13 --> n20
    n84 --> n93
    n72 --> n84
    n55 --> n73
    n19 --> n30
    n67 --> n85
    n86 --> n94
    n83 --> n95
    n88 --> n95
    n29 --> n48
    n51 --> n63
    n28 --> n49
    n18 --> n31
    n38 --> n64
    n40 --> n65
    n70 --> n86
    n78 --> n86
    n129 --> n137
    n128 --> n137
    n127 --> n137
    n130 --> n137
    n131 --> n137
    n15 --> n32
    n17 --> n32
    n57 --> n74
    n64 --> n74
    n54 --> n74
    n134 --> n151
    n67 --> n87
    n87 --> n96
    n85 --> n96
    n12 --> n14
    n29 --> n50
    n82 --> n97
    n86 --> n97
    n60 --> n75
    n60 --> n76
    n94 --> n109
    n110 --> n119
    n21 --> n77
    n65 --> n77
    n112 --> n120
    n101 --> n121
    n104 --> n121
    n103 --> n121
    n120 --> n127
    n120 --> n128
    n120 --> n129
    n120 --> n130
    n120 --> n131
    n21 --> n51
    n27 --> n52
    n66 --> n88
    n96 --> n110
    n132 --> n138
    n121 --> n132
    n124 --> n139
    n91 --> n111
    n96 --> n112
    n61 --> n78
    n58 --> n78
    n59 --> n78
    n18 --> n33
    n20 --> n33
    n84 --> n98
    n13 x--x n14
    n140 x--x n144
    n141 x--x n146
    n152 x--x n154
    n153 x--x n155
    n54 x--x n64
    n122 x--x n123
    n38 x--x n39
    n38 x--x n40
    n91 x--x n92
    n39 x--x n40
    n16 x--x n18
    n16 x--x n19
    n16 x--x n20
    n82 x--x n86
    n18 x--x n19
    n18 x--x n20
    n69 x--x n70
    n69 x--x n72
    n69 x--x n78
    n70 x--x n72
    n70 x--x n78
    n19 x--x n20
    n62 x--x n63
    n72 x--x n78
    n108 x--x n110
    n108 x--x n112
    n93 x--x n98
    n110 x--x n112
```

# VEN_expand_the_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n157(("VEN_expand_the_navy"))
        n5["VEN_fighter_development"]
        n158["VEN_venezuelan_military_academy"]
    end
    subgraph tier_1["Tier 1"]
        n159{"VEN_destroyer_effort"}
        n3["VEN_expand_zulia_shipping"]
        n160["VEN_marine_forces"]
        n161{"VEN_replace_miniscule_vessels"}
    end
    subgraph tier_2["Tier 2"]
        n162["VEN_amphibious_exercises"]
        n163["VEN_carrier_development"]
        n7["VEN_naval_aircraft"]
        n164["VEN_the_big_guns"]
        n165["VEN_trade_fleets"]
    end
    subgraph tier_3["Tier 3"]
        n166["VEN_naval_attrition"]
    end
    subgraph tier_4["Tier 4"]
        n167["VEN_protect_curacao"]
    end
    n160 --> n162
    n159 --> n163
    n161 --> n163
    n157 --> n159
    n157 --> n3
    n158 --> n160
    n157 --> n160
    n3 --> n7
    n5 --> n7
    n164 --> n166
    n163 --> n166
    n166 --> n167
    n165 --> n167
    n157 --> n161
    n159 --> n164
    n161 --> n164
    n3 --> n165
    n163 x--x n164
```

# VEN_national_development

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n5["VEN_fighter_development"]
        n168{"VEN_national_development"}
    end
    subgraph tier_1["Tier 1"]
        n2["VEN_acquire_czech_weaponry"]
        n169["VEN_expand_oil_industry"]
        n170["VEN_fund_independent_arms_industries"]
        n171["VEN_modern_machinery"]
        n172["VEN_national_recovery_act"]
    end
    subgraph tier_2["Tier 2"]
        n173["VEN_adopt_rearmament_policies"]
        n174["VEN_alternatives_to_oil"]
        n175["VEN_build_rural_schools"]
        n176["VEN_develop_domestic_railways"]
        n177["VEN_engineering_schools"]
        n8["VEN_purchase_british_aircraft"]
    end
    subgraph tier_3["Tier 3"]
        n178["VEN_expand_curacao_refinery"]
        n179["VEN_explosive_factories"]
        n180["VEN_invest_mining_industry"]
        n181["VEN_open_rubber_plantations"]
        n182["VEN_production_quotas"]
    end
    subgraph tier_4["Tier 4"]
        n183["VEN_establish_IFE"]
        n184["VEN_improve_living_standards"]
        n185["VEN_industrial_development"]
        n186["VEN_mighty_weaponry"]
        n187["VEN_national_defense_funds"]
        n188["VEN_promote_foreign_investment"]
    end
    subgraph tier_5["Tier 5"]
        n189["VEN_acheiving_autarky"]
        n190["VEN_lift_oil_curse"]
    end
    n183 --> n189
    n188 --> n189
    n168 --> n2
    n2 --> n173
    n170 --> n173
    n172 --> n174
    n171 --> n175
    n171 --> n176
    n169 --> n177
    n181 --> n183
    n177 --> n178
    n168 --> n169
    n173 --> n179
    n168 --> n170
    n180 --> n184
    n180 --> n185
    n174 --> n180
    n184 --> n190
    n185 --> n190
    n176 --> n186
    n179 --> n186
    n168 --> n171
    n182 --> n187
    n179 --> n187
    n168 --> n172
    n177 --> n181
    n173 --> n182
    n181 --> n188
    n5 --> n8
    n2 --> n8
    n2 x--x n170
    n169 x--x n172
```

# VEN_venezuelan_military_academy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n157["VEN_expand_the_navy"]
        n158(("VEN_venezuelan_military_academy"))
    end
    subgraph tier_1["Tier 1"]
        n191["VEN_form_the_GNB"]
        n160["VEN_marine_forces"]
        n192["VEN_modernize_our_weaponry"]
    end
    subgraph tier_2["Tier 2"]
        n162["VEN_amphibious_exercises"]
        n193["VEN_field_piece_research"]
        n194["VEN_logistical_brigades"]
        n195["VEN_radio_technologies"]
    end
    subgraph tier_3["Tier 3"]
        n196["VEN_army_motorization"]
        n197["VEN_bicycle_battalions"]
        n198["VEN_central_intelligence"]
        n199["VEN_new_military_institute"]
    end
    subgraph tier_4["Tier 4"]
        n200["VEN_adapt_to_the_amazons"]
        n201["VEN_decryption_department"]
        n202["VEN_develop_venezuelan_armour"]
    end
    subgraph tier_5["Tier 5"]
        n203["VEN_study_nuclear_power"]
    end
    n197 --> n200
    n196 --> n200
    n160 --> n162
    n194 --> n196
    n195 --> n196
    n194 --> n197
    n195 --> n198
    n198 --> n201
    n196 --> n202
    n192 --> n193
    n158 --> n191
    n192 --> n194
    n158 --> n160
    n157 --> n160
    n158 --> n192
    n195 --> n199
    n192 --> n195
    n200 --> n203
```
