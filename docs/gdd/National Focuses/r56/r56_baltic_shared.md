# BAL_UNIFIED_baltic_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("BAL_UNIFIED_baltic_unification"))
    end
    subgraph tier_1["Tier 1"]
        n2["BAL_UNIFIED_coordinate_the_land_equipment_manufacturers"]
        n3["BAL_UNIFIED_exploit_our_common_resources"]
    end
    subgraph tier_2["Tier 2"]
        n4{"BAL_UNIFIED_VEF_electronics"}
        n5["BAL_UNIFIED_estonian_shale_oil"]
    end
    subgraph tier_3["Tier 3"]
        n6["BAL_UNIFIED_VEF_bombing_sights"]
        n7["BAL_UNIFIED_VEF_cameras"]
    end
    n4 --> n6
    n4 --> n7
    n2 --> n4
    n1 --> n2
    n3 --> n5
    n1 --> n3
    n6 x--x n7
```
