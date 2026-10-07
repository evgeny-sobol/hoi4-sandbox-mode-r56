# ARG_air_force_reform

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"ARG_air_force_reform"}
        n2["ARG_carrier_modernization"]
    end
    subgraph tier_1["Tier 1"]
        n3["ARG_aviation_schools"]
        n4["ARG_bomber_modernization"]
        n5["ARG_cas_innovation"]
        n6["ARG_heavy_fighter_modernization"]
        n7["ARG_light_fighter_modernization"]
    end
    subgraph tier_2["Tier 2"]
        n8["ARG_air_base_dev"]
        n9["ARG_air_doctrine"]
        n10["ARG_air_innovations"]
    end
    subgraph tier_3["Tier 3"]
        n11["ARG_air_heroes"]
        n12["ARG_nav_innovation"]
    end
    n3 --> n8
    n3 --> n9
    n9 --> n11
    n3 --> n10
    n1 --> n3
    n1 --> n4
    n1 --> n5
    n1 --> n6
    n1 --> n7
    n2 --> n12
    n10 --> n12
    n4 x--x n5
    n6 x--x n7
```

# ARG_army_reform

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13{"ARG_army_reform"}
    end
    subgraph tier_1["Tier 1"]
        n14["ARG_external_advisors"]
        n15["ARG_military_academy"]
    end
    subgraph tier_2["Tier 2"]
        n16["ARG_artillery_modernization"]
        n17["ARG_motorized_army"]
        n18["ARG_new_officers_programme"]
        n19["ARG_study_foreign_equipment"]
    end
    subgraph tier_3["Tier 3"]
        n20["ARG_equipment_modernization"]
        n21["ARG_mechanized_experiments"]
        n22["ARG_specialized_artillery"]
        n23["ARG_study_foreign_tanks"]
        n24["ARG_volunteer_corps"]
    end
    subgraph tier_4["Tier 4"]
        n25["ARG_equipment_innovation"]
        n26["ARG_standarized_equipment"]
        n27{"ARG_tanks_modernization"}
    end
    subgraph tier_5["Tier 5"]
        n28["ARG_cruiser_tanks_experiments"]
        n29["ARG_heavy_tanks_experiments"]
        n30["ARG_special_forces"]
        n31["ARG_tanks_experiments"]
    end
    n14 --> n16
    n15 --> n16
    n27 --> n28
    n20 --> n25
    n19 --> n20
    n13 --> n14
    n27 --> n29
    n17 --> n21
    n13 --> n15
    n14 --> n17
    n15 --> n17
    n14 --> n18
    n15 --> n18
    n25 --> n30
    n16 --> n22
    n20 --> n26
    n14 --> n19
    n15 --> n19
    n17 --> n23
    n27 --> n31
    n23 --> n27
    n18 --> n24
    n28 x--x n29
    n14 x--x n15
```

# ARG_end_of_economic_depresion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n32(("ARG_end_of_economic_depresion"))
    end
    subgraph tier_1["Tier 1"]
        n33["ARG_establish_the_bcra"]
        n34["ARG_industrial_census"]
        n35["ARG_infrastructure_development"]
        n36["ARG_law_11729"]
        n37["ARG_mil_production_effort"]
    end
    subgraph tier_2["Tier 2"]
        n38["ARG_imports_substitution"]
        n39["ARG_infrastructure_development_2"]
        n40["ARG_inmigrant_wave"]
        n41["ARG_mil_production_effort_2"]
    end
    subgraph tier_3["Tier 3"]
        n42["ARG_barn_of_the_world"]
        n43["ARG_industrial_development"]
        n44["ARG_mil_production_effort_3"]
        n45["ARG_technological_initiative"]
    end
    subgraph tier_4["Tier 4"]
        n46["ARG_industrial_development_2"]
        n47["ARG_nuclear_committe"]
        n48["ARG_pioneers"]
        n49["ARG_proving_grounds"]
    end
    subgraph tier_5["Tier 5"]
        n50["ARG_balseiro_institute"]
        n51["ARG_industrial_development_3"]
        n52["ARG_secret_weapons"]
    end
    n47 --> n50
    n48 --> n50
    n38 --> n42
    n32 --> n33
    n34 --> n38
    n32 --> n34
    n38 --> n43
    n43 --> n46
    n46 --> n51
    n32 --> n35
    n35 --> n39
    n36 --> n40
    n32 --> n36
    n32 --> n37
    n37 --> n41
    n41 --> n44
    n45 --> n47
    n45 --> n48
    n44 --> n49
    n48 --> n52
    n47 --> n52
    n49 --> n52
    n39 --> n45
    n38 --> n45
    n41 --> n45
