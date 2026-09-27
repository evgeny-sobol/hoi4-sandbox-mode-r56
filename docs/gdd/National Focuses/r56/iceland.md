# ICE_expand_the_fishing_industry

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ICE_expand_the_fishing_industry"))
        n2["ICE_mineral_prospecting"]
    end
    subgraph tier_1["Tier 1"]
        n3["ICE_agricultural_expansion"]
        n4{"ICE_hydroelectric_power"}
    end
    subgraph tier_2["Tier 2"]
        n5["ICE_advanced_technology"]
        n6["ICE_develop_icelandic_shipping"]
        n7["ICE_heavy_industry"]
    end
    subgraph tier_3["Tier 3"]
        n8["ICE_expand_the_harbour"]
        n9["ICE_iceland_air"]
        n10["ICE_infrastructure_development"]
        n11["ICE_local_arms_industry"]
        n12["ICE_reykjavik_dockyards"]
    end
    subgraph tier_4["Tier 4"]
        n13["ICE_expand_the_civilian_fleet"]
        n14["ICE_hrafninn_flygur"]
        n15["ICE_industrial_research_school"]
    end
    subgraph tier_5["Tier 5"]
        n16["ICE_geothermic_banana_production"]
    end
    n4 --> n5
    n1 --> n3
    n4 --> n6
    n12 --> n13
    n6 --> n8
    n7 --> n8
    n15 --> n16
    n4 --> n7
    n9 --> n14
    n1 --> n4
    n2 --> n4
    n5 --> n9
    n11 --> n15
    n12 --> n15
    n9 --> n15
    n7 --> n10
    n5 --> n10
    n7 --> n11
    n6 --> n12
    n5 x--x n6
    n5 x--x n7
    n6 x--x n7
    n1 x--x n2
```

# ICE_international_trade

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17(("ICE_international_trade"))
    end
    subgraph tier_1["Tier 1"]
        n18["ICE_banking_on_the_future"]
    end
    subgraph tier_2["Tier 2"]
        n19["ICE_infiltration"]
    end
    n17 --> n18
    n18 --> n19
```

# ICE_mineral_prospecting

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ICE_expand_the_fishing_industry"]
        n2(("ICE_mineral_prospecting"))
    end
    subgraph tier_1["Tier 1"]
        n4{"ICE_hydroelectric_power"}
        n20["ICE_off_shore_oil_drilling"]
    end
    subgraph tier_2["Tier 2"]
        n5["ICE_advanced_technology"]
        n6["ICE_develop_icelandic_shipping"]
        n7["ICE_heavy_industry"]
    end
    subgraph tier_3["Tier 3"]
        n8["ICE_expand_the_harbour"]
        n9["ICE_iceland_air"]
        n10["ICE_infrastructure_development"]
        n11["ICE_local_arms_industry"]
        n12["ICE_reykjavik_dockyards"]
    end
    subgraph tier_4["Tier 4"]
        n13["ICE_expand_the_civilian_fleet"]
        n14["ICE_hrafninn_flygur"]
        n15["ICE_industrial_research_school"]
    end
    subgraph tier_5["Tier 5"]
        n16["ICE_geothermic_banana_production"]
    end
    n4 --> n5
    n4 --> n6
    n12 --> n13
    n6 --> n8
    n7 --> n8
    n15 --> n16
    n4 --> n7
    n9 --> n14
    n1 --> n4
    n2 --> n4
    n5 --> n9
    n11 --> n15
    n12 --> n15
    n9 --> n15
    n7 --> n10
    n5 --> n10
    n7 --> n11
    n2 --> n20
    n6 --> n12
    n5 x--x n6
    n5 x--x n7
    n6 x--x n7
    n1 x--x n2
```

# ICE_not_our_king

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n21(("ICE_not_our_king"))
        n22["ICE_the_kingdom_of_iceland"]
    end
    subgraph tier_1["Tier 1"]
        n23["ICE_anti_capitalist_propaganda"]
        n24["ICE_expand_the_industrial_base"]
    end
    subgraph tier_2["Tier 2"]
        n25["ICE_international_relations"]
        n26["ICE_prepare_for_the_revolution"]
        n27["ICE_rally_the_workers_of_reykjavik"]
        n28["ICE_state_visits"]
    end
    subgraph tier_3["Tier 3"]
        n29["ICE_general_strike"]
        n30["ICE_organize_a_march"]
    end
    subgraph tier_4["Tier 4"]
        n31{"ICE_break_with_the_crown"}
    end
    subgraph tier_5["Tier 5"]
        n32["ICE_embrace_the_workers_revolution"]
        n33["ICE_state_corporatism"]
    end
    subgraph tier_6["Tier 6"]
        n34["ICE_international_brigades"]
        n35["ICE_organize_the_greyshirts"]
        n36["ICE_research_cooperation"]
        n37["ICE_state_owned_industry"]
    end
    subgraph tier_7["Tier 7"]
        n38["ICE_infiltrating_the_british_isles"]
        n39["ICE_the_viking_spirit"]
        n40["ICE_transformation_of_nature"]
    end
    subgraph tier_8["Tier 8"]
        n41["ICE_international_research_community"]
        n42["ICE_reclaiming_the_empire"]
        n43["ICE_recruiting_international_workers"]
        n44["ICE_securing_the_north_sea_passage"]
    end
    subgraph tier_9["Tier 9"]
        n45["ICE_vinland"]
    end
    n21 --> n23
    n29 --> n31
    n30 --> n31
    n31 --> n32
    n21 --> n24
    n27 --> n29
    n34 --> n38
    n32 --> n34
    n25 --> n34
    n24 --> n25
    n40 --> n41
    n26 --> n30
    n33 --> n35
    n23 --> n26
    n24 --> n27
    n39 --> n42
    n40 --> n43
    n38 --> n43
    n33 --> n36
    n28 --> n36
    n39 --> n44
    n31 --> n33
    n32 --> n37
    n23 --> n28
    n35 --> n39
    n37 --> n40
    n42 --> n45
    n44 --> n45
    n32 x--x n33
    n21 x--x n22
```

