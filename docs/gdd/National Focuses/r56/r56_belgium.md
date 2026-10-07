# BEL_Support_the_congo_railways

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["BEL_Expand_the_port_of_Antwerp"]
        n2(("BEL_Support_the_congo_railways"))
    end
    subgraph tier_1["Tier 1"]
        n3["BEL_congo_rubber"]
        n4["BEL_support_copper_mining"]
        n5["BEL_support_tungsten_mining"]
        n6["BEL_transform_the_congo"]
    end
    subgraph tier_2["Tier 2"]
        n7["BEL_congo_rubber2"]
        n8["BEL_further_nuclear_research"]
        n9["BEL_support_copper_mining2"]
        n10["BEL_support_tungsten_mining2"]
        n11["BEL_transform_the_congo2"]
    end
    subgraph tier_3["Tier 3"]
        n12["BEL_support_tungsten_mining3"]
        n13["BEL_transform_the_congo3"]
    end
    subgraph tier_4["Tier 4"]
        n14["BEL_support_tungsten_mining4"]
    end
    n2 --> n3
    n3 --> n7
    n6 --> n8
    n1 --> n8
    n2 --> n4
    n4 --> n9
    n2 --> n5
    n5 --> n10
    n10 --> n12
    n12 --> n14
    n2 --> n6
    n6 --> n11
    n11 --> n13
```

# BEL_accept_van_den_den_bergen_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["BEL_Expand_the_port_of_Antwerp"]
        n15(("BEL_accept_van_den_den_bergen_plan"))
        n16["BEL_begin_rearmement"]
        n17["BEL_urbanize_wallonie"]
        n18["BEL_van_overstraeten_aa_guns"]
    end
    subgraph tier_1["Tier 1"]
        n19["BEL_form_air_guard_of_the_territory"]
        n20{"BEL_invest_in_FN_Herstal"}
        n21["BEL_lessons_from_wwi"]
        n22{"BEL_motorised_support"}
    end
    subgraph tier_2["Tier 2"]
        n23["BEL_equipement_modernization"]
        n24["BEL_establish_radio_stations"]
        n25["BEL_fortress_belgium"]
        n26["BEL_fortress_french_border"]
        n27{"BEL_light_tank_destroyers"}
        n28["BEL_logistical_brigades"]
        n29{"BEL_restore_the_auto_canon_unit"}
        n30["BEL_support_innovation"]
    end
    subgraph tier_3["Tier 3"]
        n31["BEL_daring_paratroopers"]
        n32["BEL_doctrines_of_the_present"]
        n33{"BEL_experimental_weaponry"}
        n34{"BEL_prototype_weapons"}
        n35["BEL_reinforce_antwerp_brussels"]
        n36["BEL_urban_projects_capital2"]
    end
    subgraph tier_4["Tier 4"]
        n37["BEL_Antwerp_Oil_Industry"]
        n38["BEL_buy_back_the_railway_gun"]
        n39["BEL_continue_the_tank_destroyer_program"]
        n40["BEL_military_research_interest"]
        n41["BEL_modernize_tanks"]
        n42["BEL_resist_and_bite_r56"]
        n43["BEL_specialized_divisions"]
    end
    subgraph tier_5["Tier 5"]
        n44["BEL_invest_in_nuclear_program"]
    end
    n36 --> n37
    n34 --> n38
    n34 --> n39
    n27 --> n39
    n23 --> n31
    n23 --> n32
    n21 --> n23
    n19 --> n24
    n23 --> n33
    n16 --> n19
    n15 --> n19
    n18 --> n19
    n20 --> n25
    n20 --> n26
    n17 --> n20
    n16 --> n20
    n15 --> n20
    n40 --> n44
    n16 --> n21
    n15 --> n21
    n22 --> n27
    n22 --> n28
    n33 --> n40
    n34 --> n40
    n34 --> n41
    n27 --> n41
    n29 --> n41
    n16 --> n22
    n15 --> n22
    n23 --> n34
    n25 --> n35
    n26 --> n35
    n33 --> n42
    n22 --> n29
    n33 --> n43
    n1 --> n30
    n20 --> n30
    n30 --> n36
    n15 x--x n16
    n39 x--x n41
    n25 x--x n26
    n27 x--x n29
    n42 x--x n43
```

