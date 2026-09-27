# ECU_Alert_in_the_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ECU_Alert_in_the_front"))
    end
    subgraph tier_1["Tier 1"]
        n2{"ECU_desperate_mobilization"}
    end
    subgraph tier_2["Tier 2"]
        n3["ECU_focus_on_defending_quito"]
        n4["ECU_gallos_plan"]
    end
    subgraph tier_3["Tier 3"]
        n5["ECU_adquire_usa_planes"]
        n6["ECU_industralize_the_amazon"]
        n7["ECU_our_true_borders"]
    end
    subgraph tier_4["Tier 4"]
        n8["ECU_annex_the_north_of_Peru"]
    end
    n3 --> n5
    n4 --> n5
    n6 --> n8
    n7 --> n8
    n5 --> n8
    n1 --> n2
    n2 --> n3
    n2 --> n4
    n3 --> n6
    n4 --> n6
    n3 --> n7
    n4 --> n7
    n3 x--x n4
```
