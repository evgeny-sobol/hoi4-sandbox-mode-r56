# CEL_aviation_air_academy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"CEL_aviation_air_academy"}
    end
    subgraph tier_1["Tier 1"]
        n2["CEL_bimotor_aircrafts"]
        n3["CEL_build_trainer_aircrafts"]
    end
    subgraph tier_2["Tier 2"]
        n4["CEL_support_designers_innovations"]
        n5["CEL_train_mechanics"]
        n6["CEL_train_pilots"]
    end
    subgraph tier_3["Tier 3"]
        n7["CEL_naval_aviation"]
        n8["CEL_refine_air_doctrine"]
    end
    subgraph tier_4["Tier 4"]
        n9["CEL_radar_network"]
    end
    n1 --> n2
    n1 --> n3
    n5 --> n7
    n4 --> n7
    n8 --> n9
    n6 --> n8
    n4 --> n8
    n3 --> n4
    n2 --> n4
    n3 --> n5
    n2 --> n5
    n3 --> n6
    n2 --> n6
    n2 x--x n3
```

# CEL_celtic_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10(("CEL_celtic_unification"))
    end
    subgraph tier_1["Tier 1"]
        n11["CEL_defend_union"]
        n12["CEL_integrate_areas"]
        n13["CEL_strengthen_shipping_routes"]
    end
    subgraph tier_2["Tier 2"]
        n14["CEL_brittany_industry"]
        n15["CEL_coal_mining"]
        n16["CEL_develop_ireland"]
        n17["CEL_naval_buildup"]
        n18["CEL_rule_the_air"]
        n19["CEL_scottish_steel_sector"]
    end
    subgraph tier_3["Tier 3"]
        n20["CEL_Brest_Oil_Industry"]
        n21["CEL_appropriate_harland_and_wolff"]
        n22["CEL_celtic_carriers"]
        n23["CEL_dingham_ammunition_factory"]
        n24["CEL_morgan_line"]
        n25["CEL_newport_artillery"]
    end
    subgraph tier_4["Tier 4"]
        n26["CEL_celtic_unity"]
    end
    subgraph tier_5["Tier 5"]
        n27["CEL_go_for_galicia"]
    end
    n14 --> n20
    n16 --> n21
    n12 --> n14
    n17 --> n22
    n18 --> n26
    n22 --> n26
    n12 --> n15
    n10 --> n11
    n12 --> n16
    n19 --> n23
    n26 --> n27
    n10 --> n12
    n14 --> n24
    n13 --> n17
    n15 --> n25
    n11 --> n18
    n12 --> n19
    n10 --> n13
```

# CEL_establish_the_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28(("CEL_establish_the_army"))
        n29["CEL_industrial_modernization"]
        n30["CEL_support_steel_sector"]
    end
    subgraph tier_1["Tier 1"]
        n31["CEL_domestic_ammunition_production"]
    end
    subgraph tier_2["Tier 2"]
        n32["CEL_domestic_artillery_production"]
        n33["CEL_redesign_small_arms"]
    end
    subgraph tier_3["Tier 3"]
        n34["CEL_artillery_modernization"]
        n35["CEL_domestic_tank_production"]
        n36["CEL_motorization_plan"]
        n37["CEL_new_tactics"]
    end
    subgraph tier_4["Tier 4"]
        n38["CEL_field_hospitals"]
        n39["CEL_mechanization_effort"]
        n40["CEL_signal_companies"]
    end
    subgraph tier_5["Tier 5"]
        n41["CEL_modern_logistics"]
        n42["CEL_planning_staff"]
    end
    subgraph tier_6["Tier 6"]
        n43["CEL_establish_special_forces"]
    end
    subgraph tier_7["Tier 7"]
        n44["CEL_spirit_of_the_army"]
    end
    n32 --> n34
    n29 --> n31
    n28 --> n31
    n31 --> n32
    n32 --> n35
    n30 --> n35
    n42 --> n43
    n36 --> n38
    n36 --> n39
    n38 --> n41
    n39 --> n41
    n40 --> n41
    n33 --> n36
    n32 --> n37
    n33 --> n37
    n37 --> n42
    n40 --> n42
    n31 --> n33
    n36 --> n40
    n37 --> n40
    n43 --> n44
