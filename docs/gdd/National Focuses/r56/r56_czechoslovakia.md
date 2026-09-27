# CZE_R56_devalue_the_koruna

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CZE_R56_devalue_the_koruna"))
        n2["CZE_armament_program"]
        n3["CZE_czechoslovak_firearms"]
        n4["CZE_revitalising_the_danube_flotilla"]
        n5["CZE_the_central_role_of_artillery_citadels"]
    end
    subgraph tier_1["Tier 1"]
        n6["CZE_R56_ramp_up_cement_production"]
        n7["CZE_R56_support_consumer_goods_industry"]
        n8["CZE_R56_support_strategic_industries"]
        n9["CZE_poldi_steelworks"]
    end
    subgraph tier_2["Tier 2"]
        n10["CZE_R56_allocate_funds_to_rop"]
        n11["CZE_R56_complete_the_dubnica_nad_vahom_munition_factory"]
        n12["CZE_R56_eastern_urbanization_project"]
        n13["CZE_R56_expand_heavy_industry"]
        n14["CZE_R56_fund_praga_plants"]
        n15["CZE_R56_improve_highway_connections"]
    end
    subgraph tier_3["Tier 3"]
        n16["CZE_R56_direct_praha_bratislava_railway_connection"]
        n17["CZE_R56_expand_the_praha_ruzyne_airport"]
        n18["CZE_R56_firearms_deliveries"]
        n19["CZE_R56_prospect_for_new_resources"]
        n20["CZE_new_tanks"]
    end
    subgraph tier_4["Tier 4"]
        n21["CZE_R56_chemical_industry_development"]
        n22["CZE_R56_order_military_trucks"]
        n23["CZE_R56_produce_the_slovenska_strela_railcars"]
        n24["CZE_R56_secure_armament_contracts"]
        n25["CZE_artillery_focus"]
        n26["CZE_holek_brothers"]
    end
    subgraph tier_5["Tier 5"]
        n27["CZE_R56_czech_technical_university"]
        n28["CZE_R56_expand_the_commercial_tyre_production"]
        n29["CZE_armoured_cars"]
        n30["CZE_explosives_production"]
    end
    subgraph tier_6["Tier 6"]
        n31["CZE_R56_establish_new_uranium_mines"]
        n32["CZE_R56_rocket_research"]
        n33["CZE_mechanized_units"]
        n34["CZE_new_tank_design"]
    end
    subgraph tier_7["Tier 7"]
        n35["CZE_R56_nuclear_physics_institute"]
    end
    n6 --> n10
    n19 --> n21
    n8 --> n11
    n2 --> n11
    n21 --> n27
    n15 --> n16
    n7 --> n12
    n27 --> n31
    n7 --> n13
    n21 --> n28
    n23 --> n28
    n15 --> n17
    n3 --> n18
    n11 --> n18
    n8 --> n14
    n6 --> n15
    n31 --> n35
    n20 --> n22
    n16 --> n23
    n12 --> n19
    n13 --> n19
    n1 --> n6
    n27 --> n32
    n18 --> n24
    n1 --> n7
    n1 --> n8
    n20 --> n29
    n26 --> n29
    n18 --> n25
    n3 --> n25
    n25 --> n30
    n5 --> n30
    n11 --> n26
    n18 --> n26
    n29 --> n33
    n22 --> n34
    n27 --> n34
    n14 --> n20
    n4 --> n9
    n1 --> n9
