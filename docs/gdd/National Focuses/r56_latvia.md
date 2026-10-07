# LAT_a_rejection_of_ulmanis

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("LAT_a_rejection_of_ulmanis"))
        n2{"LAT_ulmanis_in_control_of_the_government"}
    end
    subgraph tier_1["Tier 1"]
        n3["LAT_assemble_a_new_seima"]
        n4["LAT_coalition_with_the_communists"]
        n5["LAT_radical_opposition"]
    end
    subgraph tier_2["Tier 2"]
        n6["LAT_liberal_economic_reforms"]
        n7["LAT_proclaim_the_new_state"]
        n8["LAT_proclaim_the_peoples_republic"]
        n9{"LAT_redraft_the_constitution"}
    end
    subgraph tier_3["Tier 3"]
        n10["LAT_a_western_ally"]
        n11["LAT_baltic_cooperation"]
        n12["LAT_centralize_farming_production"]
        n13["LAT_discredit_totalitarianism"]
        n14["LAT_hail_the_struggle"]
        n15["LAT_join_comintern"]
        n16["LAT_latvian_militarism"]
        n17["LAT_privatize_the_industry"]
        n18["LAT_rally_the_workers"]
    end
    subgraph tier_4["Tier 4"]
        n19["LAT_democratic_gem_of_eastern_europe"]
        n20["LAT_eliminate_capitalism"]
        n21["LAT_irridentist_youth"]
        n22["LAT_latvian_chauvinism"]
        n23["LAT_liberate_estonia"]
        n24["LAT_liberate_lithuania"]
    end
    subgraph tier_5["Tier 5"]
        n25["LAT_baltics_under_one_flag"]
        n26["LAT_form_the_baltic_union"]
    end
    subgraph tier_6["Tier 6"]
        n27["LAT_spread_the_revolution"]
    end
    n9 --> n10
    n2 --> n10
    n1 --> n3
    n9 --> n11
    n2 --> n11
    n22 --> n25
    n21 --> n25
    n8 --> n12
    n1 --> n4
    n11 --> n19
    n13 --> n19
    n9 --> n13
    n12 --> n20
    n23 --> n26
    n24 --> n26
    n7 --> n14
    n16 --> n21
    n8 --> n15
    n16 --> n22
    n7 --> n16
    n3 --> n6
    n18 --> n23
    n18 --> n24
    n7 --> n17
    n5 --> n7
    n4 --> n8
    n1 --> n5
    n8 --> n18
    n3 --> n9
    n26 --> n27
    n10 x--x n11
```

# LAT_enforce_the_succession_law

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13["LAT_discredit_totalitarianism"]
        n28(("LAT_enforce_the_succession_law"))
        n9{"LAT_redraft_the_constitution"}
    end
    subgraph tier_1["Tier 1"]
        n2{"LAT_ulmanis_in_control_of_the_government"}
    end
    subgraph tier_2["Tier 2"]
        n10["LAT_a_western_ally"]
        n11["LAT_baltic_cooperation"]
        n29["LAT_corporate_statism"]
        n30["LAT_form_the_aizsargi"]
        n31["LAT_nationalize_important_industries"]
    end
    subgraph tier_3["Tier 3"]
        n32["LAT_assimilate_minorities"]
        n19["LAT_democratic_gem_of_eastern_europe"]
        n33["LAT_house_of_proffesions"]
        n34["LAT_micromanage_the_economy"]
    end
    subgraph tier_4["Tier 4"]
        n35["LAT_equal_latvia"]
        n36["LAT_top_of_the_line_agrarianism"]
    end
    n9 --> n10
    n2 --> n10
    n29 --> n32
    n9 --> n11
    n2 --> n11
    n2 --> n29
    n11 --> n19
    n13 --> n19
    n33 --> n35
    n32 --> n35
    n2 --> n30
    n29 --> n33
    n31 --> n34
    n2 --> n31
    n34 --> n36
    n33 --> n36
    n28 --> n2
    n10 x--x n11
```
