# POL_assemble_the_regency_council

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("POL_assemble_the_regency_council"))
        n2["POL_complete_april_constitution"]
        n3["POL_organize_the_peasants_strike"]
        n4["POL_radicalize_the_front"]
        n5["POL_rewrite_1935_constitution"]
    end
    subgraph tier_1["Tier 1"]
        n6{"POL_fulfil_fifth_of_november"}
        n7["POL_seek_an_alliance_with_kaiser"]
    end
    subgraph tier_2["Tier 2"]
        n8["POL_claiming_lithuania"]
        n9["POL_cossack_king"]
        n10["POL_habsburg"]
        n11["POL_hohenzollern"]
        n12["POL_romanov"]
    end
    subgraph tier_3["Tier 3"]
        n13["POL_invite_exiled_nobility"]
        n14["POL_levy_liechtenstein_properties"]
        n15["POL_restoration_of_the_royal_sejm"]
        n16["POL_restore_bermontians"]
        n17["POL_restore_the_diet_of_galicia"]
        n18["POL_soldier_king"]
    end
    subgraph tier_4["Tier 4"]
        n19["POL_demand_LIT_pavel"]
        n20["POL_institute_royal_guards"]
        n21["POL_internal_romanian_support"]
        n22["POL_kings_guard"]
        n23["POL_pan_slavism"]
        n24["POL_royal_hussars"]
        n25["POL_support_monarchism_in_LIT"]
        n26["POL_support_monarchy_in_CZE"]
    end
    subgraph tier_5["Tier 5"]
        n27["POL_arm_monarchist_militants"]
        n28{"POL_demand_slovakia_pavel"}
        n29{"POL_demand_yugoslav_subjugation"}
        n30{"POL_governorate_livonia"}
        n31["POL_habsburg_monarchist_militants"]
        n32["POL_king_of_bohemia"]
        n33["POL_king_of_lithuania"]
        n34["POL_press_the_habsburg_claim"]
        n35{"POL_royal_officer_corps"}
    end
    subgraph tier_6["Tier 6"]
        n36["POL_LIT_union"]
        n37["POL_align_with_habsburgs"]
        n38["POL_assert_western_claims"]
        n39["POL_claim_russia"]
        n40["POL_king_michaels_coup"]
        n41["POL_seek_german_alignment"]
        n42["POL_trust_in_the_west"]
        n43["POL_unite_west_slavia"]
    end
    subgraph tier_7["Tier 7"]
        n44["POL_assert_eastern_claims_pavel"]
        n45{"POL_claim_livonia"}
        n46["POL_demand_pomerania"]
        n47["POL_demand_slovakia_monarchy"]
        n48["POL_expand_lithuanian_shipyards"]
        n49["POL_join_CZE_industry"]
        n50["POL_join_CZE_rails"]
        n51["POL_lithuanian_rail"]
        n52{"POL_merge_internal_governments"}
        n53["POL_reclaim_west_slavia"]
    end
    subgraph tier_8["Tier 8"]
        n54["POL_claim_greater_lithuania"]
        n55["POL_claim_prussia"]
        n56["POL_complete_the_bermontian_mission"]
        n57["POL_join_CZE_military"]
        n58["POL_merge_the_arms_industries"]
        n59["POL_pro_allied_government"]
        n60["POL_proclaim_slavic_unity"]
        n61["POL_push_for_ruthenia"]
        n62["POL_royal_dictatorship"]
    end
    subgraph tier_9["Tier 9"]
        n63["POL_ROM_join_allies"]
        n64["POL_demand_slovakia"]
        n65["POL_greater_commonwealth"]
        n66["POL_merge_civilian_industries"]
        n67["POL_warsaw_to_crimea_railway"]
    end
    subgraph tier_10["Tier 10"]
        n68["POL_restore_poland_hungary"]
    end
    n33 --> n36
    n19 --> n36
    n59 --> n63
    n35 --> n37
    n25 --> n27
    n21 --> n27
    n41 --> n44
    n28 --> n38
    n30 --> n38
    n45 --> n54
    n36 --> n45
    n33 --> n45
    n27 --> n45
    n45 --> n55
    n30 --> n39
    n28 --> n39
    n29 --> n39
    n6 --> n8
    n46 --> n56
    n44 --> n56
    n6 --> n9
    n16 --> n19
    n13 --> n19
    n38 --> n46
    n39 --> n46
    n62 --> n64
    n43 --> n47
    n19 --> n28
    n23 --> n29
    n19 --> n29
    n36 --> n48
    n1 --> n6
    n19 --> n30
    n54 --> n65
    n55 --> n65
    n6 --> n10
    n26 --> n31
    n24 --> n31
    n6 --> n11
    n15 --> n20
    n11 --> n21
    n15 --> n21
    n12 --> n13
    n43 --> n49
    n49 --> n57
    n50 --> n57
    n43 --> n50
    n21 --> n40
    n27 --> n40
    n26 --> n32
    n24 --> n32
    n25 --> n33
    n20 --> n33
    n18 --> n22
    n10 --> n14
    n11 --> n14
    n36 --> n51
    n58 --> n66
    n40 --> n52
    n51 --> n58
    n13 --> n23
    n22 --> n34
    n52 --> n59
    n45 --> n59
    n39 --> n60
    n46 --> n60
    n51 --> n61
    n37 --> n53
    n42 --> n53
    n43 --> n53
    n8 --> n15
    n11 --> n15
    n9 --> n16
    n64 --> n68
    n10 --> n17
    n6 --> n12
    n52 --> n62
    n17 --> n24
    n18 --> n24
    n22 --> n35
    n1 --> n7
    n28 --> n41
    n30 --> n41
    n10 --> n18
    n15 --> n25
    n8 --> n25
    n17 --> n26
    n35 --> n42
    n32 --> n43
    n31 --> n43
    n61 --> n67
    n37 x--x n42
    n1 x--x n2
    n1 x--x n3
    n1 x--x n4
    n1 x--x n5
    n38 x--x n39
    n38 x--x n41
    n39 x--x n41
    n8 x--x n9
    n8 x--x n10
    n8 x--x n11
    n8 x--x n12
    n9 x--x n10
    n9 x--x n11
    n9 x--x n12
    n10 x--x n11
    n10 x--x n12
    n11 x--x n12
    n59 x--x n62
