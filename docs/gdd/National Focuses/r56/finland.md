# FIN_enhance_southern_infrastructure

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("FIN_enhance_southern_infrastructure"))
        n2["FIN_industrial_upgrade_in_harjavalta"]
        n3["FIN_outokumpu_for_defence_industry"]
    end
    subgraph tier_1["Tier 1"]
        n4["FIN_industrial_development"]
    end
    subgraph tier_2["Tier 2"]
        n5["FIN_bank_of_aland"]
        n6["FIN_janiskoski_power_plant"]
        n7["FIN_tire_factory_at_nokia"]
        n8["FIN_vaisala_radiosonde_tests"]
    end
    subgraph tier_3["Tier 3"]
        n9["FIN_contract_with_yhteissisu"]
        n10["FIN_expand_imatra_hydropower_plant"]
        n11["FIN_found_pohjolan_voima"]
        n12["FIN_suomen_akatemia"]
    end
    subgraph tier_4["Tier 4"]
        n13["FIN_expand_mining_prospection"]
        n14["FIN_makola_mine"]
        n15["FIN_power_from_the_dams"]
    end
    subgraph tier_5["Tier 5"]
        n16["FIN_elijarvi_mine"]
    end
    subgraph tier_6["Tier 6"]
        n17["FIN_tornio_steel_factory"]
    end
    n4 --> n5
    n7 --> n9
    n3 --> n9
    n13 --> n16
    n6 --> n10
    n10 --> n13
    n2 --> n13
    n6 --> n11
    n1 --> n4
    n4 --> n6
    n10 --> n14
    n10 --> n15
    n5 --> n12
    n4 --> n7
    n16 --> n17
    n4 --> n8
```

# FIN_finnish_neutrality

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18{"FIN_finnish_neutrality"}
        n19["FIN_keepers_of_the_north"]
        n20["FIN_right_wing_policies"]
        n21["FIN_seek_german_protection"]
        n22["FIN_social_democracy"]
        n23{"FIN_suomalainen_sosialismi"}
        n24{"fin_comfoc"}
        n25["fin_demcomunbanfoc"]
        n26["fin_greatfinfoc"]
        n27["fin_nationalismfoc"]
    end
    subgraph tier_1["Tier 1"]
        n28{"FIN_national_unity"}
        n29["FIN_political_unity"]
        n30["FIN_reach_out_to_scandinavia"]
        n31["FIN_weapon_caches"]
        n32["fin_karjalafoc"]
        n33["fin_removeclaimfoc"]
    end
    subgraph tier_2["Tier 2"]
        n34["FIN_a_cry_for_help"]
        n35["FIN_align_the_agrarian_league"]
        n36["FIN_arm_the_lotta_svard"]
        n37["FIN_collaboration_with_the_left"]
        n38{"FIN_moderate_politics"}
        n39["FIN_railways_and_infrastructure"]
        n40["FIN_the_finnish_swedish_peoples_party"]
        n41["FIN_viron_kansa"]
    end
    subgraph tier_3["Tier 3"]
        n42["FIN_ambitions_in_the_south"]
        n43["FIN_join_the_allies"]
        n44["FIN_northern_defense_front"]
        n45["FIN_repurpose_small_industries"]
        n46["FIN_the_lone_wolf"]
        n47["FIN_union_of_finnish_brothers_in_arms"]
    end
    subgraph tier_4["Tier 4"]
        n48["FIN_cooperation_with_germany"]
        n49{"FIN_expand_state_military_factories"}
        n50["FIN_industrialize_the_region"]
        n51["FIN_militarized_society"]
        n52["FIN_military_aid"]
        n53["FIN_parmis_devils"]
    end
    subgraph tier_5["Tier 5"]
        n54["FIN_a_new_course_for_kokoomus"]
        n55["FIN_dreams_of_expansionism"]
        n56["FIN_german_military_advisors"]
        n57["FIN_increase_military_investment"]
        n58{"FIN_joint_scientific_program"}
        n59["FIN_mineral_wealth_development"]
        n60["FIN_strengthen_military_administration"]
        n61["FIN_wartsila_engine_production"]
        n62["fin_techengfoc"]
    end
    subgraph tier_6["Tier 6"]
        n63["FIN_finnish_march_of_conquest"]
        n64["FIN_modernize_the_army"]
        n65["FIN_modernize_the_industry"]
        n66["FIN_the_finnish_throne"]
    end
    subgraph tier_7["Tier 7"]
        n67["FIN_greater_finland"]
    end
    n28 --> n34
    n49 --> n54
    n29 --> n35
    n22 --> n35
    n25 --> n35
    n41 --> n42
    n28 --> n36
    n29 --> n37
    n46 --> n48
    n49 --> n55
    n45 --> n49
    n61 --> n63
    n56 --> n63
    n48 --> n56
    n63 --> n67
    n51 --> n67
    n19 --> n67
    n26 --> n67
    n52 --> n57
    n50 --> n57
    n44 --> n50
    n38 --> n43
    n50 --> n58
    n48 --> n58
    n52 --> n58
    n47 --> n51
    n43 --> n52
    n52 --> n59
    n30 --> n38
    n58 --> n64
    n58 --> n65
    n18 --> n28
    n20 --> n28
    n27 --> n28
    n38 --> n44
    n47 --> n53
    n18 --> n29
    n29 --> n39
    n18 --> n30
    n39 --> n45
    n49 --> n60
    n22 --> n40
    n29 --> n40
    n25 --> n40
    n54 --> n66
    n38 --> n46
    n36 --> n47
    n28 --> n41
    n48 --> n61
    n18 --> n31
    n20 --> n31
    n27 --> n31
    n18 --> n32
    n23 --> n32
    n24 --> n32
    n18 --> n33
    n23 --> n33
    n24 --> n33
    n52 --> n62
    n34 x--x n21
    n54 x--x n55
    n54 x--x n60
    n55 x--x n60
    n18 x--x n20
    n18 x--x n23
    n18 x--x n24
    n18 x--x n27
    n43 x--x n44
    n43 x--x n46
    n64 x--x n65
    n44 x--x n46
    n32 x--x n33
```

