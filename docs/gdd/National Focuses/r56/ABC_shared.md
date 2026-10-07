# ABC_establish_a_general_staff

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ABC_establish_a_general_staff"))
    end
    subgraph tier_1["Tier 1"]
        n2["ABC_army_reform"]
    end
    subgraph tier_2["Tier 2"]
        n3["ABC_army_modernization"]
        n4["ABC_doctrine_effort"]
        n5["ABC_equipment_effort"]
    end
    subgraph tier_3["Tier 3"]
        n6["ABC_doctrine_effort_2"]
        n7["ABC_equipment_effort_2"]
        n8["ABC_equipment_effort_3"]
        n9["ABC_establish_a_armor_corp"]
        n10["ABC_motorization_effort"]
    end
    subgraph tier_4["Tier 4"]
        n11["ABC_establish_a_military_academy"]
        n12["ABC_field_hospitals"]
        n13["ABC_mechanization_effort"]
        n14["ABC_signal_companies"]
        n15["ABC_special_forces"]
    end
    subgraph tier_5["Tier 5"]
        n16["ABC_modern_logistics"]
    end
    subgraph tier_6["Tier 6"]
        n17["ABC_LIB_professionalize_the_frontier_force"]
    end
    n11 --> n17
    n16 --> n17
    n2 --> n3
    n1 --> n2
    n2 --> n4
    n4 --> n6
    n2 --> n5
    n5 --> n7
    n5 --> n8
    n3 --> n9
    n6 --> n11
    n10 --> n12
    n9 --> n13
    n10 --> n13
    n12 --> n16
    n13 --> n16
    n14 --> n16
    n3 --> n10
    n9 --> n14
    n8 --> n15
    n6 --> n15
    n7 --> n15
```
