# GRN_develop_greenland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("GRN_develop_greenland"))
    end
    subgraph tier_1["Tier 1"]
        n2["GRN_encourage_fishing"]
        n3["GRN_expand_the_ivittuut_mine"]
        n4["GRN_prospecting_new_sites"]
    end
    subgraph tier_2["Tier 2"]
        n5["GRN_protect_greenland"]
    end
    subgraph tier_3["Tier 3"]
        n6["GRN_the_carrier_which_came_in_from_the_cold"]
    end
    n1 --> n2
    n1 --> n3
    n1 --> n4
    n4 --> n5
    n3 --> n5
    n5 --> n6
```
