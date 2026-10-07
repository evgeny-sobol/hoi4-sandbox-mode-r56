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
        n14["YUG_modern_tanks"]
        n15["YUG_motorized_recon_companies"]
        n16["YUG_tank_conversions"]
    end
    subgraph tier_4["Tier 4"]
        n17["YUG_form_parachute_battalions"]
        n18["YUG_medal_for_extreme_bravery"]
        n19["YUG_tank_licenses"]
    end
    n7 --> n12
    n3 --> n6
    n1 --> n2
    n11 --> n13
    n10 --> n13
    n5 --> n7
    n15 --> n17
    n4 --> n8
    n13 --> n18
    n6 --> n14
    n1 --> n3
    n3 --> n9
    n8 --> n15
    n1 --> n4
    n1 --> n5
    n2 --> n10
    n2 --> n11
    n6 --> n16
    n14 --> n19
    n14 x--x n16
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
    n33 x--x n34
    n38 x--x n39
```

# YUG_modernize_the_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n48{"YUG_modernize_the_air_force"}
    end
    subgraph tier_1["Tier 1"]
        n49["YUG_local_developers"]
        n50["YUG_purchase_foreign"]
    end
    subgraph tier_2["Tier 2"]
        n51["YUG_ikarus"]
        n52{"YUG_license_production"}
        n53["YUG_rogozarski"]
        n54["YUG_zmaj"]
    end
    subgraph tier_3["Tier 3"]
        n55["YUG_bomber_license"]
        n56["YUG_fighter_license"]
        n57["YUG_form_mechanics"]
        n58["YUG_kraljevo_state_airlines_factory"]
        n59["YUG_the_ik_3"]
    end
    subgraph tier_4["Tier 4"]
        n60["YUG_bomber_project"]
        n61["YUG_expanded_repair_facilities"]
        n62["YUG_heavy_fighter_project"]
    end
    n52 --> n55
    n59 --> n60
    n58 --> n61
    n57 --> n61
    n52 --> n56
    n52 --> n57
    n51 --> n57
    n53 --> n57
    n54 --> n57
    n59 --> n62
    n49 --> n51
    n52 --> n58
    n50 --> n52
    n48 --> n49
    n48 --> n50
    n49 --> n53
    n51 --> n59
    n53 --> n59
    n54 --> n59
    n49 --> n54
    n55 x--x n56
    n49 x--x n50
```

# YUG_recognize_the_soviet_union

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n63["YUG_friendship_treaty_with_italy"]
        n64(("YUG_recognize_the_soviet_union"))
        n65["YUG_reinforce_old_alliances"]
        n66["YUG_western_focus"]
    end
    subgraph tier_1["Tier 1"]
        n67["YUG_form_peasant_councils"]
    end
    subgraph tier_2["Tier 2"]
        n68{"YUG_abolish_the_monarchy"}
        n69["YUG_brigadistas"]
        n70["YUG_local_militias"]
    end
    subgraph tier_3["Tier 3"]
        n71["YUG_organized_partizans"]
        n72["YUG_soviet_cooperation"]
        n73["YUG_yugoslavian_international_communism"]
        n74["YUG_yugoslavian_path_to_communism"]
    end
    subgraph tier_4["Tier 4"]
        n75["YUG_form_the_federal_republic"]
        n76["YUG_join_comintern"]
        n77["YUG_pan_slavic_workers_congress"]
    end
    subgraph tier_5["Tier 5"]
        n78["YUG_economic_centralization"]
        n79["YUG_federal_defense_council"]
        n80["YUG_invite_albania"]
        n81["YUG_invite_bulgaria"]
        n82["YUG_neutralize_the_opposition"]
        n83["YUG_research_collaboration"]
    end
    subgraph tier_6["Tier 6"]
        n84["YUG_pan_balkan_workers_congress"]
    end
    subgraph tier_7["Tier 7"]
        n85["YUG_form_the_balkan_federation"]
        n86["YUG_invite_greece"]
        n87["YUG_invite_hungary"]
        n88["YUG_invite_romania"]
    end
    subgraph tier_8["Tier 8"]
        n89["YUG_invite_turkey"]
    end
    n67 --> n68
    n63 --> n69
    n65 --> n69
    n67 --> n69
    n75 --> n78
    n75 --> n79
    n64 --> n67
    n84 --> n85
    n74 --> n75
    n72 --> n75
    n73 --> n75
    n77 --> n80
    n77 --> n81
    n84 --> n86
    n84 --> n87
    n84 --> n88
    n86 --> n89
    n87 --> n89
    n88 --> n89
    n72 --> n76
    n65 --> n70
    n63 --> n70
    n67 --> n70
    n75 --> n82
    n70 --> n71
    n81 --> n84
    n80 --> n84
    n79 --> n84
    n82 --> n84
    n74 --> n77
    n76 --> n83
    n68 --> n72
    n68 --> n73
    n68 --> n74
    n64 x--x n66
    n72 x--x n73
    n72 x--x n74
    n73 x--x n74
