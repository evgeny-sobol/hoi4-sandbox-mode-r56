# CHI_industrial_investment2

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CHI_industrial_investment2"))
    end
    subgraph tier_1["Tier 1"]
        n2["CHI_local_arms_production2"]
        n3["CHI_public_education_reform2"]
    end
    subgraph tier_2["Tier 2"]
        n4["CHI_local_arms_development2"]
        n5["CHI_long_term_economic_planning2"]
    end
    subgraph tier_3["Tier 3"]
        n6["CHI_heavy_weapons_development2"]
    end
    n4 --> n6
    n2 --> n4
    n1 --> n2
    n2 --> n5
    n1 --> n3
```

# CHI_maintain_the_status_quo

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n7{"CHI_cooperation_with_the_nationalists"}
        n8{"CHI_maintain_the_status_quo"}
        n9["CHI_secure_internal_politics2"]
    end
    subgraph tier_1["Tier 1"]
        n10["CHI_allow_civillian_pillaging"]
        n11["CHI_bribe_chinese_officials"]
        n12["CHI_centralise_authority_around_the_warlord"]
        n13["CHI_contacts_in_the_roc"]
        n14["CHI_denounce_the_japanese_empire"]
        n15["CHI_request_kmt_protection"]
        n16["CHI_siphon_local_trade"]
        n17["SIC_the_sichuan_clique"]
        n18["SIK_cooperate_with_the_ussr"]
        n19["SIK_office_of_sinkiang_border_commissioner"]
        n20["XIC_discussions_in_luochuan"]
        n21["XIC_finish_the_encirclement_campaign_r56"]
        n22["XIC_sixth_encirclement_campaign"]
        n23["XIC_towards_peace_across_china_r56"]
        n24["XSM_the_military_governor"]
        n25["YUN_rally_around_long_yun"]
        n26["r56_XSM_sideline_family_conflicts"]
    end
    subgraph tier_2["Tier 2"]
        n27{"CHI_an_oath_of_loyalty"}
        n28{"CHI_mass_drug_export"}
        n29["CHI_secure_kmt_funds"]
        n30["CHI_seize_assets_for_the_military"]
        n31["CHI_seize_japanese_assets"]
        n32["CHI_seize_western_assets"]
        n33["KHM_expand_the_madrasas"]
        n34["KHM_indian_expeditionary_forces_plan"]
        n35["SIC_the_armies_of_yang_sen"]
        n36["SIC_the_domain_of_liu_wenhui"]
        n37["SIC_the_governor_of_sichuan"]
        n38["SIK_establish_the_xinjiangneft"]
        n39["SIK_military_cooperation"]
        n40["SIK_six_great_policies"]
        n41["SIK_utilize_asperovs_contacts"]
        n42{"XIC_consolidate_authority_in_shaanxi_r56"}
        n43{"XIC_force_an_end_to_the_fighting_r56"}
        n44["XIC_non_agression_pact_with_the_cpc"]
        n45["XIC_request_relocation_to_northeastern_command"]
        n46["XIC_send_a_representative_to_sheng_shicai"]
        n47["XSM_a_hui_army"]
        n48["XSM_sway_the_people"]
        n49["YUN_a_land_of_mountains"]
        n50["YUN_expand_local_infrastructure"]
        n51{"r56_XSM_strengthening_our_position"}
    end
    subgraph tier_3["Tier 3"]
        n52["CHI_a_concerted_effort_to_the_japanese_sphere"]
        n53["CHI_proliferate_the_chinese_drug_trade"]
        n54["CHI_recruit_the_disenfanchised"]
        n55["CHI_seize_chinese_assets"]
        n56["KHM_promote_anti_communism"]
        n57["SIC_anti_communism"]
        n58["SIC_develop_chongqing"]
        n59["SIC_develop_xikang"]
        n60["SIK_a_soviet_airforce"]
        n61["SIK_cooperate_with_the_nkvd"]
        n62["SIK_invest_in_the_dushanzi_oil_fields"]
        n63{"SIK_march_into_khotan"}
        n64["SIK_three_year_plan_for_reconstruction"]
        n65["XIC_a_new_path_for_china_r56"]
        n66["XIC_invite_zuolin_loyalsits"]
        n67["XIC_reestablish_the_zhili_army"]
        n68["XIC_return_to_nanjing_r56"]
        n69["XIC_synthesis_with_the_communists_r56"]
        n70["XIC_the_fushi_conference"]
        n71{"XSM_sweep_out_communists"}
        n72["YUN_political_reforms"]
        n73["YUN_strive_for_self_sufficiency"]
        n74["r56_XSM_demand_submission"]
        n75["r56_XSM_strike_at_the_detractors"]
    end
    subgraph tier_4["Tier 4"]
        n76["CHI_a_grand_army_for_the_warlord"]
        n77["KHM_raise_additional_dungan_regiments"]
        n78["SIC_armor_efforts"]
        n79["SIC_drive_out_the_japanese"]
        n80["SIC_push_back_the_tibetans"]
        n81["SIK_a_new_xinjiang"]
        n82["SIK_a_united_sinkiang_clique"]
        n83["SIK_pursue_further_soviet_integration"]
        n84["SIK_soviet_intervention"]
        n85["XIC_anti_japanese_national_salvation_agreement"]
        n86["XIC_recruit_mancurian_bandits"]
        n87["XIC_restore_the_glory_of_the_fengtian_army"]
        n88["XSM_send_ma_lin_on_hajj"]
        n89["XSM_the_civilian_governor_remains"]
        n90["YUN_eduational_reforms"]
        n91["r56_XSM_a_united_ma_state"]
    end
    subgraph tier_5["Tier 5"]
        n92["SIC_sichuan_still_stands"]
        n93["SIK_a_new_nationality_policy"]
        n94["SIK_ensure_a_clean_government"]
        n95["SIK_protector_of_the_kyrgiz"]
        n96["SIK_settle_dzungarian_tribes"]
        n97["SIK_transformation_of_nature"]
        n98["XIC_form_the_anti_japanese_comrades_association"]
        n99["XIC_reclaim_the_lost_birthright"]
        n100["XIC_withdraw_forces_from_yanan"]
        n101["XSM_ma_qis_natural_successor"]
        n102["XSM_recruit_salar_officers"]
        n103["XSM_solidifying_control"]
        n104["YUN_the_democratic_fortress"]
    end
    subgraph tier_6["Tier 6"]
        n105{"SIK_king_of_sinkiang"}
        n106["XIC_invite_chiang_for_troop_inspections"]
        n107["XIC_restore_the_homeland"]
        n108["XSM_rebuild_the_ninghai_army"]
        n109["YUN_strengthen_burmic_ties"]
    end
    subgraph tier_7["Tier 7"]
        n110["SIK_reaffirm_soviet_connections"]
        n111["SIK_reestablish_the_guominjun"]
        n112["SIK_rejoin_the_central_government"]
        n113["XIC_revive_the_beiyang_government"]
    end
    n28 --> n52
    n54 --> n76
    n27 --> n76
    n8 --> n10
    n14 --> n27
    n12 --> n27
    n8 --> n11
    n8 --> n12
    n8 --> n13
    n8 --> n14
    n16 --> n28
    n13 --> n28
    n28 --> n53
    n30 --> n54
    n8 --> n15
    n15 --> n29
    n10 --> n30
    n27 --> n55
    n14 --> n31
    n12 --> n32
    n8 --> n16
    n26 --> n33
    n26 --> n34
    n33 --> n56
    n56 --> n77
    n35 --> n57
    n58 --> n78
    n37 --> n58
    n36 --> n59
    n57 --> n79
    n59 --> n80
    n78 --> n92
    n17 --> n35
    n17 --> n36
    n17 --> n37
    n7 --> n17
    n8 --> n17
    n82 --> n93
    n83 --> n93
    n64 --> n81
    n61 --> n81
    n39 --> n60
    n63 --> n82
    n41 --> n61
    n8 --> n18
    n84 --> n94
    n83 --> n94
    n18 --> n38
    n38 --> n62
    n82 --> n105
    n93 --> n105
    n39 --> n63
    n19 --> n63
    n18 --> n39
    n8 --> n19
    n84 --> n95
    n63 --> n83
    n105 --> n110
    n105 --> n111
    n105 --> n112
    n82 --> n96
    n19 --> n40
    n63 --> n84
    n41 --> n64
    n84 --> n97
    n83 --> n97
    n81 --> n97
    n18 --> n41
    n42 --> n65
    n70 --> n85
    n21 --> n42
    n8 --> n20
    n7 --> n20
    n8 --> n21
    n7 --> n21
    n23 --> n43
    n85 --> n98
    n98 --> n106
    n100 --> n106
    n45 --> n66
    n20 --> n44
    n87 --> n99
    n67 --> n86
    n45 --> n67
    n22 --> n45
    n67 --> n87
    n66 --> n87
    n99 --> n107
    n43 --> n68
    n42 --> n68
    n107 --> n113
    n20 --> n46
    n8 --> n22
    n7 --> n22
    n43 --> n69
    n44 --> n70
    n46 --> n70
    n8 --> n23
    n7 --> n23
    n85 --> n100
    n24 --> n47
    n89 --> n101
    n103 --> n108
    n88 --> n102
    n71 --> n88
    n89 --> n103
    n88 --> n103
    n24 --> n48
    n48 --> n71
    n47 --> n71
    n71 --> n89
    n8 --> n24
    n7 --> n24
    n25 --> n49
    n72 --> n90
    n73 --> n90
    n25 --> n50
    n49 --> n72
    n8 --> n25
    n7 --> n25
    n104 --> n109
    n50 --> n73
    n90 --> n104
    n74 --> n91
    n75 --> n91
    n51 --> n74
    n8 --> n26
    n26 --> n51
    n51 --> n75
    n52 x--x n53
    n8 x--x n9
    n15 x--x n55
    n82 x--x n83
    n82 x--x n84
    n83 x--x n84
    n110 x--x n111
    n110 x--x n112
    n111 x--x n112
    n65 x--x n68
    n65 x--x n69
    n20 x--x n22
    n21 x--x n23
    n68 x--x n69
    n88 x--x n89
    n74 x--x n75
```

