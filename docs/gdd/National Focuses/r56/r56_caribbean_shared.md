# CARIB_caribbean_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CARIB_caribbean_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["CARIB_defend_the_new_union"]
        n3["CARIB_develop_mining"]
        n4["CARIB_improve_local_infrastructure"]
    end
    subgraph tier_2["Tier 2"]
        n5["CARIB_antilles_gold_deposits"]
        n6["CARIB_ethnic_collaboration"]
        n7["CARIB_naval_buildup"]
        n8["CARIB_united_armed_forces"]
    end
    subgraph tier_3["Tier 3"]
        n9["CARIB_legacy_of_piracy"]
    end
    n3 --> n5
    n1 --> n2
    n1 --> n3
    n4 --> n6
    n1 --> n4
    n7 --> n9
    n4 --> n7
    n2 --> n8
```
