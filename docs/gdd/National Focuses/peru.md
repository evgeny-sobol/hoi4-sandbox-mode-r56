# PRU_a_reborn_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"PRU_a_reborn_navy"}
    end
    subgraph tier_1["Tier 1"]
        n2["PRU_expand_the_naval_factory_of_bellavista"]
        n3["PRU_work_with_foreigners"]
    end
    subgraph tier_2["Tier 2"]
        n4{"PRU_National_Admiralty_Corps"}
        n5{"PRU_modernize_destroyers"}
        n6["PRU_naval_industry"]
    end
    subgraph tier_3["Tier 3"]
        n7["PRU_Modernize_our_submarines"]
        n8["PRU_expand_naval_production"]
        n9["PRU_modernize_battleships"]
        n10["PRU_modernize_carrier"]
        n11["PRU_the_grau_class_project"]
    end
    subgraph tier_4["Tier 4"]
        n12["PRU_naval_doctrine"]
    end
    n4 --> n7
    n2 --> n4
    n3 --> n4
    n6 --> n8
    n1 --> n2
    n5 --> n9
    n5 --> n10
    n3 --> n5
    n2 --> n5
    n8 --> n12
    n2 --> n6
    n3 --> n6
    n4 --> n11
    n1 --> n3
    n7 x--x n11
    n2 x--x n3
    n9 x--x n10
```

# PRU_czech_equipment_aquisition

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13(("PRU_czech_equipment_aquisition"))
        n14["PRU_start_aircraft_purchase"]
    end
    subgraph tier_1["Tier 1"]
        n15["PRU_andean_warfare"]
        n16["PRU_czech_tanks"]
        n17["PRU_italian_guns"]
    end
    subgraph tier_2["Tier 2"]
        n18["PRU_create_the_infantry_and_cavalry_schools"]
        n19["PRU_expand_the_national_arsenal"]
        n20["PRU_foreign_licenses"]
        n21["PRU_invite_italian_military_mission"]
        n22["PRU_invite_soviet_military_mission"]
        n23["PRU_modernize_the_infantry_kit"]
        n24["PRU_paratrooper_company"]
        n25["PRU_study_the_blueprints"]
    end
    subgraph tier_3["Tier 3"]
        n26["PRU_include_llamas_in_the_army"]
        n27["PRU_jungle_training"]
        n28["PRU_motorization"]
        n29["PRU_new_weapons_new_tactics"]
    end
    subgraph tier_4["Tier 4"]
        n30["PRU_reformed_logistics"]
    end
    n13 --> n15
    n15 --> n18
    n13 --> n16
    n17 --> n19
    n16 --> n20
    n18 --> n26
    n17 --> n21
    n17 --> n22
    n13 --> n17
    n23 --> n27
    n15 --> n23
    n23 --> n28
    n18 --> n28
    n19 --> n29
    n25 --> n29
    n15 --> n24
    n14 --> n24
    n27 --> n30
    n28 --> n30
    n16 --> n25
```

# PRU_diversify_steel_production

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n31{"PRU_diversify_steel_production"}
        n32{"PRU_enlarge_paita_seaport"}
        n33["PRU_invite_foreign_experts"]
        n34["PRU_rely_on_international_trade"]
    end
    subgraph tier_1["Tier 1"]
        n35["PRU_prioritize_self_sufficiency"]
    end
    subgraph tier_2["Tier 2"]
        n36{"PRU_bolster_the_timber_industry"}
        n37["PRU_construct_the_pan_american_highway"]
        n38["PRU_finalize_transition_from_libra_to_sol_de_oro"]
        n39{"PRU_finish_callahuanca_hydroelectric_plant"}
        n40["PRU_foundation_for_the_urban_normal_school"]
        n41["PRU_support_private_resource_ventures"]
        n42["PRU_talara_refinery_expansion"]
    end
    subgraph tier_3["Tier 3"]
        n43["PRU_bring_education_to_the_countryside"]
        n44["PRU_economic_centralization"]
        n45["PRU_end_the_lima_arequipa_rivalry"]
        n46["PRU_expand_gold_and_silver_mining"]
        n47["PRU_seize_foreign_businesses"]
        n48["PRU_settle_amazonian_frontier"]
        n49["PRU_subsidize_rubber_production"]
        n50["PRU_supplement_zinc_and_lead_concentrators"]
    end
    subgraph tier_4["Tier 4"]
        n51["PRU_yearname_organic_law_of_education"]
    end
    n34 --> n36
    n35 --> n36
    n40 --> n43
    n34 --> n37
    n35 --> n37
    n32 --> n44
    n39 --> n44
    n39 --> n45
    n36 --> n45
    n41 --> n46
    n34 --> n38
    n35 --> n38
    n34 --> n39
    n35 --> n39
    n35 --> n40
    n31 --> n35
    n41 --> n47
    n35 --> n47
    n36 --> n48
    n41 --> n49
    n41 --> n50
    n34 --> n41
    n35 --> n41
    n35 --> n42
    n33 --> n51
    n44 --> n51
    n45 --> n51
    n44 x--x n45
    n35 x--x n34
