# SOV_civil_war_konev

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SOV_civil_war_konev"))
        n2["SOV_civil_war_power_struggle"]
    end
    subgraph tier_1["Tier 1"]
        n3["SOV_civil_war_conduct_mass_arrests"]
        n4["SOV_civil_war_implament_recovery_programs"]
        n5["SOV_civil_war_rehabilitate_military"]
    end
    subgraph tier_2["Tier 2"]
        n6["SOV_civil_war_empower_khrushchev"]
    end
    n1 --> n3
    n5 --> n6
    n3 --> n6
    n4 --> n6
    n1 --> n4
    n1 --> n5
    n1 x--x n2
```

# SOV_civil_war_power_struggle

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["SOV_civil_war_konev"]
        n2{"SOV_civil_war_power_struggle"}
    end
    subgraph tier_1["Tier 1"]
        n7["SOV_civil_war_in_the_name_of_the_czar"]
        n8{"SOV_civil_war_new_vozhd"}
        n9["SOV_civil_war_peoples_virtue"]
    end
    subgraph tier_2["Tier 2"]
        n10["SOV_civil_war_adopt_soviet_policies"]
        n11["SOV_civil_war_amnesty_for_political_opponents"]
        n12["SOV_civil_war_form_solider_committees"]
        n13["SOV_civil_war_form_the_white_emigres"]
        n14["SOV_civil_war_promote_the_asno_detachment"]
        n15["SOV_civil_war_purge_splinter_factions"]
    end
    subgraph tier_3["Tier 3"]
        n16["SOV_civil_war_abolish_death_penalty"]
        n17["SOV_civil_war_agrarian_socialism"]
        n18["SOV_civil_war_cultural_autonomy"]
        n19["SOV_civil_war_follow_corportism"]
        n20["SOV_civil_war_orthadox_resurgance"]
        n21["SOV_civil_war_reinstate_royal_exiles"]
        n22["SOV_civil_war_white_exiles"]
    end
    subgraph tier_4["Tier 4"]
        n23["SOV_civil_war_accept_constituion"]
        n24{"SOV_civil_war_commit_to_the_orthodox_church"}
        n25["SOV_civil_war_create_a_national_directory"]
        n26["SOV_civil_war_impose_national_unions"]
        n27["SOV_civil_war_purge_religous_beurocracy"]
        n28{"SOV_civil_war_reject_cosmopolitanism"}
    end
    subgraph tier_5["Tier 5"]
        n29["SOV_civil_war_russian_women_fascist_movement"]
        n30["SOV_civil_war_the_free_russian_people"]
        n31["SOV_civil_war_union_of_fascist_little_ones"]
    end
    subgraph tier_6["Tier 6"]
        n32["SOV_civil_war_all_russian_alligences"]
        n33["SOV_civil_war_baltic_freedom"]
        n34["SOV_civil_war_polish_autonomy"]
    end
    subgraph tier_7["Tier 7"]
        n35["SOV_civil_war_imperial_legacy"]
    end
    subgraph tier_8["Tier 8"]
        n36["SOV_civil_war_reclaim_polish_overlordship"]
        n37["SOV_civil_war_rule_over_the_mongols"]
        n38["SOV_civil_war_solve_the_karelian_question"]
    end
    subgraph tier_9["Tier 9"]
        n39["SOV_civil_war_crush_our_eastern_rival"]
        n40["SOV_civil_war_our_american_holding"]
        n41["SOV_civil_war_reclaim_bessarabia"]
    end
    n11 --> n16
    n12 --> n16
    n20 --> n23
    n22 --> n23
    n7 --> n10
    n11 --> n17
    n12 --> n17
    n31 --> n32
    n29 --> n32
    n9 --> n11
    n30 --> n33
    n19 --> n24
    n17 --> n25
    n16 --> n25
    n18 --> n25
    n37 --> n39
    n11 --> n18
    n12 --> n18
    n14 --> n19
    n13 --> n19
    n9 --> n12
    n8 --> n13
    n23 --> n35
    n32 --> n35
    n19 --> n26
    n2 --> n7
    n2 --> n8
    n10 --> n20
    n37 --> n40
    n2 --> n9
    n30 --> n34
    n8 --> n14
    n17 --> n27
    n16 --> n27
    n18 --> n27
    n7 --> n15
    n36 --> n41
    n35 --> n36
    n10 --> n21
    n15 --> n21
    n19 --> n28
    n35 --> n37
    n28 --> n29
    n35 --> n38
    n25 --> n30
    n27 --> n30
    n24 --> n31
    n15 --> n22
    n13 x--x n14
    n7 x--x n8
    n7 x--x n9
    n1 x--x n2
    n8 x--x n9
    n29 x--x n31
```