```

# POL_clamp_down_on_danzig

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n69["POL_attract_poles_to_gdynia"]
        n70(("POL_clamp_down_on_danzig"))
        n71["POL_develop_polish_ship_building"]
    end
    subgraph tier_1["Tier 1"]
        n72["POL_ban_the_nazi_party"]
        n73["POL_study_foreign_built_ships"]
    end
    subgraph tier_2["Tier 2"]
        n74["POL_develop_gdansk_ship_building"]
        n75["POL_expand_gdynia_seaport"]
        n76["POL_integrate_gdansk_industries"]
    end
    subgraph tier_3["Tier 3"]
        n77["POL_Maritime_Defense_Fund"]
        n78{"POL_Naval_Officers_School"}
        n79{"POL_import_submarine_technology"}
    end
    subgraph tier_4["Tier 4"]
        n80["POL_High_Frequency_Radio_Detection"]
        n81["POL_a_cruiser_navy"]
        n82["POL_coastal_defense"]
        n83["POL_commerce_attack"]
        n84["POL_strike_force"]
    end
    subgraph tier_5["Tier 5"]
        n85["POL_Maritime_and_Colonial_League"]
        n86["POL_River_Flotillas"]
        n87["POL_baltic_navy"]
    end
    n78 --> n80
    n76 --> n77
    n75 --> n77
    n81 --> n85
    n76 --> n78
    n75 --> n78
    n82 --> n86
    n78 --> n81
    n84 --> n87
    n82 --> n87
    n70 --> n72
    n78 --> n82
    n79 --> n82
    n79 --> n83
    n72 --> n74
    n69 --> n75
    n73 --> n75
    n76 --> n79
    n75 --> n79
    n72 --> n76
    n78 --> n84
    n79 --> n84
    n71 --> n73
    n70 --> n73
    n70 x--x n71
    n82 x--x n84
```