```

# PRU_fly_with_the_sun

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15["PRU_andean_warfare"]
        n52(("PRU_fly_with_the_sun"))
    end
    subgraph tier_1["Tier 1"]
        n14{"PRU_start_aircraft_purchase"}
        n53["PRU_strengthen_the_air_force"]
        n54{"PRU_work_with_our_designs"}
    end
    subgraph tier_2["Tier 2"]
        n55["PRU_acquire_italian_planes"]
        n56["PRU_acquire_usa_planes"]
        n57["PRU_air_innovations"]
        n24["PRU_paratrooper_company"]
        n58["PRU_total_production"]
        n59["PRU_work_on_heavy_aircraft"]
        n60["PRU_work_on_light_aircraft"]
    end
    subgraph tier_3["Tier 3"]
        n61["PRU_heroes_of_the_air"]
    end
    n14 --> n55
    n14 --> n56
    n53 --> n57
    n57 --> n61
    n58 --> n61
    n15 --> n24
    n14 --> n24
    n52 --> n14
    n52 --> n53
    n53 --> n58
    n54 --> n59
    n54 --> n60
    n52 --> n54
    n55 x--x n56
    n59 x--x n60
```

# PRU_industrial_modernization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n62{"PRU_industrial_modernization"}
        n63{"PRU_maranon_basin_model"}
        n35["PRU_prioritize_self_sufficiency"]
    end
    subgraph tier_1["Tier 1"]
        n34["PRU_rely_on_international_trade"]
        n64["PRU_strengthen_locomotive_industry"]
    end
    subgraph tier_2["Tier 2"]
        n36{"PRU_bolster_the_timber_industry"}
        n65["PRU_centralize_the_railway_network"]
        n37["PRU_construct_the_pan_american_highway"]
        n32{"PRU_enlarge_paita_seaport"}
        n38["PRU_finalize_transition_from_libra_to_sol_de_oro"]
        n39{"PRU_finish_callahuanca_hydroelectric_plant"}
        n33["PRU_invite_foreign_experts"]
        n41["PRU_support_private_resource_ventures"]
    end
    subgraph tier_3["Tier 3"]
        n44["PRU_economic_centralization"]
        n45["PRU_end_the_lima_arequipa_rivalry"]
        n46["PRU_expand_gold_and_silver_mining"]
        n47["PRU_seize_foreign_businesses"]
        n48["PRU_settle_amazonian_frontier"]
        n49["PRU_subsidize_rubber_production"]
        n50["PRU_supplement_zinc_and_lead_concentrators"]
    end
    subgraph tier_4["Tier 4"]
        n51["PRU_yearname_organic_law_of_education"]
    end
    n34 --> n36
    n35 --> n36
    n64 --> n65
    n34 --> n37
    n35 --> n37
    n32 --> n44
    n39 --> n44
    n39 --> n45
    n36 --> n45
    n34 --> n32
    n41 --> n46
    n34 --> n38
    n35 --> n38
    n34 --> n39
    n35 --> n39
    n34 --> n33
    n62 --> n34
    n63 --> n34
    n41 --> n47
    n35 --> n47
    n36 --> n48
    n62 --> n64
    n41 --> n49
    n41 --> n50
    n34 --> n41
    n35 --> n41
    n33 --> n51
    n44 --> n51
    n45 --> n51
    n44 x--x n45
    n35 x--x n34
