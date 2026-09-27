# GRE_fight_depression

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("GRE_fight_depression"))
    end
    subgraph tier_1["Tier 1"]
        n2["GRE_end_the_depression"]
    end
    subgraph tier_2["Tier 2"]
        n3["GRE_army_reform"]
        n4{"GRE_aviation_effort"}
        n5["GRE_civilian_shipbuilders"]
        n6["GRE_economic_recovery"]
        n7["GRE_fund_the_navy"]
    end
    subgraph tier_3["Tier 3"]
        n8["GRE_armor_effort"]
        n9["GRE_cas_focus"]
        n10["GRE_fighter_focus"]
        n11{"GRE_heavy_cruiser_effort"}
        n12["GRE_industrial_effort"]
        n13["GRE_infrastructure_effort"]
        n14{"GRE_naval_construction"}
        n15["GRE_naval_way"]
        n16["GRE_new_plans"]
        n17["GRE_support_artillery"]
        n18["GRE_support_equipment_modernization"]
    end
    subgraph tier_4["Tier 4"]
        n19["GRE_battleship_focus"]
        n20["GRE_bomber_focus"]
        n21["GRE_carrier_focus"]
        n22["GRE_further_air_plans"]
        n23["GRE_industrial_effort_2"]
        n24["GRE_infantry_weapons"]
        n25["GRE_land_doctrine_1"]
        n26["GRE_light_ship_effort"]
        n27["GRE_med_armor_effort"]
        n28["GRE_olive_export"]
        n29["GRE_submarine_effort"]
    end
    subgraph tier_5["Tier 5"]
        n30["GRE_base_strike"]
        n31["GRE_establish_a_general_staff"]
        n32["GRE_extra_tech_slot"]
        n33["GRE_fleet_in_being"]
        n34["GRE_motorization_effort"]
        n35["GRE_naval_artillery"]
        n36["GRE_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n37["GRE_bullet_factories"]
        n38["GRE_further_development"]
        n39["GRE_jobs_for_the_people"]
        n40["GRE_mechanization_effort"]
        n41["GRE_the_final_plans"]
    end
    subgraph tier_7["Tier 7"]
        n42["GRE_polymer_effort"]
    end
    subgraph tier_8["Tier 8"]
        n43["GRE_industrial_innovations"]
    end
    n3 --> n8
    n2 --> n3
    n2 --> n4
    n21 --> n30
    n11 --> n19
    n10 --> n20
    n9 --> n20
    n32 --> n37
    n11 --> n21
    n4 --> n9
    n2 --> n5
    n2 --> n6
    n1 --> n2
    n25 --> n31
    n23 --> n32
    n4 --> n10
    n19 --> n33
    n2 --> n7
    n10 --> n22
    n9 --> n22
    n32 --> n38
    n7 --> n11
    n6 --> n12
    n12 --> n23
    n13 --> n23
    n42 --> n43
    n16 --> n24
    n6 --> n13
    n32 --> n39
    n16 --> n25
    n14 --> n26
    n34 --> n40
    n8 --> n27
    n24 --> n34
    n19 --> n35
    n7 --> n14
    n5 --> n14
    n7 --> n15
    n3 --> n16
    n12 --> n28
    n38 --> n42
    n25 --> n36
    n14 --> n29
    n3 --> n17
    n3 --> n18
    n30 --> n41
    n33 --> n41
    n19 x--x n21
    n9 x--x n10
    n26 x--x n29
```

# GRE_political_awakening

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n44(("GRE_political_awakening"))
    end
    subgraph tier_1["Tier 1"]
        n45{"GRE_divided_nation"}
    end
    subgraph tier_2["Tier 2"]
        n46["GRE_aftermath_of_the_victory_of_the_people"]
        n47["GRE_democratic_approach"]
        n48["GRE_national_security_concerns"]
        n49["GRE_national_union"]
        n50{"GRE_reinforce_royal_dictatorship"}
    end
    subgraph tier_3["Tier 3"]
        n51["GRE_agrarian_protests"]
        n52["GRE_begin_internal_reforms"]
        n53["GRE_british_allignment"]
        n54["GRE_crush_kke"]
        n55["GRE_devout_to_the_monarchy"]
        n56["GRE_diplomatic_actions"]
        n57["GRE_establish_the_royal_armory"]
        n58["GRE_glorify_race"]
        n59["GRE_internal_affairs"]
        n60["GRE_king_general"]
        n61["GRE_no_allignment"]
        n62{"GRE_prepare_expansion"}
        n63["GRE_recruitment_focus"]
        n64["GRE_royal_roads"]
        n65["GRE_strategic_interests"]
    end
    subgraph tier_4["Tier 4"]
        n66{"GRE_alliances"}
        n67["GRE_befriend_france"]
        n68["GRE_create_a_new_economic_plan"]
        n69["GRE_demand_dodecanese"]
        n70["GRE_demand_east_thrace"]
        n71["GRE_denounce_metaxism"]
        n72["GRE_ensure_stability"]
        n73{"GRE_expansionism"}
        n74["GRE_fate_of_the_royal_family"]
        n75["GRE_honor_byzantium"]
        n76["GRE_king_george_line"]
        n77["GRE_purchase_cyprus"]
        n78{"GRE_purge_republicans"}
        n79["GRE_reclaim_cyprus"]
        n80["GRE_reinforce_4th_of_august_regime"]
        n81["GRE_restaff_the_army_command"]
        n82["GRE_rival_germany"]
        n83["GRE_royal_guards"]
    end
    subgraph tier_5["Tier 5"]
        n84["GRE_absolute_monarchy"]
        n85["GRE_befriend_britain"]
        n86{"GRE_befriend_germany"}
        n87{"GRE_befriend_italy"}
        n88["GRE_begin_reconstruction"]
        n89["GRE_deal_with_klaras"]
        n90["GRE_democratic_economic_policy"]
        n91["GRE_embrace_metaxism"]
        n92["GRE_enosis"]
        n93["GRE_french_innovations"]
        n94["GRE_megali_idea"]
        n95["GRE_monarchist_fervour"]
        n96["GRE_political_opposition"]
        n97["GRE_protect_northern_minorities"]
        n98["GRE_reclaim_dodecanese"]
        n99["GRE_reform_agricultural_economy"]
        n100["GRE_rival_italy"]
        n101["GRE_share_power"]
    end
    subgraph tier_6["Tier 6"]
        n102["GRE_a_stong_kingdom"]
        n103["GRE_allied_membership"]
        n104["GRE_british_innovetions"]
        n105["GRE_control_the_stocks"]
        n106["GRE_create_EON"]
        n107["GRE_dodecanese_for_membership"]
        n108["GRE_dominant_ideology"]
        n109["GRE_foreign_investments"]
        n110["GRE_found_opla"]
        n111["GRE_improve_roads"]
        n112["GRE_international_socialist_volunteers"]
        n113["GRE_join_the_axis"]
        n114["GRE_metaxas_bullet_industry"]
        n115["GRE_metaxas_industry"]
        n116["GRE_metaxas_unions"]
        n117["GRE_purge_remaining_fascist_remnants"]
        n118["GRE_welfare_state"]
        n119{"GRE_world_stage"}
    end
    subgraph tier_7["Tier 7"]
        n120["GRE_Reinforce_the_hierarchy"]
        n121["GRE_abandon_the_west"]
        n122["GRE_ask_for_cyprus"]
        n123["GRE_create_the_IKA"]
        n124["GRE_create_the_civil_guard"]
        n125["GRE_dont_tread_the_empire"]
        n126["GRE_enforce_nationalization"]
        n127["GRE_metaxas_line"]
        n128["GRE_military_reforms"]
        n129["GRE_military_teachings"]
        n130{"GRE_promote_peace_in_the_balkans"}
        n131["GRE_protect_albania"]
    end
    subgraph tier_8["Tier 8"]
        n132["GRE_city_defenses"]
        n133["GRE_italian_war"]
        n134["GRE_join_balkan_entente"]
        n135{"GRE_marxs_dream"}
        n136["GRE_metaxa_militarism"]
        n137["GRE_metaxas_line_expanded"]
        n138["GRE_surprise_attack_italy"]
    end
    subgraph tier_9["Tier 9"]
        n139["GRE_ally_the_balkans"]
        n140["GRE_befriend_sov"]
        n141["GRE_join_the_balkanic_revolution"]
        n142["GRE_third_hellenic_civilization_r56"]
    end
    subgraph tier_10["Tier 10"]
        n143["GRE_aid_the_pcr"]
        n144["GRE_buy_sov_guns"]
        n145["GRE_form_new_government"]
        n146["GRE_invite_albania"]
        n147["GRE_invite_bulgaria"]
        n148["GRE_liberate_the_straits"]
        n149["GRE_subjugate_albania"]
        n150["GRE_subjugate_bulgaria"]
    end
    subgraph tier_11["Tier 11"]
        n151["GRE_invite_yugoslavia"]
        n152["GRE_join_comintern"]
        n153["GRE_subjugate_yugoslavia"]
    end
    subgraph tier_12["Tier 12"]
        n154["GRE_joint_economic_cooperation_with_the_ussr"]
        n155["GRE_utopian_paradise"]
    end
    n117 --> n120
    n75 --> n102
    n77 --> n102
    n79 --> n102
    n101 --> n102
    n84 --> n102
    n119 --> n121
    n78 --> n84
    n45 --> n46
    n48 --> n51
    n139 --> n143
    n141 --> n143
    n140 --> n143
    n65 --> n66
    n100 --> n103
    n85 --> n103
    n135 --> n139
    n103 --> n122
    n67 --> n85
    n56 --> n67
    n66 --> n86
    n66 --> n87
    n135 --> n140
    n46 --> n52
    n80 --> n88
    n50 --> n53
    n85 --> n104
    n140 --> n144
    n128 --> n132
    n99 --> n105
    n91 --> n106
    n52 --> n68
    n111 --> n123
    n115 --> n123
    n112 --> n124
    n48 --> n54
    n81 --> n89
    n62 --> n69
    n62 --> n70
    n45 --> n47
    n72 --> n90
    n71 --> n90
    n59 --> n71
    n50 --> n55
    n47 --> n56
    n44 --> n45
    n87 --> n107
    n96 --> n108
    n119 --> n125
    n80 --> n91
    n105 --> n126
    n73 --> n92
    n59 --> n72
    n50 --> n57
    n65 --> n73
    n52 --> n74
    n90 --> n109
    n140 --> n145
    n89 --> n110
    n67 --> n93
    n49 --> n58
    n60 --> n75
    n88 --> n111
    n47 --> n59
    n89 --> n112
    n139 --> n146
    n139 --> n147
    n146 --> n151
    n147 --> n151
    n129 --> n133
    n130 --> n134
    n145 --> n152
    n144 --> n152
    n86 --> n113
    n135 --> n141
    n152 --> n154
    n50 --> n60
    n61 --> n76
    n53 --> n76
    n139 --> n148
    n141 --> n148
    n140 --> n148
    n126 --> n135
    n89 --> n135
    n120 --> n135
    n73 --> n94
    n127 --> n136
    n129 --> n136
    n88 --> n114
    n88 --> n115
    n106 --> n127
    n127 --> n137
    n88 --> n116
    n109 --> n128
    n118 --> n128
    n106 --> n129
    n80 --> n95
    n45 --> n48
    n45 --> n49
    n50 --> n61
    n80 --> n96
    n50 --> n62
    n119 --> n130
    n119 --> n131
    n74 --> n97
    n62 --> n77
    n97 --> n117
    n55 --> n78
    n62 --> n79
    n73 --> n98
    n49 --> n63
    n68 --> n99
    n54 --> n80
    n51 --> n80
    n45 --> n50
    n52 --> n81
    n56 --> n82
    n82 --> n100
    n62 --> n83
    n50 --> n64
    n78 --> n101
    n49 --> n65
    n139 --> n149
    n141 --> n149
    n139 --> n150
    n141 --> n150
    n149 --> n153
    n150 --> n153
    n128 --> n138
    n123 --> n142
    n127 --> n142
    n121 --> n142
    n125 --> n142
    n134 --> n142
    n153 --> n155
    n90 --> n118
    n91 --> n119
    n121 x--x n125
    n121 x--x n134
    n84 x--x n101
    n46 x--x n47
    n46 x--x n48
    n46 x--x n49
    n46 x--x n50
    n139 x--x n140
    n139 x--x n141
    n87 x--x n98
    n140 x--x n141
    n53 x--x n61
    n47 x--x n48
    n47 x--x n49
    n47 x--x n50
    n107 x--x n113
    n125 x--x n134
    n48 x--x n49
    n48 x--x n50
    n49 x--x n50
    n77 x--x n79
```
