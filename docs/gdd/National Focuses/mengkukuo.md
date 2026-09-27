# MEN_an_independent_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"MEN_an_independent_army"}
    end
    subgraph tier_1["Tier 1"]
        n2["MEN_continue_the_ways_of_old"]
        n3["MEN_embrace_horses_of_steel"]
    end
    subgraph tier_2["Tier 2"]
        n4["MEN_acquire_japanese_designs"]
        n5["MEN_breed_strong_horses"]
        n6["MEN_forces_for_the_south"]
        n7["MEN_motorization_of_the_army"]
        n8["MEN_rebuilding_the_disaster_of_suiyan"]
        n9["MEN_understanding_blitzkreig_doctine"]
    end
    subgraph tier_3["Tier 3"]
        n10["MEN_every_man_a_rifle"]
        n11["MEN_every_man_a_truck"]
        n12["MEN_integrate_the_grand_han_righteous_army"]
        n13["MEN_japanese_military_advisors"]
        n14["MEN_open_the_kalgan_military_academy"]
        n15["MEN_reorganize_the_command_chain"]
    end
    subgraph tier_4["Tier 4"]
        n16["MEN_establish_tank_workshops"]
        n17["MEN_modernize_our_artillery"]
        n18["MEN_train_the_officers"]
    end
    subgraph tier_5["Tier 5"]
        n19["MEN_masters_of_the_steppe"]
    end
    n3 --> n4
    n2 --> n5
    n1 --> n2
    n1 --> n3
    n11 --> n16
    n5 --> n10
    n6 --> n10
    n9 --> n11
    n7 --> n11
    n2 --> n6
    n8 --> n12
    n6 --> n13
    n18 --> n19
    n17 --> n19
    n10 --> n17
    n3 --> n7
    n8 --> n14
    n3 --> n8
    n2 --> n8
    n8 --> n15
    n10 --> n18
    n3 --> n9
    n2 x--x n3
```

# MEN_establish_the_bank_of_mengjiang

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20{"MEN_establish_the_bank_of_mengjiang"}
    end
    subgraph tier_1["Tier 1"]
        n21["MEN_fuel_for_the_war_machine"]
        n22["MEN_prioritize_industrialization"]
    end
    subgraph tier_2["Tier 2"]
        n23["MEN_exploit_suiyuan"]
        n24["MEN_japanese_backed_coal_plants"]
        n25["MEN_mongol_industral_investment"]
        n26["MEN_open_public_schools"]
        n27["MEN_open_suiyuan_mining_facilitys"]
        n28["MEN_trade_focus"]
    end
    subgraph tier_3["Tier 3"]
        n29["MEN_establish_the_daimo_koshi"]
        n30["MEN_from_steppes_into_factories"]
        n31["MEN_further_research_grants"]
    end
    subgraph tier_4["Tier 4"]
        n32["MEN_expand_chahar_arms_workshops"]
        n33["MEN_improve_regional_infastructure"]
        n34["MEN_industrialization_achieved"]
        n35["MEN_suiyuan_industry"]
    end
    n24 --> n29
    n27 --> n29
    n30 --> n32
    n21 --> n23
    n22 --> n23
    n28 --> n30
    n25 --> n30
    n20 --> n21
    n26 --> n31
    n29 --> n33
    n30 --> n34
    n21 --> n24
    n22 --> n25
    n21 --> n26
    n22 --> n26
    n21 --> n27
    n20 --> n22
    n23 --> n35
    n30 --> n35
    n22 --> n28
    n21 x--x n22
```

