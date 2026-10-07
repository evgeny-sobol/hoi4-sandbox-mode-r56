# SCA_scandinavian_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SCA_scandinavian_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["SCA_northern_swedish_iron"]
        n3["SCA_norwegian_aluminium_sector"]
        n4["SCA_trans_scandinavian_railway"]
        n5["SCA_trelleborg_rubber_factory"]
    end
    subgraph tier_2["Tier 2"]
        n6["SCA_unified_armament_industries"]
    end
    n1 --> n2
    n1 --> n3
    n1 --> n4
    n1 --> n5
    n3 --> n6
```
