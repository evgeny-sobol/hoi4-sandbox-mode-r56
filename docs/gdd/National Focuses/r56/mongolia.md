# MON_establish_provisional_airforce

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"MON_establish_provisional_airforce"}
        n2["MON_large_ships_effort"]
    end
    subgraph tier_1["Tier 1"]
        n3["MON_capital_operations_focus"]
        n4["MON_situational_aerial_presence"]
    end
    subgraph tier_2["Tier 2"]
        n5["MON_air_recon_and_intelligence_protection"]
        n6["MON_focus_on_local_engagements"]
        n7["MON_foreign_air_equipment_coordination"]
        n8["MON_institute_air_landing_batallions"]
        n9["MON_wastness_devours"]
    end
    subgraph tier_3["Tier 3"]
        n10["MON_improve_air_doctrine"]
        n11["MON_strengthen_air_navy_cooperation"]
    end
    n3 --> n5
    n4 --> n5
    n1 --> n3
    n4 --> n6
    n4 --> n7
    n3 --> n7
    n7 --> n10
    n4 --> n8
    n3 --> n8
    n1 --> n4
    n6 --> n11
    n2 --> n11
    n3 --> n9
    n3 x--x n4
```

# MON_establish_the_trade_fleet

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12{"MON_establish_the_trade_fleet"}
        n13{"MON_fund_mongolian_naval_forces"}
    end
    subgraph tier_1["Tier 1"]
        n14["MON_ensure_branches_independence"]
        n15["MON_lease_foreign_dockyards"]
    end
    subgraph tier_2["Tier 2"]
        n16["MON_joint_naval_academy"]
        n17["MON_local_specialists"]
    end
    subgraph tier_3["Tier 3"]
        n18["MON_naval_integration"]
    end
    n12 --> n14
    n13 --> n14
    n15 --> n16
    n12 --> n15
    n14 --> n17
    n16 --> n18
    n17 --> n18
    n14 x--x n15
```

# MON_expand_the_general_staff

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19{"MON_expand_the_general_staff"}
        n20{"MON_organize_army_inspection"}
    end
    subgraph tier_1["Tier 1"]
        n21{"MON_favour_young_officers"}
        n22{"MON_foundation_for_special_task_battalion"}
        n23["MON_legacy_of_tachanka"]
        n24["MON_old_heritage"]
        n25["MON_ratify_battleplans"]
        n26["MON_soldier_devotion"]
        n27{"MON_support_old_officers_corps"}
    end
    subgraph tier_2["Tier 2"]
        n28["MON_adopt_tsogs_methods"]
        n29["MON_experimental_mobility"]
        n30["MON_gobi_training_facilities"]
        n31["MON_mountainous_specialization"]
        n32["MON_rely_on_soviet_tactics"]
        n33["MON_revive_forgotten_doctrines"]
        n34["MON_the_grand_stratagem"]
    end
    subgraph tier_3["Tier 3"]
        n35["MON_acquire_foreign_tank_designs"]
        n36["MON_bolster_national_awareness"]
        n37["MON_equipment_recovery_teams"]
        n38["MON_favour_stronghold_defenses"]
        n39["MON_focus_on_infantry"]
        n40["MON_improve_militia_formations"]
        n41["MON_investigate_improvement_opportunities"]
        n42["MON_strengthen_air_land_links"]
        n43["MON_study_motorized_equipment"]
        n44["MON_support_tactical_decision_freedom"]
        n45["MON_weapon_prototype_development"]
    end
    subgraph tier_4["Tier 4"]
        n46["MON_advanced_fortification_studies"]
        n47["MON_combined_arms_operations"]
        n48["MON_expand_universal_military_act"]
        n49["MON_feature_compact_mortar_designs"]
        n50["MON_ideological_loyalty_of_the_masses"]
        n51["MON_mass_firearm_production"]
        n52["MON_optimize_infantry_formations"]
        n53["MON_specialization_on_vehicle_production"]
        n54["MON_the_inevitable_counterblow"]
        n55["MON_utilize_new_designs_strength"]
    end
    subgraph tier_5["Tier 5"]
        n56["MON_good_old_new_ways"]
        n57["MON_suitable_high_command"]
        n58["MON_the_ultimate_weapon"]
        n59["MON_train_specialized_crews"]
        n60["MON_unified_operational_command"]
    end
    n29 --> n35
    n21 --> n28
    n27 --> n28
    n38 --> n46
    n33 --> n36
    n42 --> n47
    n31 --> n37
    n30 --> n37
    n36 --> n48
    n21 --> n29
    n34 --> n38
    n19 --> n21
    n41 --> n49
    n32 --> n39
    n20 --> n22
    n19 --> n22
    n22 --> n30
    n50 --> n56
    n48 --> n56
    n40 --> n50
    n33 --> n40
    n28 --> n41
    n19 --> n23
    n45 --> n51
    n22 --> n31
    n19 --> n24
    n44 --> n52
    n19 --> n25
    n20 --> n25
    n21 --> n32
    n27 --> n32
    n27 --> n33
    n19 --> n26
    n43 --> n53
    n28 --> n42
    n29 --> n43
    n51 --> n57
    n54 --> n57
    n19 --> n27
    n20 --> n27
    n34 --> n44
    n21 --> n34
    n27 --> n34
    n39 --> n54
    n49 --> n58
    n47 --> n58
    n55 --> n59
    n53 --> n59
    n52 --> n60
    n46 --> n60
    n35 --> n55
    n32 --> n45
    n28 x--x n29
    n28 x--x n32
    n28 x--x n33
    n28 x--x n34
    n29 x--x n32
    n29 x--x n33
    n29 x--x n34
    n21 x--x n27
    n30 x--x n31
    n23 x--x n24
    n23 x--x n26
    n24 x--x n26
    n32 x--x n33
    n32 x--x n34
    n33 x--x n34
