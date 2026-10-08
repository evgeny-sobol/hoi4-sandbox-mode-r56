# FRA_CHEDN

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"FRA_CHEDN"}
        n2["FRA_enact_plan_v"]
        n3["FRA_new_french_fighter"]
    end
    subgraph tier_1["Tier 1"]
        n4{"FRA_experiment_castex_strategies"}
        n5{"FRA_lay_down_the_jean_bart"}
    end
    subgraph tier_2["Tier 2"]
        n6["FRA_adapt_young_school_concepts"]
        n7["FRA_capital_ship_focus"]
        n8["FRA_carrier_focus"]
        n9["FRA_colonial_naval_bases"]
        n10["FRA_mediterranean_special_measures"]
        n11["FRA_the_le_hardi_class_destroyer"]
    end
    subgraph tier_3["Tier 3"]
        n12["FRA_carrier_planes"]
        n13["FRA_darlan_doctrine"]
        n14["FRA_develop_colonial_dockyards"]
        n15["FRA_improved_screen_ships"]
        n16["FRA_strategic_manoeuvre"]
        n17["FRA_undersea_combat"]
    end
    subgraph tier_4["Tier 4"]
        n18["FRA_naval_construction_program"]
    end
    subgraph tier_5["Tier 5"]
        n19["FRA_barrage_david"]
        n20["FRA_increase_repair_capabilities"]
        n21["FRA_naval_gunnery"]
        n22["FRA_prioritize_the_joffre"]
        n23["FRA_standardisation_engine"]
        n24["FRA_supprt_the_aeronavale"]
    end
    subgraph tier_6["Tier 6"]
        n25["FRA_jet_effort"]
    end
    n4 --> n6
    n2 --> n19
    n18 --> n19
    n4 --> n7
    n5 --> n7
    n5 --> n8
    n8 --> n12
    n5 --> n9
    n7 --> n13
    n8 --> n13
    n9 --> n14
    n1 --> n4
    n11 --> n15
    n18 --> n20
    n3 --> n25
    n19 --> n25
    n1 --> n5
    n4 --> n10
    n5 --> n10
    n15 --> n18
    n7 --> n18
    n8 --> n18
    n18 --> n21
    n18 --> n22
    n8 --> n22
    n18 --> n23
    n6 --> n16
    n2 --> n24
    n18 --> n24
    n4 --> n11
    n5 --> n11
    n6 --> n17
    n7 x--x n8
    n4 x--x n5
