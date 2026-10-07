# SPR_republican_victory

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["SPR_nationalist_victory"]
        n2{"SPR_republican_victory"}
    end
    subgraph tier_1["Tier 1"]
        n3["SPR_PCE_leadership"]
        n4["SPR_continue_azana_work"]
        n5["SPR_psoe_leadership"]
    end
    subgraph tier_2["Tier 2"]
        n6["SPR_appease_the_workers"]
        n7["SPR_begin_collectivization"]
        n8["SPR_continue_the_secularization_policies"]
        n9["SPR_purge_the_liberals"]
        n10["SPR_socialize_the_means_of_production"]
        n11["SPR_the_left_front"]
    end
    subgraph tier_3["Tier 3"]
        n12{"SPR_establish_soviet_democracy"}
        n13{"SPR_establish_the_oraa"}
        n14["SPR_uphold_the_1931_constitution"]
    end
    subgraph tier_4["Tier 4"]
        n15["SPR_align_with_the_new_france"]
        n16["SPR_join_the_comintern"]
        n17["SPR_repair_relations_with_the_west"]
    end
    subgraph tier_5["Tier 5"]
        n18["SPR_confront_the_hearth_of_fascism"]
        n19["SPR_demand_gibraltar"]
        n20["SPR_intervention_in_portugal"]
        n21["SPR_learn_from_the_royal_navy"]
    end
    n2 --> n3
    n12 --> n15
    n4 --> n6
    n3 --> n7
    n17 --> n18
    n15 --> n18
    n2 --> n4
    n4 --> n8
    n16 --> n19
    n11 --> n12
    n10 --> n12
    n9 --> n13
    n7 --> n13
    n15 --> n20
    n16 --> n20
    n13 --> n16
    n12 --> n16
    n17 --> n21
    n2 --> n5
    n3 --> n9
    n14 --> n17
    n5 --> n10
    n5 --> n11
    n8 --> n14
    n6 --> n14
    n3 x--x n4
    n3 x--x n5
    n15 x--x n16
    n4 x--x n5
    n1 x--x n2
```
