# CSA_rebuild_the_confederate_industry

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CSA_rebuild_the_confederate_industry"))
        n2["GEN_Ships_England"]
    end
    subgraph tier_1["Tier 1"]
        n3["CSA_focus_on_civilian_department"]
        n4["CSA_focus_on_military_department"]
        n5["CSA_rural_education_act"]
    end
    subgraph tier_2["Tier 2"]
        n6["CSA_electrification_of_the_countryside"]
        n7["CSA_invest_tennessee_mining"]
        n8["CSA_lake_city_ammunition"]
        n9["CSA_rebuild_richmond_industry"]
    end
    subgraph tier_3["Tier 3"]
        n10["CSA_expand_louisiana_texas_railway"]
        n11["CSA_hydraulic_plants"]
        n12["CSA_invest_virginia_tungsten"]
        n13["CSA_rubber_reserve_company"]
    end
    subgraph tier_4["Tier 4"]
        n14["CSA_develop_the_midwest"]
        n15["CSA_expand_new_orleans_shipping"]
        n16["CSA_national_defense_funds"]
    end
    n11 --> n14
    n10 --> n14
    n3 --> n6
    n9 --> n10
    n2 --> n15
    n11 --> n15
    n1 --> n3
    n1 --> n4
    n6 --> n11
    n4 --> n7
    n7 --> n12
    n4 --> n8
    n13 --> n16
    n12 --> n16
    n3 --> n9
    n8 --> n13
    n1 --> n5
```

# CSA_restablish_the_confederate_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17(("CSA_restablish_the_confederate_army"))
    end
    subgraph tier_1["Tier 1"]
        n18{"CSA_war_powers_act"}
    end
    subgraph tier_2["Tier 2"]
        n19["CSA_claim_the_caribbean"]
        n20["CSA_eliminate_the_southern_threat"]
        n21["CSA_invite_synarchist_mexico"]
        n22["CSA_secure_mexico"]
        n23["CSA_secure_the_neutral_states"]
    end
    n18 --> n19
    n18 --> n20
    n18 --> n21
    n18 --> n22
    n18 --> n23
    n17 --> n18
    n20 x--x n21
    n20 x--x n22
    n21 x--x n22
```
