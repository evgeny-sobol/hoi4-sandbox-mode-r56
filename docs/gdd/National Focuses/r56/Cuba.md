# CUB_air_base_expansion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CUB_air_base_expansion"))
        n2["CUB_caribbean_navy"]
    end
    subgraph tier_1["Tier 1"]
        n3{"CUB_air_innovations"}
        n4{"CUB_fighter_modernisation"}
        n5["CUB_rectify_the_injustice"]
    end
    subgraph tier_2["Tier 2"]
        n6{"CUB_heavy_fighter_concept"}
        n7["CUB_naval_bomber_experiments"]
    end
    subgraph tier_3["Tier 3"]
        n8["CUB_light_bomber_focus"]
        n9["CUB_medium_bomber_focus"]
    end
    subgraph tier_4["Tier 4"]
        n10["CUB_air_modernisations_programme"]
    end
    subgraph tier_5["Tier 5"]
        n11["CUB_rocket_development"]
    end
    n1 --> n3
    n8 --> n10
    n9 --> n10
    n1 --> n4
    n3 --> n6
    n4 --> n6
    n6 --> n8
    n4 --> n8
    n6 --> n9
    n3 --> n9
    n3 --> n7
    n1 --> n5
    n2 --> n5
    n10 --> n11
    n8 x--x n9
```

# CUB_caribbean_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["CUB_air_base_expansion"]
        n2(("CUB_caribbean_navy"))
    end
    subgraph tier_1["Tier 1"]
        n12["CUB_import_submarine_technology"]
        n5["CUB_rectify_the_injustice"]
        n13["CUB_study_foreign_built_ships"]
    end
    subgraph tier_2["Tier 2"]
        n14["CUB_a_cruiser_navy"]
        n15["CUB_commerce_attack"]
        n16{"CUB_the_twin_threats"}
    end
    subgraph tier_3["Tier 3"]
        n17["CUB_coastal_defense"]
        n18["CUB_strike_force"]
    end
    subgraph tier_4["Tier 4"]
        n19["CUB_naval_equipment"]
    end
    n13 --> n14
    n16 --> n17
    n12 --> n15
    n2 --> n12
    n18 --> n19
    n17 --> n19
    n1 --> n5
    n2 --> n5
    n16 --> n18
    n2 --> n13
    n12 --> n16
    n13 --> n16
    n17 x--x n18
```

# CUB_maximo_gomez_command_academy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20(("CUB_maximo_gomez_command_academy"))
    end
    subgraph tier_1["Tier 1"]
        n21["CUB_motorized_army"]
        n22["CUB_study_foreign_tanks"]
        n23["CUB_weapon_modernisation"]
    end
    subgraph tier_2["Tier 2"]
        n24["CUB_improve_army_logistics"]
        n25["CUB_study_new_land_doctrines"]
    end
    subgraph tier_3["Tier 3"]
        n26["CUB_cruisers_experiments"]
        n27["CUB_elite_tank_forces"]
        n28["CUB_special_forces"]
    end
    subgraph tier_4["Tier 4"]
        n29["CUB_army_modernisation"]
        n30["CUB_jungle_specialization"]
    end
    n27 --> n29
    n28 --> n29
    n24 --> n26
    n24 --> n27
    n22 --> n24
    n21 --> n24
    n28 --> n30
    n20 --> n21
    n25 --> n28
    n20 --> n22
    n21 --> n25
    n23 --> n25
    n20 --> n23