```

# FRA_action_francaise

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26(("FRA_action_francaise"))
        n27["FRA_cagoule_coup"]
        n28{"FRA_diplomatic_freedom"}
        n29["FRA_far_right_leagues"]
        n30["FRA_front_liberte"]
        n31["FRA_radicalize_front"]
        n32{"FRA_state_reorganisation"}
        n33["FRA_status_quo"]
        n34{"FRA_support_ppf"}
        n35{"FRA_we_want_petain"}
    end
    subgraph tier_1["Tier 1"]
        n36{"FRA_papal_rehabilitation"}
        n37{"FRA_repeal_the_law_of_exile"}
        n38["FRA_root_out_communism"]
    end
    subgraph tier_2["Tier 2"]
        n39["FRA_brumaire_movement"]
        n40{"FRA_side_with_the_orleanists"}
        n41{"FRA_support_the_legitimatises"}
        n42["FRA_unify_the_metropole"]
    end
    subgraph tier_3["Tier 3"]
        n43["FRA_assist_the_carlist_cause"]
        n44["FRA_counter_the_fascist_infulence"]
        n45["FRA_militarist_society"]
        n46["FRA_national_integralism"]
        n47["FRA_support_the_spanish_nationalists"]
        n48{"FRA_the_new_continental_system"}
        n49{"FRA_union_latins"}
    end
    subgraph tier_4["Tier 4"]
        n50["FRA_anti_german_front"]
        n51["FRA_camelots_roi"]
        n52{"FRA_compromise_with_germany"}
        n53{"FRA_demand_wallonia"}
        n54{"FRA_intervene_in_the_spanish_civil_war"}
        n55["FRA_invite_portugal"]
        n56["FRA_keep_the_separation_of_church_and_state"]
        n57["FRA_legacy_of_the_grande_armee"]
        n58{"FRA_our_natural_borders"}
        n59["FRA_oust_maurras"]
        n60["FRA_social_nationalism"]
        n61{"FRA_ultimatum_to_belgium"}
    end
    subgraph tier_5["Tier 5"]
        n62["FRA_a_more_durable_tilsit_treaty"]
        n63["FRA_ally_italy"]
        n64["FRA_approach_poland_and_romania"]
        n65["FRA_approach_the_empire_of_brazil"]
        n66{"FRA_claim_rhineland"}
        n67["FRA_constitutional_monarchy"]
        n68{"FRA_crush_germany"}
        n69["FRA_decentralise_the_state"]
        n70["FRA_destroy_albion"]
        n71["FRA_empire_pact_with_spain"]
        n72["FRA_monarchist_invite_yugoslavia"]
        n73["FRA_napoleon_iii_legacy"]
        n74{"FRA_nothern_italy_claim"}
        n75["FRA_pact_with_spain"]
        n76["FRA_reorganize_the_dutch"]
        n77["FRA_restore_ancient_reights"]
        n78["FRA_revise_versailles"]
        n79["FRA_secure_catalonia"]
        n80["FRA_secure_the_crown_of_spain"]
        n81["FRA_split_belgium"]
    end
    subgraph tier_6["Tier 6"]
        n82["FRA_anti_communism_r56"]
        n83["FRA_claim_the_andorran_throne"]
        n84["FRA_convince_spain"]
        n85["FRA_dismantle_germany"]
        n86["FRA_disunite_germany"]
        n87["FRA_disunite_italy"]
        n88["FRA_embrace_the_counter_revolution"]
        n89["FRA_empire_invite_yugoslavia"]
        n90["FRA_empire_obtain_polish_cryptological_data"]
        n91["FRA_metropolitan_priority"]
        n92["FRA_operation_charlemagna"]
        n93["FRA_proclaim_the_dual_monarchy"]
        n94["FRA_public_works"]
        n95["FRA_restore_the_mexican_monarchy"]
        n96["FRA_return_to_dalmatia"]
        n97["FRA_second_march_on_moscow"]
        n98["FRA_secure_iberia"]
        n99["FRA_split_switzerland"]
        n100["FRA_take_back_north_america"]
        n101["FRA_woo_italy"]
    end
    subgraph tier_7["Tier 7"]
        n102["FRA_pacify_the_spanish_countryside"]
        n103["FRA_plan_xiv"]
        n104["FRA_strike_urss"]
    end
    n58 --> n62
    n50 --> n63
    n63 --> n82
    n75 --> n82
    n47 --> n50
    n58 --> n64
    n58 --> n65
    n52 --> n65
    n41 --> n43
    n36 --> n39
    n37 --> n39
    n46 --> n51
    n53 --> n66
    n61 --> n66
    n80 --> n83
    n48 --> n52
    n59 --> n67
    n56 --> n67
    n66 --> n84
    n49 --> n84
    n40 --> n44
    n58 --> n68
    n60 --> n69
    n34 --> n53
    n35 --> n53
    n32 --> n53
    n49 --> n53
    n58 --> n70
    n52 --> n70
    n66 --> n85
    n68 --> n86
    n74 --> n87
    n69 --> n88
    n77 --> n88
    n74 --> n89
    n64 --> n90
    n58 --> n71
    n52 --> n71
    n43 --> n54
    n49 --> n55
    n44 --> n56
    n45 --> n57
    n67 --> n91
    n39 --> n45
    n50 --> n72
    n58 --> n73
    n52 --> n73
    n40 --> n46
    n41 --> n46
    n58 --> n74
    n52 --> n74
    n66 --> n92
    n78 --> n92
    n48 --> n58
    n44 --> n59
    n93 --> n102
    n50 --> n75
    n26 --> n36
    n85 --> n103
    n80 --> n93
    n67 --> n94
    n58 --> n76
    n26 --> n37
    n60 --> n77
    n70 --> n95
    n74 --> n96
    n28 --> n78
    n53 --> n78
    n61 --> n78
    n29 --> n38
    n26 --> n38
    n68 --> n97
    n58 --> n79
    n52 --> n79
    n79 --> n98
    n54 --> n80
    n36 --> n40
    n37 --> n40
    n46 --> n60
    n52 --> n81
    n78 --> n99
    n99 --> n104
    n36 --> n41
    n37 --> n41
    n41 --> n47
    n40 --> n47
    n70 --> n100
    n39 --> n48
    n34 --> n61
    n35 --> n61
    n32 --> n61
    n49 --> n61
    n27 --> n42
    n30 --> n42
    n36 --> n42
    n41 --> n49
    n66 --> n101
    n49 --> n101
    n62 x--x n97
    n26 x--x n29
    n26 x--x n31
    n26 x--x n33
    n43 x--x n47
    n39 x--x n40
    n39 x--x n41
    n66 x--x n78
    n52 x--x n58
    n84 x--x n80
    n44 x--x n46
    n53 x--x n61
    n89 x--x n96
    n71 x--x n79
    n73 x--x n74
    n40 x--x n41
```

