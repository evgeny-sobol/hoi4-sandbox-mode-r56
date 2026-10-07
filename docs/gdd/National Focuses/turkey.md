# TUR_hava_okulu

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["TUR_construct_the_cakmak_line"]
        n2(("TUR_hava_okulu"))
        n3["TUR_modernising_the_army"]
    end
    subgraph tier_1["Tier 1"]
        n4["TUR_expand_the_air_bases"]
    end
    subgraph tier_2["Tier 2"]
        n5{"TUR_accelerate_native_fighter_designs"}
        n6["TUR_expand_the_golcuk_naval_base"]
    end
    subgraph tier_3["Tier 3"]
        n7["TUR_invoke_the_methods_of_mehmed_ii"]
        n8["TUR_patrol_the_seas"]
        n9{"TUR_relocate_from_yildiz_palace"}
    end
    subgraph tier_4["Tier 4"]
        n10["TUR_the_legacy_of_osmanli_donanmasi"]
        n11["TUR_the_path_of_the_wolf"]
        n12["TUR_turkish_air_defense_platforms"]
    end
    subgraph tier_5["Tier 5"]
        n13["TUR_fortified_defensive_bases"]
    end
    subgraph tier_6["Tier 6"]
        n14["TUR_turk_silahli_kuvvetleri"]
    end
    n4 --> n5
    n2 --> n4
    n3 --> n6
    n4 --> n6
    n1 --> n13
    n10 --> n13
    n11 --> n13
    n12 --> n13
    n5 --> n7
    n5 --> n8
    n6 --> n9
    n9 --> n10
    n9 --> n11
    n13 --> n14
    n8 --> n12
    n7 --> n12
    n7 x--x n8
    n10 x--x n11
```

# TUR_learning_from_the_great_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n4["TUR_expand_the_air_bases"]
        n15(("TUR_learning_from_the_great_war"))
        n12["TUR_turkish_air_defense_platforms"]
    end
    subgraph tier_1["Tier 1"]
        n3{"TUR_modernising_the_army"}
    end
    subgraph tier_2["Tier 2"]
        n16["TUR_embrace_military_tradition"]
        n6["TUR_expand_the_golcuk_naval_base"]
        n17["TUR_mechanising_our_army"]
    end
    subgraph tier_3["Tier 3"]
        n9{"TUR_relocate_from_yildiz_palace"}
        n18["TUR_superiority_of_arms"]
        n19["TUR_the_kirikkale_tank"]
        n20["TUR_utilising_our_terrain"]
    end
    subgraph tier_4["Tier 4"]
        n1["TUR_construct_the_cakmak_line"]
        n10["TUR_the_legacy_of_osmanli_donanmasi"]
        n11["TUR_the_path_of_the_wolf"]
    end
    subgraph tier_5["Tier 5"]
        n13["TUR_fortified_defensive_bases"]
        n21["TUR_fortifying_the_bosporus"]
        n22["TUR_the_pontic_redoubt"]
    end
    subgraph tier_6["Tier 6"]
        n14["TUR_turk_silahli_kuvvetleri"]
    end
    n18 --> n1
    n3 --> n16
    n3 --> n6
    n4 --> n6
    n1 --> n13
    n10 --> n13
    n11 --> n13
    n12 --> n13
    n1 --> n21
    n3 --> n17
    n15 --> n3
    n6 --> n9
    n16 --> n18
    n17 --> n18
    n17 --> n19
    n9 --> n10
    n9 --> n11
    n1 --> n22
    n13 --> n14
    n16 --> n20
    n16 x--x n17
    n10 x--x n11
```