# POL_complete_april_constitution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n88["POL_Align_With_Japan"]
        n89["POL_Found_Our_Own_Faction"]
        n90{"POL_Interventionist_Foreign_Policy"}
        n91["POL_Invite_Sweden"]
        n92{"POL_Polish_Czechoslovakian_Alliance"}
        n93["POL_The_Endecja_Movement"]
        n94["POL_The_Front_Morges"]
        n95["POL_Universalism"]
        n1["POL_assemble_the_regency_council"]
        n2(("POL_complete_april_constitution"))
        n96["POL_morges_economic_union"]
        n3["POL_organize_the_peasants_strike"]
        n97["POL_press_for_liberia"]
        n4["POL_radicalize_the_front"]
        n5["POL_rewrite_1935_constitution"]
    end
    subgraph tier_1["Tier 1"]
        n98["POL_Invite_Hungary"]
        n99["POL_Pressure_Czechoslovakia"]
        n100["POL_Silesia_Or_War"]
        n101["POL_polish_militarism"]
    end
    subgraph tier_2["Tier 2"]
        n102["POL_consolidate_sanation_government"]
    end
    subgraph tier_3["Tier 3"]
        n103["POL_Consolidate_The_Nationalist_Wing"]
        n104["POL_Reaffirm_Ties_With_Romania"]
        n105{"POL_the_castle"}
        n106{"POL_the_sanation_left"}
        n107{"POL_the_sanation_right"}
    end
    subgraph tier_4["Tier 4"]
        n108{"POL_Budget_Reform"}
        n109["POL_Defensive_Focus"]
        n110{"POL_Polish_Revanchism"}
        n111["POL_codify_national_unity"]
        n112["POL_department_for_home_defence"]
        n113["POL_draft_a_new_constitution"]
        n114["POL_eliminate_socialist_parties"]
        n115["POL_legion_of_merit"]
        n116["POL_modus_vivendi"]
        n117{"POL_second_man_of_the_state"}
        n118["POL_support_right_paramilitaries"]
        n119["POL_the_left_chairman"]
    end
    subgraph tier_5["Tier 5"]
        n120["POL_Army_Modernisation"]
        n121["POL_Devalue_Zloty"]
        n122["POL_Polish_German_Trade_Agreement"]
        n123["POL_Prepare_For_The_upcoming_conflict"]
        n124{"POL_camp_of_national_unity"}
        n125{"POL_common_organization_of_society"}
        n126["POL_dissolve_the_sejm"]
        n127{"POL_ozon"}
        n128["POL_preserve_bougoise_democracy"]
        n129["POL_promote_chemical_industry"]
    end
    subgraph tier_6["Tier 6"]
        n130["POL_Re_Expand_The_Military"]
        n131{"POL_Third_Europe"}
        n132{"POL_dissolve_the_bbwr"}
        n133["POL_preserve_baltic_independence"]
        n134["POL_reopen_the_maritime_and_colonial_league"]
    end
    subgraph tier_7["Tier 7"]
        n135["POL_Align_With_Kaiserreich"]
        n136["POL_The_Intermarium"]
        n137{"POL_align_with_the_west"}
        n138["POL_baltic_security"]
        n139["POL_invite_romania_to_morges"]
    end
    subgraph tier_8["Tier 8"]
        n140["POL_Fund_The_Promethean_Program"]
        n141["POL_Invite_Yugoslavia"]
        n142["POL_baltic_alliance_focus"]
        n143["POL_invite_ukraine"]
        n144["POL_join_allies"]
        n145{"POL_lithuanian_annexation"}
        n146["POL_lithuanian_ultimatum"]
        n147["POL_protect_czechozlovakia"]
    end
    subgraph tier_9["Tier 9"]
        n148["POL_Minsk_Or_War"]
        n149["POL_lithuanian_alliance"]
        n150["POL_romanian_alliance"]
        n151["POL_romanian_bridgehead_strategy"]
    end
    subgraph tier_10["Tier 10"]
        n152["POL_Finnish_Guarantee"]
        n153["POL_Sarny_Fortified_Area"]
    end
    subgraph tier_unplaced["Unplaced (cycle)"]
        n154["POL_The_Baltic_Alliance"]
        n155["POL_baltic_ultimatums"]
        n156["POL_pan_slavic_revanchism"]
        n157["POL_sea_to_sea"]
        n158["POL_the_neighbours_protection"]
        n159["POL_the_old_borders"]
    end
    n132 --> n135
    n117 --> n120
    n105 --> n108
    n93 --> n103
    n102 --> n103
    n94 --> n109
    n106 --> n109
    n117 --> n121
    n108 --> n121
    n91 --> n152
    n150 --> n152
    n136 --> n152
    n136 --> n140
    n89 --> n140
    n88 --> n140
    n131 --> n98
    n95 --> n98
    n136 --> n141
    n89 --> n141
    n140 --> n148
    n119 --> n122
    n103 --> n110
    n119 --> n123
    n156 --> n99
    n95 --> n99
    n123 --> n130
    n102 --> n104
    n151 --> n153
    n131 --> n100
    n95 --> n100
    n131 --> n154
    n132 --> n136
    n90 --> n136
    n92 --> n131
    n124 --> n131
    n127 --> n131
    n110 --> n131
    n92 --> n131
    n124 --> n137
    n132 --> n137
    n127 --> n137
    n138 --> n142
    n136 --> n142
    n132 --> n138
    n131 --> n155
    n145 --> n155
    n108 --> n124
    n117 --> n124
    n107 --> n111
    n119 --> n125
    n101 --> n102
    n107 --> n112
    n125 --> n132
    n114 --> n126
    n106 --> n113
    n105 --> n114
    n96 --> n139
    n133 --> n139
    n136 --> n143
    n137 --> n144
    n106 --> n115
    n146 --> n149
    n137 --> n145
    n131 --> n145
    n137 --> n146
    n106 --> n116
    n117 --> n127
    n131 --> n156
    n2 --> n101
    n128 --> n133
    n109 --> n128
    n90 --> n128
    n108 --> n129
    n138 --> n147
    n136 --> n147
    n97 --> n134
    n128 --> n134
    n147 --> n150
    n144 --> n151
    n155 --> n157
    n159 --> n157
    n107 --> n117
    n107 --> n118
    n102 --> n105
    n106 --> n119
    n131 --> n158
    n156 --> n159
    n102 --> n106
    n102 --> n107
    n135 x--x n136
    n108 x--x n117
    n108 x--x n119
    n154 x--x n155
    n131 x--x n137
    n131 x--x n138
    n137 x--x n138
    n1 x--x n2
    n124 x--x n132
    n124 x--x n127
    n111 x--x n113
    n2 x--x n3
    n2 x--x n4
    n2 x--x n5
    n132 x--x n127
    n145 x--x n146
    n117 x--x n119
