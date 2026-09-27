# EGY_a_humiliation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"EGY_a_humiliation"}
    end
    subgraph tier_1["Tier 1"]
        n2["EGY_stretch_out_the_hand"]
        n3["EGY_three_nos"]
    end
    n1 --> n2
    n1 --> n3
    n2 x--x n3
```

# EGY_banha_industrial_sectors

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n4(("EGY_banha_industrial_sectors"))
        n5["EGY_construct_khartoum_juba_link"]
        n6["EGY_development_in_sudan"]
    end
    subgraph tier_1["Tier 1"]
        n7["EGY_banque_misr"]
        n8["EGY_ministry_of_resources"]
        n9["EGY_promote_agricultural_development"]
    end
    subgraph tier_2["Tier 2"]
        n10["EGY_develop_the_east"]
        n11["EGY_expand_the_aswan_hydroelectric_facility"]
        n12["EGY_misr_for_trade_and_oil"]
    end
    subgraph tier_3["Tier 3"]
        n13["EGY_expand_jonglei_aluminum"]
        n14["EGY_national_defence_funds"]
    end
    subgraph tier_4["Tier 4"]
        n15["EGY_military_build"]
        n16["EGY_rural_education_plan"]
    end
    n4 --> n7
    n7 --> n10
    n5 --> n13
    n12 --> n13
    n7 --> n11
    n14 --> n15
    n6 --> n8
    n4 --> n8
    n8 --> n12
    n11 --> n14
    n10 --> n14
    n4 --> n9
    n14 --> n16
```

# EGY_development_in_sudan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n4["EGY_banha_industrial_sectors"]
        n6(("EGY_development_in_sudan"))
    end
    subgraph tier_1["Tier 1"]
        n5["EGY_construct_khartoum_juba_link"]
        n8["EGY_ministry_of_resources"]
    end
    subgraph tier_2["Tier 2"]
        n12["EGY_misr_for_trade_and_oil"]
    end
    subgraph tier_3["Tier 3"]
        n13["EGY_expand_jonglei_aluminum"]
    end
    n6 --> n5
    n5 --> n13
    n12 --> n13
    n6 --> n8
    n4 --> n8
    n8 --> n12
```

# EGY_egyptian_military_academy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17["EGY_defence_of_cairo"]
        n18{"EGY_egyptian_military_academy"}
    end
    subgraph tier_1["Tier 1"]
        n19["EGY_continue_army_segregation"]
        n20["EGY_sudanese_volunteers"]
    end
    subgraph tier_2["Tier 2"]
        n21["EGY_modernize_our_weaponry"]
    end
    subgraph tier_3["Tier 3"]
        n22["EGY_air_defenses"]
        n23["EGY_field_piece_research"]
        n24["EGY_logistical_brigades"]
        n25["EGY_radio_technologies"]
    end
    subgraph tier_4["Tier 4"]
        n26["EGY_central_intelligence"]
        n27["EGY_continue_motorization_of_the_army"]
        n28["EGY_desert_camouflage"]
        n29["EGY_new_military_institute"]
    end
    subgraph tier_5["Tier 5"]
        n30["EGY_decryption_department"]
        n31["EGY_develop_egyptian_armour"]
        n32["EGY_unit_777"]
    end
    subgraph tier_6["Tier 6"]
        n33["EGY_study_nuclear_power"]
    end
    n17 --> n22
    n21 --> n22
    n25 --> n26
    n18 --> n19
    n24 --> n27
    n25 --> n27
    n26 --> n30
    n24 --> n28
    n27 --> n31
    n21 --> n23
    n21 --> n24
    n19 --> n21
    n20 --> n21
    n25 --> n29
    n21 --> n25
    n32 --> n33
    n18 --> n20
    n28 --> n32
    n27 --> n32
    n19 x--x n20
```

