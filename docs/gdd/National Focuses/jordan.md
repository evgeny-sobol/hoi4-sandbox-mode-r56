# JOR_national_conference

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"JOR_national_conference"}
    end
    subgraph tier_1["Tier 1"]
        n2["JOR_ally_opposition"]
        n3["JOR_appease_tribes"]
    end
    subgraph tier_2["Tier 2"]
        n4["JOR_circassion_integration"]
        n5["JOR_meet_arabs"]
        n6["JOR_rally_orthodox"]
        n7["JOR_salvage_ottoman_assets"]
    end
    subgraph tier_3["Tier 3"]
        n8["JOR_begin_treaty_discussions"]
        n9["JOR_revolt"]
    end
    subgraph tier_4["Tier 4"]
        n10{"JOR_operation_hashem"}
    end
    subgraph tier_5["Tier 5"]
        n11["JOR_army_victory"]
        n12["JOR_utaybah_victory"]
    end
    n1 --> n2
    n1 --> n3
    n10 --> n11
    n7 --> n8
    n4 --> n8
    n3 --> n4
    n2 --> n5
    n9 --> n10
    n2 --> n6
    n5 --> n9
    n6 --> n9
    n3 --> n7
    n10 --> n12
    n2 x--x n3
    n11 x--x n12
```
