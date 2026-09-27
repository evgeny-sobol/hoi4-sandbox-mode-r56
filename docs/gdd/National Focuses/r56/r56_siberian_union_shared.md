# SIB_siberian_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SIB_siberian_unification"))
        n2["TRK_turkestan_unification"]
    end
    subgraph tier_1["Tier 1"]
        n3["SIB_connect_the_cities"]
        n4["SIB_develop_mining"]
    end
    subgraph tier_2["Tier 2"]
        n5["SIB_ethnic_collaboration"]
    end
    subgraph tier_3["Tier 3"]
        n6["SIB_claim_a_fitting_title"]
        n7["SIB_state-funded_projects"]
        n8["SIB_utilize_ainu_expertise"]
    end
    n5 --> n6
    n1 --> n3
    n1 --> n4
    n3 --> n5
    n5 --> n7
    n5 --> n8
    n1 x--x n2
```
