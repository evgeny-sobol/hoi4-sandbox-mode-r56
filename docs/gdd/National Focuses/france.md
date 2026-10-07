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
        n72["FRA_napoleon_iii_legacy"]
        n73{"FRA_nothern_italy_claim"}
        n74["FRA_pact_with_spain"]
        n75["FRA_reorganize_the_dutch"]
        n76["FRA_restore_ancient_reights"]
        n77["FRA_revise_versailles"]
        n78["FRA_secure_catalonia"]
        n79["FRA_secure_the_crown_of_spain"]
        n80["FRA_split_belgium"]
    end
    subgraph tier_6["Tier 6"]
        n81["FRA_anti_communism_r56"]
        n82["FRA_claim_the_andorran_throne"]
        n83["FRA_convince_spain"]
        n84["FRA_dismantle_germany"]
        n85["FRA_disunite_germany"]
        n86["FRA_disunite_italy"]
        n87["FRA_embrace_the_counter_revolution"]
        n88["FRA_empire_invite_yugoslavia"]
        n89["FRA_empire_obtain_polish_cryptological_data"]
        n90["FRA_metropolitan_priority"]
        n91["FRA_operation_charlemagna"]
        n92["FRA_proclaim_the_dual_monarchy"]
        n93["FRA_public_works"]
        n94["FRA_restore_the_mexican_monarchy"]
        n95["FRA_return_to_dalmatia"]
        n96["FRA_second_march_on_moscow"]
        n97["FRA_secure_iberia"]
        n98["FRA_split_switzerland"]
        n99["FRA_take_back_north_america"]
        n100["FRA_woo_italy"]
    end
    subgraph tier_7["Tier 7"]
        n101["FRA_pacify_the_spanish_countryside"]
        n102["FRA_plan_xiv"]
        n103["FRA_strike_urss"]
    end
    n58 --> n62
    n50 --> n63
    n63 --> n81
    n74 --> n81
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
    n79 --> n82
    n48 --> n52
    n59 --> n67
    n56 --> n67
    n66 --> n83
    n49 --> n83
    n40 --> n44
    n58 --> n68
    n60 --> n69
    n34 --> n53
    n35 --> n53
    n32 --> n53
    n49 --> n53
    n58 --> n70
    n52 --> n70
    n66 --> n84
    n68 --> n85
    n73 --> n86
    n69 --> n87
    n76 --> n87
    n73 --> n88
    n64 --> n89
    n58 --> n71
    n52 --> n71
    n43 --> n54
    n49 --> n55
    n44 --> n56
    n45 --> n57
    n67 --> n90
    n39 --> n45
    n58 --> n72
    n52 --> n72
    n40 --> n46
    n41 --> n46
    n58 --> n73
    n52 --> n73
    n66 --> n91
    n77 --> n91
    n48 --> n58
    n44 --> n59
    n92 --> n101
    n50 --> n74
    n26 --> n36
    n84 --> n102
    n79 --> n92
    n67 --> n93
    n58 --> n75
    n26 --> n37
    n60 --> n76
    n70 --> n94
    n73 --> n95
    n28 --> n77
    n53 --> n77
    n61 --> n77
    n29 --> n38
    n26 --> n38
    n68 --> n96
    n58 --> n78
    n52 --> n78
    n78 --> n97
    n54 --> n79
    n36 --> n40
    n37 --> n40
    n46 --> n60
    n52 --> n80
    n77 --> n98
    n98 --> n103
    n36 --> n41
    n37 --> n41
    n41 --> n47
    n40 --> n47
    n70 --> n99
    n39 --> n48
    n34 --> n61
    n35 --> n61
    n32 --> n61
    n49 --> n61
    n27 --> n42
    n30 --> n42
    n36 --> n42
    n41 --> n49
    n66 --> n100
    n49 --> n100
    n62 x--x n96
    n26 x--x n29
    n26 x--x n31
    n26 x--x n33
    n43 x--x n47
    n39 x--x n40
    n39 x--x n41
    n66 x--x n77
    n52 x--x n58
    n83 x--x n79
    n44 x--x n46
    n53 x--x n61
    n88 x--x n95
    n71 x--x n78
    n72 x--x n73
    n40 x--x n41