# TUR_one_party_many_faces

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n23{"TUR_one_party_many_faces"}
        n24{"TUR_solidify_the_seventh_inonu_government"}
    end
    subgraph tier_1["Tier 1"]
        n25{"TUR_continue_the_policy_of_etatism"}
        n26["TUR_fully_integrate_the_is_bank"]
        n27["TUR_ratify_the_six_arrows"]
    end
    subgraph tier_2["Tier 2"]
        n28["TUR_peace_at_home"]
        n29["TUR_privatize_the_anadolu_agency"]
        n30{"TUR_revive_turkish_revolutionism"}
        n31["TUR_the_montreux_convention"]
        n32["TUR_the_sanayiciler"]
        n33["TUR_turkish_state_railways"]
    end
    subgraph tier_3["Tier 3"]
        n34["TUR_assess_our_future"]
        n35["TUR_cooperate_with_the_debt_council"]
        n36["TUR_lift_the_ban_on_other_political_parties"]
        n37{"TUR_rehabilitate_the_kadro_movement"}
        n38["TUR_reinforce_state_arsenals"]
        n39{"TUR_reinvigorate_turkish_nationalism"}
        n40{"TUR_the_guardians_of_kemalism"}
        n41["TUR_the_hatay_issue"]
        n42["TUR_the_second_five_year_plan"]
        n43["TUR_treaty_of_saadabad"]
    end
    subgraph tier_4["Tier 4"]
        n44["TUR_abuse_the_office_of_soil_products"]
        n45["TUR_expand_the_university_education_network"]
        n46{"TUR_holding_our_first_multi_party_election"}
        n47["TUR_kemalism_and_the_modern_movement"]
        n48["TUR_kemalist_socialist_theory"]
        n49["TUR_loosen_the_laws_on_secularism"]
        n50["TUR_peace_in_the_world"]
        n51["TUR_permit_regional_elections"]
        n52["TUR_the_sun_language_theory"]
        n53["TUR_turk_ulusu"]
        n54["TUR_utilize_foreign_capital"]
        n55["TUR_variant_turkish_tax_focus"]
    end
    subgraph tier_5["Tier 5"]
        n56["TUR_a_common_destiny_for_all_of_turkey"]
        n57{"TUR_create_the_turkish_workers_militia"}
        n58["TUR_democratic_transition_focus"]
        n59["TUR_hunt_down_fifth_columnist_islamists"]
        n60["TUR_integrate_the_fascist_council"]
        n61["TUR_patriotism_over_internationalism"]
        n62["TUR_purify_the_diyanet"]
        n63["TUR_reconfigure_our_foreign_policy"]
        n64["TUR_traditionalize_the_ataturk_legacy"]
    end
    subgraph tier_6["Tier 6"]
        n65["TUR_a_city_of_spies"]
        n66["TUR_continue_to_prioritise_balkan_integrity"]
        n67["TUR_fatherland_first"]
        n68["TUR_halk_ve_devlet"]
        n69["TUR_lift_the_turkiye_komunist_partisis_exile"]
        n70["TUR_nationalise_all_private_industry"]
        n71{"TUR_pivot_to_the_past"}
        n72["TUR_privatize_our_infrastructure"]
        n73["TUR_provide_refuge_to_the_victims_of_fascism"]
        n74["TUR_renew_the_turkish_soviet_non_aggression_pact"]
        n75["TUR_restack_the_officer_corps"]
        n76["TUR_salt_the_scars_of_the_great_war"]
        n77{"TUR_the_anglo_turkish_agreement"}
        n78["TUR_the_chester_concession"]
        n79["TUR_the_german_turkish_friendship_treaty"]
        n80["TUR_the_italo_turkish_friendship_treaty"]
    end
    subgraph tier_7["Tier 7"]
        n81{"TUR_adana_to_baku_highway"}
        n82["TUR_american_motor_factories"]
        n83["TUR_applying_british_oil_embargoes_on_iraq"]
        n84["TUR_back_the_traditionalist_cause"]
        n85["TUR_bomber_schematics"]
        n86{"TUR_deal_for_the_oniki_islands"}
        n87["TUR_host_exiled_scientists"]
        n88{"TUR_invite_german_officers_to_izmir"}
        n89["TUR_purchase_italian_light_tanks"]
        n90["TUR_reaffirm_the_balkan_pact"]
        n91["TUR_rebuilding_our_nation"]
        n92["TUR_reconciling_kemalism_with_bolshevism"]
        n93["TUR_refining_our_strategies"]
        n94{"TUR_restore_the_divan"}
        n95["TUR_the_batumi_accord"]
        n96["TUR_the_clodius_agreement"]
    end
    subgraph tier_8["Tier 8"]
        n97{"TUR_approve_the_funkplan"}
        n98["TUR_balkan_defense_council"]
        n99["TUR_create_the_balkan_central_bank"]
        n100{"TUR_georgian_manganese_extraction"}
        n101{"TUR_reapproachment_with_the_west"}
        n102["TUR_reclaiming_our_lost_empire"]
        n103["TUR_reinstate_the_darulfununu_sahane"]
        n104["TUR_return_of_the_sultan"]
        n105{"TUR_the_italo_turkish_naval_academy"}
        n106["TUR_the_petra_proposal"]
        n107["TUR_the_true_muslim_unity"]
        n108["TUR_three_year_industrial_plan"]
    end
    subgraph tier_9["Tier 9"]
        n109["TUR_black_sea_swindle"]
        n110["TUR_imperial_factories"]
        n111["TUR_institutional_reorganization"]
        n112["TUR_join_the_allies"]
        n113["TUR_join_the_axis"]
        n114["TUR_join_the_central_powers"]
        n115["TUR_joint_budgets_on_fortifications"]
        n116["TUR_purge_the_kemalists"]
        n117["TUR_readdress_the_montreux_convention"]
        n118["TUR_reaffirm_balkan_hegemony"]
        n119["TUR_the_damascus_diktat"]
        n120["TUR_the_mediterranean_entente"]
        n121["TUR_the_pan_national_association_of_ulemas"]
        n122["TUR_the_red_apples_of_sevres"]
        n123["TUR_the_treaty_for_prosperity_and_trade"]
    end
    subgraph tier_10["Tier 10"]
        n124["TUR_aligning_bulgaria"]
        n125["TUR_british_dockyards_in_turkey"]
        n126["TUR_collaborative_civil_works_programme"]
        n127["TUR_connecting_our_capitals"]
        n128["TUR_dissolve_the_ODPA"]
        n129["TUR_establish_the_committee_of_pan_turkism"]
        n130["TUR_expanded_credit_on_our_debts"]
        n131["TUR_fate_of_greece"]
        n132["TUR_fortifying_contentious_areas"]
        n133["TUR_increase_german_military_aid"]
        n134{"TUR_integrated_armed_forces"}
        n135["TUR_joint_caucasian_turkish_officer_school"]
        n136["TUR_learning_from_the_tripolitanian_war"]
        n137["TUR_pack_for_a_long_winter"]
        n138["TUR_partnership_pact_with_bulgaria"]
        n139["TUR_peninsular_network_of_factories"]
        n140["TUR_realize_the_nightmare_of_meiji"]
        n141["TUR_reclaim_macedonia"]
        n142["TUR_revert_mesopotamian_campaign"]
        n143["TUR_strengthening_our_navies"]
        n144["TUR_supporting_the_east"]
        n145["TUR_the_international_of_proletarian_freethinkers"]
        n146["TUR_the_tuz_golu_training_facility"]
    end
    subgraph tier_11["Tier 11"]
        n147["TUR_avenge_the_treaty_of_sevres"]
        n148["TUR_capitalise_on_rising_kurdish_nationalism"]
        n149["TUR_cooperative_research_centers"]
        n150["TUR_expanding_our_navy"]
        n151["TUR_extend_an_olive_branch_to_bulgaria"]
        n152["TUR_integrate_german_officers_into_the_army"]
        n153["TUR_mediterranean_merchant_fleet"]
        n154["TUR_officers_of_the_revolution"]
        n155["TUR_preempt_bulgarian_alignment"]
        n156["TUR_preempt_ideological_threat"]
        n157["TUR_rebuke_the_treaty_of_lausanne"]
        n158["TUR_restore_suleinmans_heritage"]
        n159["TUR_scrapping_our_debts"]
        n160["TUR_secure_the_iraqi_oil"]
        n161["TUR_seize_the_peninsula"]
        n162["TUR_solidify_the_iberian_flank"]
        n163["TUR_the_balkan_academy_of_science"]
    end
    subgraph tier_12["Tier 12"]
        n164["TUR_combined_operational_strategies"]
        n165["TUR_edirne_research_exchange"]
        n166["TUR_engulf_the_akdeniz"]
        n167["TUR_region_security_initiative"]
    end
    subgraph tier_13["Tier 13"]
        n168["TUR_brace_against_the_red_menace"]
        n169["TUR_crush_the_warmongers_in_rome"]
        n170["TUR_push_for_the_forceful_militarization"]
        n171["TUR_securing_iran"]
        n172["TUR_seizing_the_romanian_oil_fields"]
        n173["TUR_taking_over_defense_of_the_gulf"]
    end
    subgraph tier_14["Tier 14"]
        n174["TUR_restoring_our_nations_pride"]
    end
    subgraph tier_15["Tier 15"]
        n175["TUR_misak_i_milli"]
    end
    subgraph tier_16["Tier 16"]
        n176{"TUR_annul_the_ankara_anlasmasi"}
        n177{"TUR_rebuke_the_treaty_of_kars"}
        n178["TUR_recover_the_kardzhali_vilayet"]
    end
    subgraph tier_17["Tier 17"]
        n179["TUR_cypriot_and_oniki_ilhak"]
        n180["TUR_konfederasyon"]
        n181["TUR_liberate_the_kurdish_diaspora"]
        n182["TUR_reuniting_thrace_through_force"]
        n183["TUR_unite_the_azeri_diaspora"]
    end
    subgraph tier_18["Tier 18"]
        n184["TUR_turanist_ambition"]
    end
    subgraph tier_19["Tier 19"]
        n185["TUR_cin_turkleri"]
        n186["TUR_crowning_ourselves_with_the_fin_ugor"]
        n187["TUR_subdue_the_magyars"]
    end
    n63 --> n65
    n47 --> n56
    n48 --> n56
    n40 --> n44
    n74 --> n81
    n118 --> n124
    n78 --> n82
    n175 --> n176
    n77 --> n83
    n96 --> n97
    n31 --> n34
    n143 --> n147
    n136 --> n147
    n71 --> n84
    n90 --> n98
    n102 --> n109
    n78 --> n85
    n77 --> n85
    n164 --> n168
    n165 --> n168
    n112 --> n125
    n143 --> n148
    n136 --> n148
    n184 --> n185
    n120 --> n126
    n151 --> n164
    n155 --> n164
    n99 --> n127
    n123 --> n127
    n24 --> n25
    n23 --> n25
    n63 --> n66
    n32 --> n35
    n126 --> n149
    n133 --> n149
    n90 --> n99
    n48 --> n57
    n184 --> n186
    n164 --> n169
    n165 --> n169
    n178 --> n179
    n80 --> n86
    n46 --> n58
    n117 --> n128
    n113 --> n128
    n163 --> n165
    n151 --> n165
    n155 --> n165
    n162 --> n166
    n153 --> n166
    n113 --> n129
    n35 --> n45
    n112 --> n130
    n125 --> n150
    n134 --> n151
    n120 --> n131
    n62 --> n67
    n60 --> n67
    n115 --> n132
    n23 --> n26
    n95 --> n100
    n57 --> n68
    n36 --> n46
    n73 --> n87
    n55 --> n59
    n104 --> n110
    n113 --> n133
    n104 --> n111
    n133 --> n152
    n47 --> n60
    n115 --> n134
    n99 --> n134
    n79 --> n88
    n77 --> n112
    n101 --> n112
    n88 --> n113
    n97 --> n113
    n102 --> n114
    n99 --> n115
    n98 --> n115
    n117 --> n135
    n39 --> n47
    n37 --> n47
    n37 --> n48
    n177 --> n180
    n117 --> n136
    n176 --> n181
    n29 --> n36
    n57 --> n69
    n40 --> n49
    n39 --> n49
    n126 --> n153
    n174 --> n175
    n57 --> n70
    n135 --> n154
    n113 --> n137
    n112 --> n138
    n120 --> n138
    n48 --> n61
    n25 --> n28
    n34 --> n50
    n123 --> n139
    n36 --> n51
    n64 --> n71
    n134 --> n155
    n137 --> n156
    n58 --> n72
    n26 --> n29
    n63 --> n73
    n80 --> n89
    n104 --> n116
    n49 --> n62
    n167 --> n170
    n23 --> n27
    n81 --> n117
    n100 --> n117
    n102 --> n118
    n66 --> n90
    n122 --> n140
    n94 --> n101
    n71 --> n91
    n175 --> n177
    n146 --> n157
    n137 --> n157
    n118 --> n141
    n94 --> n102
    n68 --> n92
    n69 --> n92
    n50 --> n63
    n175 --> n178
    n71 --> n93
    n150 --> n167
    n130 --> n167
    n30 --> n37
    n32 --> n38
    n94 --> n103
    n84 --> n103
    n30 --> n39
    n63 --> n74
    n62 --> n75
    n60 --> n75
    n141 --> n158
    n124 --> n158
    n71 --> n94
    n170 --> n174
    n166 --> n174
    n157 --> n174
    n147 --> n174
    n164 --> n174
    n94 --> n104
    n84 --> n104
    n178 --> n182
    n119 --> n142
    n25 --> n30
    n24 --> n30
    n56 --> n76
    n128 --> n159
    n146 --> n160
    n167 --> n171
    n142 --> n161
    n167 --> n172
    n131 --> n162
    n117 --> n143
    n184 --> n187
    n119 --> n144
    n109 --> n144
    n167 --> n173
    n58 --> n77
    n63 --> n77
    n123 --> n163
    n127 --> n163
    n74 --> n95
    n58 --> n78
    n63 --> n78
    n79 --> n96
    n102 --> n119
    n63 --> n79
    n28 --> n40
    n31 --> n41
    n117 --> n145
    n63 --> n80
    n89 --> n105
    n105 --> n120
    n86 --> n120
    n26 --> n31
    n25 --> n31
    n107 --> n121
    n83 --> n106
    n102 --> n122
    n26 --> n32
    n25 --> n32
    n33 --> n42
    n39 --> n52
    n108 --> n123
    n84 --> n107
    n113 --> n146
    n90 --> n108
    n46 --> n64
    n31 --> n43
    n179 --> n184
    n182 --> n184
    n180 --> n184
    n183 --> n184
    n181 --> n184
    n40 --> n53
    n41 --> n53
    n26 --> n33
    n25 --> n33
    n177 --> n183
    n35 --> n54
    n40 --> n55
    n39 --> n55
    n84 x--x n94
    n25 x--x n26
    n58 x--x n64
    n151 x--x n155
    n68 x--x n69
    n112 x--x n113
    n112 x--x n117
    n112 x--x n120
    n113 x--x n117
    n113 x--x n120
    n47 x--x n48
    n180 x--x n183
    n181 x--x n183
    n49 x--x n55
    n28 x--x n30
    n117 x--x n120
    n101 x--x n102
    n37 x--x n39
