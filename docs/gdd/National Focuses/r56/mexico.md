# MEX_focus_national_bank

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["MEX_focus_arrest_general_cedillo"]
        n2["MEX_focus_coastal_defence_plan"]
        n3{"MEX_focus_national_bank"}
        n4["MEX_focus_xefo"]
    end
    subgraph tier_1["Tier 1"]
        n5["MEX_focus_agricultural_credit_bank"]
        n6["MEX_focus_liberalize_the_banking_sector"]
        n7["MEX_focus_military_budget_review"]
        n8["MEX_fund_national_railway_company"]
    end
    subgraph tier_2["Tier 2"]
        n9["MEX_focus_confederation_of_mexican_workers"]
        n10["MEX_focus_end_land_reform"]
        n11["MEX_focus_gulf_coast_naval_yards"]
        n12["MEX_focus_heroic_military_college"]
        n13["MEX_focus_pacific_coast_naval_yards"]
        n14["MEX_focus_rural_infrastructure"]
        n15["MEX_focus_strike_breaking"]
    end
    subgraph tier_3["Tier 3"]
        n16["MEX_focus_aviation_workshops"]
        n17{"MEX_focus_brown_water_navy"}
        n18["MEX_focus_peripheral_infrastructure"]
        n19["MEX_focus_privatization"]
        n20["MEX_focus_rent_freeze"]
        n21["MEX_focus_urban_development"]
        n22["MEX_focus_weapons_modernisation"]
    end
    subgraph tier_4["Tier 4"]
        n23["MEX_focus_blue_water_navy"]
        n24{"MEX_focus_caudillo_private_armies"}
        n25["MEX_focus_cientifico_camarilla"]
        n26["MEX_focus_ejido_worker_militias"]
        n27["MEX_focus_military_aviation_specialists"]
        n28["MEX_focus_raiding_navy"]
        n29["MEX_focus_rural_schools"]
        n30["MEX_focus_tank_workshops"]
    end
    subgraph tier_5["Tier 5"]
        n31{"MEX_focus_army_expansion_programme"}
        n32{"MEX_focus_oil_field_expansion"}
        n33["MEX_focus_party_of_the_revolution"]
        n34["MEX_focus_support_general_cedillo"]
    end
    subgraph tier_6["Tier 6"]
        n35["MEX_focus_aerial_artillery"]
        n36["MEX_focus_heavy_artillery"]
        n37{"MEX_focus_nationalize_the_oil_fields"}
        n38["MEX_focus_northern_steel_plants"]
        n39["MEX_focus_royal_dutch_shell"]
    end
    subgraph tier_7["Tier 7"]
        n40["MEX_encourage_foreign_immigration"]
        n41["MEX_focus_community_of_nations"]
        n42["MEX_focus_compensation"]
        n43["MEX_focus_engineering_school"]
        n44["MEX_focus_german_resource_exchange"]
        n45["MEX_focus_oil_revenue_reinvestment"]
        n46["MEX_focus_oppose_yanqui_imperialism"]
        n47["MEX_sign_the_sinclair_agreements"]
    end
    subgraph tier_8["Tier 8"]
        n48["MEX_focus_capital_reserves"]
        n49["MEX_focus_international_proletarianism"]
        n50["MEX_focus_liberty_and_justice_for_all"]
        n51["MEX_focus_new_world_order"]
        n52["MEX_focus_purchase_belize"]
        n53["MEX_focus_television_innovators"]
        n54["MEX_green_revolution"]
        n55["MEX_invite_ibec_investors"]
        n56["MEX_solidify_the_davis_deal"]
        n57["MEX_subsidize_national_economy"]
    end
    subgraph tier_9["Tier 9"]
        n58["MEX_focus_aztec_eagles"]
        n59["MEX_focus_interior_defence_plan"]
        n60["MEX_launch_the_bracero_program"]
    end
    subgraph tier_10["Tier 10"]
        n61["MEX_focus_international_peacekeepers"]
        n62["MEX_focus_march_southwards"]
    end
    subgraph tier_11["Tier 11"]
        n63["MEX_focus_unify_centroamerica"]
    end
    subgraph tier_12["Tier 12"]
        n64["MEX_focus_integrate_the_south"]
        n65["MEX_focus_liberate_the_caribbean"]
        n66["MEX_focus_push_past_the_darien_gap"]
        n67["MEX_focus_seize_the_panama_canal"]
        n68["MEX_focus_the_empresss_grand_armada"]
    end
    subgraph tier_13["Tier 13"]
        n69["MEX_focus_andean_offensive"]
        n70["MEX_focus_forge_an_overseas_empire"]
        n71["MEX_focus_fortify_the_canal"]
        n72["MEX_focus_integrate_the_caribbean"]
        n73["MEX_focus_rescind_the_mexican_cession"]
        n74["MEX_focus_return_to_the_peninsula"]
    end
    subgraph tier_14["Tier 14"]
        n75["MEX_focus_assert_control_in_manila"]
        n76["MEX_focus_redeem_aztlan"]
        n77["MEX_focus_the_defenders_of_catholicism"]
    end
    n39 --> n40
    n37 --> n40
    n31 --> n35
    n3 --> n5
    n66 --> n69
    n30 --> n31
    n27 --> n31
    n73 --> n75
    n12 --> n16
    n50 --> n58
    n17 --> n23
    n13 --> n17
    n11 --> n17
    n45 --> n48
    n19 --> n24
    n21 --> n25
    n39 --> n41
    n37 --> n42
    n5 --> n9
    n20 --> n26
    n6 --> n10
    n38 --> n43
    n4 --> n43
    n68 --> n70
    n67 --> n71
    n37 --> n44
    n7 --> n11
    n31 --> n36
    n7 --> n12
    n65 --> n72
    n63 --> n64
    n49 --> n59
    n51 --> n59
    n58 --> n61
    n52 --> n61
    n46 --> n49
    n3 --> n6
    n63 --> n65
    n42 --> n50
    n47 --> n50
    n59 --> n62
    n2 --> n62
    n16 --> n27
    n3 --> n7
    n32 --> n37
    n44 --> n51
    n32 --> n38
    n29 --> n32
    n25 --> n32
    n39 --> n45
    n37 --> n45
    n37 --> n46
    n7 --> n13
    n26 --> n33
    n14 --> n18
    n10 --> n19
    n41 --> n52
    n63 --> n66
    n17 --> n28
    n73 --> n76
    n9 --> n20
    n67 --> n73
    n68 --> n74
    n32 --> n39
    n5 --> n14
    n18 --> n29
    n63 --> n67
    n6 --> n15
    n24 --> n34
    n22 --> n30
    n43 --> n53
    n74 --> n77
    n63 --> n68
    n62 --> n63
    n15 --> n21
    n12 --> n22
    n3 --> n8
    n43 --> n54
    n42 --> n55
    n50 --> n60
    n37 --> n47
    n44 --> n56
    n46 --> n57
    n35 x--x n36
    n5 x--x n6
    n1 x--x n34
    n23 x--x n28
    n42 x--x n44
    n42 x--x n46
    n42 x--x n47
    n44 x--x n46
    n37 x--x n39
