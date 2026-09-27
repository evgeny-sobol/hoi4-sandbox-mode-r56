# INS_industrial_centralisation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("INS_industrial_centralisation"))
    end
    subgraph tier_1["Tier 1"]
        n2["INS_colonial_infrastructure"]
        n3["INS_continue_the_modernisation"]
        n4["INS_restore_the_arms_factories"]
    end
    subgraph tier_2["Tier 2"]
        n5["INS_civilian_works"]
        n6["INS_connect_the_islands"]
        n7["INS_earthworks"]
    end
    subgraph tier_3["Tier 3"]
        n8["INS_phillips_radio"]
        n9["INS_the_royal_batavian_society"]
    end
    subgraph tier_4["Tier 4"]
        n10["INS_economic_independence"]
        n11["INS_royal_scientific_cooperation"]
    end
    subgraph tier_5["Tier 5"]
        n12["INS_invite_foreign_investors"]
        n13["INS_scientific_exceptionalism"]
    end
    subgraph tier_6["Tier 6"]
        n14["INS_koninklijk_paketvaart_maatschappij"]
    end
    n3 --> n5
    n1 --> n2
    n2 --> n6
    n1 --> n3
    n4 --> n7
    n8 --> n10
    n9 --> n10
    n10 --> n12
    n12 --> n14
    n13 --> n14
    n5 --> n8
    n6 --> n8
    n1 --> n4
    n8 --> n11
    n10 --> n13
    n7 --> n9
    n6 --> n9
```

# INS_kebangkitan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15["INS_concessions_to_the_nationalists"]
        n16["INS_jewel_of_the_pacific"]
        n17{"INS_kebangkitan"}
        n18{"INS_stay_with_the_netherlands"}
    end
    subgraph tier_1["Tier 1"]
        n19{"INS_PKI"}
        n20{"INS_PNI"}
        n21["INS_empower_the_volksraad"]
    end
    subgraph tier_2["Tier 2"]
        n22["INS_favour_the_radicals"]
        n23["INS_gapi_focus"]
        n24["INS_gather_the_opposition"]
        n25["INS_promote_national_independence"]
        n26["INS_reinvigorate_the_pfi"]
        n27["INS_reorganize_the_underground"]
        n28["INS_reunify_pppki"]
        n29["INS_the_new_party_leadership"]
        n30["INS_westernisation"]
    end
    subgraph tier_3["Tier 3"]
        n31["INS_consolidate_the_right"]
        n32{"INS_defensive_politics"}
        n33{"INS_demand_volksraad_elections"}
        n34{"INS_launch_the_revolution"}
        n35["INS_suara_rakyat"]
        n36{"INS_the_coup"}
    end
    subgraph tier_4["Tier 4"]
        n37["INS_establish_true_equality"]
        n38["INS_implement_the_sharia"]
        n39["INS_issue_emergency_powers"]
        n40{"INS_limited_autonomy"}
        n41["INS_nationalize_the_factories"]
        n42["INS_our_own_path"]
        n43["INS_reinforce_the_national_identity"]
        n44["INS_the_agreement"]
    end
    subgraph tier_5["Tier 5"]
        n45["INS_asian_superiority"]
        n46["INS_death_to_colonialism"]
        n47["INS_equal_under_god"]
        n48["INS_hari_kemerdekaan"]
        n49["INS_implement_a_democratic_system"]
        n50["INS_join_allies"]
        n51["INS_join_the_comintern"]
        n52["INS_liberate_the_northern_muslims"]
        n53["INS_maphilindo"]
    end
    subgraph tier_6["Tier 6"]
        n54["INS_claim_guinea"]
        n55["INS_claim_timor"]
        n56["INS_konfrontasi"]
        n57["INS_liberate_the_philippines"]
        n58{"INS_unity_in_diversity_r56"}
    end
    subgraph tier_7["Tier 7"]
        n59["INS_peacetime_economics"]
        n60["INS_strike_japan"]
    end
    n17 --> n19
    n17 --> n20
    n42 --> n45
    n48 --> n54
    n48 --> n55
    n22 --> n31
    n38 --> n46
    n41 --> n46
    n30 --> n32
    n15 --> n32
    n24 --> n33
    n25 --> n33
    n17 --> n21
    n18 --> n21
    n38 --> n47
    n34 --> n37
    n20 --> n22
    n21 --> n23
    n16 --> n23
    n21 --> n24
    n42 --> n48
    n44 --> n48
    n37 --> n49
    n33 --> n38
    n32 --> n39
    n40 --> n50
    n37 --> n51
    n43 --> n51
    n48 --> n56
    n27 --> n34
    n29 --> n34
    n38 --> n52
    n48 --> n57
    n32 --> n40
    n33 --> n40
    n40 --> n53
    n33 --> n41
    n36 --> n42
    n58 --> n59
    n21 --> n25
    n34 --> n43
    n20 --> n26
    n19 --> n27
    n19 --> n28
    n20 --> n28
    n58 --> n60
    n27 --> n35
    n36 --> n44
    n34 --> n44
    n26 --> n36
    n22 --> n36
    n19 --> n29
    n50 --> n58
    n53 --> n58
    n16 --> n30
    n21 --> n30
    n19 x--x n20
    n19 x--x n21
    n20 x--x n21
    n21 x--x n16
    n22 x--x n26
    n38 x--x n40
    n50 x--x n53
    n17 x--x n18
    n42 x--x n44
    n59 x--x n60
    n27 x--x n29
```

