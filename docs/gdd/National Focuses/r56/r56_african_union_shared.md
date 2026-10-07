# AFR_african_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("AFR_african_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["AFR_connect_the_cities"]
        n3["AFR_develop_mining"]
        n4["AFR_tropical_warfare"]
    end
    subgraph tier_2["Tier 2"]
        n5["AFR_african_built_ships"]
        n6["AFR_amcor_plate_mill"]
        n7["AFR_ethnic_collaboration"]
    end
    subgraph tier_3["Tier 3"]
        n8["AFR_claim_a_fitting_title"]
        n9["AFR_state_funded_projects"]
        n10["UNIFIED_africa_trans_african_railway"]
    end
    n2 --> n5
    n3 --> n6
    n7 --> n8
    n1 --> n2
    n1 --> n3
    n2 --> n7
    n7 --> n9
    n1 --> n4
    n7 --> n10
```