# CHI_proclaim_rival_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n114(("CHI_proclaim_rival_government"))
    end
    subgraph tier_1["Tier 1"]
        n115["CHI_march_on_nanjing"]
        n116["CHI_march_on_the_cliques"]
    end
    subgraph tier_2["Tier 2"]
        n117["CHI_prepare_to_kick_out_the_japanese"]
        n118["CHI_the_great_restoration"]
    end
    subgraph tier_3["Tier 3"]
        n119["CHI_an_all_chinese_university"]
        n120["CHI_demand_repealing_of_the_unequal_treaties"]
        n121["CHI_integrate_the_warlords"]
    end
    subgraph tier_4["Tier 4"]
        n122["CHI_a_great_unitary_china"]
    end
    n120 --> n122
    n119 --> n122
    n118 --> n119
    n118 --> n120
    n118 --> n121
    n114 --> n115
    n114 --> n116
    n115 --> n117
    n115 --> n118
```

# CHI_review_the_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n123{"CHI_review_the_army"}
    end
    subgraph tier_1["Tier 1"]
        n124{"CHI_a_central_high_command"}
        n125{"CHI_a_decentralized_high_command"}
        n126["CHI_review_the_fortifications"]
    end
    subgraph tier_2["Tier 2"]
        n127["CHI_a_modern_army"]
        n128["CHI_an_auxuliary_army"]
        n129["CHI_defense_of_the_fatherland"]
        n130["CHI_initial_fortification_tests"]
        n131["CHI_uncaring_warfare"]
    end
    subgraph tier_3["Tier 3"]
        n132["CHI_a_gruelling_training_regimen"]
        n133["CHI_a_gun_behind_every_rock"]
        n134["CHI_a_military_planning_school"]
        n135["CHI_a_proper_high_command"]
        n136["CHI_appropriate_civillian_stockpiles"]
        n137["CHI_fortify_the_frontier"]
        n138["CHI_high_level_forifications"]
        n139["CHI_legalize_farm_helping"]
        n140["CHI_slash_ration_sizes"]
    end
    subgraph tier_4["Tier 4"]
        n141["CHI_a_new_recruitment_centre"]
        n142["CHI_mass_military_impressment"]
        n143["CHI_task_specific_planning"]
        n144["CHI_the_country_is_where_the_general_is"]
    end
    subgraph tier_5["Tier 5"]
        n145["CHI_modern_warfare"]
        n146["CHI_mountain_training"]
    end
    subgraph tier_6["Tier 6"]
        n147["CHI_a_new_special_forces_project"]
        n148["CHI_a_new_tank_project"]
    end
    subgraph tier_7["Tier 7"]
        n149["CHI_uplift_the_special_forces"]
        n150["CHI_uplift_the_tanks"]
    end
    n123 --> n124
    n123 --> n125
    n128 --> n132
    n129 --> n133
    n131 --> n133
    n128 --> n134
    n127 --> n134
    n124 --> n127
    n135 --> n141
    n132 --> n147
    n146 --> n147
    n132 --> n148
    n145 --> n148
    n127 --> n135
    n129 --> n135
    n124 --> n128
    n131 --> n136
    n125 --> n129
    n130 --> n137
    n130 --> n138
    n126 --> n130
    n131 --> n139
    n139 --> n142
    n136 --> n142
    n141 --> n145
    n134 --> n145
    n141 --> n146
    n133 --> n146
    n123 --> n126
    n131 --> n140
    n128 --> n143
    n134 --> n143
    n131 --> n144
    n133 --> n144
    n125 --> n131
    n147 --> n149
    n148 --> n150
    n124 x--x n125
    n127 x--x n128
    n129 x--x n131
```