```

# CZE_czechoslovak_government_reform

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36["CZE_acquire_access_for_soviets"]
        n37["CZE_claims_bohemian_crown"]
        n38{"CZE_czechoslovak_government_reform"}
        n39["CZE_france_alliance"]
    end
    subgraph tier_1["Tier 1"]
        n40{"CZE_empower_internationalism"}
        n41["CZE_extend_military_service"]
        n42{"CZE_sokol_movement"}
    end
    subgraph tier_2["Tier 2"]
        n43["CZE_2nd_departnment"]
        n44{"CZE_boycott_press_law"}
        n45["CZE_democratic_reforms"]
        n46{"CZE_state_defense_law"}
    end
    subgraph tier_3["Tier 3"]
        n47["CZE_collectivize_key_industries"]
        n48{"CZE_czech_fascism_onrise"}
        n49["CZE_handle_the_communist_power_grab"]
        n50{"CZE_intelligence_service_defense"}
        n51{"CZE_national_unity_government"}
        n52{"CZE_state_defense_guard"}
        n53["CZE_strengthen_communism"]
        n54["CZE_sudetenland_autonomy"]
    end
    subgraph tier_4["Tier 4"]
        n55{"CZE_ban_communism"}
        n56["CZE_collectivize_farms"]
        n57["CZE_five_year_plan"]
        n58["CZE_intelligence_service_offense"]
        n59["CZE_levy_liechtenstein_properties"]
        n60{"CZE_partial_mobilization"}
        n61["CZE_peoples_revolution"]
        n62{"CZE_petition_league_of_nations"}
        n63["CZE_soviet_intelligence"]
    end
    subgraph tier_5["Tier 5"]
        n64["CZE_currency_reform"]
        n65["CZE_infiltrate_abwehr"]
        n66["CZE_join_allies"]
        n67{"CZE_military_coup"}
        n68["CZE_nazi_puppet"]
        n69["CZE_suppress_the_church"]
        n70["CZE_uranium_for_soviets"]
    end
    subgraph tier_6["Tier 6"]
        n71["CZE_join_axis"]
        n72["CZE_join_commitern"]
        n73["CZE_support_oster"]
        n74["CZE_zaolzie_for_alliance"]
    end
    subgraph tier_7["Tier 7"]
        n75["CZE_expand_soviet_ties"]
        n76["CZE_faction_research_exchange"]
        n77["CZE_together_against_berlin"]
    end
    subgraph tier_8["Tier 8"]
        n78["CZE_split_poland"]
    end
    subgraph tier_9["Tier 9"]
        n79["CZE_union_with_warsaw"]
    end
    n39 --> n43
    n41 --> n43
    n48 --> n55
    n40 --> n44
    n53 --> n56
    n44 --> n47
    n57 --> n64
    n46 --> n48
    n40 --> n45
    n42 --> n45
    n38 --> n40
    n72 --> n75
    n38 --> n41
    n66 --> n76
    n71 --> n76
    n72 --> n76
    n68 --> n76
    n37 --> n76
    n53 --> n57
    n44 --> n49
    n58 --> n65
    n43 --> n50
    n50 --> n58
    n62 --> n66
    n55 --> n71
    n67 --> n71
    n61 --> n72
    n70 --> n72
    n51 --> n59
    n54 --> n59
    n60 --> n67
    n48 --> n67
    n46 --> n51
    n45 --> n51
    n51 --> n68
    n55 --> n68
    n62 --> n68
    n52 --> n60
    n50 --> n60
    n53 --> n61
    n54 --> n62
    n38 --> n42
    n50 --> n63
    n75 --> n78
    n46 --> n52
    n41 --> n52
    n42 --> n46
    n44 --> n53
    n45 --> n54
    n65 --> n73
    n56 --> n69
    n74 --> n77
    n78 --> n79
    n63 --> n70
    n36 --> n70
    n67 --> n74
    n55 --> n74
    n55 x--x n67
    n44 x--x n45
    n48 x--x n60
    n45 x--x n46
    n40 x--x n42
    n49 x--x n53
    n71 x--x n68
    n71 x--x n74
    n67 x--x n63
```

# CZE_france_alliance

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36["CZE_acquire_access_for_soviets"]
        n55{"CZE_ban_communism"}
        n48{"CZE_czech_fascism_onrise"}
        n41["CZE_extend_military_service"]
        n39(("CZE_france_alliance"))
        n66["CZE_join_allies"]
        n68["CZE_nazi_puppet"]
        n61["CZE_peoples_revolution"]
        n80["CZE_soviet_treaties"]
        n52{"CZE_state_defense_guard"}
    end
    subgraph tier_1["Tier 1"]
        n43["CZE_2nd_departnment"]
        n81{"CZE_french_military_mission"}
    end
    subgraph tier_2["Tier 2"]
        n50{"CZE_intelligence_service_defense"}
        n82["CZE_revive_little_entente"]
    end
    subgraph tier_3["Tier 3"]
        n58["CZE_intelligence_service_offense"]
        n83{"CZE_invite_romania"}
        n84{"CZE_invite_yugoslavia"}
        n60{"CZE_partial_mobilization"}
        n63["CZE_soviet_intelligence"]
    end
    subgraph tier_4["Tier 4"]
        n85["CZE_hungarian_alliance"]
        n86["CZE_hungary_intervention"]
        n65["CZE_infiltrate_abwehr"]
        n67{"CZE_military_coup"}
        n70["CZE_uranium_for_soviets"]
    end
    subgraph tier_5["Tier 5"]
        n37["CZE_claims_bohemian_crown"]
        n71["CZE_join_axis"]
        n72["CZE_join_commitern"]
        n73["CZE_support_oster"]
        n74["CZE_zaolzie_for_alliance"]
    end
    subgraph tier_6["Tier 6"]
        n75["CZE_expand_soviet_ties"]
        n76["CZE_faction_research_exchange"]
        n77["CZE_together_against_berlin"]
    end
    subgraph tier_7["Tier 7"]
        n78["CZE_split_poland"]
    end
    subgraph tier_8["Tier 8"]
        n79["CZE_union_with_warsaw"]
    end
    n39 --> n43
    n41 --> n43
    n86 --> n37
    n85 --> n37
    n72 --> n75
    n66 --> n76
    n71 --> n76
    n72 --> n76
    n68 --> n76
    n37 --> n76
    n39 --> n81
    n83 --> n85
    n84 --> n85
    n83 --> n86
    n84 --> n86
    n58 --> n65
    n43 --> n50
    n50 --> n58
    n82 --> n83
    n82 --> n84
    n55 --> n71
    n67 --> n71
    n61 --> n72
    n70 --> n72
    n60 --> n67
    n48 --> n67
    n52 --> n60
    n50 --> n60
    n81 --> n82
    n50 --> n63
    n75 --> n78
    n65 --> n73
    n74 --> n77
    n78 --> n79
    n63 --> n70
    n36 --> n70
    n67 --> n74
    n55 --> n74
    n55 x--x n67
    n48 x--x n60
    n85 x--x n86
    n71 x--x n68
    n71 x--x n74
    n67 x--x n63
    n82 x--x n80
