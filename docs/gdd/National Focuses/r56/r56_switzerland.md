# SWI_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SWI_army"))
        n2["SWI_planning"]
    end
    subgraph tier_1["Tier 1"]
        n3{"SWI_modern_arty"}
        n4{"SWI_update_army"}
    end
    subgraph tier_2["Tier 2"]
        n5["SWI_a_land_of_mountains"]
        n6["SWI_choose_cons"]
        n7["SWI_end_con"]
        n8["SWI_heer"]
    end
    subgraph tier_3["Tier 3"]
        n9["SWI_con_to_army"]
        n10["SWI_improve_con"]
        n11["SWI_mountain_artillery"]
    end
    subgraph tier_4["Tier 4"]
        n12["SWI_new_mil"]
        n13["SWI_ready_for_all"]
    end
    n4 --> n5
    n3 --> n5
    n2 --> n5
    n4 --> n6
    n3 --> n6
    n7 --> n9
    n4 --> n7
    n3 --> n7
    n4 --> n8
    n3 --> n8
    n2 --> n8
    n6 --> n10
    n1 --> n3
    n5 --> n11
    n9 --> n12
    n10 --> n13
    n1 --> n4
    n6 x--x n7
```

# SWI_build_docks

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14(("SWI_build_docks"))
        n15["SWI_naval_doc"]
        n16["SWI_other_air"]
    end
    subgraph tier_1["Tier 1"]
        n17["SWI_reform_flotilla"]
    end
    subgraph tier_2["Tier 2"]
        n18["SWI_expand_docks"]
        n19["SWI_naval_catchup"]
    end
    subgraph tier_3["Tier 3"]
        n20["SWI_fast_build_navy"]
        n21["SWI_naval_air"]
    end
    n17 --> n18
    n19 --> n20
    n19 --> n21
    n16 --> n21
    n17 --> n19
    n14 --> n17
    n15 --> n17
```

# SWI_fortifications

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n22(("SWI_fortifications"))
        n3["SWI_modern_arty"]
        n4["SWI_update_army"]
    end
    subgraph tier_1["Tier 1"]
        n23["SWI_first_line"]
        n2["SWI_planning"]
    end
    subgraph tier_2["Tier 2"]
        n5["SWI_a_land_of_mountains"]
        n24["SWI_aa"]
        n25["SWI_extended_army"]
        n8["SWI_heer"]
    end
    subgraph tier_3["Tier 3"]
        n11["SWI_mountain_artillery"]
        n26{"SWI_redoubt"}
    end
    subgraph tier_4["Tier 4"]
        n27["SWI_fortress"]
        n28["SWI_three_layer"]
    end
    n4 --> n5
    n3 --> n5
    n2 --> n5
    n2 --> n24
    n23 --> n24
    n23 --> n25
    n22 --> n23
    n26 --> n27
    n4 --> n8
    n3 --> n8
    n2 --> n8
    n5 --> n11
    n22 --> n2
    n25 --> n26
    n26 --> n28
    n27 x--x n28
```

# SWI_geistige

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29{"SWI_geistige"}
    end
    subgraph tier_1["Tier 1"]
        n30["SWI_burger"]
        n31{"SWI_richtlinienbewegung"}
        n32{"SWI_rise_of_front"}
    end
    subgraph tier_2["Tier 2"]
        n33{"SWI_compromise"}
        n34["SWI_corporatism"]
        n35["SWI_go_left"]
        n36["SWI_kill_henne"]
        n37{"SWI_pro_company"}
    end
    subgraph tier_3["Tier 3"]
        n38["SWI_continue_neutral"]
        n39["SWI_helvetia"]
        n40["SWI_old_confederation"]
        n41["SWI_one_man"]
        n42["SWI_pro_allies"]
        n43["SWI_radical_left"]
    end
    subgraph tier_4["Tier 4"]
        n44["SWI_anti_communism"]
        n45["SWI_end_neutral_left"]
        n46["SWI_foreign_trade"]
        n47["SWI_irredentism"]
    end
    subgraph tier_5["Tier 5"]
        n48["SWI_support_friends"]
    end
    subgraph tier_6["Tier 6"]
        n49["SWI_intervention_in_liechtenstein_r56"]
    end
    n42 --> n44
    n29 --> n30
    n31 --> n33
    n33 --> n38
    n37 --> n38
    n32 --> n34
    n43 --> n45
    n38 --> n46
    n31 --> n35
    n33 --> n39
    n37 --> n39
    n48 --> n49
    n44 --> n49
    n40 --> n47
    n41 --> n47
    n32 --> n36
    n36 --> n40
    n34 --> n41
    n33 --> n42
    n30 --> n37
    n35 --> n43
    n29 --> n31
    n29 --> n32
    n45 --> n48
    n42 --> n48
    n30 x--x n31
    n30 x--x n32
    n33 x--x n35
    n38 x--x n42
    n34 x--x n36
    n31 x--x n32
```