# FRA_colonial_investments

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n105{"FRA_colonial_investments"}
        n106["FRA_tools_modernisation"]
    end
    subgraph tier_1["Tier 1"]
        n107["FRA_continue_mandat"]
        n108["FRA_sncf"]
        n109["FRA_vienot_agreement"]
    end
    subgraph tier_2["Tier 2"]
        n110["FRA_consolidate_african_federations"]
        n111["FRA_develop_algeria"]
        n112["FRA_develop_morocco"]
        n113["FRA_monetary_tripartite_agreement"]
        n114["FRA_rewrite_protectorate_treaties"]
        n115["FRA_the_blum_viollette_proposal"]
    end
    subgraph tier_3["Tier 3"]
        n116["FRA_autonomy_indochina"]
        n117["FRA_cnrs"]
        n118["FRA_develop_indochine"]
        n119["FRA_develop_tunisia"]
        n120{"FRA_expand_the_citizenship"}
    end
    subgraph tier_4["Tier 4"]
        n121["FRA_buy_heavy_water"]
        n122["FRA_encourage_immigration"]
        n123{"FRA_gueye_lamine_law"}
        n124["FRA_technology_sharing"]
    end
    subgraph tier_5["Tier 5"]
        n125["FRA_france_undividable"]
        n126["FRA_overseas_departements"]
        n127["FRA_research_grants"]
        n128["FRA_sahara_oil"]
        n129["FRA_tungsten_mines"]
    end
    subgraph tier_6["Tier 6"]
        n130["FRA_french_union"]
    end
    n114 --> n116
    n110 --> n116
    n117 --> n121
    n113 --> n117
    n109 --> n110
    n105 --> n107
    n107 --> n111
    n108 --> n111
    n112 --> n118
    n111 --> n118
    n107 --> n112
    n112 --> n119
    n111 --> n119
    n120 --> n122
    n115 --> n120
    n120 --> n125
    n123 --> n125
    n125 --> n130
    n116 --> n123
    n108 --> n113
    n106 --> n113
    n123 --> n126
    n121 --> n127
    n109 --> n114
    n124 --> n128
    n106 --> n108
    n105 --> n108
    n117 --> n124
    n119 --> n124
    n107 --> n115
    n109 --> n115
    n124 --> n129
    n118 --> n129
    n105 --> n109
    n107 x--x n109
    n122 x--x n125
```

# FRA_continue_the_fight_in_africa

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n131(("FRA_continue_the_fight_in_africa"))
    end
    subgraph tier_1["Tier 1"]
        n132["FRA_mobilize_the_empire"]
    end
    subgraph tier_2["Tier 2"]
        n133["FRA_continue_the_fight2"]
        n134["FRA_equatorial_african_gold_mining2"]
        n135["FRA_radio_brazzaville2"]
    end
    subgraph tier_3["Tier 3"]
        n136["FRA_colonial_recruitment2"]
        n137["FRA_exploit_rubber_vines2"]
        n138["FRA_improve_equatorial_roads2"]
        n139["FRA_the_free_french_navy2"]
        n140["FRA_the_regiment_normandie2"]
    end
    subgraph tier_4["Tier 4"]
        n141["FRA_an_african_army2"]
        n142["FRA_prepare_for_our_return2"]
    end
    subgraph tier_5["Tier 5"]
        n143["FRA_improved_logistics2"]
    end
    n136 --> n141
    n133 --> n136
    n132 --> n133
    n132 --> n134
    n134 --> n137
    n134 --> n138
    n141 --> n143
    n131 --> n132
    n139 --> n142
    n132 --> n135
    n133 --> n139
    n133 --> n140
```

