# PLY_UNIFIED_polynesian_unifacation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PLY_UNIFIED_polynesian_unifacation"))
    end
    subgraph tier_1["Tier 1"]
        n2["PLY_UNIFIED_connect_the_villages"]
        n3["PLY_UNIFIED_defend_our_union"]
        n4["PLY_UNIFIED_educational_reform"]
        n5["PLY_UNIFIED_exploit_resources"]
    end
    subgraph tier_2["Tier 2"]
        n6["PLY_UNIFIED_connect_the_islands"]
        n7["PLY_UNIFIED_exploit_the_fijian_goldmines"]
        n8["PLY_UNIFIED_exploit_the_nauruan_phosphate_mines"]
        n9["PLY_UNIFIED_first_steps_towards_modernisation"]
        n10["PLY_UNIFIED_united_armed_forces"]
    end
    subgraph tier_3["Tier 3"]
        n11["PLY_UNIFIED_develop_taiwan"]
        n12["PLY_UNIFIED_seize_japanese_assets"]
    end
    n2 --> n6
    n1 --> n2
    n1 --> n3
    n6 --> n11
    n9 --> n11
    n1 --> n4
    n1 --> n5
    n5 --> n7
    n5 --> n8
    n2 --> n9
    n9 --> n12
    n8 --> n12
    n3 --> n10
```

# PLY_agriculture_based_economy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13{"PLY_agriculture_based_economy"}
        n14["PLY_eradicate_the_threat_of_droughts"]
        n15["PLY_new_building_projects"]
        n16{"PLY_tourism_based_industry"}
    end
    subgraph tier_1["Tier 1"]
        n17["PLY_british_investment"]
        n18["PLY_expand_the_banana_platnations"]
        n19["PLY_expand_the_fishing_sector"]
        n20["PLY_japanese_investment"]
    end
    subgraph tier_2["Tier 2"]
        n21["PLY_anti_drought_measures"]
        n22["PLY_british_heavy_industry"]
        n23["PLY_japanese_heavy_industry"]
        n24["PLY_open_up_the_university_of_the_south_pacific"]
    end
    subgraph tier_3["Tier 3"]
        n25["PLY_develop_the_villages"]
        n26["PLY_purchase_foreign_licenses"]
    end
    subgraph tier_4["Tier 4"]
        n27["PLY_coastal_protection"]
        n28["PLY_exploit_our_resources"]
        n29["PLY_reform_taxes"]
    end
    subgraph tier_5["Tier 5"]
        n30["PLY_develop_port"]
        n31["PLY_free_trade"]
    end
    subgraph tier_6["Tier 6"]
        n32["PLY_industrial_boom"]
    end
    subgraph tier_7["Tier 7"]
        n33["PLY_modernize_railway_system"]
        n34["PLY_nation_wide_industrial_expansion"]
    end
    subgraph tier_8["Tier 8"]
        n35["PLY_modern_electronic_devices"]
    end
    subgraph tier_9["Tier 9"]
        n36["PLY_new_research_complex"]
    end
    subgraph tier_10["Tier 10"]
        n37["PLY_wrath_of_the_water_gods"]
    end
    n18 --> n21
    n19 --> n21
    n17 --> n22
    n13 --> n17
    n16 --> n17
    n25 --> n27
    n27 --> n30
    n14 --> n30
    n21 --> n25
    n13 --> n18
    n13 --> n19
    n25 --> n28
    n15 --> n31
    n27 --> n31
    n31 --> n32
    n30 --> n32
    n20 --> n23
    n13 --> n20
    n16 --> n20
    n33 --> n35
    n34 --> n35
    n32 --> n33
    n32 --> n34
    n35 --> n36
    n17 --> n24
    n20 --> n24
    n22 --> n26
    n23 --> n26
    n25 --> n29
    n36 --> n37
    n13 x--x n16
    n17 x--x n20
```

# PLY_build_airport

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n38(("PLY_build_airport"))
        n39["PLY_naval_academy"]
    end
    subgraph tier_1["Tier 1"]
        n40["PLY_the_air_fleet"]
    end
    subgraph tier_2["Tier 2"]
        n41["PLY_torpedo_bombers"]
    end
    n38 --> n40
    n39 --> n41
    n40 --> n41