# CHI_sea_develop_capital_r56

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n151(("CHI_sea_develop_capital_r56"))
    end
    subgraph tier_1["Tier 1"]
        n152["CHI_sea_develop_capital_arsenal_r56"]
        n153["CHI_sea_further_industrial_investment_r56"]
    end
    subgraph tier_2["Tier 2"]
        n154["CHI_sea_expand_public_education_r56"]
        n155["CHI_sea_long_term_economic_planning_r56"]
        n156["CHI_sea_small_arms_production_r56"]
    end
    subgraph tier_3["Tier 3"]
        n157{"CHI_sea_fund_research_projects_r56"}
        n158["CHI_sea_heavy_weapons_development_r56"]
        n159["CHI_sea_industrial_research_projects_r56"]
    end
    subgraph tier_4["Tier 4"]
        n160["CHI_sea_modern_warfare_r56"]
        n161["CHI_sea_rely_on_our_infantry_r56"]
    end
    n151 --> n152
    n153 --> n154
    n152 --> n154
    n154 --> n157
    n151 --> n153
    n156 --> n158
    n155 --> n159
    n153 --> n155
    n157 --> n160
    n157 --> n161
    n152 --> n156
    n160 x--x n161
```

# CHI_secure_internal_politics2

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n8{"CHI_maintain_the_status_quo"}
        n9{"CHI_secure_internal_politics2"}
    end
    subgraph tier_1["Tier 1"]
        n7{"CHI_cooperation_with_the_nationalists"}
        n162{"CHI_oust_KMT_influence"}
    end
    subgraph tier_2["Tier 2"]
        n163["CHI_a_bulwark_of_defense"]
        n164["CHI_a_time_for_integration"]
        n165{"CHI_abandon_china"}
        n166["CHI_cooperation_with_the_communists"]
        n167["CHI_investments_from_nanjing"]
        n168{"CHI_new_model_province2"}
        n169{"CHI_opposition"}
        n170["CHI_technological_cooperation2"]
        n17["SIC_the_sichuan_clique"]
        n20["XIC_discussions_in_luochuan"]
        n21["XIC_finish_the_encirclement_campaign_r56"]
        n22["XIC_sixth_encirclement_campaign"]
        n23["XIC_towards_peace_across_china_r56"]
        n24["XSM_the_military_governor"]
        n25["YUN_rally_around_long_yun"]
    end
    subgraph tier_3["Tier 3"]
        n171["CHI_a_great_purge"]
        n172{"CHI_an_alternative_to_the_KMT"}
        n173["CHI_chinese_defense_industry"]
        n174["CHI_commander_political_training"]
        n175["CHI_embrace_corruption"]
        n176["CHI_expand_regional_identity"]
        n177{"CHI_fire_the_flames_of_islam"}
        n178["CHI_land_redistribution2"]
        n179["CHI_national_defense_fund"]
        n180["CHI_preempt_corruption"]
        n181["CHI_professionalize_the_army"]
        n182["CHI_public_works2"]
        n183["CHI_seek_japanese_support"]
        n35["SIC_the_armies_of_yang_sen"]
        n36["SIC_the_domain_of_liu_wenhui"]
        n37["SIC_the_governor_of_sichuan"]
        n42{"XIC_consolidate_authority_in_shaanxi_r56"}
        n43{"XIC_force_an_end_to_the_fighting_r56"}
        n44["XIC_non_agression_pact_with_the_cpc"]
        n45["XIC_request_relocation_to_northeastern_command"]
        n46["XIC_send_a_representative_to_sheng_shicai"]
        n47["XSM_a_hui_army"]
        n48["XSM_sway_the_people"]
        n49["YUN_a_land_of_mountains"]
        n50["YUN_expand_local_infrastructure"]
    end
    subgraph tier_4["Tier 4"]
        n184["CHI_a_declaration_of_statehood"]
        n185["CHI_a_religion_of_peace"]
        n186["CHI_a_true_chinese_republic"]
        n187["CHI_absolute_obedience"]
        n188["CHI_army_reform"]
        n189["CHI_begin_invitation_of_the_kwantung_army"]
        n190["CHI_begin_jihad_against_the_oppressors"]
        n191["CHI_break_the_kmt_stranglehold"]
        n192["CHI_cater_to_the_past"]
        n193["CHI_commence_nra_takeover"]
        n194["CHI_dabble_in_the_opium_trade"]
        n195["CHI_demand_workplace_integrity"]
        n196["CHI_devolop_a_cult_of_personality"]
        n197["CHI_ideological_education2"]
        n198["CHI_japanese_money"]
        n199["CHI_labor_reform2"]
        n200["CHI_land_value_tax2"]
        n201["CHI_meet_with_the_army"]
        n202["CHI_national_defense_state"]
        n203["CHI_prepare_for_national_unification2"]
        n204["CHI_prepare_for_the_three_year_plan"]
        n205["CHI_ramp_up_anti_communist_retoric"]
        n206["CHI_reinvigorate_the_national_economy"]
        n207["CHI_rural_militias2"]
        n57["SIC_anti_communism"]
        n58["SIC_develop_chongqing"]
        n59["SIC_develop_xikang"]
        n65["XIC_a_new_path_for_china_r56"]
        n66["XIC_invite_zuolin_loyalsits"]
        n67["XIC_reestablish_the_zhili_army"]
        n68["XIC_return_to_nanjing_r56"]
        n69["XIC_synthesis_with_the_communists_r56"]
        n70["XIC_the_fushi_conference"]
        n71{"XSM_sweep_out_communists"}
        n72["YUN_political_reforms"]
        n73["YUN_strive_for_self_sufficiency"]
    end
    subgraph tier_5["Tier 5"]
        n208{"CHI_alignment_with_the_kmt"}
        n209["CHI_an_integritable_workforce"]
        n210["CHI_an_organized_resistance_militia"]
        n211["CHI_arrest_kmt_officers"]
        n212["CHI_arrest_kmt_officials"]
        n213["CHI_begin_the_desinofication_of_root"]
        n214["CHI_communist_administrators2"]
        n215["CHI_crush_the_farmers"]
        n216["CHI_display_the_cruelty_of_chaing_and_mao"]
        n217["CHI_empower_the_regional_pla"]
        n218["CHI_fully_embrace_the_opium_trade"]
        n219["CHI_further_japanese_guns"]
        n220["CHI_government_of_national_salvation"]
        n221["CHI_increase_metal_output"]
        n222["CHI_increase_workplace_efficiency"]
        n223["CHI_infiltrate_hui_communities"]
        n224["CHI_japanese_military_support"]
        n225["CHI_judiciary_reforms2"]
        n226["CHI_military_training_in_japan"]
        n227["CHI_party_founding_act"]
        n228["CHI_professionalize_the_army_mp"]
        n229["CHI_project_gaosu_gonglu"]
        n230["CHI_project_gongchang"]
        n231["CHI_propaganda_against_the_kmt"]
        n232["CHI_question_of_the_system"]
        n233["CHI_radicalize_anti_japanese_retoric"]
        n234["CHI_radicalize_chinese_nationalism"]
        n235["CHI_reempower_religious_ideas"]
        n236["CHI_reinvest_the_collectivisations"]
        n237{"CHI_secure_warlord_support"}
        n238["CHI_submit_to_tokyo"]
        n239["CHI_the_territories_to_free"]
        n240["CHI_train_everywhere_always"]
        n241["CHI_unite_the_province"]
        n242["CHI_use_anti_chinese_intel_from_japan"]
        n78["SIC_armor_efforts"]
        n79["SIC_drive_out_the_japanese"]
        n80["SIC_push_back_the_tibetans"]
        n85["XIC_anti_japanese_national_salvation_agreement"]
        n86["XIC_recruit_mancurian_bandits"]
        n87["XIC_restore_the_glory_of_the_fengtian_army"]
        n88["XSM_send_ma_lin_on_hajj"]
        n89["XSM_the_civilian_governor_remains"]
        n90["YUN_eduational_reforms"]
    end
    subgraph tier_6["Tier 6"]
        n243["CHI_a_cleansing_of_the_new_state"]
        n244["CHI_a_japanese_national_government"]
        n245["CHI_a_new_alternative_form_of_nationalism"]
        n246["CHI_a_radical_hui"]
        n247["CHI_a_turkestani_national_state"]
        n248["CHI_additional_gongchang"]
        n249["CHI_advanced_metal_extraction"]
        n250["CHI_an_alternative_to_the_two"]
        n251["CHI_anti_KMT_propaganda"]
        n252{"CHI_assemble_the_regency_council"}
        n253["CHI_begin_the_war"]
        n254["CHI_break_the_back_of_the_kmt_forces"]
        n255{"CHI_convene_the_national_unity_congress"}
        n256["CHI_crush_the_workers"]
        n257["CHI_implement_new_methods"]
        n258["CHI_join_the_chinese_soviet"]
        n259["CHI_make_a_detailed_home_plan"]
        n260["CHI_our_own_military"]
        n261["CHI_our_own_military_industrial_complex"]
        n262["CHI_question_of_the_constitution"]
        n263["CHI_seize_the_colonial_possessions"]
        n264["CHI_shaping_the_state_in_ones_own_image"]
        n265["CHI_swap_out_non_hui_nobility"]
        n266["CHI_troops_for_mao"]
        n267["CHI_ultimatum_to_the_warlord"]
        n268["CHI_upgrade_the_gonglu"]
        n92["SIC_sichuan_still_stands"]
        n98["XIC_form_the_anti_japanese_comrades_association"]
        n99["XIC_reclaim_the_lost_birthright"]
        n100["XIC_withdraw_forces_from_yanan"]
        n101["XSM_ma_qis_natural_successor"]
        n102["XSM_recruit_salar_officers"]
        n103["XSM_solidifying_control"]
        n104["YUN_the_democratic_fortress"]
    end
    subgraph tier_7["Tier 7"]
        n269["CHI_a_constitutional_monarchy"]
        n270["CHI_a_largescale_economy"]
        n271["CHI_a_modern_workplace"]
        n272["CHI_a_new_chinese_empire"]
        n273["CHI_a_new_peoples_republic"]
        n274["CHI_an_economy_for_the_proletariat"]
        n275["CHI_consolidate_control_over_china"]
        n276["CHI_deal_with_anti_japanese_hatred"]
        n277["CHI_declare_victory_over_the_fiends"]
        n278["CHI_enshrine_the_national_savior"]
        n279["CHI_finalize_the_gonglu"]
        n280["CHI_full_membership_in_the_republic"]
        n281["CHI_hold_free_elections"]
        n282["CHI_lay_claim_to_muslim_china"]
        n283["CHI_learn_from_the_maoists"]
        n284["CHI_loyalty_has_its_rewards"]
        n285["CHI_oust_kmt_troublemakers"]
        n286["CHI_republic_without_democracy"]
        n287["CHI_synthetic_oil_production"]
        n288{"CHI_the_jihad_successfull"}
        n106["XIC_invite_chiang_for_troop_inspections"]
        n107["XIC_restore_the_homeland"]
        n108["XSM_rebuild_the_ninghai_army"]
        n109["YUN_strengthen_burmic_ties"]
    end
    subgraph tier_8["Tier 8"]
        n289["CHI_a_great_turkestan"]
        n290["CHI_a_model_province_indeed"]
        n291["CHI_an_islamic_state"]
        n292["CHI_begin_operations"]
        n293["CHI_denounce_the_roc"]
        n294["CHI_federalist_victory"]
        n295["CHI_instate_sharia_law"]
        n296["CHI_lkmt_victory"]
        n297["CHI_national_regeneration_league_victory"]
        n298["CHI_open_domestic_politics"]
        n299["CHI_prepare_supply_lines"]
        n300["CHI_stabilize_the_economy"]
        n301["CHI_staff_the_royal_court"]
        n302["CHI_state_confutionism"]
        n303["CHI_supreme_leader_of_all_china"]
        n304["CHI_the_caliphate_of_china"]
        n305["CHI_the_three_principles_of_the_nation"]
        n306["CHI_the_warlord_stays"]
        n307{"CHI_western_victory"}
        n113["XIC_revive_the_beiyang_government"]
    end
    subgraph tier_9["Tier 9"]
        n308["CHI_a_victory_for_islam"]
        n309["CHI_adopt_the_penal_code"]
        n310["CHI_an_enabling_act"]
        n311["CHI_begin_preparations_for_jihad"]
        n312["CHI_begin_the_quest_for_developental_aid"]
        n313["CHI_christian_democracy"]
        n314["CHI_consolidate_imperial_power"]
        n315["CHI_empower_the_federal_states"]
        n316["CHI_minzhu_minsheng"]
        n317["CHI_province_work_force_conscription"]
        n318["CHI_reinstate_the_jizya"]
        n319["CHI_royal_splendour"]
        n320["CHI_sanchun"]
        n321["CHI_sanqiang"]
        n322["CHI_santong"]
        n323["CHI_secular_institutions"]
        n324["CHI_strengthen_the_conservatives"]
        n325["CHI_strengthen_the_radicals"]
        n326["CHI_the_national_unity_government"]
        n327["CHI_totaltarianism_after_allahs_word"]
    end
    subgraph tier_10["Tier 10"]
        n328["CHI_a_new_federalist_national_government"]
        n329["CHI_a_unitary_education"]
        n330["CHI_american_money"]
        n331["CHI_an_appeal_for_autonomy"]
        n332["CHI_british_money"]
        n333["CHI_cai"]
        n334["CHI_collect_funds_for_the_jihad"]
        n335["CHI_consolidate_the_national_unity_government"]
        n336["CHI_core_tenants_of_the_faith"]
        n337["CHI_crackdown_on_the_kmt"]
        n338["CHI_eliminate_all_dissent"]
        n339["CHI_empower_party_democracy"]
        n340["CHI_empower_the_capitalists"]
        n341["CHI_empower_the_military"]
        n342["CHI_enforced_social_values"]
        n343["CHI_entice_british_investments"]
        n344["CHI_envoy_to_germany"]
        n345["CHI_french_money"]
        n346["CHI_full_hezhong"]
        n347["CHI_guo"]
        n348["CHI_hoist_the_red_flag"]
        n349["CHI_invest_in_the_royal_army"]
        n350["CHI_min"]
        n351["CHI_modernize_the_armed_forces"]
        n352["CHI_nationalist_socialist_indoctrination"]
        n353["CHI_nationalize_corrupt_buisnesses"]
        n354["CHI_provide_funds_for_local_infrastructure"]
        n355["CHI_reach_out_to_the_local_elites"]
        n356["CHI_ready_the_army_of_jihad"]
        n357["CHI_wang"]
        n358["CHI_wen"]
        n359["CHI_work_out_provincial_workforce_regulations"]
        n360["CHI_wu"]
        n361["CHI_xie"]
        n362["CHI_xin"]
        n363["CHI_zhi"]
    end
    subgraph tier_11["Tier 11"]
        n364["CHI_a_declaration_from_the_clergy"]
        n365["CHI_a_god_honorig_legal_code"]
        n366["CHI_a_modern_economy"]
        n367["CHI_a_national_chinese_empire"]
        n368["CHI_appropriate_the_fuhrerprinzip"]
        n369{"CHI_autonomy_for_the_fractured_states"}
        n370["CHI_begin_local_industrialisation"]
        n371["CHI_begin_the_cultural_revolution"]
        n372["CHI_conversion_by_the_sword"]
        n373["CHI_economic_mobilization"]
        n374["CHI_enforce_local_military_budgets"]
        n375["CHI_foster_a_chinese_volksgemeinschaft"]
        n376["CHI_full_autarky"]
        n377["CHI_modern_innovations"]
        n378{"CHI_prepare_for_national_unification"}
        n379["CHI_prepare_to_unite_the_kingdom"]
        n380["CHI_reach_out_to_nanjing"]
        n381["CHI_rewrite_the_constitiution"]
        n382["CHI_stabilze_the_economy"]
        n383["CHI_strike_forth"]
        n384["CHI_the_second_thrid_congress_of_the_kmt"]
        n385["CHI_total_mobilization_for_the_emporer"]
    end
    subgraph tier_12["Tier 12"]
        n386["CHI_a_coalition_gov_for_national_survival"]
        n387["CHI_a_final_blow_to_the_kmt"]
        n388["CHI_a_modern_national_army"]
        n389["CHI_beacon_of_federalism"]
        n390["CHI_break_the_confucionists"]
        n391["CHI_construct_minarets"]
        n392["CHI_demand_transferance_of_national_power"]
        n393["CHI_donations_for_the_national_army"]
        n394["CHI_donations_for_the_welfare_of_the_people"]
        n395["CHI_drive_out_the_foreign_devils"]
        n396["CHI_help_the_cim"]
        n397["CHI_import_western_technology"]
        n398{"CHI_lobby_for_western_recognition"}
        n399["CHI_pillage_the_occupied_lands"]
        n400{"CHI_prepare_for_the_second_northern_expedition"}
        n401["CHI_reach_out_to_moscow"]
        n402["CHI_reorganize_the_party_along_lenninist_lines"]
        n403{"CHI_seek_recognition_from_the_occident"}
        n404["CHI_society_as_allah_ordained_it"]
        n405["CHI_state_funding_for_religious_schools"]
        n406["CHI_the_fate_of_the_overrun_lands"]
        n407["CHI_there_is_only_one_language_chaing_speaks"]
        n408["CHI_unbridled_capitalism"]
        n409["CHI_undo_the_damage_of_the_cim"]
    end
    subgraph tier_13["Tier 13"]
        n410["CHI_a_new_republic"]
        n411["CHI_a_new_socalled_religion"]
        n412["CHI_collapse_the_coalition"]
        n413{"CHI_democratic_centralism"}
        n414["CHI_destroy_foreign_thought"]
        n415["CHI_extol_chinese_nationalism"]
        n416["CHI_further_increase_resource_output"]
        n417["CHI_join_the_republican_government"]
        n418["CHI_one_china_two_systems"]
        n419["CHI_only_we_can_save_china"]
        n420["CHI_purge_the_reactionary"]
        n421["CHI_request_military_aid"]
        n422["CHI_request_official_recognition"]
        n423["CHI_resurrect_the_anti_chaing_coalition"]
        n424["CHI_take_leadership_of_islam"]
    end
    subgraph tier_14["Tier 14"]
        n425["CHI_a_final_warning"]
        n426["CHI_a_friendship_with_the_warlords"]
        n427["CHI_a_soviet_tank_advisors"]
        n428["CHI_an_alliance_with_the_rightists"]
        n429["CHI_an_olive_branch_to_the_communists"]
        n430["CHI_announce_full_communism"]
        n431{"CHI_full_control_over_the_apparatus_of_education"}
        n432["CHI_joint_ultimatum_to_prc"]
        n433["CHI_seek_support_from_the_democrats"]
        n434["CHI_socialism_not_communism"]
        n435["CHI_the_revolution_successfull"]
    end
    subgraph tier_15["Tier 15"]
        n436["CHI_a_place_in_the_comintern"]
        n437["CHI_enforce_loyalty_to_the_revolution"]
        n438["CHI_enshrine_the_yuan"]
        n439["CHI_free_china_from_imperialism"]
        n440["CHI_land_value_tax_3"]
        n441["CHI_march_on_chaing"]
        n442["CHI_state_atheism"]
        n443["CHI_support_chinese_religion"]
    end
    subgraph tier_16["Tier 16"]
        n444["CHI_federalism_the_savior_of_china"]
        n445["CHI_purge_the_decadence"]
        n446["CHI_seize_the_mantle_of_national_governance"]
        n447["CHI_sideline_the_radicals"]
        n448["CHI_state_owned_corporations"]
        n449["CHI_transfer_factories_to_the_proletariat"]
    end
    subgraph tier_17["Tier 17"]
        n450["CHI_beacon_of_communism"]
        n451["CHI_beacon_of_socialism"]
        n452["CHI_seize_merchant_property"]
    end
    subgraph tier_18["Tier 18"]
        n453["CHI_nationalize_foreign_assets"]
    end
    n7 --> n163
    n212 --> n243
    n211 --> n243
    n378 --> n386
    n252 --> n269
    n319 --> n364
    n337 --> n364
    n176 --> n184
    n364 --> n387
    n417 --> n425
    n423 --> n426
    n336 --> n365
    n166 --> n171
    n288 --> n289
    n238 --> n244
    n248 --> n270
    n279 --> n290
    n270 --> n290
    n271 --> n290
    n287 --> n290
    n343 --> n366
    n373 --> n388
    n377 --> n388
    n257 --> n271
    n361 --> n367
    n347 --> n367
    n358 --> n367
    n212 --> n245
    n211 --> n245
    n184 --> n245
    n252 --> n272
    n255 --> n272
    n315 --> n328
    n264 --> n273
    n403 --> n410
    n398 --> n410
    n390 --> n411
    n409 --> n411
    n432 --> n436
    n430 --> n436
    n223 --> n246
    n231 --> n246
    n177 --> n185
    n421 --> n427
    n7 --> n164
    n172 --> n186
    n213 --> n247
    n327 --> n329
    n309 --> n329
    n292 --> n308
    n162 --> n165
    n171 --> n187
    n230 --> n248
    n295 --> n309
    n221 --> n249
    n185 --> n208
    n312 --> n330
    n423 --> n428
    n169 --> n172
    n216 --> n250
    n315 --> n331
    n261 --> n274
    n297 --> n310
    n195 --> n209
    n288 --> n291
    n423 --> n429
    n190 --> n210
    n413 --> n430
    n227 --> n251
    n357 --> n368
    n350 --> n368
    n173 --> n188
    n168 --> n188
    n191 --> n211
    n191 --> n212
    n235 --> n252
    n233 --> n252
    n328 --> n369
    n449 --> n450
    n437 --> n450
    n346 --> n389
    n359 --> n389
    n370 --> n389
    n448 --> n451
    n438 --> n451
    n183 --> n189
    n177 --> n190
    n354 --> n370
    n282 --> n292
    n304 --> n311
    n291 --> n311
    n289 --> n311
    n247 --> n311
    n362 --> n371
    n363 --> n371
    n358 --> n371
    n201 --> n213
    n184 --> n213
    n307 --> n312
    n206 --> n312
    n239 --> n253
    n210 --> n254
    n231 --> n254
    n371 --> n390
    n176 --> n191
    n312 --> n332
    n321 --> n333
    n172 --> n192
    n168 --> n173
    n163 --> n173
    n307 --> n313
    n386 --> n412
    n311 --> n334
    n300 --> n334
    n163 --> n174
    n174 --> n193
    n181 --> n193
    n200 --> n214
    n244 --> n275
    n301 --> n314
    n302 --> n314
    n326 --> n335
    n383 --> n391
    n234 --> n255
    n233 --> n255
    n338 --> n372
    n318 --> n372
    n162 --> n166
    n9 --> n7
    n313 --> n336
    n314 --> n337
    n293 --> n337
    n205 --> n215
    n215 --> n256
    n175 --> n194
    n243 --> n276
    n259 --> n277
    n253 --> n277
    n369 --> n392
    n180 --> n195
    n402 --> n413
    n272 --> n293
    n269 --> n293
    n395 --> n414
    n172 --> n196
    n205 --> n216
    n375 --> n393
    n378 --> n393
    n375 --> n394
    n371 --> n395
    n361 --> n395
    n351 --> n373
    n327 --> n338
    n168 --> n175
    n324 --> n339
    n325 --> n339
    n323 --> n340
    n294 --> n315
    n324 --> n341
    n187 --> n217
    n354 --> n374
    n430 --> n437
    n309 --> n342
    n243 --> n278
    n245 --> n278
    n434 --> n438
    n319 --> n343
    n316 --> n344
    n165 --> n176
    n402 --> n415
    n439 --> n444
    n281 --> n294
    n268 --> n279
    n165 --> n177
    n7 --> n177
    n353 --> n375
    n352 --> n375
    n425 --> n439
    n312 --> n345
    n333 --> n376
    n413 --> n431
    n315 --> n346
    n258 --> n280
    n194 --> n218
    n408 --> n416
    n189 --> n219
    n205 --> n220
    n322 --> n347
    n365 --> n396
    n325 --> n348
    n251 --> n281
    n262 --> n281
    n178 --> n197
    n222 --> n257
    n382 --> n397
    n204 --> n221
    n204 --> n222
    n190 --> n223
    n288 --> n295
    n319 --> n349
    n7 --> n167
    n198 --> n224
    n189 --> n224
    n183 --> n198
    n225 --> n258
    n214 --> n258
    n392 --> n417
    n346 --> n417
    n422 --> n432
    n197 --> n225
    n182 --> n199
    n166 --> n178
    n178 --> n200
    n430 --> n440
    n434 --> n440
    n265 --> n282
    n267 --> n282
    n258 --> n283
    n281 --> n296
    n381 --> n398
    n266 --> n284
    n240 --> n259
    n433 --> n441
    n429 --> n441
    n426 --> n441
    n428 --> n441
    n176 --> n201
    n189 --> n226
    n322 --> n350
    n297 --> n316
    n351 --> n377
    n313 --> n351
    n323 --> n351
    n167 --> n179
    n173 --> n202
    n163 --> n202
    n286 --> n297
    n281 --> n297
    n326 --> n352
    n316 --> n352
    n316 --> n353
    n452 --> n453
    n7 --> n168
    n403 --> n418
    n398 --> n418
    n378 --> n419
    n400 --> n419
    n278 --> n298
    n162 --> n169
    n226 --> n260
    n219 --> n260
    n224 --> n260
    n236 --> n261
    n9 --> n162
    n250 --> n285
    n256 --> n285
    n186 --> n227
    n383 --> n399
    n168 --> n180
    n352 --> n378
    n176 --> n203
    n384 --> n400
    n168 --> n204
    n179 --> n204
    n282 --> n299
    n337 --> n379
    n163 --> n181
    n188 --> n228
    n204 --> n229
    n204 --> n230
    n190 --> n231
    n317 --> n354
    n294 --> n317
    n166 --> n182
    n437 --> n445
    n402 --> n420
    n232 --> n262
    n186 --> n232
    n196 --> n233
    n192 --> n233
    n196 --> n234
    n183 --> n205
    n384 --> n401
    n341 --> n380
    n339 --> n380
    n312 --> n355
    n311 --> n356
    n192 --> n235
    n300 --> n318
    n295 --> n318
    n200 --> n236
    n176 --> n206
    n384 --> n402
    n255 --> n286
    n401 --> n421
    n401 --> n422
    n378 --> n423
    n400 --> n423
    n340 --> n381
    n301 --> n319
    n182 --> n207
    n305 --> n320
    n305 --> n321
    n305 --> n322
    n307 --> n323
    n185 --> n237
    n169 --> n183
    n365 --> n403
    n423 --> n433
    n449 --> n452
    n448 --> n452
    n213 --> n263
    n441 --> n446
    n217 --> n264
    n438 --> n447
    n413 --> n434
    n338 --> n404
    n329 --> n404
    n342 --> n404
    n372 --> n404
    n288 --> n300
    n355 --> n382
    n272 --> n301
    n269 --> n301
    n431 --> n442
    n272 --> n302
    n269 --> n302
    n365 --> n405
    n440 --> n448
    n434 --> n448
    n296 --> n324
    n296 --> n325
    n356 --> n383
    n189 --> n238
    n431 --> n443
    n260 --> n303
    n285 --> n303
    n275 --> n303
    n237 --> n265
    n249 --> n287
    n391 --> n424
    n7 --> n170
    n288 --> n304
    n367 --> n406
    n246 --> n288
    n254 --> n288
    n297 --> n326
    n411 --> n435
    n414 --> n435
    n348 --> n384
    n339 --> n384
    n193 --> n239
    n272 --> n305
    n281 --> n306
    n369 --> n407
    n349 --> n385
    n360 --> n385
    n295 --> n327
    n193 --> n240
    n440 --> n449
    n430 --> n449
    n217 --> n266
    n208 --> n267
    n381 --> n408
    n371 --> n409
    n193 --> n241
    n229 --> n268
    n189 --> n242
    n322 --> n357
    n320 --> n358
    n281 --> n307
    n317 --> n359
    n321 --> n360
    n320 --> n361
    n321 --> n362
    n320 --> n363
    n35 --> n57
    n58 --> n78
    n37 --> n58
    n36 --> n59
    n57 --> n79
    n59 --> n80
    n78 --> n92
    n17 --> n35
    n17 --> n36
    n17 --> n37
    n7 --> n17
    n8 --> n17
    n42 --> n65
    n70 --> n85
    n21 --> n42
    n8 --> n20
    n7 --> n20
    n8 --> n21
    n7 --> n21
    n23 --> n43
    n85 --> n98
    n98 --> n106
    n100 --> n106
    n45 --> n66
    n20 --> n44
    n87 --> n99
    n67 --> n86
    n45 --> n67
    n22 --> n45
    n67 --> n87
    n66 --> n87
    n99 --> n107
    n43 --> n68
    n42 --> n68
    n107 --> n113
    n20 --> n46
    n8 --> n22
    n7 --> n22
    n43 --> n69
    n44 --> n70
    n46 --> n70
    n8 --> n23
    n7 --> n23
    n85 --> n100
    n24 --> n47
    n89 --> n101
    n103 --> n108
    n88 --> n102
    n71 --> n88
    n89 --> n103
    n88 --> n103
    n24 --> n48
    n48 --> n71
    n47 --> n71
    n71 --> n89
    n8 --> n24
    n7 --> n24
    n25 --> n49
    n72 --> n90
    n73 --> n90
    n25 --> n50
    n49 --> n72
    n8 --> n25
    n7 --> n25
    n104 --> n109
    n50 --> n73
    n90 --> n104
    n163 x--x n177
    n163 x--x n168
    n386 x--x n419
    n386 x--x n423
    n269 x--x n272
    n289 x--x n291
    n289 x--x n304
    n272 x--x n286
    n410 x--x n418
    n185 x--x n190
    n186 x--x n192
    n186 x--x n196
    n165 x--x n166
    n165 x--x n169
    n172 x--x n183
    n291 x--x n304
    n430 x--x n434
    n192 x--x n196
    n313 x--x n323
    n166 x--x n169
    n7 x--x n162
    n392 x--x n407
    n175 x--x n180
    n176 x--x n177
    n177 x--x n168
    n8 x--x n9
    n419 x--x n423
    n442 x--x n443
    n265 x--x n267
    n65 x--x n68
    n65 x--x n69
    n20 x--x n22
    n21 x--x n23
    n68 x--x n69
    n88 x--x n89
```

# KHM_call_for_aid

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n454(("KHM_call_for_aid"))
        n455["KHM_strike_the_governor"]
    end
    subgraph tier_1["Tier 1"]
        n456{"KHM_push_them_back"}
    end
    subgraph tier_2["Tier 2"]
        n457["KHM_our_position_remains"]
        n458["KHM_the_sinkiang_ma_clique"]
    end
    n456 --> n457
    n454 --> n456
    n455 --> n456
    n456 --> n458
    n454 x--x n455
    n457 x--x n458
```

# KHM_strike_the_governor

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n454["KHM_call_for_aid"]
        n455(("KHM_strike_the_governor"))
    end
    subgraph tier_1["Tier 1"]
        n456{"KHM_push_them_back"}
    end
    subgraph tier_2["Tier 2"]
        n457["KHM_our_position_remains"]
        n458["KHM_the_sinkiang_ma_clique"]
    end
    n456 --> n457
    n454 --> n456
    n455 --> n456
    n456 --> n458
    n454 x--x n455
    n457 x--x n458
```
