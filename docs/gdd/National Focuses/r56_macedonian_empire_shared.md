# MAE_EMPIRE_persian_imperial_ambitions

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("MAE_EMPIRE_persian_imperial_ambitions"))
    end
    subgraph tier_1["Tier 1"]
        n2["MAE_EMPIRE_connect_the_cities"]
        n3["MAE_EMPIRE_develop_mining"]
        n4["MAE_EMPIRE_military_camelry"]
    end
    subgraph tier_2["Tier 2"]
        n5["MAE_EMPIRE_appease_muslims"]
    end
    subgraph tier_3["Tier 3"]
        n6["MAE_EMPIRE_trans_persian_railway"]
    end
    n2 --> n5
    n1 --> n2
    n1 --> n3
    n1 --> n4
    n5 --> n6
```
