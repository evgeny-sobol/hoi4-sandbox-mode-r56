# NZL_allocate_resources_to_the_rnzf

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["NZL_advanced_convoy_escorts"]
        n2(("NZL_allocate_resources_to_the_rnzf"))
        n3["NZL_strenghten_british_ties"]
    end
    subgraph tier_1["Tier 1"]
        n4{"NZL_aircraft_research_group"}
        n5["NZL_construct_the_whenuapai_base"]
        n6["NZL_empire_air_training_scheme"]
        n7["NZL_pilot_recruitment_drive"]
    end
    subgraph tier_2["Tier 2"]
        n8["NZL_close_air_support"]
        n9["NZL_form_the_actual_new_zealander_airforce"]
        n10["NZL_goverment_funded_aircraft_production"]
        n11["NZL_improve_the_radars"]
        n12["NZL_tactical_bombing"]
    end
    subgraph tier_3["Tier 3"]
        n13["NZL_aircraft_engine_upgrades"]
        n14["NZL_develop_anti_air_capabilities"]
        n15["NZL_into_the_jet_age"]
        n16["NZL_taranaki_oil_field"]
        n17["NZL_womens_auxiliary_air_force"]
    end
    subgraph tier_4["Tier 4"]
        n18["NZL_long_range_patrols"]
    end
    n12 --> n13
    n8 --> n13
    n2 --> n4
    n4 --> n8
    n2 --> n5
    n11 --> n14
    n10 --> n14
    n3 --> n6
    n2 --> n6
    n7 --> n9
    n5 --> n10
    n5 --> n11
    n9 --> n15
    n13 --> n18
    n1 --> n18
    n2 --> n7
    n4 --> n12
    n10 --> n16
    n9 --> n17
    n11 --> n17
    n8 x--x n12
```

# NZL_army_review

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19(("NZL_army_review"))
        n20["NZL_serving_the_empire"]
    end
    subgraph tier_1["Tier 1"]
        n21["NZL_distribute_the_national_defense_budget"]
        n22{"NZL_expand_our_tank_warfare"}
        n23["NZL_remember_anzac"]
        n24["NZL_waiouru_excercises"]
    end
    subgraph tier_2["Tier 2"]
        n25["NZL_abandon_and_combat_enemy_armour"]
        n26["NZL_engineer_and_supply_corp"]
        n27["NZL_munition_companies_investments"]
        n28["NZL_pursue_indigenous_designs"]
        n29{"NZL_the_second_nzl_volunteer_force"}
    end
    subgraph tier_3["Tier 3"]
        n30["NZL_adapt_to_the_jungles"]
        n31["NZL_bren_transport_carrier"]
        n32["NZL_foundations_of_an_aritllery_regiment"]
        n33["NZL_hot_climate_equipment"]
        n34["NZL_motorization_efforts"]
        n35["NZL_the_charlton_rifle"]
        n36["NZL_womens_auxiliary_army"]
    end
    subgraph tier_4["Tier 4"]
        n37["NZL_a_reinvigorated_force"]
        n38["NZL_army_of_thieves"]
    end
    subgraph tier_5["Tier 5"]
        n39["NZL_conscript_the_sheep"]
        n40["NZL_new_zealand_special_forces"]
    end
    n32 --> n37
    n34 --> n37
    n35 --> n37
    n22 --> n25
    n29 --> n30
    n33 --> n38
    n30 --> n38
    n28 --> n31
    n25 --> n31
    n37 --> n39
    n19 --> n21
    n23 --> n26
    n19 --> n22
    n27 --> n32
    n29 --> n33
    n26 --> n34
    n27 --> n34
    n21 --> n27
    n24 --> n27
    n38 --> n40
    n22 --> n28
    n19 --> n23
    n27 --> n35
    n20 --> n29
    n23 --> n29
    n19 --> n24
    n26 --> n36
    n25 x--x n28
    n30 x--x n33
```