```

# FRA_colonial_investments

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n104{"FRA_colonial_investments"}
        n105["FRA_tools_modernisation"]
    end
    subgraph tier_1["Tier 1"]
        n106["FRA_continue_mandat"]
        n107["FRA_sncf"]
        n108["FRA_vienot_agreement"]
    end
    subgraph tier_2["Tier 2"]
        n109["FRA_consolidate_african_federations"]
        n110["FRA_develop_algeria"]
        n111["FRA_develop_morocco"]
        n112["FRA_monetary_tripartite_agreement"]
        n113["FRA_rewrite_protectorate_treaties"]
        n114["FRA_the_blum_viollette_proposal"]
    end
    subgraph tier_3["Tier 3"]
        n115["FRA_autonomy_indochina"]
        n116["FRA_cnrs"]
        n117["FRA_develop_indochine"]
        n118["FRA_develop_tunisia"]
        n119{"FRA_expand_the_citizenship"}
    end
    subgraph tier_4["Tier 4"]
        n120["FRA_buy_heavy_water"]
        n121["FRA_encourage_immigration"]
        n122{"FRA_gueye_lamine_law"}
        n123["FRA_technology_sharing"]
    end
    subgraph tier_5["Tier 5"]
        n124["FRA_france_undividable"]
        n125["FRA_overseas_departements"]
        n126["FRA_research_grants"]
        n127["FRA_sahara_oil"]
        n128["FRA_tungsten_mines"]
    end
    subgraph tier_6["Tier 6"]
        n129["FRA_french_union"]
    end
    n113 --> n115
    n109 --> n115
    n116 --> n120
    n112 --> n116
    n108 --> n109
    n104 --> n106
    n106 --> n110
    n107 --> n110
    n111 --> n117
    n110 --> n117
    n106 --> n111
    n111 --> n118
    n110 --> n118
    n119 --> n121
    n114 --> n119
    n119 --> n124
    n122 --> n124
    n124 --> n129
    n115 --> n122
    n107 --> n112
    n105 --> n112
    n122 --> n125
    n120 --> n126
    n108 --> n113
    n123 --> n127
    n105 --> n107
    n104 --> n107
    n116 --> n123
    n118 --> n123
    n106 --> n114
    n108 --> n114
    n123 --> n128
    n117 --> n128
    n104 --> n108
    n106 x--x n108
    n121 x--x n124
```

# FRA_continue_the_fight_in_africa

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n130(("FRA_continue_the_fight_in_africa"))
    end
    subgraph tier_1["Tier 1"]
        n131["FRA_mobilize_the_empire"]
    end
    subgraph tier_2["Tier 2"]
        n132["FRA_continue_the_fight2"]
        n133["FRA_equatorial_african_gold_mining2"]
        n134["FRA_radio_brazzaville2"]
    end
    subgraph tier_3["Tier 3"]
        n135["FRA_colonial_recruitment2"]
        n136["FRA_exploit_rubber_vines2"]
        n137["FRA_improve_equatorial_roads2"]
        n138["FRA_the_free_french_navy2"]
        n139["FRA_the_regiment_normandie2"]
    end
    subgraph tier_4["Tier 4"]
        n140["FRA_an_african_army2"]
        n141["FRA_prepare_for_our_return2"]
    end
    subgraph tier_5["Tier 5"]
        n142["FRA_improved_logistics2"]
    end
    n135 --> n140
    n132 --> n135
    n131 --> n132
    n131 --> n133
    n133 --> n136
    n133 --> n137
    n140 --> n142
    n130 --> n131
    n138 --> n141
    n131 --> n134
    n132 --> n138
    n132 --> n139