```

# MON_form_the_provisional_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61["MON_adopt_sun_yat_sen_principles"]
        n62{"MON_approach_japan"}
        n63["MON_denounce_politizised_army"]
        n64(("MON_form_the_provisional_government"))
        n65["MON_hold_plenum_of_central_committee"]
        n66["MON_host_emergency_great_khural_assembly"]
        n67["MON_rely_on_national_strength"]
        n68{"MON_sabotage_great_khural"}
        n69["MON_stabilize_the_country"]
    end
    subgraph tier_1["Tier 1"]
        n70{"MON_appeal_to_china"}
        n71["MON_assists_deviants_struggle"]
        n72["MON_faciliate_cooperation_with_china"]
        n73["MON_matters_of_internal_affairs"]
    end
    subgraph tier_2["Tier 2"]
        n74{"MON_ensure_rural_support"}
        n75["MON_expand_the_role_of_urga_national_library"]
        n76{"MON_guard_southern_border"}
        n77["MON_infiltrate_the_railway_system"]
        n78{"MON_rally_the_radicals"}
        n79{"MON_return_of_prodigal_son"}
        n80{"MON_strengthen_buddhist_community"}
    end
    subgraph tier_3["Tier 3"]
        n81["MON_invite_pince_su"]
        n82["MON_search_new_bogd_khan"]
        n83["MON_shelter_the_banished"]
        n84["MON_strong_leader_genden"]
    end
    subgraph tier_4["Tier 4"]
        n85["MON_continue_new_course_policy"]
        n86{"MON_dealing_with_soviet_sympathisers"}
        n87["MON_incorporate_buddhism"]
        n88["MON_launch_a_coup"]
        n89["MON_proclaim_the_second_bogd_khanate"]
        n90["MON_the_new_chairman"]
    end
    subgraph tier_5["Tier 5"]
        n91["MON_empower_hudonets"]
        n92["MON_get_rich"]
        n93["MON_independent_army_structure"]
    end
    subgraph tier_6["Tier 6"]
        n94["MON_ensure_soldier_loyalty"]
        n95{"MON_provide_for_the_people"}
        n96["MON_reform_the_high_command"]
    end
    subgraph tier_7["Tier 7"]
        n97{"MON_abolish_the_secretary_system"}
        n98{"MON_mongolian_peoples_army"}
        n99["MON_oust_genden"]
        n100["MON_subsidise_the_military"]
    end
    subgraph tier_8["Tier 8"]
        n101["MON_changes_within"]
        n102["MON_leader_of_the_equal"]
        n103["MON_spread_of_anarcho_communism"]
    end
    subgraph tier_9["Tier 9"]
        n104["MON_abolish_the_currency"]
        n105["MON_full_social_equality"]
        n106["MON_promote_religious_socialism"]
    end
    subgraph tier_10["Tier 10"]
        n107["MON_cooperation_with_kuomintang"]
        n108["MON_eradicate_private_property"]
        n109["MON_remove_hierarchical_structures"]
        n110["MON_support_buddhist_monasteries"]
        n111["MON_workers_control_and_discipline"]
    end
    subgraph tier_11["Tier 11"]
        n112["MON_finalize_state_reforms"]
        n113{"MON_nationalism"}
        n114{"MON_put_an_end_to_the_arat_system"}
    end
    subgraph tier_12["Tier 12"]
        n115{"MON_codify_democratic_principles"}
        n116["MON_revoke_the_kyakhta_treaty"]
    end
    subgraph tier_13["Tier 13"]
        n117["MON_five_races_under_one_union"]
    end
    subgraph tier_14["Tier 14"]
        n118["MON_confrontations_with_warlords"]
        n119["MON_the_battle_for_tuva_uriankai"]
    end
    n101 --> n104
    n95 --> n97
    n64 --> n70
    n64 --> n71
    n99 --> n101
    n61 --> n115
    n113 --> n115
    n116 --> n118
    n117 --> n118
    n84 --> n85
    n61 --> n107
    n106 --> n107
    n84 --> n86
    n85 --> n91
    n73 --> n74
    n93 --> n94
    n105 --> n108
    n104 --> n108
    n72 --> n75
    n67 --> n72
    n64 --> n72
    n111 --> n112
    n109 --> n112
    n113 --> n117
    n115 --> n117
    n114 --> n117
    n101 --> n105
    n85 --> n92
    n73 --> n76
    n84 --> n87
    n63 --> n93
    n86 --> n93
    n71 --> n77
    n62 --> n81
    n78 --> n81
    n81 --> n88
    n86 --> n102
    n98 --> n102
    n97 --> n102
    n64 --> n73
    n66 --> n73
    n96 --> n98
    n94 --> n98
    n107 --> n113
    n95 --> n99
    n82 --> n89
    n102 --> n106
    n91 --> n95
    n92 --> n95
    n107 --> n114
    n73 --> n78
    n62 --> n78
    n93 --> n96
    n105 --> n109
    n71 --> n79
    n114 --> n116
    n70 --> n82
    n80 --> n82
    n76 --> n83
    n74 --> n83
    n99 --> n103
    n70 --> n80
    n73 --> n80
    n68 --> n84
    n79 --> n84
    n95 --> n100
    n106 --> n110
    n116 --> n119
    n117 --> n119
    n83 --> n90
    n104 --> n111
    n117 x--x n116
    n64 x--x n65
    n64 x--x n66
    n64 x--x n67
    n81 x--x n82
    n81 x--x n83
    n102 x--x n99
    n82 x--x n83
    n69 x--x n84
```