```

# CZE_ministry_of_defense

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n8["CZE_R56_support_strategic_industries"]
        n37["CZE_claims_bohemian_crown"]
        n66["CZE_join_allies"]
        n71["CZE_join_axis"]
        n87(("CZE_ministry_of_defense"))
        n68["CZE_nazi_puppet"]
        n20["CZE_new_tanks"]
        n61["CZE_peoples_revolution"]
        n82["CZE_revive_little_entente"]
        n63["CZE_soviet_intelligence"]
    end
    subgraph tier_1["Tier 1"]
        n88["CZE_R56_finish_the_masaryk_military_hospital"]
        n2["CZE_armament_program"]
        n89["CZE_legacy_of_legions"]
        n90{"CZE_military_education"}
        n91["CZE_reorganize_general_staff"]
    end
    subgraph tier_2["Tier 2"]
        n92["CZE_R56_air_is_our_sea"]
        n11["CZE_R56_complete_the_dubnica_nad_vahom_munition_factory"]
        n3["CZE_czechoslovak_firearms"]
        n93{"CZE_military_maneuvers"}
        n94["CZE_military_science_institute"]
        n80["CZE_soviet_treaties"]
    end
    subgraph tier_3["Tier 3"]
        n18["CZE_R56_firearms_deliveries"]
        n36["CZE_acquire_access_for_soviets"]
        n95["CZE_complete_the_shift_towards_static_defence"]
        n96["CZE_czechoslovak_airforce"]
        n97["CZE_pilot_training"]
        n98["CZE_return_to_mobile_defence"]
    end
    subgraph tier_4["Tier 4"]
        n99["CZE_R56_expand_aircraft_production"]
        n24["CZE_R56_secure_armament_contracts"]
        n25["CZE_artillery_focus"]
        n100["CZE_border_brigades"]
        n101["CZE_extend_military_service_army"]
        n26["CZE_holek_brothers"]
        n102["CZE_integrate_aspects_of_mobile_defence"]
        n103["CZE_mobile_army"]
        n5["CZE_the_central_role_of_artillery_citadels"]
        n70["CZE_uranium_for_soviets"]
        n104["CZE_walter_engines"]
    end
    subgraph tier_5["Tier 5"]
        n105["CZE_R56_new_bomber_prototypes"]
        n29["CZE_armoured_cars"]
        n106["CZE_construct_additional_defence_lines"]
        n107["CZE_engineer_corps"]
        n30["CZE_explosives_production"]
        n108["CZE_fund_further_monoplane_experiments"]
        n109["CZE_indirect_combat"]
        n72["CZE_join_commitern"]
        n110["CZE_new_doctrines"]
        n111["CZE_prepare_new_plan"]
        n112["CZE_reform_the_rop"]
        n113["CZE_the_new_sturmbaons"]
    end
    subgraph tier_6["Tier 6"]
        n114["CZE_R56_heavy_fighter_experiments"]
        n115["CZE_an_impregnable_wall"]
        n116["CZE_cas_focus"]
        n75["CZE_expand_soviet_ties"]
        n76["CZE_faction_research_exchange"]
        n33["CZE_mechanized_units"]
        n117["CZE_repurpose_the_rop"]
        n118["CZE_the_legacy_of_kaiserjagers"]
    end
    subgraph tier_7["Tier 7"]
        n119["CZE_advanced_aircraft_prototypes"]
        n120["CZE_air_modernization"]
        n121["CZE_mobile_artillery"]
        n122["CZE_paradesant_brigade"]
        n78["CZE_split_poland"]
    end
    subgraph tier_8["Tier 8"]
        n123["CZE_an_armoured_army"]
        n124["CZE_jet_engine_research"]
        n79["CZE_union_with_warsaw"]
    end
    n90 --> n92
    n8 --> n11
    n2 --> n11
    n96 --> n99
    n97 --> n99
    n87 --> n88
    n3 --> n18
    n11 --> n18
    n108 --> n114
    n104 --> n105
    n18 --> n24
    n80 --> n36
    n114 --> n119
    n105 --> n119
    n105 --> n120
    n114 --> n120
    n121 --> n123
    n118 --> n123
    n112 --> n115
    n106 --> n115
    n87 --> n2
    n20 --> n29
    n26 --> n29
    n18 --> n25
    n3 --> n25
    n95 --> n100
    n98 --> n100
    n109 --> n116
    n99 --> n116
    n93 --> n95
    n102 --> n106
    n92 --> n96
    n2 --> n3
    n100 --> n107
    n72 --> n75
    n25 --> n30
    n5 --> n30
    n95 --> n101
    n66 --> n76
    n71 --> n76
    n72 --> n76
    n68 --> n76
    n37 --> n76
    n104 --> n108
    n99 --> n108
    n11 --> n26
    n18 --> n26
    n103 --> n109
    n95 --> n102
    n119 --> n124
    n61 --> n72
    n70 --> n72
    n87 --> n89
    n29 --> n33
    n87 --> n90
    n89 --> n93
    n91 --> n93
    n90 --> n93
    n90 --> n94
    n98 --> n103
    n117 --> n121
    n100 --> n110
    n105 --> n122
    n114 --> n122
    n92 --> n97
    n100 --> n111
    n102 --> n112
    n87 --> n91
    n109 --> n117
    n93 --> n98
    n90 --> n80
    n75 --> n78
    n95 --> n5
    n113 --> n118
    n100 --> n113
    n103 --> n113
    n78 --> n79
    n63 --> n70
    n36 --> n70
    n96 --> n104
    n95 x--x n98
    n82 x--x n80
```

