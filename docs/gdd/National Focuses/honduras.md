# HON_airforce

```mermaid
flowchart TD
    n1["HON_air_bases"]
    n2["HON_air_doctrine"]
    n3(("HON_airforce"))
    n4["HON_army_aviation"]
    n5["HON_army_aviation_2"]
    n6["HON_aviation"]
    n7["HON_naval_aviation"]
    n2 --> n1
    n5 --> n2
    n3 --> n4
    n6 --> n5
    n4 --> n6
    n7 --> n6
    n3 --> n7
```

# HON_army

```mermaid
flowchart TD
    n8["HON_arms"]
    n9["HON_arms_2"]
    n10(("HON_army"))
    n11["HON_army_support"]
    n12["HON_conscription"]
    n13["HON_faster_small_arms"]
    n14["HON_jungle_infant"]
    n15["HON_jungle_moto"]
    n16["HON_jungle_training"]
    n17["HON_land_doc"]
    n18["HON_land_doc_2"]
    n19["HON_land_doc_3"]
    n20["HON_mech_effort"]
    n21["HON_special_forces"]
    n22["HON_special_forces_2"]
    n23["HON_tank_effort"]
    n10 --> n8
    n12 --> n8
    n10 --> n9
    n12 --> n9
    n9 --> n11
    n11 --> n13
    n16 --> n14
    n16 --> n15
    n23 --> n15
    n22 --> n16
    n19 --> n16
    n10 --> n17
    n12 --> n17
    n17 --> n18
    n18 --> n19
    n23 --> n20
    n8 --> n21
    n21 --> n22
    n13 --> n23
```

# HON_conscription

```mermaid
flowchart TD
    n8["HON_arms"]
    n9["HON_arms_2"]
    n10["HON_army"]
    n11["HON_army_support"]
    n12(("HON_conscription"))
    n13["HON_faster_small_arms"]
    n14["HON_jungle_infant"]
    n15["HON_jungle_moto"]
    n16["HON_jungle_training"]
    n17["HON_land_doc"]
    n18["HON_land_doc_2"]
    n19["HON_land_doc_3"]
    n20["HON_mech_effort"]
    n21["HON_special_forces"]
    n22["HON_special_forces_2"]
    n23["HON_tank_effort"]
    n10 --> n8
    n12 --> n8
    n10 --> n9
    n12 --> n9
    n9 --> n11
    n11 --> n13
    n16 --> n14
    n16 --> n15
    n23 --> n15
    n22 --> n16
    n19 --> n16
    n10 --> n17
    n12 --> n17
    n17 --> n18
    n18 --> n19
    n23 --> n20
    n8 --> n21
    n21 --> n22
    n13 --> n23
```

# HON_examine_industry

```mermaid
flowchart TD
    n24["HON_better_research"]
    n25["HON_build_civfact1"]
    n26["HON_build_civfact2"]
    n27["HON_build_docks1"]
    n28["HON_build_infra1"]
    n29["HON_build_infra2"]
    n30["HON_build_milfact1"]
    n31["HON_build_milfact2"]
    n32["HON_build_milfact3"]
    n33(("HON_examine_industry"))
    n34["HON_new_university"]
    n35["HON_power_research"]
    n36["HON_tech_industry"]
    n36 --> n24
    n26 --> n24
    n28 --> n25
    n30 --> n25
    n34 --> n26
    n25 --> n27
    n31 --> n27
    n33 --> n28
    n25 --> n29
    n31 --> n29
    n33 --> n30
    n28 --> n31
    n30 --> n31
    n36 --> n32
    n26 --> n32
    n27 --> n34
    n29 --> n34
    n32 --> n35
    n24 --> n35
    n34 --> n36
```

# HON_navy

```mermaid
flowchart TD
    n37["HON_invest_in_battleships"]
    n38["HON_invest_in_carriers"]
    n39["HON_invest_in_cruisers"]
    n40["HON_invest_in_destroyers"]
    n41["HON_invest_in_subs"]
    n42["HON_invest_in_subs_2"]
    n43["HON_invest_in_subs_3"]
    n44["HON_naval_doctrines"]
    n45(("HON_navy"))
    n46["HON_navy_infrastructure"]
    n39 --> n37
    n39 --> n38
    n40 --> n39
    n45 --> n40
    n45 --> n41
    n41 --> n42
    n42 --> n43
    n37 --> n44
    n38 --> n44
    n43 --> n44
    n44 --> n46
```