```

# PLY_develop_our_dockyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n42(("PLY_develop_our_dockyards"))
        n43["PLY_special_forces"]
        n40["PLY_the_air_fleet"]
    end
    subgraph tier_1["Tier 1"]
        n44["PLY_develop_indigenous_models"]
        n39["PLY_naval_academy"]
    end
    subgraph tier_2["Tier 2"]
        n45["PLY_big_guns"]
        n46["PLY_recruit_marines"]
        n41["PLY_torpedo_bombers"]
    end
    n44 --> n45
    n42 --> n44
    n42 --> n39
    n39 --> n46
    n43 --> n46
    n39 --> n41
    n40 --> n41
```

# PLY_militarize_the_police_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n47(("PLY_militarize_the_police_force"))
        n39["PLY_naval_academy"]
    end
    subgraph tier_1["Tier 1"]
        n48["PLY_weaponry_modernization"]
    end
    subgraph tier_2["Tier 2"]
        n43["PLY_special_forces"]
        n49["PLY_the_polynesian_industrial_fund"]
    end
    subgraph tier_3["Tier 3"]
        n50["PLY_economic_mobilization"]
        n51["PLY_military_institute"]
        n46["PLY_recruit_marines"]
    end
    subgraph tier_4["Tier 4"]
        n52["PLY_encourage_local_arms_production"]
        n53["PLY_open_university"]
    end
    subgraph tier_5["Tier 5"]
        n54["PLY_introduce_motorization_technologies"]
        n55["PLY_resource_commission"]
        n56["PLY_the_roars_of_thunder"]
    end
    subgraph tier_6["Tier 6"]
        n57["PLY_the_steel_lions"]
    end
    n49 --> n50
    n50 --> n52
    n53 --> n54
    n43 --> n51
    n49 --> n51
    n51 --> n53
    n39 --> n46
    n43 --> n46
    n52 --> n55
    n48 --> n43
    n48 --> n49
    n53 --> n56
    n52 --> n56
    n54 --> n57
    n47 --> n48
```

# PLY_tourism_based_industry

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13{"PLY_agriculture_based_economy"}
        n27["PLY_coastal_protection"]
        n16{"PLY_tourism_based_industry"}
    end
    subgraph tier_1["Tier 1"]
        n17["PLY_british_investment"]
        n58["PLY_invite_foreign_workers"]
        n20["PLY_japanese_investment"]
    end
    subgraph tier_2["Tier 2"]
        n22["PLY_british_heavy_industry"]
        n59["PLY_infrastructure_works"]
        n23["PLY_japanese_heavy_industry"]
        n24["PLY_open_up_the_university_of_the_south_pacific"]
        n60["PLY_workshops"]
    end
    subgraph tier_3["Tier 3"]
        n61["PLY_a_paradise"]
        n26["PLY_purchase_foreign_licenses"]
    end
    subgraph tier_4["Tier 4"]
        n62["PLY_burn_the_forest"]
        n14["PLY_eradicate_the_threat_of_droughts"]
        n15["PLY_new_building_projects"]
    end
    subgraph tier_5["Tier 5"]
        n30["PLY_develop_port"]
        n31["PLY_free_trade"]
    end
    subgraph tier_6["Tier 6"]
        n32["PLY_industrial_boom"]
    end
    subgraph tier_7["Tier 7"]
        n33["PLY_modernize_railway_system"]
        n34["PLY_nation_wide_industrial_expansion"]
    end
    subgraph tier_8["Tier 8"]
        n35["PLY_modern_electronic_devices"]
    end
    subgraph tier_9["Tier 9"]
        n36["PLY_new_research_complex"]
    end
    subgraph tier_10["Tier 10"]
        n37["PLY_wrath_of_the_water_gods"]
    end
    n59 --> n61
    n60 --> n61
    n17 --> n22
    n13 --> n17
    n16 --> n17
    n61 --> n62
    n27 --> n30
    n14 --> n30
    n61 --> n14
    n15 --> n31
    n27 --> n31
    n31 --> n32
    n30 --> n32
    n58 --> n59
    n16 --> n58
    n20 --> n23
    n13 --> n20
    n16 --> n20
    n33 --> n35
    n34 --> n35
    n32 --> n33
    n32 --> n34
    n61 --> n15
    n35 --> n36
    n17 --> n24
    n20 --> n24
    n22 --> n26
    n23 --> n26
    n58 --> n60
    n36 --> n37
    n13 x--x n16
    n17 x--x n20
```