```

# PRU_look_to_the_past

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n66["PRU_give_power_to_general_ureta"]
        n67(("PRU_look_to_the_past"))
        n68["PRU_organize_future_elections"]
        n69["PRU_peruvian_blackshirts"]
    end
    subgraph tier_1["Tier 1"]
        n70{"PRU_delay_elections"}
    end
    subgraph tier_2["Tier 2"]
        n71{"PRU_appoint_a_peruvian_monarch"}
        n72{"PRU_invite_carlos"}
        n73["PRU_the_problem_of_the_quechuas"]
    end
    subgraph tier_3["Tier 3"]
        n74{"PRU_hispanism"}
        n75["PRU_labour_reforms"]
        n76["PRU_negotiate_with_communal_chiefs"]
        n77["PRU_restore_the_viceroyalty_system"]
        n78["PRU_royal_haciendas"]
        n79["PRU_the_owners_of_the_mountains"]
        n80["PRU_the_rebel_inca"]
    end
    subgraph tier_4["Tier 4"]
        n81["PRU_Convince_supporters_of_Flores"]
        n82["PRU_alliance_with_spain"]
        n83["PRU_appoint_new_quechua_soldiers"]
        n84{"PRU_hispanic_union"}
        n85{"PRU_legacy_of_guayaquil_treaty"}
        n86["PRU_look_to_the_past_2"]
        n87["PRU_prepare_for_another_pacific_war"]
        n88["PRU_runan_caycu"]
        n89["PRU_spanish_civil_war_involvement"]
    end
    subgraph tier_5["Tier 5"]
        n90["PRU_Support_the_Catholic_Church"]
        n91{"PRU_Support_the_banana_industry"}
        n92["PRU_organize_marches_in_the_north"]
        n93["PRU_reclaim_chile"]
        n94["PRU_reclaim_ecuador"]
        n95{"PRU_secure_the_central_america"}
        n96["PRU_secure_the_northern_road_network"]
        n97{"PRU_the_inca_congress"}
    end
    subgraph tier_6["Tier 6"]
        n98["PRU_alliance_with_mexico"]
        n99["PRU_crown_an_inca"]
        n100["PRU_launch_the_coup"]
        n101["PRU_reclaim_colombia"]
        n102["PRU_red_pachamama"]
        n103["PRU_regain_the_new_spain_heritage"]
        n104["PRU_strengthen_nationalist_rhetoric"]
        n105["PRU_the_only_sun"]
    end
    subgraph tier_7["Tier 7"]
        n106["PRU_Collectivize_the_land"]
        n107["PRU_Create_the_Royal_Army"]
        n108["PRU_The_Soldier_King"]
        n109["PRU_convince_the_high_command"]
        n110["PRU_illapa_the_thunder_of_the_andes"]
        n111["PRU_reclaim_venezuela"]
        n112["PRU_reject_international_ideologies"]
        n113["PRU_secure_plata_states"]
        n114["PRU_secure_the_future_of_the_nation"]
    end
    subgraph tier_8["Tier 8"]
        n115{"PRU_Acquire_French_weapons"}
        n116{"PRU_Royal_Construction_Program"}
        n117{"PRU_integrate_the_Quechuas_into_the_army"}
        n118["PRU_organize_protests_in_the_south"]
        n119["PRU_revolutionary_andes"]
        n120["PRU_the_true_owners_of_america"]
    end
    subgraph tier_9["Tier 9"]
        n121["PRU_defend_our_empire"]
        n122["PRU_huayna_capac_heritage"]
        n123["PRU_liberate_the_indigenous_people_of_america"]
        n124["PRU_reclaim_bolivia"]
        n125["PRU_retake_antofagasta"]
        n126["PRU_sons_of_the_conquistador"]
        n127["PRU_the_march_of_the_four_suyos"]
    end
    subgraph tier_10["Tier 10"]
        n128["PRU_create_orejones_battalions"]
        n129["PRU_form_the_royal_guard_of_Peru"]
        n130["PRU_give_arms_to_the_people"]
        n131["PRU_integrate_the_northern_realm"]
        n132["PRU_militarize_the_homeland"]
        n133["PRU_recreate_the_Inca_farming_system"]
        n134["PRU_unite_with_diaguita_and_toconote"]
    end
    subgraph tier_11["Tier 11"]
        n135["PRU_Receive_refugees_from_the_Spanish_civil_war"]
        n136["PRU_inca_heavy_industry"]
        n137["PRU_knights_of_the_new_world"]
        n138["PRU_nationalize_the_industry"]
        n139["PRU_restore_the_kanchas"]
        n140["PRU_secure_the_southern_Andes"]
    end
    subgraph tier_12["Tier 12"]
        n141["PRU_adquire_american_industry"]
        n142["PRU_call_british_sailors"]
        n143["PRU_monumental_architecture"]
        n144["PRU_viva_el_rey"]
    end
    subgraph tier_13["Tier 13"]
        n145["PRU_contact_pedro"]
        n146["PRU_establish_the_mitimaes"]
        n147["PRU_restore_the_borders_of_the_empire"]
        n148["PRU_return_to_europe"]
        n149["PRU_secure_the_coast"]
    end
    subgraph tier_14["Tier 14"]
        n150{"PRU_create_the_united_kingdom_of_spain"}
        n151{"PRU_expel_europeans_from_south_america"}
        n152["PRU_restore_the_empire"]
        n153["PRU_return_of_the_inkari"]
    end
    subgraph tier_15["Tier 15"]
        n154["PRU_claim_the_habsburg_territories"]
        n155["PRU_claim_the_portuguese_empire"]
        n156["PRU_new_world_army"]
        n157["PRU_restore_the_argentina_empire"]
        n158["PRU_restore_the_colombia_empire"]
        n159["PRU_the_pact_of_lima"]
        n160["PRU_unified_by_will"]
        n161["PRU_unified_in_spirit"]
    end
    subgraph tier_16["Tier 16"]
        n162["PRU_america_imperial"]
        n163["PRU_call_hans"]
        n164{"PRU_das_inkareich"}
        n165["PRU_the_new_royal_road"]
    end
    subgraph tier_17["Tier 17"]
        n166["PRU_A_new_war_machine"]
        n167["PRU_american_reich"]
        n168["PRU_recognize_german_power"]
        n169["PRU_recognize_german_power_2"]
    end
    n165 --> n166
    n163 --> n166
    n108 --> n115
    n102 --> n106
    n77 --> n81
    n78 --> n81
    n75 --> n81
    n100 --> n107
    n132 --> n135
    n107 --> n116
    n81 --> n90
    n86 --> n90
    n84 --> n91
    n100 --> n108
    n139 --> n141
    n95 --> n98
    n91 --> n98
    n74 --> n82
    n158 --> n162
    n157 --> n162
    n164 --> n167
    n70 --> n71
    n80 --> n83
    n76 --> n83
    n136 --> n142
    n159 --> n163
    n150 --> n154
    n150 --> n155
    n144 --> n145
    n99 --> n109
    n127 --> n128
    n148 --> n150
    n97 --> n99
    n156 --> n164
    n117 --> n121
    n115 --> n121
    n67 --> n70
    n141 --> n146
    n147 --> n151
    n126 --> n129
    n121 --> n129
    n126 --> n130
    n121 --> n130
    n74 --> n84
    n69 --> n74
    n66 --> n74
    n72 --> n74
    n115 --> n122
    n118 --> n122
    n119 --> n122
    n120 --> n122
    n102 --> n110
    n104 --> n110
    n128 --> n136
    n133 --> n136
    n107 --> n117
    n108 --> n117
    n122 --> n131
    n70 --> n72
    n130 --> n137
    n71 --> n75
    n92 --> n100
    n96 --> n100
    n90 --> n100
    n74 --> n85
    n118 --> n123
    n120 --> n123
    n119 --> n123
    n77 --> n86
    n78 --> n86
    n75 --> n86
    n126 --> n132
    n121 --> n132
    n136 --> n143
    n139 --> n143
    n129 --> n138
    n73 --> n76
    n153 --> n156
    n81 --> n92
    n86 --> n92
    n112 --> n118
    n109 --> n118
    n74 --> n87
    n115 --> n124
    n118 --> n124
    n119 --> n124
    n120 --> n124
    n87 --> n93
    n94 --> n101
    n85 --> n94
    n101 --> n111
    n164 --> n168
    n164 --> n169
    n127 --> n133
    n97 --> n102
    n95 --> n103
    n91 --> n103
    n99 --> n112
    n152 --> n157
    n143 --> n147
    n152 --> n158
    n145 --> n152
    n128 --> n139
    n133 --> n139
    n72 --> n77
    n115 --> n125
    n118 --> n125
    n119 --> n125
    n120 --> n125
    n147 --> n153
    n144 --> n148
    n110 --> n119
    n106 --> n119
    n72 --> n78
    n71 --> n78
    n80 --> n88
    n79 --> n88
    n105 --> n113
    n84 --> n95
    n85 --> n95
    n142 --> n149
    n104 --> n114
    n81 --> n96
    n86 --> n96
    n134 --> n140
    n117 --> n126
    n116 --> n126
    n74 --> n89
    n97 --> n104
    n88 --> n97
    n83 --> n97
    n118 --> n127
    n120 --> n127
    n119 --> n127
    n159 --> n165
    n93 --> n105
    n73 --> n79
    n153 --> n159
    n70 --> n73
    n73 --> n80
    n114 --> n120
    n110 --> n120
    n151 --> n160
    n151 --> n161
    n124 --> n134
    n125 --> n134
    n138 --> n144
    n137 --> n144
    n135 --> n144
    n91 x--x n95
    n98 x--x n103
    n167 x--x n168
    n71 x--x n72
    n71 x--x n73
    n154 x--x n155
    n99 x--x n102
    n99 x--x n104
    n121 x--x n126
    n84 x--x n85
    n84 x--x n87
    n72 x--x n73
    n75 x--x n77
    n75 x--x n78
    n67 x--x n68
    n102 x--x n104
    n77 x--x n78
    n160 x--x n161
```

