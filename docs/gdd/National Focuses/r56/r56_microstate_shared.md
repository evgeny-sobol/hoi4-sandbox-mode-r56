# MICRO_build_capital_airport

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("MICRO_build_capital_airport"))
        n2["MICRO_root_naval_academy"]
    end
    subgraph tier_1["Tier 1"]
        n3["MICRO_the_root_air_fleet"]
    end
    subgraph tier_2["Tier 2"]
        n4["MICRO_torpedo_bombers"]
    end
    n1 --> n3
    n2 --> n4
    n3 --> n4
```

# MICRO_develop_our_dockyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n5(("MICRO_develop_our_dockyards"))
        n6["MICRO_develop_special_forces"]
        n3["MICRO_the_root_air_fleet"]
    end
    subgraph tier_1["Tier 1"]
        n7["MICRO_develop_indigenous_models"]
        n2["MICRO_root_naval_academy"]
    end
    subgraph tier_2["Tier 2"]
        n8["MICRO_recruit_marines"]
        n9["MICRO_the_big_guns"]
        n4["MICRO_torpedo_bombers"]
    end
    n5 --> n7
    n2 --> n8
    n6 --> n8
    n5 --> n2
    n7 --> n9
    n2 --> n4
    n3 --> n4
```

# MICRO_militarize_the_police_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10(("MICRO_militarize_the_police_force"))
        n2["MICRO_root_naval_academy"]
    end
    subgraph tier_1["Tier 1"]
        n11["MICRO_weaponry_modernization"]
    end
    subgraph tier_2["Tier 2"]
        n6["MICRO_develop_special_forces"]
        n12["MICRO_the_root_industrial_fund"]
    end
    subgraph tier_3["Tier 3"]
        n13["LUX_nationalise_railway_companies"]
        n14["MICRO_economic_mobilization"]
        n8["MICRO_recruit_marines"]
        n15["MICRO_root_military_institute"]
    end
    subgraph tier_4["Tier 4"]
        n16["MICRO_encourage_local_arms_production"]
        n17["MICRO_the_grand_university_of_capital"]
    end
    subgraph tier_5["Tier 5"]
        n18["MICRO_introduce_motorization_technologies"]
        n19["MICRO_resource_commission"]
        n20["MICRO_the_roars_of_thunder"]
    end
    subgraph tier_6["Tier 6"]
        n21["MICRO_the_steel_lions"]
    end
    n12 --> n13
    n11 --> n6
    n12 --> n14
    n14 --> n16
    n17 --> n18
    n2 --> n8
    n6 --> n8
    n16 --> n19
    n6 --> n15
    n12 --> n15
    n15 --> n17
    n17 --> n20
    n16 --> n20
    n11 --> n12
    n18 --> n21
    n10 --> n11
```
