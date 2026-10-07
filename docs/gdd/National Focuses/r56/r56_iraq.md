# IRQ_air_base_expansion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("IRQ_air_base_expansion"))
    end
    subgraph tier_1["Tier 1"]
        n2{"IRQ_air_innovations"}
        n3{"IRQ_fighter_modernisation"}
    end
    subgraph tier_2["Tier 2"]
        n4{"IRQ_heavy_fighter_concept"}
        n5["IRQ_naval_bomber_experiments"]
    end
    subgraph tier_3["Tier 3"]
        n6["IRQ_light_bomber_focus"]
        n7["IRQ_medium_bomber_focus"]
    end
    subgraph tier_4["Tier 4"]
        n8["IRQ_air_modernisations_programme"]
    end
    subgraph tier_5["Tier 5"]
        n9["IRQ_rocket_development"]
    end
    n1 --> n2
    n6 --> n8
    n7 --> n8
    n1 --> n3
    n2 --> n4
    n3 --> n4
    n4 --> n6
    n3 --> n6
    n4 --> n7
    n2 --> n7
    n2 --> n5
    n8 --> n9
    n6 x--x n7
```

# IRQ_arab_industrial_revolution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10(("IRQ_arab_industrial_revolution"))
    end
    subgraph tier_1["Tier 1"]
        n11["IRQ_ghazis_propaganda_station"]
        n12["IRQ_modernisation_of_rural_villages"]
        n13["IRQ_the_basis_of_the_economy"]
    end
    subgraph tier_2["Tier 2"]
        n14["IRQ_expanded_oil_drilling"]
        n15["IRQ_iraqi_republic_railways"]
        n16["IRQ_royal_armament_factories"]
        n17["IRQ_total_eletrification"]
    end
    subgraph tier_3["Tier 3"]
        n18["IRQ_finish_the_railyways"]
        n19["IRQ_labor_camps"]
        n20["IRQ_mosul_military_stockpile"]
        n21["IRQ_rapid_industrialization"]
    end
    subgraph tier_4["Tier 4"]
        n22["IRQ_rebuild_baghdad"]
        n23["IRQ_steel_mining"]
    end
    subgraph tier_5["Tier 5"]
        n24["IRQ_establish_the_univeristy_of_baghdad"]
    end
    subgraph tier_6["Tier 6"]
        n25["IRQ_create_the_iraqi_block_cipher"]
        n26["IRQ_design_the_osirak_reactor"]
        n27["IRQ_license_cipher_machines"]
    end
    subgraph tier_7["Tier 7"]
        n28["IRQ_expand_the_univeristy"]
    end
    n24 --> n25
    n24 --> n26
    n22 --> n24
    n23 --> n24
    n26 --> n28
    n11 --> n14
    n15 --> n18
    n10 --> n11
    n12 --> n15
    n16 --> n19
    n24 --> n27
    n10 --> n12
    n14 --> n20
    n17 --> n21
    n18 --> n22
    n21 --> n22
    n11 --> n16
    n19 --> n23
    n20 --> n23
    n10 --> n13
    n12 --> n17
```

# IRQ_persian_gulf_supremacy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29(("IRQ_persian_gulf_supremacy"))
    end
    subgraph tier_1["Tier 1"]
        n30["IRQ_import_submarine_technology"]
        n31["IRQ_study_foreign_built_ships"]
    end
    subgraph tier_2["Tier 2"]
        n32["IRQ_a_cruiser_navy"]
        n33["IRQ_commerce_attack"]
        n34{"IRQ_the_twin_threats"}
    end
    subgraph tier_3["Tier 3"]
        n35["IRQ_coastal_defense"]
        n36["IRQ_strike_force"]
    end
    subgraph tier_4["Tier 4"]
        n37["IRQ_persian_gulf_navy"]
    end
    subgraph tier_5["Tier 5"]
        n38["IRQ_naval_equipment"]
    end
    n31 --> n32
    n34 --> n35
    n30 --> n33
    n29 --> n30
    n37 --> n38
    n36 --> n37
    n35 --> n37
    n34 --> n36
    n29 --> n31
    n30 --> n34
    n31 --> n34
    n35 x--x n36
