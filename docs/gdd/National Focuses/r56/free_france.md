# FRA_appeal_to_the_french_nation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("FRA_appeal_to_the_french_nation"))
        n2["FRA_cooperation_with_the_communists"]
        n3["FRA_the_civil_and_military_organization"]
    end
    subgraph tier_1["Tier 1"]
        n4["FRA_appeal_to_overseas_territories"]
        n5["FRA_continue_the_fight"]
    end
    subgraph tier_2["Tier 2"]
        n6["FRA_colonial_recruitment"]
        n7["FRA_equatorial_african_gold_mining"]
        n8["FRA_intervention_in_central_africa"]
        n9["FRA_intervention_in_indochina"]
        n10["FRA_intervention_in_madagascar"]
        n11["FRA_intervention_in_north_africa"]
        n12["FRA_intervention_in_syria"]
        n13["FRA_intervention_in_west_africa"]
        n14["FRA_radio_brazzaville"]
        n15["FRA_the_free_french_navy"]
        n16["FRA_the_regiment_normandie"]
    end
    subgraph tier_3["Tier 3"]
        n17["FRA_an_african_army"]
        n18["FRA_exploit_rubber_vines"]
        n19["FRA_form_the_national_committee"]
        n20["FRA_improve_equatorial_roads"]
        n21["FRA_prepare_for_our_return"]
    end
    subgraph tier_4["Tier 4"]
        n22["FRA_form_the_provisional_government_of_the_republic"]
        n23["FRA_improved_logistics"]
        n24["FRA_national_council_of_the_resistance"]
    end
    subgraph tier_5["Tier 5"]
        n25["FRA_french_forces_of_the_interior"]
        n26["FRA_national_uprising"]
    end
    n6 --> n17
    n1 --> n4
    n5 --> n6
    n1 --> n5
    n4 --> n7
    n7 --> n18
    n10 --> n19
    n12 --> n19
    n9 --> n19
    n11 --> n19
    n13 --> n19
    n8 --> n19
    n19 --> n22
    n24 --> n25
    n7 --> n20
    n17 --> n23
    n4 --> n8
    n4 --> n9
    n4 --> n10
    n4 --> n11
    n4 --> n12
    n4 --> n13
    n3 --> n24
    n2 --> n24
    n19 --> n24
    n24 --> n26
    n15 --> n21
    n4 --> n14
    n5 --> n15
    n5 --> n16
```

# FRA_refus_absurde

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19["FRA_form_the_national_committee"]
        n27(("FRA_refus_absurde"))
    end
    subgraph tier_1["Tier 1"]
        n28["FRA_connections_to_industrialists"]
        n29["FRA_reach_out_to_trade_unions"]
        n30["FRA_the_maquis"]
    end
    subgraph tier_2["Tier 2"]
        n2["FRA_cooperation_with_the_communists"]
        n3["FRA_the_civil_and_military_organization"]
    end
    subgraph tier_3["Tier 3"]
        n24["FRA_national_council_of_the_resistance"]
    end
    subgraph tier_4["Tier 4"]
        n25["FRA_french_forces_of_the_interior"]
        n26["FRA_national_uprising"]
    end
    n27 --> n28
    n29 --> n2
    n24 --> n25
    n3 --> n24
    n2 --> n24
    n19 --> n24
    n24 --> n26
    n27 --> n29
    n28 --> n3
    n27 --> n30
```
