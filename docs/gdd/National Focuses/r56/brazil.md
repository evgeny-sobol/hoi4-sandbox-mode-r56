# BRA_coffee_crisis_aftermath

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("BRA_coffee_crisis_aftermath"))
    end
    subgraph tier_1["Tier 1"]
        n2["BRA_desenvolvimentismo"]
        n3["BRA_radio_nacional"]
    end
    subgraph tier_2["Tier 2"]
        n4["BRA_companhia_siderurgica_nacional"]
        n5["BRA_deal_with_the_cangaceiro"]
        n6["BRA_promote_immigration_to_brazil"]
        n7["BRA_promote_resource_extraction"]
        n8["BRA_stimulate_the_civilian_economy"]
    end
    subgraph tier_3["Tier 3"]
        n9["BRA_batalha_do_borracha"]
        n10["BRA_domestic_arms_industry"]
        n11["BRA_establish_caloi"]
        n12["BRA_invest_in_railways"]
        n13["BRA_reach_out_to_the_great_powers"]
    end
    subgraph tier_4["Tier 4"]
        n14["BRA_banco_do_brasil"]
        n15["BRA_establish_companhia_vale_do_rio_doce"]
        n16{"BRA_invest_in_road_infrastructure"}
        n17["BRA_national_petroleum_council"]
        n18["BRA_war_production"]
    end
    subgraph tier_5["Tier 5"]
        n19["BRA_bonus_tech_slot"]
        n20["BRA_centralize_development"]
        n21["BRA_expand_fordlandia"]
        n22["BRA_fabrica_nacional_de_motores"]
        n23["BRA_federal_development"]
        n24["BRA_invest_in_ports"]
    end
    subgraph tier_6["Tier 6"]
        n25["BRA_financial_stimulation"]
    end
    n9 --> n14
    n4 --> n9
    n7 --> n9
    n16 --> n19
    n14 --> n20
    n2 --> n4
    n3 --> n4
    n3 --> n5
    n1 --> n2
    n8 --> n10
    n7 --> n11
    n4 --> n11
    n9 --> n15
    n16 --> n21
    n16 --> n22
    n14 --> n23
    n20 --> n25
    n23 --> n25
    n17 --> n24
    n7 --> n12
    n4 --> n12
    n9 --> n16
    n12 --> n16
    n12 --> n17
    n2 --> n6
    n3 --> n7
    n2 --> n7
    n1 --> n3
    n7 --> n13
    n4 --> n13
    n2 --> n8
    n10 --> n18
    n21 x--x n22
