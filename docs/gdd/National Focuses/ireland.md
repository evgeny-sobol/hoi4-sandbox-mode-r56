# IRE_fine_gael

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("IRE_fine_gael"))
        n2["IRE_finna_fail"]
    end
    subgraph tier_1["Tier 1"]
        n3{"IRE_hold_public_funding_oppertunities"}
        n4{"IRE_radio_broadcasts"}
        n5{"IRE_rally_rural_ireland"}
        n6["IRE_treet"]
    end
    subgraph tier_2["Tier 2"]
        n7["IRE_coa"]
        n8{"IRE_oduffy_expulsion"}
        n9{"IRE_oust_the_moderates"}
    end
    subgraph tier_3["Tier 3"]
        n10["IRE_accept_dominin_status"]
        n11{"IRE_agricultural_pasturing"}
        n12{"IRE_establish_the_coorperate_state"}
        n13["IRE_raise_the_irish_brigade"]
    end
    subgraph tier_4["Tier 4"]
        n14["IRE_free_trade"]
        n15["IRE_protectionism"]
        n16["IRE_rid_alien_influence"]
    end
    subgraph tier_5["Tier 5"]
        n17["IRE_british_arms"]
        n18["IRE_irelands_oppertunity"]
    end
    subgraph tier_6["Tier 6"]
        n19["IRE_claim_the_celtic_world"]
    end
    n8 --> n10
    n8 --> n11
    n9 --> n11
    n14 --> n17
    n18 --> n19
    n6 --> n7
    n8 --> n12
    n9 --> n12
    n11 --> n14
    n12 --> n14
    n1 --> n3
    n15 --> n18
    n4 --> n8
    n3 --> n8
    n5 --> n8
    n4 --> n9
    n3 --> n9
    n5 --> n9
    n11 --> n15
    n12 --> n15
    n1 --> n4
    n9 --> n13
    n1 --> n5
    n13 --> n16
    n2 --> n6
    n1 --> n6
    n11 x--x n12
    n1 x--x n2
    n14 x--x n15
    n8 x--x n9
```

# IRE_finna_fail

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["IRE_fine_gael"]
        n2(("IRE_finna_fail"))
    end
    subgraph tier_1["Tier 1"]
        n20["IRE_abolish_the_upper_house"]
        n21["IRE_emergency_powers_act"]
        n22["IRE_push_the_constituition"]
        n6["IRE_treet"]
    end
    subgraph tier_2["Tier 2"]
        n23["IRE_broad_censorship_programs"]
        n7["IRE_coa"]
        n24["IRE_infectious_disease_wage"]
        n25["IRE_president_replacement"]
        n26["IRE_temporary_state_guidance"]
    end
    subgraph tier_3["Tier 3"]
        n27{"IRE_ira_defense_force_memebrship"}
        n28["IRE_recognize_the_palce_of_the_church"]
    end
    subgraph tier_4["Tier 4"]
        n29["IRE_northern_ireland_for_assistance"]
        n30["IRE_promote_neutrality"]
    end
    n2 --> n20
    n21 --> n23
    n6 --> n7
    n2 --> n21
    n22 --> n24
    n23 --> n27
    n26 --> n27
    n27 --> n29
    n22 --> n25
    n27 --> n30
    n2 --> n22
    n24 --> n28
    n25 --> n28
    n21 --> n26
    n2 --> n6
    n1 --> n6
    n1 x--x n2
    n29 x--x n30
```