```

# CUB_results_of_the_presidential_election

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n31{"CUB_results_of_the_presidential_election"}
    end
    subgraph tier_1["Tier 1"]
        n32{"CUB_victory_for_garcia_menocal"}
        n33{"CUB_victory_for_gomez"}
    end
    subgraph tier_2["Tier 2"]
        n34["CUB_military_coup"]
        n35["CUB_oppose_the_presidency"]
        n36["CUB_seek_falangist_support"]
        n37["CUB_the_nine_cent_law"]
    end
    subgraph tier_3["Tier 3"]
        n38["CUB_ctc_recruitment"]
        n39["CUB_exert_influence_over_the_military"]
        n40["CUB_galvanize_the_ctc"]
        n41["CUB_issue_amnesties"]
        n42["CUB_military_pensions"]
        n43["CUB_minimum_wage_laws"]
        n44["CUB_repeal_liberal_policies"]
        n45["CUB_secure_united_states_political_support"]
        n46["CUB_taxation_reforms"]
    end
    subgraph tier_4["Tier 4"]
        n47["CUB_gather_political_support"]
        n48["CUB_government_reshuffle"]
        n49["CUB_invite_american_corporations"]
        n50["CUB_law_of_sugar_coordination"]
        n51["CUB_reach_out_to_trujillo"]
        n52["CUB_retirement_pensions"]
        n53["CUB_seek_soviet_support"]
        n54["CUB_unionize_the_sugar_mills"]
    end
    subgraph tier_5["Tier 5"]
        n55["CUB_american_sugar_investments"]
        n56["CUB_conduct_joint_military_excercises"]
        n57["CUB_confederation_of_cuban_workers"]
        n58["CUB_deal_with_the_mafia"]
        n59["CUB_encourage_anti_communist_violence"]
        n60["CUB_external_interests"]
        n61["CUB_implement_a_new_constitution"]
        n62["CUB_overthrow_the_menocal_government"]
        n63["CUB_reduce_american_influence"]
        n64["CUB_unite_hispaniola"]
    end
    subgraph tier_6["Tier 6"]
        n65["CUB_adapt_the_five_year_plan"]
        n66["CUB_caribbean_unity"]
        n67["CUB_create_a_central_committee"]
        n68["CUB_join_the_allies"]
        n69["CUB_rewrite_the_constitution"]
        n70["CUB_secure_power"]
    end
    subgraph tier_7["Tier 7"]
        n71["CUB_american_air_bases"]
        n72{"CUB_caribbean_dominance"}
        n73["CUB_deal_with_batista"]
        n74["CUB_establish_soviet_diplomatic_relations"]
        n75["CUB_increase_education_funding"]
        n76["CUB_intervene_ACW"]
        n77["CUB_modernize_medical_care"]
        n78["CUB_one_caribbean_policy"]
        n79["CUB_seize_foreign_sugar_mills"]
        n80["CUB_spanish_civil_war_involvement"]
        n81["CUB_stabilize_internal_politics"]
        n82["CUB_state_visit_to_the_soviet_union"]
        n83["CUB_the_cuban_politburo"]
        n84["CUB_winning_the_battle_of_the_caribbean"]
    end
    subgraph tier_8["Tier 8"]
        n85["CUB_amphibious_invasion_preparation"]
        n86["CUB_army_expansion"]
        n87["CUB_collectivize_the_sugar_plantations"]
        n88["CUB_command_the_caribbean"]
        n89["CUB_deal_with_haitian_oppressors"]
        n90["CUB_establish_rural_hospitals"]
        n91["CUB_establish_the_dgi"]
        n92["CUB_invite_NKVD_officers"]
        n93["CUB_join_with_japan"]
        n94["CUB_liberate_the_dominican_republic"]
        n95["CUB_military_improvements"]
        n96["CUB_radio_mil_diez"]
        n97["CUB_study_soviet_tactics"]
        n98["CUB_subjugate_hispaniola"]
        n99["CUB_subvert_american_influence"]
    end
    subgraph tier_9["Tier 9"]
        n100["CUB_communism_in_the_caribbean"]
        n101["CUB_demand_jamaica_and_the_bahamas"]
        n102["CUB_demand_the_eastern_isles"]
        n103["CUB_education_for_the_masses"]
        n104["CUB_expand_the_plantations"]
        n105["CUB_falangist_ideas_in_schools"]
        n106["CUB_invite_german_companies"]
        n107["CUB_invite_our_spanish_brothers"]
        n108["CUB_panhispanic_diplomacy"]
        n109["CUB_recruit_civilian_informants"]
        n110["CUB_soviet_tank_factories"]
        n111["CUB_special_amphibious_training"]
        n112["CUB_the_caribbean_guard"]
    end
    subgraph tier_10["Tier 10"]
        n113["CUB_end_american_imperialism"]
        n114["CUB_fuel_the_south_american_revolution"]
        n115["CUB_industrialize_the_islands"]
        n116["CUB_join_the_reich"]
        n117["CUB_lay_claim_to_curacao_and_trinidad"]
        n118["CUB_nationalize_foreign_sugar_mills"]
        n119["CUB_strengthen_catholic_identity"]
        n120["CUB_sugar_for_oil"]
        n121["CUB_support_communist_china"]
    end
    subgraph tier_11["Tier 11"]
        n122["CUB_island_development_plan"]
        n123["CUB_island_fortification_project"]
        n124["CUB_seize_venezuela"]
    end
    n62 --> n65
    n68 --> n71
    n49 --> n55
    n72 --> n85
    n72 --> n86
    n70 --> n72
    n60 --> n72
    n64 --> n66
    n79 --> n87
    n72 --> n88
    n89 --> n100
    n94 --> n100
    n51 --> n56
    n50 --> n57
    n62 --> n67
    n35 --> n38
    n70 --> n73
    n78 --> n89
    n49 --> n58
    n98 --> n101
    n98 --> n102
    n87 --> n103
    n47 --> n59
    n100 --> n113
    n77 --> n90
    n69 --> n74
    n83 --> n91
    n36 --> n39
    n87 --> n104
    n48 --> n60
    n99 --> n105
    n100 --> n114
    n35 --> n40
    n44 --> n47
    n39 --> n47
    n45 --> n48
    n48 --> n61
    n69 --> n75
    n104 --> n115
    n70 --> n76
    n60 --> n76
    n82 --> n92
    n45 --> n49
    n99 --> n106
    n88 --> n107
    n117 --> n122
    n117 --> n123
    n37 --> n41
    n63 --> n68
    n55 --> n68
    n106 --> n116
    n72 --> n93
    n43 --> n50
    n102 --> n117
    n101 --> n117
    n78 --> n94
    n33 --> n34
    n77 --> n95
    n34 --> n42
    n37 --> n43
    n69 --> n77
    n105 --> n118
    n67 --> n78
    n32 --> n35
    n54 --> n62
    n99 --> n108
    n83 --> n96
    n45 --> n51
    n91 --> n109
    n96 --> n109
    n52 --> n63
    n36 --> n44
    n43 --> n52
    n57 --> n69
    n63 --> n69
    n59 --> n70
    n34 --> n45
    n32 --> n36
    n40 --> n53
    n65 --> n79
    n117 --> n124
    n97 --> n110
    n92 --> n110
    n70 --> n80
    n60 --> n80
    n85 --> n111
    n70 --> n81
    n48 --> n81
    n67 --> n82
    n105 --> n119
    n82 --> n97
    n72 --> n98
    n81 --> n99
    n104 --> n120
    n100 --> n121
    n37 --> n46
    n34 --> n46
    n86 --> n112
    n67 --> n83
    n33 --> n37
    n38 --> n54
    n40 --> n54
    n51 --> n64
    n31 --> n32
    n31 --> n33
    n68 --> n84
    n88 x--x n93
    n34 x--x n37
    n35 x--x n36
    n32 x--x n33
```

# CUB_the_four_year_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n125(("CUB_the_four_year_plan"))
    end
    subgraph tier_1["Tier 1"]
        n126["CUB_central_region_strategy"]
        n127["CUB_fill_the_railways_gaps"]
        n128["CUB_marta_abreu_university"]
    end
    subgraph tier_2["Tier 2"]
        n129["CUB_agrarian_reform"]
        n130["CUB_expansion_of_new_towns"]
        n131["CUB_start_central_industrial_region"]
        n132["CUB_steel_mills"]
    end
    subgraph tier_3["Tier 3"]
        n133["CUB_arial_defence_of_cuba"]
        n134["CUB_cuban_oil"]
        n135["CUB_expand_central_industrial_region"]
        n136["CUB_expansion_of_universities"]
    end
    n127 --> n129
    n131 --> n133
    n125 --> n126
    n132 --> n134
    n131 --> n135
    n126 --> n130
    n130 --> n136
    n125 --> n127
    n125 --> n128
    n127 --> n131
    n126 --> n131
    n127 --> n132
```