```

# FRA_de_gaulle_strategy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n143(("FRA_de_gaulle_strategy"))
        n144["FRA_fortification_focus"]
        n145["FRA_giraud_plan"]
    end
    subgraph tier_1["Tier 1"]
        n146["FRA_alpine_forts"]
        n147["FRA_motorized_focus"]
    end
    subgraph tier_2["Tier 2"]
        n148["FRA_artillery_focus"]
        n149["FRA_infantry_tanks"]
        n150["FRA_mechanized_focus"]
        n151["FRA_the_mas38"]
    end
    subgraph tier_3["Tier 3"]
        n152["FRA_army_reform"]
        n153["FRA_infantry_focus"]
        n154["FRA_light_medium_armor"]
        n155["FRA_tank_modernisation"]
        n156["FRA_the_somua_s35"]
    end
    subgraph tier_4["Tier 4"]
        n157["FRA_commandos_marine"]
        n158["FRA_division_cuirassee"]
        n159["FRA_foreign_legion"]
    end
    subgraph tier_5["Tier 5"]
        n160["FRA_africa_army"]
        n161["FRA_colonial_troops"]
    end
    n159 --> n160
    n145 --> n146
    n143 --> n146
    n149 --> n152
    n151 --> n152
    n148 --> n152
    n144 --> n148
    n147 --> n148
    n159 --> n161
    n152 --> n157
    n152 --> n158
    n152 --> n159
    n151 --> n153
    n144 --> n149
    n147 --> n149
    n150 --> n154
    n147 --> n150
    n143 --> n147
    n150 --> n155
    n144 --> n151
    n147 --> n151
    n149 --> n156
    n143 x--x n145
```

# FRA_far_right_leagues

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["FRA_action_francaise"]
        n29{"FRA_far_right_leagues"}
        n36["FRA_papal_rehabilitation"]
        n31["FRA_radicalize_front"]
        n79["FRA_secure_the_crown_of_spain"]
        n33["FRA_status_quo"]
        n49{"FRA_union_latins"}
    end
    subgraph tier_1["Tier 1"]
        n27["FRA_cagoule_coup"]
        n30{"FRA_front_liberte"}
        n38["FRA_root_out_communism"]
    end
    subgraph tier_2["Tier 2"]
        n162["FRA_service_ordre_legionnaire"]
        n32{"FRA_state_reorganisation"}
        n34{"FRA_support_ppf"}
        n42["FRA_unify_the_metropole"]
        n35{"FRA_we_want_petain"}
    end
    subgraph tier_3["Tier 3"]
        n163["FRA_alliance_with_industrialists"]
        n164["FRA_class_collaboration"]
        n53{"FRA_demand_wallonia"}
        n28{"FRA_diplomatic_freedom"}
        n165["FRA_the_three_levers"]
        n61{"FRA_ultimatum_to_belgium"}
    end
    subgraph tier_4["Tier 4"]
        n66{"FRA_claim_rhineland"}
        n77["FRA_revise_versailles"]
    end
    subgraph tier_5["Tier 5"]
        n83["FRA_convince_spain"]
        n84["FRA_dismantle_germany"]
        n91["FRA_operation_charlemagna"]
        n98["FRA_split_switzerland"]
        n100["FRA_woo_italy"]
    end
    subgraph tier_6["Tier 6"]
        n102["FRA_plan_xiv"]
        n103["FRA_strike_urss"]
    end
    n32 --> n163
    n29 --> n27
    n53 --> n66
    n61 --> n66
    n34 --> n164
    n35 --> n164
    n66 --> n83
    n49 --> n83
    n34 --> n53
    n35 --> n53
    n32 --> n53
    n49 --> n53
    n34 --> n28
    n35 --> n28
    n66 --> n84
    n29 --> n30
    n66 --> n91
    n77 --> n91
    n84 --> n102
    n28 --> n77
    n53 --> n77
    n61 --> n77
    n29 --> n38
    n26 --> n38
    n27 --> n162
    n77 --> n98
    n27 --> n32
    n98 --> n103
    n30 --> n34
    n34 --> n165
    n35 --> n165
    n34 --> n61
    n35 --> n61
    n32 --> n61
    n49 --> n61
    n27 --> n42
    n30 --> n42
    n36 --> n42
    n30 --> n35
    n66 --> n100
    n49 --> n100
    n26 x--x n29
    n27 x--x n30
    n66 x--x n77
    n83 x--x n79
    n53 x--x n61
    n29 x--x n31
    n29 x--x n33
    n34 x--x n35