# PRU_maranon_basin_model

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n62{"PRU_industrial_modernization"}
        n63{"PRU_maranon_basin_model"}
        n35["PRU_prioritize_self_sufficiency"]
    end
    subgraph tier_1["Tier 1"]
        n34["PRU_rely_on_international_trade"]
    end
    subgraph tier_2["Tier 2"]
        n36{"PRU_bolster_the_timber_industry"}
        n37["PRU_construct_the_pan_american_highway"]
        n32{"PRU_enlarge_paita_seaport"}
        n38["PRU_finalize_transition_from_libra_to_sol_de_oro"]
        n39{"PRU_finish_callahuanca_hydroelectric_plant"}
        n33["PRU_invite_foreign_experts"]
        n41["PRU_support_private_resource_ventures"]
    end
    subgraph tier_3["Tier 3"]
        n44["PRU_economic_centralization"]
        n45["PRU_end_the_lima_arequipa_rivalry"]
        n46["PRU_expand_gold_and_silver_mining"]
        n47["PRU_seize_foreign_businesses"]
        n48["PRU_settle_amazonian_frontier"]
        n49["PRU_subsidize_rubber_production"]
        n50["PRU_supplement_zinc_and_lead_concentrators"]
    end
    subgraph tier_4["Tier 4"]
        n51["PRU_yearname_organic_law_of_education"]
    end
    n34 --> n36
    n35 --> n36
    n34 --> n37
    n35 --> n37
    n32 --> n44
    n39 --> n44
    n39 --> n45
    n36 --> n45
    n34 --> n32
    n41 --> n46
    n34 --> n38
    n35 --> n38
    n34 --> n39
    n35 --> n39
    n34 --> n33
    n62 --> n34
    n63 --> n34
    n41 --> n47
    n35 --> n47
    n36 --> n48
    n41 --> n49
    n41 --> n50
    n34 --> n41
    n35 --> n41
    n33 --> n51
    n44 --> n51
    n45 --> n51
    n44 x--x n45
    n35 x--x n34