# EGY_expand_the_defence_department

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n34(("EGY_expand_the_defence_department"))
        n21["EGY_modernize_our_weaponry"]
    end
    subgraph tier_1["Tier 1"]
        n35["EGY_fortify_sudan"]
        n36["EGY_reinforce_the_north"]
        n37["EGY_the_eastern_frontier"]
    end
    subgraph tier_2["Tier 2"]
        n17["EGY_defence_of_cairo"]
    end
    subgraph tier_3["Tier 3"]
        n22["EGY_air_defenses"]
        n38["EGY_organize_the_egyptian_resistance"]
    end
    subgraph tier_4["Tier 4"]
        n39["EGY_evacuate_industrial_reserves"]
        n40["EGY_the_army_in_exile"]
    end
    subgraph tier_5["Tier 5"]
        n41["EGY_exile_naval_forces"]
        n42["EGY_exiles_in_the_air"]
    end
    n17 --> n22
    n21 --> n22
    n36 --> n17
    n35 --> n17
    n37 --> n17
    n38 --> n39
    n40 --> n41
    n39 --> n41
    n40 --> n42
    n34 --> n35
    n17 --> n38
    n34 --> n36
    n38 --> n40
    n34 --> n37
```

# EGY_expand_the_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n43(("EGY_expand_the_navy"))
        n44["EGY_royal_egyptian_airforce"]
    end
    subgraph tier_1["Tier 1"]
        n45["EGY_el_saka_forces"]
        n46["EGY_expand_alexandria_shipping"]
        n47{"EGY_hunt_class_destroyers"}
        n48{"EGY_replace_miniscule_vessels"}
    end
    subgraph tier_2["Tier 2"]
        n49["EGY_amphibious_exercises"]
        n50["EGY_big_farouq"]
        n51["EGY_carrier_development"]
        n52["EGY_develop_port_sudan"]
        n53["EGY_solve_the_canal_issue"]
        n54["EGY_the_suez_alternative"]
    end
    subgraph tier_3["Tier 3"]
        n55["EGY_militarize_the_canal_zone"]
        n56["EGY_naval_attrition"]
    end
    subgraph tier_4["Tier 4"]
        n57["EGY_navy_of_the_two_banks"]
    end
    subgraph tier_5["Tier 5"]
        n58["EGY_supremacy_over_the_mediterranean"]
    end
    n45 --> n49
    n47 --> n50
    n48 --> n50
    n47 --> n51
    n48 --> n51
    n46 --> n52
    n43 --> n45
    n43 --> n46
    n43 --> n47
    n53 --> n55
    n50 --> n56
    n51 --> n56
    n56 --> n57
    n54 --> n57
    n43 --> n48
    n46 --> n53
    n44 --> n53
    n57 --> n58
    n46 --> n54
    n50 x--x n51
```

# EGY_reestablish_control_of_the_EAAF

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46["EGY_expand_alexandria_shipping"]
        n59(("EGY_reestablish_control_of_the_EAAF"))
    end
    subgraph tier_1["Tier 1"]
        n60["EGY_abu_suweir_air_base"]
        n61["EGY_victor_taits_legacy"]
    end
    subgraph tier_2["Tier 2"]
        n62["EGY_purchase_audax_fighters"]
        n44["EGY_royal_egyptian_airforce"]
    end
    subgraph tier_3["Tier 3"]
        n63["EGY_al_zafir_kahi_missles"]
        n64["EGY_bomber_production"]
        n65["EGY_radar_defence_technologies"]
        n53["EGY_solve_the_canal_issue"]
    end
    subgraph tier_4["Tier 4"]
        n55["EGY_militarize_the_canal_zone"]
    end
    n59 --> n60
    n44 --> n63
    n44 --> n64
    n53 --> n55
    n61 --> n62
    n44 --> n65
    n60 --> n44
    n61 --> n44
    n46 --> n53
    n44 --> n53
    n59 --> n61