# FIN_increase_military_budget

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10["FIN_expand_imatra_hydropower_plant"]
        n68(("FIN_increase_military_budget"))
        n7["FIN_tire_factory_at_nokia"]
    end
    subgraph tier_1["Tier 1"]
        n69["FIN_suomen_ilmavoimat"]
        n70["FIN_suomen_maavoimat"]
        n71["FIN_suomen_merivoimat"]
    end
    subgraph tier_2["Tier 2"]
        n72["FIN_acquire_andros_dockyards"]
        n73{"FIN_coastal_defense"}
        n74["FIN_expand_air_bases"]
        n75["FIN_extra_refresher_exercises"]
        n76["FIN_mannerheim_line"]
        n77{"FIN_naval_airforce"}
        n78["FIN_operation_kilpapurjehdus"]
        n3["FIN_outokumpu_for_defence_industry"]
        n79["FIN_pilot_training"]
        n80["FIN_strengthen_the_naval_bases"]
        n81["FIN_the_merchant_fleet"]
        n82["FIN_underground_resistance_cells"]
    end
    subgraph tier_3["Tier 3"]
        n9["FIN_contract_with_yhteissisu"]
        n83["FIN_conversion_of_civilian_vessels"]
        n84["FIN_deep_sea_raiders"]
        n85["FIN_defense_in_depth"]
        n86["FIN_expand_air_force_academy"]
        n87["FIN_expand_ship_building_industry"]
        n88["FIN_foreign_aircraft"]
        n89["FIN_helsinki_air_defense"]
        n2["FIN_industrial_upgrade_in_harjavalta"]
        n90["FIN_integrate_oy_tikkakoski"]
        n91["FIN_jaeger_movement"]
        n92["FIN_marine_jaeger_divisions"]
        n93{"FIN_national_aircraft_production"}
        n94["FIN_oy_alkoholiliike"]
        n95["FIN_rapid_raiders"]
        n96{"FIN_salvaged_and_retooled"}
        n97["FIN_the_cold_front"]
    end
    subgraph tier_4["Tier 4"]
        n98{"FIN_dominate_the_skies"}
        n13["FIN_expand_mining_prospection"]
        n99["FIN_foreign_armor"]
        n100["FIN_motti_tactics"]
        n101["FIN_national_firepower"]
        n102["FIN_salpa_line"]
        n103["FIN_sea_mines_strategy"]
        n104{"FIN_support_for_ground_forces"}
        n105["FIN_winter_warfare"]
    end
    subgraph tier_5["Tier 5"]
        n16["FIN_elijarvi_mine"]
        n106["FIN_expand_production_lines"]
        n107["FIN_expansion_towards_the_atlantic"]
        n108{"FIN_finnish_radio_intelligence"}
        n109{"FIN_long_range_patrols"}
        n110["FIN_modernize_production_lines"]
        n111{"FIN_utilize_the_sami"}
    end
    subgraph tier_6["Tier 6"]
        n112["FIN_national_armor_focus"]
        n113["FIN_sissi"]
        n17["FIN_tornio_steel_factory"]
    end
    subgraph tier_7["Tier 7"]
        n114["FIN_innovative_designs"]
    end
    n71 --> n72
    n71 --> n73
    n7 --> n9
    n3 --> n9
    n81 --> n83
    n73 --> n83
    n73 --> n84
    n76 --> n85
    n93 --> n98
    n13 --> n16
    n69 --> n74
    n79 --> n86
    n10 --> n13
    n2 --> n13
    n104 --> n106
    n98 --> n106
    n80 --> n87
    n72 --> n87
    n103 --> n107
    n87 --> n107
    n70 --> n75
    n100 --> n108
    n74 --> n88
    n96 --> n99
    n76 --> n89
    n74 --> n89
    n3 --> n2
    n112 --> n114
    n3 --> n90
    n75 --> n91
    n105 --> n109
    n100 --> n109
    n70 --> n76
    n73 --> n92
    n98 --> n110
    n104 --> n110
    n77 --> n110
    n91 --> n100
    n96 --> n100
    n97 --> n100
    n74 --> n93
    n79 --> n93
    n96 --> n112
    n108 --> n112
    n90 --> n101
    n69 --> n77
    n71 --> n77
    n70 --> n78
    n70 --> n3
    n3 --> n94
    n69 --> n79
    n73 --> n95
    n85 --> n102
    n75 --> n96
    n95 --> n103
    n84 --> n103
    n109 --> n113
    n108 --> n113
    n111 --> n113
    n71 --> n80
    n68 --> n69
    n68 --> n70
    n68 --> n71
    n93 --> n104
    n75 --> n97
    n71 --> n81
    n16 --> n17
    n70 --> n82
    n105 --> n111
    n97 --> n105
    n84 x--x n95
    n98 x--x n104
    n106 x--x n110
    n112 x--x n113
