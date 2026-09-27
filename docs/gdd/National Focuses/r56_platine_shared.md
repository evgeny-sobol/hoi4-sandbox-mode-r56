# PLA_platine_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PLA_platine_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["PLA_defend_the_new_union"]
        n3["PLA_develop_mining"]
        n4["PLA_improve_local_infrastructure"]
    end
    subgraph tier_2["Tier 2"]
        n5["PLA_hispanic_cooperation"]
        n6["PLA_naval_buildup"]
        n7["PLA_oil_in_the_tierra_del_fuego"]
        n8["PLA_united_armed_forces"]
    end
    n1 --> n2
    n1 --> n3
    n4 --> n5
    n1 --> n4
    n4 --> n6
    n3 --> n7
    n4 --> n7
    n2 --> n8
```
