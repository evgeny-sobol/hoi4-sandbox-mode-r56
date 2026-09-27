# KAT_the_geological_scandal

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("KAT_the_geological_scandal"))
    end
    subgraph tier_1["Tier 1"]
        n2{"KAT_Military_Buildup"}
        n3["KAT_gold_mining"]
        n4["KAT_improve_the_road_network"]
        n5["KAT_katangese_copper"]
    end
    subgraph tier_2["Tier 2"]
        n6["KAT_Civilian_One"]
        n7["KAT_copper_cartridges"]
        n8["KAT_invite_american_investors"]
        n9["KAT_invite_german_investors"]
        n10["KAT_invite_soviet_planners"]
        n11["KAT_rare_minerals"]
    end
    subgraph tier_3["Tier 3"]
        n12["KAT_American_Air"]
        n13["KAT_Automobile"]
        n14["KAT_Civilian_Two"]
        n15["KAT_Futher_Investments"]
        n16["KAT_Soviet_Heavy_Industry"]
        n17["KAT_german_heavy_industry_expansion"]
    end
    subgraph tier_4["Tier 4"]
        n18["KAT_Excavation"]
        n19["KAT_Licences"]
        n20["KAT_Research"]
    end
    subgraph tier_5["Tier 5"]
        n21["KAT_Autarky"]
        n22["KAT_Refinery"]
        n23["KAT_exploit_the_yellowcake"]
    end
    n8 --> n12
    n18 --> n21
    n8 --> n13
    n9 --> n13
    n10 --> n13
    n4 --> n6
    n6 --> n14
    n14 --> n18
    n3 --> n18
    n5 --> n18
    n8 --> n15
    n9 --> n15
    n10 --> n15
    n12 --> n19
    n17 --> n19
    n16 --> n19
    n1 --> n2
    n18 --> n22
    n20 --> n22
    n14 --> n20
    n10 --> n16
    n5 --> n7
    n2 --> n7
    n18 --> n23
    n9 --> n17
    n1 --> n3
    n1 --> n4
    n2 --> n8
    n2 --> n9
    n2 --> n10
    n1 --> n5
    n3 --> n11
    n5 --> n11
    n8 x--x n9
    n8 x--x n10
    n9 x--x n10
```
