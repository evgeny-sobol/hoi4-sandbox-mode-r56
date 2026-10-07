# POR_army_reorganization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("POR_army_reorganization"))
    end
    subgraph tier_1["Tier 1"]
        n2["POR_corpo_do_estado_maior"]
        n3["POR_metropolitan_army"]
    end
    subgraph tier_2["Tier 2"]
        n4["POR_staff_wargames"]
        n5{"POR_standardization"}
    end
    subgraph tier_3["Tier 3"]
        n6["POR_defend_the_borders"]
        n7["POR_elastic_defense"]
        n8["POR_field_maneuvers"]
    end
    subgraph tier_4["Tier 4"]
        n9["POR_tropas_paraquedistas"]
    end
    subgraph tier_5["Tier 5"]
        n10["POR_regimento_de_comandos"]
    end
    n1 --> n2
    n5 --> n6
    n5 --> n7
    n4 --> n8
    n1 --> n3
    n9 --> n10
    n2 --> n4
    n3 --> n5
    n6 --> n9
    n7 --> n9
    n6 x--x n7
```

# POR_colonial_assimilation_policy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n11{"POR_colonial_assimilation_policy"}
        n12["POR_roads_bridges_and_dams"]
    end
    subgraph tier_1["Tier 1"]
        n13{"POR_colonial_army"}
        n14["POR_haven_of_neutrality_macau"]
        n15["POR_infrastructure_in_angola"]
        n16["POR_luso_tropicalism"]
        n17{"POR_restart_investment_into_timor"}
    end
    subgraph tier_2["Tier 2"]
        n18["POR_develop_north_angola"]
        n19["POR_invest_in_sandalwood_and_coffee_production"]
        n20["POR_limited_self_rule"]
        n21["POR_revert_the_local_autonomy_policies"]
    end
    subgraph tier_3["Tier 3"]
        n22["POR_develop_south_angola"]
    end
    subgraph tier_4["Tier 4"]
        n23["POR_develop_mozambique"]
        n24["POR_portuguese_oil"]
    end
    n11 --> n13
    n22 --> n23
    n15 --> n18
    n12 --> n18
    n18 --> n22
    n11 --> n14
    n11 --> n15
    n17 --> n19
    n13 --> n20
    n11 --> n16
    n22 --> n24
    n11 --> n17
    n17 --> n21
    n19 x--x n21
    n20 x--x n16
```

# POR_continue_the_public_works

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25{"POR_continue_the_public_works"}
        n15["POR_infrastructure_in_angola"]
        n26["POR_naval_research_institute"]
    end
    subgraph tier_1["Tier 1"]
        n27["POR_food_industries"]
        n28{"POR_instituto_superior_tecnico"}
    end
    subgraph tier_2["Tier 2"]
        n29["POR_industrial_modernization"]
        n30["POR_ogma"]
        n31["POR_ogme"]
        n12["POR_roads_bridges_and_dams"]
        n32["POR_textile_industry"]
    end
    subgraph tier_3["Tier 3"]
        n33["POR_a_new_industry"]
        n18["POR_develop_north_angola"]
        n34["POR_extraction_industries"]
        n35{"POR_light_aircraft_focus"}
        n36["POR_military_vehicles"]
        n37["POR_portuguese_artillery"]
    end
    subgraph tier_4["Tier 4"]
        n38["POR_advanced_light_aircraft"]
        n22["POR_develop_south_angola"]
        n39["POR_hydroelectricity"]
        n40{"POR_military_research_facilities"}
    end
    subgraph tier_5["Tier 5"]
        n41["POR_advanced_artillery"]
        n42["POR_air_naval_research"]
        n43["POR_armor_focus"]
        n23["POR_develop_mozambique"]
        n44["POR_jet_research"]
        n24["POR_portuguese_oil"]
    end
    subgraph tier_6["Tier 6"]
        n45["POR_mechanized_focus"]
    end
    n29 --> n33
    n37 --> n41
    n40 --> n41
    n35 --> n38
    n26 --> n42
    n38 --> n42
    n40 --> n43
    n22 --> n23
    n15 --> n18
    n12 --> n18
    n18 --> n22
    n12 --> n34
    n25 --> n27
    n34 --> n39
    n28 --> n29
    n25 --> n28
    n38 --> n44
    n30 --> n35
    n43 --> n45
    n36 --> n40
    n37 --> n40
    n35 --> n40
    n31 --> n36
    n28 --> n30
    n28 --> n31
    n31 --> n37
    n22 --> n24
    n28 --> n12
    n27 --> n32
    n38 x--x n43
    n27 x--x n29
