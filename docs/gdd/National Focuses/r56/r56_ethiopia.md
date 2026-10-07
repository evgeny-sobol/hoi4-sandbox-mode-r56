# ETH_black_lions

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ETH_black_lions"))
        n2["ETH_ferenghi"]
    end
    subgraph tier_1["Tier 1"]
        n3["ETH_regimental_system"]
    end
    subgraph tier_2["Tier 2"]
        n4["ETH_officer_schools"]
    end
    subgraph tier_3["Tier 3"]
        n5["ETH_harar_academy"]
    end
    subgraph tier_4["Tier 4"]
        n6["ETH_tank_refurbishment_plant"]
    end
    n4 --> n5
    n3 --> n4
    n1 --> n3
    n2 --> n3
    n5 --> n6
```

# ETH_christmas_offensive

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ETH_black_lions"]
        n7(("ETH_christmas_offensive"))
        n8["ETH_modern_technology"]
    end
    subgraph tier_1["Tier 1"]
        n9["ETH_national_mobilization"]
    end
    subgraph tier_2["Tier 2"]
        n10["ETH_homeland_defense"]
        n11["ETH_mountain_forts"]
        n12["ETH_plea_to_lon"]
    end
    subgraph tier_3["Tier 3"]
        n13["ETH_capital_forts"]
        n2{"ETH_ferenghi"}
        n14["ETH_hold_line"]
    end
    subgraph tier_4["Tier 4"]
        n15["ETH_addiba_university"]
        n16["ETH_ensure_the_church_support"]
        n17["ETH_german_equipment"]
        n18["ETH_japanese_assistance"]
        n19["ETH_rain_iron"]
        n3["ETH_regimental_system"]
    end
    subgraph tier_5["Tier 5"]
        n20["ETH_extra_research_slot_2"]
        n21["ETH_german_design"]
        n22{"ETH_japanese_navy_focus"}
        n4["ETH_officer_schools"]
    end
    subgraph tier_6["Tier 6"]
        n5["ETH_harar_academy"]
        n23["ETH_join_the_japanese"]
        n24["ETH_lion_roar"]
        n25["ETH_secure_seuz"]
        n26["ETH_silk_road_test"]
        n27["ETH_torpedoes_focus"]
    end
    subgraph tier_7["Tier 7"]
        n28{"ETH_demand_summit"}
        n29["ETH_expand_the_infrastructure"]
        n30{"ETH_steel_industry"}
        n6["ETH_tank_refurbishment_plant"]
    end
    subgraph tier_8["Tier 8"]
        n31["ETH_diplomatic_legitimacy"]
        n32["ETH_oil_industry"]
        n33["ETH_r56_rebuilding_the_country"]
        n34["ETH_rare_metals"]
    end
    subgraph tier_9["Tier 9"]
        n35["ETH_r56_reintegrate_aussa"]
    end
    subgraph tier_10["Tier 10"]
        n36["ETH_reclaim_aksum"]
    end
    subgraph tier_11["Tier 11"]
        n37["ETH_death_to_saudis"]
        n38["ETH_demand_british_somalia"]
        n39["ETH_demand_french_somalia"]
    end
    subgraph tier_12["Tier 12"]
        n40["ETH_demand_solomon_kingdom"]
    end
    n8 --> n15
    n2 --> n15
    n11 --> n13
    n36 --> n37
    n36 --> n38
    n36 --> n39
    n37 --> n40
    n38 --> n40
    n24 --> n28
    n28 --> n31
    n14 --> n16
    n26 --> n29
    n15 --> n20
    n12 --> n2
    n17 --> n21
    n2 --> n17
    n4 --> n5
    n10 --> n14
    n9 --> n10
    n2 --> n18
    n18 --> n22
    n22 --> n23
    n22 --> n24
    n21 --> n24
    n9 --> n11
    n7 --> n9
    n3 --> n4
    n30 --> n32
    n9 --> n12
    n28 --> n33
    n33 --> n35
    n13 --> n19
    n30 --> n34
    n35 --> n36
    n1 --> n3
    n2 --> n3
    n21 --> n25
    n20 --> n26
    n26 --> n30
    n5 --> n6
    n22 --> n27
    n31 x--x n23
    n17 x--x n18
    n32 x--x n34
```

# ETH_land_development

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["ETH_ferenghi"]
        n41(("ETH_land_development"))
        n42["ETH_mil_factory"]
    end
    subgraph tier_1["Tier 1"]
        n43["ETH_urban_factories"]
    end
    subgraph tier_2["Tier 2"]
        n8["ETH_modern_technology"]
    end
    subgraph tier_3["Tier 3"]
        n15["ETH_addiba_university"]
        n44["ETH_mil_factory2"]
    end
    subgraph tier_4["Tier 4"]
        n20["ETH_extra_research_slot_2"]
    end
    subgraph tier_5["Tier 5"]
        n26["ETH_silk_road_test"]
    end
    subgraph tier_6["Tier 6"]
        n29["ETH_expand_the_infrastructure"]
        n30{"ETH_steel_industry"}
    end
    subgraph tier_7["Tier 7"]
        n32["ETH_oil_industry"]
        n34["ETH_rare_metals"]
    end
    n8 --> n15
    n2 --> n15
    n26 --> n29
    n15 --> n20
    n42 --> n44
    n8 --> n44
    n43 --> n8
    n30 --> n32
    n30 --> n34
    n20 --> n26
    n26 --> n30
    n41 --> n43
    n32 x--x n34
```

# ETH_mil_factory

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n42(("ETH_mil_factory"))
        n8["ETH_modern_technology"]
    end
    subgraph tier_1["Tier 1"]
        n44["ETH_mil_factory2"]
    end
    n42 --> n44
    n8 --> n44
```

# ETH_modern_airforce

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n45(("ETH_modern_airforce"))
    end
    subgraph tier_1["Tier 1"]
        n46["ETH_airbase_eritea"]
        n47["ETH_airbase_somalia"]
    end
    subgraph tier_2["Tier 2"]
        n48["ETH_develop_airforce"]
    end
    n45 --> n46
    n45 --> n47
    n47 --> n48
    n46 --> n48
```

# ETH_red_sea_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n49(("ETH_red_sea_focus"))
    end
    subgraph tier_1["Tier 1"]
        n50["ETH_develop_eritrea"]
        n51["ETH_develop_somalia"]
    end
    subgraph tier_2["Tier 2"]
        n52["ETH_fortify_eritrea"]
        n53["ETH_fortify_somalia"]
    end
    subgraph tier_3["Tier 3"]
        n54{"ETH_modern_navy"}
    end
    subgraph tier_4["Tier 4"]
        n55["ETH_amphibious_operations"]
        n56["ETH_battleship_primacy"]
        n57["ETH_carrier_primacy"]
    end
    n54 --> n55
    n54 --> n56
    n54 --> n57
    n49 --> n50
    n49 --> n51
    n50 --> n52
    n51 --> n53
    n53 --> n54
    n52 --> n54
    n56 x--x n57
```