```

# POL_develop_polish_ship_building

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n70["POL_clamp_down_on_danzig"]
        n71(("POL_develop_polish_ship_building"))
        n76["POL_integrate_gdansk_industries"]
    end
    subgraph tier_1["Tier 1"]
        n160["POL_Seek_Accommodation_With_Germany"]
        n69["POL_attract_poles_to_gdynia"]
        n73["POL_study_foreign_built_ships"]
    end
    subgraph tier_2["Tier 2"]
        n161["POL_German_Berlinka_Highway_Project"]
        n162["POL_Ribbentrop_Beck_Pact"]
        n75["POL_expand_gdynia_seaport"]
    end
    subgraph tier_3["Tier 3"]
        n163["POL_Break_Away_From_Germany"]
        n77["POL_Maritime_Defense_Fund"]
        n78{"POL_Naval_Officers_School"}
        n79{"POL_import_submarine_technology"}
    end
    subgraph tier_4["Tier 4"]
        n80["POL_High_Frequency_Radio_Detection"]
        n81["POL_a_cruiser_navy"]
        n82["POL_coastal_defense"]
        n83["POL_commerce_attack"]
        n84["POL_strike_force"]
    end
    subgraph tier_5["Tier 5"]
        n85["POL_Maritime_and_Colonial_League"]
        n86["POL_River_Flotillas"]
        n87["POL_baltic_navy"]
    end
    n162 --> n163
    n160 --> n161
    n78 --> n80
    n76 --> n77
    n75 --> n77
    n81 --> n85
    n76 --> n78
    n75 --> n78
    n160 --> n162
    n82 --> n86
    n71 --> n160
    n78 --> n81
    n71 --> n69
    n84 --> n87
    n82 --> n87
    n78 --> n82
    n79 --> n82
    n79 --> n83
    n69 --> n75
    n73 --> n75
    n76 --> n79
    n75 --> n79
    n78 --> n84
    n79 --> n84
    n71 --> n73
    n70 --> n73
    n70 x--x n71
    n82 x--x n84
```

# POL_organize_the_peasants_strike

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["POL_assemble_the_regency_council"]
        n2["POL_complete_april_constitution"]
        n3(("POL_organize_the_peasants_strike"))
        n133["POL_preserve_baltic_independence"]
        n128["POL_preserve_bougoise_democracy"]
        n4["POL_radicalize_the_front"]
        n5["POL_rewrite_1935_constitution"]
    end
    subgraph tier_1["Tier 1"]
        n164{"POL_woo_morges_staff"}
    end
    subgraph tier_2["Tier 2"]
        n165["POL_arm_peasant_militia"]
        n166["POL_ease_sanationist_tensions"]
        n167{"POL_raise_the_black_madonna"}
        n168{"POL_state_national_council"}
    end
    subgraph tier_3["Tier 3"]
        n169{"POL_KPP_focus"}
        n170["POL_a_leftist_sejm"]
        n171["POL_communal_governance"]
        n172["POL_elect_a_PSL_leader"]
        n173["POL_empower_the_morges"]
        n174["POL_reassemble_the_sejm"]
    end
    subgraph tier_4["Tier 4"]
        n175["POL_dabrowszczacy"]
        n176{"POL_invest_in_the_peasantry"}
        n177["POL_polish_path_to_socialism"]
        n178["POL_surrender_the_east"]
    end
    subgraph tier_5["Tier 5"]
        n179{"POL_anti_imperialism"}
        n180["POL_leftist_economics"]
        n181["POL_lower_class_education"]
        n182["POL_morges_pact"]
        n183["POL_polish_peoples_republic"]
    end
    subgraph tier_6["Tier 6"]
        n184["POL_anti_capitalist_revolution"]
        n185["POL_anti_fascist_military"]
        n186["POL_committee_of_national_liberation"]
        n96["POL_morges_economic_union"]
        n187["POL_non_discriminatory_recruitment"]
        n188{"POL_pressure_for_the_west"}
        n189{"POL_soviet_industry"}
        n190{"POL_soviet_military_staff"}
    end
    subgraph tier_7["Tier 7"]
        n191["POL_armia_ludowa"]
        n192["POL_baltic_socialism"]
        n193["POL_com_independence"]
        n194["POL_greater_polish_SSR"]
        n139["POL_invite_romania_to_morges"]
        n97["POL_press_for_liberia"]
        n195["POL_purchase_madagascar"]
    end
    subgraph tier_8["Tier 8"]
        n196["POL_dismantle_capitalist_empires"]
        n134["POL_reopen_the_maritime_and_colonial_league"]
        n197["POL_support_colonial_workers_strikes"]
    end
    subgraph tier_9["Tier 9"]
        n198["POL_dismantle_fascist_empires"]
        n199["POL_social_commonwealth"]
    end
    subgraph tier_10["Tier 10"]
        n200["POL_dismantle_soviet_empire"]
    end
    n168 --> n169
    n168 --> n170
    n179 --> n184
    n182 --> n185
    n177 --> n179
    n164 --> n165
    n186 --> n191
    n187 --> n191
    n184 --> n192
    n189 --> n193
    n188 --> n193
    n190 --> n193
    n180 --> n186
    n168 --> n171
    n169 --> n175
    n172 --> n175
    n192 --> n196
    n196 --> n198
    n198 --> n200
    n164 --> n166
    n167 --> n172
    n167 --> n173
    n189 --> n194
    n188 --> n194
    n190 --> n194
    n172 --> n176
    n96 --> n139
    n133 --> n139
    n177 --> n180
    n178 --> n180
    n176 --> n180
    n177 --> n181
    n178 --> n181
    n176 --> n181
    n182 --> n96
    n176 --> n182
    n180 --> n187
    n169 --> n177
    n178 --> n183
    n184 --> n97
    n182 --> n97
    n183 --> n188
    n96 --> n195
    n164 --> n167
    n167 --> n174
    n97 --> n134
    n128 --> n134
    n196 --> n199
    n183 --> n189
    n183 --> n190
    n164 --> n168
    n97 --> n197
    n184 --> n197
    n169 --> n178
    n3 --> n164
    n169 x--x n172
    n184 x--x n182
    n165 x--x n166
    n1 x--x n3
    n193 x--x n194
    n2 x--x n3
    n3 x--x n4
    n3 x--x n5
    n177 x--x n178
