# SPR_nationalist_victory

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"SPR_nationalist_victory"}
        n2["SPR_republican_victory"]
    end
    subgraph tier_1["Tier 1"]
        n3["SPR_cement_franco_rule"]
        n4["SPR_crush_regional_governments_r56"]
        n5{"SPR_restore_the_monarchy"}
    end
    subgraph tier_2["Tier 2"]
        n6{"SPR_king_javier_I"}
        n7{"SPR_king_juan_iii"}
        n8["SPR_policia_armada"]
        n9["SPR_pursue_autarky_policies"]
    end
    subgraph tier_3["Tier 3"]
        n10["ITA_align_with_italy"]
        n11["SPA_r56_alliance_with_the_kaiserreich"]
        n12["SPA_r56_carlist_diplomacy"]
        n13["SPA_r56_spanish_austrian_diplomatic_unity"]
        n14["SPR_british_alignment"]
        n15["SPR_issue_political_amnesties"]
        n16["SPR_ministry_of_religous_affairs"]
        n17{"SPR_sindicato_vertical"}
        n18["SPR_stay_out_of_conflicts"]
    end
    subgraph tier_4["Tier 4"]
        n19["SPR_claims_against_italy"]
        n20["SPR_common_front_against_nazism"]
        n21["SPR_establish_traditional_cortes"]
        n22["SPR_expand_pyrenees_fortifications"]
        n23["SPR_francoist_neutrality"]
        n24{"SPR_join_italy"}
        n25{"SPR_join_the_axis"}
        n26["SPR_reclaim_gibraltar"]
        n27["SPR_support_the_free_market"]
        n28{"SPR_una_grande_y_libre"}
    end
    subgraph tier_5["Tier 5"]
        n29["SPR_a_permanent_legion_condor"]
        n30["SPR_befriend_portugal"]
        n31["SPR_claim_sardinia_and_sicily"]
        n32["SPR_decentralize_the_kingdom"]
        n33["SPR_further_the_iberian_pact"]
        n34["SPR_help_the_royal_navy"]
        n35["SPR_learn_from_the_regia_marina"]
        n36["SPR_the_transition"]
        n37["SPR_unify_iberia"]
    end
    subgraph tier_6["Tier 6"]
        n38["SPR_claims_on_france"]
        n39["SPR_retake_gibraltar"]
    end
    n6 --> n10
    n6 --> n11
    n6 --> n12
    n6 --> n13
    n25 --> n29
    n24 --> n30
    n25 --> n30
    n28 --> n30
    n7 --> n14
    n6 --> n14
    n1 --> n3
    n20 --> n31
    n14 --> n19
    n37 --> n38
    n30 --> n38
    n17 --> n20
    n1 --> n4
    n21 --> n32
    n16 --> n21
    n18 --> n22
    n17 --> n23
    n23 --> n33
    n20 --> n34
    n7 --> n15
    n17 --> n24
    n17 --> n25
    n5 --> n6
    n5 --> n7
    n24 --> n35
    n6 --> n16
    n3 --> n8
    n3 --> n9
    n10 --> n26
    n1 --> n5
    n37 --> n39
    n30 --> n39
    n9 --> n17
    n8 --> n17
    n7 --> n18
    n6 --> n18
    n15 --> n27
    n27 --> n36
    n17 --> n28
    n24 --> n37
    n25 --> n37
    n28 --> n37
    n10 x--x n11
    n10 x--x n12
    n10 x--x n13
    n10 x--x n14
    n10 x--x n18
    n11 x--x n12
    n11 x--x n13
    n11 x--x n14
    n11 x--x n18
    n12 x--x n13
    n12 x--x n14
    n12 x--x n18
    n13 x--x n14
    n13 x--x n18
    n30 x--x n37
    n14 x--x n18
    n3 x--x n5
    n20 x--x n23
    n20 x--x n24
    n20 x--x n25
    n20 x--x n28
    n23 x--x n24
    n23 x--x n25
    n23 x--x n28
    n24 x--x n25
    n24 x--x n28
    n25 x--x n28
    n6 x--x n7
    n1 x--x n2
```