```

# BRA_end_the_state_of_emergency

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26{"BRA_end_the_state_of_emergency"}
        n27{"BRA_ethical_internationalism"}
        n28["BRA_prepare_for_second_intentona"]
        n29["BRA_reward_army_loyalty"]
        n30["BRA_tribunal_de_seguranca_nacional"]
    end
    subgraph tier_1["Tier 1"]
        n31{"BRA_repeal_the_national_security_law"}
        n32{"BRA_romanticize_the_old_empire"}
    end
    subgraph tier_2["Tier 2"]
        n33["BRA_continue_centralization"]
        n34["BRA_greater_federalism"]
        n35["BRA_petropolis_line"]
        n36["BRA_vassouras_line"]
    end
    subgraph tier_3["Tier 3"]
        n37["BRA_court_the_military"]
        n38["BRA_implement_a_national_guard"]
        n39["BRA_restore_the_coffee_barons"]
    end
    subgraph tier_4["Tier 4"]
        n40["BRA_ban_the_communist_party"]
        n41["BRA_constitutional_monarchy"]
        n42["BRA_end_military_interference"]
        n43["BRA_establish_the_brazilian_investment_bank"]
        n44["BRA_nationalize_the_banks"]
    end
    subgraph tier_5["Tier 5"]
        n45["BRA_church"]
        n46["BRA_free_speech"]
        n47["BRA_implement_article_138"]
        n48["BRA_invest_in_the_armed_forces"]
        n49["BRA_issue_lordships"]
        n50["BRA_posts_for_generals"]
        n51["BRA_undermine_democracy"]
    end
    subgraph tier_6["Tier 6"]
        n52["BRA_address_labor_disputes"]
        n53["BRA_promote_agriculture"]
        n54["BRA_royal_colleges"]
        n55["BRA_tech_slot_2"]
        n56["BRA_third_republic"]
        n57["BRA_united_states_of_brazil"]
        n58["BRA_use_the_national_security_law"]
    end
    subgraph tier_7["Tier 7"]
        n59["BRA_combat_separatism"]
        n60{"BRA_empire_of_brazil"}
        n61["BRA_invite_foreign_companies"]
        n62["BRA_penal_battalions"]
        n63{"BRA_the_international_crisis"}
        n64["BRA_united_kingdom_of_brazil_and_portugal"]
        n65["BRA_war_bonds"]
    end
    subgraph tier_8["Tier 8"]
        n66["BRA_amazonian_settlement"]
        n67["BRA_demand_portugese_submission"]
        n68["BRA_demand_portugese_territory"]
        n69["BRA_reclaim_territory_in_south_america"]
    end
    subgraph tier_9["Tier 9"]
        n70["BRA_expand_colonial_empire"]
        n71["BRA_restoration_of_honor"]
        n72["BRA_spirit_of_acre_war"]
    end
    subgraph tier_10["Tier 10"]
        n73{"BRA_secure_our_borders"}
    end
    subgraph tier_11["Tier 11"]
        n74["BRA_cooperation_in_the_americas"]
        n75["BRA_domination_of_the_americas"]
    end
    subgraph tier_12["Tier 12"]
        n76["BRA_berlin_accords"]
        n77["BRA_defense_of_the_fatherland"]
        n78["BRA_defense_spending"]
        n79["BRA_form_mercosul"]
        n80["BRA_guyana_crisis"]
        n81["BRA_no_communism_in_south_america"]
        n82["BRA_no_fascism_in_south_america"]
        n83["BRA_reach_out_to_our_neighbors"]
        n84["BRA_rome_accords"]
        n85["BRA_washington_accords"]
    end
    subgraph tier_13["Tier 13"]
        n86["BRA_attack_bolivia"]
        n87["BRA_disrupt_operation_bolivar"]
        n88["BRA_expand_operation_bolivar"]
        n89["BRA_foreign_legion"]
        n90["BRA_italian_car_industry"]
        n91["BRA_natal_naval_base"]
        n92["BRA_paraguay_intervention"]
        n93{"BRA_potenji_river_conference"}
        n94["BRA_smoking_cobras"]
        n95{"BRA_south_american_defense_cooperation"}
    end
    subgraph tier_14["Tier 14"]
        n96["BRA_attack_chile"]
        n97["BRA_german_subs"]
        n98["BRA_german_tanks"]
        n99["BRA_italian_aircraft"]
        n100["BRA_italian_trucks"]
        n101["BRA_provoke_argentina"]
        n102["BRA_senta_a_pua"]
        n103["BRA_south_american_research_cooperation"]
        n104["BRA_us_brazil_technology_exchange"]
    end
    subgraph tier_15["Tier 15"]
        n105["BRA_german_cooperation"]
        n106["BRA_italian_cooperation"]
        n107["BRA_panama_push"]
        n108["BRA_united_states_of_south_america"]
    end
    subgraph tier_16["Tier 16"]
        n109["BRA_unify_south_america"]
    end
    n46 --> n52
    n50 --> n52
    n62 --> n66
    n80 --> n86
    n92 --> n96
    n86 --> n96
    n37 --> n40
    n75 --> n76
    n43 --> n45
    n52 --> n59
    n39 --> n41
    n31 --> n33
    n73 --> n74
    n63 --> n74
    n33 --> n37
    n75 --> n77
    n74 --> n78
    n60 --> n67
    n60 --> n68
    n78 --> n87
    n73 --> n75
    n27 --> n75
    n58 --> n60
    n38 --> n42
    n37 --> n43
    n68 --> n70
    n67 --> n70
    n69 --> n70
    n76 --> n88
    n84 --> n88
    n83 --> n89
    n75 --> n79
    n42 --> n46
    n98 --> n105
    n97 --> n105
    n88 --> n97
    n88 --> n98
    n31 --> n34
    n75 --> n80
    n34 --> n38
    n44 --> n47
    n41 --> n48
    n52 --> n61
    n41 --> n49
    n90 --> n99
    n84 --> n90
    n76 --> n90
    n100 --> n106
    n99 --> n106
    n90 --> n100
    n85 --> n91
    n38 --> n44
    n74 --> n81
    n74 --> n82
    n101 --> n107
    n96 --> n107
    n80 --> n92
    n58 --> n62
    n32 --> n35
    n40 --> n50
    n85 --> n93
    n49 --> n53
    n86 --> n101
    n92 --> n101
    n74 --> n83
    n60 --> n69
    n26 --> n31
    n68 --> n71
    n67 --> n71
    n69 --> n71
    n36 --> n39
    n35 --> n39
    n26 --> n32
    n75 --> n84
    n48 --> n54
    n29 --> n73
    n71 --> n73
    n91 --> n102
    n85 --> n94
    n83 --> n95
    n95 --> n103
    n68 --> n72
    n67 --> n72
    n69 --> n72
    n47 --> n55
    n45 --> n55
    n52 --> n63
    n50 --> n56
    n41 --> n51
    n105 --> n109
    n106 --> n109
    n107 --> n109
    n58 --> n64
    n46 --> n57
    n104 --> n108
    n103 --> n108
    n93 --> n104
    n51 --> n58
    n32 --> n36
    n52 --> n65
    n74 --> n85
    n33 x--x n34
    n74 x--x n75
    n67 x--x n68
    n26 x--x n28
    n26 x--x n30
    n35 x--x n36
    n31 x--x n32
    n103 x--x n104
```