```

# POR_estado_novo

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46{"POR_estado_novo"}
        n47{"POR_popular_front"}
        n48["POR_support_the_spanish_republic"]
        n49["POR_the_popular_front_bloc"]
        n50["POR_they_need_our_help"]
        n51["POR_visit_the_front"]
    end
    subgraph tier_1["Tier 1"]
        n52["POR_a_royal_wedding"]
        n53["POR_strict_neutrality_in_the_spanish_civil_war"]
        n54["POR_support_the_spanish_nationalists"]
    end
    subgraph tier_2["Tier 2"]
        n55["POR_british_guns"]
        n56["POR_british_investment_in_mines"]
        n57{"POR_portuguese_legion"}
        n58["POR_the_return_of_duarte"]
    end
    subgraph tier_3["Tier 3"]
        n59["POR_british_industrial_investments"]
        n60["POR_monarchist_uprising_in_brazil"]
        n61["POR_national_syndicalism"]
        n62["POR_observation_mission"]
        n63["POR_promote_the_monarchist_cause_in_portugal"]
        n64["POR_strengthen_the_regime"]
        n65["POR_support_a_spanish_monarchy_in_the_war"]
    end
    subgraph tier_4["Tier 4"]
        n66{"POR_allow_free_elections"}
        n67["POR_appease_monarchists"]
        n68["POR_assist_the_requetes"]
        n69["POR_ditadura_militar"]
        n70["POR_refuse_the_naval_blockade"]
        n71{"POR_restoration_of_the_monarchy"}
        n72{"POR_send_assistance"}
        n73["POR_the_capital_of_espionage"]
        n74{"POR_the_empire_of_brazil"}
    end
    subgraph tier_5["Tier 5"]
        n75{"POR_camisas_azuis"}
        n76{"POR_concordat_with_the_holy_see"}
        n77["POR_iberian_summit"]
        n78["POR_intervention_in_spain"]
        n79["POR_join_the_allies"]
        n80{"POR_join_the_carlist_fight"}
        n81["POR_luso_monarchist_cooperation"]
        n82{"POR_mapa_cor_de_rosa"}
        n83{"POR_national_gold_reserves"}
        n84["POR_nationalist_intervention"]
        n85["POR_protect_chinese_civilians"]
        n86["POR_remember_olivenca"]
        n87["POR_securing_the_free_world"]
        n88["POR_the_kingdom_reunited"]
    end
    subgraph tier_6["Tier 6"]
        n89["POR_honor_anglo_portuguese_alliance"]
        n90["POR_join_the_axis"]
        n91["POR_luso_imperial_and_royal_armies"]
        n92["POR_proudly_alone"]
        n93["POR_recover_brazil"]
        n94["POR_recover_the_east_indies"]
        n95["POR_the_fifth_empire"]
        n96["POR_the_royal_iberian_alliance"]
    end
    subgraph tier_7["Tier 7"]
        n97["POR_deal_with_fascism"]
        n98["POR_deal_with_the_japanese_threat"]
        n99["POR_expand_the_chinese_territories"]
        n100["POR_invite_andorra"]
        n101["POR_latin_america"]
        n102["POR_oppose_germany"]
        n103["POR_research_agreements"]
        n104["POR_research_sharing"]
        n105["POR_the_eastern_menace"]
    end
    subgraph tier_8["Tier 8"]
        n106["POR_the_communist_threat"]
    end
    n46 --> n52
    n59 --> n66
    n64 --> n67
    n65 --> n68
    n53 --> n55
    n56 --> n59
    n55 --> n59
    n51 --> n59
    n53 --> n56
    n69 --> n75
    n67 --> n76
    n86 --> n97
    n96 --> n97
    n95 --> n98
    n94 --> n98
    n61 --> n69
    n90 --> n99
    n95 --> n99
    n76 --> n89
    n66 --> n77
    n72 --> n77
    n50 --> n78
    n66 --> n78
    n96 --> n100
    n66 --> n79
    n75 --> n90
    n68 --> n80
    n88 --> n101
    n93 --> n101
    n81 --> n91
    n71 --> n81
    n74 --> n81
    n70 --> n82
    n58 --> n60
    n67 --> n83
    n57 --> n61
    n72 --> n84
    n57 --> n62
    n79 --> n102
    n89 --> n102
    n54 --> n57
    n58 --> n63
    n50 --> n85
    n66 --> n85
    n49 --> n85
    n83 --> n92
    n76 --> n92
    n82 --> n93
    n82 --> n94
    n61 --> n70
    n58 --> n70
    n71 --> n86
    n90 --> n103
    n79 --> n104
    n89 --> n104
    n63 --> n71
    n66 --> n87
    n62 --> n72
    n57 --> n64
    n47 --> n53
    n46 --> n53
    n58 --> n65
    n46 --> n54
    n64 --> n73
    n101 --> n106
    n92 --> n106
    n92 --> n105
    n60 --> n74
    n75 --> n95
    n71 --> n88
    n74 --> n88
    n52 --> n58
    n80 --> n96
    n52 x--x n53
    n52 x--x n54
    n52 x--x n48
    n46 x--x n47
    n89 x--x n92
    n77 x--x n84
    n90 x--x n95
    n81 x--x n93
    n81 x--x n88
    n61 x--x n64
    n93 x--x n88
    n86 x--x n96
    n53 x--x n54
    n53 x--x n48
    n54 x--x n48
```