# MON_fund_mongolian_naval_forces

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12{"MON_establish_the_trade_fleet"}
        n6["MON_focus_on_local_engagements"]
        n13{"MON_fund_mongolian_naval_forces"}
        n16["MON_joint_naval_academy"]
        n15["MON_lease_foreign_dockyards"]
    end
    subgraph tier_1["Tier 1"]
        n120["MON_amphibious_effort"]
        n14["MON_ensure_branches_independence"]
        n121["MON_improve_naval_doctrines"]
        n2["MON_large_ships_effort"]
        n122["MON_maritime_infantry"]
        n123{"MON_prioritize_small_vessels"}
    end
    subgraph tier_2["Tier 2"]
        n17["MON_local_specialists"]
        n124["MON_sea_raiders"]
        n11["MON_strengthen_air_navy_cooperation"]
        n125["MON_support_the_mechants"]
    end
    subgraph tier_3["Tier 3"]
        n126["MON_emphasise_naval_blockades"]
        n127["MON_modernize_escort_tactics"]
        n18["MON_naval_integration"]
    end
    n13 --> n120
    n124 --> n126
    n12 --> n14
    n13 --> n14
    n13 --> n121
    n13 --> n2
    n14 --> n17
    n13 --> n122
    n125 --> n127
    n16 --> n18
    n17 --> n18
    n13 --> n123
    n123 --> n124
    n6 --> n11
    n2 --> n11
    n123 --> n125
    n14 x--x n15
    n124 x--x n125