# CZE_revitalising_the_danube_flotilla

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["CZE_R56_devalue_the_koruna"]
        n4(("CZE_revitalising_the_danube_flotilla"))
    end
    subgraph tier_1["Tier 1"]
        n9["CZE_poldi_steelworks"]
        n125{"CZE_return_to_the_coastline"}
        n126["CZE_shkoda_heavy_cannons"]
    end
    subgraph tier_2["Tier 2"]
        n127["CZE_a_new_strategy"]
        n128["CZE_rebuild_our_navy"]
    end
    subgraph tier_3["Tier 3"]
        n129["CZE_build_the_ersatz_huszar_destroyers"]
        n130["CZE_modernize_the_whitehead_torpedo"]
        n131["CZE_naval_bomber_focus"]
        n132["CZE_return_to_the_fleet_in_being_doctrine"]
    end
    subgraph tier_4["Tier 4"]
        n133["CZE_a_matter_of_prestige"]
        n134["CZE_focus_on_u-boats"]
        n135["CZE_modern_anti-torpedo_protection"]
    end
    subgraph tier_5["Tier 5"]
        n136{"CZE_begin_building_the_radetzky_battleship"}
        n137["CZE_contesting_the_adriatic"]
        n138["CZE_unrestricted_submarine_warfare"]
    end
    subgraph tier_6["Tier 6"]
        n139["CZE_our_battleship_fleet"]
        n140["CZE_our_own_aircraft_carrier"]
        n141["CZE_quiet_and_deadly"]
    end
    subgraph tier_7["Tier 7"]
        n142["CZE_aero_carrier_fighters"]
        n143["CZE_heavy_fighter_cover"]
        n144["CZE_mediterrenean_wolfpacks"]
        n145["CZE_radar_instalations_in_dalmatia"]
    end
    n132 --> n133
    n125 --> n127
    n140 --> n142
    n133 --> n136
    n127 --> n129
    n135 --> n137
    n134 --> n137
    n133 --> n137
    n129 --> n134
    n139 --> n143
    n141 --> n144
    n130 --> n135
    n127 --> n130
    n128 --> n130
    n127 --> n131
    n136 --> n139
    n136 --> n140
    n4 --> n9
    n1 --> n9
    n138 --> n141
    n140 --> n145
    n139 --> n145
    n125 --> n128
    n4 --> n125
    n128 --> n132
    n4 --> n126
    n134 --> n138
    n127 x--x n128
    n139 x--x n140
```