```

# YUG_western_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n67["YUG_form_peasant_councils"]
        n64["YUG_recognize_the_soviet_union"]
        n66{"YUG_western_focus"}
    end
    subgraph tier_1["Tier 1"]
        n63["YUG_friendship_treaty_with_italy"]
        n65["YUG_reinforce_old_alliances"]
    end
    subgraph tier_2["Tier 2"]
        n90{"YUG_attract_allied_capital"}
        n91{"YUG_attract_axis_capital"}
        n69["YUG_brigadistas"]
        n70["YUG_local_militias"]
    end
    subgraph tier_3["Tier 3"]
        n92{"YUG_evolution"}
        n93{"YUG_limited_self_government"}
        n71["YUG_organized_partizans"]
    end
    subgraph tier_4["Tier 4"]
        n94{"YUG_crush_the_ustasa"}
        n95{"YUG_devolved_croatia"}
        n96["YUG_dissolve_serbia"]
        n97{"YUG_establish_the_banovina_of_croatia"}
        n98{"YUG_united_autonomous_croatia"}
    end
    subgraph tier_5["Tier 5"]
        n99{"YUG_ban_slovene_nationalist_parties"}
        n100["YUG_divide_bosnia"]
        n101["YUG_safeguard_bosnia"]
        n102{"YUG_slovenia_for_support"}
    end
    subgraph tier_6["Tier 6"]
        n103{"YUG_concessions_for_macedonians"}
        n104{"YUG_fate_of_banat"}
        n105{"YUG_surrender_macedonia"}
    end
    subgraph tier_7["Tier 7"]
        n106["YUG_end_the_regency"]
        n107["YUG_invite_german_military_mission"]
        n108{"YUG_join_axis"}
        n109["YUG_towards_independence"]
        n110["YUG_united_kingdom"]
    end
    subgraph tier_8["Tier 8"]
        n111{"YUG_coronation"}
        n112["YUG_defence_army_of_yugoslavia"]
        n113["YUG_guarantee_religious_liberties"]
        n114{"YUG_royal_wedding"}
        n115["YUG_surrender_italian_claims"]
        n116["YUG_zara_for_axis"]
    end
    subgraph tier_9["Tier 9"]
        n117["YUG_claim_bulgaria"]
        n118["YUG_defence_league"]
        n119["YUG_enforced_neutrality"]
        n120["YUG_invite_italian_naval_experts"]
        n121["YUG_join_allies"]
        n122["YUG_reunite_the_kingdom"]
        n123["YUG_subjugate_albania"]
    end
    subgraph tier_10["Tier 10"]
        n124["YUG_allied_air_combat_school"]
        n125["YUG_fortress_yugoslavia"]
        n126["YUG_press_bulgarian_claims_on_thrace"]
        n127["YUG_proclaim_greater_yugoslavia"]
    end
    subgraph tier_11["Tier 11"]
        n128["YUG_all_yugoslavian_regiments"]
    end
    n127 --> n128
    n118 --> n128
    n121 --> n124
    n63 --> n90
    n65 --> n90
    n63 --> n91
    n65 --> n91
    n94 --> n99
    n97 --> n99
    n63 --> n69
    n65 --> n69
    n67 --> n69
    n116 --> n117
    n115 --> n117
    n102 --> n103
    n99 --> n103
    n106 --> n111
    n108 --> n111
    n92 --> n94
    n109 --> n112
    n112 --> n118
    n93 --> n95
    n93 --> n96
    n98 --> n100
    n95 --> n100
    n103 --> n106
    n105 --> n106
    n104 --> n106
    n114 --> n119
    n111 --> n119
    n92 --> n97
    n91 --> n92
    n96 --> n104
    n101 --> n104
    n100 --> n104
    n119 --> n125
    n66 --> n63
    n110 --> n113
    n103 --> n107
    n105 --> n107
    n104 --> n107
    n116 --> n120
    n115 --> n120
    n114 --> n121
    n111 --> n121
    n103 --> n108
    n105 --> n108
    n104 --> n108
    n90 --> n93
    n65 --> n70
    n63 --> n70
    n67 --> n70
    n70 --> n71
    n117 --> n126
    n117 --> n127
    n123 --> n127
    n66 --> n65
    n113 --> n122
    n106 --> n114
    n98 --> n101
    n95 --> n101
    n94 --> n102
    n97 --> n102
    n116 --> n123
    n115 --> n123
    n108 --> n115
    n102 --> n105
    n99 --> n105
    n104 --> n109
    n93 --> n98
    n104 --> n110
    n108 --> n116
    n99 x--x n102
    n103 x--x n105
    n94 x--x n97
    n95 x--x n98
    n100 x--x n101
    n106 x--x n108
    n119 x--x n121
    n92 x--x n93
    n63 x--x n65
    n64 x--x n66
    n115 x--x n116
    n109 x--x n110
```