```

# FIN_right_wing_policies

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n63["FIN_finnish_march_of_conquest"]
        n18["FIN_finnish_neutrality"]
        n20{"FIN_right_wing_policies"}
        n23["FIN_suomalainen_sosialismi"]
        n26["fin_greatfinfoc"]
        n27["fin_nationalismfoc"]
    end
    subgraph tier_1["Tier 1"]
        n115["FIN_discredit_the_democratic_system"]
        n28{"FIN_national_unity"}
        n116["FIN_prepare_a_military_coup"]
        n31["FIN_weapon_caches"]
    end
    subgraph tier_2["Tier 2"]
        n34["FIN_a_cry_for_help"]
        n117{"FIN_a_fascist_regime"}
        n36["FIN_arm_the_lotta_svard"]
        n41["FIN_viron_kansa"]
    end
    subgraph tier_3["Tier 3"]
        n118["FIN_academic_karelian_society"]
        n42["FIN_ambitions_in_the_south"]
        n119["FIN_finnish_supremacy_in_the_north"]
        n120["FIN_join_axis"]
        n121["FIN_patriotic_peoples_movement"]
        n21["FIN_seek_german_protection"]
        n47["FIN_union_of_finnish_brothers_in_arms"]
    end
    subgraph tier_4["Tier 4"]
        n122["FIN_finnish_legion_of_honor"]
        n123["FIN_industrial_cooperation"]
        n124["FIN_maan_turva"]
        n51["FIN_militarized_society"]
        n125["FIN_military_research"]
        n126["FIN_mustapaidat"]
        n53["FIN_parmis_devils"]
        n127["FIN_tactical_wargaming_department"]
        n128["FIN_take_over_the_suojeluskunta"]
    end
    subgraph tier_5["Tier 5"]
        n129["FIN_advanced_jaeger_training_program"]
        n130["FIN_bring_foreign_armor_experts"]
        n131["FIN_finnish_irredentism"]
        n132["FIN_indoctrinate_the_workers"]
        n133["FIN_military_promotions"]
        n134["FIN_sotilaalliset_kappalaiset"]
    end
    subgraph tier_6["Tier 6"]
        n135["FIN_intellectual_elite"]
        n19["FIN_keepers_of_the_north"]
        n136["FIN_national_fanatism"]
    end
    subgraph tier_7["Tier 7"]
        n67["FIN_greater_finland"]
    end
    n28 --> n34
    n115 --> n117
    n116 --> n117
    n117 --> n118
    n125 --> n129
    n122 --> n129
    n41 --> n42
    n28 --> n36
    n125 --> n130
    n123 --> n130
    n20 --> n115
    n122 --> n131
    n127 --> n131
    n119 --> n122
    n117 --> n119
    n63 --> n67
    n51 --> n67
    n19 --> n67
    n26 --> n67
    n124 --> n132
    n120 --> n123
    n133 --> n135
    n132 --> n135
    n117 --> n120
    n131 --> n19
    n130 --> n19
    n118 --> n124
    n47 --> n51
    n128 --> n133
    n120 --> n125
    n121 --> n126
    n134 --> n136
    n18 --> n28
    n20 --> n28
    n27 --> n28
    n47 --> n53
    n117 --> n121
    n20 --> n116
    n117 --> n21
    n126 --> n134
    n119 --> n127
    n121 --> n128
    n118 --> n128
    n36 --> n47
    n28 --> n41
    n18 --> n31
    n20 --> n31
    n27 --> n31
    n34 x--x n21
    n115 x--x n116
    n18 x--x n20
    n119 x--x n120
    n20 x--x n23
```