# FRA_de_gaulle_strategy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n144(("FRA_de_gaulle_strategy"))
        n145["FRA_fortification_focus"]
        n146["FRA_giraud_plan"]
    end
    subgraph tier_1["Tier 1"]
        n147["FRA_alpine_forts"]
        n148["FRA_motorized_focus"]
    end
    subgraph tier_2["Tier 2"]
        n149["FRA_artillery_focus"]
        n150["FRA_infantry_tanks"]
        n151["FRA_mechanized_focus"]
        n152["FRA_the_mas38"]
    end
    subgraph tier_3["Tier 3"]
        n153["FRA_army_reform"]
        n154["FRA_infantry_focus"]
        n155["FRA_light_medium_armor"]
        n156["FRA_tank_modernisation"]
        n157["FRA_the_somua_s35"]
    end
    subgraph tier_4["Tier 4"]
        n158["FRA_commandos_marine"]
        n159["FRA_division_cuirassee"]
        n160["FRA_foreign_legion"]
    end
    subgraph tier_5["Tier 5"]
        n161["FRA_africa_army"]
        n162["FRA_colonial_troops"]
    end
    n160 --> n161
    n146 --> n147
    n144 --> n147
    n150 --> n153
    n152 --> n153
    n149 --> n153
    n145 --> n149
    n148 --> n149
    n160 --> n162
    n153 --> n158
    n153 --> n159
    n153 --> n160
    n152 --> n154
    n145 --> n150
    n148 --> n150
    n151 --> n155
    n148 --> n151
    n144 --> n148
    n151 --> n156
    n145 --> n152
    n148 --> n152
    n150 --> n157
    n144 x--x n146
```

# FRA_far_right_leagues

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["FRA_action_francaise"]
        n29{"FRA_far_right_leagues"}
        n36["FRA_papal_rehabilitation"]
        n31["FRA_radicalize_front"]
        n80["FRA_secure_the_crown_of_spain"]
        n33["FRA_status_quo"]
        n49{"FRA_union_latins"}
    end
    subgraph tier_1["Tier 1"]
        n27["FRA_cagoule_coup"]
        n30{"FRA_front_liberte"}
        n38["FRA_root_out_communism"]
    end
    subgraph tier_2["Tier 2"]
        n163["FRA_service_ordre_legionnaire"]
        n32{"FRA_state_reorganisation"}
        n34{"FRA_support_ppf"}
        n42["FRA_unify_the_metropole"]
        n35{"FRA_we_want_petain"}
    end
    subgraph tier_3["Tier 3"]
        n164["FRA_alliance_with_industrialists"]
        n165["FRA_class_collaboration"]
        n53{"FRA_demand_wallonia"}
        n28{"FRA_diplomatic_freedom"}
        n166["FRA_the_three_levers"]
        n61{"FRA_ultimatum_to_belgium"}
    end
    subgraph tier_4["Tier 4"]
        n66{"FRA_claim_rhineland"}
        n78["FRA_revise_versailles"]
    end
    subgraph tier_5["Tier 5"]
        n84["FRA_convince_spain"]
        n85["FRA_dismantle_germany"]
        n92["FRA_operation_charlemagna"]
        n99["FRA_split_switzerland"]
        n101["FRA_woo_italy"]
    end
    subgraph tier_6["Tier 6"]
        n103["FRA_plan_xiv"]
        n104["FRA_strike_urss"]
    end
    n32 --> n164
    n29 --> n27
    n53 --> n66
    n61 --> n66
    n34 --> n165
    n35 --> n165
    n66 --> n84
    n49 --> n84
    n34 --> n53
    n35 --> n53
    n32 --> n53
    n49 --> n53
    n34 --> n28
    n35 --> n28
    n66 --> n85
    n29 --> n30
    n66 --> n92
    n78 --> n92
    n85 --> n103
    n28 --> n78
    n53 --> n78
    n61 --> n78
    n29 --> n38
    n26 --> n38
    n27 --> n163
    n78 --> n99
    n27 --> n32
    n99 --> n104
    n30 --> n34
    n34 --> n166
    n35 --> n166
    n34 --> n61
    n35 --> n61
    n32 --> n61
    n49 --> n61
    n27 --> n42
    n30 --> n42
    n36 --> n42
    n30 --> n35
    n66 --> n101
    n49 --> n101
    n26 x--x n29
    n27 x--x n30
    n66 x--x n78
    n84 x--x n80
    n53 x--x n61
    n29 x--x n31
    n29 x--x n33
    n34 x--x n35
```

