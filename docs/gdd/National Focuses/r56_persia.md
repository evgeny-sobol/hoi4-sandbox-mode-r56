# PER_adopt_western_style_military_bureaucracy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"PER_adopt_western_style_military_bureaucracy"}
    end
    subgraph tier_1["Tier 1"]
        n2{"PER_continue_sending_cadets_abroad"}
        n3{"PER_invite_foreign_officers"}
        n4["PER_maintain_air_land_links"]
        n5["PER_maintain_navy_land_links"]
        n6["PER_rifles_modernisation"]
        n7["PER_separate_the_air_force"]
        n8["PER_separate_the_navy"]
    end
    subgraph tier_2["Tier 2"]
        n9{"PER_adopt_german_doctrines"}
        n10{"PER_adopt_guerilla_tactics"}
        n11{"PER_adopt_soviet_tactics"}
        n12["PER_cas_troops_assistance"]
        n13{"PER_continue_using_western_doctrines"}
        n14["PER_dominate_the_persian_gulf"]
        n15["PER_ensure_commercial_protection"]
        n16["PER_expand_shipbuilding_capacities"]
        n17["PER_independent_bombers_bataillons"]
        n18["PER_local_fighters_development"]
        n19["PER_motorize_the_cavalry"]
        n20{"PER_rely_on_artillery_firepower"}
        n21["PER_terrain_specialization"]
    end
    subgraph tier_3["Tier 3"]
        n22["PER_air_officers_academy"]
        n23["PER_develop_logistic_bataillons"]
        n24["PER_ghale_morghi_air_bases"]
        n25["PER_hunt_the_submarines"]
        n26["PER_import_tanks_designs"]
        n27["PER_maintain_universal_drafting"]
        n28{"PER_modernise_our_artillery"}
        n29["PER_revise_universal_drafting_law"]
        n30["PER_submarines_experimentations"]
    end
    subgraph tier_4["Tier 4"]
        n31["PER_anti_aircraft_defense"]
        n32["PER_carrier_development"]
        n33["PER_counter_enemy_armor"]
        n34["PER_counter_enemy_bombers"]
    end
    n2 --> n9
    n3 --> n9
    n3 --> n10
    n2 --> n10
    n3 --> n11
    n2 --> n11
    n18 --> n22
    n24 --> n31
    n22 --> n31
    n25 --> n32
    n30 --> n32
    n4 --> n12
    n1 --> n2
    n2 --> n13
    n3 --> n13
    n28 --> n33
    n28 --> n34
    n21 --> n23
    n8 --> n14
    n5 --> n15
    n5 --> n16
    n8 --> n16
    n18 --> n24
    n15 --> n25
    n19 --> n26
    n7 --> n17
    n1 --> n3
    n7 --> n18
    n4 --> n18
    n1 --> n4
    n1 --> n5
    n11 --> n27
    n9 --> n27
    n13 --> n27
    n10 --> n27
    n20 --> n27
    n19 --> n28
    n21 --> n28
    n6 --> n19
    n2 --> n20
    n3 --> n20
    n13 --> n29
    n9 --> n29
    n11 --> n29
    n10 --> n29
    n20 --> n29
    n1 --> n6
    n1 --> n7
    n1 --> n8
    n14 --> n30
    n6 --> n21
    n9 x--x n10
    n9 x--x n11
    n9 x--x n13
    n9 x--x n20
    n10 x--x n11
    n10 x--x n13
    n10 x--x n20
    n11 x--x n13
    n11 x--x n20
    n2 x--x n3
    n13 x--x n20
    n33 x--x n34
    n4 x--x n7
    n5 x--x n8
    n27 x--x n29
