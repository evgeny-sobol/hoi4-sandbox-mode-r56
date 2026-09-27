# MAR_mari_el_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("MAR_mari_el_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["MAR_connect_the_cities"]
        n3["MAR_develop_mining"]
    end
    subgraph tier_2["Tier 2"]
        n4["MAR_ethnic_collaboration"]
    end
    subgraph tier_3["Tier 3"]
        n5["MAR_claim_a_fitting_title"]
        n6["MAR_state-funded_projects"]
    end
    n4 --> n5
    n1 --> n2
    n1 --> n3
    n2 --> n4
    n4 --> n6
```
