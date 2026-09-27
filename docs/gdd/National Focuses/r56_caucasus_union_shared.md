# CAU_caucasus_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CAU_caucasus_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["CAU_connect_the_cities"]
        n3["CAU_develop_mining"]
    end
    subgraph tier_2["Tier 2"]
        n4["CAU_ethnic_collaboration"]
    end
    subgraph tier_3["Tier 3"]
        n5["CAU_claim_a_fitting_title"]
        n6["CAU_state-funded_projects"]
    end
    n4 --> n5
    n1 --> n2
    n1 --> n3
    n2 --> n4
    n4 --> n6
```
