# YUG_army_modernization

```mermaid
flowchart TD
    n1["YUG_anti_tank_defenses"]
    n2{"YUG_armored_cavalry"}
    n3{"YUG_army_maneuvers"}
    n4(("YUG_army_modernization"))
    n5["YUG_artillery_regiments"]
    n6["YUG_domestic_artillery_production"]
    n7["YUG_form_parachute_battalions"]
    n8["YUG_independent_engineer_regiments"]
    n9["YUG_medal_for_extreme_bravery"]
    n10["YUG_modern_tanks"]
    n11["YUG_motorize_the_cavalry"]
    n12["YUG_motorized_logistics"]
    n13["YUG_motorized_recon_companies"]
    n14["YUG_mountain_brigades"]
    n15["YUG_small_arms"]
    n16["YUG_supremacy_of_defense"]
    n17["YUG_supremacy_of_offense"]
    n18["YUG_tank_conversions"]
    n19["YUG_tank_licenses"]
    n6 --> n1
    n11 --> n2
    n4 --> n3
    n17 --> n5
    n16 --> n5
    n15 --> n6
    n13 --> n7
    n14 --> n8
    n5 --> n9
    n2 --> n10
    n4 --> n11
    n11 --> n12
    n8 --> n13
    n4 --> n14
    n4 --> n15
    n3 --> n16
    n3 --> n17
    n2 --> n18
    n10 --> n19
    n10 x--x n18
    n16 x--x n17
```

# YUG_expand_the_serbian_shipyards

```mermaid
flowchart TD
    n20["YUG_adriatic_specialization"]
    n21["YUG_coastal_defense"]
    n22["YUG_contest_the_adriatic"]
    n23(("YUG_expand_the_serbian_shipyards"))
    n24["YUG_expand_the_split_shipyards"]
    n25{"YUG_expand_the_submarine_fleet"}
    n26{"YUG_heavy_cruiser_project"}
    n27{"YUG_modern_destroyers"}
    n28["YUG_naval_bombers"]
    n29["YUG_skilled_pilots"]
    n27 --> n20
    n25 --> n20
    n23 --> n21
    n21 --> n25
    n28 --> n27
    n22 --> n28
    n21 --> n28
    n26 --> n29
    n27 --> n29
    n20 x--x n29
    n23 x--x n24
```

# YUG_expand_the_split_shipyards

```mermaid
flowchart TD
    n20["YUG_adriatic_specialization"]
    n21["YUG_coastal_defense"]
    n22["YUG_contest_the_adriatic"]
    n23["YUG_expand_the_serbian_shipyards"]
    n24(("YUG_expand_the_split_shipyards"))
    n25{"YUG_expand_the_submarine_fleet"}
    n26{"YUG_heavy_cruiser_project"}
    n27{"YUG_modern_destroyers"}
    n28["YUG_naval_bombers"]
    n30["YUG_replace_the_dalmacija"]
    n29["YUG_skilled_pilots"]
    n27 --> n20
    n25 --> n20
    n24 --> n22
    n30 --> n26
    n28 --> n27
    n22 --> n28
    n21 --> n28
    n22 --> n30
    n26 --> n29
    n27 --> n29
    n20 x--x n29
    n23 x--x n24
```

# YUG_industrialization_program

```mermaid
flowchart TD
    n31["YUG_central_management"]
    n32["YUG_develop_civilian_industry"]
    n33["YUG_develop_military_industry"]
    n34["YUG_develop_slovenian_industry"]
    n35{"YUG_expand_the_mining_industry"}
    n36["YUG_expand_the_sarajevo_arsenals"]
    n37["YUG_expand_the_university_of_belgrad"]
    n38["YUG_expand_the_university_of_ljubljana"]
    n39{"YUG_expand_the_university_of_zagreb"}
    n40["YUG_exploit_the_pannonian_deposits"]
    n41["YUG_improve_light_industry"]
    n42["YUG_improve_serbian_rail_network"]
    n43(("YUG_industrialization_program"))
    n44["YUG_integrated_rail_network"]
    n45["YUG_local_self_management"]
    n46["YUG_rare_minerals_exploitation"]
    n47["YUG_serbian_steel"]
    n37 --> n31
    n35 --> n32
    n35 --> n33
    n44 --> n34
    n43 --> n35
    n45 --> n36
    n31 --> n36
    n42 --> n37
    n34 --> n38
    n32 --> n39
    n33 --> n39
    n46 --> n40
    n44 --> n41
    n42 --> n41
    n39 --> n42
    n39 --> n44
    n34 --> n45
    n35 --> n46
    n42 --> n47
    n32 x--x n33
    n42 x--x n44
```

