# COG_Support_the_congo_railways

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("COG_Support_the_congo_railways"))
    end
    subgraph tier_1["Tier 1"]
        n2["COG_congo_rubber"]
        n3["COG_support_copper_mining"]
        n4["COG_support_tungsten_mining"]
        n5["COG_transform_the_congo"]
    end
    subgraph tier_2["Tier 2"]
        n6["COG_congo_rubber2"]
        n7["COG_establish_radio_stations"]
        n8["COG_export_to_new_markets"]
        n9["COG_industrial_effort"]
        n10["COG_support_copper_mining2"]
        n11["COG_support_tungsten_mining2"]
    end
    subgraph tier_3["Tier 3"]
        n12["COG_congo_rubber3"]
        n13["COG_extra_tech_slot"]
        n14["COG_production_effort"]
        n15["COG_radio_divisional_support"]
        n16["COG_support_copper_mining3"]
        n17["COG_support_tungsten_mining3"]
        n18["COG_transform_the_congo2"]
        n19["COG_war_mining_production_directorate"]
    end
    subgraph tier_4["Tier 4"]
        n20["COG_congo_rubber4"]
        n21["COG_diamond_extraction"]
        n22["COG_extra_tech_slot_2"]
        n23["COG_further_nuclear_research"]
        n24["COG_gold_extraction"]
        n25["COG_production_effort_2"]
        n26["COG_support_copper_mining4"]
        n27["COG_support_tungsten_mining4"]
        n28["COG_transform_the_congo3"]
    end
    subgraph tier_5["Tier 5"]
        n29["COG_great_inga_dam"]
    end
    n1 --> n2
    n2 --> n6
    n6 --> n12
    n12 --> n20
    n19 --> n21
    n5 --> n7
    n5 --> n8
    n3 --> n8
    n4 --> n8
    n7 --> n13
    n13 --> n22
    n13 --> n23
    n19 --> n24
    n26 --> n29
    n27 --> n29
    n28 --> n29
    n5 --> n9
    n9 --> n14
    n14 --> n25
    n7 --> n15
    n1 --> n3
    n3 --> n10
    n10 --> n16
    n16 --> n26
    n1 --> n4
    n4 --> n11
    n11 --> n17
    n17 --> n27
    n1 --> n5
    n9 --> n18
    n18 --> n28
    n8 --> n19
```

# COG_colonial_autonomy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n30{"COG_colonial_autonomy"}
        n31{"COG_colonial_loyalty"}
    end
    subgraph tier_1["Tier 1"]
        n32["COG_affinity_fascism"]
        n33["COG_empower_congolese"]
    end
    subgraph tier_2["Tier 2"]
        n34["COG_affinity_new_order"]
        n35["COG_burn_royal_portraits"]
    end
    subgraph tier_3["Tier 3"]
        n36{"COG_independence"}
    end
    subgraph tier_4["Tier 4"]
        n37{"COG_doctrinal_marxism"}
        n38{"COG_manipulate_native_masses"}
    end
    subgraph tier_5["Tier 5"]
        n39["COG_african_diplomacy"]
        n40["COG_communist_army"]
        n41["COG_join_axis"]
        n42["COG_join_comintern"]
        n43["COG_join_italy"]
        n44["COG_masses_education"]
        n45["COG_mobilize_colonial_manpower"]
    end
    subgraph tier_6["Tier 6"]
        n46["COG_build_revolution"]
        n47["COG_colonial_claims"]
        n48["COG_german_scientists"]
        n49["COG_influence_liberia"]
        n50["COG_influence_south_africa"]
        n51["COG_italian_scientists"]
        n52["COG_political_commissars"]
        n53["COG_technology_sharing_communism"]
    end
    subgraph tier_7["Tier 7"]
        n54["COG_technology_sharing_fascism"]
    end
    n30 --> n32
    n32 --> n34
    n37 --> n39
    n44 --> n46
    n33 --> n35
    n45 --> n47
    n37 --> n40
    n36 --> n37
    n30 --> n33
    n31 --> n33
    n41 --> n48
    n34 --> n36
    n35 --> n36
    n39 --> n49
    n39 --> n50
    n43 --> n51
    n38 --> n41
    n37 --> n42
    n38 --> n43
    n36 --> n38
    n37 --> n44
    n38 --> n45
    n40 --> n52
    n39 --> n53
    n42 --> n53
    n51 --> n54
    n48 --> n54
    n32 x--x n33
    n39 x--x n42
    n30 x--x n31
    n37 x--x n38
    n41 x--x n43
```

