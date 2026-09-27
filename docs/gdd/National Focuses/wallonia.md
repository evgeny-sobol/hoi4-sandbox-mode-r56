# orphans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"GEN_Strenghten_Democracy"}
    end
    subgraph tier_1["Tier 1"]
        n2["WLL_conservatism_focus"]
        n3["WLL_welfare_focus"]
    end
    subgraph tier_2["Tier 2"]
        n4["WLL_rearmament_agreement"]
    end
    n1 --> n2
    n3 --> n4
    n2 --> n4
    n1 --> n3
    n2 x--x n3
```