# YUG_modernize_the_air_force

```mermaid
flowchart TD
    n48["YUG_bomber_license"]
    n49["YUG_bomber_project"]
    n50["YUG_expanded_repair_facilities"]
    n51["YUG_fighter_license"]
    n52["YUG_form_mechanics"]
    n53["YUG_heavy_fighter_project"]
    n54["YUG_ikarus"]
    n55["YUG_kraljevo_state_airlines_factory"]
    n56{"YUG_license_production"}
    n57["YUG_local_developers"]
    n58{"YUG_modernize_the_air_force"}
    n59["YUG_purchase_foreign"]
    n60["YUG_rogozarski"]
    n61["YUG_the_ik_3"]
    n62["YUG_zmaj"]
    n56 --> n48
    n61 --> n49
    n55 --> n50
    n52 --> n50
    n56 --> n51
    n56 --> n52
    n54 --> n52
    n60 --> n52
    n62 --> n52
    n61 --> n53
    n57 --> n54
    n56 --> n55
    n59 --> n56
    n58 --> n57
    n58 --> n59
    n57 --> n60
    n54 --> n61
    n60 --> n61
    n62 --> n61
    n57 --> n62
    n48 x--x n51
    n57 x--x n59
```

# YUG_recognize_the_soviet_union

```mermaid
flowchart TD
    n63{"YUG_abolish_the_monarchy"}
    n64["YUG_brigadistas"]
    n65["YUG_economic_centralization"]
    n66["YUG_federal_defense_council"]
    n67["YUG_form_peasant_councils"]
    n68["YUG_form_the_balkan_federation"]
    n69["YUG_form_the_federal_republic"]
    n70["YUG_friendship_treaty_with_italy"]
    n71["YUG_invite_albania"]
    n72["YUG_invite_bulgaria"]
    n73["YUG_invite_greece"]
    n74["YUG_invite_hungary"]
    n75["YUG_invite_romania"]
    n76["YUG_invite_turkey"]
    n77["YUG_join_comintern"]
    n78["YUG_local_militias"]
    n79["YUG_neutralize_the_opposition"]
    n80["YUG_organized_partizans"]
    n81["YUG_pan_balkan_workers_congress"]
    n82["YUG_pan_slavic_workers_congress"]
    n83(("YUG_recognize_the_soviet_union"))
    n84["YUG_reinforce_old_alliances"]
    n85["YUG_research_collaboration"]
    n86["YUG_soviet_cooperation"]
    n87["YUG_western_focus"]
    n88["YUG_yugoslavian_international_communism"]
    n89["YUG_yugoslavian_path_to_communism"]
    n67 --> n63
    n70 --> n64
    n84 --> n64
    n67 --> n64
    n69 --> n65
    n69 --> n66
    n83 --> n67
    n81 --> n68
    n89 --> n69
    n86 --> n69
    n88 --> n69
    n82 --> n71
    n82 --> n72
    n81 --> n73
    n81 --> n74
    n81 --> n75
    n73 --> n76
    n74 --> n76
    n75 --> n76
    n86 --> n77
    n84 --> n78
    n70 --> n78
    n67 --> n78
    n69 --> n79
    n78 --> n80
    n72 --> n81
    n71 --> n81
    n66 --> n81
    n79 --> n81
    n89 --> n82
    n77 --> n85
    n63 --> n86
    n63 --> n88
    n63 --> n89
    n83 x--x n87
    n86 x--x n88
    n86 x--x n89
    n88 x--x n89
```

# YUG_western_focus