```

# PER_appoint_zahedi

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35{"PER_appoint_zahedi"}
        n36["PER_continue_government_purges"]
        n37["PER_diplomatic_balance"]
        n38["PER_restore_constitutionalism"]
        n39["PER_revive_the_jungle_movement"]
    end
    subgraph tier_1["Tier 1"]
        n40["PER_embrace_persian_identity"]
        n41{"PER_encourage_german_trade"}
        n42["PER_halt_religious_persecutions"]
    end
    subgraph tier_2["Tier 2"]
        n43["PER_crush_religious_resistance"]
        n44["PER_pro_german_diplomacy"]
        n45["PER_religious_militarism"]
        n46{"PER_strategic_nationalizations"}
    end
    subgraph tier_3["Tier 3"]
        n47["PER_diplomatic_independence"]
        n48["PER_reorganization_of_the_state"]
        n49["PER_steel_deals"]
    end
    subgraph tier_4["Tier 4"]
        n50["PER_agressive_pan_iranism"]
        n51["PER_heroic_sacrifice"]
    end
    subgraph tier_5["Tier 5"]
        n52["PER_reclaim_iraq"]
        n53["PER_retake_afghanistan"]
    end
    subgraph tier_6["Tier 6"]
        n54["PER_our_central_asian_brothers"]
    end
    n44 --> n50
    n47 --> n50
    n40 --> n43
    n46 --> n47
    n35 --> n40
    n36 --> n41
    n35 --> n41
    n35 --> n42
    n47 --> n51
    n53 --> n54
    n52 --> n54
    n41 --> n44
    n50 --> n52
    n42 --> n45
    n46 --> n48
    n50 --> n53
    n44 --> n49
    n40 --> n46
    n42 --> n46
    n35 x--x n36
    n35 x--x n38
    n35 x--x n39
    n37 x--x n44
    n47 x--x n44
    n40 x--x n42
```

# PER_continue_government_purges

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35["PER_appoint_zahedi"]
        n36(("PER_continue_government_purges"))
        n47["PER_diplomatic_independence"]
        n38["PER_restore_constitutionalism"]
        n39["PER_revive_the_jungle_movement"]
    end
    subgraph tier_1["Tier 1"]
        n41{"PER_encourage_german_trade"}
        n55["PER_forced_secularization_r56"]
        n56{"PER_increase_funds_for_the_army"}
    end
    subgraph tier_2["Tier 2"]
        n37["PER_diplomatic_balance"]
        n44["PER_pro_german_diplomacy"]
        n57["PER_secular_nationalism"]
        n58["PER_trial_of_the_fifty_three"]
    end
    subgraph tier_3["Tier 3"]
        n50["PER_agressive_pan_iranism"]
        n59["PER_reaffirm_friendship_with_turkey"]
        n49["PER_steel_deals"]
    end
    subgraph tier_4["Tier 4"]
        n52["PER_reclaim_iraq"]
        n53["PER_retake_afghanistan"]
    end
    subgraph tier_5["Tier 5"]
        n54["PER_our_central_asian_brothers"]
    end
    n44 --> n50
    n47 --> n50
    n56 --> n37
    n36 --> n41
    n35 --> n41
    n36 --> n55
    n36 --> n56
    n53 --> n54
    n52 --> n54
    n41 --> n44
    n37 --> n59
    n50 --> n52
    n50 --> n53
    n55 --> n57
    n44 --> n49
    n56 --> n58
    n55 --> n58
    n35 x--x n36
    n36 x--x n38
    n36 x--x n39
    n37 x--x n44
    n47 x--x n44
