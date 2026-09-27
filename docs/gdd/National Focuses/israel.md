# ISR_ad_halom

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ISR_ad_halom"))
        n2["ISR_win"]
    end
    subgraph tier_1["Tier 1"]
        n3{"ISR_form_the_israeli_navy"}
        n4["ISR_provisional_government"]
        n5["ISR_raise_jewish_militias"]
    end
    subgraph tier_2["Tier 2"]
        n6["ISR_Sea_Dominance"]
        n7["ISR_Small_Navy"]
        n8["ISR_building_the_new_homeland"]
        n9["ISR_form_the_mossad"]
        n10["ISR_formalize_military"]
        n11["ISR_israel_military_industries"]
        n12["ISR_national_higher_education"]
        n13["ISR_reading_power_station"]
    end
    subgraph tier_3["Tier 3"]
        n14["ISR_Dockyards"]
        n15["ISR_Study_Ships"]
        n16["ISR_Submarine"]
        n17["ISR_equipment_modernization"]
        n18["ISR_kibbutz_production"]
        n19["ISR_land_reclamation"]
        n20["ISR_link_communities"]
        n21["ISR_plane_imports"]
        n22["ISR_proffesional_army_training"]
        n23["ISR_special_night_squads"]
        n24["ISR_world_wide_spy_web"]
    end
    subgraph tier_4["Tier 4"]
        n25["ISR_Battleship"]
        n26["ISR_Carrier"]
        n27["ISR_Ships_American"]
        n28["ISR_Ships_England"]
        n29["ISR_establish_a_military_academy"]
        n30["ISR_firearms_production"]
        n31["ISR_independent_steel_production"]
        n32{"ISR_israeli_air_school"}
        n33["ISR_military_vehicles"]
        n34["ISR_special_forces"]
        n35["ISR_stealth_upgrades"]
        n36["ISR_volunteer_pilots"]
    end
    subgraph tier_5["Tier 5"]
        n37["ISR_Cruisers"]
        n38["ISR_Destroyer"]
        n39["ISR_Navy_Aircrafts"]
        n40["ISR_armored_vehicles"]
        n41["ISR_bimotor_aircrafts"]
        n42["ISR_build_trainer_aircrafts"]
        n43["ISR_form_the_techni"]
        n44["ISR_industrial_expansion_plan"]
        n45["ISR_issue_the_israeli_lira"]
        n46["ISR_modern_logistics"]
    end
    subgraph tier_6["Tier 6"]
        n47["ISR_Naval_Doctrine"]
    end
    n14 --> n25
    n14 --> n26
    n25 --> n37
    n26 --> n37
    n25 --> n38
    n26 --> n38
    n7 --> n14
    n6 --> n14
    n37 --> n47
    n38 --> n47
    n25 --> n47
    n26 --> n39
    n3 --> n6
    n15 --> n27
    n15 --> n28
    n3 --> n7
    n6 --> n15
    n7 --> n16
    n33 --> n40
    n31 --> n40
    n32 --> n41
    n32 --> n42
    n4 --> n8
    n11 --> n17
    n23 --> n29
    n17 --> n29
    n18 --> n30
    n2 --> n3
    n1 --> n3
    n4 --> n9
    n32 --> n43
    n5 --> n10
    n18 --> n31
    n30 --> n44
    n31 --> n44
    n5 --> n11
    n21 --> n32
    n31 --> n45
    n8 --> n18
    n8 --> n19
    n8 --> n20
    n20 --> n33
    n11 --> n33
    n33 --> n46
    n29 --> n46
    n4 --> n12
    n10 --> n21
    n10 --> n22
    n2 --> n4
    n1 --> n4
    n2 --> n5
    n1 --> n5
    n4 --> n13
    n22 --> n34
    n23 --> n34
    n10 --> n23
    n16 --> n35
    n21 --> n36
    n9 --> n24
    n6 x--x n7
    n41 x--x n42
