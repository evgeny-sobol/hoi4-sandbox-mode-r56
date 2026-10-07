# KOR_Industrial_Boom

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("KOR_Industrial_Boom"))
    end
    subgraph tier_1["Tier 1"]
        n2["KOR_Industrial_Expansion"]
    end
    subgraph tier_2["Tier 2"]
        n3["KOR_modern_electronics"]
    end
    subgraph tier_3["Tier 3"]
        n4["KOR_expanded_research_programs"]
    end
    n1 --> n2
    n3 --> n4
    n2 --> n3
```

# KOR_collaboration_with_japan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n5{"KOR_collaboration_with_japan"}
        n6{"KOR_collaboration_with_overlord"}
        n7["KOR_conventional_warfare"]
        n8["KOR_guerilla_experience"]
        n9{"KOR_return_of_the_government_in_exile"}
    end
    subgraph tier_1["Tier 1"]
        n10{"KOR_experience_of_the_korean_liberation_army"}
        n11{"KOR_new_korean_army"}
        n12{"KOR_reorganize_the_administration"}
        n13{"KOR_repeal_colonial_restrictions"}
    end
    subgraph tier_2["Tier 2"]
        n14{"KOR_amnesty_for_ex_japanese_army_officers"}
        n15{"KOR_apply_democratic_program"}
        n16["KOR_army_reform"]
        n17["KOR_defense_mobilization"]
        n18["KOR_develop_gold_mining_near_unsan"]
        n19{"KOR_embrace_peoples_tutelage"}
        n20{"KOR_integrate_socialist_aligned_guerillas"}
        n21["KOR_rise_of_the_chaebols"]
        n22["KOR_take_over_air_bases"]
    end
    subgraph tier_3["Tier 3"]
        n23["KOR_army_modernization"]
        n24["KOR_equipment_effort"]
        n25["KOR_establish_a_military_academy"]
        n26["KOR_hyundai_engineering"]
        n27["KOR_hyundai_vehicles"]
        n28["KOR_internationalism_focus"]
        n29["KOR_keep_ties_with_the_KMT"]
        n30["KOR_nationalism_focus"]
        n31["KOR_pyeongtaek_airplane_workshop"]
        n32["KOR_restore_imperial_power"]
        n33["KOR_search_allies"]
        n34["KOR_semi_isolation"]
        n35["KOR_seoul_busan_infrastructure"]
        n36["KOR_supervize_equipment_production"]
    end
    subgraph tier_4["Tier 4"]
        n37["KOR_bomber"]
        n38["KOR_cement_monarchic_rule"]
        n39["KOR_daelim_petrochemicals"]
        n40["KOR_defensive_preparation"]
        n41["KOR_equipment_effort_2"]
        n42["KOR_equipment_effort_3"]
        n43["KOR_establish_a_armor_corp"]
        n44["KOR_expand_jinsen_arsenal"]
        n45["KOR_fighter"]
        n46["KOR_invade_manchuria"]
        n47["KOR_militarism"]
        n48["KOR_modernize_mining_industry"]
        n49["KOR_motorization_effort"]
        n50["KOR_naval_bomber"]
        n51["KOR_youth_units"]
    end
    subgraph tier_5["Tier 5"]
        n52["KOR_devotion_to_the_emperor"]
        n53["KOR_field_hospitals"]
        n54["KOR_invade_soviet_union"]
        n55["KOR_mechanization_effort"]
        n56["KOR_military_industrial_cooperation"]
        n57["KOR_modernized_air_force"]
        n58["KOR_signal_companies"]
        n59["KOR_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n60["KOR_modern_logistics"]
    end
    n10 --> n14
    n11 --> n14
    n13 --> n15
    n12 --> n15
    n16 --> n23
    n10 --> n16
    n11 --> n16
    n8 --> n16
    n7 --> n16
    n31 --> n37
    n32 --> n38
    n27 --> n39
    n13 --> n17
    n10 --> n17
    n15 --> n40
    n28 --> n40
    n13 --> n18
    n12 --> n18
    n47 --> n52
    n13 --> n19
    n12 --> n19
    n16 --> n24
    n24 --> n41
    n24 --> n42
    n23 --> n43
    n16 --> n25
    n26 --> n44
    n27 --> n44
    n9 --> n10
    n5 --> n10
    n6 --> n10
    n49 --> n53
    n31 --> n45
    n21 --> n26
    n21 --> n27
    n10 --> n20
    n20 --> n28
    n15 --> n46
    n28 --> n46
    n30 --> n46
    n32 --> n46
    n47 --> n54
    n15 --> n29
    n19 --> n29
    n43 --> n55
    n49 --> n55
    n30 --> n47
    n32 --> n47
    n44 --> n56
    n48 --> n56
    n39 --> n56
    n53 --> n60
    n55 --> n60
    n58 --> n60
    n26 --> n48
    n45 --> n57
    n37 --> n57
    n50 --> n57
    n23 --> n49
    n14 --> n30
    n31 --> n50
    n5 --> n11
    n6 --> n11
    n22 --> n31
    n9 --> n12
    n5 --> n12
    n6 --> n12
    n9 --> n13
    n5 --> n13
    n6 --> n13
    n14 --> n32
    n12 --> n21
    n13 --> n21
    n15 --> n33
    n15 --> n34
    n21 --> n35
    n43 --> n58
    n49 --> n58
    n42 --> n59
    n41 --> n59
    n16 --> n36
    n10 --> n22
    n7 --> n22
    n8 --> n22
    n30 --> n51
    n28 --> n51
    n14 x--x n20
    n15 x--x n28
    n15 x--x n30
    n15 x--x n32
    n5 x--x n6
    n10 x--x n11
    n28 x--x n30
    n28 x--x n32
    n29 x--x n33
    n29 x--x n34
    n30 x--x n32
    n33 x--x n34
```

