# VIC_emergency_powers_to_petain

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("VIC_emergency_powers_to_petain"))
    end
    subgraph tier_1["Tier 1"]
        n2["VIC_armistice_army"]
        n3["VIC_the_legionary_service_order"]
        n4["VIC_the_national_bureau_of_statistics"]
        n5["VIC_the_national_revolution"]
    end
    subgraph tier_2["Tier 2"]
        n6["VIC_anti_bolshevist_volunteers"]
        n7["VIC_chantiers_de_la_jeunesse"]
        n8["VIC_down_with_marianne"]
        n9["VIC_form_the_milice"]
        n10["VIC_long_term_economic_planning"]
        n11["VIC_prosecute_the_losers"]
        n12["VIC_rebuild_the_military"]
    end
    subgraph tier_3["Tier 3"]
        n13["VIC_concessions_to_the_germans"]
        n14["VIC_finish_the_naval_buildup"]
        n15["VIC_hidden_materials"]
        n16["VIC_modernize_the_airforce"]
        n17["VIC_police_nationale"]
        n18["VIC_rationing"]
    end
    subgraph tier_4["Tier 4"]
        n19["VIC_aid_small_businesses"]
        n20["VIC_analyze_our_defeat"]
        n21["VIC_gazogenes_and_michelin_tires"]
        n22["VIC_learn_from_the_enemy"]
        n23["VIC_mandatory_work_service"]
        n24["VIC_negociate_the_release_of_officers"]
        n25["VIC_up_with_jean_darc"]
    end
    subgraph tier_5["Tier 5"]
        n26["VIC_buy_from_the_enemy"]
        n27["VIC_celebrate_motherhood"]
        n28["VIC_phalange_africaine"]
        n29["VIC_reinforce_the_STO"]
        n30["VIC_venerate_the_craftsman"]
    end
    subgraph tier_6["Tier 6"]
        n31["VIC_a_nation_reborn"]
    end
    subgraph tier_7["Tier 7"]
        n32["VIC_end_the_occupation"]
    end
    n27 --> n31
    n30 --> n31
    n29 --> n31
    n24 --> n31
    n18 --> n19
    n15 --> n20
    n3 --> n6
    n1 --> n2
    n22 --> n26
    n25 --> n27
    n2 --> n7
    n11 --> n13
    n5 --> n8
    n31 --> n32
    n12 --> n14
    n3 --> n9
    n18 --> n21
    n12 --> n15
    n16 --> n22
    n5 --> n10
    n13 --> n23
    n12 --> n16
    n7 --> n24
    n13 --> n24
    n24 --> n28
    n8 --> n17
    n5 --> n11
    n10 --> n18
    n2 --> n12
    n23 --> n29
    n1 --> n3
    n1 --> n4
    n1 --> n5
    n17 --> n25
    n19 --> n30
```
