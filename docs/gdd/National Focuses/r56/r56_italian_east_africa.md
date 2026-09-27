# AOI_securing_east_africa

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("AOI_securing_east_africa"))
    end
    subgraph tier_1["Tier 1"]
        n2["AOI_establish_provincial_capitals"]
        n3["AOI_warm_climate_equipment"]
    end
    subgraph tier_2["Tier 2"]
        n4["AOI_establish_a_general_staff"]
    end
    subgraph tier_3["Tier 3"]
        n5["AOI_organize_the_police_structure"]
        n6["AOI_warm_climate_training"]
    end
    subgraph tier_4["Tier 4"]
        n7["AOI_army_modernization"]
        n8["AOI_equipment_effort"]
        n9["AOI_expand_ascari_recruitment"]
        n10["AOI_italian_african_police"]
    end
    subgraph tier_5["Tier 5"]
        n11["AOI_camelry_expertise"]
        n12["AOI_colonial_secret_department"]
        n13["AOI_equipment_effort_2"]
        n14["AOI_equipment_effort_3"]
        n15["AOI_establish_a_armor_corp"]
        n16["AOI_infantry_camouflage"]
        n17["AOI_motorization_effort"]
    end
    subgraph tier_6["Tier 6"]
        n18["AOI_establish_a_military_academy"]
        n19["AOI_field_hospitals"]
        n20["AOI_mechanization_effort"]
        n21["AOI_signal_companies"]
        n22["AOI_special_forces"]
    end
    subgraph tier_7["Tier 7"]
        n23["AOI_modern_logistics"]
    end
    n5 --> n7
    n6 --> n7
    n9 --> n11
    n10 --> n12
    n5 --> n8
    n6 --> n8
    n8 --> n13
    n8 --> n14
    n7 --> n15
    n3 --> n4
    n15 --> n18
    n14 --> n18
    n1 --> n2
    n5 --> n9
    n17 --> n19
    n8 --> n16
    n5 --> n10
    n6 --> n10
    n15 --> n20
    n17 --> n20
    n19 --> n23
    n20 --> n23
    n21 --> n23
    n7 --> n17
    n4 --> n5
    n15 --> n21
    n14 --> n22
    n16 --> n22
    n13 --> n22
    n1 --> n3
    n4 --> n6
```
