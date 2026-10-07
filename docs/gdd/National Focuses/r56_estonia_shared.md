# EST_air_base_expansion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("EST_air_base_expansion"))
    end
    subgraph tier_1["Tier 1"]
        n2{"EST_air_innovations"}
        n3{"EST_fighter_modernisation"}
    end
    subgraph tier_2["Tier 2"]
        n4{"EST_heavy_fighter_concept"}
        n5["EST_naval_bomber_experiments"]
    end
    subgraph tier_3["Tier 3"]
        n6["EST_light_bomber_focus"]
        n7["EST_medium_bomber_focus"]
    end
    subgraph tier_4["Tier 4"]
        n8["EST_air_modernisations_programme"]
    end
    n1 --> n2
    n6 --> n8
    n7 --> n8
    n1 --> n3
    n2 --> n4
    n3 --> n4
    n4 --> n6
    n3 --> n6
    n4 --> n7
    n2 --> n7
    n2 --> n5
    n6 x--x n7
```

# EST_build_paldiski_port

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n9(("EST_build_paldiski_port"))
    end
    subgraph tier_1["Tier 1"]
        n10["EST_escort_effort"]
        n11["EST_expand_port_paldiski"]
        n12["EST_navy_tactics"]
    end
    subgraph tier_2["Tier 2"]
        n13["EST_destroyer_focus"]
        n14["EST_special_marine_forces"]
    end
    n12 --> n13
    n9 --> n10
    n9 --> n11
    n9 --> n12
    n10 --> n14
```

# EST_prepare_for_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15(("EST_prepare_for_war"))
        n16["EST_tallinn_tartu_highways"]
        n17["EST_the_four_year_plan"]
    end
    subgraph tier_1["Tier 1"]
        n18["EST_foreign_cooperation"]
        n19["EST_invest_in_the_military"]
        n20["EST_standardization_of_equipment"]
    end
    subgraph tier_2["Tier 2"]
        n21["EST_develop_our_railroads"]
        n22["EST_motorized_focus"]
        n23["EST_protect_against_the_red_army"]
        n24["EST_study_foreign_tanks"]
    end
    subgraph tier_3["Tier 3"]
        n25{"EST_Livonian_bridgehead_strategy"}
        n26["EST_foundation_of_kumu"]
        n27["EST_invite_german_experts"]
    end
    subgraph tier_4["Tier 4"]
        n28["EST_anti_tank_guns"]
        n29["EST_artillery_modernisation"]
        n30["EST_start_central_industrial_region"]
    end
    subgraph tier_5["Tier 5"]
        n31["EST_army_modernisation"]
        n32["EST_finish_central_industrial_region"]
        n33["EST_the_bombe"]
    end
    n22 --> n25
    n25 --> n28
    n28 --> n31
    n29 --> n31
    n25 --> n29
    n19 --> n21
    n30 --> n32
    n15 --> n18
    n21 --> n26
    n17 --> n19
    n15 --> n19
    n24 --> n27
    n18 --> n22
    n18 --> n23
    n20 --> n23
    n15 --> n20
    n16 --> n30
    n26 --> n30
    n20 --> n24
    n30 --> n33
    n28 x--x n29
```

# EST_the_four_year_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15["EST_prepare_for_war"]
        n17(("EST_the_four_year_plan"))
    end
    subgraph tier_1["Tier 1"]
        n34["EST_build_better_capital"]
        n19["EST_invest_in_the_military"]
    end
    subgraph tier_2["Tier 2"]
        n21["EST_develop_our_railroads"]
        n35["EST_more_civilian_factories"]
    end
    subgraph tier_3["Tier 3"]
        n26["EST_foundation_of_kumu"]
        n36{"EST_heavy_industry"}
        n37["EST_kohta_jarve_oil_sources"]
        n16["EST_tallinn_tartu_highways"]
    end
    subgraph tier_4["Tier 4"]
        n38["EST_invest_in_the_military_II"]
        n39["EST_more_civilian_factories_II"]
        n40["EST_planned_expansion"]
        n30["EST_start_central_industrial_region"]
    end
    subgraph tier_5["Tier 5"]
        n41["EST_additional_research_slot"]
        n32["EST_finish_central_industrial_region"]
        n33["EST_the_bombe"]
    end
    n39 --> n41
    n38 --> n41
    n17 --> n34
    n19 --> n21
    n30 --> n32
    n21 --> n26
    n35 --> n36
    n17 --> n19
    n15 --> n19
    n36 --> n38
    n35 --> n37
    n34 --> n35
    n36 --> n39
    n37 --> n40
    n16 --> n30
    n26 --> n30
    n35 --> n16
    n30 --> n33
    n38 x--x n39
```
