# TIB_aquire_modern_machinery

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("TIB_aquire_modern_machinery"))
        n2["TIB_masters_of_the_mountain"]
        n3["TIB_modern_army_structure"]
    end
    subgraph tier_1["Tier 1"]
        n4["TIB_develop_the_drapchi_lekhung"]
        n5["TIB_drabshi_lekhoung_power_plant"]
        n6["TIB_expand_the_drapchi_arsenal"]
    end
    subgraph tier_2["Tier 2"]
        n7["TIB_equipment_effort"]
        n8["TIB_new_production_chains"]
        n9["TIB_rekindle_the_land_suvery_of_1922"]
        n10["TIB_rural_infrastructure_development"]
        n11["TIB_utilize_the_cattle_industry"]
    end
    subgraph tier_3["Tier 3"]
        n12["TIB_exploit_the_gunkar_copper"]
        n13["TIB_extract_gold_from_the_riverbeds"]
        n14{"TIB_naval_effort"}
        n15["TIB_optimize_production"]
        n16["TIB_our_own_artillery"]
    end
    subgraph tier_4["Tier 4"]
        n17["TIB_flexible_navy"]
        n18["TIB_large_navy"]
        n19["TIB_mountain_artillery_training"]
    end
    subgraph tier_5["Tier 5"]
        n20["TIB_cruiser_effort"]
        n21["TIB_submarine_effort"]
    end
    subgraph tier_6["Tier 6"]
        n22["TIB_capital_ships_effort"]
        n23["TIB_destroyer_effort"]
    end
    n20 --> n22
    n18 --> n20
    n17 --> n20
    n21 --> n23
    n1 --> n4
    n1 --> n5
    n6 --> n7
    n1 --> n6
    n9 --> n12
    n9 --> n13
    n14 --> n17
    n14 --> n18
    n16 --> n19
    n2 --> n19
    n8 --> n14
    n7 --> n14
    n4 --> n8
    n6 --> n8
    n8 --> n15
    n11 --> n15
    n7 --> n16
    n3 --> n16
    n5 --> n9
    n5 --> n10
    n17 --> n21
    n18 --> n21
    n5 --> n11
    n4 --> n11
    n17 x--x n18
```

# TIB_army_review

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n24(("TIB_army_review"))
        n7["TIB_equipment_effort"]
    end
    subgraph tier_1["Tier 1"]
        n25["TIB_officers_professionalism"]
        n26["TIB_train_monks_and_clerks_as_officers"]
    end
    subgraph tier_2["Tier 2"]
        n27["TIB_improve_military_tactics"]
        n3["TIB_modern_army_structure"]
    end
    subgraph tier_3["Tier 3"]
        n28{"TIB_build_air_strip"}
        n29["TIB_expand_our_logistic_capabilities"]
        n2["TIB_masters_of_the_mountain"]
        n16["TIB_our_own_artillery"]
    end
    subgraph tier_4["Tier 4"]
        n30["TIB_large_airframes"]
        n19["TIB_mountain_artillery_training"]
        n31["TIB_small_airframes"]
    end
    subgraph tier_5["Tier 5"]
        n32["TIB_invest_into_the_air_force"]
    end
    n27 --> n28
    n27 --> n29
    n25 --> n27
    n31 --> n32
    n30 --> n32
    n28 --> n30
    n3 --> n2
    n27 --> n2
    n25 --> n3
    n16 --> n19
    n2 --> n19
    n24 --> n25
    n7 --> n16
    n3 --> n16
    n28 --> n31
    n24 --> n26
    n30 x--x n31
```