# ICE_the_armed_forces_of_iceland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46{"ICE_the_armed_forces_of_iceland"}
    end
    subgraph tier_1["Tier 1"]
        n47["ICE_a_naval_hub_in_the_atlantic"]
        n48["ICE_an_airbase_in_the_sea"]
    end
    subgraph tier_2["Tier 2"]
        n49["ICE_flying_boats"]
        n50["ICE_mine_iceland"]
        n51["ICE_modernizing_the_coast_guard"]
    end
    subgraph tier_3["Tier 3"]
        n52["ICE_emergency_conversions"]
        n53["ICE_low_cost_aircrafts"]
        n54{"ICE_support_equipment"}
    end
    subgraph tier_4["Tier 4"]
        n55["ICE_a_profesional_army"]
        n56["ICE_enact_conscription"]
    end
    subgraph tier_5["Tier 5"]
        n57["ICE_civilian_war_duty"]
        n58["ICE_doctrinal_studies"]
        n59{"ICE_thungur_hnifur"}
    end
    subgraph tier_6["Tier 6"]
        n60["ICE_death_from_above"]
        n61["ICE_taking_the_fight_to_our_enemies"]
        n62["ICE_we_shall_defend_our_island"]
    end
    n46 --> n47
    n54 --> n55
    n46 --> n48
    n56 --> n57
    n59 --> n60
    n55 --> n58
    n50 --> n52
    n51 --> n52
    n54 --> n56
    n48 --> n49
    n49 --> n53
    n51 --> n53
    n47 --> n50
    n48 --> n51
    n47 --> n51
    n51 --> n54
    n59 --> n61
    n55 --> n59
    n56 --> n59
    n59 --> n62
    n47 x--x n48
    n55 x--x n56
    n60 x--x n61
    n60 x--x n62
    n61 x--x n62
```

# ICE_the_kingdom_of_iceland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n21["ICE_not_our_king"]
        n22{"ICE_the_kingdom_of_iceland"}
    end
    subgraph tier_1["Tier 1"]
        n63["ICE_declare_absolute_neutrality"]
        n64["ICE_united_we_stand"]
    end
    subgraph tier_2["Tier 2"]
        n65["ICE_engineering_projects"]
        n66["ICE_infrastructure_projects"]
        n67["ICE_joint_shipbuilding_programme"]
        n68["ICE_royal_marines"]
        n69["ICE_the_icelandic_police_force"]
    end
    subgraph tier_3["Tier 3"]
        n70["ICE_gardhur_airfield"]
        n71["ICE_joint_military_training"]
        n72["ICE_patrolling_the_atlantic"]
        n73["ICE_the_merchant_fleet"]
    end
    subgraph tier_4["Tier 4"]
        n74["ICE_anglo_icelandic_relations"]
        n75["ICE_expand_industrial_complexes"]
        n76["ICE_industrial_cooperation"]
        n77["ICE_not_standing_idly_by"]
        n78["ICE_political_unity"]
    end
    subgraph tier_5["Tier 5"]
        n79["ICE_american_protection"]
        n80["ICE_expanding_the_university_of_reykjavik"]
        n81["ICE_fighting_as_equals"]
        n82["ICE_trade_relations"]
    end
    subgraph tier_6["Tier 6"]
        n83["ICE_compensation"]
        n84["ICE_keflavik_airbase"]
        n85["ICE_modernizing_the_island"]
        n86["ICE_republicanism"]
    end
    subgraph tier_7["Tier 7"]
        n87["ICE_american_investments"]
        n88["ICE_state_owned_enterprises"]
    end
    subgraph tier_8["Tier 8"]
        n89["ICE_american_soldiers"]
    end
    subgraph tier_9["Tier 9"]
        n90["ICE_iceland_defense_force"]
    end
    n84 --> n87
    n78 --> n79
    n87 --> n89
    n73 --> n74
    n81 --> n83
    n22 --> n63
    n63 --> n65
    n70 --> n75
    n73 --> n75
    n71 --> n75
    n72 --> n75
    n77 --> n80
    n78 --> n80
    n77 --> n81
    n66 --> n70
    n89 --> n90
    n72 --> n76
    n63 --> n66
    n68 --> n71
    n64 --> n67
    n79 --> n84
    n80 --> n85
    n71 --> n77
    n72 --> n77
    n67 --> n72
    n70 --> n78
    n73 --> n78
    n82 --> n86
    n64 --> n68
    n85 --> n88
    n64 --> n69
    n63 --> n69
    n65 --> n73
    n78 --> n82
    n22 --> n64
    n63 x--x n64
    n21 x--x n22
```