# BRA_prepare_for_second_intentona

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["BRA_end_the_state_of_emergency"]
        n28(("BRA_prepare_for_second_intentona"))
        n30["BRA_tribunal_de_seguranca_nacional"]
    end
    subgraph tier_1["Tier 1"]
        n110{"BRA_infilitrate_the_military"}
        n111{"BRA_radicalize_the_proletariat"}
    end
    subgraph tier_2["Tier 2"]
        n112{"BRA_free_prestes"}
        n113{"BRA_revive_the_anl"}
    end
    subgraph tier_3["Tier 3"]
        n114{"BRA_launch_the_revolution"}
        n115["BRA_seek_soviet_support"]
        n116{"BRA_sway_the_cangaco"}
    end
    subgraph tier_4["Tier 4"]
        n117["BRA_align_with_moscow"]
        n118["BRA_cangaco_coup"]
        n119["BRA_oust_prestes"]
    end
    subgraph tier_5["Tier 5"]
        n120["BRA_international_brigades"]
        n121["BRA_kgbrazil"]
        n122["BRA_nationalization_of_industry"]
        n123{"BRA_soviet_economic_aid"}
        n124["BRA_tech_slot_3"]
    end
    subgraph tier_6["Tier 6"]
        n125["BRA_collectivization_of_agriculture"]
        n126["BRA_license_with_the_soviets"]
        n127["BRA_purchase_soviet_equipment"]
        n128{"BRA_rapid_industrialization"}
        n129["BRA_sway_the_neighbors"]
    end
    subgraph tier_7["Tier 7"]
        n130["BRA_allow_the_church_to_operate"]
        n131["BRA_collectivization_of_transport"]
        n132["BRA_soviet_arms_industry"]
        n133["BRA_state_atheism"]
    end
    subgraph tier_8["Tier 8"]
        n134["BRA_equality_for_women"]
    end
    subgraph tier_9["Tier 9"]
        n135{"BRA_spread_the_revolution"}
    end
    subgraph tier_10["Tier 10"]
        n136["BRA_join_the_comintern"]
        n137["BRA_the_latin_american_socialist_cooperative"]
    end
    subgraph tier_11["Tier 11"]
        n138["BRA_anti_imperialism"]
        n139["BRA_end_south_american_capitalism"]
        n140["BRA_establish_ulasr"]
        n141["BRA_jaguar_diplomacy"]
        n142["BRA_smash_fascism"]
    end
    n114 --> n117
    n112 --> n117
    n128 --> n130
    n136 --> n138
    n137 --> n138
    n114 --> n118
    n116 --> n118
    n122 --> n125
    n125 --> n131
    n136 --> n139
    n137 --> n139
    n133 --> n134
    n130 --> n134
    n137 --> n140
    n136 --> n140
    n110 --> n112
    n111 --> n112
    n28 --> n110
    n117 --> n120
    n119 --> n120
    n118 --> n120
    n137 --> n141
    n136 --> n141
    n135 --> n136
    n117 --> n121
    n119 --> n121
    n118 --> n121
    n112 --> n114
    n113 --> n114
    n123 --> n126
    n117 --> n122
    n119 --> n122
    n118 --> n122
    n114 --> n119
    n113 --> n119
    n123 --> n127
    n28 --> n111
    n122 --> n128
    n111 --> n113
    n110 --> n113
    n112 --> n115
    n136 --> n142
    n137 --> n142
    n126 --> n132
    n127 --> n132
    n117 --> n123
    n132 --> n135
    n134 --> n135
    n128 --> n133
    n113 --> n116
    n121 --> n129
    n117 --> n124
    n119 --> n124
    n118 --> n124
    n135 --> n137
    n117 x--x n118
    n117 x--x n119
    n130 x--x n133
    n118 x--x n119
    n26 x--x n28
    n112 x--x n113
    n136 x--x n137
    n126 x--x n127
    n28 x--x n30
