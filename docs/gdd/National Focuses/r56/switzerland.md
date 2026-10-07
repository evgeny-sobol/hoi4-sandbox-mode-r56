# SWI_armed_neutrality

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"SWI_armed_neutrality"}
    end
    subgraph tier_1["Tier 1"]
        n2["SWI_frontier_defense_plan"]
        n3["SWI_national_defense_fund"]
        n4["SWI_promote_guisan"]
    end
    subgraph tier_2["Tier 2"]
        n5["SWI_all_adults_training"]
        n6["SWI_fight_until_death"]
        n7["SWI_fortify_border_with_france"]
        n8["SWI_fortify_border_with_germany"]
        n9["SWI_fortify_border_with_italy"]
        n10["SWI_increase_defense_budget"]
        n11["SWI_liechtenstein_defence_plan"]
        n12["SWI_national_redoubt"]
        n13["SWI_patriotic_shooting_clubs"]
        n14["SWI_spirit_of_saint_bernard"]
    end
    subgraph tier_3["Tier 3"]
        n15["SWI_aktion_nationaler_widerstand"]
        n16{"SWI_expand_weapons_industry"}
        n17{"SWI_expedite_mobilization"}
        n18["SWI_reduce_military_training_age"]
        n19["SWI_support_the_liechtensteiner_army"]
        n20["SWI_total_defense"]
        n21["SWI_train_swiss_women"]
        n22["SWI_veteran_sharpshooter_divisions"]
    end
    subgraph tier_4["Tier 4"]
        n23["SWI_alpine_specialization"]
        n24["SWI_anti_tank_divisions"]
        n25["SWI_citizen_supply_mandate"]
        n26["SWI_fortify_the_jura"]
        n27["SWI_heer_und_haus"]
        n28["SWI_prepare_infrastructure_and_industry"]
        n29["SWI_rig_infrastructure_to_blow"]
        n30["SWI_swiss_armored_divisions"]
        n31{"SWI_the_army_position"}
    end
    subgraph tier_5["Tier 5"]
        n32["SWI_air_research"]
        n33["SWI_attack_from_the_mountains"]
        n34["SWI_emergency_industry"]
        n35["SWI_fortify_sargans_gotthard_and_st_maurice"]
        n36["SWI_fortify_ticino"]
        n37["SWI_integrate_refugees_into_the_army"]
        n38["SWI_luftschutz"]
        n39["SWI_ortswehren"]
        n40["SWI_prolonged_service"]
        n41["SWI_swiss_heavy_planes"]
        n42["SWI_tank_development"]
    end
    subgraph tier_6["Tier 6"]
        n43["SWI_air_production"]
        n44["SWI_artillery"]
        n45["SWI_defend_the_skies"]
        n46["SWI_enhanced_training"]
        n47["SWI_expand_special_forces"]
        n48["SWI_expanded_military_support"]
        n49["SWI_mechanized_support"]
        n50["SWI_spirit_of_resistance"]
    end
    subgraph tier_7["Tier 7"]
        n51["SWI_industrial_production"]
        n52["SWI_mountaneer_paratroopers"]
    end
    n41 --> n43
    n32 --> n43
    n23 --> n32
    n13 --> n15
    n4 --> n5
    n2 --> n5
    n16 --> n23
    n22 --> n24
    n42 --> n44
    n26 --> n33
    n22 --> n25
    n18 --> n25
    n33 --> n45
    n34 --> n45
    n29 --> n34
    n40 --> n46
    n35 --> n47
    n36 --> n47
    n10 --> n16
    n37 --> n48
    n12 --> n17
    n2 --> n6
    n2 --> n7
    n2 --> n8
    n2 --> n9
    n25 --> n35
    n17 --> n26
    n25 --> n36
    n1 --> n2
    n15 --> n27
    n3 --> n10
    n49 --> n51
    n44 --> n51
    n31 --> n37
    n4 --> n11
    n2 --> n11
    n27 --> n38
    n42 --> n49
    n43 --> n52
    n1 --> n3
    n4 --> n12
    n27 --> n39
    n4 --> n13
    n2 --> n13
    n22 --> n28
    n18 --> n28
    n31 --> n40
    n1 --> n4
    n5 --> n18
    n17 --> n29
    n38 --> n50
    n39 --> n50
    n4 --> n14
    n2 --> n14
    n11 --> n19
    n16 --> n30
    n23 --> n41
    n30 --> n42
    n20 --> n31
    n6 --> n20
    n13 --> n21
    n5 --> n22
    n23 x--x n30
    n26 x--x n29
    n2 x--x n4
    n37 x--x n40