# NZL_expand_devonport

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13["NZL_aircraft_engine_upgrades"]
        n41(("NZL_expand_devonport"))
    end
    subgraph tier_1["Tier 1"]
        n42["NZL_solidify_the_new_zealand_division"]
        n43["NZL_supply_the_new_zealand_navy_divsion"]
    end
    subgraph tier_2["Tier 2"]
        n44["NZL_naval_profit"]
        n45["NZL_support_ships"]
        n46["NZL_train_new_officers"]
    end
    subgraph tier_3["Tier 3"]
        n47{"NZL_form_the_new_zealand_navy"}
    end
    subgraph tier_4["Tier 4"]
        n48["NZL_destroyer_production"]
        n49["NZL_submarine_production"]
    end
    subgraph tier_5["Tier 5"]
        n1["NZL_advanced_convoy_escorts"]
        n50["NZL_light_cruiser_effort"]
        n51["NZL_naval_equipment"]
        n52["NZL_shore_defences"]
        n53["NZL_subs"]
    end
    subgraph tier_6["Tier 6"]
        n18["NZL_long_range_patrols"]
        n54["NZL_submarine_hunters"]
        n55["NZL_unrestricted_submarine_warfare"]
    end
    n48 --> n1
    n47 --> n48
    n44 --> n47
    n45 --> n47
    n46 --> n47
    n49 --> n50
    n13 --> n18
    n1 --> n18
    n48 --> n51
    n49 --> n51
    n42 --> n44
    n48 --> n52
    n41 --> n42
    n1 --> n54
    n47 --> n49
    n49 --> n53
    n41 --> n43
    n43 --> n45
    n42 --> n45
    n42 --> n46
    n53 --> n55
    n50 --> n55
    n48 x--x n49
```

# NZL_industrialization_fund

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n56(("NZL_industrialization_fund"))
    end
    subgraph tier_1["Tier 1"]
        n57["NZL_connect_the_nation"]
        n58["NZL_end_sustenance_work"]
        n59["NZL_modernize_railways"]
    end
    subgraph tier_2["Tier 2"]
        n60{"NZL_aquire_foreign_machinery"}
        n61{"NZL_industrial_awakening"}
        n62{"NZL_modernize_hydroelectric_power"}
        n63{"NZL_the_inudtrial_segment"}
    end
    subgraph tier_3["Tier 3"]
        n64["NZL_prioritize_city_growth"]
        n65["NZL_prioritize_rural_growth"]
    end
    subgraph tier_4["Tier 4"]
        n66["NZL_expand_auckland_industrial_park"]
        n67["NZL_industrialize_christchurch"]
        n68["NZL_open_pike_river_mine"]
        n69["NZL_the_wairarapa_sheep_farms"]
    end
    subgraph tier_5["Tier 5"]
        n70["NZL_hire_physicists"]
        n71["NZL_massey_university"]
        n72["NZL_new_zealand_steel_works"]
        n73["NZL_the_wairarapa_sheep_cattle_farm"]
    end
    subgraph tier_6["Tier 6"]
        n74["NZL_the_tsunami_project"]
    end
    n58 --> n60
    n57 --> n60
    n56 --> n57
    n56 --> n58
    n64 --> n66
    n66 --> n70
    n67 --> n70
    n58 --> n61
    n57 --> n61
    n64 --> n67
    n69 --> n71
    n59 --> n62
    n57 --> n62
    n56 --> n59
    n67 --> n72
    n68 --> n72
    n65 --> n68
    n60 --> n64
    n61 --> n64
    n63 --> n64
    n62 --> n65
    n61 --> n65
    n63 --> n65
    n59 --> n63
    n57 --> n63
    n70 --> n74
    n69 --> n73
    n65 --> n69
    n64 x--x n65
```