# TIB_convene_the_tsongdu

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n33["TIB_complete_diplomatic_isolation"]
        n34{"TIB_convene_the_tsongdu"}
        n35["TIB_persuade_the_regent"]
        n36{"TIB_request_british_military_aid"}
    end
    subgraph tier_1["Tier 1"]
        n37["TIB_appoint_thutob_regent"]
        n38{"TIB_disband_the_tsongdu"}
        n39["TIB_search_the_dalai_lama"]
    end
    subgraph tier_2["Tier 2"]
        n40["TIB_centralize_power"]
        n41["TIB_free_the_sage"]
        n42["TIB_legacy_of_long_march"]
        n43{"TIB_prevent_an_officers_coup"}
    end
    subgraph tier_3["Tier 3"]
        n44["TIB_contact_the_cpc"]
        n45["TIB_organize_workers_strikes"]
        n46["TIB_return_to_old_ways"]
        n47["TIB_support_the_allies"]
        n48{"TIB_sway_the_aristocrats"}
    end
    subgraph tier_4["Tier 4"]
        n49["TIB_alone_against_the_storm"]
        n50["TIB_approach_the_revolutionaries"]
        n51["TIB_establish_the_tibetan_mirror"]
        n52["TIB_open_the_chamdo_road"]
        n53["TIB_the_qinghai_expedition"]
    end
    subgraph tier_5["Tier 5"]
        n54["TIB_alienate_kunphela"]
        n55["TIB_aquire_british_guns"]
        n56["TIB_attain_american_advisors"]
        n57{"TIB_expand_the_tdyl"}
        n58{"TIB_found_the_secret_police"}
        n59["TIB_infiltrate_the_military"]
        n60["TIB_land_redistribution"]
        n61["TIB_undermine_the_kashag"]
    end
    subgraph tier_6["Tier 6"]
        n62["TIB_education_for_the_masses"]
        n63["TIB_follow_maos_lead"]
        n64["TIB_invite_kuomintang_generals"]
        n65["TIB_invite_soviet_advisors"]
        n66["TIB_nationalize_the_industry"]
        n67["TIB_revenge_for_the_sage"]
        n68["TIB_topple_the_feudal_regime"]
    end
    subgraph tier_7["Tier 7"]
        n69{"TIB_cult_of_personality"}
        n70["TIB_disempower_the_monasteries"]
        n71["TIB_five_year_plan"]
        n72["TIB_form_the_khamba_traders_association"]
        n73["TIB_grant_monastic_priviliges"]
        n74["TIB_introduce_political_reforms"]
        n75["TIB_open_the_sikkim_trade_office"]
        n76{"TIB_the_tibetan_cultural_revolution"}
    end
    subgraph tier_8["Tier 8"]
        n77["TIB_foreign_economic_aid"]
        n78{"TIB_implement_the_three_principles"}
        n79["TIB_integrate_the_hinterland"]
        n80["TIB_invite_western_advisors"]
        n81["TIB_join_the_chinese"]
        n82["TIB_join_the_comintern"]
        n83["TIB_secularize_the_nation"]
        n84{"TIB_the_british_model"}
    end
    subgraph tier_9["Tier 9"]
        n85["TIB_a_strong_and_united_tibet"]
        n86["TIB_cooperate_with_the_pla"]
        n87["TIB_enforce_state_atheism"]
        n88["TIB_join_allies"]
        n89["TIB_pressure_the_south"]
        n90["TIB_the_gyegu_expedition"]
        n91["TIB_the_tale_of_two_brothers"]
        n92["TIB_utilize_political_commisars"]
    end
    subgraph tier_10["Tier 10"]
        n93["TIB_across_the_himalayas"]
        n94["TIB_anti_imperialist_propaganda"]
        n95["TIB_behead_the_red_sun_in_the_east"]
        n96["TIB_full_social_mobilization"]
        n97["TIB_invite_foreign_advisors"]
        n98["TIB_liberate_amdo"]
        n99["TIB_proclaim_greater_tibet"]
        n100["TIB_reopen_british_school"]
        n101["TIB_unite_the_himalayas"]
    end
    subgraph tier_11["Tier 11"]
        n102["TIB_beacon_of_the_plateau"]
        n103["TIB_crush_the_warlords"]
        n104["TIB_extinguish_the_rising_sun"]
    end
    n78 --> n85
    n84 --> n85
    n86 --> n93
    n91 --> n93
    n49 --> n54
    n50 --> n54
    n48 --> n49
    n91 --> n94
    n86 --> n94
    n34 --> n37
    n48 --> n50
    n50 --> n55
    n52 --> n56
    n51 --> n56
    n97 --> n102
    n100 --> n102
    n92 --> n95
    n37 --> n40
    n42 --> n44
    n81 --> n86
    n101 --> n103
    n97 --> n103
    n63 --> n69
    n65 --> n69
    n34 --> n38
    n68 --> n70
    n57 --> n62
    n82 --> n87
    n47 --> n51
    n53 --> n57
    n94 --> n104
    n101 --> n104
    n65 --> n71
    n60 --> n71
    n58 --> n63
    n57 --> n63
    n75 --> n77
    n68 --> n72
    n53 --> n58
    n38 --> n41
    n86 --> n96
    n67 --> n73
    n72 --> n78
    n70 --> n78
    n50 --> n59
    n73 --> n79
    n67 --> n74
    n88 --> n97
    n59 --> n64
    n58 --> n65
    n75 --> n80
    n84 --> n88
    n69 --> n81
    n76 --> n81
    n69 --> n82
    n53 --> n60
    n38 --> n42
    n89 --> n98
    n90 --> n98
    n60 --> n66
    n47 --> n52
    n67 --> n75
    n68 --> n75
    n42 --> n45
    n82 --> n89
    n81 --> n89
    n37 --> n43
    n92 --> n99
    n88 --> n100
    n40 --> n46
    n43 --> n46
    n54 --> n67
    n61 --> n67
    n34 --> n39
    n35 --> n39
    n70 --> n83
    n36 --> n47
    n43 --> n47
    n41 --> n48
    n74 --> n84
    n73 --> n84
    n82 --> n90
    n81 --> n90
    n45 --> n53
    n44 --> n53
    n78 --> n91
    n62 --> n76
    n63 --> n76
    n55 --> n68
    n59 --> n68
    n49 --> n61
    n85 --> n101
    n82 --> n92
    n85 x--x n88
    n85 x--x n91
    n49 x--x n50
    n37 x--x n38
    n33 x--x n47
    n34 x--x n35
    n63 x--x n65
    n41 x--x n42
    n81 x--x n82