```

# ARG_infamous_decade

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n53{"ARG_infamous_decade"}
    end
    subgraph tier_1["Tier 1"]
        n54{"ARG_argentinas_destiny"}
        n55{"ARG_the_will_of_the_people_focus"}
    end
    subgraph tier_2["Tier 2"]
        n56["ARG_break_roca_runciman_treaty"]
        n57["ARG_land_of_the_worker"]
        n58{"ARG_liberty_focus"}
        n59{"ARG_nationalism"}
        n60["ARG_one_mind"]
    end
    subgraph tier_3["Tier 3"]
        n61{"ARG_external_help_focus"}
        n62["ARG_integrate_native_tribes"]
        n63["ARG_join_the_axis_r56"]
        n64["ARG_national_catholicism"]
        n65["ARG_national_fanatism"]
        n66["ARG_neutrality"]
        n67["ARG_political_correctness"]
        n68["ARG_south_americas_talks"]
        n69["ARG_spanish_civil_war_involvement"]
        n70["ARG_ussr_coop"]
    end
    subgraph tier_4["Tier 4"]
        n71["ARG_anti_war_treaty"]
        n72["ARG_brazil_coop"]
        n73["ARG_communist_secret_police"]
        n74["ARG_german_joint_military_operations"]
        n75["ARG_indoctrination_focus"]
        n76["ARG_join_the_holy_see"]
        n77["ARG_militarism"]
        n78["ARG_military_youth"]
        n79["ARG_political_repression"]
        n80["ARG_uk_coop"]
        n81["ARG_usa_coop"]
        n82["ARG_ussr_research_agreement"]
    end
    subgraph tier_5["Tier 5"]
        n83["ARG_anti_war_treaty_2"]
        n84["ARG_brazil_non_agression"]
        n85["ARG_claim_uruguay"]
        n86["ARG_eden_malbran_treaty"]
        n87["ARG_expand_the_intelligence_services"]
        n88["ARG_join_the_defense_of_the_hemisphere"]
        n89["ARG_malvinas_argentinas"]
        n90["ARG_paramilitarism"]
        n91{"ARG_political_commissars"}
        n92["ARG_usa_military_coop"]
        n93{"ARG_ussr_four_year_plan"}
    end
    subgraph tier_6["Tier 6"]
        n94["ARG_american_industrial_investments"]
        n95["ARG_american_oil_concern"]
        n96["ARG_anti_war_treaty_3"]
        n97["ARG_brazil_joint_exercises"]
        n98["ARG_demand_georgia"]
        n99["ARG_ideological_propaganda"]
        n100{"ARG_rallying_the_workers"}
        n101["ARG_red_army"]
        n102["ARG_uk_industrial_coop"]
        n103["ARG_uk_naval_coop"]
        n104["ARG_uruguay_ocupation"]
        n105["ARG_usa_technological_coop"]
    end
    subgraph tier_7["Tier 7"]
        n106["ARG_claim_chile"]
        n107["ARG_claim_paraguay"]
        n108["ARG_internationalism"]
        n109["ARG_join_the_allies_r56"]
        n110["ARG_join_the_comintern"]
        n111["ARG_la_patria_grande"]
    end
    subgraph tier_8["Tier 8"]
        n112["ARG_ask_for_georgia"]
        n113["ARG_ask_for_malvinas"]
        n114["ARG_claim_bolivia"]
        n115["ARG_occupy_paraguay"]
        n116["ARG_occupy_uruguay"]
    end
    subgraph tier_9["Tier 9"]
        n117["ARG_supremacy_over_brazil"]
    end
    n88 --> n94
    n88 --> n95
    n68 --> n71
    n71 --> n83
    n83 --> n96
    n53 --> n54
    n109 --> n112
    n109 --> n113
    n68 --> n72
    n84 --> n97
    n72 --> n84
    n54 --> n56
    n107 --> n114
    n104 --> n106
    n104 --> n107
    n77 --> n85
    n67 --> n73
    n89 --> n98
    n80 --> n86
    n73 --> n87
    n58 --> n61
    n63 --> n74
    n87 --> n99
    n67 --> n75
    n60 --> n62
    n91 --> n108
    n100 --> n108
    n102 --> n109
    n103 --> n109
    n59 --> n63
    n93 --> n110
    n100 --> n110
    n81 --> n88
    n64 --> n76
    n96 --> n111
    n54 --> n57
    n55 --> n58
    n77 --> n89
    n65 --> n77
    n63 --> n77
    n65 --> n78
    n59 --> n64
    n59 --> n65
    n54 --> n59
    n58 --> n66
    n108 --> n115
    n110 --> n115
    n108 --> n116
    n110 --> n116
    n55 --> n60
    n78 --> n90
    n75 --> n91
    n57 --> n67
    n66 --> n79
    n91 --> n100
    n93 --> n100
    n91 --> n101
    n60 --> n68
    n59 --> n69
    n57 --> n69
    n106 --> n117
    n114 --> n117
    n53 --> n55
    n61 --> n80
    n86 --> n102
    n86 --> n103
    n85 --> n104
    n61 --> n81
    n81 --> n92
    n92 --> n105
    n57 --> n70
    n82 --> n93
    n70 --> n82
    n54 x--x n55
    n61 x--x n66
    n108 x--x n110
    n63 x--x n65
    n57 x--x n59
    n58 x--x n60
    n80 x--x n81
```

# ARG_navy_reform

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10["ARG_air_innovations"]
        n118(("ARG_navy_reform"))
    end
    subgraph tier_1["Tier 1"]
        n119{"ARG_fleet_modernization"}
        n120["ARG_overseas_officer_training"]
        n121["ARG_state_dockyards"]
    end
    subgraph tier_2["Tier 2"]
        n122["ARG_capital_ships_development"]
        n123["ARG_carrier_development"]
        n124["ARG_naval_development_I"]
        n125["ARG_naval_exercises"]
        n126["ARG_screening_ships_modernization"]
        n127["ARG_submarines_modernization"]
    end
    subgraph tier_3["Tier 3"]
        n128["ARG_capital_ships_modernization"]
        n2["ARG_carrier_modernization"]
        n129["ARG_cruisers_modernization"]
        n130["ARG_submarines_experiments"]
    end
    subgraph tier_4["Tier 4"]
        n12["ARG_nav_innovation"]
        n131["ARG_naval_doctrine"]
    end
    n119 --> n122
    n122 --> n128
    n119 --> n123
    n123 --> n2
    n126 --> n129
    n118 --> n119
    n2 --> n12
    n10 --> n12
    n121 --> n124
    n129 --> n131
    n130 --> n131
    n128 --> n131
    n2 --> n131
    n120 --> n125
    n118 --> n120
    n119 --> n126
    n118 --> n121
    n127 --> n130
    n119 --> n127
    n122 x--x n123
    n126 x--x n127
```