# FRA_form_the_first_strategic_bombing_unit

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n167(("FRA_form_the_first_strategic_bombing_unit"))
        n168["FRA_interwar_experience"]
        n18["FRA_naval_construction_program"]
    end
    subgraph tier_1["Tier 1"]
        n169["FRA_air_bases"]
        n170["FRA_modernisation_program"]
        n171["FRA_purchase_american_fighters"]
        n172["FRA_support_the_ecole_de_lair"]
    end
    subgraph tier_2["Tier 2"]
        n2["FRA_enact_plan_v"]
        n173["FRA_faire_face"]
    end
    subgraph tier_3["Tier 3"]
        n19["FRA_barrage_david"]
        n174["FRA_develop_bomber_fleet"]
        n3["FRA_new_french_fighter"]
        n175["FRA_provide_aerial_support"]
        n24["FRA_supprt_the_aeronavale"]
    end
    subgraph tier_4["Tier 4"]
        n176["FRA_follow_up_on_the_potez"]
        n25["FRA_jet_effort"]
    end
    n168 --> n169
    n167 --> n169
    n2 --> n19
    n18 --> n19
    n2 --> n174
    n172 --> n2
    n170 --> n2
    n172 --> n173
    n174 --> n176
    n3 --> n25
    n19 --> n25
    n167 --> n170
    n2 --> n3
    n2 --> n175
    n167 --> n171
    n167 --> n172
    n168 --> n172
    n2 --> n24
    n18 --> n24
```

# FRA_giraud_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n144["FRA_de_gaulle_strategy"]
        n146(("FRA_giraud_plan"))
        n148["FRA_motorized_focus"]
    end
    subgraph tier_1["Tier 1"]
        n147["FRA_alpine_forts"]
        n145["FRA_fortification_focus"]
    end
    subgraph tier_2["Tier 2"]
        n149["FRA_artillery_focus"]
        n177["FRA_commission_fortified_regions"]
        n150["FRA_infantry_tanks"]
        n152["FRA_the_mas38"]
    end
    subgraph tier_3["Tier 3"]
        n153["FRA_army_reform"]
        n178["FRA_extend_the_maginot_line"]
        n179["FRA_heavy_armor_focus"]
        n154["FRA_infantry_focus"]
        n157["FRA_the_somua_s35"]
    end
    subgraph tier_4["Tier 4"]
        n158["FRA_commandos_marine"]
        n159["FRA_division_cuirassee"]
        n160["FRA_foreign_legion"]
    end
    subgraph tier_5["Tier 5"]
        n161["FRA_africa_army"]
        n162["FRA_colonial_troops"]
    end
    n160 --> n161
    n146 --> n147
    n144 --> n147
    n150 --> n153
    n152 --> n153
    n149 --> n153
    n145 --> n149
    n148 --> n149
    n160 --> n162
    n153 --> n158
    n145 --> n177
    n153 --> n159
    n177 --> n178
    n153 --> n160
    n146 --> n145
    n177 --> n179
    n152 --> n154
    n145 --> n150
    n148 --> n150
    n145 --> n152
    n148 --> n152
    n150 --> n157
    n144 x--x n146
```