```

# TIB_persuade_the_regent

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n34["TIB_convene_the_tsongdu"]
        n35(("TIB_persuade_the_regent"))
        n43{"TIB_prevent_an_officers_coup"}
    end
    subgraph tier_1["Tier 1"]
        n105["TIB_reinforce_the_kashag"]
        n39["TIB_search_the_dalai_lama"]
        n106["TIB_utilize_the_dob_dobs"]
    end
    subgraph tier_2["Tier 2"]
        n107{"TIB_reintroduce_monastic_tax"}
        n36{"TIB_request_british_military_aid"}
    end
    subgraph tier_3["Tier 3"]
        n33["TIB_complete_diplomatic_isolation"]
        n108["TIB_denounce_regents_corruption"]
        n47["TIB_support_the_allies"]
    end
    subgraph tier_4["Tier 4"]
        n109["TIB_enhance_the_education_system"]
        n51["TIB_establish_the_tibetan_mirror"]
        n110["TIB_guard_the_borders"]
        n52["TIB_open_the_chamdo_road"]
        n111["TIB_promote_traditional_values"]
    end
    subgraph tier_5["Tier 5"]
        n56["TIB_attain_american_advisors"]
    end
    n52 --> n56
    n51 --> n56
    n36 --> n33
    n107 --> n33
    n107 --> n108
    n108 --> n109
    n47 --> n51
    n33 --> n110
    n47 --> n52
    n108 --> n111
    n33 --> n111
    n35 --> n105
    n105 --> n107
    n106 --> n107
    n105 --> n36
    n34 --> n39
    n35 --> n39
    n36 --> n47
    n43 --> n47
    n35 --> n106
    n33 x--x n47
    n34 x--x n35
```