```

# POL_prepare_for_the_inevitable

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n201(("POL_prepare_for_the_inevitable"))
    end
    subgraph tier_1["Tier 1"]
        n202["POL_Evacuate_Polands_Gold_Reserves"]
        n203["POL_accept_border_realignment"]
        n204["POL_expand_polish_intelligence"]
        n205["POL_foreign_air_support"]
        n206["POL_foreign_naval_support"]
    end
    subgraph tier_2["Tier 2"]
        n207["POL_aces_in_exile"]
        n208["POL_foreign_army_support"]
        n209["POL_niech_zyje_opor"]
        n210["POL_resistance_industries"]
        n211["POL_the_cyclometer"]
        n212["POL_the_long_push_home"]
    end
    subgraph tier_3["Tier 3"]
        n213["POL_exile_industries"]
        n214["POL_the_bombe"]
    end
    n201 --> n202
    n201 --> n203
    n205 --> n207
    n210 --> n213
    n201 --> n204
    n201 --> n205
    n205 --> n208
    n201 --> n206
    n204 --> n209
    n202 --> n210
    n211 --> n214
    n204 --> n211
    n204 --> n212
```

# POL_prepare_for_the_next_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n215(("POL_prepare_for_the_next_war"))
    end
    subgraph tier_1["Tier 1"]
        n216["POL_Expand_the_Lucznik_State_Arms_Factory"]
        n217["POL_Kasprzycki_Gamelin_Convention"]
        n218["POL_Modlin_Fortress"]
        n219["POL_Plan_W"]
        n220["POL_new_military_academy"]
        n221["POL_plan_east"]
        n222["POL_plan_west"]
    end
    subgraph tier_2["Tier 2"]
        n223["POL_Class_A_Reservists"]
        n224["POL_KOR_Committee_For_Defense"]
        n225["POL_Plan_Z"]
        n226["POL_belorussian_army"]
        n227["POL_eastern_conscripts"]
        n228["POL_expand_poznan_forts"]
        n229["POL_fortification_of_belarus"]
        n230["POL_fortification_of_ukraine"]
        n231["POL_hel_fortified_area"]
        n232["POL_invest_anti_air"]
        n233["POL_local_eastern_plans"]
        n234["POL_local_western_plans"]
        n235["POL_ruthenian_army"]
        n236["POL_sabotage_polish_industry"]
        n237["POL_silesia_fortified_area"]
        n238["POL_standardisation_of_equipment"]
        n239["POL_sudeten_mountaineers"]
        n240["POL_supply_the_rail_nexus"]
        n241["POL_the_prusya_army"]
        n242["POL_the_prusya_line"]
    end
    subgraph tier_3["Tier 3"]
        n243["POL_Land_Mine_Detectors"]
        n244["POL_Military_Aviation_Exports"]
        n245["POL_Wartime_Industry"]
        n246{"POL_army_modernisation"}
        n247["POL_complete_plan_east"]
        n248["POL_complete_plan_west"]
    end
    subgraph tier_4["Tier 4"]
        n249["POL_Artillery_Motorization"]
        n250["POL_Wz_35_Anti_Tank_Rifle"]
        n251{"POL_air_innovations"}
        n252["POL_attract_foreign_motors"]
        n253{"POL_fighter_modernisation"}
        n254["POL_modernising_the_cavalry"]
    end
    subgraph tier_5["Tier 5"]
        n255["POL_Cegielski_Artillery_Factory"]
        n256["POL_Independent_Parachute_Brigades"]
        n257["POL_Modernize_The_Starachowice_Works"]
        n258["POL_adaptive_designs"]
        n259{"POL_heavy_fighter_concept"}
        n260["POL_naval_bomber_experiments"]
        n261["POL_study_foreign_tanks"]
    end
    subgraph tier_6["Tier 6"]
        n262["POL_Gundlach_Periscope"]
        n263["POL_anti_blitz_vehicles"]
        n264["POL_cruiser_tank_experiments"]
        n265["POL_light_bomber_focus"]
        n266["POL_medium_bomber_focus"]
    end
    subgraph tier_7["Tier 7"]
        n267["POL_Mielec_Aircraft_Factory"]
        n268["POL_Swiatecki_Bomb_Slip"]
        n269["POL_air_modernisations_programme"]
    end
    subgraph tier_8["Tier 8"]
        n270["POL_rocket_development"]
    end
    n246 --> n249
    n249 --> n255
    n219 --> n223
    n215 --> n216
    n261 --> n262
    n251 --> n256
    n220 --> n224
    n215 --> n217
    n238 --> n243
    n265 --> n267
    n238 --> n244
    n249 --> n257
    n215 --> n218
    n215 --> n219
    n219 --> n225
    n266 --> n268
    n223 --> n245
    n225 --> n245
    n246 --> n250
    n252 --> n258
    n250 --> n258
    n244 --> n251
    n265 --> n269
    n266 --> n269
    n261 --> n263
    n250 --> n263
    n238 --> n246
    n246 --> n252
    n221 --> n226
    n229 --> n247
    n230 --> n247
    n240 --> n247
    n227 --> n247
    n226 --> n247
    n235 --> n247
    n233 --> n247
    n241 --> n248
    n237 --> n248
    n234 --> n248
    n239 --> n248
    n232 --> n248
    n242 --> n248
    n228 --> n248
    n231 --> n248
    n261 --> n264
    n221 --> n227
    n222 --> n228
    n244 --> n253
    n221 --> n229
    n221 --> n230
    n251 --> n259
    n253 --> n259
    n222 --> n231
    n222 --> n232
    n259 --> n265
    n253 --> n265
    n221 --> n233
    n222 --> n234
    n259 --> n266
    n251 --> n266
    n246 --> n254
    n251 --> n260
    n215 --> n220
    n215 --> n221
    n215 --> n222
    n269 --> n270
    n221 --> n235
    n221 --> n236
    n222 --> n236
    n222 --> n237
    n220 --> n238
    n254 --> n261
    n252 --> n261
    n222 --> n239
    n221 --> n240
    n222 --> n241
    n222 --> n242
    n252 x--x n254
    n265 x--x n266