```

# MON_hold_plenum_of_central_committee

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n64["MON_form_the_provisional_government"]
        n65(("MON_hold_plenum_of_central_committee"))
        n66["MON_host_emergency_great_khural_assembly"]
        n128["MON_limited_research_cooperation"]
        n129["MON_open_up_the_country"]
        n130["MON_prepare_for_the_inevitable"]
        n131["MON_reach_out_to_moscow"]
        n67["MON_rely_on_national_strength"]
    end
    subgraph tier_1["Tier 1"]
        n132["MON_deal_with_genden"]
        n133["MON_joint_technological_development"]
        n134["MON_ratify_mutual_assistance_treaty"]
    end
    subgraph tier_2["Tier 2"]
        n135["MON_approach_soviet_planners"]
        n136["MON_intensify_cooperation"]
        n137{"MON_invite_frinovsky"}
        n138["MON_invite_soviet_advisors"]
        n139{"MON_secure_the_transition_of_power"}
        n140["MON_student_exchange_program"]
    end
    subgraph tier_3["Tier 3"]
        n141["MON_appoint_soviet_protege"]
        n142["MON_prepare_leftist_takeover"]
        n143["MON_reform_national_script"]
        n144["MON_reject_choibalsan_advances"]
        n145["MON_solidify_language_institutes"]
    end
    subgraph tier_4["Tier 4"]
        n146["MON_deal_with_religious_centre"]
        n147["MON_ensure_control_over_the_railways"]
        n148["MON_establish_socialist_society"]
        n149["MON_invite_political_exiles"]
        n150["MON_learn_from_lkhumbe_affair"]
        n151["MON_reorganize_homeland_security"]
        n152["MON_separate_army_and_politics"]
        n153["MON_tolerate_religious_groups"]
        n154["MON_ulaanbaatar_national_university"]
    end
    subgraph tier_5["Tier 5"]
        n155["MON_arm_civil_militia"]
        n156["MON_confiscate_soviet_weaponry"]
        n157["MON_contact_the_bandits"]
        n158["MON_decrease_defense_budget"]
        n159{"MON_ensure_mvd_loyalty"}
        n160["MON_increase_border_patrols"]
        n161["MON_local_command_structure"]
        n162["MON_partial_religious_compromise"]
        n163["MON_peasants_focus"]
        n164["MON_the_great_terror"]
        n165["MON_workers_focus"]
    end
    subgraph tier_6["Tier 6"]
        n166["MON_affirm_rearmament_program"]
        n167["MON_contest_the_insurgents"]
        n168["MON_finalize_army_reform"]
        n169["MON_new_generation_of_intelligentsia"]
        n170["MON_new_party_elite"]
        n171{"MON_seize_the_power"}
        n172["MON_support_the_rebels"]
        n173["MON_workers_and_peasants_unite_focus"]
    end
    subgraph tier_7["Tier 7"]
        n174["MON_a_socialist_republic"]
        n175["MON_assist_the_revolutionary_struggle"]
        n176["MON_begin_the_collectivization"]
        n177["MON_end_political_opportunism"]
        n178["MON_formalize_the_treaty"]
        n179["MON_reassure_the_soviets"]
        n180["MON_rebuke_1932_mediation_issue"]
        n181["MON_remove_nominal_leadership"]
        n182["MON_reorganize_state_agenda"]
        n183["MON_tackle_the_eastern_threat"]
    end
    subgraph tier_8["Tier 8"]
        n184{"MON_example_of_communist_paradise"}
        n185["MON_frontline_infrastructure"]
        n186["MON_liberalize_trade_policies"]
        n187["MON_make_use_of_monastery_assets"]
        n188["MON_seize_our_advantages"]
        n189["MON_sideline_the_left"]
        n190{"MON_stay_on_guard"}
        n191["MON_thinking_out_of_bounds"]
        n192{"MON_true_hero_for_the_people"}
    end
    subgraph tier_9["Tier 9"]
        n193["MON_central_asia_defensive_pact"]
        n194["MON_changing_times"]
        n195["MON_destabilize_the_central_plain"]
        n196{"MON_dream_of_greater_mongolia"}
        n197["MON_first_five_year_plan_focus"]
        n198["MON_means_of_propaganda"]
        n199["MON_support_the_red_army_focus"]
    end
    subgraph tier_10["Tier 10"]
        n200["MON_a_pragmatic_diplomacy"]
        n201["MON_aerial_support_initiative"]
        n202["MON_delegation_to_tuva"]
        n203["MON_expand_the_treaty"]
        n204["MON_fruits_of_revolution"]
        n205["MON_gather_ulaanbaatar_conference"]
        n206["MON_improve_transportation_network"]
        n207["MON_intervene_in_sinkiang"]
        n208["MON_join_the_big_brother"]
        n209["MON_mengjian_issue"]
        n210["MON_oppose_soviet_colonialism"]
        n211["MON_vessels_of_the_future_war"]
    end
    subgraph tier_11["Tier 11"]
        n212["MON_disagreements_with_sinkiang"]
        n213["MON_divide_spheres_of_influence"]
        n214["MON_expand_influence_into_greater_steppe"]
        n215["MON_gobi_border_realignment"]
        n216["MON_industrial_relocation"]
        n217["MON_new_comintern_beacon"]
        n218["MON_one_mongolia_policy"]
        n219["MON_support_east_siberian_independists"]
        n220["MON_weaken_soviet_control_over_northwestern_siberia"]
    end
    subgraph tier_12["Tier 12"]
        n221["MON_a_unity_with_buryats"]
        n222["MON_increase_presence_in_caucasus"]
        n223["MON_infiltrate_transural_region"]
        n224["MON_joint_pilgrimage_to_mount_wutai"]
        n225["MON_one_union_government"]
        n226["MON_plea_to_the_russian_far_east"]
        n227["MON_secure_hexi_corridor"]
        n228["MON_secure_the_rear"]
    end
    subgraph tier_13["Tier 13"]
        n229["MON_incorporate_new_lands"]
        n230["MON_launch_peoples_uprising"]
        n231["MON_reignite_the_civil_war"]
        n232["MON_struggle_for_communal_liberation"]
        n233["MON_the_second_northern_expedition"]
    end
    n196 --> n200
    n168 --> n174
    n173 --> n174
    n212 --> n221
    n202 --> n221
    n199 --> n201
    n160 --> n166
    n137 --> n141
    n139 --> n141
    n134 --> n135
    n150 --> n155
    n166 --> n175
    n171 --> n176
    n190 --> n193
    n192 --> n193
    n184 --> n194
    n192 --> n194
    n190 --> n194
    n147 --> n156
    n147 --> n157
    n159 --> n167
    n65 --> n132
    n141 --> n146
    n152 --> n158
    n196 --> n202
    n193 --> n202
    n191 --> n195
    n200 --> n212
    n205 --> n213
    n192 --> n196
    n184 --> n196
    n190 --> n196
    n171 --> n177
    n142 --> n147
    n131 --> n159
    n148 --> n159
    n144 --> n148
    n177 --> n184
    n179 --> n184
    n210 --> n214
    n193 --> n203
    n161 --> n168
    n158 --> n168
    n184 --> n197
    n192 --> n197
    n190 --> n197
    n172 --> n178
    n174 --> n185
    n130 --> n185
    n195 --> n204
    n198 --> n204
    n196 --> n205
    n200 --> n215
    n205 --> n215
    n199 --> n206
    n205 --> n229
    n221 --> n229
    n151 --> n160
    n152 --> n160
    n214 --> n222
    n206 --> n216
    n220 --> n223
    n133 --> n136
    n193 --> n207
    n132 --> n137
    n142 --> n149
    n134 --> n138
    n194 --> n208
    n213 --> n224
    n65 --> n133
    n223 --> n230
    n226 --> n230
    n222 --> n230
    n142 --> n150
    n174 --> n186
    n152 --> n161
    n182 --> n187
    n191 --> n198
    n193 --> n209
    n206 --> n217
    n204 --> n217
    n164 --> n169
    n164 --> n170
    n200 --> n218
    n217 --> n225
    n193 --> n210
    n129 --> n210
    n150 --> n162
    n148 --> n163
    n219 --> n226
    n137 --> n142
    n65 --> n134
    n171 --> n179
    n166 --> n180
    n133 --> n143
    n140 --> n143
    n228 --> n231
    n227 --> n231
    n139 --> n144
    n170 --> n181
    n169 --> n181
    n141 --> n151
    n171 --> n182
    n170 --> n182
    n213 --> n227
    n213 --> n228
    n132 --> n139
    n134 --> n139
    n176 --> n188
    n149 --> n171
    n157 --> n171
    n155 --> n171
    n162 --> n171
    n156 --> n171
    n144 --> n152
    n174 --> n189
    n128 --> n145
    n140 --> n145
    n174 --> n190
    n130 --> n190
    n225 --> n232
    n133 --> n140
    n128 --> n140
    n210 --> n219
    n159 --> n172
    n184 --> n199
    n192 --> n199
    n166 --> n183
    n151 --> n164
    n146 --> n164
    n224 --> n233
    n228 --> n233
    n179 --> n191
    n144 --> n153
    n181 --> n192
    n183 --> n192
    n145 --> n154
    n143 --> n154
    n199 --> n211
    n210 --> n220
    n163 --> n173
    n165 --> n173
    n148 --> n165
    n200 x--x n205
    n141 x--x n142
    n141 x--x n144
    n193 x--x n196
    n193 x--x n129
    n167 x--x n172
    n196 x--x n129
    n177 x--x n179
    n64 x--x n65
    n65 x--x n66
    n65 x--x n67
    n142 x--x n144
```