# BEL_air_force_congo

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n45(("BEL_air_force_congo"))
        n46["BEL_expand_the_navy"]
        n47["BEL_revise_air_doctrine"]
        n18["BEL_van_overstraeten_aa_guns"]
    end
    subgraph tier_1["Tier 1"]
        n48["BEL_Renard_fighters"]
        n49{"BEL_license_production"}
    end
    subgraph tier_2["Tier 2"]
        n50["BEL_SABCAs_bombers"]
        n51["BEL_aerial_support"]
        n52["BEL_fighter_license"]
    end
    subgraph tier_3["Tier 3"]
        n53["BEL_Foreign_aviation_studies"]
        n54["BEL_SABCAs_CAS"]
    end
    subgraph tier_4["Tier 4"]
        n55["BEL_interest_in_carriers"]
        n56["BEL_start_rocket_program"]
    end
    n50 --> n53
    n52 --> n53
    n47 --> n48
    n45 --> n48
    n50 --> n54
    n52 --> n54
    n49 --> n50
    n48 --> n51
    n49 --> n52
    n46 --> n55
    n53 --> n55
    n47 --> n49
    n45 --> n49
    n53 --> n56
    n50 x--x n52
    n45 x--x n47
    n45 x--x n18
```

# BEL_begin_rearmement

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["BEL_Expand_the_port_of_Antwerp"]
        n15["BEL_accept_van_den_den_bergen_plan"]
        n16(("BEL_begin_rearmement"))
        n17["BEL_urbanize_wallonie"]
        n18["BEL_van_overstraeten_aa_guns"]
    end
    subgraph tier_1["Tier 1"]
        n19["BEL_form_air_guard_of_the_territory"]
        n20{"BEL_invest_in_FN_Herstal"}
        n21["BEL_lessons_from_wwi"]
        n22{"BEL_motorised_support"}
    end
    subgraph tier_2["Tier 2"]
        n23["BEL_equipement_modernization"]
        n24["BEL_establish_radio_stations"]
        n25["BEL_fortress_belgium"]
        n26["BEL_fortress_french_border"]
        n27{"BEL_light_tank_destroyers"}
        n28["BEL_logistical_brigades"]
        n29{"BEL_restore_the_auto_canon_unit"}
        n30["BEL_support_innovation"]
    end
    subgraph tier_3["Tier 3"]
        n31["BEL_daring_paratroopers"]
        n32["BEL_doctrines_of_the_present"]
        n33{"BEL_experimental_weaponry"}
        n34{"BEL_prototype_weapons"}
        n35["BEL_reinforce_antwerp_brussels"]
        n36["BEL_urban_projects_capital2"]
    end
    subgraph tier_4["Tier 4"]
        n37["BEL_Antwerp_Oil_Industry"]
        n38["BEL_buy_back_the_railway_gun"]
        n39["BEL_continue_the_tank_destroyer_program"]
        n40["BEL_military_research_interest"]
        n41["BEL_modernize_tanks"]
        n42["BEL_resist_and_bite_r56"]
        n43["BEL_specialized_divisions"]
    end
    subgraph tier_5["Tier 5"]
        n44["BEL_invest_in_nuclear_program"]
    end
    n36 --> n37
    n34 --> n38
    n34 --> n39
    n27 --> n39
    n23 --> n31
    n23 --> n32
    n21 --> n23
    n19 --> n24
    n23 --> n33
    n16 --> n19
    n15 --> n19
    n18 --> n19
    n20 --> n25
    n20 --> n26
    n17 --> n20
    n16 --> n20
    n15 --> n20
    n40 --> n44
    n16 --> n21
    n15 --> n21
    n22 --> n27
    n22 --> n28
    n33 --> n40
    n34 --> n40
    n34 --> n41
    n27 --> n41
    n29 --> n41
    n16 --> n22
    n15 --> n22
    n23 --> n34
    n25 --> n35
    n26 --> n35
    n33 --> n42
    n22 --> n29
    n33 --> n43
    n1 --> n30
    n20 --> n30
    n30 --> n36
    n15 x--x n16
    n39 x--x n41
    n25 x--x n26
    n27 x--x n29
    n42 x--x n43
```