```

# FRA_form_the_first_strategic_bombing_unit

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n166(("FRA_form_the_first_strategic_bombing_unit"))
        n167["FRA_interwar_experience"]
        n18["FRA_naval_construction_program"]
    end
    subgraph tier_1["Tier 1"]
        n168["FRA_air_bases"]
        n169["FRA_modernisation_program"]
        n170["FRA_purchase_american_fighters"]
        n171["FRA_support_the_ecole_de_lair"]
    end
    subgraph tier_2["Tier 2"]
        n2["FRA_enact_plan_v"]
        n172["FRA_faire_face"]
    end
    subgraph tier_3["Tier 3"]
        n19["FRA_barrage_david"]
        n173["FRA_develop_bomber_fleet"]
        n3["FRA_new_french_fighter"]
        n174["FRA_provide_aerial_support"]
        n24["FRA_supprt_the_aeronavale"]
    end
    subgraph tier_4["Tier 4"]
        n175["FRA_follow_up_on_the_potez"]
        n25["FRA_jet_effort"]
    end
    n167 --> n168
    n166 --> n168
    n2 --> n19
    n18 --> n19
    n2 --> n173
    n171 --> n2
    n169 --> n2
    n171 --> n172
    n173 --> n175
    n3 --> n25
    n19 --> n25
    n166 --> n169
    n2 --> n3
    n2 --> n174
    n166 --> n170
    n166 --> n171
    n167 --> n171
    n2 --> n24
    n18 --> n24
```

# FRA_giraud_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n143["FRA_de_gaulle_strategy"]
        n145(("FRA_giraud_plan"))
        n147["FRA_motorized_focus"]
    end
    subgraph tier_1["Tier 1"]
        n146["FRA_alpine_forts"]
        n144["FRA_fortification_focus"]
    end
    subgraph tier_2["Tier 2"]
        n148["FRA_artillery_focus"]
        n176["FRA_commission_fortified_regions"]
        n149["FRA_infantry_tanks"]
        n151["FRA_the_mas38"]
    end
    subgraph tier_3["Tier 3"]
        n152["FRA_army_reform"]
        n177["FRA_extend_the_maginot_line"]
        n178["FRA_heavy_armor_focus"]
        n153["FRA_infantry_focus"]
        n156["FRA_the_somua_s35"]
    end
    subgraph tier_4["Tier 4"]
        n157["FRA_commandos_marine"]
        n158["FRA_division_cuirassee"]
        n159["FRA_foreign_legion"]
    end
    subgraph tier_5["Tier 5"]
        n160["FRA_africa_army"]
        n161["FRA_colonial_troops"]
    end
    n159 --> n160
    n145 --> n146
    n143 --> n146
    n149 --> n152
    n151 --> n152
    n148 --> n152
    n144 --> n148
    n147 --> n148
    n159 --> n161
    n152 --> n157
    n144 --> n176
    n152 --> n158
    n176 --> n177
    n152 --> n159
    n145 --> n144
    n176 --> n178
    n151 --> n153
    n144 --> n149
    n147 --> n149
    n144 --> n151
    n147 --> n151
    n149 --> n156
    n143 x--x n145