# NZL_national_party_triumphant

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n75(("NZL_national_party_triumphant"))
        n76["NZL_the_labour_partys_reform"]
        n77["NZL_unite_communist_movements"]
    end
    subgraph tier_1["Tier 1"]
        n78["NZL_absorb_conservative_remains"]
        n79["NZL_appeal_rural_communities"]
        n80["NZL_condem_intervention"]
        n81{"NZL_the_stance_on_maori"}
    end
    subgraph tier_2["Tier 2"]
        n82["NZL_equality_conscription"]
        n83["NZL_fight_militant_worker_union"]
        n84["NZL_integrate_maori_into_new_zealand"]
        n85["NZL_maori_autonomy"]
    end
    subgraph tier_3["Tier 3"]
        n86["NZL_maori_into_economy"]
        n87["NZL_minor_native_representation_in_gov"]
        n88["NZL_protect_maori_land"]
        n89["NZL_respect_maori_culture"]
        n90["NZL_tackle_inflation"]
        n91["NZL_war_council"]
    end
    subgraph tier_4["Tier 4"]
        n92["NZL_inlist_the_maori"]
        n93["NZL_open_up_to_free_market"]
        n94["NZL_the_natives_of_new_zealand"]
    end
    subgraph tier_5["Tier 5"]
        n95["NZL_combined_intelligence_centre"]
        n96["NZL_construct_shore_fortification"]
        n97["NZL_corporate_innovations"]
        n98["NZL_the_maori_division"]
    end
    n75 --> n78
    n75 --> n79
    n93 --> n95
    n75 --> n80
    n93 --> n96
    n93 --> n97
    n80 --> n82
    n79 --> n82
    n78 --> n82
    n80 --> n83
    n79 --> n83
    n78 --> n83
    n88 --> n92
    n87 --> n92
    n81 --> n84
    n81 --> n85
    n85 --> n86
    n84 --> n87
    n90 --> n93
    n91 --> n93
    n84 --> n88
    n85 --> n89
    n83 --> n90
    n92 --> n98
    n94 --> n98
    n89 --> n94
    n86 --> n94
    n76 --> n81
    n75 --> n81
    n77 --> n81
    n82 --> n91
    n84 x--x n85
    n75 x--x n76
    n75 x--x n77
```

# NZL_open_ties_with_washington

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n99(("NZL_open_ties_with_washington"))
        n100["NZL_reaffirm_commonwelth_commitments"]
    end
    subgraph tier_1["Tier 1"]
        n101["NZL_anzus_treaty"]
        n102["NZL_ford_munition_plant"]
        n103["NZL_mutual_aid_agreement"]
    end
    n99 --> n101
    n100 --> n101
    n99 --> n102
    n99 --> n103
```

# NZL_reaffirm_commonwelth_commitments

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n99["NZL_open_ties_with_washington"]
        n100(("NZL_reaffirm_commonwelth_commitments"))
    end
    subgraph tier_1["Tier 1"]
        n101["NZL_anzus_treaty"]
        n104["NZL_australian_nzl_agreement"]
    end
    n99 --> n101
    n100 --> n101
    n100 --> n104
```

# NZL_strenghten_british_ties

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["NZL_allocate_resources_to_the_rnzf"]
        n23["NZL_remember_anzac"]
        n3(("NZL_strenghten_british_ties"))
    end
    subgraph tier_1["Tier 1"]
        n6["NZL_empire_air_training_scheme"]
        n20["NZL_serving_the_empire"]
    end
    subgraph tier_2["Tier 2"]
        n105["NZL_supply_food_stuffs"]
        n29{"NZL_the_second_nzl_volunteer_force"}
    end
    subgraph tier_3["Tier 3"]
        n30["NZL_adapt_to_the_jungles"]
        n33["NZL_hot_climate_equipment"]
    end
    subgraph tier_4["Tier 4"]
        n38["NZL_army_of_thieves"]
    end
    subgraph tier_5["Tier 5"]
        n40["NZL_new_zealand_special_forces"]
    end
    n29 --> n30
    n33 --> n38
    n30 --> n38
    n3 --> n6
    n2 --> n6
    n29 --> n33
    n38 --> n40
    n3 --> n20
    n20 --> n105
    n20 --> n29
    n23 --> n29
    n30 x--x n33
```

# NZL_the_goodwill_mission

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n106(("NZL_the_goodwill_mission"))
    end