```

# CEL_industrial_modernization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28["CEL_establish_the_army"]
        n29(("CEL_industrial_modernization"))
    end
    subgraph tier_1["Tier 1"]
        n31["CEL_domestic_ammunition_production"]
        n45["CEL_expand_the_construction_sector"]
        n46["CEL_utilize_our_resources"]
    end
    subgraph tier_2["Tier 2"]
        n32["CEL_domestic_artillery_production"]
        n47["CEL_improve_national_infrastructure"]
        n33["CEL_redesign_small_arms"]
        n30["CEL_support_steel_sector"]
    end
    subgraph tier_3["Tier 3"]
        n34["CEL_artillery_modernization"]
        n48["CEL_develop_aluminium_industry"]
        n49["CEL_develop_the_shale_oil_sector"]
        n35["CEL_domestic_tank_production"]
        n50["CEL_industrial_research"]
        n36["CEL_motorization_plan"]
        n37["CEL_new_tactics"]
        n51["CEL_support_light_industry"]
    end
    subgraph tier_4["Tier 4"]
        n38["CEL_field_hospitals"]
        n52["CEL_mechanical_computing"]
        n39["CEL_mechanization_effort"]
        n40["CEL_signal_companies"]
        n53["CEL_substitution_technologies"]
    end
    subgraph tier_5["Tier 5"]
        n41["CEL_modern_logistics"]
        n42["CEL_planning_staff"]
        n54["CEL_project_taranis"]
    end
    subgraph tier_6["Tier 6"]
        n43["CEL_establish_special_forces"]
    end
    subgraph tier_7["Tier 7"]
        n44["CEL_spirit_of_the_army"]
    end
    n32 --> n34
    n30 --> n48
    n47 --> n48
    n47 --> n49
    n29 --> n31
    n28 --> n31
    n31 --> n32
    n32 --> n35
    n30 --> n35
    n42 --> n43
    n29 --> n45
    n36 --> n38
    n46 --> n47
    n45 --> n47
    n47 --> n50
    n30 --> n50
    n51 --> n52
    n36 --> n39
    n38 --> n41
    n39 --> n41
    n40 --> n41
    n33 --> n36
    n32 --> n37
    n33 --> n37
    n37 --> n42
    n40 --> n42
    n52 --> n54
    n50 --> n54
    n31 --> n33
    n36 --> n40
    n37 --> n40
    n43 --> n44
    n49 --> n53
    n30 --> n51
    n46 --> n30
    n45 --> n30
    n29 --> n46
```

# CEL_naval_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n55(("CEL_naval_effort"))
    end
    subgraph tier_1["Tier 1"]
        n56{"CEL_national_admiralty"}
        n57{"CEL_shipbuilding_contacts"}
    end
    subgraph tier_2["Tier 2"]
        n58["CEL_carrier_strikes"]
        n59["CEL_cruiser_focus"]
        n60["CEL_destroyer_focus"]
        n61["CEL_naval_mine_warfare"]
        n62["CEL_the_blocade_doctrine"]
        n63["CEL_the_fleet_of_old"]
    end
    subgraph tier_3["Tier 3"]
        n64["CEL_a_s_warfare"]
        n65["CEL_battleship_focus"]
        n66["CEL_increase_naval_production"]
        n67["CEL_naval_air_groups"]
        n68["CEL_silent_service"]
    end
    subgraph tier_4["Tier 4"]
        n69["CEL_domestic_torpedo_production"]
        n70["CEL_lessons_for_the_air_force"]
        n71["CEL_stealth_upgrades"]
        n72["CEL_the_biggest_battleship"]
    end
    n60 --> n64
    n59 --> n64
    n63 --> n65
    n57 --> n58
    n56 --> n58
    n57 --> n59
    n56 --> n59
    n57 --> n60
    n56 --> n60
    n68 --> n69
    n67 --> n69
    n60 --> n66
    n59 --> n66
    n67 --> n70
    n55 --> n56
    n58 --> n67
    n57 --> n61
    n56 --> n61
    n55 --> n57
    n62 --> n68
    n68 --> n71
    n65 --> n72
    n57 --> n62
    n56 --> n62
    n57 --> n63
    n56 --> n63
    n58 x--x n62
    n58 x--x n63
    n62 x--x n63
```
