# PHI_air_base_expansion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PHI_air_base_expansion"))
        n2["PHI_study_allied_and_axis_naval_tactics"]
    end
    subgraph tier_1["Tier 1"]
        n3{"PHI_air_innovations"}
        n4{"PHI_fighter_modernisation"}
    end
    subgraph tier_2["Tier 2"]
        n5["PHI_heavy_fighter_concept"]
        n6["PHI_light_bomber_focus"]
        n7["PHI_medium_bomber_focus"]
    end
    subgraph tier_3["Tier 3"]
        n8["PHI_air_modernisations_program"]
        n9["PHI_naval_bomber_experiments"]
    end
    subgraph tier_4["Tier 4"]
        n10["PHI_rocket_development"]
    end
    n1 --> n3
    n6 --> n8
    n7 --> n8
    n1 --> n4
    n3 --> n5
    n4 --> n5
    n4 --> n6
    n3 --> n7
    n6 --> n9
    n2 --> n9
    n8 --> n10
    n6 x--x n7
```

# PHI_post_indenpence_stabilization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n11{"PHI_post_indenpence_stabilization"}
    end
    subgraph tier_1["Tier 1"]
        n12{"PHI_a_new_regime"}
        n13["PHI_follow_the_american_way"]
    end
    subgraph tier_2["Tier 2"]
        n14["PHI_fighting_filipinos"]
        n15["PHI_huk_revolutionaries"]
        n16["PHI_open_the_agricultural_bank"]
        n17["PHI_support_the_ganap_party"]
        n18["PHI_the_wage_rationalization_act"]
    end
    subgraph tier_3["Tier 3"]
        n19["PHI_ideological_fanaticism"]
        n20["PHI_move_agriculture_southwards"]
        n21["PHI_reach_out_to_spain"]
        n22["PHI_soviet_trade_mission"]
        n23["PHI_sway_the_military"]
        n24["PHI_the_agricultural_tenancy_act"]
    end
    subgraph tier_4["Tier 4"]
        n25["PHI_enact_womens_suffrage"]
        n26["PHI_executive_order"]
        n27["PHI_hukbalap_rebellion"]
        n28["PHI_may_2nd_uprising"]
    end
    subgraph tier_5["Tier 5"]
        n29["PHI_accept_refugees"]
        n30{"PHI_adopt_a_national_language"}
        n31["PHI_aid_the_nationalist_cause"]
        n32["PHI_attract_american_investments"]
        n33["PHI_cooperate_with_ganap"]
        n34["PHI_crush_the_bourgeoisie"]
        n35["PHI_subsidize_anscor"]
        n36["PHI_supress_the_radicals"]
    end
    subgraph tier_6["Tier 6"]
        n37{"PHI_claim_the_spanish_mantle"}
        n38{"PHI_improve_workers_rights"}
        n39{"PHI_industrialize_the_south"}
        n40["PHI_invite_foreign_scientists"]
        n41{"PHI_maintain_the_status_quo"}
        n42["PHI_militarize_the_society"]
        n43{"PHI_move_towards_independence"}
        n44["PHI_privatize_the_industry"]
    end
    subgraph tier_7["Tier 7"]
        n45{"PHI_align_with_the_japanese"}
        n46["PHI_carving_our_own_destiny"]
        n47["PHI_join_the_allies"]
        n48{"PHI_join_the_axis"}
        n49["PHI_join_the_comintern"]
        n50["PHI_the_guam_referendum"]
        n51["PHI_the_pan_malayan_confederation"]
    end
    subgraph tier_8["Tier 8"]
        n52["PHI_befriend_the_carlists"]
        n53["PHI_bring_democracy_to_japan"]
        n54["PHI_form_the_popular_front"]
        n55["PHI_greater_philippines_concept"]
        n56["PHI_pan_asian_cooperation"]
        n57["PHI_purge_the_trotskyists"]
        n58["PHI_spread_the_revolution"]
    end
    subgraph tier_9["Tier 9"]
        n59["PHI_across_the_sea"]
        n60{"PHI_invite_francisco"}
        n61["PHI_liberate_the_indonesians"]
        n62["PHI_oust_the_asian_colonizers"]
        n63["PHI_rule_the_pacific"]
        n64["PHI_secure_the_east_indies"]
        n65["PHI_steal_the_pearl_of_the_east"]
    end
    subgraph tier_10["Tier 10"]
        n66["PHI_alliance_with_the_spanish"]
        n67["PHI_return_to_the_homeland"]
        n68["PHI_towards_a_free_southeast_asia"]
    end
    subgraph tier_11["Tier 11"]
        n69["PHI_strike_the_portugese_colonies"]
    end
    n11 --> n12
    n25 --> n29
    n55 --> n59
    n25 --> n30
    n26 --> n30
    n28 --> n31
    n27 --> n31
    n37 --> n45
    n60 --> n66
    n26 --> n32
    n45 --> n52
    n48 --> n52
    n47 --> n53
    n51 --> n53
    n39 --> n46
    n38 --> n46
    n35 --> n37
    n28 --> n33
    n27 --> n34
    n24 --> n25
    n24 --> n26
    n12 --> n14
    n13 --> n14
    n11 --> n13
    n46 --> n54
    n48 --> n55
    n12 --> n15
    n23 --> n27
    n19 --> n27
    n22 --> n27
    n17 --> n19
    n15 --> n19
    n34 --> n38
    n34 --> n39
    n35 --> n40
    n34 --> n40
    n52 --> n60
    n41 --> n47
    n43 --> n47
    n37 --> n48
    n39 --> n49
    n58 --> n61
    n30 --> n41
    n23 --> n28
    n19 --> n28
    n21 --> n28
    n35 --> n42
    n16 --> n20
    n30 --> n43
    n13 --> n16
    n45 --> n62
    n58 --> n62
    n51 --> n56
    n35 --> n44
    n49 --> n57
    n17 --> n21
    n60 --> n67
    n52 --> n63
    n55 --> n63
    n55 --> n64
    n15 --> n22
    n46 --> n58
    n49 --> n58
    n58 --> n65
    n67 --> n69
    n66 --> n69
    n28 --> n35
    n12 --> n17
    n27 --> n36
    n17 --> n23
    n15 --> n23
    n16 --> n24
    n18 --> n24
    n41 --> n50
    n43 --> n51
    n13 --> n18
    n61 --> n68
    n65 --> n68
    n12 x--x n13
    n45 x--x n48
    n66 x--x n67
    n52 x--x n55
    n46 x--x n49
    n15 x--x n17
    n47 x--x n51
    n41 x--x n43
```

