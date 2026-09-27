# TUR_continue_the_military_reorganization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("TUR_continue_the_military_reorganization"))
    end
    subgraph tier_1["Tier 1"]
        n2["TUR_doctrine_on_western_lines"]
        n3["TUR_rejuvenate_the_great_war_arsenal"]
    end
    subgraph tier_2["Tier 2"]
        n4["TUR_begin_economic_mobilization"]
        n5["TUR_defending_our_borders"]
        n6["TUR_expand_officer_schools"]
        n7["TUR_standardize_infantry_equipment"]
        n8{"TUR_streamline_conscription"}
    end
    subgraph tier_3["Tier 3"]
        n9["TUR_begin_domestic_aircraft_production"]
        n10["TUR_begin_mechanization_developments"]
        n11["TUR_expand_recruitment"]
        n12["TUR_expand_the_turkish_state_arsenal"]
        n13["TUR_infantry_advancements"]
        n14["TUR_logistical_advancements"]
        n15["TUR_maximize_orientation"]
        n16["TUR_strengthen_troop_coordination"]
    end
    subgraph tier_4["Tier 4"]
        n17["TUR_combat_engineers"]
        n18["TUR_infantry_is_our_backbone"]
        n19["TUR_tank_centered_force"]
        n20["TUR_troop_specialization"]
    end
    n4 --> n9
    n3 --> n4
    n7 --> n10
    n16 --> n17
    n14 --> n17
    n3 --> n5
    n1 --> n2
    n2 --> n6
    n3 --> n6
    n8 --> n11
    n4 --> n12
    n7 --> n13
    n13 --> n18
    n7 --> n14
    n8 --> n14
    n8 --> n15
    n1 --> n3
    n3 --> n7
    n2 --> n7
    n3 --> n8
    n2 --> n8
    n7 --> n16
    n8 --> n16
    n10 --> n19
    n15 --> n20
    n11 --> n20
    n11 x--x n15
```

# TUR_continue_the_moderate_course

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n21(("TUR_continue_the_moderate_course"))
        n22["TUR_demand_free_elections"]
        n23["TUR_further_the_reforms"]
        n24["TUR_revolution_not_reform"]
        n25["TUR_support_the_conservative_opposition"]
    end
    subgraph tier_1["Tier 1"]
        n26["TUR_further_agricultural_cooperative_reform"]
        n27{"TUR_instate_constitutional_secularism"}
        n28{"TUR_nationalist_policies"}
    end
    subgraph tier_2["Tier 2"]
        n29{"TUR_continue_ataturks_reforms"}
        n30{"TUR_cult_of_the_marshal"}
        n31["TUR_mechanize_the_farming_sector"]
    end
    subgraph tier_3["Tier 3"]
        n32{"TUR_expand_the_centralization_efforts"}
        n33["TUR_renew_the_democratic_reforms"]
        n34["TUR_turkish_grain_board"]
        n35["TUR_war_bonds"]
        n36["TUR_wartime_rationing"]
    end
    subgraph tier_4["Tier 4"]
        n37["TUR_accomplishing_ataturks_dream"]
        n38["TUR_befriend_the_fascist_council"]
        n39["TUR_expand_land_reform"]
        n40["TUR_expand_the_village_institute_program"]
        n41["TUR_relax_the_secular_policies"]
        n42["TUR_solidify_the_dictatorship"]
        n43["TUR_wealth_tax"]
    end
    subgraph tier_5["Tier 5"]
        n44["TUR_consolidate_the_chp"]
        n45["TUR_further_constitutional_reform"]
        n46["TUR_further_eastern_developments"]
        n47["TUR_golden_age_of_the_republic"]
        n48["TUR_military_youth"]
        n49["TUR_ministry_of_labor_and_social_security"]
        n50["TUR_new_state_enterprise"]
    end
    subgraph tier_6["Tier 6"]
        n51["TUR_pan_turkism"]
    end
    subgraph tier_7["Tier 7"]
        n52["TUR_free_the_bulgarian_turks"]
        n53["TUR_our_final_battle"]
        n54["TUR_reclaim_ataturks_home"]
        n55["TUR_strike_east"]
    end
    n33 --> n37
    n32 --> n38
    n38 --> n44
    n27 --> n29
    n28 --> n30
    n33 --> n39
    n32 --> n39
    n30 --> n32
    n32 --> n40
    n33 --> n40
    n51 --> n52
    n21 --> n26
    n37 --> n45
    n42 --> n46
    n42 --> n47
    n21 --> n27
    n26 --> n31
    n38 --> n48
    n37 --> n49
    n42 --> n49
    n21 --> n28
    n37 --> n50
    n51 --> n53
    n44 --> n51
    n51 --> n54
    n32 --> n41
    n29 --> n33
    n32 --> n42
    n51 --> n55
    n29 --> n34
    n30 --> n34
    n22 --> n34
    n23 --> n34
    n29 --> n35
    n30 --> n35
    n22 --> n35
    n23 --> n35
    n29 --> n36
    n30 --> n36
    n22 --> n36
    n23 --> n36
    n36 --> n43
    n38 x--x n42
    n29 x--x n30
    n21 x--x n24
    n21 x--x n25
    n32 x--x n33
```