# FIN_suomalainen_sosialismi

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18{"FIN_finnish_neutrality"}
        n29["FIN_political_unity"]
        n20["FIN_right_wing_policies"]
        n23{"FIN_suomalainen_sosialismi"}
        n24{"fin_comfoc"}
        n25["fin_demcomunbanfoc"]
    end
    subgraph tier_1["Tier 1"]
        n22{"FIN_social_democracy"}
        n137{"FIN_towards_a_red_government"}
        n32["fin_karjalafoc"]
        n33["fin_removeclaimfoc"]
    end
    subgraph tier_2["Tier 2"]
        n35["FIN_align_the_agrarian_league"]
        n138["FIN_antagonize_the_soviets"]
        n139["FIN_approach_the_soviets"]
        n140["FIN_pragmatic_socialism"]
        n40["FIN_the_finnish_swedish_peoples_party"]
        n141{"FIN_the_second_finnish_civil_war"}
    end
    subgraph tier_3["Tier 3"]
        n142["FIN_cooperate_with_social_democrats"]
        n143{"FIN_defensive_preparations"}
        n144["FIN_finnish_federation_of_trade_unions"]
        n145["FIN_finnish_learned_societies"]
        n146{"FIN_finno_estonian_union"}
        n147{"FIN_finno_soviet_pact"}
        n148["FIN_mineral_wealth"]
        n149["FIN_social_democratic_womens_union"]
        n150{"FIN_sosialistinen_eduskuntaryhma"}
        n151["FIN_the_peoples_democratic_league"]
        n152["FIN_the_workers_state"]
    end
    subgraph tier_4["Tier 4"]
        n153["FIN_approach_major_democracies"]
        n154["FIN_funds_from_kalevala_koru_oy"]
        n155["FIN_join_the_comintern"]
        n156["FIN_subsidized_national_industrialization"]
        n157["FIN_the_red_watch"]
        n158["FIN_trade_agreements"]
        n159["FIN_united_under_the_north_star"]
    end
    subgraph tier_5["Tier 5"]
        n160["FIN_aid_for_entrepreneurs"]
        n161["FIN_confederated_finno_russian_republics"]
        n162["FIN_control_the_flux_of_iron_ore"]
        n163["FIN_finnish_autonomy"]
        n164["FIN_finnish_influence_in_the_baltic"]
        n165["FIN_integrate_kola_and_karelia"]
        n166["FIN_secure_the_baltic_sea"]
    end
    subgraph tier_6["Tier 6"]
        n167["FIN_british_threat"]
        n168["FIN_german_threat"]
        n169["FIN_keepers_of_the_baltic_countries"]
        n170["FIN_preserve_sapmi"]
        n171["FIN_proclaim_greater_finland"]
        n172["FIN_socialist_welfare"]
        n173["FIN_soviet_threat"]
    end
    subgraph tier_7["Tier 7"]
        n174["FIN_red_finland"]
    end
    n153 --> n160
    n159 --> n160
    n29 --> n35
    n22 --> n35
    n25 --> n35
    n137 --> n138
    n22 --> n138
    n150 --> n153
    n143 --> n153
    n137 --> n139
    n22 --> n139
    n165 --> n167
    n159 --> n161
    n153 --> n162
    n141 --> n142
    n138 --> n143
    n155 --> n163
    n138 --> n144
    n139 --> n144
    n155 --> n164
    n159 --> n164
    n139 --> n145
    n138 --> n145
    n139 --> n146
    n138 --> n146
    n139 --> n147
    n149 --> n154
    n148 --> n154
    n164 --> n168
    n166 --> n168
    n155 --> n165
    n141 --> n155
    n147 --> n155
    n165 --> n169
    n164 --> n169
    n140 --> n148
    n22 --> n140
    n164 --> n170
    n162 --> n171
    n160 --> n171
    n169 --> n174
    n159 --> n166
    n153 --> n166
    n23 --> n22
    n140 --> n149
    n166 --> n172
    n140 --> n150
    n166 --> n173
    n160 --> n173
    n147 --> n156
    n22 --> n40
    n29 --> n40
    n25 --> n40
    n141 --> n151
    n152 --> n157
    n137 --> n141
    n141 --> n152
    n23 --> n137
    n143 --> n158
    n146 --> n159
    n18 --> n32
    n23 --> n32
    n24 --> n32
    n18 --> n33
    n23 --> n33
    n24 --> n33
    n138 x--x n139
    n153 x--x n155
    n153 x--x n159
    n18 x--x n23
    n155 x--x n159
    n20 x--x n23
    n22 x--x n137
    n32 x--x n33