```

# POL_radicalize_the_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n135["POL_Align_With_Kaiserreich"]
        n1["POL_assemble_the_regency_council"]
        n138["POL_baltic_security"]
        n2["POL_complete_april_constitution"]
        n132{"POL_dissolve_the_bbwr"}
        n96["POL_morges_economic_union"]
        n3["POL_organize_the_peasants_strike"]
        n97["POL_press_for_liberia"]
        n4(("POL_radicalize_the_front"))
        n5["POL_rewrite_1935_constitution"]
        n106["POL_the_sanation_left"]
    end
    subgraph tier_1["Tier 1"]
        n271{"POL_The_Great_Peasant_Strike"}
    end
    subgraph tier_2["Tier 2"]
        n94["POL_The_Front_Morges"]
        n272["POL_The_Polish_Socialist_Party"]
    end
    subgraph tier_3["Tier 3"]
        n273["POL_Austerity_Measures"]
        n274["POL_Civil_Service_Reform"]
        n109["POL_Defensive_Focus"]
        n275["POL_Seek_Accommodation_With_The_USSR"]
        n276["POL_State_Capitalism"]
        n277["POL_the_Agrarian_Reform"]
    end
    subgraph tier_4["Tier 4"]
        n278{"POL_Beck_Molotov_Pact"}
        n90{"POL_Interventionist_Foreign_Policy"}
        n279["POL_Subsidized_Universal_Education"]
        n280["POL_The_Leviathan_Group"]
        n281["POL_Workers_Brigades"]
    end
    subgraph tier_5["Tier 5"]
        n282["POL_Attract_Foreign_Investment"]
        n283["POL_Draw_Closer_To_France"]
        n284["POL_Draw_Closer_To_The_USSR"]
        n285["POL_Mandatory_Firearm_Ownership"]
        n286["POL_Seek_Autonomy"]
        n136["POL_The_Intermarium"]
        n128["POL_preserve_bougoise_democracy"]
    end
    subgraph tier_6["Tier 6"]
        n287["POL_Baltic_Naval_Vanguard"]
        n288["POL_License_Soviet_Equipment"]
        n289["POL_Political_Commissars"]
        n290["POL_Preemptive_Strike"]
        n291["POL_The_Three_Year_Plan"]
        n142["POL_baltic_alliance_focus"]
        n143["POL_invite_ukraine"]
        n133["POL_preserve_baltic_independence"]
        n147["POL_protect_czechozlovakia"]
        n134["POL_reopen_the_maritime_and_colonial_league"]
    end
    subgraph tier_7["Tier 7"]
        n292["POL_Polish_Peoples_Army"]
        n293["POL_Socialist_Realism"]
        n294["POL_Vladimir_Lenin_Steelworks"]
        n139["POL_invite_romania_to_morges"]
        n150["POL_romanian_alliance"]
    end
    subgraph tier_8["Tier 8"]
        n88["POL_Align_With_Japan"]
        n89["POL_Found_Our_Own_Faction"]
    end
    subgraph tier_9["Tier 9"]
        n140["POL_Fund_The_Promethean_Program"]
        n91["POL_Invite_Sweden"]
        n141["POL_Invite_Yugoslavia"]
    end
    subgraph tier_10["Tier 10"]
        n152["POL_Finnish_Guarantee"]
        n148["POL_Minsk_Or_War"]
    end
    n292 --> n88
    n285 --> n88
    n280 --> n282
    n272 --> n273
    n284 --> n287
    n275 --> n278
    n94 --> n274
    n94 --> n109
    n106 --> n109
    n90 --> n283
    n278 --> n284
    n91 --> n152
    n150 --> n152
    n136 --> n152
    n292 --> n89
    n285 --> n89
    n136 --> n140
    n89 --> n140
    n88 --> n140
    n274 --> n90
    n89 --> n91
    n136 --> n141
    n89 --> n141
    n284 --> n288
    n281 --> n285
    n140 --> n148
    n273 --> n292
    n289 --> n292
    n285 --> n292
    n284 --> n289
    n286 --> n289
    n283 --> n290
    n272 --> n275
    n278 --> n286
    n291 --> n293
    n272 --> n276
    n276 --> n279
    n271 --> n94
    n4 --> n271
    n132 --> n136
    n90 --> n136
    n274 --> n280
    n271 --> n272
    n284 --> n291
    n286 --> n291
    n291 --> n294
    n276 --> n281
    n138 --> n142
    n136 --> n142
    n96 --> n139
    n133 --> n139
    n136 --> n143
    n128 --> n133
    n109 --> n128
    n90 --> n128
    n138 --> n147
    n136 --> n147
    n97 --> n134
    n128 --> n134
    n147 --> n150
    n272 --> n277
    n94 --> n277
    n135 x--x n136
    n284 x--x n286
    n94 x--x n272
    n1 x--x n4
    n2 x--x n4
    n3 x--x n4
    n4 x--x n5
```