```mermaid
flowchart TD
    n90["YUG_all_yugoslavian_regiments"]
    n91["YUG_allied_air_combat_school"]
    n92{"YUG_attract_allied_capital"}
    n93{"YUG_attract_axis_capital"}
    n94{"YUG_ban_slovene_nationalist_parties"}
    n64["YUG_brigadistas"]
    n95["YUG_claim_bulgaria"]
    n96{"YUG_concessions_for_macedonians"}
    n97{"YUG_coronation"}
    n98{"YUG_crush_the_ustasa"}
    n99["YUG_defence_army_of_yugoslavia"]
    n100["YUG_defence_league"]
    n101{"YUG_devolved_croatia"}
    n102["YUG_dissolve_serbia"]
    n103["YUG_divide_bosnia"]
    n104["YUG_end_the_regency"]
    n105["YUG_enforced_neutrality"]
    n106{"YUG_establish_the_banovina_of_croatia"}
    n107{"YUG_evolution"}
    n108{"YUG_fate_of_banat"}
    n67["YUG_form_peasant_councils"]
    n109["YUG_fortress_yugoslavia"]
    n70["YUG_friendship_treaty_with_italy"]
    n110["YUG_guarantee_religious_liberties"]
    n111["YUG_invite_german_military_mission"]
    n112["YUG_invite_italian_naval_experts"]
    n113["YUG_join_allies"]
    n114{"YUG_join_axis"}
    n115{"YUG_limited_self_government"}
    n78["YUG_local_militias"]
    n80["YUG_organized_partizans"]
    n116["YUG_press_bulgarian_claims_on_thrace"]
    n117["YUG_proclaim_greater_yugoslavia"]
    n83["YUG_recognize_the_soviet_union"]
    n84["YUG_reinforce_old_alliances"]
    n118["YUG_reunite_the_kingdom"]
    n119{"YUG_royal_wedding"}
    n120["YUG_safeguard_bosnia"]
    n121{"YUG_slovenia_for_support"}
    n122["YUG_subjugate_albania"]
    n123["YUG_surrender_italian_claims"]
    n124{"YUG_surrender_macedonia"}
    n125["YUG_towards_independence"]
    n126{"YUG_united_autonomous_croatia"}
    n127["YUG_united_kingdom"]
    n87{"YUG_western_focus"}
    n128["YUG_zara_for_axis"]
    n117 --> n90
    n100 --> n90
    n113 --> n91
    n70 --> n92
    n84 --> n92
    n70 --> n93
    n84 --> n93
    n98 --> n94
    n106 --> n94
    n70 --> n64
    n84 --> n64
    n67 --> n64
    n128 --> n95
    n123 --> n95
    n121 --> n96
    n94 --> n96
    n104 --> n97
    n114 --> n97
    n107 --> n98
    n125 --> n99
    n99 --> n100
    n115 --> n101
    n115 --> n102
    n126 --> n103
    n101 --> n103
    n96 --> n104
    n124 --> n104
    n108 --> n104
    n119 --> n105
    n97 --> n105
    n107 --> n106
    n93 --> n107
    n102 --> n108
    n120 --> n108
    n103 --> n108
    n105 --> n109
    n87 --> n70
    n127 --> n110
    n96 --> n111
    n124 --> n111
    n108 --> n111
    n128 --> n112
    n123 --> n112
    n119 --> n113
    n97 --> n113
    n96 --> n114
    n124 --> n114
    n108 --> n114
    n92 --> n115
    n84 --> n78
    n70 --> n78
    n67 --> n78
    n78 --> n80
    n95 --> n116
    n95 --> n117
    n122 --> n117
    n87 --> n84
    n110 --> n118
    n104 --> n119
    n126 --> n120
    n101 --> n120
    n98 --> n121
    n106 --> n121
    n128 --> n122
    n123 --> n122
    n114 --> n123
    n121 --> n124
    n94 --> n124
    n108 --> n125
    n115 --> n126
    n108 --> n127
    n114 --> n128
    n94 x--x n121
    n96 x--x n124
    n98 x--x n106
    n101 x--x n126
    n103 x--x n120
    n104 x--x n114
    n105 x--x n113
    n107 x--x n115
    n70 x--x n84
    n83 x--x n87
    n123 x--x n128
    n125 x--x n127
```