```

# ISR_legacy_of_the_conference

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ISR_ad_halom"]
        n48["ISR_assume_the_national_cause"]
        n49(("ISR_legacy_of_the_conference"))
        n50["ISR_operation_yoav"]
        n51["ISR_purge_irgun"]
        n52["ISR_the_west_bank"]
    end
    subgraph tier_1["Tier 1"]
        n3{"ISR_form_the_israeli_navy"}
        n4["ISR_provisional_government"]
        n5["ISR_raise_jewish_militias"]
        n2{"ISR_win"}
    end
    subgraph tier_unplaced["Unplaced (cycle)"]
        n25["ISR_Battleship"]
        n26["ISR_Carrier"]
        n37["ISR_Cruisers"]
        n38["ISR_Destroyer"]
        n14["ISR_Dockyards"]
        n47["ISR_Naval_Doctrine"]
        n39["ISR_Navy_Aircrafts"]
        n6["ISR_Sea_Dominance"]
        n27["ISR_Ships_American"]
        n28["ISR_Ships_England"]
        n7["ISR_Small_Navy"]
        n15["ISR_Study_Ships"]
        n16["ISR_Submarine"]
        n53["ISR_abandon_eretz_yisrael"]
        n54["ISR_abandon_jordan"]
        n55["ISR_affirm_territorial_claims"]
        n56["ISR_alone"]
        n57["ISR_am_yisrael_hai"]
        n58["ISR_appeal_middle_class"]
        n59["ISR_appeal_to_diaspora"]
        n60["ISR_appeal_to_haganah"]
        n61["ISR_appeal_west"]
        n62["ISR_appease_religious"]
        n63["ISR_arab_recruitment"]
        n40["ISR_armored_vehicles"]
        n64["ISR_arms_sourcing"]
        n65["ISR_avenge_tragedies"]
        n66["ISR_begin_nationalization"]
        n67["ISR_begin_takes_over"]
        n68["ISR_ben_gurion_stays"]
        n69{"ISR_best_of_the_best"}
        n70["ISR_betar_revived"]
        n41["ISR_bimotor_aircrafts"]
        n71["ISR_brighter_future"]
        n72["ISR_build_third_temple"]
        n42["ISR_build_trainer_aircrafts"]
        n8["ISR_building_the_new_homeland"]
        n73["ISR_campaign_women"]
        n74["ISR_cement_five_mems"]
        n75["ISR_cement_histadrut_powers"]
        n76["ISR_cement_jewish_identity"]
        n77["ISR_centralization"]
        n78{"ISR_centre"}
        n79["ISR_centre_victorious"]
        n80["ISR_clean_resistance"]
        n81["ISR_consolidate_power"]
        n82{"ISR_convene_knesset"}
        n83["ISR_cooperate_maki"]
        n84["ISR_cooperate_religious"]
        n85["ISR_crown_of_david"]
        n86["ISR_demand_secular_education"]
        n87["ISR_destroy_nazi"]
        n88{"ISR_develop_gush_dan"}
        n89["ISR_develop_negev"]
        n90["ISR_develop_road_infrastructure"]
        n91["ISR_draft_constitution"]
        n92["ISR_economic_liberalisation"]
        n93["ISR_education_reforms"]
        n94["ISR_elect_president"]
        n95["ISR_empower_stern_gang"]
        n96["ISR_end_austerity"]
        n17["ISR_equipment_modernization"]
        n29["ISR_establish_a_military_academy"]
        n97["ISR_establish_bituah_leumi"]
        n98["ISR_exempt_yeshiva_students"]
        n99["ISR_expand_immigrant_infrastructure"]
        n100["ISR_expand_industrial_hubs"]
        n101["ISR_expand_rural_influence"]
        n102{"ISR_expand_settlement"}
        n103["ISR_expand_support_uses"]
        n104["ISR_factory_investments"]
        n105["ISR_fight_resistance"]
        n30["ISR_firearms_production"]
        n106["ISR_fix_bureaucracy"]
        n107["ISR_foreign_experts"]
        n108["ISR_form_DLN"]
        n9["ISR_form_the_mossad"]
        n43["ISR_form_the_techni"]
        n10["ISR_formalize_military"]
        n109["ISR_fund_religious_education"]
        n110["ISR_fund_urban_areas"]
        n111["ISR_further_industry_expansions"]
        n112["ISR_further_palestinian_negotiations"]
        n113["ISR_galilee_development"]
        n114["ISR_gather_outside_support"]
        n115["ISR_gather_the_loyalists"]
        n116["ISR_general_zionists"]
        n117{"ISR_hashomer"}
        n118["ISR_hashomer_leads"]
        n119{"ISR_hatzohar"}
        n120["ISR_herzl_followers"]
        n121["ISR_herzl_successor"]
        n122["ISR_histadrut_legislation"]
        n123["ISR_histardrut_deregulation"]
        n124["ISR_increase_urban_investments"]
        n31["ISR_independent_steel_production"]
        n44["ISR_industrial_expansion_plan"]
        n125["ISR_into_the_desert"]
        n126["ISR_invest_in_kibbutzim"]
        n127["ISR_invest_in_white_collar"]
        n128["ISR_iranian_alliance"]
        n129["ISR_irgun_in_power"]
        n11["ISR_israel_military_industries"]
        n32{"ISR_israeli_air_school"}
        n45["ISR_issue_the_israeli_lira"]
        n130["ISR_jabotinsky_death"]
        n131["ISR_join_ENG"]
        n132["ISR_join_ITA"]
        n133["ISR_join_SOV"]
        n134["ISR_join_USA"]
        n135["ISR_join_fascists"]
        n136["ISR_join_soviet"]
        n137["ISR_joint_military_exercises"]
        n138["ISR_judea_fell"]
        n139["ISR_judea_rise"]
        n18["ISR_kibbutz_production"]
        n140{"ISR_kill_stern"}
        n19["ISR_land_reclamation"]
        n141["ISR_lean_hatzohar"]
        n142["ISR_lean_mapai"]
        n143{"ISR_legacy_of_basel"}
        n144["ISR_lessen_austerity"]
        n145["ISR_lessen_soviet_stance"]
        n146["ISR_levantine_commune"]
        n147["ISR_limited_austerity"]
        n148{"ISR_limited_return"}
        n20["ISR_link_communities"]
        n149{"ISR_mapai"}
        n150["ISR_mapai_cemented"]
        n151["ISR_mapai_hashomer"]
        n152{"ISR_martial_law"}
        n153["ISR_merge_unions"]
        n154["ISR_middle_class_investments"]
        n33["ISR_military_vehicles"]
        n46["ISR_modern_logistics"]
        n155{"ISR_moses_hess_legacy"}
        n12["ISR_national_higher_education"]
        n156["ISR_negotiate_lehi_defectors"]
        n157{"ISR_nile_to_euphrates"}
        n158{"ISR_only_thus"}
        n159["ISR_open_economy"]
        n160["ISR_operation_ezra_nehamiah"]
        n161["ISR_operation_magic_carpet"]
        n162["ISR_our_rightful_land"]
        n163["ISR_palestinian_compromises"]
        n164["ISR_partition_syria"]
        n165["ISR_periphery_investments"]
        n21["ISR_plane_imports"]
        n22["ISR_proffesional_army_training"]
        n166["ISR_progressives"]
        n167["ISR_promise_arabs"]
        n168["ISR_promote_electronic_developments"]
        n169["ISR_promote_urban"]
        n170["ISR_push_jewish"]
        n171["ISR_push_militarism"]
        n172["ISR_push_military_industries"]
        n173["ISR_push_secular"]
        n174["ISR_push_secular_education"]
        n13["ISR_reading_power_station"]
        n175["ISR_recognize_beduin"]
        n176["ISR_reconciliation"]
        n177["ISR_reject_lesser_israel"]
        n178["ISR_revisionist_revolution"]
        n179["ISR_schizo_nazbol"]
        n180{"ISR_secularize_public_laws"}
        n181["ISR_seize_foreign_assets"]
        n182["ISR_seize_lebanon"]
        n183["ISR_settlement_projects"]
        n184["ISR_setup_public_transit"]
        n185["ISR_sharett_diplomacy"]
        n186["ISR_sharett_reforms"]
        n187["ISR_sharett_takes_over"]
        n188{"ISR_shearim"}
        n189["ISR_shift_rightwards"]
        n190["ISR_soviet_cooperation"]
        n191["ISR_soviet_support"]
        n34["ISR_special_forces"]
        n23["ISR_special_night_squads"]
        n192["ISR_status_quo_agreement"]
        n193["ISR_status_quo_arabs"]
        n194["ISR_steady"]
        n35["ISR_stealth_upgrades"]
        n195{"ISR_stern_cult"}
        n196["ISR_strengthen_maki"]
        n197["ISR_strengthen_military_industrial"]
        n198["ISR_strengthen_progressives"]
        n199["ISR_strengthen_union"]
        n200["ISR_strike_egypt"]
        n201["ISR_strike_infrastructure"]
        n202["ISR_support_irgun_fighters"]
        n203["ISR_support_maronite_lebanese"]
        n204["ISR_syria_war"]
        n205["ISR_tax_reforms"]
        n206{"ISR_the_ageing_father"}
        n207["ISR_the_east_bank"]
        n208["ISR_the_elections"]
        n209["ISR_the_five_mems"]
        n210{"ISR_the_italian_model"}
        n211{"ISR_the_periphery_strategy"}
        n212["ISR_the_religious_front"]
        n213{"ISR_the_revisionist_split"}
        n214["ISR_to_the_euphrates"]
        n215["ISR_to_the_suez"]
        n216["ISR_toe_line"]
        n217{"ISR_turkish_alliance"}
        n218["ISR_two_state_solution"]
        n219["ISR_undo_austerity"]
        n36["ISR_volunteer_pilots"]
        n220["ISR_watch_yishuv_leaders"]
        n221["ISR_weaken_histadrut"]
        n222["ISR_welfare_for_refugees"]
        n223["ISR_womens_rights"]
        n224["ISR_work_with_arab"]
        n24["ISR_world_wide_spy_web"]
        n225{"ISR_yodefet_masada_betar"}
    end
    n14 --> n25
    n14 --> n26
    n25 --> n37
    n26 --> n37
    n25 --> n38
    n26 --> n38
    n7 --> n14
    n6 --> n14
    n37 --> n47
    n38 --> n47
    n25 --> n47
    n26 --> n39
    n3 --> n6
    n15 --> n27
    n15 --> n28
    n3 --> n7
    n6 --> n15
    n7 --> n16
    n152 --> n53
    n102 --> n53
    n119 --> n54
    n119 --> n55
    n188 --> n56
    n155 --> n56
    n143 --> n56
    n225 --> n56
    n91 --> n57
    n56 --> n57
    n133 --> n57
    n131 --> n57
    n134 --> n57
    n132 --> n57
    n78 --> n58
    n127 --> n59
    n174 --> n59
    n115 --> n60
    n150 --> n61
    n79 --> n61
    n178 --> n61
    n149 --> n62
    n77 --> n63
    n33 --> n40
    n31 --> n40
    n138 --> n64
    n201 --> n65
    n114 --> n65
    n150 --> n66
    n74 --> n67
    n206 --> n68
    n168 --> n69
    n124 --> n69
    n84 --> n70
    n202 --> n70
    n54 --> n70
    n55 --> n70
    n32 --> n41
    n101 --> n71
    n167 --> n71
    n145 --> n71
    n83 --> n71
    n195 --> n72
    n32 --> n42
    n4 --> n8
    n78 --> n73
    n76 --> n74
    n221 --> n74
    n159 --> n74
    n66 --> n75
    n209 --> n76
    n190 --> n77
    n100 --> n77
    n82 --> n78
    n208 --> n79
    n138 --> n80
    n105 --> n81
    n2 --> n82
    n117 --> n83
    n119 --> n84
    n60 --> n85
    n156 --> n85
    n149 --> n86
    n57 --> n87
    n90 --> n88
    n68 --> n89
    n116 --> n90
    n94 --> n91
    n219 --> n92
    n66 --> n93
    n118 --> n94
    n150 --> n94
    n79 --> n94
    n178 --> n94
    n213 --> n95
    n81 --> n96
    n11 --> n17
    n23 --> n29
    n17 --> n29
    n66 --> n97
    n109 --> n98
    n59 --> n99
    n196 --> n100
    n117 --> n101
    n177 --> n102
    n64 --> n103
    n96 --> n104
    n122 --> n104
    n129 --> n105
    n18 --> n30
    n216 --> n106
    n219 --> n107
    n149 --> n108
    n2 --> n3
    n1 --> n3
    n4 --> n9
    n32 --> n43
    n5 --> n10
    n212 --> n109
    n68 --> n110
    n123 --> n111
    n205 --> n111
    n187 --> n112
    n126 --> n113
    n95 --> n114
    n213 --> n115
    n208 --> n116
    n82 --> n117
    n208 --> n118
    n82 --> n119
    n73 --> n120
    n58 --> n120
    n141 --> n120
    n142 --> n120
    n110 --> n121
    n89 --> n121
    n81 --> n122
    n189 --> n123
    n92 --> n124
    n18 --> n31
    n30 --> n44
    n31 --> n44
    n204 --> n125
    n182 --> n125
    n216 --> n126
    n198 --> n127
    n211 --> n128
    n2 --> n129
    n5 --> n11
    n21 --> n32
    n31 --> n45
    n81 --> n130
    n188 --> n131
    n155 --> n131
    n143 --> n131
    n225 --> n131
    n225 --> n132
    n188 --> n133
    n188 --> n134
    n155 --> n134
    n143 --> n134
    n225 --> n134
    n195 --> n135
    n140 --> n135
    n179 --> n136
    n210 --> n137
    n85 --> n138
    n203 --> n139
    n164 --> n139
    n8 --> n18
    n157 --> n140
    n8 --> n19
    n78 --> n141
    n78 --> n142
    n193 --> n143
    n154 --> n143
    n99 --> n143
    n97 --> n144
    n75 --> n144
    n93 --> n144
    n117 --> n145
    n63 --> n146
    n153 --> n146
    n199 --> n147
    n147 --> n148
    n191 --> n148
    n8 --> n20
    n82 --> n149
    n208 --> n150
    n208 --> n151
    n177 --> n152
    n77 --> n153
    n111 --> n154
    n20 --> n33
    n11 --> n33
    n33 --> n46
    n29 --> n46
    n160 --> n155
    n121 --> n155
    n185 --> n155
    n4 --> n12
    n115 --> n156
    n65 --> n157
    n138 --> n158
    n103 --> n158
    n181 --> n158
    n183 --> n158
    n80 --> n158
    n165 --> n159
    n68 --> n160
    n187 --> n160
    n144 --> n161
    n152 --> n162
    n102 --> n162
    n144 --> n163
    n217 --> n164
    n209 --> n165
    n10 --> n21
    n10 --> n22
    n208 --> n166
    n117 --> n167
    n107 --> n168
    n149 --> n169
    n2 --> n4
    n1 --> n4
    n81 --> n170
    n170 --> n171
    n220 --> n171
    n209 --> n172
    n151 --> n173
    n198 --> n174
    n2 --> n5
    n1 --> n5
    n4 --> n13
    n176 --> n175
    n216 --> n176
    n67 --> n177
    n208 --> n178
    n140 --> n179
    n223 --> n180
    n197 --> n181
    n207 --> n182
    n138 --> n183
    n150 --> n184
    n118 --> n184
    n186 --> n185
    n112 --> n185
    n187 --> n186
    n206 --> n187
    n218 --> n188
    n146 --> n188
    n69 --> n189
    n88 --> n189
    n196 --> n190
    n199 --> n191
    n22 --> n34
    n23 --> n34
    n10 --> n23
    n98 --> n192
    n198 --> n193
    n189 --> n193
    n169 --> n194
    n108 --> n194
    n62 --> n194
    n86 --> n194
    n16 --> n35
    n157 --> n195
    n148 --> n196
    n138 --> n197
    n69 --> n198
    n180 --> n198
    n118 --> n199
    n210 --> n200
    n95 --> n201
    n119 --> n202
    n210 --> n203
    n211 --> n203
    n207 --> n204
    n189 --> n205
    n163 --> n206
    n161 --> n206
    n195 --> n207
    n140 --> n207
    n70 --> n208
    n120 --> n208
    n194 --> n208
    n71 --> n208
    n178 --> n209
    n158 --> n210
    n158 --> n211
    n208 --> n212
    n130 --> n213
    n204 --> n214
    n182 --> n215
    n148 --> n216
    n211 --> n217
    n224 --> n218
    n175 --> n218
    n79 --> n219
    n21 --> n36
    n81 --> n220
    n172 --> n221
    n150 --> n222
    n118 --> n222
    n51 --> n2
    n48 --> n2
    n49 --> n2
    n50 --> n2
    n52 --> n2
    n49 --> n2
    n166 --> n223
    n176 --> n224
    n113 --> n224
    n9 --> n24
    n162 --> n225
    n53 --> n225
    n6 x--x n7
    n53 x--x n162
    n54 x--x n55
    n56 x--x n131
    n56 x--x n132
    n56 x--x n133
    n56 x--x n134
    n62 x--x n86
    n68 x--x n187
    n41 x--x n42
    n78 x--x n117
    n78 x--x n119
    n78 x--x n149
    n82 x--x n129
    n83 x--x n145
    n95 x--x n115
    n117 x--x n119
    n117 x--x n149
    n119 x--x n149
    n131 x--x n132
    n131 x--x n133
    n131 x--x n134
    n132 x--x n133
    n132 x--x n134
    n133 x--x n134
    n135 x--x n179
    n140 x--x n195
    n141 x--x n142
    n164 x--x n203
    n189 x--x n198
    n196 x--x n216
    n210 x--x n211
```