# POL_rewrite_1935_constitution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n137{"POL_align_with_the_west"}
        n1["POL_assemble_the_regency_council"]
        n138["POL_baltic_security"]
        n124{"POL_camp_of_national_unity"}
        n2["POL_complete_april_constitution"]
        n102["POL_consolidate_sanation_government"]
        n146["POL_lithuanian_ultimatum"]
        n3["POL_organize_the_peasants_strike"]
        n127{"POL_ozon"}
        n4["POL_radicalize_the_front"]
        n5(("POL_rewrite_1935_constitution"))
    end
    subgraph tier_1["Tier 1"]
        n295{"POL_Nationalist_Rhetoric"}
        n145{"POL_lithuanian_annexation"}
    end
    subgraph tier_2["Tier 2"]
        n93["POL_The_Endecja_Movement"]
        n296["POL_The_National_Radical_Camp"]
    end
    subgraph tier_3["Tier 3"]
        n297["POL_Align_With_Italy"]
        n298["POL_Align_With_Russia"]
        n299["POL_All_Polish_Youth"]
        n300["POL_Beyond_The_Proletariat"]
        n103["POL_Consolidate_The_Nationalist_Wing"]
        n301["POL_Invest_In_The_Middle_Class"]
        n302["POL_Mend_Ties_With_Czechoslovakia"]
        n303["POL_Propaganda_Corps"]
    end
    subgraph tier_4["Tier 4"]
        n304["POL_Autarky"]
        n305["POL_Folk_High_Schools"]
        n92{"POL_Polish_Czechoslovakian_Alliance"}
        n110{"POL_Polish_Revanchism"}
        n306["POL_The_Student_Movement"]
        n95["POL_Universalism"]
        n307["POL_konfederacja_narodu"]
    end
    subgraph tier_5["Tier 5"]
        n98["POL_Invite_Hungary"]
        n308["POL_Invite_Nationalist_Spain"]
        n99["POL_Pressure_Czechoslovakia"]
        n100["POL_Silesia_Or_War"]
        n131{"POL_Third_Europe"}
        n309["POL_polish_shock_battallions"]
        n310["POL_support_falangists_in_the_americas"]
    end
    subgraph tier_unplaced["Unplaced (cycle)"]
        n154["POL_The_Baltic_Alliance"]
        n155["POL_baltic_ultimatums"]
        n156["POL_pan_slavic_revanchism"]
        n157["POL_sea_to_sea"]
        n158["POL_the_neighbours_protection"]
        n159["POL_the_old_borders"]
    end
    n93 --> n297
    n296 --> n297
    n93 --> n298
    n296 --> n298
    n93 --> n299
    n296 --> n299
    n300 --> n304
    n296 --> n300
    n93 --> n103
    n102 --> n103
    n301 --> n305
    n93 --> n301
    n131 --> n98
    n95 --> n98
    n95 --> n308
    n93 --> n302
    n296 --> n302
    n5 --> n295
    n302 --> n92
    n103 --> n110
    n156 --> n99
    n95 --> n99
    n296 --> n303
    n131 --> n100
    n95 --> n100
    n131 --> n154
    n295 --> n93
    n295 --> n296
    n299 --> n306
    n92 --> n131
    n124 --> n131
    n127 --> n131
    n110 --> n131
    n92 --> n131
    n303 --> n95
    n131 --> n155
    n145 --> n155
    n303 --> n307
    n137 --> n145
    n131 --> n145
    n131 --> n156
    n307 --> n309
    n155 --> n157
    n159 --> n157
    n95 --> n310
    n131 --> n158
    n156 --> n159
    n154 x--x n155
    n93 x--x n296
    n131 x--x n137
    n131 x--x n138
    n1 x--x n5
    n2 x--x n5
    n145 x--x n146
    n3 x--x n5
    n4 x--x n5
