# YUG_army_modernization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("YUG_army_modernization"))
    end
    subgraph tier_1["Tier 1"]
        n2{"YUG_army_maneuvers"}
        n3["YUG_motorize_the_cavalry"]
        n4["YUG_mountain_brigades"]
        n5["YUG_small_arms"]
    end
    subgraph tier_2["Tier 2"]
        n6{"YUG_armored_cavalry"}
        n7["YUG_domestic_artillery_production"]
        n8["YUG_independent_engineer_regiments"]
        n9["YUG_motorized_logistics"]
        n10["YUG_supremacy_of_defense"]
        n11["YUG_supremacy_of_offense"]
    end
    subgraph tier_3["Tier 3"]
        n12["YUG_anti_tank_defenses"]
        n13["YUG_artillery_regiments"]
        n14["YUG_form_parachute_battalions"]
        n15["YUG_modern_tanks"]
        n16["YUG_motorized_recon_companies"]
        n17["YUG_tank_conversions"]
    end
    subgraph tier_4["Tier 4"]
        n18["YUG_medal_for_extreme_bravery"]
        n19["YUG_tank_licenses"]
    end
    n7 --> n12
    n3 --> n6
    n1 --> n2
    n11 --> n13
    n10 --> n13
    n5 --> n7
    n8 --> n14
    n4 --> n8
    n13 --> n18
    n6 --> n15
    n1 --> n3
    n3 --> n9
    n3 --> n16
    n8 --> n16
    n1 --> n4
    n1 --> n5
    n2 --> n10
    n2 --> n11
    n6 --> n17
    n15 --> n19
    n15 x--x n17
    n10 x--x n11
```

# YUG_expand_the_serbian_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20["YUG_contest_the_adriatic"]
        n21(("YUG_expand_the_serbian_shipyards"))
        n22["YUG_expand_the_split_shipyards"]
        n23{"YUG_heavy_cruiser_project"}
    end
    subgraph tier_1["Tier 1"]
        n24["YUG_coastal_defense"]
    end
    subgraph tier_2["Tier 2"]
        n25{"YUG_expand_the_submarine_fleet"}
        n26["YUG_naval_bombers"]
    end
    subgraph tier_3["Tier 3"]
        n27{"YUG_modern_destroyers"}
    end
    subgraph tier_4["Tier 4"]
        n28["YUG_adriatic_specialization"]
        n29["YUG_skilled_pilots"]
    end
    n27 --> n28
    n25 --> n28
    n21 --> n24
    n24 --> n25
    n26 --> n27
    n20 --> n26
    n24 --> n26
    n23 --> n29
    n27 --> n29
    n28 x--x n29
    n21 x--x n22
```

# YUG_expand_the_split_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n24["YUG_coastal_defense"]
        n21["YUG_expand_the_serbian_shipyards"]
        n22(("YUG_expand_the_split_shipyards"))
        n25{"YUG_expand_the_submarine_fleet"}
    end
    subgraph tier_1["Tier 1"]
        n20["YUG_contest_the_adriatic"]
    end
    subgraph tier_2["Tier 2"]
        n26["YUG_naval_bombers"]
        n30["YUG_replace_the_dalmacija"]
    end
    subgraph tier_3["Tier 3"]
        n23{"YUG_heavy_cruiser_project"}
        n27{"YUG_modern_destroyers"}
    end
    subgraph tier_4["Tier 4"]
        n28["YUG_adriatic_specialization"]
        n29["YUG_skilled_pilots"]
    end
    n27 --> n28
    n25 --> n28
    n22 --> n20
    n30 --> n23
    n26 --> n27
    n20 --> n26
    n24 --> n26
    n20 --> n30
    n23 --> n29
    n27 --> n29
    n28 x--x n29
    n21 x--x n22
```

# YUG_industrialization_program

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n31(("YUG_industrialization_program"))
    end
    subgraph tier_1["Tier 1"]
        n32{"YUG_expand_the_mining_industry"}
    end
    subgraph tier_2["Tier 2"]
        n33["YUG_develop_civilian_industry"]
        n34["YUG_develop_military_industry"]
        n35["YUG_rare_minerals_exploitation"]
    end
    subgraph tier_3["Tier 3"]
        n36{"YUG_expand_the_university_of_zagreb"}
        n37["YUG_exploit_the_pannonian_deposits"]
    end
    subgraph tier_4["Tier 4"]
        n38["YUG_improve_serbian_rail_network"]
        n39["YUG_integrated_rail_network"]
    end
    subgraph tier_5["Tier 5"]
        n40["YUG_develop_slovenian_industry"]
        n41["YUG_expand_the_university_of_belgrad"]
        n42["YUG_improve_light_industry"]
        n43["YUG_serbian_steel"]
    end
    subgraph tier_6["Tier 6"]
        n44["YUG_central_management"]
        n45["YUG_expand_the_university_of_ljubljana"]
        n46["YUG_local_self_management"]
    end
    subgraph tier_7["Tier 7"]
        n47["YUG_expand_the_sarajevo_arsenals"]
        n48["YUG_yugoslav_nuclear_program"]
    end
    subgraph tier_8["Tier 8"]
        n49["YUG_uranium_prospecting_in_buhovo"]
    end
    n41 --> n44
    n32 --> n33
    n32 --> n34
    n39 --> n40
    n31 --> n32
    n46 --> n47
    n44 --> n47
    n38 --> n41
    n40 --> n45
    n33 --> n36
    n34 --> n36
    n35 --> n37
    n39 --> n42
    n38 --> n42
    n36 --> n38
    n36 --> n39
    n40 --> n46
    n32 --> n35
    n38 --> n43
    n48 --> n49
    n44 --> n48
    n46 --> n48
    n33 x--x n34
    n38 x--x n39
```