```

# BRA_tribunal_de_seguranca_nacional

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["BRA_end_the_state_of_emergency"]
        n28["BRA_prepare_for_second_intentona"]
        n71["BRA_restoration_of_honor"]
        n63{"BRA_the_international_crisis"}
        n30(("BRA_tribunal_de_seguranca_nacional"))
    end
    subgraph tier_1["Tier 1"]
        n143{"BRA_ensure_continued_military_support"}
        n144{"BRA_work_with_the_integralists"}
    end
    subgraph tier_2["Tier 2"]
        n145{"BRA_cohen_plan"}
    end
    subgraph tier_3["Tier 3"]
        n146["BRA_estado_moderno"]
        n147["BRA_estado_novo"]
    end
    subgraph tier_4["Tier 4"]
        n148{"BRA_anaue"}
        n149{"BRA_the_polaca"}
    end
    subgraph tier_5["Tier 5"]
        n150["BRA_autarky"]
        n151["BRA_ban_political_parties"]
        n152["BRA_corporatism"]
        n153{"BRA_departamento_feminino"}
        n154["BRA_establish_psad"]
        n155{"BRA_reject_cosmopolitanism"}
        n156["BRA_uruguay_ultimatum"]
    end
    subgraph tier_6["Tier 6"]
        n157["BRA_decree_no_37"]
        n158["BRA_departamendo_de_propaganda"]
        n159["BRA_departamento_de_ordem_politica_e_social"]
        n160["BRA_federal_employment_plan"]
        n161["BRA_in_vargas_we_trust"]
        n162["BRA_integrity_of_the_fatherland"]
    end
    subgraph tier_7["Tier 7"]
        n163["BRA_brazil_integral"]
        n29{"BRA_reward_army_loyalty"}
        n164["BRA_tech_slot_1"]
    end
    subgraph tier_8["Tier 8"]
        n165["BRA_depose_vargas"]
        n27{"BRA_ethical_internationalism"}
        n166{"BRA_reinvigorate_the_navy"}
        n73{"BRA_secure_our_borders"}
    end
    subgraph tier_9["Tier 9"]
        n74["BRA_cooperation_in_the_americas"]
        n75["BRA_domination_of_the_americas"]
        n167{"BRA_support_rural_folk"}
        n168{"BRA_support_the_landowners"}
    end
    subgraph tier_10["Tier 10"]
        n76["BRA_berlin_accords"]
        n169["BRA_consolidation_of_labor_laws"]
        n77["BRA_defense_of_the_fatherland"]
        n78["BRA_defense_spending"]
        n79["BRA_form_mercosul"]
        n80["BRA_guyana_crisis"]
        n81["BRA_no_communism_in_south_america"]
        n82["BRA_no_fascism_in_south_america"]
        n83["BRA_reach_out_to_our_neighbors"]
        n84["BRA_rome_accords"]
        n170["BRA_support_industrialists"]
        n85["BRA_washington_accords"]
    end
    subgraph tier_11["Tier 11"]
        n86["BRA_attack_bolivia"]
        n87["BRA_disrupt_operation_bolivar"]
        n88["BRA_expand_operation_bolivar"]
        n89["BRA_foreign_legion"]
        n90["BRA_italian_car_industry"]
        n91["BRA_natal_naval_base"]
        n92["BRA_paraguay_intervention"]
        n93{"BRA_potenji_river_conference"}
        n94["BRA_smoking_cobras"]
        n95{"BRA_south_american_defense_cooperation"}
    end
    subgraph tier_12["Tier 12"]
        n96["BRA_attack_chile"]
        n97["BRA_german_subs"]
        n98["BRA_german_tanks"]
        n99["BRA_italian_aircraft"]
        n100["BRA_italian_trucks"]
        n101["BRA_provoke_argentina"]
        n102["BRA_senta_a_pua"]
        n103["BRA_south_american_research_cooperation"]
        n104["BRA_us_brazil_technology_exchange"]
    end
    subgraph tier_13["Tier 13"]
        n105["BRA_german_cooperation"]
        n106["BRA_italian_cooperation"]
        n107["BRA_panama_push"]
        n108["BRA_united_states_of_south_america"]
    end
    subgraph tier_14["Tier 14"]
        n109["BRA_unify_south_america"]
    end
    n146 --> n148
    n80 --> n86
    n92 --> n96
    n86 --> n96
    n149 --> n150
    n148 --> n150
    n149 --> n151
    n75 --> n76
    n161 --> n163
    n162 --> n163
    n143 --> n145
    n144 --> n145
    n168 --> n169
    n167 --> n169
    n73 --> n74
    n63 --> n74
    n148 --> n152
    n149 --> n152
    n154 --> n157
    n151 --> n157
    n75 --> n77
    n74 --> n78
    n150 --> n158
    n152 --> n158
    n152 --> n159
    n150 --> n159
    n148 --> n153
    n29 --> n165
    n78 --> n87
    n73 --> n75
    n27 --> n75
    n30 --> n143
    n149 --> n154
    n144 --> n146
    n145 --> n146
    n143 --> n147
    n145 --> n147
    n163 --> n27
    n76 --> n88
    n84 --> n88
    n154 --> n160
    n151 --> n160
    n83 --> n89
    n75 --> n79
    n98 --> n105
    n97 --> n105
    n88 --> n97
    n88 --> n98
    n75 --> n80
    n155 --> n161
    n153 --> n161
    n155 --> n162
    n153 --> n162
    n90 --> n99
    n84 --> n90
    n76 --> n90
    n100 --> n106
    n99 --> n106
    n90 --> n100
    n85 --> n91
    n74 --> n81
    n74 --> n82
    n101 --> n107
    n96 --> n107
    n80 --> n92
    n85 --> n93
    n86 --> n101
    n92 --> n101
    n74 --> n83
    n163 --> n166
    n148 --> n155
    n157 --> n29
    n160 --> n29
    n75 --> n84
    n29 --> n73
    n71 --> n73
    n91 --> n102
    n85 --> n94
    n83 --> n95
    n95 --> n103
    n168 --> n170
    n167 --> n170
    n29 --> n167
    n166 --> n167
    n29 --> n168
    n166 --> n168
    n159 --> n164
    n158 --> n164
    n147 --> n149
    n105 --> n109
    n106 --> n109
    n107 --> n109
    n104 --> n108
    n103 --> n108
    n148 --> n156
    n149 --> n156
    n93 --> n104
    n74 --> n85
    n30 --> n144
    n150 x--x n152
    n169 x--x n170
    n74 x--x n75
    n26 x--x n30
    n146 x--x n147
    n161 x--x n162
    n28 x--x n30
    n103 x--x n104
    n167 x--x n168
```