```

# EGY_revolt_against_the_opressors

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n66(("EGY_revolt_against_the_opressors"))
        n67["EGY_sever_the_ties"]
        n68["EGY_solidify_british_ties"]
    end
    subgraph tier_1["Tier 1"]
        n69["EGY_exploit_sudanese_separatism"]
        n70["EGY_rally_the_green_shirts"]
        n71["EGY_reach_out_to_germany"]
    end
    subgraph tier_2["Tier 2"]
        n72["EGY_strengthen_the_brotherhood"]
    end
    subgraph tier_3["Tier 3"]
        n73["EGY_dismantle_the_aristocracy"]
        n74["EGY_integrate_the_green_shirts"]
    end
    subgraph tier_4["Tier 4"]
        n75["EGY_crush_the_israeli_state2"]
        n76["EGY_islamic_fiscal_theory"]
        n77["EGY_islamic_militarism"]
    end
    subgraph tier_5["Tier 5"]
        n78["EGY_an_agrarian_society"]
        n79["EGY_disband_sudanese_partisans"]
        n80["EGY_guns_for_the_people"]
        n81["EGY_national_healthcare"]
    end
    subgraph tier_6["Tier 6"]
        n82["EGY_encourage_islamic_immigration"]
    end
    subgraph tier_7["Tier 7"]
        n83["EGY_education_for_the_poor"]
        n84{"EGY_nationalisation_of_industries"}
    end
    subgraph tier_8["Tier 8"]
        n85["EGY_formalise_the_german_alliance"]
        n86["EGY_masters_of_the_arab_world"]
    end
    subgraph tier_9["Tier 9"]
        n87["EGY_expand_the_sabotage_division"]
        n88["EGY_german_military_assistance"]
        n89["EGY_german_military_mission"]
        n90{"EGY_religious_nationalism"}
        n91["EGY_securing_control_of_africa"]
    end
    subgraph tier_10["Tier 10"]
        n92["EGY_alliance_with_saud"]
        n93["EGY_egyptian_panzers"]
        n94["EGY_reclaim_the_holy_sites"]
        n95["EGY_war_with_britain"]
    end
    subgraph tier_11["Tier 11"]
        n96["EGY_anti_imperialist_uniformity"]
        n97["EGY_secure_the_levant"]
        n98["EGY_support_the_iraqi_golden_square"]
    end
    subgraph tier_12["Tier 12"]
        n99{"EGY_demand_libyan_control"}
        n100{"EGY_invite_iran"}
        n101{"EGY_invite_iraq"}
    end
    subgraph tier_13["Tier 13"]
        n102{"EGY_reconcile_with_turkey"}
        n103{"EGY_secure_the_bosporus"}
    end
    subgraph tier_14["Tier 14"]
        n104["EGY_alliance_with_greece"]
        n105["EGY_secure_the_hellenic_mandate"]
    end
    subgraph tier_15["Tier 15"]
        n106["EGY_topple_the_oppressive_empire"]
    end
    n103 --> n104
    n102 --> n104
    n90 --> n92
    n77 --> n78
    n92 --> n96
    n74 --> n75
    n98 --> n99
    n97 --> n99
    n76 --> n79
    n72 --> n73
    n81 --> n83
    n82 --> n83
    n88 --> n93
    n89 --> n93
    n80 --> n82
    n78 --> n82
    n85 --> n87
    n86 --> n87
    n66 --> n69
    n84 --> n85
    n85 --> n88
    n85 --> n89
    n77 --> n80
    n72 --> n74
    n96 --> n100
    n96 --> n101
    n73 --> n76
    n73 --> n77
    n74 --> n77
    n84 --> n86
    n76 --> n81
    n82 --> n84
    n81 --> n84
    n66 --> n70
    n66 --> n71
    n90 --> n94
    n99 --> n102
    n101 --> n102
    n100 --> n102
    n86 --> n90
    n99 --> n103
    n101 --> n103
    n100 --> n103
    n103 --> n105
    n102 --> n105
    n94 --> n97
    n85 --> n91
    n70 --> n72
    n94 --> n98
    n104 --> n106
    n105 --> n106
    n91 --> n95
    n104 x--x n105
    n92 x--x n94
    n85 x--x n86
    n102 x--x n103
    n66 x--x n67
    n66 x--x n68
```