# SWI_international

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n50(("SWI_international"))
    end
    subgraph tier_1["Tier 1"]
        n51["SWI_banks"]
        n52{"SWI_go_fra"}
        n53{"SWI_go_ger"}
        n54{"SWI_go_ita"}
        n55["SWI_red_cross"]
    end
    subgraph tier_2["Tier 2"]
        n56{"SWI_end_neutral"}
        n57{"SWI_saty_neutral"}
    end
    subgraph tier_3["Tier 3"]
        n58["SWI_democratic_diplo"]
        n59{"SWI_fascist_diplo"}
        n60["SWI_recognize_ussr"]
        n61["SWI_stay_neutral"]
    end
    subgraph tier_4["Tier 4"]
        n62["SWI_internal_focus"]
        n63["SWI_join_allies"]
        n64["SWI_join_cominterm"]
        n65["SWI_join_germany"]
        n66["SWI_join_italy"]
    end
    subgraph tier_5["Tier 5"]
        n67["SWI_expand_uni"]
        n68["SWI_extend_maginot"]
        n69["SWI_french_tech"]
        n70["SWI_ger_tech"]
        n71["SWI_italian_tech"]
        n72["SWI_sov_tech"]
        n73["SWI_sov_weapons"]
    end
    subgraph tier_6["Tier 6"]
        n74["SWI_air_inno"]
    end
    n71 --> n74
    n70 --> n74
    n50 --> n51
    n56 --> n58
    n54 --> n56
    n53 --> n56
    n52 --> n56
    n62 --> n67
    n63 --> n68
    n56 --> n59
    n63 --> n69
    n65 --> n70
    n50 --> n52
    n50 --> n53
    n50 --> n54
    n61 --> n62
    n66 --> n71
    n58 --> n63
    n60 --> n64
    n59 --> n65
    n59 --> n66
    n56 --> n60
    n50 --> n55
    n54 --> n57
    n53 --> n57
    n52 --> n57
    n64 --> n72
    n64 --> n73
    n57 --> n61
    n58 x--x n59
    n58 x--x n60
    n58 x--x n61
    n56 x--x n57
    n59 x--x n60
    n59 x--x n61
    n65 x--x n66
    n60 x--x n61
```

# SWI_naval_doc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14["SWI_build_docks"]
        n15(("SWI_naval_doc"))
        n16["SWI_other_air"]
    end
    subgraph tier_1["Tier 1"]
        n17["SWI_reform_flotilla"]
    end
    subgraph tier_2["Tier 2"]
        n18["SWI_expand_docks"]
        n19["SWI_naval_catchup"]
    end
    subgraph tier_3["Tier 3"]
        n20["SWI_fast_build_navy"]
        n21["SWI_naval_air"]
    end
    n17 --> n18
    n19 --> n20
    n19 --> n21
    n16 --> n21
    n17 --> n19
    n14 --> n17
    n15 --> n17
```

# SWI_reorganise_af

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19["SWI_naval_catchup"]
        n75{"SWI_reorganise_af"}
    end
    subgraph tier_1["Tier 1"]
        n76["SWI_foreign_air"]
        n77["SWI_home_air"]
    end
    subgraph tier_2["Tier 2"]
        n78["SWI_fighter_focus"]
        n79["SWI_focus_foreign_air"]
        n80["SWI_focus_home_air"]
    end
    subgraph tier_3["Tier 3"]
        n81["SWI_defend_homeskies"]
        n16["SWI_other_air"]
    end
    subgraph tier_4["Tier 4"]
        n82["SWI_interceptors"]
        n21["SWI_naval_air"]
    end
    n79 --> n81
    n80 --> n81
    n76 --> n78
    n77 --> n78
    n76 --> n79
    n77 --> n80
    n75 --> n76
    n75 --> n77
    n81 --> n82
    n16 --> n82
    n19 --> n21
    n16 --> n21
    n79 --> n16
    n80 --> n16
    n76 x--x n77
```

# SWI_trade

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n83(("SWI_trade"))
    end
    subgraph tier_1["Tier 1"]
        n84["SWI_railroads"]
        n85["SWI_renegotiate"]
    end
    subgraph tier_2["Tier 2"]
        n86["SWI_prepare"]
    end
    subgraph tier_3["Tier 3"]
        n87["SWI_modern_mil_facs"]
        n88["SWI_shadow"]
        n89["SWI_stock"]
    end
    subgraph tier_4["Tier 4"]
        n90["SWI_convoys"]
        n91["SWI_light_naval_guns"]
        n92["SWI_modern_at_weapons"]
        n93["SWI_shadow_seize"]
        n94["SWI_stop_export"]
        n95["SWI_wahlen"]
    end
    subgraph tier_5["Tier 5"]
        n96["SWI_agri"]
        n97["SWI_fuel_ration"]
        n98["SWI_mines"]
    end
    subgraph tier_6["Tier 6"]
        n99["SWI_bicycle_infantry"]
        n100["SWI_chemical"]
    end
    subgraph tier_7["Tier 7"]
        n101["SWI_secret_wunderwaffe"]
    end
    n95 --> n96
    n97 --> n99
    n96 --> n100
    n97 --> n100
    n88 --> n90
    n93 --> n97
    n95 --> n97
    n87 --> n91
    n94 --> n98
    n87 --> n92
    n86 --> n87
    n85 --> n86
    n84 --> n86
    n83 --> n84
    n83 --> n85
    n100 --> n101
    n98 --> n101
    n86 --> n88
    n88 --> n93
    n86 --> n89
    n88 --> n94
    n87 --> n94
    n88 --> n95
    n89 --> n95
```