# HON_politics

```mermaid
flowchart TD
    n47["HON_a_call_to_arms"]
    n48["HON_against_axis"]
    n49["HON_against_imperialism"]
    n50{"HON_agricola"}
    n51["HON_american_arms"]
    n52["HON_american_support"]
    n53["HON_appoint_brooks"]
    n54["HON_banana_boats"]
    n55["HON_banana_empire"]
    n56["HON_better_industry"]
    n57["HON_buy_canal"]
    n58["HON_campesino_republic"]
    n59["HON_carias_legacy"]
    n60["HON_caribfed"]
    n61["HON_carlist_coup"]
    n62["HON_coastal_forts"]
    n63["HON_collective_agriculture"]
    n64["HON_collectivization"]
    n65["HON_continue_the_fight"]
    n66{"HON_corporate_alliance"}
    n67["HON_corporate_consolidation"]
    n68["HON_corporate_expansion"]
    n69["HON_destroy_fascism_communist"]
    n70["HON_economica"]
    n71["HON_eliminate_competition"]
    n72["HON_empower_domestic_competition"]
    n73["HON_empower_the_consumer_council"]
    n74["HON_establish_a_secret_police_communist"]
    n75["HON_five_year_plan"]
    n76["HON_form_honduran_requetes"]
    n77["HON_fortifications"]
    n78["HON_free_other_latin_markets"]
    n79["HON_free_our_markets"]
    n80["HON_fruit_security"]
    n81{"HON_fruitful_partnership"}
    n82["HON_go_communist"]
    n83["HON_gran_colombia"]
    n84["HON_great_white"]
    n85["HON_haciendas"]
    n86["HON_herrera_jailbreak"]
    n87["HON_honduran_red_army"]
    n88["HON_improved_production"]
    n89["HON_inquisition"]
    n90["HON_integrate_requetes"]
    n91["HON_intendancies"]
    n92["HON_internships"]
    n93{"HON_invite_carlists"}
    n94["HON_invite_ford"]
    n95["HON_invite_juan"]
    n96["HON_invite_zemurray"]
    n97["HON_irca"]
    n98["HON_join_allies"]
    n99["HON_join_soviets"]
    n100{"HON_join_the_fight"}
    n101["HON_kings_finest"]
    n102["HON_land_reform"]
    n103["HON_libargent"]
    n104["HON_liberal_amnesty"]
    n105{"HON_liberate_brazil"}
    n106["HON_liberate_central"]
    n107{"HON_liberate_costarica"}
    n108["HON_liberate_guatemala"]
    n109["HON_liberate_mexico"]
    n110["HON_liberate_mexico_again"]
    n111["HON_liberate_nicaragua"]
    n112["HON_liberate_panama"]
    n113{"HON_liberate_salvador"}
    n114["HON_liblaplata"]
    n115["HON_libperbol"]
    n116["HON_mirco"]
    n117["HON_monarchist_coup"]
    n118["HON_peasant_revolution"]
    n119["HON_peoples_army"]
    n120["HON_peoples_university"]
    n121["HON_peoples_war"]
    n122{"HON_politics"}
    n123["HON_prepare_the_liberation"]
    n124["HON_proclaim_new_spain"]
    n125["HON_protect_our_private_businesses"]
    n126["HON_purchase_belize"]
    n127["HON_reclaim_america"]
    n128["HON_reclaim_costarica"]
    n129["HON_reclaim_cuba"]
    n130["HON_reclaim_guatemala"]
    n131["HON_reclaim_hispanola"]
    n132["HON_reclaim_mexico"]
    n133["HON_reclaim_nicaragua"]
    n134["HON_reclaim_salvador"]
    n135["HON_reclaim_spain"]
    n136["HON_reconquista"]
    n137["HON_refined_goods"]
    n138["HON_reform_the_spanish_empire"]
    n139["HON_renounce_throne_rights"]
    n140["HON_restoration_wars"]
    n141["HON_restore_colonial_suzrenity"]
    n142["HON_seize_plantations"]
    n143["HON_socialist_block"]
    n144["HON_soviet_guns"]
    n145["HON_soviet_intel"]
    n146["HON_soviet_military_buildup"]
    n147["HON_soviet_milmission"]
    n148["HON_soviet_support"]
    n149["HON_spanish_civil_war_involvement"]
    n150["HON_spanish_guns"]
    n151["HON_spanish_millitary_mission"]
    n152["HON_stabilize_economy"]
    n153["HON_status_quo"]
    n154["HON_study_soviet_tactics"]
    n155["HON_suggest_fascism"]
    n156["HON_suggest_monarchy"]
    n157["HON_support_the_indochinese_communists"]
    n158["HON_support_the_prc"]
    n159{"HON_support_the_south_american_communists"}
    n160["HON_support_the_spanish_monarchy"]
    n161["HON_take_costa_rica"]
    n162["HON_take_elsalvador"]
    n163["HON_take_guatemala"]
    n164["HON_take_nicaragua"]
    n165{"HON_take_panama"}
    n166["HON_united_fruit_coup"]
    n167["HON_usa_naval_bases"]
    n168["HON_usa_naval_doctrine"]
    n144 --> n47
    n56 --> n48
    n77 --> n48
    n159 --> n49
    n105 --> n49
    n54 --> n50
    n166 --> n51
    n155 --> n52
    n153 --> n53
    n84 --> n54
    n94 --> n54
    n81 --> n55
    n66 --> n55
    n104 --> n56
    n161 --> n57
    n143 --> n58
    n99 --> n58
    n167 --> n59
    n168 --> n59
    n123 --> n60
    n93 --> n61
    n85 --> n62
    n142 --> n63
    n142 --> n64
    n100 --> n65
    n50 --> n66
    n165 --> n66
    n80 --> n67
    n51 --> n67
    n55 --> n68
    n159 --> n69
    n105 --> n69
    n137 --> n70
    n55 --> n71
    n66 --> n72
    n79 --> n73
    n118 --> n74
    n63 --> n75
    n64 --> n75
    n160 --> n76
    n104 --> n77
    n79 --> n78
    n125 --> n79
    n166 --> n80
    n50 --> n81
    n122 --> n82
    n109 --> n83
    n60 --> n83
    n97 --> n84
    n117 --> n85
    n82 --> n86
    n154 --> n87
    n166 --> n88
    n70 --> n89
    n93 --> n90
    n85 --> n91
    n52 --> n92
    n65 --> n93
    n97 --> n94
    n156 --> n95
    n155 --> n96
    n88 --> n97
    n48 --> n98
    n113 --> n99
    n107 --> n99
    n76 --> n100
    n117 --> n101
    n75 --> n102
    n83 --> n103
    n152 --> n104
    n114 --> n105
    n119 --> n106
    n111 --> n107
    n106 --> n108
    n123 --> n109
    n47 --> n110
    n106 --> n111
    n107 --> n112
    n113 --> n112
    n108 --> n113
    n103 --> n114
    n115 --> n114
    n83 --> n115
    n55 --> n116
    n95 --> n117
    n86 --> n118
    n148 --> n118
    n118 --> n119
    n75 --> n120
    n149 --> n121
    n58 --> n123
    n143 --> n123
    n136 --> n124
    n89 --> n124
    n132 --> n124
    n72 --> n125
    n163 --> n126
    n124 --> n127
    n133 --> n128
    n130 --> n128
    n134 --> n128
    n133 --> n129
    n130 --> n129
    n134 --> n129
    n140 --> n130
    n129 --> n131
    n128 --> n131
    n128 --> n132
    n140 --> n133
    n140 --> n134
    n124 --> n135
    n70 --> n136
    n62 --> n137
    n91 --> n137
    n100 --> n138
    n138 --> n139
    n150 --> n140
    n101 --> n140
    n139 --> n141
    n151 --> n141
    n118 --> n142
    n113 --> n143
    n107 --> n143
    n58 --> n144
    n99 --> n144
    n144 --> n145
    n154 --> n146
    n144 --> n147
    n82 --> n148
    n166 --> n149
    n118 --> n149
    n117 --> n150
    n138 --> n151
    n53 --> n152
    n122 --> n153
    n147 --> n154
    n122 --> n155
    n122 --> n156
    n158 --> n157
    n47 --> n158
    n158 --> n159
    n117 --> n160
    n163 --> n161
    n67 --> n162
    n164 --> n163
    n67 --> n164
    n161 --> n165
    n52 --> n166
    n96 --> n166
    n98 --> n167
    n98 --> n168
    n49 x--x n69
    n55 x--x n72
    n61 x--x n90
    n65 x--x n138
    n66 x--x n81
    n82 x--x n153
    n82 x--x n155
    n82 x--x n156
    n99 x--x n143
    n153 x--x n155
    n153 x--x n156
    n155 x--x n156
```