# TUR_continue_the_naval_expansion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n56(("TUR_continue_the_naval_expansion"))
        n57["TUR_found_an_air_war_academy"]
    end
    subgraph tier_1["Tier 1"]
        n58["TUR_doctrinal_advancement"]
        n59["TUR_expand_black_sea_presence"]
        n60["TUR_expand_mediteranean_bases"]
        n61["TUR_expand_the_golcuk_shipyard"]
        n62["TUR_new_shipyards"]
    end
    subgraph tier_2["Tier 2"]
        n63["TUR_amphibious_warfare"]
        n64["TUR_balanced_navy"]
        n65["TUR_modern_radar"]
        n66["TUR_r56_the_path_of_the_wolf"]
    end
    subgraph tier_3["Tier 3"]
        n67["TUR_control_our_seas"]
        n68["TUR_modern_sub_surface_peripherals"]
    end
    n58 --> n63
    n58 --> n64
    n64 --> n67
    n56 --> n58
    n56 --> n59
    n57 --> n59
    n56 --> n60
    n57 --> n60
    n56 --> n61
    n60 --> n65
    n59 --> n65
    n66 --> n68
    n56 --> n62
    n58 --> n66
```

# TUR_continue_the_push_for_autarky

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n69(("TUR_continue_the_push_for_autarky"))
    end
    subgraph tier_1["Tier 1"]
        n70["TUR_connecting_the_eastern_provinces"]
        n71["TUR_develop_the_new_capital"]
        n72["TUR_expand_the_aegean_economic_heartland"]
        n73["TUR_implement_western_electronics"]
    end
    subgraph tier_2["Tier 2"]
        n74["TUR_drill_southeast_anatolia"]
        n75["TUR_expand_the_bursa_textile_industry"]
        n76["TUR_expand_the_izmir_cement_industry"]
        n77["TUR_tenmak"]
        n78["TUR_the_industrialization_of_central_anatolia"]
        n79["TUR_village_institutes_program"]
    end
    subgraph tier_3["Tier 3"]
        n80["TUR_black_sea_grain_exports"]
        n81["TUR_eradicate_rural_illiteracy"]
        n82["TUR_expand_the_eastern_railway_networks"]
        n83["TUR_exploit_the_sivas_iron_mines"]
        n84["TUR_middle_east_institute_of_technology"]
    end
    subgraph tier_4["Tier 4"]
        n85["TUR_central_anatolian_heavy_industry"]
        n86["TUR_expand_the_ergani_copper_industry"]
        n87["TUR_support_malatya_raw_exports"]
    end
    n78 --> n80
    n83 --> n85
    n82 --> n85
    n69 --> n70
    n69 --> n71
    n70 --> n74
    n79 --> n81
    n69 --> n72
    n72 --> n75
    n78 --> n82
    n83 --> n86
    n82 --> n86
    n72 --> n76
    n78 --> n83
    n69 --> n73
    n76 --> n84
    n75 --> n84
    n83 --> n87
    n82 --> n87
    n73 --> n77
    n70 --> n78
    n70 --> n79
```

