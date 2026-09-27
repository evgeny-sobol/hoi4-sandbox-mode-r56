# ICE_coastguard

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ICE_coastguard"))
    end
    subgraph tier_1["Tier 1"]
        n2["ICE_build_dock"]
        n3["ICE_nav_doc"]
        n4["ICE_sea_air"]
    end
    subgraph tier_2["Tier 2"]
        n5["ICE_dockyards_2"]
        n6["ICE_land_and_sea"]
        n7["ICE_ships"]
        n8["ICE_sub"]
    end
    subgraph tier_3["Tier 3"]
        n9["ICE_air_doctrine"]
        n10["ICE_from_afar"]
        n11["ICE_screen_ships"]
    end
    subgraph tier_4["Tier 4"]
        n12["ICE_anti_sub"]
        n13["ICE_expand_rocketry"]
        n14["ICE_fighting_ships"]
    end
    subgraph tier_5["Tier 5"]
        n15["ICE_coast_guard"]
        n16["ICE_nuke"]
    end
    n6 --> n9
    n8 --> n12
    n11 --> n12
    n1 --> n2
    n11 --> n15
    n12 --> n15
    n5 --> n15
    n2 --> n5
    n10 --> n13
    n5 --> n14
    n11 --> n14
    n7 --> n14
    n6 --> n10
    n4 --> n6
    n1 --> n3
    n9 --> n16
    n13 --> n16
    n5 --> n11
    n8 --> n11
    n1 --> n4
    n2 --> n7
    n2 --> n8
```

# ICE_look_away

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"ICE_look_away"}
        n18["ICE_look_den"]
        n19["ICE_recycling_programs"]
    end
    subgraph tier_1["Tier 1"]
        n20{"ICE_look_out"}
    end
    subgraph tier_2["Tier 2"]
        n21["ICE_end_neutrality"]
        n22["ICE_fas_rallies"]
        n23["ICE_strong_neutral"]
        n24["ICE_sup_com"]
        n25["ICE_sup_dem"]
    end
    subgraph tier_3["Tier 3"]
        n26["ICE_abolish_althing"]
        n27["ICE_close_eng"]
        n28["ICE_close_usa"]
        n29["ICE_com_rallies"]
        n30["ICE_distance_den"]
        n31["ICE_fas_youth"]
        n32["ICE_mil_facs"]
    end
    subgraph tier_4["Tier 4"]
        n33["ICE_com_takeover"]
        n34["ICE_fas_leader"]
        n35["ICE_guarantees"]
        n36["ICE_war_manu"]
    end
    subgraph tier_5["Tier 5"]
        n37["ICE_break_den"]
        n38["ICE_eng_defences"]
        n39["ICE_ikarus"]
        n40["ICE_join_allies"]
        n41["ICE_join_com"]
        n42["ICE_usa_airport"]
        n43["ICE_vikings"]
    end
    subgraph tier_6["Tier 6"]
        n44["ICE_ally_tech"]
        n45["ICE_com_kill_oppressors"]
        n46["ICE_eng_expand_airport"]
        n47["ICE_ger_coop"]
        n48["ICE_mountain_train"]
        n49["ICE_shieldmaidens"]
        n50["ICE_sov_group"]
        n51["ICE_sov_tech"]
    end
    subgraph tier_7["Tier 7"]
        n52["ICE_ger_tech"]
    end
    n22 --> n26
    n40 --> n44
    n42 --> n44
    n38 --> n44
    n35 --> n37
    n33 --> n37
    n21 --> n27
    n21 --> n28
    n41 --> n45
    n37 --> n45
    n24 --> n29
    n29 --> n33
    n25 --> n30
    n20 --> n21
    n27 --> n38
    n35 --> n38
    n23 --> n38
    n38 --> n46
    n26 --> n34
    n20 --> n22
    n22 --> n31
    n39 --> n47
    n47 --> n52
    n30 --> n35
    n34 --> n39
    n35 --> n40
    n33 --> n41
    n18 --> n20
    n17 --> n20
    n19 --> n32
    n21 --> n32
    n38 --> n48
    n43 --> n49
    n31 --> n49
    n41 --> n50
    n41 --> n51
    n20 --> n23
    n20 --> n24
    n17 --> n25
    n20 --> n25
    n28 --> n42
    n23 --> n42
    n35 --> n42
    n34 --> n43
    n32 --> n36
    n21 x--x n23
    n22 x--x n24
    n22 x--x n25
    n17 x--x n18
    n24 x--x n25
```

