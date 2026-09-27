# HON_airforce

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("HON_airforce"))
    end
    subgraph tier_1["Tier 1"]
        n2["HON_army_aviation"]
        n3["HON_naval_aviation"]
    end
    subgraph tier_2["Tier 2"]
        n4["HON_aviation"]
    end
    subgraph tier_3["Tier 3"]
        n5["HON_army_aviation_2"]
    end
    subgraph tier_4["Tier 4"]
        n6["HON_air_doctrine"]
    end
    subgraph tier_5["Tier 5"]
        n7["HON_air_bases"]
    end
    n6 --> n7
    n5 --> n6
    n1 --> n2
    n4 --> n5
    n2 --> n4
    n3 --> n4
    n1 --> n3
```

# HON_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n8(("HON_army"))
        n9["HON_conscription"]
    end
    subgraph tier_1["Tier 1"]
        n10["HON_arms"]
        n11["HON_arms_2"]
        n12["HON_land_doc"]
    end
    subgraph tier_2["Tier 2"]
        n13["HON_army_support"]
        n14["HON_land_doc_2"]
        n15["HON_special_forces"]
    end
    subgraph tier_3["Tier 3"]
        n16["HON_faster_small_arms"]
        n17["HON_land_doc_3"]
        n18["HON_special_forces_2"]
    end
    subgraph tier_4["Tier 4"]
        n19["HON_jungle_training"]
        n20["HON_tank_effort"]
    end
    subgraph tier_5["Tier 5"]
        n21["HON_jungle_infant"]
        n22["HON_jungle_moto"]
        n23["HON_mech_effort"]
    end
    n8 --> n10
    n9 --> n10
    n8 --> n11
    n9 --> n11
    n11 --> n13
    n13 --> n16
    n19 --> n21
    n19 --> n22
    n20 --> n22
    n18 --> n19
    n17 --> n19
    n8 --> n12
    n9 --> n12
    n12 --> n14
    n14 --> n17
    n20 --> n23
    n10 --> n15
    n15 --> n18
    n16 --> n20
```

# HON_conscription

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n8["HON_army"]
        n9(("HON_conscription"))
    end
    subgraph tier_1["Tier 1"]
        n10["HON_arms"]
        n11["HON_arms_2"]
        n12["HON_land_doc"]
    end
    subgraph tier_2["Tier 2"]
        n13["HON_army_support"]
        n14["HON_land_doc_2"]
        n15["HON_special_forces"]
    end
    subgraph tier_3["Tier 3"]
        n16["HON_faster_small_arms"]
        n17["HON_land_doc_3"]
        n18["HON_special_forces_2"]
    end
    subgraph tier_4["Tier 4"]
        n19["HON_jungle_training"]
        n20["HON_tank_effort"]
    end
    subgraph tier_5["Tier 5"]
        n21["HON_jungle_infant"]
        n22["HON_jungle_moto"]
        n23["HON_mech_effort"]
    end
    n8 --> n10
    n9 --> n10
    n8 --> n11
    n9 --> n11
    n11 --> n13
    n13 --> n16
    n19 --> n21
    n19 --> n22
    n20 --> n22
    n18 --> n19
    n17 --> n19
    n8 --> n12
    n9 --> n12
    n12 --> n14
    n14 --> n17
    n20 --> n23
    n10 --> n15
    n15 --> n18
    n16 --> n20
```

# HON_examine_industry

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n24(("HON_examine_industry"))
    end
    subgraph tier_1["Tier 1"]
        n25["HON_build_infra1"]
        n26["HON_build_milfact1"]
    end
    subgraph tier_2["Tier 2"]
        n27["HON_build_civfact1"]
        n28["HON_build_milfact2"]
    end
    subgraph tier_3["Tier 3"]
        n29["HON_build_docks1"]
        n30["HON_build_infra2"]
    end
    subgraph tier_4["Tier 4"]
        n31["HON_new_university"]
    end
    subgraph tier_5["Tier 5"]
        n32["HON_build_civfact2"]
        n33["HON_tech_industry"]
    end
    subgraph tier_6["Tier 6"]
        n34["HON_better_research"]
        n35["HON_build_milfact3"]
    end
    subgraph tier_7["Tier 7"]
        n36["HON_power_research"]
    end
    n33 --> n34
    n32 --> n34
    n25 --> n27
    n26 --> n27
    n31 --> n32
    n27 --> n29
    n28 --> n29
    n24 --> n25
    n27 --> n30
    n28 --> n30
    n24 --> n26
    n25 --> n28
    n26 --> n28
    n33 --> n35
    n32 --> n35
    n29 --> n31
    n30 --> n31
    n35 --> n36
    n34 --> n36
    n31 --> n33
```