```

# POL_the_four_year_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n311(("POL_the_four_year_plan"))
    end
    subgraph tier_1["Tier 1"]
        n312["POL_Stomil_Debica_Rubber_Plant"]
        n313["POL_additional_research_slot1"]
        n314["POL_central_region_strategy"]
        n315["POL_fill_the_railways_gaps"]
    end
    subgraph tier_2["Tier 2"]
        n316["POL_Huta_Stalowa_Wola_Steel_Mill"]
        n317["POL_agrarian_reform"]
        n318["POL_central_defence_of_poland"]
        n319["POL_expansion_of_new_towns"]
        n320["POL_invest_in_the_old_polish_region"]
        n321["POL_national_defence_fund"]
    end
    subgraph tier_3["Tier 3"]
        n322{"POL_additional_research_slot2"}
        n323["POL_develop_upper_silesia"]
        n324["POL_expand_katowice_mines"]
        n325["POL_invest_in_eastern_poland"]
        n326["POL_modernize_congressional_factories"]
        n327["POL_start_central_industrial_region"]
    end
    subgraph tier_4["Tier 4"]
        n328["POL_abolish_segregated_seating"]
        n329["POL_expand_central_industrial_region"]
        n330["POL_ideological_fanaticism"]
        n331["POL_warsaw_main_railway_station"]
    end
    subgraph tier_5["Tier 5"]
        n332["POL_Start_The_Fifteen_Year_Plan"]
        n333["POL_atomic_physics_institute"]
    end
    subgraph tier_6["Tier 6"]
        n334["POL_Phase_I_Military_Rearmament"]
    end
    subgraph tier_7["Tier 7"]
        n335["POL_Phase_II_Infrastructure_Development"]
    end
    subgraph tier_8["Tier 8"]
        n336["POL_Construct_Hydroelectric_Power_Plants"]
        n337["POL_Phase_III_Agriculture_and_Education"]
    end
    subgraph tier_9["Tier 9"]
        n338["POL_Electrification_of_the_Countryside"]
        n339["POL_Phase_IV_Urbanization"]
    end
    subgraph tier_10["Tier 10"]
        n340["POL_Expansion_Of_New_Towns"]
        n341["POL_Phase_V_Equalize_Poland_A_and_B"]
    end
    n335 --> n336
    n336 --> n338
    n339 --> n340
    n315 --> n316
    n335 --> n337
    n334 --> n335
    n337 --> n339
    n332 --> n334
    n339 --> n341
    n323 --> n332
    n331 --> n332
    n329 --> n332
    n311 --> n312
    n322 --> n328
    n311 --> n313
    n319 --> n322
    n315 --> n317
    n330 --> n333
    n328 --> n333
    n315 --> n318
    n314 --> n318
    n311 --> n314
    n318 --> n323
    n327 --> n329
    n319 --> n324
    n314 --> n319
    n311 --> n315
    n322 --> n330
    n317 --> n325
    n318 --> n325
    n314 --> n320
    n320 --> n326
    n315 --> n321
    n319 --> n327
    n326 --> n331
    n328 x--x n330
```