```

# fin_comfoc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18{"FIN_finnish_neutrality"}
        n29["FIN_political_unity"]
        n22["FIN_social_democracy"]
        n23{"FIN_suomalainen_sosialismi"}
        n24{"fin_comfoc"}
        n27["fin_nationalismfoc"]
    end
    subgraph tier_1["Tier 1"]
        n25["fin_demcomunbanfoc"]
        n175["fin_indoctrination"]
        n32["fin_karjalafoc"]
        n33["fin_removeclaimfoc"]
        n176["fin_restoreredguard"]
    end
    subgraph tier_2["Tier 2"]
        n35["FIN_align_the_agrarian_league"]
        n40["FIN_the_finnish_swedish_peoples_party"]
        n177["fin_demandgovchange"]
        n178["fin_propaganda"]
        n179["fin_revolutionfoc"]
    end
    subgraph tier_3["Tier 3"]
        n180{"fin_banfascism"}
        n181["fin_wwrevol"]
    end
    subgraph tier_4["Tier 4"]
        n182["fin_jointhecomintern"]
        n183["fin_ourownway"]
    end
    subgraph tier_5["Tier 5"]
        n184["fin_norrevolution"]
        n185["fin_sovietcomfoc"]
        n186["fin_unholyalliance"]
    end
    subgraph tier_6["Tier 6"]
        n187["fin_estoniaforkarjala"]
        n188["fin_nordicom"]
        n189["fin_takedownaxis"]
    end
    subgraph tier_7["Tier 7"]
        n190["fin_balticsafety"]
    end
    n29 --> n35
    n22 --> n35
    n25 --> n35
    n22 --> n40
    n29 --> n40
    n25 --> n40
    n188 --> n190
    n179 --> n180
    n177 --> n180
    n25 --> n177
    n24 --> n25
    n186 --> n187
    n24 --> n175
    n180 --> n182
    n18 --> n32
    n23 --> n32
    n24 --> n32
    n184 --> n188
    n183 --> n184
    n180 --> n183
    n175 --> n178
    n18 --> n33
    n23 --> n33
    n24 --> n33
    n24 --> n176
    n176 --> n179
    n183 --> n185
    n186 --> n189
    n182 --> n186
    n178 --> n181
    n18 x--x n24
    n24 x--x n27
    n25 x--x n176
    n182 x--x n183
    n32 x--x n33
```