# MEN_petition_nima-odsor_to_stay_in_shangbei

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36["MEN_deal_with_the_bayannur_princes"]
        n37(("MEN_petition_nima-odsor_to_stay_in_shangbei"))
        n38["MEN_radicalize_the_peasants"]
        n39["MEN_strengthen_ties_with_japan"]
    end
    subgraph tier_1["Tier 1"]
        n40["MEN_consolidate_national_rule"]
        n41["MEN_root_out_japanese_loyality"]
    end
    subgraph tier_2["Tier 2"]
        n42{"MEN_compromise_with_nanjing"}
    end
    subgraph tier_3["Tier 3"]
        n43["MEN_no_country_for_fascist_sympathisers"]
        n44["MEN_reform_rather_then_change"]
    end
    subgraph tier_4["Tier 4"]
        n45["MEN_reform_the_mongolian_council"]
        n46{"MEN_reinvite_the_chinese_military"}
        n47{"MEN_tear_up_the_qin_doihara_agreement"}
    end
    subgraph tier_5["Tier 5"]
        n48{"MEN_the_principle_of_democracy"}
        n49{"MEN_the_principle_of_nationalism"}
    end
    subgraph tier_6["Tier 6"]
        n50{"MEN_fortify_the_capital"}
        n51["MEN_request_chinese_investment"]
        n52["MEN_strengthen_our_buddhist_identity"]
        n53["MEN_subdue_the_communist_threat"]
        n54["MEN_work_with_the_communists"]
    end
    subgraph tier_7["Tier 7"]
        n55["MEN_down_with_the_colonizer"]
        n56["MEN_embrace_the_new_life_movement"]
        n57["MEN_invite_western_scholars"]
        n58["MEN_request_suiyuan_and_ordos"]
        n59["MEN_transition_into_the_third_phase"]
    end
    subgraph tier_8["Tier 8"]
        n60["MEN_anti_japanese_stratagems"]
        n61["MEN_promote_confucian_principles"]
        n62["MEN_request_mongol_territories_dem"]
        n63["MEN_steer_the_industry"]
        n64["MEN_the_revival_of_the_spirit"]
    end
    subgraph tier_9["Tier 9"]
        n65["MEN_clean_the_cities"]
        n66["MEN_greater_mongolian_reunification"]
        n67["MEN_nationalism_democracy_welfare"]
    end
    subgraph tier_10["Tier 10"]
        n68["MEN_end_the_humiliation"]
    end
    n58 --> n60
    n55 --> n60
    n64 --> n65
    n61 --> n65
    n40 --> n42
    n41 --> n42
    n37 --> n40
    n50 --> n55
    n54 --> n56
    n53 --> n56
    n67 --> n68
    n49 --> n50
    n60 --> n66
    n51 --> n57
    n62 --> n67
    n63 --> n67
    n42 --> n43
    n56 --> n61
    n42 --> n44
    n43 --> n45
    n44 --> n45
    n44 --> n46
    n48 --> n51
    n59 --> n62
    n50 --> n58
    n37 --> n41
    n59 --> n63
    n36 --> n52
    n49 --> n52
    n49 --> n53
    n48 --> n53
    n43 --> n47
    n47 --> n48
    n46 --> n48
    n46 --> n49
    n56 --> n64
    n51 --> n59
    n49 --> n54
    n48 --> n54
    n55 x--x n58
    n43 x--x n44
    n37 x--x n38
    n37 x--x n39
    n53 x--x n54
    n48 x--x n49
```

# MEN_radicalize_the_peasants

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n37["MEN_petition_nima-odsor_to_stay_in_shangbei"]
        n38{"MEN_radicalize_the_peasants"}
        n39["MEN_strengthen_ties_with_japan"]
    end
    subgraph tier_1["Tier 1"]
        n69["MEN_contact_the_communists"]
        n70["MEN_reach_out_to_the_soviets"]
    end
    subgraph tier_2["Tier 2"]
        n71["MEN_establish_peasant_militias"]
    end
    subgraph tier_3["Tier 3"]
        n72{"MEN_the_second_bailingmiao_uprising"}
    end
    subgraph tier_4["Tier 4"]
        n73["MEN_favour_the_cooperationists"]
        n74["MEN_invite_ulanhu_from_mongolia"]
    end
    subgraph tier_5["Tier 5"]
        n75["MEN_promote_chinese_unity"]
        n76["MEN_request_soviet_industrial_aid"]
        n77["MEN_soviet_mongol_military_cooperation"]
    end
    subgraph tier_6["Tier 6"]
        n78["MEN_cooperate_with_china"]
        n79["MEN_nationalize_key_industry"]
        n80{"MEN_stamp_out_fascist_sympathies"}
    end
    subgraph tier_7["Tier 7"]
        n81["MEN_integrate_the_chinese_into_the_army"]
        n82["MEN_join_the_comintern"]
        n83["MEN_loyalty_to_the_maoists"]
    end
    subgraph tier_8["Tier 8"]
        n84["MEN_fund_communists_in_kmt"]
        n85{"MEN_join_the_united_front"}
        n86{"MEN_joint_invasion_of_shx"}
        n87["MEN_propose_mongol_unification"]
    end
    subgraph tier_9["Tier 9"]
        n88["MEN_beacon_of_resistance"]
        n89{"MEN_behead_the_cornered_fox"}
        n90["MEN_down_with_the_generalissimo"]
        n91["MEN_focus_on_the_greater_threat"]
    end
    subgraph tier_10["Tier 10"]
        n92{"MEN_form_the_inner_mongolia_autonomous_region"}
        n93["MEN_pivot_to_the_west"]
        n94["MEN_prioritize_the_eastern_threat"]
        n95["MEN_the_honour_of_death"]
    end
    subgraph tier_11["Tier 11"]
        n96["MEN_ask_the_prc_to_return_our_lands"]
        n97["MEN_fortify_the_east"]
        n98["MEN_fortify_the_south"]
        n99["MEN_reclaim_our_lands"]
        n100["MEN_soviet_mongol_mutual_assistance"]
    end
    subgraph tier_12["Tier 12"]
        n101["MEN_liberate_the_tuvans"]
        n102["MEN_swallow_the_rising_sun"]
    end
    n92 --> n96
    n85 --> n88
    n87 --> n89
    n38 --> n69
    n75 --> n78
    n86 --> n90
    n70 --> n71
    n69 --> n71
    n72 --> n73
    n86 --> n91
    n85 --> n91
    n91 --> n92
    n90 --> n92
    n94 --> n97
    n94 --> n98
    n83 --> n84
    n82 --> n84
    n78 --> n81
    n79 --> n81
    n72 --> n74
    n80 --> n82
    n81 --> n85
    n83 --> n86
    n96 --> n101
    n99 --> n101
    n80 --> n83
    n75 --> n79
    n89 --> n93
    n89 --> n94
    n73 --> n75
    n82 --> n87
    n38 --> n70
    n92 --> n99
    n74 --> n76
    n74 --> n77
    n93 --> n100
    n76 --> n80
    n77 --> n80
    n98 --> n102
    n97 --> n102
    n88 --> n95
    n71 --> n72
    n96 x--x n99
    n69 x--x n70
    n90 x--x n91
    n73 x--x n74
    n82 x--x n83
    n37 x--x n38
    n93 x--x n94
    n38 x--x n39
```

