# MAN_tsr_pacify_the_countryside

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("MAN_tsr_pacify_the_countryside"))
    end
    subgraph tier_1["Tier 1"]
        n2{"MAN_tsr_army_modernization"}
        n3["MAN_tsr_invite_japanese_settlers"]
        n4{"MAN_tsr_trade_delegation"}
    end
    subgraph tier_2["Tier 2"]
        n5["MAN_tsr_assertiveness"]
        n6["MAN_tsr_collective_farms"]
        n7["MAN_tsr_expand_the_textile_industry"]
        n8["MAN_tsr_mukden_military_academy"]
        n9["MAN_tsr_obedience"]
    end
    subgraph tier_3["Tier 3"]
        n10["MAN_tsr_expand_the_navy"]
        n11["MAN_tsr_first_five_year_plan"]
        n12["MAN_tsr_hoankyoku"]
        n13["MAN_tsr_law_university"]
        n14{"MAN_tsr_request_control_of_the_railways"}
    end
    subgraph tier_4["Tier 4"]
        n15["MAN_tsr_alliance_with_the_kwantung_army"]
        n16{"MAN_tsr_five_equal_peoples"}
        n17["MAN_tsr_invite_japanese_investors"]
        n18["MAN_tsr_mukden_arsenal"]
        n19["MAN_tsr_research_and_education_department"]
        n20{"MAN_tsr_staff_the_court_with_manchus"}
    end
    subgraph tier_5["Tier 5"]
        n21["MAN_tsr_bolster_nationalism"]
        n22["MAN_tsr_empower_the_legislative_council"]
        n23["MAN_tsr_expand_showa_steel_works"]
        n24["MAN_tsr_expand_the_imperial_guards"]
        n25["MAN_tsr_expand_the_railways"]
        n26["MAN_tsr_further_mobilization"]
        n27["MAN_tsr_mamc"]
        n28["MAN_tsr_question_the_emperors_authority"]
        n29["MAN_tsr_request_dalian"]
        n30["MAN_tsr_strengthen_the_manchukuo_imperial_army"]
        n31["MAN_tsr_strengthen_ties_with_nissan"]
        n32["MAN_tsr_white_russian_advisers"]
    end
    subgraph tier_6["Tier 6"]
        n33["MAN_tsr_bandit_recruitment"]
        n34["MAN_tsr_develop_aluminum_sources"]
        n35["MAN_tsr_expand_xingan_army"]
        n36["MAN_tsr_five_people_armies"]
        n37["MAN_tsr_local_arms_procurement"]
        n38["MAN_tsr_mangyo"]
        n39["MAN_tsr_purge_the_general_affairs_council"]
        n40["MAN_tsr_social_research_unit"]
        n41{"MAN_tsr_the_question_of_leadership"}
    end
    subgraph tier_7["Tier 7"]
        n42{"MAN_tsr_a_new_dawn_over_manchuria"}
        n43["MAN_tsr_ally_bandit_leaders"]
        n44["MAN_tsr_chinese_leadership"]
        n45["MAN_tsr_empire_of_manchukuo"]
        n46{"MAN_tsr_independence_war"}
        n47["MAN_tsr_persuade_the_IMPRP"]
        n48["MAN_tsr_reform_the_civil_service"]
        n49["MAN_tsr_second_five_year_plan"]
    end
    subgraph tier_8["Tier 8"]
        n50["MAN_tsr_a_new_constitution"]
        n51{"MAN_tsr_depose_puyi"}
        n52["MAN_tsr_embrace_state_shintoism"]
        n53["MAN_tsr_imperial_divinity"]
        n54["MAN_tsr_national_cooperation_government"]
        n55["MAN_tsr_national_defense_state"]
        n56["MAN_tsr_vassalize_mengukuo"]
    end
    subgraph tier_9["Tier 9"]
        n57["MAN_tsr_division_of_power"]
        n58["MAN_tsr_promote_manchu_identity"]
        n59["MAN_tsr_reclaim_our_lost_possessions"]
        n60["MAN_tsr_reestablish_the_qing_army"]
        n61["MAN_tsr_the_new_beiyang_government"]
        n62["MAN_tsr_the_two_emperors"]
        n63["MAN_tsr_work_with_the_kempeitai"]
        n64["MAN_tsr_zhao_shangzhis_coup"]
    end
    subgraph tier_10["Tier 10"]
        n65["MAN_tsr_ally_the_soviet_republic"]
        n66["MAN_tsr_beiyang_university"]
        n67["MAN_tsr_claim_outer_manchuria"]
        n68["MAN_tsr_raise_the_yong_ying"]
        n69{"MAN_tsr_reclaim_the_empire"}
        n70["MAN_tsr_reform_the_army"]
        n71["MAN_tsr_the_southern_expedition"]
    end
    subgraph tier_11["Tier 11"]
        n72["MAN_tsr_assert_our_authority"]
        n73["MAN_tsr_imperial_university"]
        n74["MAN_tsr_offer_vassalization"]
        n75["MAN_tsr_proclaim_the_republic_of_china"]
        n76["MAN_tsr_research_cooperation"]
        n77["MAN_tsr_soviet_aid"]
        n78["MAN_tsr_the_long_march_south"]
    end
    subgraph tier_12["Tier 12"]
        n79["MAN_tsr_a_new_self_strengthening_movement"]
        n80["MAN_tsr_an_industrial_power"]
        n81["MAN_tsr_finish_off_the_japanese_threat"]
        n82["MAN_tsr_move_capitals"]
        n83["MAN_tsr_proclaim_the_peoples_republic"]
        n84["MAN_tsr_reestablish_the_gansu_braves"]
        n85["MAN_tsr_request_our_lost_territories"]
    end
    subgraph tier_13["Tier 13"]
        n86["MAN_tsr_claim_the_mandate_of_heaven"]
    end
    n46 --> n50
    n33 --> n42
    n72 --> n79
    n74 --> n79
    n11 --> n15
    n33 --> n43
    n64 --> n65
    n75 --> n80
    n1 --> n2
    n69 --> n72
    n4 --> n5
    n28 --> n33
    n61 --> n66
    n20 --> n21
    n16 --> n21
    n41 --> n44
    n58 --> n67
    n63 --> n67
    n82 --> n86
    n3 --> n6
    n42 --> n51
    n23 --> n34
    n50 --> n57
    n45 --> n52
    n41 --> n45
    n16 --> n22
    n17 --> n23
    n20 --> n24
    n9 --> n10
    n17 --> n25
    n4 --> n7
    n30 --> n35
    n75 --> n81
    n9 --> n11
    n14 --> n16
    n32 --> n36
    n15 --> n26
    n9 --> n12
    n46 --> n53
    n69 --> n73
    n39 --> n46
    n11 --> n17
    n1 --> n3
    n6 --> n13
    n8 --> n13
    n7 --> n13
    n24 --> n37
    n18 --> n27
    n31 --> n38
    n23 --> n38
    n25 --> n38
    n72 --> n82
    n74 --> n82
    n11 --> n18
    n2 --> n8
    n44 --> n54
    n49 --> n55
    n2 --> n9
    n69 --> n74
    n33 --> n47
    n78 --> n83
    n71 --> n75
    n52 --> n58
    n21 --> n39
    n16 --> n28
    n60 --> n68
    n53 --> n59
    n60 --> n69
    n72 --> n84
    n74 --> n84
    n53 --> n60
    n50 --> n60
    n61 --> n70
    n39 --> n48
    n5 --> n14
    n15 --> n29
    n65 --> n85
    n78 --> n85
    n13 --> n19
    n65 --> n76
    n38 --> n49
    n25 --> n40
    n65 --> n77
    n14 --> n20
    n15 --> n30
    n17 --> n31
    n65 --> n78
    n51 --> n61
    n30 --> n41
    n26 --> n41
    n61 --> n71
    n56 --> n62
    n54 --> n62
    n1 --> n4
    n44 --> n56
    n16 --> n32
    n52 --> n63
    n51 --> n64
    n50 x--x n51
    n50 x--x n53
    n72 x--x n74
    n5 x--x n9
    n21 x--x n28
    n44 x--x n45
    n51 x--x n53
    n16 x--x n20
    n61 x--x n64
```