# KOR_collaboration_with_overlord

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n5{"KOR_collaboration_with_japan"}
        n6{"KOR_collaboration_with_overlord"}
        n7["KOR_conventional_warfare"]
        n8["KOR_guerilla_experience"]
        n9{"KOR_return_of_the_government_in_exile"}
    end
    subgraph tier_1["Tier 1"]
        n10{"KOR_experience_of_the_korean_liberation_army"}
        n11{"KOR_new_korean_army"}
        n12{"KOR_reorganize_the_administration"}
        n13{"KOR_repeal_colonial_restrictions"}
    end
    subgraph tier_2["Tier 2"]
        n14{"KOR_amnesty_for_ex_japanese_army_officers"}
        n15{"KOR_apply_democratic_program"}
        n16["KOR_army_reform"]
        n17["KOR_defense_mobilization"]
        n18["KOR_develop_gold_mining_near_unsan"]
        n19{"KOR_embrace_peoples_tutelage"}
        n20{"KOR_integrate_socialist_aligned_guerillas"}
        n21["KOR_rise_of_the_chaebols"]
        n22["KOR_take_over_air_bases"]
    end
    subgraph tier_3["Tier 3"]
        n23["KOR_army_modernization"]
        n24["KOR_equipment_effort"]
        n25["KOR_establish_a_military_academy"]
        n26["KOR_hyundai_engineering"]
        n27["KOR_hyundai_vehicles"]
        n28["KOR_internationalism_focus"]
        n29["KOR_keep_ties_with_the_KMT"]
        n30["KOR_nationalism_focus"]
        n31["KOR_pyeongtaek_airplane_workshop"]
        n32["KOR_restore_imperial_power"]
        n33["KOR_search_allies"]
        n34["KOR_semi_isolation"]
        n35["KOR_seoul_busan_infrastructure"]
        n36["KOR_supervize_equipment_production"]
    end
    subgraph tier_4["Tier 4"]
        n37["KOR_bomber"]
        n38["KOR_cement_monarchic_rule"]
        n39["KOR_daelim_petrochemicals"]
        n40["KOR_defensive_preparation"]
        n41["KOR_equipment_effort_2"]
        n42["KOR_equipment_effort_3"]
        n43["KOR_establish_a_armor_corp"]
        n44["KOR_expand_jinsen_arsenal"]
        n45["KOR_fighter"]
        n46["KOR_invade_manchuria"]
        n47["KOR_militarism"]
        n48["KOR_modernize_mining_industry"]
        n49["KOR_motorization_effort"]
        n50["KOR_naval_bomber"]
        n51["KOR_youth_units"]
    end
    subgraph tier_5["Tier 5"]
        n52["KOR_devotion_to_the_emperor"]
        n53["KOR_field_hospitals"]
        n54["KOR_invade_soviet_union"]
        n55["KOR_mechanization_effort"]
        n56["KOR_military_industrial_cooperation"]
        n57["KOR_modernized_air_force"]
        n58["KOR_signal_companies"]
        n59["KOR_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n60["KOR_modern_logistics"]
    end
    n10 --> n14
    n11 --> n14
    n13 --> n15
    n12 --> n15
    n16 --> n23
    n10 --> n16
    n11 --> n16
    n8 --> n16
    n7 --> n16
    n31 --> n37
    n32 --> n38
    n27 --> n39
    n13 --> n17
    n10 --> n17
    n15 --> n40
    n28 --> n40
    n13 --> n18
    n12 --> n18
    n47 --> n52
    n13 --> n19
    n12 --> n19
    n16 --> n24
    n24 --> n41
    n24 --> n42
    n23 --> n43
    n16 --> n25
    n26 --> n44
    n27 --> n44
    n9 --> n10
    n5 --> n10
    n6 --> n10
    n49 --> n53
    n31 --> n45
    n21 --> n26
    n21 --> n27
    n10 --> n20
    n20 --> n28
    n15 --> n46
    n28 --> n46
    n30 --> n46
    n32 --> n46
    n47 --> n54
    n15 --> n29
    n19 --> n29
    n43 --> n55
    n49 --> n55
    n30 --> n47
    n32 --> n47
    n44 --> n56
    n48 --> n56
    n39 --> n56
    n53 --> n60
    n55 --> n60
    n58 --> n60
    n26 --> n48
    n45 --> n57
    n37 --> n57
    n50 --> n57
    n23 --> n49
    n14 --> n30
    n31 --> n50
    n5 --> n11
    n6 --> n11
    n22 --> n31
    n9 --> n12
    n5 --> n12
    n6 --> n12
    n9 --> n13
    n5 --> n13
    n6 --> n13
    n14 --> n32
    n12 --> n21
    n13 --> n21
    n15 --> n33
    n15 --> n34
    n21 --> n35
    n43 --> n58
    n49 --> n58
    n42 --> n59
    n41 --> n59
    n16 --> n36
    n10 --> n22
    n7 --> n22
    n8 --> n22
    n30 --> n51
    n28 --> n51
    n14 x--x n20
    n15 x--x n28
    n15 x--x n30
    n15 x--x n32
    n5 x--x n6
    n10 x--x n11
    n28 x--x n30
    n28 x--x n32
    n29 x--x n33
    n29 x--x n34
    n30 x--x n32
    n33 x--x n34
```

# KOR_hanjin_heavy_industries

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61(("KOR_hanjin_heavy_industries"))
        n62["KOR_peoples_fleet"]
    end
    subgraph tier_1["Tier 1"]
        n63["KOR_cruiser_focus"]
        n64["KOR_destroyer_focus"]
        n65{"KOR_national_admiralty"}
    end
    subgraph tier_2["Tier 2"]
        n66["KOR_a_s_warfare"]
        n67["KOR_carrier_strikes"]
        n68["KOR_increase_naval_production"]
        n69["KOR_naval_mine_warfare"]
        n70["KOR_the_blocade_doctrine"]
        n71["KOR_the_old_japanese_model"]
    end
    subgraph tier_3["Tier 3"]
        n72["KOR_battleship_focus"]
        n73["KOR_naval_air_groups"]
        n74["KOR_silent_service"]
    end
    subgraph tier_4["Tier 4"]
        n75["KOR_lessons_for_the_air_force"]
        n76["KOR_stealth_upgrades"]
        n77["KOR_the_biggest_battleship"]
    end
    n64 --> n66
    n63 --> n66
    n71 --> n72
    n65 --> n67
    n61 --> n63
    n62 --> n63
    n61 --> n64
    n62 --> n64
    n63 --> n68
    n64 --> n68
    n65 --> n68
    n73 --> n75
    n61 --> n65
    n62 --> n65
    n67 --> n73
    n63 --> n69
    n64 --> n69
    n70 --> n74
    n74 --> n76
    n72 --> n77
    n65 --> n70
    n65 --> n71
    n67 x--x n70
    n67 x--x n71
    n61 x--x n62
    n70 x--x n71
```

# KOR_peoples_committee_of_korea

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10["KOR_experience_of_the_korean_liberation_army"]
        n11["KOR_new_korean_army"]
        n78{"KOR_peoples_committee_of_korea"}
    end
    subgraph tier_1["Tier 1"]
        n7["KOR_conventional_warfare"]
        n79["KOR_encourage_collectivism"]
        n8["KOR_guerilla_experience"]
        n80["KOR_sideline_cho_man_sik"]
    end
    subgraph tier_2["Tier 2"]
        n16["KOR_army_reform"]
        n81["KOR_industrial_modernization_plan"]
        n82{"KOR_supreme_leader"}
        n22["KOR_take_over_air_bases"]
    end
    subgraph tier_3["Tier 3"]
        n83["KOR_adopt_maoism"]
        n23["KOR_army_modernization"]
        n84["KOR_complete_collectivization"]
        n24["KOR_equipment_effort"]
        n25["KOR_establish_a_military_academy"]
        n85["KOR_great_banner_of_songun"]
        n86["KOR_join_the_asian_communist_solidarity"]
        n87["KOR_loyalty_to_moscow"]
        n88["KOR_metallurgy"]
        n31["KOR_pyeongtaek_airplane_workshop"]
        n89["KOR_state_heavy_industry"]
        n36["KOR_supervize_equipment_production"]
        n90["KOR_war_industry"]
    end
    subgraph tier_4["Tier 4"]
        n37["KOR_bomber"]
        n41["KOR_equipment_effort_2"]
        n42["KOR_equipment_effort_3"]
        n43["KOR_establish_a_armor_corp"]
        n45["KOR_fighter"]
        n91["KOR_leader_technical_university"]
        n49["KOR_motorization_effort"]
        n50["KOR_naval_bomber"]
        n92["KOR_prosperity_propaganda"]
    end
    subgraph tier_5["Tier 5"]
        n53["KOR_field_hospitals"]
        n55["KOR_mechanization_effort"]
        n57["KOR_modernized_air_force"]
        n58["KOR_signal_companies"]
        n59["KOR_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n60["KOR_modern_logistics"]
    end
    n82 --> n83
    n16 --> n23
    n10 --> n16
    n11 --> n16
    n8 --> n16
    n7 --> n16
    n31 --> n37
    n81 --> n84
    n78 --> n7
    n78 --> n79
    n16 --> n24
    n24 --> n41
    n24 --> n42
    n23 --> n43
    n16 --> n25
    n49 --> n53
    n31 --> n45
    n82 --> n85
    n78 --> n8
    n79 --> n81
    n82 --> n86
    n88 --> n91
    n89 --> n91
    n82 --> n87
    n43 --> n55
    n49 --> n55
    n81 --> n88
    n53 --> n60
    n55 --> n60
    n58 --> n60
    n45 --> n57
    n37 --> n57
    n50 --> n57
    n23 --> n49
    n31 --> n50
    n84 --> n92
    n22 --> n31
    n78 --> n80
    n43 --> n58
    n49 --> n58
    n42 --> n59
    n41 --> n59
    n81 --> n89
    n16 --> n36
    n80 --> n82
    n10 --> n22
    n7 --> n22
    n8 --> n22
    n81 --> n90
    n83 x--x n86
    n83 x--x n87
    n7 x--x n8
    n86 x--x n87
```

# KOR_peoples_fleet

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61["KOR_hanjin_heavy_industries"]
        n62(("KOR_peoples_fleet"))
    end
    subgraph tier_1["Tier 1"]
        n63["KOR_cruiser_focus"]
        n64["KOR_destroyer_focus"]
        n65{"KOR_national_admiralty"}
    end
    subgraph tier_2["Tier 2"]
        n66["KOR_a_s_warfare"]
        n67["KOR_carrier_strikes"]
        n68["KOR_increase_naval_production"]
        n69["KOR_naval_mine_warfare"]
        n70["KOR_the_blocade_doctrine"]
        n71["KOR_the_old_japanese_model"]
    end
    subgraph tier_3["Tier 3"]
        n72["KOR_battleship_focus"]
        n73["KOR_naval_air_groups"]
        n74["KOR_silent_service"]
    end
    subgraph tier_4["Tier 4"]
        n75["KOR_lessons_for_the_air_force"]
        n76["KOR_stealth_upgrades"]
        n77["KOR_the_biggest_battleship"]
    end
    n64 --> n66
    n63 --> n66
    n71 --> n72
    n65 --> n67
    n61 --> n63
    n62 --> n63
    n61 --> n64
    n62 --> n64
    n63 --> n68
    n64 --> n68
    n65 --> n68
    n73 --> n75
    n61 --> n65
    n62 --> n65
    n67 --> n73
    n63 --> n69
    n64 --> n69
    n70 --> n74
    n74 --> n76
    n72 --> n77
    n65 --> n70
    n65 --> n71
    n67 x--x n70
    n67 x--x n71
    n61 x--x n62
    n70 x--x n71
```

# KOR_return_of_the_government_in_exile

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n5{"KOR_collaboration_with_japan"}
        n6{"KOR_collaboration_with_overlord"}
        n7["KOR_conventional_warfare"]
        n8["KOR_guerilla_experience"]
        n11{"KOR_new_korean_army"}
        n9{"KOR_return_of_the_government_in_exile"}
    end
    subgraph tier_1["Tier 1"]
        n10{"KOR_experience_of_the_korean_liberation_army"}
        n12{"KOR_reorganize_the_administration"}
        n13{"KOR_repeal_colonial_restrictions"}
    end
    subgraph tier_2["Tier 2"]
        n14{"KOR_amnesty_for_ex_japanese_army_officers"}
        n15{"KOR_apply_democratic_program"}
        n16["KOR_army_reform"]
        n17["KOR_defense_mobilization"]
        n18["KOR_develop_gold_mining_near_unsan"]
        n19{"KOR_embrace_peoples_tutelage"}
        n20{"KOR_integrate_socialist_aligned_guerillas"}
        n21["KOR_rise_of_the_chaebols"]
        n22["KOR_take_over_air_bases"]
    end
    subgraph tier_3["Tier 3"]
        n23["KOR_army_modernization"]
        n24["KOR_equipment_effort"]
        n25["KOR_establish_a_military_academy"]
        n26["KOR_hyundai_engineering"]
        n27["KOR_hyundai_vehicles"]
        n28["KOR_internationalism_focus"]
        n29["KOR_keep_ties_with_the_KMT"]
        n30["KOR_nationalism_focus"]
        n31["KOR_pyeongtaek_airplane_workshop"]
        n32["KOR_restore_imperial_power"]
        n33["KOR_search_allies"]
        n34["KOR_semi_isolation"]
        n35["KOR_seoul_busan_infrastructure"]
        n36["KOR_supervize_equipment_production"]
    end
    subgraph tier_4["Tier 4"]
        n37["KOR_bomber"]
        n38["KOR_cement_monarchic_rule"]
        n39["KOR_daelim_petrochemicals"]
        n40["KOR_defensive_preparation"]
        n41["KOR_equipment_effort_2"]
        n42["KOR_equipment_effort_3"]
        n43["KOR_establish_a_armor_corp"]
        n44["KOR_expand_jinsen_arsenal"]
        n45["KOR_fighter"]
        n46["KOR_invade_manchuria"]
        n47["KOR_militarism"]
        n48["KOR_modernize_mining_industry"]
        n49["KOR_motorization_effort"]
        n50["KOR_naval_bomber"]
        n51["KOR_youth_units"]
    end
    subgraph tier_5["Tier 5"]
        n52["KOR_devotion_to_the_emperor"]
        n53["KOR_field_hospitals"]
        n54["KOR_invade_soviet_union"]
        n55["KOR_mechanization_effort"]
        n56["KOR_military_industrial_cooperation"]
        n57["KOR_modernized_air_force"]
        n58["KOR_signal_companies"]
        n59["KOR_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n60["KOR_modern_logistics"]
    end
    n10 --> n14
    n11 --> n14
    n13 --> n15
    n12 --> n15
    n16 --> n23
    n10 --> n16
    n11 --> n16
    n8 --> n16
    n7 --> n16
    n31 --> n37
    n32 --> n38
    n27 --> n39
    n13 --> n17
    n10 --> n17
    n15 --> n40
    n28 --> n40
    n13 --> n18
    n12 --> n18
    n47 --> n52
    n13 --> n19
    n12 --> n19
    n16 --> n24
    n24 --> n41
    n24 --> n42
    n23 --> n43
    n16 --> n25
    n26 --> n44
    n27 --> n44
    n9 --> n10
    n5 --> n10
    n6 --> n10
    n49 --> n53
    n31 --> n45
    n21 --> n26
    n21 --> n27
    n10 --> n20
    n20 --> n28
    n15 --> n46
    n28 --> n46
    n30 --> n46
    n32 --> n46
    n47 --> n54
    n15 --> n29
    n19 --> n29
    n43 --> n55
    n49 --> n55
    n30 --> n47
    n32 --> n47
    n44 --> n56
    n48 --> n56
    n39 --> n56
    n53 --> n60
    n55 --> n60
    n58 --> n60
    n26 --> n48
    n45 --> n57
    n37 --> n57
    n50 --> n57
    n23 --> n49
    n14 --> n30
    n31 --> n50
    n22 --> n31
    n9 --> n12
    n5 --> n12
    n6 --> n12
    n9 --> n13
    n5 --> n13
    n6 --> n13
    n14 --> n32
    n12 --> n21
    n13 --> n21
    n15 --> n33
    n15 --> n34
    n21 --> n35
    n43 --> n58
    n49 --> n58
    n42 --> n59
    n41 --> n59
    n16 --> n36
    n10 --> n22
    n7 --> n22
    n8 --> n22
    n30 --> n51
    n28 --> n51
    n14 x--x n20
    n15 x--x n28
    n15 x--x n30
    n15 x--x n32
    n10 x--x n11
    n28 x--x n30
    n28 x--x n32
    n29 x--x n33
    n29 x--x n34
    n30 x--x n32
    n33 x--x n34
```
