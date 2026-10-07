# NRU_continue_phosphate_mining

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("NRU_continue_phosphate_mining"))
    end
    subgraph tier_1["Tier 1"]
        n2["NRU_further_phosphate_extraction"]
        n3["NRU_start_exporting_phosphate"]
    end
    subgraph tier_2["Tier 2"]
        n4["NRU_free_market"]
        n5["NRU_futher_phosphate_extracion_two"]
        n6["NRU_researchers_abroad"]
    end
    subgraph tier_3["Tier 3"]
        n7{"NRU_reap_the_benefits"}
    end
    subgraph tier_4["Tier 4"]
        n8["NRU_britian_phosphate"]
        n9["NRU_japanese_phosphate"]
        n10["NRU_soviet_phosphate"]
    end
    n7 --> n8
    n3 --> n4
    n1 --> n2
    n2 --> n5
    n7 --> n9
    n4 --> n7
    n5 --> n7
    n2 --> n6
    n3 --> n6
    n7 --> n10
    n1 --> n3
    n8 x--x n9
    n8 x--x n10
    n9 x--x n10
```

# NRU_core_kiribati

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n11(("NRU_core_kiribati"))
    end
```

# orphans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12["GEN_Naval_Effort"]
        n13["GEN_Strenghten_Democracy"]
        n14["GEN_Strenghten_Monarchy"]
    end
    subgraph tier_1["Tier 1"]
        n15["NRU_autonomy_for_the_tribes"]
        n16["NRU_establish_nauru_pacific_line"]
    end
    n14 --> n15
    n13 --> n15
    n12 --> n16
```