# MON_host_emergency_great_khural_assembly

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n70{"MON_appeal_to_china"}
        n64["MON_form_the_provisional_government"]
        n65["MON_hold_plenum_of_central_committee"]
        n66(("MON_host_emergency_great_khural_assembly"))
        n67["MON_rely_on_national_strength"]
    end
    subgraph tier_1["Tier 1"]
        n62{"MON_approach_japan"}
        n73["MON_matters_of_internal_affairs"]
    end
    subgraph tier_2["Tier 2"]
        n74{"MON_ensure_rural_support"}
        n76{"MON_guard_southern_border"}
        n78{"MON_rally_the_radicals"}
        n80{"MON_strengthen_buddhist_community"}
    end
    subgraph tier_3["Tier 3"]
        n81["MON_invite_pince_su"]
        n82["MON_search_new_bogd_khan"]
        n83["MON_shelter_the_banished"]
    end
    subgraph tier_4["Tier 4"]
        n88["MON_launch_a_coup"]
        n89["MON_proclaim_the_second_bogd_khanate"]
        n90["MON_the_new_chairman"]
    end
    n66 --> n62
    n73 --> n74
    n73 --> n76
    n62 --> n81
    n78 --> n81
    n81 --> n88
    n64 --> n73
    n66 --> n73
    n82 --> n89
    n73 --> n78
    n62 --> n78
    n70 --> n82
    n80 --> n82
    n76 --> n83
    n74 --> n83
    n70 --> n80
    n73 --> n80
    n83 --> n90
    n64 x--x n66
    n65 x--x n66
    n66 x--x n67
    n81 x--x n82
    n81 x--x n83
    n82 x--x n83