```

# SWI_back_the_national_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n53{"SWI_back_the_national_front"}
        n54["SWI_closer_democratic_ties"]
        n55{"SWI_reaffirm_spiritual_defense"}
    end
    subgraph tier_1["Tier 1"]
        n56["SWI_allied_gold"]
        n57["SWI_ban_the_communist_party"]
        n58["SWI_federal_police"]
        n59{"SWI_gotthard_union"}
        n60["SWI_seek_trade_agreement_with_germany"]
        n61["SWI_the_petition_of_the_200"]
        n62{"SWI_withdraw_from_the_league_of_nations"}
    end
    subgraph tier_2["Tier 2"]
        n63["SWI_axis_gold"]
        n64["SWI_closer_ties_with_germany"]
        n65["SWI_neutral_entente"]
        n66["SWI_panoramaheim_branch"]
        n67{"SWI_press_for_vorarlberg"}
        n68["SWI_seek_allied_trade"]
        n69["SWI_spab_counter_intelligence_agency"]
        n70["SWI_switzerland_on_the_offense"]
    end
    subgraph tier_3["Tier 3"]
        n71["SWI_crack_down_on_dissent"]
        n72["SWI_german_industrial_investments"]
        n73["SWI_infiltrate_federal_police"]
        n74["SWI_intervention_in_liechtenstein"]
        n75["SWI_limited_censorship_of_the_press"]
        n76["SWI_military_exercises_with_germany"]
        n77["SWI_pre_empt_anschluss"]
        n78["SWI_the_new_eidgenossenschaft"]
    end
    subgraph tier_4["Tier 4"]
        n79{"SWI_abandon_neutrality"}
        n80["SWI_alpine_redoubt"]
        n81["SWI_demand_french_alps"]
        n82["SWI_demand_italian_alps"]
        n83["SWI_expand_federal_police_intelligence"]
        n84["SWI_expand_the_confederation"]
        n85["SWI_tighten_press_censorship"]
    end
    subgraph tier_5["Tier 5"]
        n86["SWI_case_west"]
        n87["SWI_complete_siegfried_line"]
        n88["SWI_empower_the_council"]
        n89["SWI_martial_law"]
        n90["SWI_promote_henne"]
        n91["SWI_promote_tobler"]
        n92["SWI_the_alpine_protectorate"]
    end
    subgraph tier_6["Tier 6"]
        n93["SWI_ban_democratic_party"]
        n94["SWI_become_german_puppet"]
        n95["SWI_bring_democracy_to_germany"]
        n96["SWI_german_military_collaboration"]
        n97["SWI_liberate_italy"]
        n98["SWI_president_for_life"]
        n99["SWI_propagandize_swiss_military_tradition"]
        n100["SWI_take_over_france"]
    end
    subgraph tier_7["Tier 7"]
        n101["SWI_ask_for_vorarlberg"]
        n102["SWI_centralize_switzerland"]
        n103["SWI_guisans_coup"]
        n104["SWI_professionalize_militias"]
    end
    subgraph tier_8["Tier 8"]
        n105["SWI_join_the_axis"]
        n106["SWI_request_austrian_occupation"]
        n107["SWI_request_french_alps_occupation"]
        n108["SWI_request_italian_alps_occupation"]
        n109["SWI_return_to_the_old_switzerland"]
    end
    subgraph tier_9["Tier 9"]
        n110["SWI_the_alpine_supremacy"]
    end
    n64 --> n79
    n73 --> n79
    n55 --> n56
    n53 --> n56
    n77 --> n80
    n94 --> n101
    n60 --> n63
    n91 --> n93
    n55 --> n57
    n53 --> n57
    n90 --> n94
    n92 --> n95
    n79 --> n86
    n99 --> n102
    n93 --> n102
    n61 --> n64
    n79 --> n87
    n69 --> n71
    n77 --> n81
    n77 --> n82
    n84 --> n88
    n71 --> n83
    n78 --> n84
    n55 --> n58
    n53 --> n58
    n64 --> n72
    n91 --> n96
    n90 --> n96
    n55 --> n59
    n53 --> n59
    n92 --> n103
    n98 --> n103
    n66 --> n73
    n67 --> n74
    n104 --> n105
    n102 --> n105
    n92 --> n97
    n69 --> n75
    n83 --> n89
    n85 --> n89
    n64 --> n76
    n59 --> n65
    n53 --> n66
    n61 --> n66
    n67 --> n77
    n88 --> n98
    n59 --> n67
    n94 --> n104
    n96 --> n104
    n79 --> n90
    n79 --> n91
    n91 --> n99
    n101 --> n106
    n101 --> n107
    n101 --> n108
    n103 --> n109
    n56 --> n68
    n55 --> n60
    n53 --> n60
    n58 --> n69
    n59 --> n70
    n62 --> n70
    n92 --> n100
    n80 --> n92
    n81 --> n92
    n82 --> n92
    n106 --> n110
    n108 --> n110
    n107 --> n110
    n105 --> n110
    n67 --> n78
    n53 --> n61
    n75 --> n85
    n55 --> n62
    n53 --> n62
    n54 x--x n59
    n65 x--x n70
    n77 x--x n78
    n90 x--x n91
```