# FRA_interwar_experience

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n167["FRA_form_the_first_strategic_bombing_unit"]
        n168(("FRA_interwar_experience"))
        n170["FRA_modernisation_program"]
        n18["FRA_naval_construction_program"]
    end
    subgraph tier_1["Tier 1"]
        n169["FRA_air_bases"]
        n180["FRA_parachute_battalions"]
        n172["FRA_support_the_ecole_de_lair"]
    end
    subgraph tier_2["Tier 2"]
        n2["FRA_enact_plan_v"]
        n173["FRA_faire_face"]
    end
    subgraph tier_3["Tier 3"]
        n19["FRA_barrage_david"]
        n174["FRA_develop_bomber_fleet"]
        n3["FRA_new_french_fighter"]
        n175["FRA_provide_aerial_support"]
        n24["FRA_supprt_the_aeronavale"]
    end
    subgraph tier_4["Tier 4"]
        n176["FRA_follow_up_on_the_potez"]
        n25["FRA_jet_effort"]
    end
    n168 --> n169
    n167 --> n169
    n2 --> n19
    n18 --> n19
    n2 --> n174
    n172 --> n2
    n170 --> n2
    n172 --> n173
    n174 --> n176
    n3 --> n25
    n19 --> n25
    n2 --> n3
    n168 --> n180
    n2 --> n175
    n167 --> n172
    n168 --> n172
    n2 --> n24
    n18 --> n24
```

# FRA_radicalize_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["FRA_action_francaise"]
        n29["FRA_far_right_leagues"]
        n31{"FRA_radicalize_front"}
        n33["FRA_status_quo"]
    end
    subgraph tier_1["Tier 1"]
        n181["FRA_intervention_committee"]
        n182["FRA_intervention_in_spain"]
        n183["FRA_law_against_combat_groups"]
        n184["FRA_pcf_sfio_coalition"]
        n185["FRA_work_with_the_cgt"]
    end
    subgraph tier_2["Tier 2"]
        n186["FRA_ideological_indoctrination"]
    end
    subgraph tier_3["Tier 3"]
        n187{"FRA_commune_proclamation"}
        n188["FRA_syndicalist_revolution"]
    end
    subgraph tier_4["Tier 4"]
        n189{"FRA_collectivisation"}
        n190["FRA_grands_travaux"]
        n191["FRA_industrial_decentralization"]
    end
    subgraph tier_5["Tier 5"]
        n192["FRA_assistance_treaty"]
        n193["FRA_humanite_unie"]
    end
    subgraph tier_6["Tier 6"]
        n194["FRA_fascist_threat"]
        n195["FRA_help_the_spanish_republicans"]
        n196["FRA_research_cooperation"]
        n197["FRA_strike_empire"]
    end
    n187 --> n192
    n189 --> n192
    n188 --> n189
    n187 --> n189
    n184 --> n187
    n186 --> n187
    n193 --> n194
    n192 --> n194
    n187 --> n190
    n193 --> n195
    n189 --> n193
    n185 --> n186
    n184 --> n186
    n188 --> n191
    n31 --> n181
    n33 --> n182
    n31 --> n182
    n33 --> n183
    n31 --> n183
    n31 --> n184
    n192 --> n196
    n192 --> n197
    n193 --> n197
    n185 --> n188
    n186 --> n188
    n31 --> n185
    n26 x--x n31
    n192 x--x n193
    n29 x--x n31
    n184 x--x n185
    n31 x--x n33
```

# FRA_rearmament

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n198(("FRA_rearmament"))
    end
    subgraph tier_1["Tier 1"]
        n199["FRA_commit_automobile_manufacturer"]
        n200["FRA_war_material_licence"]
    end
    subgraph tier_2["Tier 2"]
        n201["FRA_defense_national_funds"]
    end
    subgraph tier_3["Tier 3"]
        n202["FRA_partial_mobilization"]
        n203["FRA_wartime_organisation_act"]
    end
    subgraph tier_4["Tier 4"]
        n204["FRA_aircraft_manufacturer_nationalisation"]
        n205["FRA_further_armament_program"]
        n206["FRA_military_complex_nationalisation"]
    end
    subgraph tier_5["Tier 5"]
        n207["FRA_war_effort_law"]
    end
    n202 --> n204
    n198 --> n199
    n199 --> n201
    n200 --> n201
    n203 --> n205
    n202 --> n206
    n201 --> n202
    n206 --> n207
    n204 --> n207
    n198 --> n200
    n201 --> n203
