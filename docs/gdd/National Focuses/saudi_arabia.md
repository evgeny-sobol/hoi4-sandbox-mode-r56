# SAU_army_focus_1

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"SAU_army_focus_1"}
    end
    subgraph tier_1["Tier 1"]
        n2["SAU_army_infantry"]
        n3["SAU_incorporate_nomad_tactics"]
        n4["SAU_motorization"]
        n5["SAU_yemen_lessons"]
    end
    subgraph tier_2["Tier 2"]
        n6["SAU_army_infantry_desert"]
        n7["SAU_camelry_expertise"]
        n8["SAU_encourage_general_creativity"]
        n9["SAU_support_companies"]
    end
    subgraph tier_3["Tier 3"]
        n10["SAU_artillery"]
        n11["SAU_land_doctrine1"]
        n12["SAU_romanticize_army"]
        n13["SAU_special_forces_focus"]
        n14["SAU_tank_focus"]
    end
    subgraph tier_4["Tier 4"]
        n15["SAU_develop_anti_tank_capabilities"]
        n16["SAU_general_army_buff"]
    end
    n1 --> n2
    n2 --> n6
    n6 --> n10
    n3 --> n7
    n10 --> n15
    n11 --> n15
    n5 --> n8
    n12 --> n16
    n13 --> n16
    n1 --> n3
    n6 --> n11
    n1 --> n4
    n8 --> n12
    n7 --> n12
    n7 --> n13
    n9 --> n13
    n4 --> n9
    n9 --> n14
    n1 --> n5
    n3 x--x n4
```

# SAU_the_unifier

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"SAU_the_unifier"}
    end
    subgraph tier_1["Tier 1"]
        n18{"SAU_reject_the_riyadh_line"}
        n19{"SAU_solve_the_jafurah_dispute"}
    end
    subgraph tier_2["Tier 2"]
        n20["SAU_2_Invite_the_Soviet_oil_barons"]
        n21["SAU_concessions_to_standard_oil"]
        n22["SAU_deal_with_bp"]
        n23["SAU_invite_brabag"]
    end
    subgraph tier_3["Tier 3"]
        n24{"SAU_improve_our_infrastructure"}
        n25{"SAU_invite_foreign_investors"}
        n26{"SAU_liberalize_the_market"}
        n27{"SAU_placate_the_tribes"}
    end
    subgraph tier_4["Tier 4"]
        n28{"SAU_diplomacy_in_the_sand"}
    end
    subgraph tier_5["Tier 5"]
        n29["SAU_continue_hakimovs_legacy"]
        n30["SAU_introduce_the_constitution"]
        n31["SAU_seek_german_arms"]
    end
    subgraph tier_6["Tier 6"]
        n32["SAU_democraticize_the_administration"]
        n33["SAU_enforce_the_zakat"]
        n34["SAU_enocurage_the_hajj"]
        n35["SAU_expand_the_riyadh_university"]
        n36["SAU_force_tribes_to_settle"]
        n37{"SAU_invite_western_advisors"}
        n38{"SAU_provide_shelter_for_fritz_gobba"}
        n39["SAU_reform_the_tax_system"]
    end
    subgraph tier_7["Tier 7"]
        n40{"SAU_influence_the_king"}
        n41["SAU_move_toward_german_alignment"]
        n42["SAU_western_alignment"]
    end
    subgraph tier_8["Tier 8"]
        n43["SAU_USS_quincy_meeting"]
        n44["SAU_enact_censorship"]
        n45{"SAU_increase_oil_exportations_to_the_allies"}
        n46["SAU_join_the_comintern"]
        n47["SAU_maintain_international_neutrality"]
        n48["SAU_request_german_guns"]
        n49{"SAU_spread_islam_force"}
    end
    subgraph tier_9["Tier 9"]
        n50["SAU_awoken_generation"]
        n51["SAU_deterrence"]
        n52["SAU_five_year_plan"]
        n53["SAU_form_a_volunteer_force"]
        n54["SAU_old_traditions"]
        n55{"SAU_political_correctness"}
    end
    subgraph tier_10["Tier 10"]
        n56["SAU_ask_british_colonies"]
        n57["SAU_destabilize_the_east"]
    end
    subgraph tier_11["Tier 11"]
        n58["SAU_attack_iran"]
        n59["SAU_attack_turkey"]
        n60["SAU_crush_the_golden_square"]
        n61{"SAU_war_with_yemen_and_oman"}
    end
    subgraph tier_12["Tier 12"]
        n62["SAU_autonomy_for_south_arabia"]
        n63["SAU_claim_the_sinai"]
        n64["SAU_establish_labor_camps"]
    end
    subgraph tier_13["Tier 13"]
        n65["SAU_our_rightful_domain"]
    end
    n18 --> n20
    n42 --> n43
    n45 --> n56
    n49 --> n56
    n55 --> n56
    n57 --> n58
    n57 --> n59
    n61 --> n62
    n46 --> n50
    n58 --> n63
    n59 --> n63
    n19 --> n21
    n18 --> n21
    n28 --> n29
    n56 --> n60
    n19 --> n22
    n30 --> n32
    n49 --> n57
    n55 --> n57
    n47 --> n51
    n26 --> n28
    n27 --> n28
    n41 --> n44
    n31 --> n33
    n29 --> n33
    n31 --> n34
    n61 --> n64
    n31 --> n35
    n30 --> n35
    n29 --> n35
    n46 --> n52
    n30 --> n36
    n31 --> n36
    n29 --> n36
    n42 --> n53
    n47 --> n53
    n22 --> n24
    n42 --> n45
    n33 --> n40
    n39 --> n40
    n28 --> n30
    n26 --> n30
    n24 --> n30
    n18 --> n23
    n23 --> n25
    n30 --> n37
    n40 --> n46
    n22 --> n26
    n21 --> n26
    n37 --> n47
    n40 --> n47
    n38 --> n47
    n38 --> n41
    n49 --> n54
    n63 --> n65
    n20 --> n27
    n23 --> n27
    n46 --> n55
    n31 --> n38
    n30 --> n39
    n29 --> n39
    n17 --> n18
    n41 --> n48
    n28 --> n31
    n25 --> n31
    n27 --> n31
    n26 --> n31
    n17 --> n19
    n41 --> n49
    n57 --> n61
    n56 --> n61
    n37 --> n42
    n20 x--x n21
    n20 x--x n22
    n20 x--x n23
    n56 x--x n57
    n62 x--x n64
    n21 x--x n22
    n21 x--x n23
    n29 x--x n30
    n29 x--x n31
    n22 x--x n23
    n30 x--x n31
    n46 x--x n47
    n46 x--x n41
    n46 x--x n42
    n47 x--x n41
    n47 x--x n42
    n41 x--x n42
    n18 x--x n19
```