# SWI_reaffirm_spiritual_defense

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n53{"SWI_back_the_national_front"}
        n55{"SWI_reaffirm_spiritual_defense"}
    end
    subgraph tier_1["Tier 1"]
        n56["SWI_allied_gold"]
        n111{"SWI_ban_foreign_nazi_propaganda"}
        n57["SWI_ban_the_communist_party"]
        n58["SWI_federal_police"]
        n59{"SWI_gotthard_union"}
        n112{"SWI_pro_helvetia"}
        n60["SWI_seek_trade_agreement_with_germany"]
        n62{"SWI_withdraw_from_the_league_of_nations"}
    end
    subgraph tier_2["Tier 2"]
        n113["SWI_adopt_romansh"]
        n63["SWI_axis_gold"]
        n114["SWI_ban_national_movement_for_switzerland"]
        n115["SWI_buero_ha"]
        n54["SWI_closer_democratic_ties"]
        n65["SWI_neutral_entente"]
        n67{"SWI_press_for_vorarlberg"}
        n68["SWI_seek_allied_trade"]
        n69["SWI_spab_counter_intelligence_agency"]
        n116["SWI_support_allied_espionage"]
        n70["SWI_switzerland_on_the_offense"]
    end
    subgraph tier_3["Tier 3"]
        n117["SWI_american_industrial_investments"]
        n118{"SWI_connect_to_the_maginot_line"}
        n71["SWI_crack_down_on_dissent"]
        n119{"SWI_expand_spy_networks"}
        n74["SWI_intervention_in_liechtenstein"]
        n75["SWI_limited_censorship_of_the_press"]
        n77["SWI_pre_empt_anschluss"]
        n78["SWI_the_new_eidgenossenschaft"]
    end
    subgraph tier_4["Tier 4"]
        n80["SWI_alpine_redoubt"]
        n81["SWI_demand_french_alps"]
        n82["SWI_demand_italian_alps"]
        n83["SWI_expand_federal_police_intelligence"]
        n84["SWI_expand_the_confederation"]
        n120{"SWI_share_spy_networks"}
        n121{"SWI_take_a_stance"}
        n85["SWI_tighten_press_censorship"]
    end
    subgraph tier_5["Tier 5"]
        n88["SWI_empower_the_council"]
        n122["SWI_join_france"]
        n123["SWI_join_the_allies"]
        n89["SWI_martial_law"]
        n124["SWI_secret_pact_with_the_allies"]
        n92["SWI_the_alpine_protectorate"]
    end
    subgraph tier_6["Tier 6"]
        n95["SWI_bring_democracy_to_germany"]
        n125["SWI_case_north"]
        n126["SWI_fund_resistance_groups"]
        n127["SWI_intervention_in_liechtenstein_2"]
        n128["SWI_lay_the_groundwork"]
        n97["SWI_liberate_italy"]
        n129["SWI_oasis_of_democracy"]
        n98["SWI_president_for_life"]
        n100["SWI_take_over_france"]
        n130["SWI_the_second_helvetic_republic"]
    end
    subgraph tier_7["Tier 7"]
        n131["SWI_alpine_aspirations"]
        n132["SWI_arsenal_of_the_alps"]
        n133["SWI_export_saboteurs"]
        n134["SWI_freeze_german_assets"]
        n103["SWI_guisans_coup"]
        n135["SWI_volunteer_force"]
    end
    subgraph tier_8["Tier 8"]
        n136["SWI_fighting_for_the_hills"]
        n137["SWI_fly_over_the_mountains"]
        n109["SWI_return_to_the_old_switzerland"]
        n138["SWI_thunder_in_the_valleys"]
    end
    subgraph tier_9["Tier 9"]
        n139["SWI_weapons_of_democracy"]
    end
    subgraph tier_10["Tier 10"]
        n140["SWI_exiled_government"]
        n141["SWI_jump_into_action"]
        n142["SWI_the_alpine_confederation"]
    end
    n112 --> n113
    n55 --> n56
    n53 --> n56
    n130 --> n131
    n77 --> n80
    n54 --> n117
    n128 --> n132
    n60 --> n63
    n55 --> n111
    n111 --> n114
    n112 --> n114
    n55 --> n57
    n53 --> n57
    n92 --> n95
    n112 --> n115
    n123 --> n125
    n122 --> n125
    n124 --> n125
    n111 --> n54
    n54 --> n118
    n69 --> n71
    n77 --> n81
    n77 --> n82
    n84 --> n88
    n139 --> n140
    n71 --> n83
    n116 --> n119
    n78 --> n84
    n129 --> n133
    n55 --> n58
    n53 --> n58
    n132 --> n136
    n132 --> n137
    n125 --> n134
    n123 --> n126
    n122 --> n126
    n124 --> n126
    n55 --> n59
    n53 --> n59
    n92 --> n103
    n98 --> n103
    n67 --> n74
    n124 --> n127
    n121 --> n122
    n118 --> n122
    n121 --> n123
    n133 --> n141
    n135 --> n141
    n139 --> n141
    n123 --> n128
    n122 --> n128
    n124 --> n128
    n92 --> n97
    n69 --> n75
    n83 --> n89
    n85 --> n89
    n59 --> n65
    n124 --> n129
    n67 --> n77
    n88 --> n98
    n59 --> n67
    n55 --> n112
    n103 --> n109
    n120 --> n124
    n56 --> n68
    n55 --> n60
    n53 --> n60
    n119 --> n120
    n58 --> n69
    n111 --> n116
    n59 --> n70
    n62 --> n70
    n117 --> n121
    n118 --> n121
    n92 --> n100
    n139 --> n142
    n131 --> n142
    n80 --> n92
    n81 --> n92
    n82 --> n92
    n67 --> n78
    n122 --> n130
    n132 --> n138
    n75 --> n85
    n129 --> n135
    n138 --> n139
    n137 --> n139
    n136 --> n139
    n55 --> n62
    n53 --> n62
    n115 x--x n120
    n54 x--x n59
    n122 x--x n123
    n122 x--x n124
    n123 x--x n124
    n65 x--x n70
    n77 x--x n78
```

# orphans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n143["GEN_Fighter_Competition"]
        n144["GEN_Study_Ships"]
    end
    subgraph tier_1["Tier 1"]
        n145["SWI_airspace_surveillance"]
        n146["SWI_buy_foreign_surplus_ships"]
    end
    n143 --> n145
    n144 --> n146
```