```

# NZL_the_labour_partys_reform

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n75["NZL_national_party_triumphant"]
        n76(("NZL_the_labour_partys_reform"))
        n77["NZL_unite_communist_movements"]
    end
    subgraph tier_1["Tier 1"]
        n107["NZL_begin_lobbying_for_reforms"]
        n108["NZL_critize_uk_foreign_policy"]
        n109["NZL_frasers_leadership"]
        n81{"NZL_the_stance_on_maori"}
        n110["NZL_trust_in_the_opposition"]
    end
    subgraph tier_2["Tier 2"]
        n84["NZL_integrate_maori_into_new_zealand"]
        n111["NZL_lower_labor_wages"]
        n85["NZL_maori_autonomy"]
        n112["NZL_old_age_pension"]
        n113["NZL_public_health_service"]
        n114["NZL_rally_the_opponents"]
        n115["NZL_research_grants"]
        n116["NZL_unenmployment_benefit"]
        n117["NZL_universal_medical_benefits"]
    end
    subgraph tier_3["Tier 3"]
        n118["NZL_attempt_at_a_war_economy"]
        n86["NZL_maori_into_economy"]
        n87["NZL_minor_native_representation_in_gov"]
        n88["NZL_protect_maori_land"]
        n119["NZL_reconcile_political_opponents"]
        n89["NZL_respect_maori_culture"]
        n120["NZL_review_the_prison_system"]
        n121["NZL_silence_the_discontent"]
        n122["NZL_the_social_security_acts"]
    end
    subgraph tier_4["Tier 4"]
        n123["NZL_denounce_conservative_politicians"]
        n124["NZL_fight_for_control_over_our_soldiers"]
        n92["NZL_inlist_the_maori"]
        n125["NZL_nationalize_commerical_broadcasting"]
        n126["NZL_state_controlled_bank"]
        n94["NZL_the_natives_of_new_zealand"]
    end
    subgraph tier_5["Tier 5"]
        n127["NZL_construct_state_housing"]
        n98["NZL_the_maori_division"]
    end
    n111 --> n118
    n114 --> n118
    n76 --> n107
    n125 --> n127
    n126 --> n127
    n76 --> n108
    n119 --> n123
    n120 --> n123
    n121 --> n124
    n118 --> n124
    n76 --> n109
    n88 --> n92
    n87 --> n92
    n81 --> n84
    n109 --> n111
    n81 --> n85
    n85 --> n86
    n84 --> n87
    n122 --> n125
    n107 --> n112
    n84 --> n88
    n110 --> n113
    n109 --> n114
    n115 --> n119
    n113 --> n119
    n110 --> n115
    n85 --> n89
    n115 --> n120
    n113 --> n120
    n111 --> n121
    n114 --> n121
    n122 --> n126
    n92 --> n98
    n94 --> n98
    n89 --> n94
    n86 --> n94
    n117 --> n122
    n112 --> n122
    n116 --> n122
    n76 --> n81
    n75 --> n81
    n77 --> n81
    n76 --> n110
    n107 --> n116
    n107 --> n117
    n84 x--x n85
    n75 x--x n76
    n76 x--x n77
```

# NZL_unite_communist_movements

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n75["NZL_national_party_triumphant"]
        n76["NZL_the_labour_partys_reform"]
        n77(("NZL_unite_communist_movements"))
    end
    subgraph tier_1["Tier 1"]
        n128["NZL_invite_radical_labour_exiles"]
        n129["NZL_lobby_soviet"]
        n130["NZL_the_peoples_voice"]
        n81{"NZL_the_stance_on_maori"}
    end
    subgraph tier_2["Tier 2"]
        n84["NZL_integrate_maori_into_new_zealand"]
        n85["NZL_maori_autonomy"]
        n131["NZL_nationalize_bank"]
        n132["NZL_new_wave_of_feminism"]
    end
    subgraph tier_3["Tier 3"]
        n133["NZL_maori_equality"]
        n86["NZL_maori_into_economy"]
        n87["NZL_minor_native_representation_in_gov"]
        n88["NZL_protect_maori_land"]
        n134["NZL_public_housing"]
        n89["NZL_respect_maori_culture"]
    end
    subgraph tier_4["Tier 4"]
        n135["NZL_central_research_planning"]
        n136{"NZL_encourage_selfless_citizens"}
        n92["NZL_inlist_the_maori"]
        n94["NZL_the_natives_of_new_zealand"]
    end
    subgraph tier_5["Tier 5"]
        n137["NZL_join_sov"]
        n138["NZL_neutral"]
        n98["NZL_the_maori_division"]
    end
    n134 --> n135
    n133 --> n136
    n134 --> n136
    n88 --> n92
    n87 --> n92
    n81 --> n84
    n77 --> n128
    n136 --> n137
    n77 --> n129
    n81 --> n85
    n132 --> n133
    n85 --> n86
    n84 --> n87
    n128 --> n131
    n130 --> n131
    n129 --> n131
    n136 --> n138
    n128 --> n132
    n130 --> n132
    n129 --> n132
    n84 --> n88
    n131 --> n134
    n85 --> n89
    n92 --> n98
    n94 --> n98
    n89 --> n94
    n86 --> n94
    n77 --> n130
    n76 --> n81
    n75 --> n81
    n77 --> n81
    n84 x--x n85
    n137 x--x n138
    n75 x--x n77
    n76 x--x n77
```
