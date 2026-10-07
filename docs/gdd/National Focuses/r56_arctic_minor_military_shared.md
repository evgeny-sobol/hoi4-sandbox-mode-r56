# ARCTIC_sharpshooting_tradition

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ARCTIC_sharpshooting_tradition"))
    end
    subgraph tier_1["Tier 1"]
        n2["ARCTIC_establish_a_general_staff"]
        n3["ARCTIC_komi_can_communicate"]
        n4["ARCTIC_start_them_young"]
        n5["ARCTIC_winter_training"]
    end
    subgraph tier_2["Tier 2"]
        n6["ARCTIC_encourage_fishing"]
        n7["ARCTIC_organize_army_structure"]
        n8["ARCTIC_recruit_penguins"]
        n9["ARCTIC_winter_readiness"]
    end
    subgraph tier_3["Tier 3"]
        n10["ARCTIC_army_modernization"]
        n11["ARCTIC_dissent_in_the_party"]
        n12["ARCTIC_equipment_effort"]
        n13["ARCTIC_sami_pathfinders"]
    end
    subgraph tier_4["Tier 4"]
        n14["ARCTIC_equipment_effort_2"]
        n15["ARCTIC_equipment_effort_3"]
        n16["ARCTIC_establish_a_armor_corp"]
        n17["ARCTIC_infantry_camouflage"]
        n18["ARCTIC_motorization_effort"]
        n19["ARCTIC_the_day_before_the_storm_hit"]
    end
    subgraph tier_5["Tier 5"]
        n20["ARCTIC_establish_a_military_academy"]
        n21["ARCTIC_field_hospitals"]
        n22["ARCTIC_mechanization_effort"]
        n23["ARCTIC_signal_companies"]
        n24["ARCTIC_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n25["ARCTIC_modern_logistics"]
    end
    n7 --> n10
    n8 --> n11
    n4 --> n6
    n7 --> n12
    n9 --> n12
    n12 --> n14
    n12 --> n15
    n10 --> n16
    n1 --> n2
    n16 --> n20
    n15 --> n20
    n18 --> n21
    n12 --> n17
    n1 --> n3
    n16 --> n22
    n18 --> n22
    n21 --> n25
    n22 --> n25
    n23 --> n25
    n10 --> n18
    n2 --> n7
    n4 --> n8
    n9 --> n13
    n16 --> n23
    n15 --> n24
    n17 --> n24
    n14 --> n24
    n1 --> n4
    n11 --> n19
    n5 --> n9
    n2 --> n9
    n1 --> n5
```