# MEN_strengthen_ties_with_japan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n37["MEN_petition_nima-odsor_to_stay_in_shangbei"]
        n38["MEN_radicalize_the_peasants"]
        n39(("MEN_strengthen_ties_with_japan"))
        n49["MEN_the_principle_of_nationalism"]
    end
    subgraph tier_1["Tier 1"]
        n103["MEN_the_state_founding_conference"]
    end
    subgraph tier_2["Tier 2"]
        n104["MEN_eradicate_communist_resistance"]
        n105["MEN_realize_the_zenrin_kyokai"]
    end
    subgraph tier_3["Tier 3"]
        n106["MEN_prepare_the_western_front"]
        n107["MEN_sign_the_mutual_assistance_agreement"]
    end
    subgraph tier_4["Tier 4"]
        n108{"MEN_put_an_end_to_the_raids"}
    end
    subgraph tier_5["Tier 5"]
        n109["MEN_servants_of_the_empire"]
        n110["MEN_the_spirit_of_genghis"]
    end
    subgraph tier_6["Tier 6"]
        n36["MEN_deal_with_the_bayannur_princes"]
        n111["MEN_loyalty_to_the_kwantung"]
        n112["MEN_promote_harmony_of_the_five_races"]
        n113["MEN_propse_the_formation_of_mengjiang"]
    end
    subgraph tier_7["Tier 7"]
        n114["MEN_covert_chinese_cooperation"]
        n115["MEN_help_strike_our_old_oppressers"]
        n116["MEN_reunite_our_people"]
        n52["MEN_strengthen_our_buddhist_identity"]
    end
    subgraph tier_8["Tier 8"]
        n117["MEN_eyes_behind_enemy_lines"]
        n118["MEN_request_mongol_territories"]
        n119["MEN_sabotage_the_kwantung"]
    end
    subgraph tier_9["Tier 9"]
        n120["MEN_join_the_anti_japanese_struggle"]
        n121["MEN_our_place_under_the_red_sun"]
    end
    subgraph tier_10["Tier 10"]
        n122["MEN_liberation_or_death"]
    end
    n36 --> n114
    n110 --> n36
    n103 --> n104
    n114 --> n117
    n111 --> n115
    n117 --> n120
    n119 --> n120
    n120 --> n122
    n109 --> n111
    n118 --> n121
    n104 --> n106
    n105 --> n106
    n109 --> n112
    n110 --> n113
    n109 --> n113
    n106 --> n108
    n103 --> n105
    n116 --> n118
    n115 --> n118
    n111 --> n116
    n114 --> n119
    n108 --> n109
    n105 --> n107
    n36 --> n52
    n49 --> n52
    n108 --> n110
    n39 --> n103
    n37 x--x n39
    n38 x--x n39
    n109 x--x n110
```