# ISR_revolution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ISR_ad_halom"]
        n49["ISR_legacy_of_the_conference"]
        n226(("ISR_revolution"))
    end
    subgraph tier_1["Tier 1"]
        n227{"ISR_call_diaspora_volunteers"}
        n3{"ISR_form_the_israeli_navy"}
        n4["ISR_provisional_government"]
        n5["ISR_raise_jewish_militias"]
    end
    subgraph tier_2["Tier 2"]
        n228["ISR_consolidate_haganah"]
        n229["ISR_gather_irgun"]
    end
    subgraph tier_3["Tier 3"]
        n230["ISR_begin_approach"]
        n231["ISR_ben_gurion_strategy"]
        n232["ISR_czech_weaponry"]
        n233["ISR_dealing_with_irgun"]
        n234["ISR_subvert_haganah"]
    end
    subgraph tier_4["Tier 4"]
        n235["ISR_form_the_idf"]
        n236["ISR_jerusalem_strategy"]
        n237["ISR_southern_plan"]
        n238["ISR_spread_revisionist_media"]
        n239["ISR_steal_haganah_weapons"]
        n240["ISR_subvert_irgun_influence"]
    end
    subgraph tier_5["Tier 5"]
        n48["ISR_assume_the_national_cause"]
        n50["ISR_operation_yoav"]
        n51["ISR_purge_irgun"]
        n52["ISR_the_west_bank"]
    end
    subgraph tier_6["Tier 6"]
        n2{"ISR_win"}
    end
    subgraph tier_unplaced["Unplaced (cycle)"]
        n25["ISR_Battleship"]
        n26["ISR_Carrier"]
        n37["ISR_Cruisers"]
        n38["ISR_Destroyer"]
        n14["ISR_Dockyards"]
        n47["ISR_Naval_Doctrine"]
        n39["ISR_Navy_Aircrafts"]
        n6["ISR_Sea_Dominance"]
        n27["ISR_Ships_American"]
        n28["ISR_Ships_England"]
        n7["ISR_Small_Navy"]
        n15["ISR_Study_Ships"]
        n16["ISR_Submarine"]
        n53["ISR_abandon_eretz_yisrael"]
        n54["ISR_abandon_jordan"]
        n55["ISR_affirm_territorial_claims"]
        n56["ISR_alone"]
        n57["ISR_am_yisrael_hai"]
        n58["ISR_appeal_middle_class"]
        n59["ISR_appeal_to_diaspora"]
        n60["ISR_appeal_to_haganah"]
        n61["ISR_appeal_west"]
        n62["ISR_appease_religious"]
        n63["ISR_arab_recruitment"]
        n40["ISR_armored_vehicles"]
        n64["ISR_arms_sourcing"]
        n65["ISR_avenge_tragedies"]
        n66["ISR_begin_nationalization"]
        n67["ISR_begin_takes_over"]
        n68["ISR_ben_gurion_stays"]
        n69{"ISR_best_of_the_best"}
        n70["ISR_betar_revived"]
        n41["ISR_bimotor_aircrafts"]
        n71["ISR_brighter_future"]
        n72["ISR_build_third_temple"]
        n42["ISR_build_trainer_aircrafts"]
        n8["ISR_building_the_new_homeland"]
        n73["ISR_campaign_women"]
        n74["ISR_cement_five_mems"]
        n75["ISR_cement_histadrut_powers"]
        n76["ISR_cement_jewish_identity"]
        n77["ISR_centralization"]
        n78{"ISR_centre"}
        n79["ISR_centre_victorious"]
        n80["ISR_clean_resistance"]
        n81["ISR_consolidate_power"]
        n82{"ISR_convene_knesset"}
        n83["ISR_cooperate_maki"]
        n84["ISR_cooperate_religious"]
        n85["ISR_crown_of_david"]
        n86["ISR_demand_secular_education"]
        n87["ISR_destroy_nazi"]
        n88{"ISR_develop_gush_dan"}
        n89["ISR_develop_negev"]
        n90["ISR_develop_road_infrastructure"]
        n91["ISR_draft_constitution"]
        n92["ISR_economic_liberalisation"]
        n93["ISR_education_reforms"]
        n94["ISR_elect_president"]
        n95["ISR_empower_stern_gang"]
        n96["ISR_end_austerity"]
        n17["ISR_equipment_modernization"]
        n29["ISR_establish_a_military_academy"]
        n97["ISR_establish_bituah_leumi"]
        n98["ISR_exempt_yeshiva_students"]
        n99["ISR_expand_immigrant_infrastructure"]
        n100["ISR_expand_industrial_hubs"]
        n101["ISR_expand_rural_influence"]
        n102{"ISR_expand_settlement"}
        n103["ISR_expand_support_uses"]
        n104["ISR_factory_investments"]
        n105["ISR_fight_resistance"]
        n30["ISR_firearms_production"]
        n106["ISR_fix_bureaucracy"]
        n107["ISR_foreign_experts"]
        n108["ISR_form_DLN"]
        n9["ISR_form_the_mossad"]
        n43["ISR_form_the_techni"]
        n10["ISR_formalize_military"]
        n109["ISR_fund_religious_education"]
        n110["ISR_fund_urban_areas"]
        n111["ISR_further_industry_expansions"]
        n112["ISR_further_palestinian_negotiations"]
        n113["ISR_galilee_development"]
        n114["ISR_gather_outside_support"]
        n115["ISR_gather_the_loyalists"]
        n116["ISR_general_zionists"]
        n117{"ISR_hashomer"}
        n118["ISR_hashomer_leads"]
        n119{"ISR_hatzohar"}
        n120["ISR_herzl_followers"]
        n121["ISR_herzl_successor"]
        n122["ISR_histadrut_legislation"]
        n123["ISR_histardrut_deregulation"]
        n124["ISR_increase_urban_investments"]
        n31["ISR_independent_steel_production"]
        n44["ISR_industrial_expansion_plan"]
        n125["ISR_into_the_desert"]
        n126["ISR_invest_in_kibbutzim"]
        n127["ISR_invest_in_white_collar"]
        n128["ISR_iranian_alliance"]
        n129["ISR_irgun_in_power"]
        n11["ISR_israel_military_industries"]
        n32{"ISR_israeli_air_school"}
        n45["ISR_issue_the_israeli_lira"]
        n130["ISR_jabotinsky_death"]
        n131["ISR_join_ENG"]
        n132["ISR_join_ITA"]
        n133["ISR_join_SOV"]
        n134["ISR_join_USA"]
        n135["ISR_join_fascists"]
        n136["ISR_join_soviet"]
        n137["ISR_joint_military_exercises"]
        n138["ISR_judea_fell"]
        n139["ISR_judea_rise"]
        n18["ISR_kibbutz_production"]
        n140{"ISR_kill_stern"}
        n19["ISR_land_reclamation"]
        n141["ISR_lean_hatzohar"]
        n142["ISR_lean_mapai"]
        n143{"ISR_legacy_of_basel"}
        n144["ISR_lessen_austerity"]
        n145["ISR_lessen_soviet_stance"]
        n146["ISR_levantine_commune"]
        n147["ISR_limited_austerity"]
        n148{"ISR_limited_return"}
        n20["ISR_link_communities"]
        n149{"ISR_mapai"}
        n150["ISR_mapai_cemented"]
        n151["ISR_mapai_hashomer"]
        n152{"ISR_martial_law"}
        n153["ISR_merge_unions"]
        n154["ISR_middle_class_investments"]
        n33["ISR_military_vehicles"]
        n46["ISR_modern_logistics"]
        n155{"ISR_moses_hess_legacy"}
        n12["ISR_national_higher_education"]
        n156["ISR_negotiate_lehi_defectors"]
        n157{"ISR_nile_to_euphrates"}
        n158{"ISR_only_thus"}
        n159["ISR_open_economy"]
        n160["ISR_operation_ezra_nehamiah"]
        n161["ISR_operation_magic_carpet"]
        n162["ISR_our_rightful_land"]
        n163["ISR_palestinian_compromises"]
        n164["ISR_partition_syria"]
        n165["ISR_periphery_investments"]
        n21["ISR_plane_imports"]
        n22["ISR_proffesional_army_training"]
        n166["ISR_progressives"]
        n167["ISR_promise_arabs"]
        n168["ISR_promote_electronic_developments"]
        n169["ISR_promote_urban"]
        n170["ISR_push_jewish"]
        n171["ISR_push_militarism"]
        n172["ISR_push_military_industries"]
        n173["ISR_push_secular"]
        n174["ISR_push_secular_education"]
        n13["ISR_reading_power_station"]
        n175["ISR_recognize_beduin"]
        n176["ISR_reconciliation"]
        n177["ISR_reject_lesser_israel"]
        n178["ISR_revisionist_revolution"]
        n179["ISR_schizo_nazbol"]
        n180{"ISR_secularize_public_laws"}
        n181["ISR_seize_foreign_assets"]
        n182["ISR_seize_lebanon"]
        n183["ISR_settlement_projects"]
        n184["ISR_setup_public_transit"]
        n185["ISR_sharett_diplomacy"]
        n186["ISR_sharett_reforms"]
        n187["ISR_sharett_takes_over"]
        n188{"ISR_shearim"}
        n189["ISR_shift_rightwards"]
        n190["ISR_soviet_cooperation"]
        n191["ISR_soviet_support"]
        n34["ISR_special_forces"]
        n23["ISR_special_night_squads"]
        n192["ISR_status_quo_agreement"]
        n193["ISR_status_quo_arabs"]
        n194["ISR_steady"]
        n35["ISR_stealth_upgrades"]
        n195{"ISR_stern_cult"}
        n196["ISR_strengthen_maki"]
        n197["ISR_strengthen_military_industrial"]
        n198["ISR_strengthen_progressives"]
        n199["ISR_strengthen_union"]
        n200["ISR_strike_egypt"]
        n201["ISR_strike_infrastructure"]
        n202["ISR_support_irgun_fighters"]
        n203["ISR_support_maronite_lebanese"]
        n204["ISR_syria_war"]
        n205["ISR_tax_reforms"]
        n206{"ISR_the_ageing_father"}
        n207["ISR_the_east_bank"]
        n208["ISR_the_elections"]
        n209["ISR_the_five_mems"]
        n210{"ISR_the_italian_model"}
        n211{"ISR_the_periphery_strategy"}
        n212["ISR_the_religious_front"]
        n213{"ISR_the_revisionist_split"}
        n214["ISR_to_the_euphrates"]
        n215["ISR_to_the_suez"]
        n216["ISR_toe_line"]
        n217{"ISR_turkish_alliance"}
        n218["ISR_two_state_solution"]
        n219["ISR_undo_austerity"]
        n36["ISR_volunteer_pilots"]
        n220["ISR_watch_yishuv_leaders"]
        n221["ISR_weaken_histadrut"]
        n222["ISR_welfare_for_refugees"]
        n223["ISR_womens_rights"]
        n224["ISR_work_with_arab"]
        n24["ISR_world_wide_spy_web"]
        n225{"ISR_yodefet_masada_betar"}
    end
    n14 --> n25
    n14 --> n26
    n25 --> n37
    n26 --> n37
    n25 --> n38
    n26 --> n38
    n7 --> n14
    n6 --> n14
    n37 --> n47
    n38 --> n47
    n25 --> n47
    n26 --> n39
    n3 --> n6
    n15 --> n27
    n15 --> n28
    n3 --> n7
    n6 --> n15
    n7 --> n16
    n152 --> n53
    n102 --> n53
    n119 --> n54
    n119 --> n55
    n188 --> n56
    n155 --> n56
    n143 --> n56
    n225 --> n56
    n91 --> n57
    n56 --> n57
    n133 --> n57
    n131 --> n57
    n134 --> n57
    n132 --> n57
    n78 --> n58
    n127 --> n59
    n174 --> n59
    n115 --> n60
    n150 --> n61
    n79 --> n61
    n178 --> n61
    n149 --> n62
    n77 --> n63
    n33 --> n40
    n31 --> n40
    n138 --> n64
    n239 --> n48
    n238 --> n48
    n201 --> n65
    n114 --> n65
    n229 --> n230
    n150 --> n66
    n74 --> n67
    n206 --> n68
    n228 --> n231
    n168 --> n69
    n124 --> n69
    n84 --> n70
    n202 --> n70
    n54 --> n70
    n55 --> n70
    n32 --> n41
    n101 --> n71
    n167 --> n71
    n145 --> n71
    n83 --> n71
    n195 --> n72
    n32 --> n42
    n4 --> n8
    n226 --> n227
    n78 --> n73
    n76 --> n74
    n221 --> n74
    n159 --> n74
    n66 --> n75
    n209 --> n76
    n190 --> n77
    n100 --> n77
    n82 --> n78
    n208 --> n79
    n138 --> n80
    n227 --> n228
    n105 --> n81
    n2 --> n82
    n117 --> n83
    n119 --> n84
    n60 --> n85
    n156 --> n85
    n228 --> n232
    n229 --> n232
    n228 --> n233
    n149 --> n86
    n57 --> n87
    n90 --> n88
    n68 --> n89
    n116 --> n90
    n94 --> n91
    n219 --> n92
    n66 --> n93
    n118 --> n94
    n150 --> n94
    n79 --> n94
    n178 --> n94
    n213 --> n95
    n81 --> n96
    n11 --> n17
    n23 --> n29
    n17 --> n29
    n66 --> n97
    n109 --> n98
    n59 --> n99
    n196 --> n100
    n117 --> n101
    n177 --> n102
    n64 --> n103
    n96 --> n104
    n122 --> n104
    n129 --> n105
    n18 --> n30
    n216 --> n106
    n219 --> n107
    n149 --> n108
    n233 --> n235
    n2 --> n3
    n1 --> n3
    n4 --> n9
    n32 --> n43
    n5 --> n10
    n212 --> n109
    n68 --> n110
    n123 --> n111
    n205 --> n111
    n187 --> n112
    n126 --> n113
    n227 --> n229
    n95 --> n114
    n213 --> n115
    n208 --> n116
    n82 --> n117
    n208 --> n118
    n82 --> n119
    n73 --> n120
    n58 --> n120
    n141 --> n120
    n142 --> n120
    n110 --> n121
    n89 --> n121
    n81 --> n122
    n189 --> n123
    n92 --> n124
    n18 --> n31
    n30 --> n44
    n31 --> n44
    n204 --> n125
    n182 --> n125
    n216 --> n126
    n198 --> n127
    n211 --> n128
    n2 --> n129
    n5 --> n11
    n21 --> n32
    n31 --> n45
    n81 --> n130
    n230 --> n236
    n188 --> n131
    n155 --> n131
    n143 --> n131
    n225 --> n131
    n225 --> n132
    n188 --> n133
    n188 --> n134
    n155 --> n134
    n143 --> n134
    n225 --> n134
    n195 --> n135
    n140 --> n135
    n179 --> n136
    n210 --> n137
    n85 --> n138
    n203 --> n139
    n164 --> n139
    n8 --> n18
    n157 --> n140
    n8 --> n19
    n78 --> n141
    n78 --> n142
    n193 --> n143
    n154 --> n143
    n99 --> n143
    n97 --> n144
    n75 --> n144
    n93 --> n144
    n117 --> n145
    n63 --> n146
    n153 --> n146
    n199 --> n147
    n147 --> n148
    n191 --> n148
    n8 --> n20
    n82 --> n149
    n208 --> n150
    n208 --> n151
    n177 --> n152
    n77 --> n153
    n111 --> n154
    n20 --> n33
    n11 --> n33
    n33 --> n46
    n29 --> n46
    n160 --> n155
    n121 --> n155
    n185 --> n155
    n4 --> n12
    n115 --> n156
    n65 --> n157
    n138 --> n158
    n103 --> n158
    n181 --> n158
    n183 --> n158
    n80 --> n158
    n165 --> n159
    n68 --> n160
    n187 --> n160
    n144 --> n161
    n237 --> n50
    n235 --> n50
    n152 --> n162
    n102 --> n162
    n144 --> n163
    n217 --> n164
    n209 --> n165
    n10 --> n21
    n10 --> n22
    n208 --> n166
    n117 --> n167
    n107 --> n168
    n149 --> n169
    n2 --> n4
    n1 --> n4
    n235 --> n51
    n240 --> n51
    n81 --> n170
    n170 --> n171
    n220 --> n171
    n209 --> n172
    n151 --> n173
    n198 --> n174
    n2 --> n5
    n1 --> n5
    n4 --> n13
    n176 --> n175
    n216 --> n176
    n67 --> n177
    n208 --> n178
    n140 --> n179
    n223 --> n180
    n197 --> n181
    n207 --> n182
    n138 --> n183
    n150 --> n184
    n118 --> n184
    n186 --> n185
    n112 --> n185
    n187 --> n186
    n206 --> n187
    n218 --> n188
    n146 --> n188
    n69 --> n189
    n88 --> n189
    n231 --> n237
    n196 --> n190
    n199 --> n191
    n22 --> n34
    n23 --> n34
    n10 --> n23
    n234 --> n238
    n98 --> n192
    n198 --> n193
    n189 --> n193
    n169 --> n194
    n108 --> n194
    n62 --> n194
    n86 --> n194
    n234 --> n239
    n16 --> n35
    n157 --> n195
    n148 --> n196
    n138 --> n197
    n69 --> n198
    n180 --> n198
    n118 --> n199
    n210 --> n200
    n95 --> n201
    n229 --> n234
    n233 --> n240
    n119 --> n202
    n210 --> n203
    n211 --> n203
    n207 --> n204
    n189 --> n205
    n163 --> n206
    n161 --> n206
    n195 --> n207
    n140 --> n207
    n70 --> n208
    n120 --> n208
    n194 --> n208
    n71 --> n208
    n178 --> n209
    n158 --> n210
    n158 --> n211
    n208 --> n212
    n130 --> n213
    n236 --> n52
    n239 --> n52
    n204 --> n214
    n182 --> n215
    n148 --> n216
    n211 --> n217
    n224 --> n218
    n175 --> n218
    n79 --> n219
    n21 --> n36
    n81 --> n220
    n172 --> n221
    n150 --> n222
    n118 --> n222
    n51 --> n2
    n48 --> n2
    n49 --> n2
    n50 --> n2
    n52 --> n2
    n49 --> n2
    n166 --> n223
    n176 --> n224
    n113 --> n224
    n9 --> n24
    n162 --> n225
    n53 --> n225
    n6 x--x n7
    n53 x--x n162
    n54 x--x n55
    n56 x--x n131
    n56 x--x n132
    n56 x--x n133
    n56 x--x n134
    n62 x--x n86
    n68 x--x n187
    n41 x--x n42
    n78 x--x n117
    n78 x--x n119
    n78 x--x n149
    n228 x--x n229
    n82 x--x n129
    n83 x--x n145
    n95 x--x n115
    n117 x--x n119
    n117 x--x n149
    n119 x--x n149
    n131 x--x n132
    n131 x--x n133
    n131 x--x n134
    n132 x--x n133
    n132 x--x n134
    n133 x--x n134
    n135 x--x n179
    n140 x--x n195
    n141 x--x n142
    n164 x--x n203
    n189 x--x n198
    n196 x--x n216
    n210 x--x n211
```

# ISR_suez_crisis

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n241(("ISR_suez_crisis"))
    end
    subgraph tier_1["Tier 1"]
        n242["ISR_appeal_to_france"]
        n243["ISR_appeal_to_uk"]
    end
    subgraph tier_2["Tier 2"]
        n244["ISR_prepare_the_invasion"]
    end
    subgraph tier_3["Tier 3"]
        n245["ISR_operation_sinai"]
    end
    subgraph tier_4["Tier 4"]
        n246{"ISR_a_resounding_victory"}
    end
    subgraph tier_5["Tier 5"]
        n247["ISR_one_zion"]
        n248["ISR_stretch_out_the_hand"]
    end
    n245 --> n246
    n241 --> n242
    n241 --> n243
    n246 --> n247
    n244 --> n245
    n243 --> n244
    n242 --> n244
    n246 --> n248
    n247 x--x n248
```