```

# TUR_solidify_the_seventh_inonu_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n58["TUR_democratic_transition_focus"]
        n26["TUR_fully_integrate_the_is_bank"]
        n23{"TUR_one_party_many_faces"}
        n101{"TUR_reapproachment_with_the_west"}
        n24{"TUR_solidify_the_seventh_inonu_government"}
    end
    subgraph tier_1["Tier 1"]
        n25{"TUR_continue_the_policy_of_etatism"}
    end
    subgraph tier_2["Tier 2"]
        n28["TUR_peace_at_home"]
        n30{"TUR_revive_turkish_revolutionism"}
        n31["TUR_the_montreux_convention"]
        n32["TUR_the_sanayiciler"]
        n33["TUR_turkish_state_railways"]
    end
    subgraph tier_3["Tier 3"]
        n34["TUR_assess_our_future"]
        n35["TUR_cooperate_with_the_debt_council"]
        n37{"TUR_rehabilitate_the_kadro_movement"}
        n38["TUR_reinforce_state_arsenals"]
        n39{"TUR_reinvigorate_turkish_nationalism"}
        n40{"TUR_the_guardians_of_kemalism"}
        n41["TUR_the_hatay_issue"]
        n42["TUR_the_second_five_year_plan"]
        n43["TUR_treaty_of_saadabad"]
    end
    subgraph tier_4["Tier 4"]
        n44["TUR_abuse_the_office_of_soil_products"]
        n45["TUR_expand_the_university_education_network"]
        n47["TUR_kemalism_and_the_modern_movement"]
        n48["TUR_kemalist_socialist_theory"]
        n49["TUR_loosen_the_laws_on_secularism"]
        n50["TUR_peace_in_the_world"]
        n52["TUR_the_sun_language_theory"]
        n53["TUR_turk_ulusu"]
        n54["TUR_utilize_foreign_capital"]
        n55["TUR_variant_turkish_tax_focus"]
    end
    subgraph tier_5["Tier 5"]
        n56["TUR_a_common_destiny_for_all_of_turkey"]
        n57{"TUR_create_the_turkish_workers_militia"}
        n59["TUR_hunt_down_fifth_columnist_islamists"]
        n60["TUR_integrate_the_fascist_council"]
        n61["TUR_patriotism_over_internationalism"]
        n62["TUR_purify_the_diyanet"]
        n63["TUR_reconfigure_our_foreign_policy"]
    end
    subgraph tier_6["Tier 6"]
        n65["TUR_a_city_of_spies"]
        n66["TUR_continue_to_prioritise_balkan_integrity"]
        n67["TUR_fatherland_first"]
        n68["TUR_halk_ve_devlet"]
        n69["TUR_lift_the_turkiye_komunist_partisis_exile"]
        n70["TUR_nationalise_all_private_industry"]
        n73["TUR_provide_refuge_to_the_victims_of_fascism"]
        n74["TUR_renew_the_turkish_soviet_non_aggression_pact"]
        n75["TUR_restack_the_officer_corps"]
        n76["TUR_salt_the_scars_of_the_great_war"]
        n77{"TUR_the_anglo_turkish_agreement"}
        n78["TUR_the_chester_concession"]
        n79["TUR_the_german_turkish_friendship_treaty"]
        n80["TUR_the_italo_turkish_friendship_treaty"]
    end
    subgraph tier_7["Tier 7"]
        n81{"TUR_adana_to_baku_highway"}
        n82["TUR_american_motor_factories"]
        n83["TUR_applying_british_oil_embargoes_on_iraq"]
        n85["TUR_bomber_schematics"]
        n86{"TUR_deal_for_the_oniki_islands"}
        n87["TUR_host_exiled_scientists"]
        n88{"TUR_invite_german_officers_to_izmir"}
        n112["TUR_join_the_allies"]
        n89["TUR_purchase_italian_light_tanks"]
        n90["TUR_reaffirm_the_balkan_pact"]
        n92["TUR_reconciling_kemalism_with_bolshevism"]
        n95["TUR_the_batumi_accord"]
        n96["TUR_the_clodius_agreement"]
    end
    subgraph tier_8["Tier 8"]
        n97{"TUR_approve_the_funkplan"}
        n98["TUR_balkan_defense_council"]
        n125["TUR_british_dockyards_in_turkey"]
        n99["TUR_create_the_balkan_central_bank"]
        n130["TUR_expanded_credit_on_our_debts"]
        n100{"TUR_georgian_manganese_extraction"}
        n105{"TUR_the_italo_turkish_naval_academy"}
        n106["TUR_the_petra_proposal"]
        n108["TUR_three_year_industrial_plan"]
    end
    subgraph tier_9["Tier 9"]
        n150["TUR_expanding_our_navy"]
        n113["TUR_join_the_axis"]
        n115["TUR_joint_budgets_on_fortifications"]
        n117["TUR_readdress_the_montreux_convention"]
        n120["TUR_the_mediterranean_entente"]
        n123["TUR_the_treaty_for_prosperity_and_trade"]
    end
    subgraph tier_10["Tier 10"]
        n126["TUR_collaborative_civil_works_programme"]
        n127["TUR_connecting_our_capitals"]
        n128["TUR_dissolve_the_ODPA"]
        n129["TUR_establish_the_committee_of_pan_turkism"]
        n131["TUR_fate_of_greece"]
        n132["TUR_fortifying_contentious_areas"]
        n133["TUR_increase_german_military_aid"]
        n134{"TUR_integrated_armed_forces"}
        n135["TUR_joint_caucasian_turkish_officer_school"]
        n136["TUR_learning_from_the_tripolitanian_war"]
        n137["TUR_pack_for_a_long_winter"]
        n138["TUR_partnership_pact_with_bulgaria"]
        n139["TUR_peninsular_network_of_factories"]
        n167["TUR_region_security_initiative"]
        n143["TUR_strengthening_our_navies"]
        n145["TUR_the_international_of_proletarian_freethinkers"]
        n146["TUR_the_tuz_golu_training_facility"]
    end
    subgraph tier_11["Tier 11"]
        n147["TUR_avenge_the_treaty_of_sevres"]
        n148["TUR_capitalise_on_rising_kurdish_nationalism"]
        n149["TUR_cooperative_research_centers"]
        n151["TUR_extend_an_olive_branch_to_bulgaria"]
        n152["TUR_integrate_german_officers_into_the_army"]
        n153["TUR_mediterranean_merchant_fleet"]
        n154["TUR_officers_of_the_revolution"]
        n155["TUR_preempt_bulgarian_alignment"]
        n156["TUR_preempt_ideological_threat"]
        n170["TUR_push_for_the_forceful_militarization"]
        n157["TUR_rebuke_the_treaty_of_lausanne"]
        n159["TUR_scrapping_our_debts"]
        n160["TUR_secure_the_iraqi_oil"]
        n171["TUR_securing_iran"]
        n172["TUR_seizing_the_romanian_oil_fields"]
        n162["TUR_solidify_the_iberian_flank"]
        n173["TUR_taking_over_defense_of_the_gulf"]
        n163["TUR_the_balkan_academy_of_science"]
    end
    subgraph tier_12["Tier 12"]
        n164["TUR_combined_operational_strategies"]
        n165["TUR_edirne_research_exchange"]
        n166["TUR_engulf_the_akdeniz"]
    end
    subgraph tier_13["Tier 13"]
        n168["TUR_brace_against_the_red_menace"]
        n169["TUR_crush_the_warmongers_in_rome"]
        n174["TUR_restoring_our_nations_pride"]
    end
    subgraph tier_14["Tier 14"]
        n175["TUR_misak_i_milli"]
    end
    subgraph tier_15["Tier 15"]
        n176{"TUR_annul_the_ankara_anlasmasi"}
        n177{"TUR_rebuke_the_treaty_of_kars"}
        n178["TUR_recover_the_kardzhali_vilayet"]
    end
    subgraph tier_16["Tier 16"]
        n179["TUR_cypriot_and_oniki_ilhak"]
        n180["TUR_konfederasyon"]
        n181["TUR_liberate_the_kurdish_diaspora"]
        n182["TUR_reuniting_thrace_through_force"]
        n183["TUR_unite_the_azeri_diaspora"]
    end
    subgraph tier_17["Tier 17"]
        n184["TUR_turanist_ambition"]
    end
    subgraph tier_18["Tier 18"]
        n185["TUR_cin_turkleri"]
        n186["TUR_crowning_ourselves_with_the_fin_ugor"]
        n187["TUR_subdue_the_magyars"]
    end
    n63 --> n65
    n47 --> n56
    n48 --> n56
    n40 --> n44
    n74 --> n81
    n78 --> n82
    n175 --> n176
    n77 --> n83
    n96 --> n97
    n31 --> n34
    n143 --> n147
    n136 --> n147
    n90 --> n98
    n78 --> n85
    n77 --> n85
    n164 --> n168
    n165 --> n168
    n112 --> n125
    n143 --> n148
    n136 --> n148
    n184 --> n185
    n120 --> n126
    n151 --> n164
    n155 --> n164
    n99 --> n127
    n123 --> n127
    n24 --> n25
    n23 --> n25
    n63 --> n66
    n32 --> n35
    n126 --> n149
    n133 --> n149
    n90 --> n99
    n48 --> n57
    n184 --> n186
    n164 --> n169
    n165 --> n169
    n178 --> n179
    n80 --> n86
    n117 --> n128
    n113 --> n128
    n163 --> n165
    n151 --> n165
    n155 --> n165
    n162 --> n166
    n153 --> n166
    n113 --> n129
    n35 --> n45
    n112 --> n130
    n125 --> n150
    n134 --> n151
    n120 --> n131
    n62 --> n67
    n60 --> n67
    n115 --> n132
    n95 --> n100
    n57 --> n68
    n73 --> n87
    n55 --> n59
    n113 --> n133
    n133 --> n152
    n47 --> n60
    n115 --> n134
    n99 --> n134
    n79 --> n88
    n77 --> n112
    n101 --> n112
    n88 --> n113
    n97 --> n113
    n99 --> n115
    n98 --> n115
    n117 --> n135
    n39 --> n47
    n37 --> n47
    n37 --> n48
    n177 --> n180
    n117 --> n136
    n176 --> n181
    n57 --> n69
    n40 --> n49
    n39 --> n49
    n126 --> n153
    n174 --> n175
    n57 --> n70
    n135 --> n154
    n113 --> n137
    n112 --> n138
    n120 --> n138
    n48 --> n61
    n25 --> n28
    n34 --> n50
    n123 --> n139
    n134 --> n155
    n137 --> n156
    n63 --> n73
    n80 --> n89
    n49 --> n62
    n167 --> n170
    n81 --> n117
    n100 --> n117
    n66 --> n90
    n175 --> n177
    n146 --> n157
    n137 --> n157
    n68 --> n92
    n69 --> n92
    n50 --> n63
    n175 --> n178
    n150 --> n167
    n130 --> n167
    n30 --> n37
    n32 --> n38
    n30 --> n39
    n63 --> n74
    n62 --> n75
    n60 --> n75
    n170 --> n174
    n166 --> n174
    n157 --> n174
    n147 --> n174
    n164 --> n174
    n178 --> n182
    n25 --> n30
    n24 --> n30
    n56 --> n76
    n128 --> n159
    n146 --> n160
    n167 --> n171
    n167 --> n172
    n131 --> n162
    n117 --> n143
    n184 --> n187
    n167 --> n173
    n58 --> n77
    n63 --> n77
    n123 --> n163
    n127 --> n163
    n74 --> n95
    n58 --> n78
    n63 --> n78
    n79 --> n96
    n63 --> n79
    n28 --> n40
    n31 --> n41
    n117 --> n145
    n63 --> n80
    n89 --> n105
    n105 --> n120
    n86 --> n120
    n26 --> n31
    n25 --> n31
    n83 --> n106
    n26 --> n32
    n25 --> n32
    n33 --> n42
    n39 --> n52
    n108 --> n123
    n113 --> n146
    n90 --> n108
    n31 --> n43
    n179 --> n184
    n182 --> n184
    n180 --> n184
    n183 --> n184
    n181 --> n184
    n40 --> n53
    n41 --> n53
    n26 --> n33
    n25 --> n33
    n177 --> n183
    n35 --> n54
    n40 --> n55
    n39 --> n55
    n25 x--x n26
    n151 x--x n155
    n68 x--x n69
    n112 x--x n113
    n112 x--x n117
    n112 x--x n120
    n113 x--x n117
    n113 x--x n120
    n47 x--x n48
    n180 x--x n183
    n181 x--x n183
    n49 x--x n55
    n28 x--x n30
    n117 x--x n120
    n37 x--x n39
```