# BEL_belgian_navy_in_exile

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n53["BEL_Foreign_aviation_studies"]
        n57{"BEL_belgian_navy_in_exile"}
        n58["BEL_multipurpose_bombers"]
        n59{"BEL_recreate_the_navy"}
    end
    subgraph tier_1["Tier 1"]
        n60["BEL_reinvigorate_naval_prowess_of_old"]
        n61["BEL_submarine_operations"]
    end
    subgraph tier_2["Tier 2"]
        n62["BEL_cruisers_and_destroyers"]
        n46["BEL_expand_the_navy"]
        n63["BEL_rule_the_sea_through_the_sky"]
        n64["BEL_submarine_improvements"]
    end
    subgraph tier_3["Tier 3"]
        n55["BEL_interest_in_carriers"]
        n65["BEL_naval_artillery"]
        n66["BEL_naval_mining"]
        n67["BEL_stealth_upgrades"]
    end
    n60 --> n62
    n61 --> n62
    n60 --> n46
    n46 --> n55
    n53 --> n55
    n62 --> n65
    n46 --> n65
    n62 --> n66
    n59 --> n60
    n57 --> n60
    n58 --> n63
    n61 --> n63
    n60 --> n63
    n64 --> n67
    n61 --> n64
    n59 --> n61
    n57 --> n61
    n57 x--x n59
    n60 x--x n61
```

# BEL_form_coalition_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n68{"BEL_form_coalition_government"}
        n69["BEL_go_left"]
        n70["BEL_go_right"]
        n71["BEL_king_reaction"]
    end
    subgraph tier_1["Tier 1"]
        n72["BEL_democratic_influence"]
        n73["BEL_stay_neutral"]
    end
    subgraph tier_2["Tier 2"]
        n74["BEL_army_linguistic_divide"]
        n75["BEL_benelux_economic_cooperation"]
        n76["BEL_deterrence"]
        n77{"BEL_join_britain_alliance"}
    end
    subgraph tier_3["Tier 3"]
        n78{"BEL_armed_neutrality"}
        n79{"BEL_benelux_faction"}
        n80["BEL_british_ship_designs"]
    end
    subgraph tier_4["Tier 4"]
        n81["BEL_benelux_tech_sharing_group"]
        n82["BEL_launch_V_campaign"]
        n83["BEL_technology_sharing_democracy"]
        n84["BEL_why_we_fight"]
    end
    subgraph tier_5["Tier 5"]
        n85["BEL_exiled_evacuated_industries"]
        n86["BEL_exiled_intelligence_service"]
    end
    n76 --> n78
    n73 --> n74
    n72 --> n74
    n71 --> n74
    n72 --> n75
    n75 --> n79
    n79 --> n81
    n77 --> n80
    n68 --> n72
    n73 --> n76
    n71 --> n76
    n84 --> n85
    n84 --> n86
    n72 --> n77
    n79 --> n82
    n77 --> n82
    n78 --> n82
    n68 --> n73
    n79 --> n83
    n77 --> n83
    n78 --> n83
    n79 --> n84
    n77 --> n84
    n78 --> n84
    n72 x--x n73
    n68 x--x n69
    n68 x--x n70
    n82 x--x n84
```

# BEL_go_left

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n68["BEL_form_coalition_government"]
        n69(("BEL_go_left"))
        n70["BEL_go_right"]
    end
    subgraph tier_1["Tier 1"]
        n87{"BEL_communist_brigades"}
        n88["BEL_communist_youth"]
    end
    subgraph tier_2["Tier 2"]
        n89{"BEL_communist_army"}
        n90{"BEL_support_pcf"}
        n91{"BEL_support_pcf2"}
    end
    subgraph tier_3["Tier 3"]
        n92["BEL_independent_revolution"]
        n93["BEL_sign_pact_with_soviets"]
    end
    subgraph tier_4["Tier 4"]
        n94["BEL_invite_france"]
        n95{"BEL_political_commissars"}
        n96["BEL_technology_sharing_communism"]
    end
    subgraph tier_5["Tier 5"]
        n97["BEL_communist_propaganda_Benelux"]
        n98["BEL_puppet_netherlands"]
    end
    subgraph tier_6["Tier 6"]
        n99["BEL_ideological_propaganda"]
    end
    n88 --> n89
    n69 --> n87
    n95 --> n97
    n69 --> n88
    n97 --> n99
    n89 --> n92
    n90 --> n92
    n91 --> n92
    n92 --> n94
    n92 --> n95
    n93 --> n95
    n95 --> n98
    n89 --> n93
    n90 --> n93
    n91 --> n93
    n87 --> n90
    n87 --> n91
    n92 --> n96
    n93 --> n96
    n97 x--x n98
    n68 x--x n69
    n69 x--x n70
    n92 x--x n93
    n90 x--x n91