```

# MEX_focus_plan_of_agua_prieta

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n59["MEX_focus_interior_defence_plan"]
        n38["MEX_focus_northern_steel_plants"]
        n78{"MEX_focus_plan_of_agua_prieta"}
        n34["MEX_focus_support_general_cedillo"]
    end
    subgraph tier_1["Tier 1"]
        n79["MEX_focus_ban_political_militias"]
        n80{"MEX_focus_exile_calles"}
        n81["MEX_focus_jefe_maximo"]
        n82{"MEX_focus_legacy_of_revolution"}
        n83["MEX_strengthen_seccion_primera"]
    end
    subgraph tier_2["Tier 2"]
        n84{"MEX_fill_the_loyal_cabinet"}
        n85{"MEX_focus_control_the_army"}
        n86{"MEX_focus_purge_the_bureaucracy"}
        n87{"MEX_focus_revolutionary_women"}
        n88["MEX_focus_the_red_shirts"]
        n89{"MEX_forge_the_pact_of_honor"}
        n90["MEX_purge_callistas"]
        n91["MEX_reintroduce_cientificos"]
    end
    subgraph tier_3["Tier 3"]
        n92["MEX_focus_antidisestablishmentarianism"]
        n1["MEX_focus_arrest_general_cedillo"]
        n93["MEX_focus_communist_revolution"]
        n94{"MEX_focus_depoliticised_army"}
        n95["MEX_focus_enforce_the_calles_law"]
        n96["MEX_focus_institutional_revolution"]
        n97["MEX_focus_repeal_the_calles_law"]
        n98["MEX_focus_soldaderas"]
        n99["MEX_focus_the_gold_shirts"]
        n100["MEX_focus_womens_suffrage"]
        n101["MEX_introduce_political_inquisition"]
        n102["MEX_seize_strategic_businesses"]
    end
    subgraph tier_4["Tier 4"]
        n103{"MEX_focus_abolish_capital_punishment"}
        n104["MEX_focus_international_struggle"]
        n105["MEX_focus_professional_army"]
        n106["MEX_focus_revanchist_revolution"]
        n107{"MEX_focus_rewrite_the_constitution"}
        n108{"MEX_focus_triumph_over_the_cristeros"}
        n109["MEX_rural_militias_recruitment_draft"]
        n110["MEX_the_end_of_the_imperialist_era"]
    end
    subgraph tier_5["Tier 5"]
        n111["MEX_focus_hispanic_culture"]
        n112["MEX_focus_knights_of_columbus"]
        n113{"MEX_focus_legion_of_christ"}
        n114["MEX_focus_revolutionary_class_war"]
        n115["MEX_focus_state_education"]
    end
    subgraph tier_6["Tier 6"]
        n116["MEX_focus_catholic_politics"]
        n117["MEX_focus_church_schools"]
        n118["MEX_focus_crusade_against_atheism"]
        n119{"MEX_focus_spanish_civil_war_refugees"}
        n4["MEX_focus_xefo"]
    end
    subgraph tier_7["Tier 7"]
        n120["MEX_focus_defend_the_imperial_restoration"]
        n43["MEX_focus_engineering_school"]
        n121{"MEX_focus_falangist_veterans"}
        n122["MEX_focus_law_on_industrial_promotion"]
        n123["MEX_focus_social_catholicism"]
        n124{"MEX_focus_support_spains_loyalists"}
        n125{"MEX_focus_support_the_spanish_carlists"}
        n126["MEX_focus_triumph_of_synarchism"]
    end
    subgraph tier_8["Tier 8"]
        n127["MEX_focus_bolivarian_alliance"]
        n128["MEX_focus_focus_on_european_affairs"]
        n129["MEX_focus_hispanic_alliance"]
        n130["MEX_focus_nafinsa"]
        n131["MEX_focus_realpolitik"]
        n132{"MEX_focus_synarchist_communes"}
        n53["MEX_focus_television_innovators"]
        n54["MEX_green_revolution"]
    end
    subgraph tier_9["Tier 9"]
        n2["MEX_focus_coastal_defence_plan"]
        n133["MEX_focus_invite_brazil"]
        n134["MEX_focus_liberate_the_antilles"]
        n135["MEX_focus_propaganda_pact"]
        n136["MEX_focus_reform_the_cristero_guard"]
        n137["MEX_focus_smash_the_bureaucrats"]
        n138["MEX_focus_synarchist_youth"]
    end
    subgraph tier_10["Tier 10"]
        n62["MEX_focus_march_southwards"]
        n139["MEX_focus_one_world_government"]
        n140["MEX_pan_latinism_not_pan_americanism"]
    end
    subgraph tier_11["Tier 11"]
        n63["MEX_focus_unify_centroamerica"]
        n141["MEX_lay_down_the_cooperative_basis"]
    end
    subgraph tier_12["Tier 12"]
        n64["MEX_focus_integrate_the_south"]
        n65["MEX_focus_liberate_the_caribbean"]
        n66["MEX_focus_push_past_the_darien_gap"]
        n67["MEX_focus_seize_the_panama_canal"]
        n68["MEX_focus_the_empresss_grand_armada"]
        n142["MEX_intervene_in_the_us"]
        n143["MEX_pan_american_highway"]
    end
    subgraph tier_13["Tier 13"]
        n69["MEX_focus_andean_offensive"]
        n70["MEX_focus_forge_an_overseas_empire"]
        n71["MEX_focus_fortify_the_canal"]
        n72["MEX_focus_integrate_the_caribbean"]
        n73["MEX_focus_rescind_the_mexican_cession"]
        n74["MEX_focus_return_to_the_peninsula"]
    end
    subgraph tier_14["Tier 14"]
        n75["MEX_focus_assert_control_in_manila"]
        n76["MEX_focus_redeem_aztlan"]
        n77["MEX_focus_the_defenders_of_catholicism"]
    end
    n80 --> n84
    n97 --> n103
    n66 --> n69
    n85 --> n92
    n84 --> n1
    n86 --> n1
    n73 --> n75
    n78 --> n79
    n124 --> n127
    n112 --> n116
    n112 --> n117
    n113 --> n117
    n128 --> n2
    n129 --> n2
    n127 --> n2
    n88 --> n93
    n80 --> n85
    n81 --> n85
    n113 --> n118
    n118 --> n120
    n85 --> n94
    n79 --> n94
    n85 --> n95
    n38 --> n43
    n4 --> n43
    n78 --> n80
    n119 --> n121
    n125 --> n128
    n121 --> n128
    n68 --> n70
    n67 --> n71
    n125 --> n129
    n121 --> n129
    n99 --> n111
    n104 --> n111
    n86 --> n96
    n65 --> n72
    n63 --> n64
    n99 --> n104
    n88 --> n104
    n129 --> n133
    n127 --> n133
    n78 --> n81
    n107 --> n112
    n4 --> n122
    n78 --> n82
    n107 --> n113
    n127 --> n134
    n63 --> n65
    n59 --> n62
    n2 --> n62
    n122 --> n130
    n137 --> n139
    n94 --> n105
    n128 --> n135
    n129 --> n135
    n80 --> n86
    n63 --> n66
    n125 --> n131
    n121 --> n131
    n124 --> n131
    n73 --> n76
    n132 --> n136
    n85 --> n97
    n67 --> n73
    n68 --> n74
    n99 --> n106
    n88 --> n114
    n104 --> n114
    n79 --> n87
    n82 --> n87
    n92 --> n107
    n63 --> n67
    n127 --> n137
    n116 --> n123
    n87 --> n98
    n105 --> n119
    n98 --> n119
    n111 --> n119
    n114 --> n119
    n103 --> n115
    n108 --> n115
    n119 --> n124
    n119 --> n125
    n113 --> n125
    n123 --> n132
    n126 --> n132
    n120 --> n132
    n132 --> n138
    n43 --> n53
    n74 --> n77
    n63 --> n68
    n89 --> n99
    n82 --> n88
    n118 --> n126
    n95 --> n108
    n62 --> n63
    n87 --> n100
    n115 --> n4
    n82 --> n89
    n43 --> n54
    n141 --> n142
    n84 --> n101
    n140 --> n141
    n141 --> n143
    n2 --> n140
    n80 --> n90
    n81 --> n91
    n98 --> n109
    n85 --> n102
    n78 --> n83
    n93 --> n110
    n84 x--x n86
    n1 x--x n34
    n79 x--x n82
    n127 x--x n131
    n95 x--x n97
    n80 x--x n81
    n121 x--x n124
    n121 x--x n125
    n128 x--x n129
    n128 x--x n131
    n129 x--x n131
    n112 x--x n113
    n112 x--x n115
    n113 x--x n115
    n105 x--x n98
    n136 x--x n138
    n124 x--x n125
    n99 x--x n88
```