# COG_colonial_loyalty

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n32["COG_affinity_fascism"]
        n34["COG_affinity_new_order"]
        n30{"COG_colonial_autonomy"}
        n31{"COG_colonial_loyalty"}
    end
    subgraph tier_1["Tier 1"]
        n33["COG_empower_congolese"]
        n55["COG_reinforce_colonial_government"]
    end
    subgraph tier_2["Tier 2"]
        n35["COG_burn_royal_portraits"]
        n56["COG_cracks_down_on_enemies"]
        n57["COG_increased_research_collaboration"]
    end
    subgraph tier_3["Tier 3"]
        n58["COG_colonial_defense_associations"]
        n36{"COG_independence"}
    end
    subgraph tier_4["Tier 4"]
        n59{"COG_commit_to_the_war"}
        n37{"COG_doctrinal_marxism"}
        n60{"COG_expand_force_publique_recruitment"}
        n38{"COG_manipulate_native_masses"}
    end
    subgraph tier_5["Tier 5"]
        n39["COG_african_diplomacy"]
        n40["COG_communist_army"]
        n61["COG_finance_planes_belgium"]
        n62["COG_finance_planes_britain"]
        n41["COG_join_axis"]
        n42["COG_join_comintern"]
        n43["COG_join_italy"]
        n44["COG_masses_education"]
        n63["COG_military_help"]
        n45["COG_mobilize_colonial_manpower"]
        n64["COG_technology_sharing"]
    end
    subgraph tier_6["Tier 6"]
        n46["COG_build_revolution"]
        n47["COG_colonial_claims"]
        n48["COG_german_scientists"]
        n49["COG_influence_liberia"]
        n50["COG_influence_south_africa"]
        n51["COG_italian_scientists"]
        n52["COG_political_commissars"]
        n53["COG_technology_sharing_communism"]
    end
    subgraph tier_7["Tier 7"]
        n54["COG_technology_sharing_fascism"]
    end
    n37 --> n39
    n44 --> n46
    n33 --> n35
    n45 --> n47
    n56 --> n58
    n58 --> n59
    n37 --> n40
    n55 --> n56
    n36 --> n37
    n30 --> n33
    n31 --> n33
    n58 --> n60
    n60 --> n61
    n59 --> n61
    n60 --> n62
    n59 --> n62
    n41 --> n48
    n55 --> n57
    n34 --> n36
    n35 --> n36
    n39 --> n49
    n39 --> n50
    n43 --> n51
    n38 --> n41
    n37 --> n42
    n38 --> n43
    n36 --> n38
    n37 --> n44
    n59 --> n63
    n38 --> n45
    n40 --> n52
    n31 --> n55
    n59 --> n64
    n57 --> n64
    n39 --> n53
    n42 --> n53
    n51 --> n54
    n48 --> n54
    n32 x--x n33
    n39 x--x n42
    n30 x--x n31
    n37 x--x n38
    n61 x--x n62
    n41 x--x n43
```

# COG_reform_the_force_publique

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n65(("COG_reform_the_force_publique"))
    end
    subgraph tier_1["Tier 1"]
        n66{"COG_air_force_congo"}
        n67["COG_get_rid_of_obsolete_rifles"]
        n68["COG_modernize_police_formation"]
        n69["COG_naval_effort"]
    end
    subgraph tier_2["Tier 2"]
        n70["COG_bomber_focus"]
        n71["COG_cruiser_effort"]
        n72["COG_engineers_corps"]
        n73["COG_fighter_focus"]
        n74["COG_modernize_tactics"]
        n75["COG_river_patrols"]
        n76["COG_submarine_experiments"]
    end
    subgraph tier_3["Tier 3"]
        n77["COG_capital_ships_effort"]
        n78["COG_continue_the_armament_modernization_program"]
        n79["COG_destroyer_effort"]
        n80["COG_fortify_congo_mouth"]
        n81["COG_large_navy"]
        n82["COG_long_range_fighters"]
        n83["COG_motorization_effort"]
        n84["COG_submarine_operations"]
    end
    subgraph tier_4["Tier 4"]
        n85["COG_finalize_the_equipment_modernization_program"]
        n86["COG_fleet_management"]
        n87["COG_fortify_cities"]
        n88["COG_motorised_support"]
        n89["COG_radar_system"]
        n90["COG_special_forces"]
    end
    subgraph tier_5["Tier 5"]
        n91["COG_CAS_effort"]
        n92["COG_NAV_effort"]
        n93["COG_commission_on_armored_vehicles"]
        n94["COG_jungle_training"]
        n95["COG_large_scale_exercises"]
    end
    subgraph tier_6["Tier 6"]
        n96["COG_aviation_effort_2"]
    end
    subgraph tier_7["Tier 7"]
        n97["COG_rocket_effort"]
    end
    n73 --> n91
    n70 --> n91
    n89 --> n91
    n73 --> n92
    n70 --> n92
    n89 --> n92
    n65 --> n66
    n82 --> n96
    n91 --> n96
    n92 --> n96
    n66 --> n70
    n71 --> n77
    n88 --> n93
    n85 --> n93
    n72 --> n78
    n69 --> n71
    n71 --> n79
    n67 --> n72
    n66 --> n73
    n78 --> n85
    n77 --> n86
    n79 --> n86
    n81 --> n86
    n80 --> n87
    n74 --> n80
    n65 --> n67
    n90 --> n94
    n71 --> n81
    n90 --> n95
    n70 --> n82
    n73 --> n82
    n65 --> n68
    n68 --> n74
    n83 --> n88
    n72 --> n83
    n65 --> n69
    n82 --> n89
    n68 --> n75
    n67 --> n75
    n96 --> n97
    n74 --> n90
    n75 --> n90
    n78 --> n90
    n69 --> n76
    n76 --> n84
    n70 x--x n73
```