# TUR_found_an_air_war_academy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n56["TUR_continue_the_naval_expansion"]
        n57(("TUR_found_an_air_war_academy"))
    end
    subgraph tier_1["Tier 1"]
        n88["TUR_continue_importing_western_designs"]
        n59["TUR_expand_black_sea_presence"]
        n60["TUR_expand_mediteranean_bases"]
        n89["TUR_medium_bomber_focus"]
        n90["TUR_paratrooper_developments"]
    end
    subgraph tier_2["Tier 2"]
        n91["TUR_airland_battle"]
        n92["TUR_defending_our_skies"]
        n65["TUR_modern_radar"]
        n93["TUR_naval_bombers"]
        n94["TUR_new_cannon_developments"]
    end
    n89 --> n91
    n57 --> n88
    n88 --> n92
    n56 --> n59
    n57 --> n59
    n56 --> n60
    n57 --> n60
    n57 --> n89
    n60 --> n65
    n59 --> n65
    n89 --> n93
    n88 --> n94
    n57 --> n90
```

# TUR_revolution_not_reform

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29["TUR_continue_ataturks_reforms"]
        n21["TUR_continue_the_moderate_course"]
        n30["TUR_cult_of_the_marshal"]
        n22["TUR_demand_free_elections"]
        n24{"TUR_revolution_not_reform"}
        n25["TUR_support_the_conservative_opposition"]
    end
    subgraph tier_1["Tier 1"]
        n95["TUR_kemalisms_next_step_forward"]
        n96["TUR_lead_the_underground_komunist_partisi"]
        n97["TUR_reorganize_the_kadro_movement"]
        n98["TUR_two_red_banners"]
    end
    subgraph tier_2["Tier 2"]
        n99["TUR_ally_kurdish_nationalist_groups"]
        n100["TUR_call_for_general_strike"]
        n101["TUR_expand_the_village_institutes_program_socialist"]
        n23["TUR_further_the_reforms"]
        n102["TUR_reconciliation_with_liberal_kemalists"]
        n103["TUR_request_soviet_support"]
    end
    subgraph tier_3["Tier 3"]
        n104["TUR_cement_control_over_the_party"]
        n105["TUR_storm_the_grand_national_assembly"]
        n34["TUR_turkish_grain_board"]
        n35["TUR_war_bonds"]
        n36["TUR_wartime_rationing"]
    end
    subgraph tier_4["Tier 4"]
        n106["TUR_backbone_of_the_party"]
        n107["TUR_forging_a_brighter_tomorrow"]
        n108["TUR_pave_the_road_to_progress"]
        n109["TUR_the_question_of_nationalization"]
        n110["TUR_voice_of_the_people"]
        n43["TUR_wealth_tax"]
    end
    subgraph tier_5["Tier 5"]
        n111["TUR_centralize_the_TKP"]
        n112["TUR_continue_the_democratic_transition"]
        n113["TUR_request_soviet_economic_aid"]
        n114["TUR_reward_the_working_class"]
        n115["TUR_turkish_red_army"]
    end
    n96 --> n99
    n104 --> n106
    n96 --> n100
    n23 --> n104
    n102 --> n104
    n107 --> n111
    n108 --> n112
    n95 --> n101
    n96 --> n101
    n105 --> n107
    n95 --> n23
    n24 --> n95
    n24 --> n96
    n104 --> n108
    n95 --> n102
    n24 --> n97
    n107 --> n113
    n96 --> n103
    n108 --> n114
    n100 --> n105
    n105 --> n109
    n104 --> n109
    n29 --> n34
    n30 --> n34
    n22 --> n34
    n23 --> n34
    n107 --> n115
    n24 --> n98
    n105 --> n110
    n29 --> n35
    n30 --> n35
    n22 --> n35
    n23 --> n35
    n29 --> n36
    n30 --> n36
    n22 --> n36
    n23 --> n36
    n36 --> n43
    n21 x--x n24
    n95 x--x n96
    n24 x--x n25
```