```

# PRU_organize_future_elections

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n72["PRU_invite_carlos"]
        n67["PRU_look_to_the_past"]
        n68(("PRU_organize_future_elections"))
    end
    subgraph tier_1["Tier 1"]
        n170{"PRU_empower_benavides"}
        n171["PRU_legacy_of_sachez_cerro"]
        n172["PRU_mediate_between_the_parties"]
    end
    subgraph tier_2["Tier 2"]
        n173["PRU_alerta_en_la_frontera"]
        n174["PRU_conservative_coalition"]
        n175["PRU_freedom_defenders"]
        n66{"PRU_give_power_to_general_ureta"}
        n176["PRU_new_road_conscription_law"]
        n69{"PRU_peruvian_blackshirts"}
        n177{"PRU_prolong_benavides_presidency"}
        n178["PRU_protest_against_the_cancellation"]
        n179["PRU_social_democratic_coalition"]
    end
    subgraph tier_3["Tier 3"]
        n180["PRU_Acquire_Japanese_weapons"]
        n181["PRU_Eradicate_the_traitors"]
        n182["PRU_Military_Universities"]
        n183["PRU_Return_to_Negotiate_with_Caproni"]
        n184["PRU_The_People_General"]
        n185["PRU_american_naval_doctrine"]
        n186{"PRU_benavides_nightmare"}
        n187["PRU_british_airports"]
        n188["PRU_commit_to_democratic_election"]
        n189["PRU_give_rights_to_indigenous_people"]
        n74{"PRU_hispanism"}
        n190{"PRU_incaism"}
        n191["PRU_mobilize_womans"]
        n192["PRU_protect_democratic_institutions"]
        n193["PRU_recover_from_the_economic_crisis"]
        n194{"PRU_select_a_successor_for_benavides"}
    end
    subgraph tier_4["Tier 4"]
        n195["PRU_Promote_immigration"]
        n196["PRU_alliance_with_bolivia"]
        n82["PRU_alliance_with_spain"]
        n197["PRU_exile_haya_de_la_torre"]
        n198["PRU_exile_luis_alberto_flores"]
        n199{"PRU_give_asylum_to_the_jews"}
        n200["PRU_help_our_brothers"]
        n84{"PRU_hispanic_union"}
        n201["PRU_integrate_the_church"]
        n202["PRU_leacy_of_Benavides"]
        n85{"PRU_legacy_of_guayaquil_treaty"}
        n203["PRU_legacy_of_the_war_with_ecuador"]
        n87["PRU_prepare_for_another_pacific_war"]
        n204["PRU_remember_the_Trujillo_revolution"]
        n205["PRU_revolutionary_goverment"]
        n206["PRU_select_montagne_as_successor"]
        n89["PRU_spanish_civil_war_involvement"]
        n207{"PRU_the_teachings_the_amauta"}
        n208["PRU_unite_the_andes"]
        n209{"PRU_workers_protection"}
        n210["PRU_workers_rights_act"]
    end
    subgraph tier_5["Tier 5"]
        n211["PRU_Recovering_from_the_civil_war"]
        n91{"PRU_Support_the_banana_industry"}
        n212["PRU_ask_for_enter_to_comintern"]
        n213["PRU_celebration_of_the_andean_past"]
        n214["PRU_crusade_against_radicalism_in_america"]
        n215["PRU_develop_the_provinces"]
        n216["PRU_increase_social_spending"]
        n217["PRU_industrial_cooperation"]
        n218["PRU_left_and_right_united"]
        n219["PRU_legacy_of_pachacutec"]
        n220["PRU_nationalize_the_banking_sector"]
        n221["PRU_our_revolution"]
        n93["PRU_reclaim_chile"]
        n94["PRU_reclaim_ecuador"]
        n222["PRU_reform_the_constitution"]
        n95{"PRU_secure_the_central_america"}
        n223["PRU_tax_reform"]
    end
    subgraph tier_6["Tier 6"]
        n224["PRU_Legion_Peruana"]
        n225["PRU_adean_commissars"]
        n98["PRU_alliance_with_mexico"]
        n226["PRU_collective_agriculture"]
        n227["PRU_create_apra"]
        n228["PRU_expand_the_agricultural_sector"]
        n229["PRU_follow_in_the_footsteps_of_tupac_amaru"]
        n230["PRU_god_country_and_family"]
        n231["PRU_inca_industry"]
        n232["PRU_integrate_the_indigenous"]
        n233["PRU_neo_incaic_unification"]
        n234["PRU_peruvian_military_youth"]
        n101["PRU_reclaim_colombia"]
        n235["PRU_reforma_agraria"]
        n103["PRU_regain_the_new_spain_heritage"]
        n236["PRU_research_cooperation"]
        n237["PRU_state_serves_the_people"]
        n238["PRU_strengthen_the_national_industry"]
        n105["PRU_the_only_sun"]
        n239["PRU_the_peruvian_five_year_plan"]
    end
    subgraph tier_7["Tier 7"]
        n240["PRU_Nationalize_the_brea_y_parinas"]
        n241["PRU_a_new_peru"]
        n242["PRU_aprista_guerrilla"]
        n243["PRU_consolidate_borders"]
        n244["PRU_control_the_economy"]
        n245["PRU_expand_the_military_industry"]
        n246["PRU_expand_the_volunteer_program"]
        n247["PRU_give_power_to_cgtp"]
        n248["PRU_national_investigation"]
        n249["PRU_nationalize_banking_sector"]
        n250["PRU_promote_the_military_industry"]
        n251["PRU_promote_the_national_industry"]
        n252["PRU_public_universities"]
        n253["PRU_radicalize_the_pcp"]
        n111["PRU_reclaim_venezuela"]
        n254["PRU_request_soviet_support"]
        n113["PRU_secure_plata_states"]
        n255["PRU_the_great_peruvian_red_army"]
    end
    subgraph tier_8["Tier 8"]
        n256["PRU_Bring_the_revolution_to_all_America"]
        n257["PRU_Sovereign_Industrial_Expansion"]
        n258["PRU_acquire_soviet_plane_factories"]
        n259["PRU_acquire_soviet_tanks"]
        n260{"PRU_benavides_is_dead"}
        n261["PRU_end_capitalism"]
        n262{"PRU_food_importation"}
        n263{"PRU_hasta_quemar_el_ultimo_cartucho"}
        n264{"PRU_integrate_women"}
        n265["PRU_open_universities_to_indigenous_people"]
        n266["PRU_rallying_the_peasants"]
        n267["PRU_revive_the_bolivarian_dream"]
        n268["PRU_revolutionary_vanguard"]
        n269["PRU_riva_agueros_dream"]
        n270{"PRU_wake_up_a_giant"}
    end
    subgraph tier_9["Tier 9"]
        n271["PRU_arm_the_people"]
        n272{"PRU_create_the_Lima_group"}
        n273["PRU_hit_bolivia"]
        n274["PRU_inti_raymi"]
        n275{"PRU_join_allies"}
        n276["PRU_join_axis"]
        n277["PRU_liberate_brazil"]
        n278["PRU_national_literacy_programs"]
        n279["PRU_place_odria_as_adviser"]
        n280["PRU_revolucion_restauradora"]
        n281["PRU_the_memory_of_benavides"]
        n282["PRU_the_victory_of_our_caudillo"]
        n283["PRU_trans_pacific_alliance"]
        n284["PRU_unite_the_ecuadorian_proletariat"]
    end
    subgraph tier_10["Tier 10"]
        n285["PRU_attack_germany"]
        n286["PRU_attack_japan"]
        n287["PRU_drive_out_the_banana_companies"]
        n288{"PRU_expel_the_reds_from_america"}
        n289["PRU_german_aeronautic_cooperation"]
        n290["PRU_hit_argentina"]
        n291["PRU_hit_chile"]
        n292["PRU_japanece_naval_doctrine"]
        n293["PRU_liberate_cub"]
        n294["PRU_ochenio_de_Odria"]
        n295["PRU_oil_infrastructure_expansion"]
        n296["PRU_standard_oil_refinery_initiative"]
    end
    subgraph tier_11["Tier 11"]
        n297["PRU_German_investment_in_the_military_industry"]
        n298["PRU_The_new_South_american_axis"]
        n299["PRU_a_new_military_doctrine"]
        n300["PRU_create_the_national_education_fund"]
        n301["PRU_hit_colombia"]
        n302["PRU_hit_ecuador"]
        n303["PRU_hit_venezuela"]
        n304["PRU_japanese_investment_in_the_naval_industry"]
        n305["PRU_liberate_all_cab"]
        n306["PRU_long_live_our_caudillo"]
        n307["PRU_privatize_the_public_service"]
        n308["PRU_the_new_oil_law"]
        n309["PRU_union_with_the_pcv"]
    end
    subgraph tier_12["Tier 12"]
        n310["PRU_american_fascist_union"]
        n311["PRU_great_national_construction_program"]
        n312["PRU_invite_german_military_advisors"]
        n313["PRU_invite_japanese_naval_advisors"]
        n314["PRU_mandatory_social_security"]
        n315["PRU_oil_deal_with_the_united_states"]
        n316["PRU_protect_our_businesses"]
        n317["PRU_the_final_march"]
    end
    subgraph tier_13["Tier 13"]
        n318["PRU_eliminate_the_competition"]
        n319["PRU_expand_the_oil_industry"]
        n320["PRU_the_empire_of_the_constitution"]
        n321["PRU_the_great_world_revolution"]
        n322["PRU_womens_right_to_vote"]
    end
    n66 --> n180
    n69 --> n180
    n252 --> n256
    n69 --> n181
    n289 --> n297
    n219 --> n224
    n179 --> n182
    n225 --> n240
    n226 --> n240
    n180 --> n195
    n183 --> n195
    n198 --> n211
    n66 --> n183
    n69 --> n183
    n244 --> n257
    n84 --> n91
    n66 --> n184
    n288 --> n298
    n292 --> n299
    n289 --> n299
    n232 --> n241
    n255 --> n258
    n255 --> n259
    n212 --> n225
    n172 --> n173
    n190 --> n196
    n95 --> n98
    n91 --> n98
    n74 --> n82
    n306 --> n310
    n298 --> n310
    n175 --> n185
    n227 --> n242
    n266 --> n271
    n207 --> n212
    n199 --> n212
    n275 --> n285
    n272 --> n285
    n275 --> n286
    n272 --> n286
    n250 --> n260
    n251 --> n260
    n178 --> n186
    n174 --> n187
    n196 --> n213
    n212 --> n226
    n177 --> n188
    n172 --> n174
    n231 --> n243
    n231 --> n244
    n236 --> n244
    n221 --> n227
    n264 --> n272
    n262 --> n272
    n294 --> n300
    n197 --> n214
    n198 --> n214
    n208 --> n215
    n284 --> n287
    n316 --> n318
    n317 --> n318
    n68 --> n170
    n253 --> n261
    n188 --> n197
    n188 --> n198
    n211 --> n228
    n235 --> n245
    n316 --> n319
    n238 --> n246
    n274 --> n288
    n221 --> n229
    n246 --> n262
    n248 --> n262
    n172 --> n175
    n276 --> n289
    n189 --> n199
    n239 --> n247
    n171 --> n66
    n179 --> n189
    n223 --> n230
    n308 --> n311
    n300 --> n311
    n243 --> n263
    n249 --> n263
    n186 --> n200
    n74 --> n84
    n69 --> n74
    n66 --> n74
    n72 --> n74
    n273 --> n290
    n270 --> n273
    n256 --> n273
    n260 --> n273
    n273 --> n291
    n290 --> n301
    n291 --> n301
    n290 --> n302
    n291 --> n302
    n290 --> n303
    n291 --> n303
    n215 --> n231
    n69 --> n190
    n66 --> n190
    n204 --> n216
    n196 --> n217
    n187 --> n201
    n222 --> n232
    n246 --> n264
    n248 --> n264
    n263 --> n274
    n297 --> n312
    n299 --> n312
    n304 --> n313
    n299 --> n313
    n283 --> n292
    n292 --> n304
    n264 --> n275
    n262 --> n275
    n263 --> n276
    n191 --> n202
    n209 --> n218
    n199 --> n218
    n74 --> n85
    n208 --> n219
    n206 --> n219
    n205 --> n219
    n68 --> n171
    n185 --> n203
    n193 --> n203
    n293 --> n305
    n256 --> n277
    n277 --> n293
    n271 --> n293
    n288 --> n306
    n300 --> n314
    n68 --> n172
    n174 --> n191
    n238 --> n248
    n259 --> n278
    n258 --> n278
    n231 --> n249
    n236 --> n249
    n207 --> n220
    n217 --> n233
    n213 --> n233
    n172 --> n176
    n280 --> n294
    n308 --> n315
    n282 --> n295
    n244 --> n265
    n204 --> n221
    n171 --> n69
    n211 --> n234
    n222 --> n234
    n270 --> n279
    n74 --> n87
    n296 --> n307
    n295 --> n307
    n170 --> n177
    n228 --> n250
    n228 --> n251
    n176 --> n192
    n307 --> n316
    n170 --> n178
    n229 --> n252
    n226 --> n253
    n252 --> n266
    n87 --> n93
    n94 --> n101
    n85 --> n94
    n101 --> n111
    n175 --> n193
    n206 --> n222
    n205 --> n222
    n220 --> n235
    n216 --> n235
    n95 --> n103
    n91 --> n103
    n186 --> n204
    n239 --> n254
    n217 --> n236
    n213 --> n236
    n229 --> n267
    n254 --> n267
    n263 --> n280
    n270 --> n280
    n260 --> n280
    n194 --> n205
    n254 --> n268
    n247 --> n268
    n229 --> n268
    n241 --> n269
    n105 --> n113
    n84 --> n95
    n85 --> n95
    n177 --> n194
    n194 --> n206
    n172 --> n179
    n74 --> n89
    n282 --> n296
    n218 --> n237
    n218 --> n238
    n223 --> n238
    n201 --> n223
    n202 --> n223
    n314 --> n320
    n302 --> n317
    n301 --> n317
    n303 --> n317
    n225 --> n255
    n317 --> n321
    n305 --> n321
    n260 --> n281
    n294 --> n308
    n93 --> n105
    n212 --> n239
    n186 --> n207
    n270 --> n282
    n263 --> n283
    n287 --> n309
    n190 --> n208
    n267 --> n284
    n241 --> n270
    n311 --> n322
    n315 --> n322
    n182 --> n209
    n192 --> n210
    n193 --> n210
    n180 x--x n183
    n91 x--x n95
    n298 x--x n306
    n196 x--x n208
    n98 x--x n103
    n212 x--x n218
    n285 x--x n286
    n188 x--x n194
    n272 x--x n275
    n84 x--x n85
    n84 x--x n87
    n274 x--x n276
    n274 x--x n280
    n274 x--x n283
    n276 x--x n280
    n276 x--x n283
    n67 x--x n68
    n279 x--x n280
    n177 x--x n178
    n204 x--x n207
    n280 x--x n283
    n205 x--x n206
```