```

# FRA_interwar_experience

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n166["FRA_form_the_first_strategic_bombing_unit"]
        n167(("FRA_interwar_experience"))
        n169["FRA_modernisation_program"]
        n18["FRA_naval_construction_program"]
    end
    subgraph tier_1["Tier 1"]
        n168["FRA_air_bases"]
        n179["FRA_parachute_battalions"]
        n171["FRA_support_the_ecole_de_lair"]
    end
    subgraph tier_2["Tier 2"]
        n2["FRA_enact_plan_v"]
        n172["FRA_faire_face"]
    end
    subgraph tier_3["Tier 3"]
        n19["FRA_barrage_david"]
        n173["FRA_develop_bomber_fleet"]
        n3["FRA_new_french_fighter"]
        n174["FRA_provide_aerial_support"]
        n24["FRA_supprt_the_aeronavale"]
    end
    subgraph tier_4["Tier 4"]
        n175["FRA_follow_up_on_the_potez"]
        n25["FRA_jet_effort"]
    end
    n167 --> n168
    n166 --> n168
    n2 --> n19
    n18 --> n19
    n2 --> n173
    n171 --> n2
    n169 --> n2
    n171 --> n172
    n173 --> n175
    n3 --> n25
    n19 --> n25
    n2 --> n3
    n167 --> n179
    n2 --> n174
    n166 --> n171
    n167 --> n171
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
        n180["FRA_intervention_committee"]
        n181["FRA_intervention_in_spain"]
        n182["FRA_law_against_combat_groups"]
        n183["FRA_pcf_sfio_coalition"]
        n184["FRA_work_with_the_cgt"]
    end
    subgraph tier_2["Tier 2"]
        n185["FRA_ideological_indoctrination"]
    end
    subgraph tier_3["Tier 3"]
        n186{"FRA_commune_proclamation"}
        n187["FRA_syndicalist_revolution"]
    end
    subgraph tier_4["Tier 4"]
        n188{"FRA_collectivisation"}
        n189["FRA_grands_travaux"]
        n190["FRA_industrial_decentralization"]
    end
    subgraph tier_5["Tier 5"]
        n191["FRA_assistance_treaty"]
        n192["FRA_humanite_unie"]
    end
    subgraph tier_6["Tier 6"]
        n193["FRA_fascist_threat"]
        n194["FRA_help_the_spanish_republicans"]
        n195["FRA_research_cooperation"]
        n196["FRA_strike_empire"]
    end
    n186 --> n191
    n188 --> n191
    n187 --> n188
    n186 --> n188
    n183 --> n186
    n185 --> n186
    n192 --> n193
    n191 --> n193
    n186 --> n189
    n192 --> n194
    n188 --> n192
    n184 --> n185
    n183 --> n185
    n187 --> n190
    n31 --> n180
    n33 --> n181
    n31 --> n181
    n33 --> n182
    n31 --> n182
    n31 --> n183
    n191 --> n195
    n191 --> n196
    n192 --> n196
    n184 --> n187
    n185 --> n187
    n31 --> n184
    n26 x--x n31
    n191 x--x n192
    n29 x--x n31
    n183 x--x n184
    n31 x--x n33
```

