# CYP_begin_urbanisation_efforts

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CYP_begin_urbanisation_efforts"))
        n2["CYP_continue_farming_reliance"]
        n3["CYP_rural_infrastructure"]
        n4["CYP_subsidise_fruit_farming"]
    end
    subgraph tier_1["Tier 1"]
        n5{"CYP_coastal_investments"}
        n6["CYP_railways"]
        n7{"CYP_urban_investments"}
    end
    subgraph tier_2["Tier 2"]
        n8["CYP_construct_argaka_dam"]
        n9["CYP_construct_power_plants"]
        n10["CYP_link_the_cities"]
        n11["CYP_national_industries"]
        n12["CYP_natural_build_up"]
        n13["CYP_water_infrastructure"]
    end
    subgraph tier_3["Tier 3"]
        n14["CYP_develop_heavy_industry"]
        n15["CYP_trade_port"]
        n16["CYP_utilise_stengths"]
    end
    subgraph tier_4["Tier 4"]
        n17["CYP_research_sector"]
        n18["CYP_trade_economy"]
    end
    n1 --> n5
    n2 --> n5
    n6 --> n8
    n6 --> n9
    n11 --> n14
    n12 --> n14
    n6 --> n10
    n7 --> n10
    n7 --> n11
    n7 --> n12
    n5 --> n12
    n1 --> n6
    n9 --> n17
    n14 --> n17
    n15 --> n18
    n11 --> n15
    n12 --> n15
    n1 --> n7
    n13 --> n16
    n3 --> n16
    n4 --> n13
    n5 --> n13
    n1 x--x n2
    n11 x--x n12
```

# CYP_continue_farming_reliance

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["CYP_begin_urbanisation_efforts"]
        n9["CYP_construct_power_plants"]
        n2(("CYP_continue_farming_reliance"))
        n11["CYP_national_industries"]
        n7{"CYP_urban_investments"}
    end
    subgraph tier_1["Tier 1"]
        n5{"CYP_coastal_investments"}
        n19["CYP_mining_effort"]
        n4["CYP_subsidise_fruit_farming"]
    end
    subgraph tier_2["Tier 2"]
        n12["CYP_natural_build_up"]
        n20["CYP_resource_prospecting"]
        n3["CYP_rural_infrastructure"]
        n13["CYP_water_infrastructure"]
    end
    subgraph tier_3["Tier 3"]
        n14["CYP_develop_heavy_industry"]
        n21["CYP_education_effort"]
        n15["CYP_trade_port"]
        n16["CYP_utilise_stengths"]
    end
    subgraph tier_4["Tier 4"]
        n22["CYP_educated_nation"]
        n17["CYP_research_sector"]
        n18["CYP_trade_economy"]
    end
    n1 --> n5
    n2 --> n5
    n11 --> n14
    n12 --> n14
    n21 --> n22
    n3 --> n21
    n20 --> n21
    n2 --> n19
    n7 --> n12
    n5 --> n12
    n9 --> n17
    n14 --> n17
    n19 --> n20
    n4 --> n3
    n19 --> n3
    n2 --> n4
    n15 --> n18
    n11 --> n15
    n12 --> n15
    n13 --> n16
    n3 --> n16
    n4 --> n13
    n5 --> n13
    n1 x--x n2
    n11 x--x n12
```

# CYP_decolonisation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n23(("CYP_decolonisation"))
    end
```

# CYP_establish_politics

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n24{"CYP_establish_politics"}
    end
    subgraph tier_1["Tier 1"]
        n25{"CYP_communist"}
        n26{"CYP_democracy"}
        n27{"CYP_fascist"}
        n28["CYP_neutral"]
    end
    subgraph tier_2["Tier 2"]
        n29["CYP_cyprus_first"]
        n30["CYP_enosian_government"]
        n31["CYP_enosis_fulfilled"]
        n32["CYP_ethnic_union"]
        n33["CYP_maintain_opposition_enosis"]
        n34["CYP_sovereign_country"]
        n35["CYP_support_enosis"]
    end
    n24 --> n25
    n27 --> n29
    n24 --> n26
    n26 --> n30
    n27 --> n31
    n28 --> n32
    n24 --> n27
    n25 --> n33
    n24 --> n28
    n26 --> n34
    n25 --> n35
    n25 x--x n26
    n25 x--x n27
    n25 x--x n28
    n29 x--x n31
    n26 x--x n27
    n26 x--x n28
    n30 x--x n34
    n27 x--x n28
    n33 x--x n35
```

# CYP_found_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36{"CYP_found_army"}
    end
    subgraph tier_1["Tier 1"]
        n37["CYP_across_sea"]
        n38{"CYP_equipment_modernisation"}
        n39["CYP_island_defense"]
    end
    subgraph tier_2["Tier 2"]
        n40["CYP_adopt_british_guns"]
        n41["CYP_arms_for_nation"]
        n42["CYP_create_armoured_corp"]
        n43["CYP_general_staff_attack"]
        n44["CYP_grand_defense_plan"]
        n45["CYP_marine_corp"]
        n46["CYP_trench_warfare"]
        n47["CYP_war_mobilisation"]
    end
    subgraph tier_3["Tier 3"]
        n48["CYP_create_nicosia_arsenal"]
        n49["CYP_deep_defense"]
        n50["CYP_develop_tank_variants"]
        n51["CYP_invasion_plans"]
        n52["CYP_motorisation_drive"]
        n53["CYP_prepare_coastal_defenses"]
        n54["CYP_professional_army_training"]
        n55["CYP_support_equipment"]
    end
    subgraph tier_4["Tier 4"]
        n56["CYP_guerilla_war"]
        n57["CYP_island_fortress"]
        n58["CYP_war_lessons"]
    end
    n36 --> n37
    n38 --> n40
    n38 --> n41
    n38 --> n42
    n41 --> n48
    n44 --> n49
    n42 --> n50
    n36 --> n38
    n37 --> n43
    n39 --> n44
    n51 --> n56
    n53 --> n56
    n47 --> n51
    n36 --> n39
    n49 --> n57
    n46 --> n57
    n53 --> n57
    n37 --> n45
    n40 --> n52
    n42 --> n52
    n47 --> n53
    n43 --> n54
    n45 --> n54
    n40 --> n55
    n39 --> n46
    n54 --> n58
    n51 --> n58
    n37 --> n47
    n39 --> n47
    n37 x--x n39
    n40 x--x n42
```
