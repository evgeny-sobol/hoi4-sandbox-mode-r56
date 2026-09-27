# ENG_welcome_british_exiles

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ENG_welcome_british_exiles"))
    end
    subgraph tier_1["Tier 1"]
        n2["ENG_landing_exercices"]
        n3["ENG_recruit_volunteers"]
    end
    subgraph tier_2["Tier 2"]
        n4["ENG_british_agents"]
        n5["ENG_reclaim_the_british_isles_exile"]
    end
    n3 --> n4
    n1 --> n2
    n2 --> n5
    n1 --> n3
```