```

# BEL_go_right

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n68["BEL_form_coalition_government"]
        n69["BEL_go_left"]
        n70{"BEL_go_right"}
    end
    subgraph tier_1["Tier 1"]
        n100["BEL_choose_Rex"]
        n101["BEL_choose_Verdinaso"]
    end
    subgraph tier_2["Tier 2"]
        n102["BEL_fascist_youth_organizations"]
    end
    subgraph tier_3["Tier 3"]
        n103{"BEL_belgian_militarism"}
        n104["BEL_fascist_legions"]
    end
    subgraph tier_4["Tier 4"]
        n105["BEL_an_ally_across_the_channel"]
        n106["BEL_belgium_first"]
        n107["BEL_claim_the_benelux"]
        n108["BEL_germany_millitary_coop"]
        n109["BEL_reactivate_caur_contacts"]
        n110["BEL_unite_dietsland"]
    end
    subgraph tier_5["Tier 5"]
        n111["BEL_burgundian_circuit"]
        n112["BEL_proclaim_dietsland"]
        n113["BEL_propaganda_ministry"]
        n114["BEL_technology_sharing_fascism"]
    end
    subgraph tier_6["Tier 6"]
        n115["BEL_colonial_claims"]
        n116["BEL_proclaim_dietsche_rijk"]
        n117["BEL_proclaim_thiois_empire"]
    end
    n103 --> n105
    n102 --> n103
    n103 --> n106
    n107 --> n111
    n70 --> n100
    n70 --> n101
    n103 --> n107
    n111 --> n115
    n110 --> n115
    n102 --> n104
    n100 --> n102
    n101 --> n102
    n103 --> n108
    n112 --> n116
    n110 --> n112
    n111 --> n117
    n108 --> n113
    n106 --> n113
    n109 --> n113
    n105 --> n113
    n103 --> n109
    n108 --> n114
    n106 --> n114
    n109 --> n114
    n105 --> n114
    n103 --> n110
    n105 x--x n106
    n105 x--x n108
    n105 x--x n109
    n106 x--x n108
    n106 x--x n109
    n100 x--x n101
    n107 x--x n110
    n68 x--x n70
    n108 x--x n109
    n69 x--x n70
```

# BEL_king_reaction

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n79{"BEL_benelux_faction"}
        n72["BEL_democratic_influence"]
        n77{"BEL_join_britain_alliance"}
        n71(("BEL_king_reaction"))
        n73["BEL_stay_neutral"]
    end
    subgraph tier_1["Tier 1"]
        n74["BEL_army_linguistic_divide"]
        n76["BEL_deterrence"]
        n118["BEL_purge_radical_opposition"]
    end
    subgraph tier_2["Tier 2"]
        n78{"BEL_armed_neutrality"}
        n119["BEL_reduce_parlementarism"]
    end
    subgraph tier_3["Tier 3"]
        n82["BEL_launch_V_campaign"]
        n120["BEL_restore_constitution"]
        n83["BEL_technology_sharing_democracy"]
        n84["BEL_why_we_fight"]
    end
    subgraph tier_4["Tier 4"]
        n85["BEL_exiled_evacuated_industries"]
        n86["BEL_exiled_intelligence_service"]
    end
    n76 --> n78
    n73 --> n74
    n72 --> n74
    n71 --> n74
    n73 --> n76
    n71 --> n76
    n84 --> n85
    n84 --> n86
    n79 --> n82
    n77 --> n82
    n78 --> n82
    n71 --> n118
    n118 --> n119
    n119 --> n120
    n79 --> n83
    n77 --> n83
    n78 --> n83
    n79 --> n84
    n77 --> n84
    n78 --> n84
    n82 x--x n84
```

# BEL_recreate_the_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n53["BEL_Foreign_aviation_studies"]
        n57{"BEL_belgian_navy_in_exile"}
        n58["BEL_multipurpose_bombers"]
        n59{"BEL_recreate_the_navy"}
    end
    subgraph tier_1["Tier 1"]
        n60["BEL_reinvigorate_naval_prowess_of_old"]
        n61["BEL_submarine_operations"]
    end
    subgraph tier_2["Tier 2"]
        n62["BEL_cruisers_and_destroyers"]
        n46["BEL_expand_the_navy"]
        n63["BEL_rule_the_sea_through_the_sky"]
        n64["BEL_submarine_improvements"]
    end
    subgraph tier_3["Tier 3"]
        n55["BEL_interest_in_carriers"]
        n65["BEL_naval_artillery"]
        n66["BEL_naval_mining"]
        n67["BEL_stealth_upgrades"]
    end
    n60 --> n62
    n61 --> n62
    n60 --> n46
    n46 --> n55
    n53 --> n55
    n62 --> n65
    n46 --> n65
    n62 --> n66
    n59 --> n60
    n57 --> n60
    n58 --> n63
    n61 --> n63
    n60 --> n63
    n64 --> n67
    n61 --> n64
    n59 --> n61
    n57 --> n61
    n57 x--x n59
    n60 x--x n61
```

