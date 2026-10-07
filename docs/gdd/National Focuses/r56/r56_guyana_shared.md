# GUYANA_UNIFIED_guianese_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("GUYANA_UNIFIED_guianese_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["GUYANA_UNIFIED_connect_the_cities"]
    end
    subgraph tier_2["Tier 2"]
        n3["GUYANA_UNIFIED_administrative_reorganization"]
        n4["GUYANA_UNIFIED_defend_the_new_union"]
    end
    subgraph tier_3["Tier 3"]
        n5["GUYANA_UNIFIED_develop_mining"]
        n6["GUYANA_UNIFIED_domestic_steel_production"]
        n7["GUYANA_UNIFIED_naval_buildup"]
        n8["GUYANA_UNIFIED_united_armed_forces"]
    end
    subgraph tier_4["Tier 4"]
        n9["GUYANA_UNIFIED_guyanese_gold_deposits"]
        n10["GUYANA_UNIFIED_legacy_of_piracy"]
    end
    n2 --> n3
    n1 --> n2
    n2 --> n4
    n3 --> n5
    n3 --> n6
    n5 --> n9
    n7 --> n10
    n3 --> n7
    n4 --> n8
```