```

# MON_organize_army_inspection

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19{"MON_expand_the_general_staff"}
        n29["MON_experimental_mobility"]
        n21{"MON_favour_young_officers"}
        n20{"MON_organize_army_inspection"}
    end
    subgraph tier_1["Tier 1"]
        n234["MON_demids_legacy"]
        n22{"MON_foundation_for_special_task_battalion"}
        n235["MON_mobilize_the_reserves"]
        n25["MON_ratify_battleplans"]
        n27{"MON_support_old_officers_corps"}
    end
    subgraph tier_2["Tier 2"]
        n28["MON_adopt_tsogs_methods"]
        n236["MON_desperate_measures"]
        n237["MON_field_hospital_initiative"]
        n30["MON_gobi_training_facilities"]
        n238["MON_improve_coordination_capabilities"]
        n239["MON_lessons_from_1934_rebellion"]
        n31["MON_mountainous_specialization"]
        n32["MON_rely_on_soviet_tactics"]
        n33["MON_revive_forgotten_doctrines"]
        n34["MON_the_grand_stratagem"]
    end
    subgraph tier_3["Tier 3"]
        n36["MON_bolster_national_awareness"]
        n37["MON_equipment_recovery_teams"]
        n38["MON_favour_stronghold_defenses"]
        n39["MON_focus_on_infantry"]
        n40["MON_improve_militia_formations"]
        n41["MON_investigate_improvement_opportunities"]
        n42["MON_strengthen_air_land_links"]
        n44["MON_support_tactical_decision_freedom"]
        n45["MON_weapon_prototype_development"]
    end
    subgraph tier_4["Tier 4"]
        n46["MON_advanced_fortification_studies"]
        n47["MON_combined_arms_operations"]
        n48["MON_expand_universal_military_act"]
        n49["MON_feature_compact_mortar_designs"]
        n50["MON_ideological_loyalty_of_the_masses"]
        n51["MON_mass_firearm_production"]
        n52["MON_optimize_infantry_formations"]
        n54["MON_the_inevitable_counterblow"]
    end
    subgraph tier_5["Tier 5"]
        n56["MON_good_old_new_ways"]
        n57["MON_suitable_high_command"]
        n58["MON_the_ultimate_weapon"]
        n60["MON_unified_operational_command"]
    end
    n21 --> n28
    n27 --> n28
    n38 --> n46
    n33 --> n36
    n42 --> n47
    n20 --> n234
    n235 --> n236
    n31 --> n37
    n30 --> n37
    n36 --> n48
    n34 --> n38
    n41 --> n49
    n235 --> n237
    n32 --> n39
    n20 --> n22
    n19 --> n22
    n22 --> n30
    n50 --> n56
    n48 --> n56
    n40 --> n50
    n234 --> n238
    n33 --> n40
    n28 --> n41
    n234 --> n239
    n45 --> n51
    n20 --> n235
    n22 --> n31
    n44 --> n52
    n19 --> n25
    n20 --> n25
    n21 --> n32
    n27 --> n32
    n27 --> n33
    n28 --> n42
    n51 --> n57
    n54 --> n57
    n19 --> n27
    n20 --> n27
    n34 --> n44
    n21 --> n34
    n27 --> n34
    n39 --> n54
    n49 --> n58
    n47 --> n58
    n52 --> n60
    n46 --> n60
    n32 --> n45
    n28 x--x n29
    n28 x--x n32
    n28 x--x n33
    n28 x--x n34
    n29 x--x n32
    n29 x--x n33
    n29 x--x n34
    n21 x--x n27
    n30 x--x n31
    n32 x--x n33
    n32 x--x n34
    n33 x--x n34
```