# POR_popular_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n52["POR_a_royal_wedding"]
        n46{"POR_estado_novo"}
        n89["POR_honor_anglo_portuguese_alliance"]
        n84["POR_nationalist_intervention"]
        n47{"POR_popular_front"}
        n72{"POR_send_assistance"}
        n54["POR_support_the_spanish_nationalists"]
    end
    subgraph tier_1["Tier 1"]
        n107["POR_nation_in_arms"]
        n53["POR_strict_neutrality_in_the_spanish_civil_war"]
        n48{"POR_support_the_spanish_republic"}
    end
    subgraph tier_2["Tier 2"]
        n55["POR_british_guns"]
        n56["POR_british_investment_in_mines"]
        n108["POR_nationalize_industry"]
        n109["POR_unify_leftist_youth_wings"]
        n51["POR_visit_the_front"]
        n110["POR_workers_of_iberia_unite"]
    end
    subgraph tier_3["Tier 3"]
        n59["POR_british_industrial_investments"]
        n111{"POR_reorganization_of_the_communist_party"}
        n112{"POR_the_iberian_socialist_union"}
        n50["POR_they_need_our_help"]
    end
    subgraph tier_4["Tier 4"]
        n113["POR_align_against_the_comintern"]
        n66{"POR_allow_free_elections"}
        n114["POR_communist_secret_police"]
        n115["POR_join_the_comintern"]
        n49["POR_the_popular_front_bloc"]
    end
    subgraph tier_5["Tier 5"]
        n116["POR_cooperate_with_french_militants"]
        n117["POR_expand_the_intelligence_services"]
        n77["POR_iberian_summit"]
        n78["POR_intervention_in_spain"]
        n79["POR_join_the_allies"]
        n118["POR_latin_american_communism"]
        n85["POR_protect_chinese_civilians"]
        n119["POR_research_collaboration"]
        n87["POR_securing_the_free_world"]
    end
    subgraph tier_6["Tier 6"]
        n120["POR_anti_fascism"]
        n102["POR_oppose_germany"]
        n121["POR_our_comrades_overseas"]
        n104["POR_research_sharing"]
    end
    n112 --> n113
    n59 --> n66
    n116 --> n120
    n53 --> n55
    n56 --> n59
    n55 --> n59
    n51 --> n59
    n53 --> n56
    n111 --> n114
    n115 --> n116
    n49 --> n116
    n113 --> n116
    n114 --> n117
    n66 --> n77
    n72 --> n77
    n50 --> n78
    n66 --> n78
    n66 --> n79
    n111 --> n115
    n49 --> n118
    n47 --> n107
    n107 --> n108
    n79 --> n102
    n89 --> n102
    n118 --> n121
    n50 --> n85
    n66 --> n85
    n49 --> n85
    n108 --> n111
    n109 --> n111
    n115 --> n119
    n79 --> n104
    n89 --> n104
    n66 --> n87
    n47 --> n53
    n46 --> n53
    n47 --> n48
    n110 --> n112
    n112 --> n49
    n51 --> n50
    n107 --> n109
    n48 --> n51
    n48 --> n110
    n52 x--x n53
    n52 x--x n48
    n113 x--x n115
    n113 x--x n49
    n46 x--x n47
    n77 x--x n84
    n115 x--x n49
    n53 x--x n54
    n53 x--x n48
    n54 x--x n48
    n51 x--x n110
```

# POR_second_navy_reequipment

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n38["POR_advanced_light_aircraft"]
        n122(("POR_second_navy_reequipment"))
    end
    subgraph tier_1["Tier 1"]
        n123["POR_a_powerful_merchant_marine"]
        n124["POR_arsenal_do_alfeite"]
        n125["POR_submarine_effort"]
    end
    subgraph tier_2["Tier 2"]
        n126["POR_merchant_marine_protection"]
        n127["POR_national_cruiser_production"]
    end
    subgraph tier_3["Tier 3"]
        n128["POR_atlantic_defense_strategy"]
        n129["POR_battleship_effort"]
        n130["POR_carrier_effort"]
        n131["POR_fuzileiros"]
    end
    subgraph tier_4["Tier 4"]
        n132["POR_endless_sea"]
        n26["POR_naval_research_institute"]
    end
    subgraph tier_5["Tier 5"]
        n42["POR_air_naval_research"]
    end
    n122 --> n123
    n26 --> n42
    n38 --> n42
    n122 --> n124
    n127 --> n128
    n127 --> n129
    n127 --> n130
    n128 --> n132
    n125 --> n131
    n126 --> n131
    n123 --> n126
    n124 --> n127
    n131 --> n26
    n122 --> n125
```