```

# IRQ_reform_the_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n39(("IRQ_reform_the_army"))
    end
    subgraph tier_1["Tier 1"]
        n40["IRQ_motorized_army"]
        n41["IRQ_remove_dependency_on_british_equipment"]
        n42["IRQ_study_foreign_tanks"]
    end
    subgraph tier_2["Tier 2"]
        n43["IRQ_improve_army_logistics"]
        n44["IRQ_study_new_land_doctrines"]
    end
    subgraph tier_3["Tier 3"]
        n45["IRQ_cruisers_experiments"]
        n46["IRQ_desert_specialization"]
        n47["IRQ_elte_tank_forces"]
        n48["IRQ_special_forces_r56"]
    end
    subgraph tier_4["Tier 4"]
        n49["IRQ_army_modernisation"]
        n50["IRQ_camel_corps"]
    end
    n47 --> n49
    n48 --> n49
    n46 --> n50
    n43 --> n45
    n44 --> n46
    n43 --> n47
    n42 --> n43
    n40 --> n43
    n39 --> n40
    n39 --> n41
    n44 --> n48
    n39 --> n42
    n40 --> n44
    n41 --> n44
```

# IRQ_reinforce_the_monarchy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n51(("IRQ_reinforce_the_monarchy"))
        n52["IRQ_unsupported_monarch"]
    end
    subgraph tier_1["Tier 1"]
        n53["IRQ_british_embassy2"]
        n54["IRQ_friendship_with_iran"]
        n55["IRQ_friendship_with_turkey"]
        n56["IRQ_invite_western_investors"]
        n57["IRQ_opportunistic_oil_nationalization"]
        n58["IRQ_promote_peaceful_religious_coexistence"]
        n59["IRQ_the_hashemite_diplomacy"]
    end
    subgraph tier_2["Tier 2"]
        n60["IRQ_build_our_own_diplomacy_instead"]
        n61["IRQ_favor_shiite_officers"]
        n62["IRQ_seek_foreign_industrial_support"]
        n63["IRQ_the_sadabat_pact"]
    end
    subgraph tier_3["Tier 3"]
        n64["IRQ_on_the_british_side"]
        n65["IRQ_tip_the_oil_balance"]
        n66["IRQ_united_officer_corps"]
    end
    subgraph tier_4["Tier 4"]
        n67["IRQ_reaffirm_supremacy_over_the_army"]
    end
    n51 --> n53
    n54 --> n60
    n55 --> n60
    n58 --> n61
    n51 --> n54
    n51 --> n55
    n51 --> n56
    n53 --> n64
    n62 --> n64
    n51 --> n57
    n51 --> n58
    n66 --> n67
    n56 --> n62
    n51 --> n59
    n54 --> n63
    n55 --> n63
    n53 --> n65
    n62 --> n65
    n61 --> n66
    n51 x--x n52