# ICE_look_den

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"ICE_look_away"}
        n18(("ICE_look_den"))
        n19["ICE_recycling_programs"]
    end
    subgraph tier_1["Tier 1"]
        n53["ICE_den_inf"]
        n54["ICE_den_research_collab"]
        n20{"ICE_look_out"}
    end
    subgraph tier_2["Tier 2"]
        n55["ICE_den_mil_invest"]
        n21["ICE_end_neutrality"]
        n22["ICE_fas_rallies"]
        n23["ICE_strong_neutral"]
        n24["ICE_sup_com"]
        n25["ICE_sup_dem"]
    end
    subgraph tier_3["Tier 3"]
        n26["ICE_abolish_althing"]
        n27["ICE_close_eng"]
        n28["ICE_close_usa"]
        n29["ICE_com_rallies"]
        n56["ICE_den_invest_final"]
        n30["ICE_distance_den"]
        n31["ICE_fas_youth"]
        n32["ICE_mil_facs"]
    end
    subgraph tier_4["Tier 4"]
        n33["ICE_com_takeover"]
        n34["ICE_fas_leader"]
        n35["ICE_guarantees"]
        n36["ICE_war_manu"]
    end
    subgraph tier_5["Tier 5"]
        n37["ICE_break_den"]
        n38["ICE_eng_defences"]
        n39["ICE_ikarus"]
        n40["ICE_join_allies"]
        n41["ICE_join_com"]
        n42["ICE_usa_airport"]
        n43["ICE_vikings"]
    end
    subgraph tier_6["Tier 6"]
        n44["ICE_ally_tech"]
        n45["ICE_com_kill_oppressors"]
        n46["ICE_eng_expand_airport"]
        n47["ICE_ger_coop"]
        n48["ICE_mountain_train"]
        n49["ICE_shieldmaidens"]
        n50["ICE_sov_group"]
        n51["ICE_sov_tech"]
    end
    subgraph tier_7["Tier 7"]
        n52["ICE_ger_tech"]
    end
    n22 --> n26
    n40 --> n44
    n42 --> n44
    n38 --> n44
    n35 --> n37
    n33 --> n37
    n21 --> n27
    n21 --> n28
    n41 --> n45
    n37 --> n45
    n24 --> n29
    n29 --> n33
    n18 --> n53
    n55 --> n56
    n53 --> n55
    n18 --> n54
    n25 --> n30
    n20 --> n21
    n27 --> n38
    n35 --> n38
    n23 --> n38
    n38 --> n46
    n26 --> n34
    n20 --> n22
    n22 --> n31
    n39 --> n47
    n47 --> n52
    n30 --> n35
    n34 --> n39
    n35 --> n40
    n33 --> n41
    n18 --> n20
    n17 --> n20
    n19 --> n32
    n21 --> n32
    n38 --> n48
    n43 --> n49
    n31 --> n49
    n41 --> n50
    n41 --> n51
    n20 --> n23
    n20 --> n24
    n17 --> n25
    n20 --> n25
    n28 --> n42
    n23 --> n42
    n35 --> n42
    n34 --> n43
    n32 --> n36
    n21 x--x n23
    n22 x--x n24
    n22 x--x n25
    n17 x--x n18
    n24 x--x n25
```

# ICE_national_def_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n57(("ICE_national_def_force"))
    end
    subgraph tier_1["Tier 1"]
        n58["ICE_create_ifv"]
        n59{"ICE_train_reserves"}
    end
    subgraph tier_2["Tier 2"]
        n60["ICE_look_into_armour"]
        n61["ICE_look_into_special"]
        n62["ICE_reserve_focus"]
    end
    subgraph tier_3["Tier 3"]
        n63["ICE_by_air"]
        n64["ICE_local_militia"]
        n65["ICE_mobile_warfare"]
        n66["ICE_mountain_focus"]
        n67["ICE_on_sea"]
    end
    subgraph tier_4["Tier 4"]
        n68["ICE_advanced_weapons"]
        n69["ICE_heavy_armour"]
        n70["ICE_island_defence"]
        n71["ICE_mobile_armour"]
        n72["ICE_propaganda"]
        n73["ICE_special_done"]
    end
    subgraph tier_5["Tier 5"]
        n74["ICE_pure_armour"]
    end
    n64 --> n68
    n61 --> n63
    n57 --> n58
    n65 --> n69
    n64 --> n70
    n62 --> n64
    n59 --> n60
    n59 --> n61
    n65 --> n71
    n60 --> n65
    n61 --> n66
    n61 --> n67
    n64 --> n72
    n71 --> n74
    n69 --> n74
    n59 --> n62
    n66 --> n73
    n67 --> n73
    n63 --> n73
    n57 --> n59
    n60 x--x n61
```

# ICE_roads_program

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n21["ICE_end_neutrality"]
        n75(("ICE_roads_program"))
    end
    subgraph tier_1["Tier 1"]
        n76["ICE_domestic_ind"]
        n77["ICE_new_industry"]
    end
    subgraph tier_2["Tier 2"]
        n78["ICE_infr_2"]
        n19["ICE_recycling_programs"]
    end
    subgraph tier_3["Tier 3"]
        n32["ICE_mil_facs"]
        n79["ICE_new_indu"]
        n80["ICE_refine_research"]
        n81["ICE_steel_mill"]
    end
    subgraph tier_4["Tier 4"]
        n82["ICE_discoveries"]
        n36["ICE_war_manu"]
    end
    subgraph tier_5["Tier 5"]
        n83["ICE_geothermic_banana_production_r56"]
    end
    n81 --> n82
    n80 --> n82
    n75 --> n76
    n82 --> n83
    n79 --> n83
    n77 --> n78
    n76 --> n78
    n19 --> n32
    n21 --> n32
    n19 --> n79
    n78 --> n79
    n75 --> n77
    n76 --> n19
    n78 --> n80
    n78 --> n81
    n32 --> n36
```