# fin_nationalismfoc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n63["FIN_finnish_march_of_conquest"]
        n18["FIN_finnish_neutrality"]
        n19["FIN_keepers_of_the_north"]
        n20["FIN_right_wing_policies"]
        n21["FIN_seek_german_protection"]
        n24["fin_comfoc"]
        n27{"fin_nationalismfoc"}
    end
    subgraph tier_1["Tier 1"]
        n28{"FIN_national_unity"}
        n31["FIN_weapon_caches"]
        n191["fin_axisalliancefoc"]
        n192["fin_fascist_british_alliance"]
        n193["fin_independent_diplomacy"]
        n194["fin_militarismfoc"]
    end
    subgraph tier_2["Tier 2"]
        n34["FIN_a_cry_for_help"]
        n36["FIN_arm_the_lotta_svard"]
        n195["FIN_push_towards_scandinavia"]
        n196{"FIN_the_dream_of_greater_finland_r56"}
        n41["FIN_viron_kansa"]
        n197["fin_gertechsharingfoc"]
        n198["fin_paramilitarism"]
    end
    subgraph tier_3["Tier 3"]
        n42["FIN_ambitions_in_the_south"]
        n47["FIN_union_of_finnish_brothers_in_arms"]
        n199["fin_annexnorfoc"]
        n200["fin_annexswefoc"]
        n201["fin_estonia"]
        n202["fin_germilhelpfoc"]
        n203["fin_nazisovietfoc"]
    end
    subgraph tier_4["Tier 4"]
        n51["FIN_militarized_society"]
        n53["FIN_parmis_devils"]
        n204["fin_annexdenfoc"]
    end
    subgraph tier_5["Tier 5"]
        n205["fin_annexicefoc"]
    end
    subgraph tier_6["Tier 6"]
        n26["fin_greatfinfoc"]
    end
    subgraph tier_7["Tier 7"]
        n67["FIN_greater_finland"]
    end
    n28 --> n34
    n41 --> n42
    n28 --> n36
    n63 --> n67
    n51 --> n67
    n19 --> n67
    n26 --> n67
    n47 --> n51
    n18 --> n28
    n20 --> n28
    n27 --> n28
    n47 --> n53
    n191 --> n195
    n193 --> n195
    n192 --> n195
    n191 --> n196
    n193 --> n196
    n192 --> n196
    n36 --> n47
    n28 --> n41
    n18 --> n31
    n20 --> n31
    n27 --> n31
    n200 --> n204
    n199 --> n204
    n204 --> n205
    n195 --> n199
    n195 --> n200
    n27 --> n191
    n196 --> n201
    n27 --> n192
    n197 --> n202
    n191 --> n197
    n205 --> n26
    n203 --> n26
    n201 --> n26
    n27 --> n193
    n27 --> n194
    n196 --> n203
    n194 --> n198
    n34 x--x n21
    n18 x--x n27
    n191 x--x n192
    n191 x--x n193
    n24 x--x n27
    n201 x--x n203
    n192 x--x n193
```