# PHI_shipyard_expansion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n6["PHI_light_bomber_focus"]
        n70(("PHI_shipyard_expansion"))
    end
    subgraph tier_1["Tier 1"]
        n71{"PHI_import_submarine_techology"}
        n72{"PHI_license_foreign_ships"}
    end
    subgraph tier_2["Tier 2"]
        n73["PHI_anti_sub_defense_force"]
        n74["PHI_commerce_attack"]
    end
    subgraph tier_3["Tier 3"]
        n2{"PHI_study_allied_and_axis_naval_tactics"}
    end
    subgraph tier_4["Tier 4"]
        n75["PHI_island_defense"]
        n9["PHI_naval_bomber_experiments"]
        n76["PHI_strike_force"]
    end
    subgraph tier_5["Tier 5"]
        n77["PHI_pacific_navy"]
    end
    n72 --> n73
    n71 --> n74
    n70 --> n71
    n2 --> n75
    n70 --> n72
    n6 --> n9
    n2 --> n9
    n76 --> n77
    n75 --> n77
    n2 --> n76
    n74 --> n2
    n73 --> n2
    n73 x--x n74
    n75 x--x n76
```

# PHI_teachings_of_the_usaffe

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n78(("PHI_teachings_of_the_usaffe"))
    end
    subgraph tier_1["Tier 1"]
        n79["PHI_american_imports"]
        n80["PHI_defense_of_manila"]
    end
    subgraph tier_2["Tier 2"]
        n81["PHI_develop_anti_air_capabilities"]
        n82{"PHI_island_hopping_strategy"}
        n83{"PHI_lighting_warfare"}
    end
    subgraph tier_3["Tier 3"]
        n84["PHI_american_doctrines"]
        n85["PHI_japanese_doctrines"]
        n86["PHI_study_european_tanks"]
    end
    subgraph tier_4["Tier 4"]
        n87["PHI_amphibious_operations"]
        n88["PHI_anti_tank_guns"]
        n89["PHI_create_main_battle_tanks"]
        n90["PHI_import_new_howitzers"]
    end
    subgraph tier_5["Tier 5"]
        n91["PHI_army_modernisation"]
    end
    n82 --> n84
    n78 --> n79
    n85 --> n87
    n84 --> n87
    n85 --> n88
    n86 --> n88
    n90 --> n91
    n88 --> n91
    n86 --> n89
    n78 --> n80
    n80 --> n81
    n84 --> n90
    n80 --> n82
    n79 --> n82
    n82 --> n85
    n79 --> n83
    n83 --> n86
    n84 x--x n85
    n84 x--x n86
    n85 x--x n86
```

# PHI_the_industrialized_islands_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n92(("PHI_the_industrialized_islands_plan"))
    end
    subgraph tier_1["Tier 1"]
        n93["PHI_urbanize_the_islands"]
    end
    subgraph tier_2["Tier 2"]
        n94["PHI_fund_armscor"]
        n95["PHI_manila_central_railway"]
    end
    subgraph tier_3["Tier 3"]
        n96{"PHI_expanded_chromium_mining"}
        n97["PHI_national_defence_fund"]
        n98["PHI_seize_illegal_weapons_manufacturer"]
    end
    subgraph tier_4["Tier 4"]
        n99["PHI_additional_research_slot1"]
        n100["PHI_develop_mindano"]
        n101["PHI_develop_palawan"]
    end
    subgraph tier_5["Tier 5"]
        n102["PHI_american_computer_imports"]
        n103["PHI_synth_oil"]
    end
    subgraph tier_6["Tier 6"]
        n104["PHI_additional_research_slot2"]
        n105["PHI_research_new_enegry_options"]
    end
    n97 --> n99
    n98 --> n99
    n102 --> n104
    n99 --> n102
    n96 --> n100
    n96 --> n101
    n95 --> n96
    n93 --> n94
    n93 --> n95
    n95 --> n97
    n94 --> n97
    n102 --> n105
    n94 --> n98
    n99 --> n103
    n92 --> n93
    n100 x--x n101
```