# MON_rely_on_national_strength

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n174["MON_a_socialist_republic"]
        n148["MON_establish_socialist_society"]
        n184{"MON_example_of_communist_paradise"}
        n64["MON_form_the_provisional_government"]
        n65["MON_hold_plenum_of_central_committee"]
        n66["MON_host_emergency_great_khural_assembly"]
        n133["MON_joint_technological_development"]
        n67(("MON_rely_on_national_strength"))
        n79{"MON_return_of_prodigal_son"}
        n192{"MON_true_hero_for_the_people"}
    end
    subgraph tier_1["Tier 1"]
        n240["MON_expel_choibalsan"]
        n72["MON_faciliate_cooperation_with_china"]
        n128["MON_limited_research_cooperation"]
        n241["MON_subvert_soviet_control"]
    end
    subgraph tier_2["Tier 2"]
        n75["MON_expand_the_role_of_urga_national_library"]
        n68{"MON_sabotage_great_khural"}
        n242["MON_strengthen_existing_industrial_contracts"]
        n140["MON_student_exchange_program"]
    end
    subgraph tier_3["Tier 3"]
        n143["MON_reform_national_script"]
        n145["MON_solidify_language_institutes"]
        n69["MON_stabilize_the_country"]
        n84["MON_strong_leader_genden"]
    end
    subgraph tier_4["Tier 4"]
        n85["MON_continue_new_course_policy"]
        n86{"MON_dealing_with_soviet_sympathisers"}
        n63["MON_denounce_politizised_army"]
        n243["MON_form_the_rightist_cabinet"]
        n87["MON_incorporate_buddhism"]
        n131{"MON_reach_out_to_moscow"}
        n154["MON_ulaanbaatar_national_university"]
    end
    subgraph tier_5["Tier 5"]
        n244{"MON_compromise_with_lamas"}
        n91["MON_empower_hudonets"]
        n159{"MON_ensure_mvd_loyalty"}
        n92["MON_get_rich"]
        n93["MON_independent_army_structure"]
        n130{"MON_prepare_for_the_inevitable"}
        n245["MON_repay_old_debths"]
        n246["MON_secularization_of_education"]
    end
    subgraph tier_6["Tier 6"]
        n167["MON_contest_the_insurgents"]
        n94["MON_ensure_soldier_loyalty"]
        n247["MON_excessive_military_build_up"]
        n185["MON_frontline_infrastructure"]
        n248{"MON_invite_foreign_investors"}
        n95{"MON_provide_for_the_people"}
        n96["MON_reform_the_high_command"]
        n190{"MON_stay_on_guard"}
        n172["MON_support_the_rebels"]
    end
    subgraph tier_7["Tier 7"]
        n97{"MON_abolish_the_secretary_system"}
        n193["MON_central_asia_defensive_pact"]
        n194["MON_changing_times"]
        n196{"MON_dream_of_greater_mongolia"}
        n197["MON_first_five_year_plan_focus"]
        n178["MON_formalize_the_treaty"]
        n98{"MON_mongolian_peoples_army"}
        n99["MON_oust_genden"]
        n249["MON_peace_and_prosperity"]
        n100["MON_subsidise_the_military"]
    end
    subgraph tier_8["Tier 8"]
        n200["MON_a_pragmatic_diplomacy"]
        n101["MON_changes_within"]
        n250{"MON_declare_official_neutrality"}
        n202["MON_delegation_to_tuva"]
        n203["MON_expand_the_treaty"]
        n205["MON_gather_ulaanbaatar_conference"]
        n207["MON_intervene_in_sinkiang"]
        n208["MON_join_the_big_brother"]
        n102["MON_leader_of_the_equal"]
        n209["MON_mengjian_issue"]
        n103["MON_spread_of_anarcho_communism"]
    end
    subgraph tier_9["Tier 9"]
        n104["MON_abolish_the_currency"]
        n61["MON_adopt_sun_yat_sen_principles"]
        n212["MON_disagreements_with_sinkiang"]
        n213["MON_divide_spheres_of_influence"]
        n105["MON_full_social_equality"]
        n215["MON_gobi_border_realignment"]
        n218["MON_one_mongolia_policy"]
        n129{"MON_open_up_the_country"}
        n106["MON_promote_religious_socialism"]
    end
    subgraph tier_10["Tier 10"]
        n221["MON_a_unity_with_buryats"]
        n251["MON_appeal_for_overseas_protection"]
        n252["MON_appeal_to_european_democracies"]
        n107["MON_cooperation_with_kuomintang"]
        n253["MON_democratic_foundation_of_mongolia"]
        n108["MON_eradicate_private_property"]
        n224["MON_joint_pilgrimage_to_mount_wutai"]
        n210["MON_oppose_soviet_colonialism"]
        n109["MON_remove_hierarchical_structures"]
        n254["MON_riders_of_the_storm"]
        n227["MON_secure_hexi_corridor"]
        n228["MON_secure_the_rear"]
        n255["MON_seek_democratic_alliances"]
        n110["MON_support_buddhist_monasteries"]
        n256["MON_welfare_focus"]
        n111["MON_workers_control_and_discipline"]
    end
    subgraph tier_11["Tier 11"]
        n257["MON_bulwark_against_fascist_threat"]
        n214["MON_expand_influence_into_greater_steppe"]
        n112["MON_finalize_state_reforms"]
        n258["MON_forge_asian_self_determination"]
        n229["MON_incorporate_new_lands"]
        n113{"MON_nationalism"}
        n259["MON_provide_shelter_for_refugees"]
        n114{"MON_put_an_end_to_the_arat_system"}
        n231["MON_reignite_the_civil_war"]
        n260["MON_strike_against_communist_menace"]
        n219["MON_support_east_siberian_independists"]
        n233["MON_the_second_northern_expedition"]
        n220["MON_weaken_soviet_control_over_northwestern_siberia"]
    end
    subgraph tier_12["Tier 12"]
        n115{"MON_codify_democratic_principles"}
        n222["MON_increase_presence_in_caucasus"]
        n223["MON_infiltrate_transural_region"]
        n261["MON_offer_facilities_for_exiled_scientists"]
        n226["MON_plea_to_the_russian_far_east"]
        n116["MON_revoke_the_kyakhta_treaty"]
    end
    subgraph tier_13["Tier 13"]
        n117["MON_five_races_under_one_union"]
        n230["MON_launch_peoples_uprising"]
    end
    subgraph tier_14["Tier 14"]
        n118["MON_confrontations_with_warlords"]
        n119["MON_the_battle_for_tuva_uriankai"]
    end
    n196 --> n200
    n212 --> n221
    n202 --> n221
    n101 --> n104
    n95 --> n97
    n250 --> n61
    n129 --> n251
    n129 --> n252
    n255 --> n257
    n253 --> n257
    n190 --> n193
    n192 --> n193
    n99 --> n101
    n184 --> n194
    n192 --> n194
    n190 --> n194
    n61 --> n115
    n113 --> n115
    n243 --> n244
    n116 --> n118
    n117 --> n118
    n159 --> n167
    n84 --> n85
    n61 --> n107
    n106 --> n107
    n84 --> n86
    n249 --> n250
    n196 --> n202
    n193 --> n202
    n129 --> n253
    n69 --> n63
    n200 --> n212
    n205 --> n213
    n192 --> n196
    n184 --> n196
    n190 --> n196
    n85 --> n91
    n131 --> n159
    n148 --> n159
    n93 --> n94
    n105 --> n108
    n104 --> n108
    n130 --> n247
    n210 --> n214
    n72 --> n75
    n193 --> n203
    n67 --> n240
    n67 --> n72
    n64 --> n72
    n111 --> n112
    n109 --> n112
    n184 --> n197
    n192 --> n197
    n190 --> n197
    n113 --> n117
    n115 --> n117
    n114 --> n117
    n253 --> n258
    n69 --> n243
    n172 --> n178
    n174 --> n185
    n130 --> n185
    n101 --> n105
    n196 --> n205
    n85 --> n92
    n200 --> n215
    n205 --> n215
    n84 --> n87
    n205 --> n229
    n221 --> n229
    n214 --> n222
    n63 --> n93
    n86 --> n93
    n220 --> n223
    n193 --> n207
    n245 --> n248
    n194 --> n208
    n213 --> n224
    n223 --> n230
    n226 --> n230
    n222 --> n230
    n86 --> n102
    n98 --> n102
    n97 --> n102
    n67 --> n128
    n193 --> n209
    n96 --> n98
    n94 --> n98
    n107 --> n113
    n259 --> n261
    n200 --> n218
    n250 --> n129
    n130 --> n129
    n193 --> n210
    n129 --> n210
    n95 --> n99
    n244 --> n249
    n248 --> n249
    n219 --> n226
    n131 --> n130
    n102 --> n106
    n91 --> n95
    n92 --> n95
    n253 --> n259
    n255 --> n259
    n107 --> n114
    n69 --> n131
    n133 --> n143
    n140 --> n143
    n93 --> n96
    n228 --> n231
    n227 --> n231
    n105 --> n109
    n131 --> n245
    n243 --> n245
    n114 --> n116
    n129 --> n254
    n241 --> n68
    n240 --> n68
    n243 --> n246
    n213 --> n227
    n213 --> n228
    n129 --> n255
    n128 --> n145
    n140 --> n145
    n99 --> n103
    n68 --> n69
    n174 --> n190
    n130 --> n190
    n128 --> n242
    n255 --> n260
    n253 --> n260
    n68 --> n84
    n79 --> n84
    n133 --> n140
    n128 --> n140
    n95 --> n100
    n67 --> n241
    n106 --> n110
    n210 --> n219
    n159 --> n172
    n116 --> n119
    n117 --> n119
    n224 --> n233
    n228 --> n233
    n145 --> n154
    n143 --> n154
    n210 --> n220
    n61 --> n256
    n104 --> n111
    n200 x--x n205
    n193 x--x n196
    n193 x--x n129
    n167 x--x n172
    n253 x--x n255
    n196 x--x n129
    n117 x--x n116
    n64 x--x n67
    n65 x--x n67
    n66 x--x n67
    n102 x--x n99
    n129 x--x n129
    n249 x--x n130
    n69 x--x n84
