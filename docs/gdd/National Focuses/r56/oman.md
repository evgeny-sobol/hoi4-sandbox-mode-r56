# orphans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["GEN_Conquer"]
        n2["GEN_Intervene"]
        n3["GEN_Isolated"]
        n4["GEN_begin_industrial_buildup"]
    end
    subgraph tier_1["Tier 1"]
        n5["OMA_establish_the_rial"]
        n6["OMA_reclaim_the_northern_lands"]
        n7["OMA_tear_up_the_treaties"]
    end
    subgraph tier_2["Tier 2"]
        n8["OMA_across_the_gulf"]
        n9["OMA_our_african_holdings"]
    end
    n6 --> n8
    n4 --> n5
    n6 --> n9
    n1 --> n6
    n1 --> n7
    n2 --> n7
    n3 --> n7
```