```

# FRA_status_quo

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["FRA_action_francaise"]
        n29["FRA_far_right_leagues"]
        n31["FRA_radicalize_front"]
        n33(("FRA_status_quo"))
    end
    subgraph tier_1["Tier 1"]
        n182["FRA_intervention_in_spain"]
        n183["FRA_law_against_combat_groups"]
        n208{"FRA_social_reforms"}
    end
    subgraph tier_2["Tier 2"]
        n209["FRA_support_blum"]
        n210["FRA_support_daladier"]
    end
    subgraph tier_3["Tier 3"]
        n211{"FRA_further_the_reforms"}
        n212{"FRA_increase_military_spendings"}
        n213{"FRA_rearmament_policy"}
        n214{"FRA_reynaud_economic_reforms"}
    end
    subgraph tier_4["Tier 4"]
        n215["FRA_go_with_britain"]
        n216["FRA_little_entente"]
        n217["FRA_support_the_finns"]
    end
    subgraph tier_5["Tier 5"]
        n218["FRA_arms_purchases_in_the_us"]
        n219["FRA_economic_cooperation_agreement"]
        n220["FRA_intervention"]
        n221["FRA_invite_poland"]
        n222["FRA_invite_yugoslavia"]
        n223["FRA_join_the_ententes"]
        n224["FRA_popular_front_united"]
    end
    subgraph tier_6["Tier 6"]
        n225["FRA_invite_benelux"]
        n226["FRA_invite_romania"]
        n227["FRA_research_treaty"]
    end
    subgraph tier_7["Tier 7"]
        n228["FRA_foreign_guest_workers"]
        n229["FRA_invest_in_our_weaker_allies"]
        n230["FRA_preventive_intervention"]
    end
    subgraph tier_8["Tier 8"]
        n231["FRA_coordinate_rearmament"]
    end
    n215 --> n218
    n229 --> n231
    n215 --> n219
    n226 --> n228
    n209 --> n211
    n212 --> n215
    n211 --> n215
    n214 --> n215
    n213 --> n215
    n209 --> n212
    n216 --> n220
    n33 --> n182
    n31 --> n182
    n226 --> n229
    n219 --> n225
    n224 --> n225
    n216 --> n221
    n222 --> n226
    n216 --> n222
    n216 --> n223
    n33 --> n183
    n31 --> n183
    n212 --> n216
    n211 --> n216
    n214 --> n216
    n213 --> n216
    n216 --> n224
    n215 --> n224
    n225 --> n230
    n226 --> n230
    n210 --> n213
    n224 --> n227
    n210 --> n214
    n33 --> n208
    n208 --> n209
    n208 --> n210
    n214 --> n217
    n213 --> n217
    n26 x--x n33
    n29 x--x n33
    n215 x--x n216
    n31 x--x n33
    n209 x--x n210
```

# FRA_the_council_of_rambouillet

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n232(("FRA_the_council_of_rambouillet"))
    end
```

# FRA_tools_modernisation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n105["FRA_colonial_investments"]
        n107["FRA_continue_mandat"]
        n112["FRA_develop_morocco"]
        n106(("FRA_tools_modernisation"))
    end
    subgraph tier_1["Tier 1"]
        n108["FRA_sncf"]
    end
    subgraph tier_2["Tier 2"]
        n111["FRA_develop_algeria"]
        n113["FRA_monetary_tripartite_agreement"]
    end
    subgraph tier_3["Tier 3"]
        n117["FRA_cnrs"]
        n118["FRA_develop_indochine"]
        n119["FRA_develop_tunisia"]
    end
    subgraph tier_4["Tier 4"]
        n121["FRA_buy_heavy_water"]
        n124["FRA_technology_sharing"]
    end
    subgraph tier_5["Tier 5"]
        n127["FRA_research_grants"]
        n128["FRA_sahara_oil"]
        n129["FRA_tungsten_mines"]
    end
    n117 --> n121
    n113 --> n117
    n107 --> n111
    n108 --> n111
    n112 --> n118
    n111 --> n118
    n112 --> n119
    n111 --> n119
    n108 --> n113
    n106 --> n113
    n121 --> n127
    n124 --> n128
    n106 --> n108
    n105 --> n108
    n117 --> n124
    n119 --> n124
    n124 --> n129
    n118 --> n129
```