```

# PER_democratic_promise

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n60(("PER_democratic_promise"))
        n61["PER_empower_the_shah"]
        n62["PER_falsify_elections"]
    end
    subgraph tier_1["Tier 1"]
        n63["PER_land_reforms_cw"]
        n64["PER_reform_the_administration_cw"]
    end
    subgraph tier_2["Tier 2"]
        n65["PER_nationalize_iranian_oil"]
        n66["PER_the_seven_year_plan"]
    end
    subgraph tier_3["Tier 3"]
        n67["PER_economy_without_oil"]
        n68["PER_undermine_the_shah"]
    end
    subgraph tier_4["Tier 4"]
        n69{"PER_alliance_with_the_ussr"}
        n70{"PER_compromise_with_britain"}
        n71{"PER_request_american_support"}
    end
    subgraph tier_5["Tier 5"]
        n72["PER_entrench_mosaddegh"]
        n73["PER_found_SAVAK"]
    end
    n68 --> n69
    n64 --> n69
    n68 --> n70
    n65 --> n67
    n66 --> n67
    n71 --> n72
    n70 --> n72
    n69 --> n72
    n71 --> n73
    n70 --> n73
    n60 --> n63
    n62 --> n63
    n64 --> n65
    n61 --> n65
    n60 --> n64
    n68 --> n71
    n61 --> n66
    n64 --> n66
    n65 --> n68
    n61 --> n68
    n60 x--x n62
    n72 x--x n73
```

# PER_falsify_elections

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n60["PER_democratic_promise"]
        n62(("PER_falsify_elections"))
        n64["PER_reform_the_administration_cw"]
    end
    subgraph tier_1["Tier 1"]
        n61["PER_empower_the_shah"]
        n63["PER_land_reforms_cw"]
    end
    subgraph tier_2["Tier 2"]
        n65["PER_nationalize_iranian_oil"]
        n66["PER_the_seven_year_plan"]
    end
    subgraph tier_3["Tier 3"]
        n67["PER_economy_without_oil"]
        n68["PER_undermine_the_shah"]
    end
    subgraph tier_4["Tier 4"]
        n69{"PER_alliance_with_the_ussr"}
        n70{"PER_compromise_with_britain"}
        n71{"PER_request_american_support"}
    end
    subgraph tier_5["Tier 5"]
        n72["PER_entrench_mosaddegh"]
        n73["PER_found_SAVAK"]
    end
    n68 --> n69
    n64 --> n69
    n68 --> n70
    n65 --> n67
    n66 --> n67
    n62 --> n61
    n71 --> n72
    n70 --> n72
    n69 --> n72
    n71 --> n73
    n70 --> n73
    n60 --> n63
    n62 --> n63
    n64 --> n65
    n61 --> n65
    n68 --> n71
    n61 --> n66
    n64 --> n66
    n65 --> n68
    n61 --> n68
    n60 x--x n62
    n72 x--x n73
```

# PER_foreign_exchange_controls

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n74(("PER_foreign_exchange_controls"))
        n75["PER_increase_machines_import"]
        n76["PER_increase_textile_production"]
    end
    subgraph tier_1["Tier 1"]
        n77["PER_finish_the_trans_iranian_railway"]
        n78["PER_sugar_exports"]
    end
    subgraph tier_2["Tier 2"]
        n79["PER_expand_tehran_university"]
        n80["PER_manufacture_planes"]
        n81["PER_secure_weapon_deals"]
    end
    subgraph tier_3["Tier 3"]
        n82["PER_electronic_development"]
        n83["PER_shift_toward_heavy_industry"]
    end
    subgraph tier_4["Tier 4"]
        n84["PER_increase_research_funds"]
        n85["PER_study_nuclear_power"]
    end
    n81 --> n82
    n79 --> n82
    n77 --> n79
    n74 --> n77
    n75 --> n77
    n82 --> n84
    n78 --> n80
    n77 --> n81
    n81 --> n83
    n76 --> n83
    n82 --> n85
    n74 --> n78
```

