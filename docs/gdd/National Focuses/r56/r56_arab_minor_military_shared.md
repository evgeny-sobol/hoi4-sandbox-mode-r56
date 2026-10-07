# ARAB_the_holy_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ARAB_the_holy_war"))
    end
    subgraph tier_1["Tier 1"]
        n2["ARAB_arms_shipments"]
        n3["ARAB_war_infrastructure"]
    end
    subgraph tier_2["Tier 2"]
        n4{"ARAB_army_assessments"}
    end
    subgraph tier_3["Tier 3"]
        n5["ARAB_get_rid_of_nepotism"]
        n6["ARAB_keep_nepotism"]
    end
    n1 --> n2
    n3 --> n4
    n2 --> n4
    n4 --> n5
    n4 --> n6
    n1 --> n3
    n5 x--x n6
```

# ARAB_under_the_sun

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n7(("ARAB_under_the_sun"))
    end
    subgraph tier_1["Tier 1"]
        n8["ARAB_establish_a_general_staff"]
        n9["ARAB_rely_on_tribal_levies"]
        n10["ARAB_warm_climate_training"]
    end
    subgraph tier_2["Tier 2"]
        n11["ARAB_desert_expertise"]
        n12["ARAB_organize_army_structure"]
        n13["ARAB_tribal_warrior_traditions"]
    end
    subgraph tier_3["Tier 3"]
        n14["ARAB_army_modernization"]
        n15["ARAB_camelry_expertise"]
        n16["ARAB_equipment_effort"]
        n17["ARAB_expand_the_recruitment_pool"]
    end
    subgraph tier_4["Tier 4"]
        n18["ARAB_equipment_effort_2"]
        n19["ARAB_equipment_effort_3"]
        n20["ARAB_establish_a_armor_corp"]
        n21["ARAB_infantry_camouflage"]
        n22["ARAB_motorization_effort"]
    end
    subgraph tier_5["Tier 5"]
        n23["ARAB_establish_a_military_academy"]
        n24["ARAB_field_hospitals"]
        n25["ARAB_mechanization_effort"]
        n26["ARAB_signal_companies"]
        n27["ARAB_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n28["ARAB_modern_logistics"]
    end
    n12 --> n14
    n11 --> n15
    n10 --> n11
    n8 --> n11
    n12 --> n16
    n11 --> n16
    n16 --> n18
    n16 --> n19
    n14 --> n20
    n7 --> n8
    n20 --> n23
    n19 --> n23
    n12 --> n17
    n22 --> n24
    n16 --> n21
    n20 --> n25
    n22 --> n25
    n24 --> n28
    n25 --> n28
    n26 --> n28
    n14 --> n22
    n8 --> n12
    n7 --> n9
    n20 --> n26
    n19 --> n27
    n21 --> n27
    n18 --> n27
    n9 --> n13
    n7 --> n10
```