```

# IRQ_unsupported_monarch

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n51["IRQ_reinforce_the_monarchy"]
        n52{"IRQ_unsupported_monarch"}
    end
    subgraph tier_1["Tier 1"]
        n68["IRQ_a_new_kind_of_monarch"]
        n69{"IRQ_the_end_of_the_monarchy"}
    end
    subgraph tier_2["Tier 2"]
        n70["IRQ_officers_coup"]
        n71["IRQ_the_secular_movement"]
        n72["IRQ_workers_revolution"]
    end
    subgraph tier_3["Tier 3"]
        n73["IRQ_appease_the_army"]
        n74["IRQ_british_embassy"]
        n75["IRQ_communist_oil_nationalization"]
        n76["IRQ_cult_of_personaility"]
        n77["IRQ_foriegn_fighters"]
        n78["IRQ_militarized_settlements"]
        n79["IRQ_political_purification"]
        n80["IRQ_socialist_scientists"]
    end
    subgraph tier_4["Tier 4"]
        n81["IRQ_algaylani_youth"]
        n82["IRQ_assyrian_revanchism"]
        n83["IRQ_fascist_oil_nationalization"]
        n84["IRQ_german_military_mission"]
        n85["IRQ_sell_oil_to_the_allies"]
        n86["IRQ_soviet_funding"]
        n87["IRQ_volunteer_corps"]
        n88["IRQ_welfare_state"]
        n89["IRQ_workers_culture"]
    end
    subgraph tier_5["Tier 5"]
        n90["IRQ_allied_support"]
        n91["IRQ_anti_colonialism_policy"]
        n92["IRQ_establish_the_republican_guard"]
        n93["IRQ_heavy_industry_plan"]
        n94["IRQ_join_the_allies"]
        n95{"IRQ_ministry_of_propaganda"}
        n96{"IRQ_secret_police"}
    end
    subgraph tier_6["Tier 6"]
        n97["IRQ_a_true_republic"]
        n98["IRQ_demand_persian_gulf_colonies"]
        n99["IRQ_form_the_socialist_union_of_the_mashriq"]
        n100["IRQ_join_the_comitern"]
        n101["IRQ_proclaim_the_neo_assyrian_empire"]
    end
    subgraph tier_7["Tier 7"]
        n102["IRQ_conquer_saudi"]
        n103["IRQ_demand_british_territories"]
        n104["IRQ_demand_french_colonies"]
        n105{"IRQ_invite_arabia"}
        n106{"IRQ_invite_oman"}
        n107{"IRQ_invite_yemen"}
        n108["IRQ_kurdistan_crisis"]
        n109["IRQ_operation_sublime_porte"]
        n110["IRQ_the_parition_of_persia"]
    end
    subgraph tier_8["Tier 8"]
        n111{"IRQ_Mawtini"}
        n112["IRQ_ally_the_iranian_communists"]
        n113["IRQ_ally_the_turkish_communists"]
        n114["IRQ_assisted_development"]
        n115["IRQ_demand_cyprus"]
        n116["IRQ_demand_old_turkish_lands"]
        n117["IRQ_royal_road"]
        n118["IRQ_the_red_dawn"]
    end
    subgraph tier_9["Tier 9"]
        n119["IRQ_assyria_restored"]
        n120["IRQ_conquer_persia"]
        n121["IRQ_conquer_turkey"]
    end
    n106 --> n111
    n105 --> n111
    n107 --> n111
    n52 --> n68
    n90 --> n97
    n94 --> n97
    n79 --> n81
    n87 --> n90
    n106 --> n112
    n105 --> n112
    n107 --> n112
    n106 --> n113
    n105 --> n113
    n107 --> n113
    n82 --> n91
    n69 --> n91
    n72 --> n73
    n71 --> n73
    n106 --> n114
    n107 --> n114
    n105 --> n114
    n116 --> n119
    n103 --> n119
    n117 --> n119
    n76 --> n82
    n71 --> n74
    n72 --> n75
    n111 --> n120
    n101 --> n102
    n111 --> n121
    n70 --> n76
    n101 --> n103
    n104 --> n115
    n98 --> n104
    n108 --> n116
    n91 --> n98
    n81 --> n92
    n79 --> n83
    n71 --> n77
    n96 --> n99
    n95 --> n99
    n79 --> n84
    n89 --> n93
    n88 --> n93
    n99 --> n105
    n99 --> n106
    n99 --> n107
    n85 --> n94
    n96 --> n100
    n95 --> n100
    n101 --> n108
    n72 --> n78
    n89 --> n95
    n68 --> n70
    n100 --> n109
    n70 --> n79
    n92 --> n101
    n84 --> n101
    n103 --> n117
    n102 --> n117
    n86 --> n96
    n74 --> n85
    n72 --> n80
    n78 --> n86
    n52 --> n69
    n100 --> n110
    n109 --> n118
    n110 --> n118
    n69 --> n71
    n77 --> n87
    n77 --> n88
    n80 --> n88
    n73 --> n88
    n80 --> n89
    n69 --> n72
    n68 x--x n69
    n112 x--x n120
    n113 x--x n121
    n99 x--x n100
    n51 x--x n52
    n71 x--x n72
```