# PER_increase_machines_import

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n74["PER_foreign_exchange_controls"]
        n75(("PER_increase_machines_import"))
    end
    subgraph tier_1["Tier 1"]
        n77["PER_finish_the_trans_iranian_railway"]
        n76["PER_increase_textile_production"]
    end
    subgraph tier_2["Tier 2"]
        n79["PER_expand_tehran_university"]
        n81["PER_secure_weapon_deals"]
    end
    subgraph tier_3["Tier 3"]
        n82["PER_electronic_development"]
        n83["PER_shift_toward_heavy_industry"]
    end
    subgraph tier_4["Tier 4"]
        n84["PER_increase_research_funds"]
        n85["PER_study_nuclear_power"]
    end
    n81 --> n82
    n79 --> n82
    n77 --> n79
    n74 --> n77
    n75 --> n77
    n82 --> n84
    n75 --> n76
    n77 --> n81
    n81 --> n83
    n76 --> n83
    n82 --> n85
```

# PER_restore_constitutionalism

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35["PER_appoint_zahedi"]
        n36["PER_continue_government_purges"]
        n38{"PER_restore_constitutionalism"}
        n39["PER_revive_the_jungle_movement"]
    end
    subgraph tier_1["Tier 1"]
        n86["PER_prime_minister_foroughi"]
        n87["PER_rally_around_mosaddegh"]
    end
    subgraph tier_2["Tier 2"]
        n88{"PER_align_the_army"}
        n89{"PER_de_militarize_politics"}
        n90["PER_reform_the_administration"]
    end
    subgraph tier_3["Tier 3"]
        n91["PER_align_with_britain"]
        n92["PER_anti_imperialist_position"]
        n93["PER_increase_education_funds"]
        n94["PER_land_reform_act"]
        n95["PER_nationalize_aioc"]
        n96["PER_reform_the_tax_system"]
    end
    subgraph tier_4["Tier 4"]
        n97["PER_lead_the_way"]
        n98["PER_renegociate_oil_agreements"]
        n99["PER_the_sadabat_pact"]
    end
    n86 --> n88
    n88 --> n91
    n88 --> n92
    n89 --> n92
    n87 --> n89
    n88 --> n93
    n89 --> n94
    n92 --> n97
    n89 --> n95
    n38 --> n86
    n38 --> n87
    n87 --> n90
    n86 --> n90
    n88 --> n96
    n91 --> n98
    n92 --> n99
    n91 x--x n92
    n35 x--x n38
    n36 x--x n38
    n86 x--x n87
    n38 x--x n39
```

# PER_revive_the_jungle_movement

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35["PER_appoint_zahedi"]
        n36["PER_continue_government_purges"]
        n38["PER_restore_constitutionalism"]
        n39(("PER_revive_the_jungle_movement"))
    end
    subgraph tier_1["Tier 1"]
        n100["PER_acquire_soviet_support"]
        n101["PER_assemble_the_tudeh_party"]
    end
    subgraph tier_2["Tier 2"]
        n102["PER_recreate_the_persian_socialist_soviet_republic"]
    end
    subgraph tier_3["Tier 3"]
        n103{"PER_federalize_the_nation"}
        n104{"PER_nationalize_the_means_of_production"}
    end
    subgraph tier_4["Tier 4"]
        n105{"PER_islamic_socialism_focus"}
        n106["PER_land_reforms"]
        n107{"PER_promote_atheism"}
    end
    subgraph tier_5["Tier 5"]
        n108["PER_align_with_the_soviets"]
        n109["PER_persian_way_to_socialism"]
    end
    subgraph tier_6["Tier 6"]
        n110["PER_control_the_strait"]
        n111["PER_liberation_of_arabia"]
        n112["PER_soviet_economic_help"]
    end
    n39 --> n100
    n105 --> n108
    n107 --> n108
    n39 --> n101
    n109 --> n110
    n108 --> n110
    n102 --> n103
    n104 --> n105
    n103 --> n105
    n104 --> n106
    n109 --> n111
    n102 --> n104
    n105 --> n109
    n107 --> n109
    n104 --> n107
    n103 --> n107
    n100 --> n102
    n101 --> n102
    n108 --> n112
    n108 x--x n109
    n35 x--x n39
    n36 x--x n39
    n105 x--x n107
    n38 x--x n39
```