# EGY_sever_the_ties

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n66["EGY_revolt_against_the_opressors"]
        n67{"EGY_sever_the_ties"}
        n68["EGY_solidify_british_ties"]
    end
    subgraph tier_1["Tier 1"]
        n107{"EGY_emphasise_the_need_for_reform"}
        n108["EGY_end_the_regency"]
        n109["EGY_restore_the_khedive"]
    end
    subgraph tier_2["Tier 2"]
        n110["EGY_expand_royal_land_rights"]
        n111["EGY_isolation_and_surveillance"]
        n112["EGY_mansoura_agreement"]
        n113["EGY_mobilize_the_fellahs"]
        n114["EGY_strengthen_farouks_rule"]
        n115["EGY_the_free_officers_movement"]
        n116["EGY_the_king_of_sudan"]
    end
    subgraph tier_3["Tier 3"]
        n117["EGY_academic_sciences"]
        n118["EGY_invite_german_advisors"]
        n119["EGY_liberalization_of_trade_policies"]
        n120["EGY_ministry_of_awqaf"]
        n121{"EGY_modernize_al_azhar"}
        n122{"EGY_move_back_to_the_ottomans"}
        n123["EGY_nationalize_the_blue_shirts"]
        n124["EGY_pre_empt_the_ethiopian_threat"]
        n125["EGY_restore_the_1930_constitution"]
        n126["EGY_the_kings_fleet"]
        n127["EGY_voice_of_the_arabs"]
    end
    subgraph tier_4["Tier 4"]
        n128["EGY_dissolve_parliament"]
        n129["EGY_fund_algerian_independence"]
        n130["EGY_intervene_in_the_turkish_civil_war"]
        n131["EGY_invite_foreign_investors"]
        n132["EGY_lift_restrictions_on_political_parties"]
        n133["EGY_national_education"]
        n134["EGY_permit_regional_elections"]
        n135["EGY_publicize_the_universities"]
        n136["EGY_rightful_successor_to_the_empire"]
        n137["EGY_support_the_palestinian_liberation_movement"]
        n138{"EGY_unify_with_lebanon_and_syria"}
        n139["EGY_unify_with_libya"]
    end
    subgraph tier_5["Tier 5"]
        n140["EGY_anti_israeli_coalition"]
        n141["EGY_crush_the_arabian_revolt"]
        n142["EGY_expand_the_iron_guard"]
        n143["EGY_monopoly_over_financial_endowments"]
        n144["EGY_reestablish_the_ottoman_alliance"]
        n145["EGY_solidify_control_of_the_levant"]
        n146["EGY_support_womens_suffrage"]
        n147["EGY_united_arab_republic"]
    end
    subgraph tier_6["Tier 6"]
        n148["EGY_bring_the_rest_of_arabia_into_the_fold"]
        n149{"EGY_middle_eastern_diplomacy"}
        n150["EGY_placate_the_army"]
        n151{"EGY_reclaim_the_sehzade"}
        n152{"EGY_revive_the_eyalet"}
        n153{"EGY_royalist_propaganda"}
    end
    subgraph tier_7["Tier 7"]
        n154["EGY_claim_the_albanian_throne"]
        n155["EGY_continue_international_neutrality"]
        n156["EGY_defender_of_the_arab_world_focus"]
        n157{"EGY_diplomatic_mission_to_the_soviet_union"}
        n158["EGY_dominate_the_balkans"]
        n159["EGY_imperial_factories"]
        n160["EGY_invite_ottoman_intellectuals"]
        n161["EGY_join_the_central_powers"]
        n162["EGY_militarize_the_saadabad_pact"]
        n163["EGY_pact_of_middle_eastern_solidarity"]
        n164{"EGY_seek_american_material_aid"}
        n165["EGY_treaty_of_konya"]
    end
    subgraph tier_8["Tier 8"]
        n166["EGY_anti_invasion"]
        n167["EGY_avenge_the_battle_of_tell_el_kebir"]
        n168{"EGY_found_the_new_kingdom"}
        n169["EGY_join_the_allies"]
        n170["EGY_join_the_comintern"]
        n171["EGY_the_non_alligned_movement"]
    end
    subgraph tier_9["Tier 9"]
        n172["EGY_adopt_collectivization_policies"]
        n173["EGY_finalize_albanian_irredentism"]
        n174["EGY_food_importation"]
        n175["EGY_intervention_force"]
        n176["EGY_invite_NKVD_officers"]
        n177["EGY_radicalize_the_iron_guard"]
        n178["EGY_realize_the_nightmare_of_meiji"]
        n179["EGY_reclaim_the_eastern_trade_route"]
        n180["EGY_seek_democratic_allies"]
        n181["EGY_the_flying_lions"]
        n182["EGY_the_new_egyptian_model"]
    end
    subgraph tier_10["Tier 10"]
        n183["EGY_crush_the_israeli_state"]
        n184["EGY_joint_naval_development"]
        n185["EGY_reinforce_the_cyrenaica_claim"]
        n186["EGY_rekindle_the_unstable_alliance"]
        n187["EGY_soviet_tank_factories"]
        n188["EGY_the_rashad_mission"]
    end
    subgraph tier_11["Tier 11"]
        n189["EGY_support_communist_china"]
        n190["EGY_the_guardian_of_africa"]
        n191["EGY_the_iron_intelligence_department"]
        n192["EGY_topple_the_fascist_threat"]
    end
    n110 --> n117
    n170 --> n172
    n155 --> n166
    n138 --> n140
    n161 --> n167
    n163 --> n167
    n162 --> n167
    n147 --> n148
    n153 --> n154
    n149 --> n155
    n136 --> n141
    n182 --> n183
    n177 --> n183
    n148 --> n156
    n150 --> n157
    n148 --> n157
    n114 --> n128
    n125 --> n128
    n151 --> n158
    n67 --> n107
    n67 --> n108
    n108 --> n110
    n117 --> n142
    n128 --> n142
    n168 --> n173
    n169 --> n174
    n154 --> n168
    n127 --> n129
    n151 --> n159
    n152 --> n159
    n122 --> n130
    n168 --> n175
    n170 --> n176
    n119 --> n131
    n115 --> n118
    n151 --> n160
    n152 --> n160
    n109 --> n111
    n164 --> n169
    n151 --> n161
    n152 --> n161
    n157 --> n170
    n181 --> n184
    n174 --> n184
    n112 --> n119
    n120 --> n132
    n107 --> n112
    n142 --> n149
    n151 --> n162
    n152 --> n162
    n112 --> n120
    n109 --> n113
    n115 --> n121
    n135 --> n143
    n131 --> n143
    n113 --> n122
    n111 --> n122
    n121 --> n133
    n112 --> n123
    n151 --> n163
    n152 --> n163
    n120 --> n134
    n127 --> n134
    n143 --> n150
    n146 --> n150
    n116 --> n124
    n119 --> n135
    n168 --> n177
    n167 --> n178
    n167 --> n179
    n145 --> n151
    n141 --> n151
    n130 --> n144
    n182 --> n185
    n180 --> n186
    n114 --> n125
    n67 --> n109
    n144 --> n152
    n122 --> n136
    n142 --> n153
    n150 --> n164
    n148 --> n164
    n168 --> n180
    n136 --> n145
    n172 --> n187
    n176 --> n187
    n108 --> n114
    n187 --> n189
    n121 --> n137
    n134 --> n146
    n132 --> n146
    n169 --> n181
    n107 --> n115
    n186 --> n190
    n188 --> n191
    n108 --> n116
    n109 --> n116
    n110 --> n126
    n168 --> n182
    n164 --> n171
    n157 --> n171
    n177 --> n188
    n184 --> n192
    n149 --> n165
    n127 --> n138
    n127 --> n139
    n138 --> n147
    n139 --> n147
    n129 --> n147
    n115 --> n127
    n140 x--x n137
    n154 x--x n155
    n107 x--x n107
    n107 x--x n108
    n107 x--x n109
    n108 x--x n109
    n130 x--x n136
    n169 x--x n170
    n169 x--x n171
    n161 x--x n162
    n161 x--x n163
    n170 x--x n171
    n112 x--x n115
    n162 x--x n163
    n177 x--x n180
    n177 x--x n182
    n66 x--x n67
    n180 x--x n182
    n67 x--x n68