# YUG_modernize_the_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n50{"YUG_modernize_the_air_force"}
    end
    subgraph tier_1["Tier 1"]
        n51["YUG_local_developers"]
        n52["YUG_purchase_foreign"]
    end
    subgraph tier_2["Tier 2"]
        n53["YUG_ikarus"]
        n54{"YUG_license_production"}
        n55["YUG_rogozarski"]
        n56["YUG_zmaj"]
    end
    subgraph tier_3["Tier 3"]
        n57["YUG_bomber_license"]
        n58["YUG_fighter_license"]
        n59["YUG_form_mechanics"]
        n60["YUG_kraljevo_state_airlines_factory"]
        n61["YUG_the_ik_3"]
    end
    subgraph tier_4["Tier 4"]
        n62["YUG_bomber_project"]
        n63["YUG_expanded_repair_facilities"]
        n64["YUG_heavy_fighter_project"]
    end
    n54 --> n57
    n61 --> n62
    n60 --> n63
    n59 --> n63
    n54 --> n58
    n54 --> n59
    n53 --> n59
    n55 --> n59
    n56 --> n59
    n61 --> n64
    n51 --> n53
    n54 --> n60
    n52 --> n54
    n50 --> n51
    n50 --> n52
    n51 --> n55
    n53 --> n61
    n55 --> n61
    n56 --> n61
    n51 --> n56
    n57 x--x n58
    n51 x--x n52
```

# YUG_recognize_the_soviet_union

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n65["YUG_friendship_treaty_with_italy"]
        n66(("YUG_recognize_the_soviet_union"))
        n67["YUG_reinforce_old_alliances"]
        n68["YUG_western_focus"]
    end
    subgraph tier_1["Tier 1"]
        n69["YUG_form_peasant_councils"]
    end
    subgraph tier_2["Tier 2"]
        n70{"YUG_abolish_the_monarchy"}
        n71["YUG_brigadistas"]
        n72["YUG_local_militias"]
    end
    subgraph tier_3["Tier 3"]
        n73["YUG_organized_partizans"]
        n74["YUG_soviet_cooperation"]
        n75["YUG_yugoslavian_international_communism"]
        n76["YUG_yugoslavian_path_to_communism"]
    end
    subgraph tier_4["Tier 4"]
        n77["YUG_form_the_federal_republic"]
        n78["YUG_join_comintern"]
        n79["YUG_pan_slavic_workers_congress"]
    end
    subgraph tier_5["Tier 5"]
        n80["YUG_economic_centralization"]
        n81["YUG_federal_defense_council"]
        n82["YUG_invite_albania"]
        n83["YUG_invite_bulgaria"]
        n84["YUG_neutralize_the_opposition"]
        n85["YUG_research_collaboration"]
    end
    subgraph tier_6["Tier 6"]
        n86["YUG_pan_balkan_workers_congress"]
    end
    subgraph tier_7["Tier 7"]
        n87["YUG_form_the_balkan_federation"]
        n88["YUG_invite_greece"]
        n89["YUG_invite_hungary"]
        n90["YUG_invite_romania"]
    end
    subgraph tier_8["Tier 8"]
        n91["YUG_invite_turkey"]
    end
    n69 --> n70
    n65 --> n71
    n67 --> n71
    n69 --> n71
    n77 --> n80
    n77 --> n81
    n66 --> n69
    n86 --> n87
    n76 --> n77
    n74 --> n77
    n75 --> n77
    n79 --> n82
    n79 --> n83
    n86 --> n88
    n86 --> n89
    n86 --> n90
    n88 --> n91
    n89 --> n91
    n90 --> n91
    n74 --> n78
    n67 --> n72
    n65 --> n72
    n69 --> n72
    n77 --> n84
    n72 --> n73
    n83 --> n86
    n82 --> n86
    n81 --> n86
    n84 --> n86
    n76 --> n79
    n78 --> n85
    n70 --> n74
    n70 --> n75
    n70 --> n76
    n66 x--x n68
    n74 x--x n75
    n74 x--x n76
    n75 x--x n76
```

