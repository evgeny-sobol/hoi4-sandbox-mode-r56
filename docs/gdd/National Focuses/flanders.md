# orphans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"GEN_Strenghten_Democracy"}
        n2["GEN_focus_on_synthetic_processing"]
        n3["GEN_improve_state_infrastructure"]
    end
    subgraph tier_1["Tier 1"]
        n4["FLA_Antwerp_Oil_Industry"]
        n5["FLA_coal_mines"]
        n6["FLA_conservatism_focus"]
        n7["FLA_reinforce_antwerp_brussels"]
        n8["FLA_welfare_focus"]
    end
    subgraph tier_2["Tier 2"]
        n9["FLA_rearmament_agreement"]
    end
    n2 --> n4
    n2 --> n5
    n1 --> n6
    n8 --> n9
    n6 --> n9
    n3 --> n7
    n1 --> n8
    n6 x--x n8
```