# TUR_support_the_conservative_opposition

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29["TUR_continue_ataturks_reforms"]
        n21["TUR_continue_the_moderate_course"]
        n30["TUR_cult_of_the_marshal"]
        n23["TUR_further_the_reforms"]
        n24["TUR_revolution_not_reform"]
        n25{"TUR_support_the_conservative_opposition"}
    end
    subgraph tier_1["Tier 1"]
        n116["TUR_no_more_humiliations"]
        n117["TUR_the_fight_for_popular_mandate"]
    end
    subgraph tier_2["Tier 2"]
        n118["TUR_call_for_protests_in_the_capital"]
        n119["TUR_lead_the_rural_masses"]
        n120["TUR_motion_with_four_signatures"]
    end
    subgraph tier_3["Tier 3"]
        n22["TUR_demand_free_elections"]
        n121["TUR_overthrow_inonus_government"]
    end
    subgraph tier_4["Tier 4"]
        n122["TUR_amend_the_secular_policies"]
        n123["TUR_liberalize_the_national_economy"]
        n124{"TUR_stabilize_the_nation"}
        n34["TUR_turkish_grain_board"]
        n35["TUR_war_bonds"]
        n36["TUR_wartime_rationing"]
    end
    subgraph tier_5["Tier 5"]
        n125{"TUR_dismantle_the_republican_institutions"}
        n126["TUR_end_the_ban_on_the_arabic_adhan"]
        n127["TUR_expand_foreign_trade"]
        n128["TUR_improve_our_regional_influence_r56"]
        n129{"TUR_lift_the_caliphates_exile"}
        n130["TUR_peace_between_turks_and_kurds"]
        n131{"TUR_restore_the_imperial_borders"}
        n132["TUR_specialization_led_development"]
        n43["TUR_wealth_tax"]
        n133{"TUR_western_detente"}
    end
    subgraph tier_6["Tier 6"]
        n134["TUR_amicable_ties_across_the_middle_east"]
        n135["TUR_batum_and_the_muslim_caucasian_states"]
        n136["TUR_befriend_the_bulgarians"]
        n137["TUR_claim_greater_syria"]
        n138["TUR_continue_military_rule"]
        n139["TUR_end_the_southern_threat_r56"]
        n140["TUR_liberalize_the_economy"]
        n141["TUR_one_persian_ottoman_war_to_end_them_all"]
        n142["TUR_pragmatic_expansionism"]
        n143["TUR_reclaim_the_aegean_territories"]
        n144["TUR_restore_the_imperial_divan"]
    end
    subgraph tier_7["Tier 7"]
        n145["TUR_arbiter_of_the_muslim_world"]
        n146["TUR_bureaucratic_modernization"]
        n147["TUR_claim_greater_bulgaria"]
        n148{"TUR_cross_the_suez"}
        n149["TUR_dominate_the_arabian_peninsula"]
        n150["TUR_military_first_policies"]
        n151["TUR_solidify_the_pan_islam_unity"]
        n152["TUR_subjugate_the_greeks"]
    end
    subgraph tier_8["Tier 8"]
        n153["TUR_avenge_the_1878_berlin_treaty"]
        n154["TUR_reincorporate_the_egyptian_lands"]
        n155["TUR_restore_dominion_over_albania"]
        n156["TUR_solidify_the_khedivate"]
    end
    n22 --> n122
    n131 --> n134
    n133 --> n134
    n141 --> n145
    n134 --> n145
    n147 --> n153
    n131 --> n135
    n131 --> n136
    n133 --> n136
    n144 --> n146
    n117 --> n118
    n116 --> n118
    n143 --> n147
    n131 --> n137
    n125 --> n138
    n129 --> n138
    n137 --> n148
    n120 --> n22
    n118 --> n22
    n124 --> n125
    n137 --> n149
    n122 --> n126
    n133 --> n139
    n123 --> n127
    n123 --> n128
    n122 --> n128
    n116 --> n119
    n133 --> n140
    n22 --> n123
    n124 --> n129
    n138 --> n150
    n117 --> n120
    n25 --> n116
    n131 --> n141
    n133 --> n141
    n119 --> n121
    n118 --> n121
    n122 --> n130
    n133 --> n142
    n131 --> n143
    n148 --> n154
    n147 --> n155
    n124 --> n131
    n125 --> n144
    n129 --> n144
    n148 --> n156
    n144 --> n151
    n138 --> n151
    n123 --> n132
    n121 --> n124
    n143 --> n152
    n136 --> n152
    n25 --> n117
    n29 --> n34
    n30 --> n34
    n22 --> n34
    n23 --> n34
    n29 --> n35
    n30 --> n35
    n22 --> n35
    n23 --> n35
    n29 --> n36
    n30 --> n36
    n22 --> n36
    n23 --> n36
    n36 --> n43
    n124 --> n133
    n134 x--x n141
    n136 x--x n143
    n138 x--x n144
    n21 x--x n25
    n116 x--x n117
    n154 x--x n156
    n131 x--x n133
    n24 x--x n25