# YUG_western_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n69["YUG_form_peasant_councils"]
        n66["YUG_recognize_the_soviet_union"]
        n68{"YUG_western_focus"}
    end
    subgraph tier_1["Tier 1"]
        n65["YUG_friendship_treaty_with_italy"]
        n67["YUG_reinforce_old_alliances"]
    end
    subgraph tier_2["Tier 2"]
        n92{"YUG_attract_allied_capital"}
        n93{"YUG_attract_axis_capital"}
        n71["YUG_brigadistas"]
        n72["YUG_local_militias"]
    end
    subgraph tier_3["Tier 3"]
        n94{"YUG_evolution"}
        n95{"YUG_limited_self_government"}
        n73["YUG_organized_partizans"]
    end
    subgraph tier_4["Tier 4"]
        n96{"YUG_crush_the_ustasa"}
        n97{"YUG_devolved_croatia"}
        n98["YUG_dissolve_serbia"]
        n99{"YUG_establish_the_banovina_of_croatia"}
        n100{"YUG_united_autonomous_croatia"}
    end
    subgraph tier_5["Tier 5"]
        n101{"YUG_ban_slovene_nationalist_parties"}
        n102["YUG_divide_bosnia"]
        n103["YUG_safeguard_bosnia"]
        n104{"YUG_slovenia_for_support"}
    end
    subgraph tier_6["Tier 6"]
        n105{"YUG_concessions_for_macedonians"}
        n106{"YUG_fate_of_banat"}
        n107{"YUG_surrender_macedonia"}
    end
    subgraph tier_7["Tier 7"]
        n108{"YUG_end_the_regency"}
        n109["YUG_invite_german_military_mission"]
        n110{"YUG_join_axis"}
        n111["YUG_towards_independence"]
        n112["YUG_united_kingdom"]
    end
    subgraph tier_8["Tier 8"]
        n113{"YUG_coronation"}
        n114["YUG_defence_army_of_yugoslavia"]
        n115["YUG_guarantee_religious_liberties"]
        n116["YUG_irredentism_towards_italy"]
        n117{"YUG_royal_wedding"}
        n118["YUG_surrender_italian_claims"]
        n119["YUG_zara_for_axis"]
    end
    subgraph tier_9["Tier 9"]
        n120["YUG_attack_italy"]
        n121["YUG_defence_league"]
        n122["YUG_enforced_neutrality"]
        n123["YUG_invite_italian_naval_experts"]
        n124["YUG_join_allies"]
        n125["YUG_reunite_the_kingdom"]
    end
    subgraph tier_10["Tier 10"]
        n126["YUG_allied_air_combat_school"]
        n127["YUG_claim_bulgaria"]
        n128["YUG_fortress_yugoslavia"]
        n129["YUG_subjugate_albania"]
    end
    subgraph tier_11["Tier 11"]
        n130["YUG_press_bulgarian_claims_on_thrace"]
        n131["YUG_proclaim_greater_yugoslavia"]
    end
    subgraph tier_12["Tier 12"]
        n132["YUG_all_yugoslavian_regiments"]
        n133["YUG_organize_our_alliance"]
    end
    n131 --> n132
    n121 --> n132
    n124 --> n126
    n116 --> n120
    n65 --> n92
    n67 --> n92
    n65 --> n93
    n67 --> n93
    n96 --> n101
    n99 --> n101
    n65 --> n71
    n67 --> n71
    n69 --> n71
    n119 --> n127
    n118 --> n127
    n120 --> n127
    n104 --> n105
    n101 --> n105
    n108 --> n113
    n110 --> n113
    n94 --> n96
    n111 --> n114
    n114 --> n121
    n95 --> n97
    n95 --> n98
    n100 --> n102
    n97 --> n102
    n105 --> n108
    n107 --> n108
    n106 --> n108
    n117 --> n122
    n113 --> n122
    n94 --> n99
    n93 --> n94
    n98 --> n106
    n103 --> n106
    n102 --> n106
    n122 --> n128
    n68 --> n65
    n112 --> n115
    n105 --> n109
    n107 --> n109
    n106 --> n109
    n119 --> n123
    n118 --> n123
    n110 --> n116
    n108 --> n116
    n117 --> n124
    n113 --> n124
    n105 --> n110
    n107 --> n110
    n106 --> n110
    n92 --> n95
    n67 --> n72
    n65 --> n72
    n69 --> n72
    n131 --> n133
    n72 --> n73
    n127 --> n130
    n127 --> n131
    n129 --> n131
    n68 --> n67
    n115 --> n125
    n108 --> n117
    n100 --> n103
    n97 --> n103
    n96 --> n104
    n99 --> n104
    n119 --> n129
    n118 --> n129
    n120 --> n129
    n110 --> n118
    n104 --> n107
    n101 --> n107
    n106 --> n111
    n95 --> n100
    n106 --> n112
    n110 --> n119
    n101 x--x n104
    n105 x--x n107
    n96 x--x n99
    n97 x--x n100
    n102 x--x n103
    n108 x--x n110
    n122 x--x n124
    n94 x--x n95
    n65 x--x n67
    n116 x--x n118
    n116 x--x n119
    n66 x--x n68
    n118 x--x n119
    n111 x--x n112
```
