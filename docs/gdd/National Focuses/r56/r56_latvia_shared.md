# LAT_VEF_radio_production

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"LAT_VEF_radio_production"}
        n2["LAT_rely_on_foreign_attaches"]
        n3["LAT_rethink_naval_doctrine"]
    end
    subgraph tier_1["Tier 1"]
        n4["LAT_VEF_airplanes_primacy"]
        n5["LAT_VEF_electronics_primacy"]
    end
    subgraph tier_2["Tier 2"]
        n6{"LAT_VEF_electronics_sideprojects"}
        n7["LAT_fighter_development"]
        n8["LAT_modernized_air_doctrine"]
    end
    subgraph tier_3["Tier 3"]
        n9["LAT_VEF_industrial_development"]
        n10["LAT_VEF_larger_planes"]
        n11["LAT_VEF_light_bombers"]
        n12["LAT_reinforce_the_navy_air_branch"]
        n13["LAT_trained_air_mechanics"]
    end
    subgraph tier_4["Tier 4"]
        n14["LAT_VEF_design_bombing_sights"]
        n15["LAT_VEF_modern_cameras"]
        n16["LAT_export_technical_experience"]
        n17["LAT_modernized_signal_corps"]
    end
    subgraph tier_5["Tier 5"]
        n18["LAT_VEF_radar_experiments"]
    end
    subgraph tier_6["Tier 6"]
        n19["LAT_VEF_technological_breakthrough"]
    end
    n1 --> n4
    n9 --> n14
    n10 --> n14
    n11 --> n14
    n1 --> n5
    n4 --> n6
    n7 --> n9
    n6 --> n9
    n6 --> n10
    n6 --> n11
    n7 --> n15
    n9 --> n15
    n15 --> n18
    n18 --> n19
    n14 --> n19
    n17 --> n19
    n13 --> n16
    n5 --> n7
    n4 --> n8
    n5 --> n8
    n2 --> n8
    n9 --> n17
    n3 --> n12
    n8 --> n12
    n8 --> n13
    n4 x--x n5
    n10 x--x n11
```

# LAT_rely_on_foreign_attaches

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20{"LAT_G_erenpreis_bicycle_factory"}
        n4["LAT_VEF_airplanes_primacy"]
        n5["LAT_VEF_electronics_primacy"]
        n2{"LAT_rely_on_foreign_attaches"}
        n21{"LAT_save_ford_vairogs"}
    end
    subgraph tier_1["Tier 1"]
        n22{"LAT_foreign_destroyer_contract"}
        n23{"LAT_foreign_submarine_contract"}
        n24{"LAT_general_modernization_plan"}
        n8["LAT_modernized_air_doctrine"]
        n25["LAT_new_generation_of_generals"]
        n26["LAT_study_foreign_firearm_prototypes"]
    end
    subgraph tier_2["Tier 2"]
        n27{"LAT_artillery_modernization"}
        n28["LAT_bicycle_infantry"]
        n29["LAT_draw_new_mobilization_plans"]
        n30["LAT_liepaja_naval_base"]
        n31["LAT_military_motorization_program"]
        n32["LAT_riga_shipyard"]
        n33["LAT_sellier_and_bellot_ammunitions"]
        n13["LAT_trained_air_mechanics"]
    end
    subgraph tier_3["Tier 3"]
        n34["LAT_anti_air_artillery"]
        n35["LAT_anti_tank_artillery"]
        n16["LAT_export_technical_experience"]
        n36["LAT_fortify_the_border"]
        n37["LAT_modern_infantry"]
        n38["LAT_national_tank_program"]
        n3{"LAT_rethink_naval_doctrine"}
    end
    subgraph tier_4["Tier 4"]
        n39["LAT_modernized_small_ships"]
        n12["LAT_reinforce_the_navy_air_branch"]
        n40["LAT_special_forces"]
        n41["LAT_submarine_strategy"]
    end
    subgraph tier_5["Tier 5"]
        n42["LAT_new_flagship"]
    end
    n27 --> n34
    n27 --> n35
    n24 --> n27
    n20 --> n28
    n24 --> n28
    n24 --> n29
    n13 --> n16
    n2 --> n22
    n2 --> n23
    n29 --> n36
    n2 --> n24
    n23 --> n30
    n22 --> n30
    n21 --> n31
    n24 --> n31
    n33 --> n37
    n4 --> n8
    n5 --> n8
    n2 --> n8
    n3 --> n39
    n28 --> n38
    n31 --> n38
    n41 --> n42
    n39 --> n42
    n2 --> n25
    n3 --> n12
    n8 --> n12
    n32 --> n3
    n30 --> n3
    n23 --> n32
    n22 --> n32
    n24 --> n33
    n29 --> n40
    n37 --> n40
    n2 --> n26
    n3 --> n41
    n8 --> n13
    n34 x--x n35
    n28 x--x n31
    n22 x--x n23
    n30 x--x n32
    n39 x--x n41
```

# LAT_revitalize_civilian_economy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n24{"LAT_general_modernization_plan"}
        n43(("LAT_revitalize_civilian_economy"))
    end
    subgraph tier_1["Tier 1"]
        n44["LAT_contact_foreign_industrial_partners"]
        n45["LAT_mobilize_the_banks"]
    end
    subgraph tier_2["Tier 2"]
        n46["LAT_kegums_power_plant"]
    end
    subgraph tier_3["Tier 3"]
        n47["LAT_devaluate_the_lats"]
    end
    subgraph tier_4["Tier 4"]
        n20{"LAT_G_erenpreis_bicycle_factory"}
        n48["LAT_increase_research_budget"]
        n21{"LAT_save_ford_vairogs"}
    end
    subgraph tier_5["Tier 5"]
        n28["LAT_bicycle_infantry"]
        n31["LAT_military_motorization_program"]
    end
    subgraph tier_6["Tier 6"]
        n38["LAT_national_tank_program"]
    end
    n47 --> n20
    n20 --> n28
    n24 --> n28
    n43 --> n44
    n46 --> n47
    n47 --> n48
    n44 --> n46
    n45 --> n46
    n21 --> n31
    n24 --> n31
    n43 --> n45
    n28 --> n38
    n31 --> n38
    n47 --> n21
    n28 x--x n31
```