# INS_koninklijk_nederlands_indisch_leger

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61(("INS_koninklijk_nederlands_indisch_leger"))
        n62["INS_raaf_assistance"]
    end
    subgraph tier_1["Tier 1"]
        n63["INS_form_the_home_guard"]
        n64["INS_modernize_the_military"]
    end
    subgraph tier_2["Tier 2"]
        n65["INS_ambonese_auxilaries"]
        n66["INS_braat_overvalwagen"]
        n67["INS_interventionism"]
    end
    subgraph tier_3["Tier 3"]
        n68["INS_city_fortifications"]
        n69["INS_expand_the_officers_corps"]
    end
    subgraph tier_4["Tier 4"]
        n70{"INS_non_discriminatory_conscription"}
    end
    subgraph tier_5["Tier 5"]
        n71["INS_guerilla_tactics"]
        n72["INS_preemptive_defense"]
    end
    subgraph tier_6["Tier 6"]
        n73["INS_reform_the_knil"]
    end
    n64 --> n65
    n63 --> n65
    n64 --> n66
    n65 --> n68
    n65 --> n69
    n61 --> n63
    n70 --> n71
    n63 --> n67
    n62 --> n67
    n61 --> n64
    n68 --> n70
    n69 --> n70
    n70 --> n72
    n71 --> n73
    n72 --> n73
    n71 x--x n72
```

# INS_naval_autonomy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n74["INS_knil_integration"]
        n75(("INS_naval_autonomy"))
    end
    subgraph tier_1["Tier 1"]
        n76["INS_coastal_entrenchment"]
        n77["INS_java_shipyards"]
    end
    subgraph tier_2["Tier 2"]
        n78["INS_increase_convoy_production"]
        n79["INS_naval_warfare"]
    end
    subgraph tier_3["Tier 3"]
        n80["INS_KNIL_marines"]
        n81["INS_british_ship_designs"]
    end
    subgraph tier_4["Tier 4"]
        n82["INS_air_by_sea"]
        n83{"INS_joint_wargames"}
    end
    subgraph tier_5["Tier 5"]
        n84["INS_convoy_protection"]
        n85["INS_ship_a_day_tactics"]
    end
    n79 --> n80
    n74 --> n82
    n81 --> n82
    n79 --> n81
    n75 --> n76
    n83 --> n84
    n77 --> n78
    n75 --> n77
    n80 --> n83
    n81 --> n83
    n77 --> n79
    n76 --> n79
    n83 --> n85
    n84 x--x n85
```

# INS_stay_with_the_netherlands

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19["INS_PKI"]
        n20["INS_PNI"]
        n17{"INS_kebangkitan"}
        n18{"INS_stay_with_the_netherlands"}
    end
    subgraph tier_1["Tier 1"]
        n21["INS_empower_the_volksraad"]
        n16["INS_jewel_of_the_pacific"]
    end
    subgraph tier_2["Tier 2"]
        n15["INS_concessions_to_the_nationalists"]
        n23["INS_gapi_focus"]
        n24["INS_gather_the_opposition"]
        n25["INS_promote_national_independence"]
        n30["INS_westernisation"]
    end
    subgraph tier_3["Tier 3"]
        n32{"INS_defensive_politics"}
        n33{"INS_demand_volksraad_elections"}
    end
    subgraph tier_4["Tier 4"]
        n38["INS_implement_the_sharia"]
        n39["INS_issue_emergency_powers"]
        n40{"INS_limited_autonomy"}
        n41["INS_nationalize_the_factories"]
    end
    subgraph tier_5["Tier 5"]
        n46["INS_death_to_colonialism"]
        n47["INS_equal_under_god"]
        n50["INS_join_allies"]
        n52["INS_liberate_the_northern_muslims"]
        n53["INS_maphilindo"]
    end
    subgraph tier_6["Tier 6"]
        n58{"INS_unity_in_diversity_r56"}
    end
    subgraph tier_7["Tier 7"]
        n59["INS_peacetime_economics"]
        n60["INS_strike_japan"]
    end
    n16 --> n15
    n38 --> n46
    n41 --> n46
    n30 --> n32
    n15 --> n32
    n24 --> n33
    n25 --> n33
    n17 --> n21
    n18 --> n21
    n38 --> n47
    n21 --> n23
    n16 --> n23
    n21 --> n24
    n33 --> n38
    n32 --> n39
    n18 --> n16
    n40 --> n50
    n38 --> n52
    n32 --> n40
    n33 --> n40
    n40 --> n53
    n33 --> n41
    n58 --> n59
    n21 --> n25
    n58 --> n60
    n50 --> n58
    n53 --> n58
    n16 --> n30
    n21 --> n30
    n19 x--x n21
    n20 x--x n21
    n21 x--x n16
    n38 x--x n40
    n50 x--x n53
    n17 x--x n18
    n59 x--x n60
```

# INS_the_test_flight_service

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n81["INS_british_ship_designs"]
        n63["INS_form_the_home_guard"]
        n86(("INS_the_test_flight_service"))
    end
    subgraph tier_1["Tier 1"]
        n62["INS_raaf_assistance"]
    end
    subgraph tier_2["Tier 2"]
        n87["INS_indonesian_fighter_schools"]
        n67["INS_interventionism"]
        n74["INS_knil_integration"]
    end
    subgraph tier_3["Tier 3"]
        n82["INS_air_by_sea"]
        n88["INS_the_flying_dutchmen"]
    end
    n74 --> n82
    n81 --> n82
    n62 --> n87
    n63 --> n67
    n62 --> n67
    n62 --> n74
    n86 --> n62
    n74 --> n88
```