# BEL_revise_air_doctrine

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n45["BEL_air_force_congo"]
        n46["BEL_expand_the_navy"]
        n60["BEL_reinvigorate_naval_prowess_of_old"]
        n47(("BEL_revise_air_doctrine"))
        n61["BEL_submarine_operations"]
        n18["BEL_van_overstraeten_aa_guns"]
    end
    subgraph tier_1["Tier 1"]
        n48["BEL_Renard_fighters"]
        n49{"BEL_license_production"}
        n58["BEL_multipurpose_bombers"]
    end
    subgraph tier_2["Tier 2"]
        n50["BEL_SABCAs_bombers"]
        n51["BEL_aerial_support"]
        n52["BEL_fighter_license"]
        n63["BEL_rule_the_sea_through_the_sky"]
    end
    subgraph tier_3["Tier 3"]
        n53["BEL_Foreign_aviation_studies"]
        n54["BEL_SABCAs_CAS"]
    end
    subgraph tier_4["Tier 4"]
        n55["BEL_interest_in_carriers"]
        n56["BEL_start_rocket_program"]
    end
    n50 --> n53
    n52 --> n53
    n47 --> n48
    n45 --> n48
    n50 --> n54
    n52 --> n54
    n49 --> n50
    n48 --> n51
    n49 --> n52
    n46 --> n55
    n53 --> n55
    n47 --> n49
    n45 --> n49
    n47 --> n58
    n58 --> n63
    n61 --> n63
    n60 --> n63
    n53 --> n56
    n50 x--x n52
    n45 x--x n47
    n47 x--x n18
```

# BEL_urban_projects_capital

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15["BEL_accept_van_den_den_bergen_plan"]
        n16["BEL_begin_rearmement"]
        n6["BEL_transform_the_congo"]
        n121(("BEL_urban_projects_capital"))
    end
    subgraph tier_1["Tier 1"]
        n122["BEL_urban_projects_capital_industry"]
        n17["BEL_urbanize_wallonie"]
    end
    subgraph tier_2["Tier 2"]
        n1["BEL_Expand_the_port_of_Antwerp"]
        n20{"BEL_invest_in_FN_Herstal"}
    end
    subgraph tier_3["Tier 3"]
        n25["BEL_fortress_belgium"]
        n26["BEL_fortress_french_border"]
        n8["BEL_further_nuclear_research"]
        n30["BEL_support_innovation"]
    end
    subgraph tier_4["Tier 4"]
        n35["BEL_reinforce_antwerp_brussels"]
        n36["BEL_urban_projects_capital2"]
    end
    subgraph tier_5["Tier 5"]
        n37["BEL_Antwerp_Oil_Industry"]
    end
    n36 --> n37
    n122 --> n1
    n20 --> n25
    n20 --> n26
    n6 --> n8
    n1 --> n8
    n17 --> n20
    n16 --> n20
    n15 --> n20
    n25 --> n35
    n26 --> n35
    n1 --> n30
    n20 --> n30
    n30 --> n36
    n121 --> n122
    n121 --> n17
    n25 x--x n26
```

# BEL_van_overstraeten_aa_guns

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15["BEL_accept_van_den_den_bergen_plan"]
        n45["BEL_air_force_congo"]
        n16["BEL_begin_rearmement"]
        n47["BEL_revise_air_doctrine"]
        n18(("BEL_van_overstraeten_aa_guns"))
    end
    subgraph tier_1["Tier 1"]
        n123["BEL_aa_guns_expertise"]
        n19["BEL_form_air_guard_of_the_territory"]
    end
    subgraph tier_2["Tier 2"]
        n24["BEL_establish_radio_stations"]
    end
    n18 --> n123
    n19 --> n24
    n16 --> n19
    n15 --> n19
    n18 --> n19
    n45 x--x n18
    n47 x--x n18
```