# HON_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n37(("HON_navy"))
    end
    subgraph tier_1["Tier 1"]
        n38["HON_invest_in_destroyers"]
        n39["HON_invest_in_subs"]
    end
    subgraph tier_2["Tier 2"]
        n40["HON_invest_in_cruisers"]
        n41["HON_invest_in_subs_2"]
    end
    subgraph tier_3["Tier 3"]
        n42["HON_invest_in_battleships"]
        n43["HON_invest_in_carriers"]
        n44["HON_invest_in_subs_3"]
    end
    subgraph tier_4["Tier 4"]
        n45["HON_naval_doctrines"]
    end
    subgraph tier_5["Tier 5"]
        n46["HON_navy_infrastructure"]
    end
    n40 --> n42
    n40 --> n43
    n38 --> n40
    n37 --> n38
    n37 --> n39
    n39 --> n41
    n41 --> n44
    n42 --> n45
    n43 --> n45
    n44 --> n45
    n45 --> n46
```

# HON_politics

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n47{"HON_politics"}
    end
    subgraph tier_1["Tier 1"]
        n48["HON_go_communist"]
        n49["HON_status_quo"]
        n50["HON_suggest_fascism"]
        n51["HON_suggest_monarchy"]
    end
    subgraph tier_2["Tier 2"]
        n52["HON_american_support"]
        n53["HON_appoint_brooks"]
        n54["HON_herrera_jailbreak"]
        n55["HON_invite_juan"]
        n56["HON_invite_zemurray"]
        n57["HON_soviet_support"]
    end
    subgraph tier_3["Tier 3"]
        n58["HON_internships"]
        n59["HON_monarchist_coup"]
        n60["HON_peasant_revolution"]
        n61["HON_stabilize_economy"]
        n62["HON_united_fruit_coup"]
    end
    subgraph tier_4["Tier 4"]
        n63["HON_american_arms"]
        n64["HON_establish_a_secret_police_communist"]
        n65["HON_fruit_security"]
        n66["HON_haciendas"]
        n67["HON_improved_production"]
        n68["HON_kings_finest"]
        n69["HON_liberal_amnesty"]
        n70["HON_peoples_army"]
        n71["HON_seize_plantations"]
        n72["HON_spanish_civil_war_involvement"]
        n73["HON_spanish_guns"]
        n74["HON_support_the_spanish_monarchy"]
    end
    subgraph tier_5["Tier 5"]
        n75["HON_better_industry"]
        n76["HON_coastal_forts"]
        n77["HON_collective_agriculture"]
        n78["HON_collectivization"]
        n79["HON_corporate_consolidation"]
        n80["HON_form_honduran_requetes"]
        n81["HON_fortifications"]
        n82["HON_intendancies"]
        n83["HON_irca"]
        n84["HON_liberate_central"]
        n85["HON_peoples_war"]
        n86["HON_restoration_wars"]
    end
    subgraph tier_6["Tier 6"]
        n87["HON_against_axis"]
        n88["HON_five_year_plan"]
        n89["HON_great_white"]
        n90["HON_invite_ford"]
        n91{"HON_join_the_fight"}
        n92["HON_liberate_guatemala"]
        n93["HON_liberate_nicaragua"]
        n94["HON_reclaim_guatemala"]
        n95["HON_reclaim_nicaragua"]
        n96["HON_reclaim_salvador"]
        n97["HON_refined_goods"]
        n98["HON_take_elsalvador"]
        n99["HON_take_nicaragua"]
    end
    subgraph tier_7["Tier 7"]
        n100["HON_banana_boats"]
        n101["HON_continue_the_fight"]
        n102["HON_economica"]
        n103["HON_join_allies"]
        n104["HON_land_reform"]
        n105{"HON_liberate_costarica"}
        n106{"HON_liberate_salvador"}
        n107["HON_peoples_university"]
        n108["HON_reclaim_costarica"]
        n109["HON_reclaim_cuba"]
        n110["HON_reform_the_spanish_empire"]
        n111["HON_take_guatemala"]
    end
    subgraph tier_8["Tier 8"]
        n112{"HON_agricola"}
        n113["HON_inquisition"]
        n114{"HON_invite_carlists"}
        n115["HON_join_soviets"]
        n116["HON_liberate_panama"]
        n117["HON_purchase_belize"]
        n118["HON_reclaim_hispanola"]
        n119["HON_reclaim_mexico"]
        n120["HON_reconquista"]
        n121["HON_renounce_throne_rights"]
        n122["HON_socialist_block"]
        n123["HON_spanish_millitary_mission"]
        n124["HON_take_costa_rica"]
        n125["HON_usa_naval_bases"]
        n126["HON_usa_naval_doctrine"]
    end
    subgraph tier_9["Tier 9"]
        n127["HON_buy_canal"]
        n128["HON_campesino_republic"]
        n129["HON_carias_legacy"]
        n130["HON_carlist_coup"]
        n131{"HON_fruitful_partnership"}
        n132["HON_integrate_requetes"]
        n133["HON_proclaim_new_spain"]
        n134["HON_restore_colonial_suzrenity"]
        n135{"HON_take_panama"}
    end
    subgraph tier_10["Tier 10"]
        n136{"HON_corporate_alliance"}
        n137["HON_prepare_the_liberation"]
        n138["HON_reclaim_america"]
        n139["HON_reclaim_spain"]
        n140["HON_soviet_guns"]
    end
    subgraph tier_11["Tier 11"]
        n141["HON_a_call_to_arms"]
        n142["HON_banana_empire"]
        n143["HON_caribfed"]
        n144["HON_empower_domestic_competition"]
        n145["HON_liberate_mexico"]
        n146["HON_soviet_intel"]
        n147["HON_soviet_milmission"]
    end
    subgraph tier_12["Tier 12"]
        n148["HON_corporate_expansion"]
        n149["HON_eliminate_competition"]
        n150["HON_gran_colombia"]
        n151["HON_liberate_mexico_again"]
        n152["HON_mirco"]
        n153["HON_protect_our_private_businesses"]
        n154["HON_study_soviet_tactics"]
        n155["HON_support_the_prc"]
    end
    subgraph tier_13["Tier 13"]
        n156["HON_free_our_markets"]
        n157["HON_honduran_red_army"]
        n158["HON_libargent"]
        n159["HON_libperbol"]
        n160["HON_soviet_military_buildup"]
        n161["HON_support_the_indochinese_communists"]
        n162{"HON_support_the_south_american_communists"}
    end
    subgraph tier_14["Tier 14"]
        n163["HON_empower_the_consumer_council"]
        n164["HON_free_other_latin_markets"]
        n165["HON_liblaplata"]
    end
    subgraph tier_15["Tier 15"]
        n166{"HON_liberate_brazil"}
    end
    subgraph tier_16["Tier 16"]
        n167["HON_against_imperialism"]
        n168["HON_destroy_fascism_communist"]
    end
    n140 --> n141
    n75 --> n87
    n81 --> n87
    n162 --> n167
    n166 --> n167
    n100 --> n112
    n62 --> n63
    n50 --> n52
    n49 --> n53
    n89 --> n100
    n90 --> n100
    n131 --> n142
    n136 --> n142
    n69 --> n75
    n124 --> n127
    n122 --> n128
    n115 --> n128
    n125 --> n129
    n126 --> n129
    n137 --> n143
    n114 --> n130
    n66 --> n76
    n71 --> n77
    n71 --> n78
    n91 --> n101
    n112 --> n136
    n135 --> n136
    n65 --> n79
    n63 --> n79
    n142 --> n148
    n162 --> n168
    n166 --> n168
    n97 --> n102
    n142 --> n149
    n136 --> n144
    n156 --> n163
    n60 --> n64
    n77 --> n88
    n78 --> n88
    n74 --> n80
    n69 --> n81
    n156 --> n164
    n153 --> n156
    n62 --> n65
    n112 --> n131
    n47 --> n48
    n145 --> n150
    n143 --> n150
    n83 --> n89
    n59 --> n66
    n48 --> n54
    n154 --> n157
    n62 --> n67
    n102 --> n113
    n114 --> n132
    n66 --> n82
    n52 --> n58
    n101 --> n114
    n83 --> n90
    n51 --> n55
    n50 --> n56
    n67 --> n83
    n87 --> n103
    n106 --> n115
    n105 --> n115
    n80 --> n91
    n59 --> n68
    n88 --> n104
    n150 --> n158
    n61 --> n69
    n165 --> n166
    n70 --> n84
    n93 --> n105
    n84 --> n92
    n137 --> n145
    n141 --> n151
    n84 --> n93
    n105 --> n116
    n106 --> n116
    n92 --> n106
    n158 --> n165
    n159 --> n165
    n150 --> n159
    n142 --> n152
    n55 --> n59
    n54 --> n60
    n57 --> n60
    n60 --> n70
    n88 --> n107
    n72 --> n85
    n128 --> n137
    n122 --> n137
    n120 --> n133
    n113 --> n133
    n119 --> n133
    n144 --> n153
    n111 --> n117
    n133 --> n138
    n95 --> n108
    n94 --> n108
    n96 --> n108
    n95 --> n109
    n94 --> n109
    n96 --> n109
    n86 --> n94
    n109 --> n118
    n108 --> n118
    n108 --> n119
    n86 --> n95
    n86 --> n96
    n133 --> n139
    n102 --> n120
    n76 --> n97
    n82 --> n97
    n91 --> n110
    n110 --> n121
    n73 --> n86
    n68 --> n86
    n121 --> n134
    n123 --> n134
    n60 --> n71
    n106 --> n122
    n105 --> n122
    n128 --> n140
    n115 --> n140
    n140 --> n146
    n154 --> n160
    n140 --> n147
    n48 --> n57
    n62 --> n72
    n60 --> n72
    n59 --> n73
    n110 --> n123
    n53 --> n61
    n47 --> n49
    n147 --> n154
    n47 --> n50
    n47 --> n51
    n155 --> n161
    n141 --> n155
    n155 --> n162
    n59 --> n74
    n111 --> n124
    n79 --> n98
    n99 --> n111
    n79 --> n99
    n124 --> n135
    n52 --> n62
    n56 --> n62
    n103 --> n125
    n103 --> n126
    n167 x--x n168
    n142 x--x n144
    n130 x--x n132
    n101 x--x n110
    n136 x--x n131
    n48 x--x n49
    n48 x--x n50
    n48 x--x n51
    n115 x--x n122
    n49 x--x n50
    n49 x--x n51
    n50 x--x n51
```