```

# TUR_the_montreux_convention_r56

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n157{"TUR_the_montreux_convention_r56"}
    end
    subgraph tier_1["Tier 1"]
        n158{"TUR_bicontinental_intervention"}
        n159["TUR_neutrality_through_deterrence"]
    end
    subgraph tier_2["Tier 2"]
        n160["TUR_american_lend_lease"]
        n161["TUR_anglo_turkish_friendship_agreement"]
        n162["TUR_anti_colonial_action"]
        n163{"TUR_cooperation_against_berlin"}
        n164{"TUR_cooperation_against_moscow"}
        n165["TUR_german_turkish_treaty_of_friendship"]
        n166["TUR_renew_the_soviet_non_aggression_pact"]
    end
    subgraph tier_3["Tier 3"]
        n167["TUR_amend_the_montreux_convention"]
        n168["TUR_clodius_agreement"]
        n169["TUR_demand_french_withdrawal_from_syria"]
        n170["TUR_destroy_iraqs_corrupt_monarchy"]
        n171["TUR_join_the_international_community"]
        n172["TUR_limited_mutual_assistance"]
        n173["TUR_regional_leadership"]
        n174["TUR_soviet_turkish_trade_agreement"]
        n175["TUR_take_the_shahs_head"]
    end
    subgraph tier_4["Tier 4"]
        n176["TUR_ally_the_balkan_states"]
        n177["TUR_liberate_the_peninsula"]
        n178["TUR_militarize_the_saadabat_pact"]
        n179["TUR_the_final_battle_against_global_imperialism"]
    end
    n173 --> n176
    n166 --> n167
    n159 --> n160
    n158 --> n160
    n159 --> n161
    n158 --> n162
    n157 --> n158
    n165 --> n168
    n158 --> n163
    n158 --> n164
    n162 --> n169
    n162 --> n170
    n159 --> n165
    n164 --> n171
    n163 --> n171
    n170 --> n177
    n161 --> n172
    n173 --> n178
    n157 --> n159
    n164 --> n173
    n163 --> n173
    n159 --> n166
    n166 --> n174
    n162 --> n175
    n169 --> n179
    n162 x--x n163
    n162 x--x n164
    n158 x--x n159
    n163 x--x n164
    n171 x--x n173
```
