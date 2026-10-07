# GCO_UNIFIED_gran_colombian_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("GCO_UNIFIED_gran_colombian_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["GCO_UNIFIED_connect_the_cities"]
    end
    subgraph tier_2["Tier 2"]
        n3["GCO_UNIFIED_administrative_reorganization"]
        n4["GCO_UNIFIED_defend_the_new_union"]
        n5["GCO_UNIFIED_develop_mining"]
    end
    subgraph tier_3["Tier 3"]
        n6["GCO_UNIFIED_exploit_colombian_amazonian_rubber"]
        n7["GCO_UNIFIED_naval_buildup"]
        n8["GCO_UNIFIED_united_armed_forces"]
    end
    n2 --> n3
    n1 --> n2
    n2 --> n4
    n2 --> n5
    n3 --> n6
    n5 --> n6
    n3 --> n7
    n4 --> n8
```