```

# EGY_solidify_british_ties

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n66["EGY_revolt_against_the_opressors"]
        n67["EGY_sever_the_ties"]
        n68{"EGY_solidify_british_ties"}
    end
    subgraph tier_1["Tier 1"]
        n193["EGY_continue_the_status_quo"]
        n194["EGY_egypts_place_in_the_empire"]
        n195["EGY_empower_govenor_general"]
    end
    subgraph tier_2["Tier 2"]
        n196["EGY_commonwealth_research_cooperation"]
        n197["EGY_educate_the_king"]
        n198["EGY_increase_british_military_influence"]
        n199["EGY_pacify_the_sudanese"]
        n200["EGY_the_nile_strategy"]
    end
    subgraph tier_3["Tier 3"]
        n201["EGY_cairo_logistics"]
        n202["EGY_commonwealth_investors"]
        n203["EGY_continue_british_arms_shipments"]
        n204["EGY_imperial_air_bases"]
        n205{"EGY_influence_of_the_king"}
        n206{"EGY_storm_abdeen_palace"}
    end
    subgraph tier_4["Tier 4"]
        n207["EGY_british_university_of_egypt"]
        n208["EGY_commonwealth_air_training_plan"]
        n209["EGY_egypt_serving_the_empire"]
        n210["EGY_invite_the_colonial_cabinet"]
        n211{"EGY_supply_the_empire"}
    end
    subgraph tier_5["Tier 5"]
        n212{"EGY_study_british_armor"}
        n213["EGY_welcome_british_exiles"]
    end
    subgraph tier_6["Tier 6"]
        n214["EGY_landing_exercices"]
        n215["EGY_prepare_homeland_defense"]
        n216["EGY_recruit_volunteers"]
        n217["EGY_take_the_lead_in_africa"]
    end
    subgraph tier_7["Tier 7"]
        n218["EGY_british_agents"]
        n219["EGY_reclaim_the_british_isles_exile"]
    end
    n216 --> n218
    n202 --> n207
    n203 --> n207
    n200 --> n201
    n204 --> n208
    n201 --> n208
    n196 --> n202
    n194 --> n196
    n196 --> n203
    n68 --> n193
    n193 --> n197
    n205 --> n209
    n206 --> n209
    n68 --> n194
    n68 --> n195
    n200 --> n204
    n195 --> n198
    n197 --> n205
    n206 --> n210
    n205 --> n210
    n213 --> n214
    n193 --> n199
    n194 --> n199
    n195 --> n199
    n212 --> n215
    n211 --> n215
    n214 --> n219
    n213 --> n216
    n198 --> n206
    n207 --> n212
    n204 --> n211
    n201 --> n211
    n212 --> n217
    n211 --> n217
    n194 --> n200
    n209 --> n213
    n210 --> n213
    n193 x--x n195
    n209 x--x n210
    n215 x--x n217
    n66 x--x n68
    n67 x--x n68
```