# FRA_rearmament

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n197(("FRA_rearmament"))
    end
    subgraph tier_1["Tier 1"]
        n198["FRA_commit_automobile_manufacturer"]
        n199["FRA_war_material_licence"]
    end
    subgraph tier_2["Tier 2"]
        n200["FRA_defense_national_funds"]
    end
    subgraph tier_3["Tier 3"]
        n201["FRA_partial_mobilization"]
        n202["FRA_wartime_organisation_act"]
    end
    subgraph tier_4["Tier 4"]
        n203["FRA_aircraft_manufacturer_nationalisation"]
        n204["FRA_further_armament_program"]
        n205["FRA_military_complex_nationalisation"]
    end
    subgraph tier_5["Tier 5"]
        n206["FRA_war_effort_law"]
    end
    n201 --> n203
    n197 --> n198
    n198 --> n200
    n199 --> n200
    n202 --> n204
    n201 --> n205
    n200 --> n201
    n205 --> n206
    n203 --> n206
    n197 --> n199
    n200 --> n202
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
        n181["FRA_intervention_in_spain"]
        n182["FRA_law_against_combat_groups"]
        n207{"FRA_social_reforms"}
    end
    subgraph tier_2["Tier 2"]
        n208["FRA_support_blum"]
        n209["FRA_support_daladier"]
    end
    subgraph tier_3["Tier 3"]
        n210{"FRA_further_the_reforms"}
        n211{"FRA_increase_military_spendings"}
        n212{"FRA_rearmament_policy"}
        n213{"FRA_reynaud_economic_reforms"}
    end
    subgraph tier_4["Tier 4"]
        n214["FRA_go_with_britain"]
        n215["FRA_little_entente"]
        n216["FRA_support_the_finns"]
    end
    subgraph tier_5["Tier 5"]
        n217["FRA_arms_purchases_in_the_us"]
        n218["FRA_economic_cooperation_agreement"]
        n219["FRA_intervention"]
        n220["FRA_invite_poland"]
        n221["FRA_invite_yugoslavia"]
        n222["FRA_join_the_ententes"]
        n223["FRA_popular_front_united"]
    end
    subgraph tier_6["Tier 6"]
        n224["FRA_invite_benelux"]
        n225["FRA_invite_romania"]
        n226["FRA_research_treaty"]
    end
    subgraph tier_7["Tier 7"]
        n227["FRA_foreign_guest_workers"]
        n228["FRA_invest_in_our_weaker_allies"]
        n229["FRA_preventive_intervention"]
    end
    subgraph tier_8["Tier 8"]
        n230["FRA_coordinate_rearmament"]
    end
    n214 --> n217
    n228 --> n230
    n214 --> n218
    n225 --> n227
    n208 --> n210
    n211 --> n214
    n210 --> n214
    n213 --> n214
    n212 --> n214
    n208 --> n211
    n215 --> n219
    n33 --> n181
    n31 --> n181
    n225 --> n228
    n218 --> n224
    n223 --> n224
    n215 --> n220
    n221 --> n225
    n215 --> n221
    n215 --> n222
    n33 --> n182
    n31 --> n182
    n211 --> n215
    n210 --> n215
    n213 --> n215
    n212 --> n215
    n215 --> n223
    n214 --> n223
    n224 --> n229
    n225 --> n229
    n209 --> n212
    n223 --> n226
    n209 --> n213
    n33 --> n207
    n207 --> n208
    n207 --> n209
    n213 --> n216
    n212 --> n216
    n26 x--x n33
    n29 x--x n33
    n214 x--x n215
    n31 x--x n33
    n208 x--x n209
```

# FRA_the_council_of_rambouillet

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n231(("FRA_the_council_of_rambouillet"))
    end
```

# FRA_tools_modernisation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n104["FRA_colonial_investments"]
        n106["FRA_continue_mandat"]
        n111["FRA_develop_morocco"]
        n105(("FRA_tools_modernisation"))
    end
    subgraph tier_1["Tier 1"]
        n107["FRA_sncf"]
    end
    subgraph tier_2["Tier 2"]
        n110["FRA_develop_algeria"]
        n112["FRA_monetary_tripartite_agreement"]
    end
    subgraph tier_3["Tier 3"]
        n116["FRA_cnrs"]
        n117["FRA_develop_indochine"]
        n118["FRA_develop_tunisia"]
    end
    subgraph tier_4["Tier 4"]
        n120["FRA_buy_heavy_water"]
        n123["FRA_technology_sharing"]
    end
    subgraph tier_5["Tier 5"]
        n126["FRA_research_grants"]
        n127["FRA_sahara_oil"]
        n128["FRA_tungsten_mines"]
    end
    n116 --> n120
    n112 --> n116
    n106 --> n110
    n107 --> n110
    n111 --> n117
    n110 --> n117
    n111 --> n118
    n110 --> n118
    n107 --> n112
    n105 --> n112
    n120 --> n126
    n123 --> n127
    n105 --> n107
    n104 --> n107
    n116 --> n123
    n118 --> n123
    n123 --> n128
    n117 --> n128
```