```

# MON_transfer_the_funds_of_mongolbank

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n262(("MON_transfer_the_funds_of_mongolbank"))
    end
    subgraph tier_1["Tier 1"]
        n263{"MON_build_the_railroads"}
        n264["MON_encourage_foreign_trade"]
        n265{"MON_expand_elementary_schools"}
        n266{"MON_improve_machine_tools"}
        n267["MON_strengthen_tugrik"]
        n268{"MON_study_foreign_radio_equipment"}
    end
    subgraph tier_2["Tier 2"]
        n269["MON_end_reliance_on_animal_husbandry"]
        n270["MON_pastures_into_farms"]
    end
    subgraph tier_3["Tier 3"]
        n271["MON_build_energokombinat"]
        n272["MON_build_mechanical_factory"]
        n273["MON_expand_woolwashing_facilities"]
        n274["MON_industrial_expansion"]
        n275["MON_support_arats"]
    end
    subgraph tier_4["Tier 4"]
        n276["MON_armament_expansion"]
        n277["MON_improve_mining_facilities"]
        n278["MON_new_veterinary_facilities"]
        n279["MON_ulan_bator_promcombinat"]
    end
    subgraph tier_5["Tier 5"]
        n280["MON_modernize_transportation_system"]
        n281["MON_new_research_centres"]
        n282["MON_southern_development_focus"]
    end
    subgraph tier_6["Tier 6"]
        n283["MON_assist_subsidized_region"]
        n284["MON_develop_mongolia_proper"]
        n285["MON_develop_the_rear"]
        n286["MON_encourage_southern_agriculture"]
        n287["MON_expand_chahars_processing_region"]
        n288["MON_improve_baigaal_dalai_industries"]
        n289["MON_ordos_plateau_exploitation"]
        n290["MON_southwest_resource_prospection_area"]
    end
    subgraph tier_7["Tier 7"]
        n291["MON_military_industries_expansion"]
        n292["MON_utilize_available_spaces"]
    end
    n272 --> n276
    n274 --> n276
    n280 --> n283
    n270 --> n271
    n269 --> n271
    n270 --> n272
    n269 --> n272
    n262 --> n263
    n280 --> n284
    n280 --> n285
    n262 --> n264
    n282 --> n286
    n266 --> n269
    n268 --> n269
    n282 --> n287
    n262 --> n265
    n270 --> n273
    n269 --> n273
    n280 --> n288
    n262 --> n266
    n271 --> n277
    n269 --> n274
    n285 --> n291
    n288 --> n291
    n284 --> n291
    n283 --> n291
    n276 --> n280
    n278 --> n280
    n276 --> n281
    n278 --> n281
    n275 --> n278
    n273 --> n278
    n282 --> n289
    n263 --> n270
    n265 --> n270
    n276 --> n282
    n278 --> n282
    n282 --> n290
    n262 --> n267
    n262 --> n268
    n270 --> n275
    n271 --> n279
    n290 --> n292
    n286 --> n292
    n287 --> n292
    n289 --> n292
    n269 x--x n270
```
