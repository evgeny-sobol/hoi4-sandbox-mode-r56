# PER_UNIFIED_persian_imperial_ambitions

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PER_UNIFIED_persian_imperial_ambitions"))
    end
    subgraph tier_1["Tier 1"]
        n2["PER_UNIFIED_connect_the_cities"]
        n3["PER_UNIFIED_develop_mining"]
        n4["PER_UNIFIED_military_camelry"]
    end
    subgraph tier_2["Tier 2"]
        n5["PER_UNIFIED_ethnic_collaboration"]
    end
    subgraph tier_3["Tier 3"]
        n6["PER_UNIFIED_glory_of_cyrus"]
        n7["PER_UNIFIED_trans_persian_railway"]
    end
    n1 --> n2
    n1 --> n3
    n2 --> n5
    n5 --> n6
    n1 --> n4
    n5 --> n7
```
