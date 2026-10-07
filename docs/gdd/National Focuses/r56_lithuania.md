# LIT_Aviation_Effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"LIT_Aviation_Effort"}
    end
    subgraph tier_1["Tier 1"]
        n2{"LIT_Foreign_Design"}
        n3["LIT_fund_the_anbo"]
    end
    subgraph tier_2["Tier 2"]
        n4["LIT_Aircraft_England"]
        n5["LIT_Aircraft_German"]
        n6["LIT_Aircraft_Italian"]
        n7["LIT_Aircraft_Soviet"]
        n8["LIT_Aircraft_american"]
        n9["LIT_Aircraft_japanese"]
        n10["LIT_import_foreign_engines"]
    end
    subgraph tier_3["Tier 3"]
        n11["LIT_Bomber_Competition"]
        n12["LIT_Fighter_Competition"]
        n13["LIT_German_Rocketry"]
        n14["LIT_modernize_planes"]
        n15["LIT_open_pilot_training_facilities"]
    end
    subgraph tier_4["Tier 4"]
        n16["LIT_Close_Air_Support"]
        n17["LIT_Shared_Air_Doctrine"]
        n18["LIT_aircraft_design_cooperation"]
        n19["LIT_anbo_viii"]
        n20["LIT_open_new_aviation_workshops"]
    end
    subgraph tier_5["Tier 5"]
        n21["LIT_antanas_gustaitis_reforms"]
    end
    n2 --> n4
    n2 --> n5
    n2 --> n6
    n2 --> n7
    n2 --> n8
    n2 --> n9
    n5 --> n11
    n4 --> n11
    n8 --> n11
    n7 --> n11
    n6 --> n11
    n9 --> n11
    n12 --> n16
    n4 --> n12
    n5 --> n12
    n7 --> n12
    n6 --> n12
    n9 --> n12
    n1 --> n2
    n5 --> n13
    n12 --> n17
    n11 --> n17
    n12 --> n18
    n11 --> n18
    n14 --> n19
    n19 --> n21
    n20 --> n21
    n1 --> n3
    n3 --> n10
    n10 --> n14
    n15 --> n20
    n10 --> n15
    n4 x--x n8
    n5 x--x n6
    n7 x--x n9
    n2 x--x n3
```

# LIT_a_separate_branch

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n22(("LIT_a_separate_branch"))
    end
    subgraph tier_1["Tier 1"]
        n23["LIT_baltic_navy"]
    end
    subgraph tier_2["Tier 2"]
        n24["LIT_cruisers_development"]
        n25{"LIT_expansion_of_naval_facilities"}
        n26["LIT_study_foreign_navies"]
    end
    subgraph tier_3["Tier 3"]
        n27["LIT_educate_naval_officers_abroad"]
        n28["LIT_klaipda_shipyards"]
        n29["LIT_purchase_foreign_ships"]
        n30["LIT_ventoji_shipyards"]
    end
    subgraph tier_4["Tier 4"]
        n31["LIT_cooperate_with_maritime_organisations"]
        n32{"LIT_develop_indigenous_designs"}
        n33["LIT_purchase_french_ships"]
        n34["LIT_purchase_italian_ships"]
    end
    subgraph tier_5["Tier 5"]
        n35["LIT_defend_the_coast"]
        n36["LIT_raiding_fleet"]
        n37["LIT_revisit_naval_doctrine"]
    end
    subgraph tier_6["Tier 6"]
        n38["LIT_focus_on_destroyer_production"]
        n39["LIT_found_the_lithuanian_maritime_academy"]
        n40["LIT_streamline_submarine_production"]
    end
    n22 --> n23
    n27 --> n31
    n23 --> n24
    n32 --> n35
    n28 --> n32
    n30 --> n32
    n26 --> n27
    n25 --> n27
    n23 --> n25
    n35 --> n38
    n37 --> n39
    n25 --> n28
    n26 --> n29
    n29 --> n33
    n29 --> n34
    n32 --> n36
    n31 --> n37
    n36 --> n40
    n23 --> n26
    n25 --> n30
    n35 x--x n36
    n28 x--x n30
```

# LIT_announce_upcoming_elections

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n41{"LIT_announce_upcoming_elections"}
    end
    subgraph tier_1["Tier 1"]
        n42["LIT_force_parties_to_reregister"]
        n43["LIT_lcp_resurgence"]
        n44{"LIT_solicit_ratikiss_support"}
        n45["LIT_voldemarininkai_coup"]
    end
    subgraph tier_2["Tier 2"]
        n46["LIT_amend_the_electoral_law"]
        n47["LIT_decrease_representation"]
        n48["LIT_dissolve_the_seimas"]
        n49{"LIT_hold_fair_elections"}
        n50["LIT_preparing_for_the_uprising"]
        n51["LIT_reform_the_iron_wolf"]
        n52["LIT_rehabilitate_organisers_of_the_1934_coup"]
        n53["LIT_return_of_voldemaras"]
    end
    subgraph tier_3["Tier 3"]
        n54["LIT_continue_griniuss_presidency"]
        n55["LIT_elect_the_fourth_seimas"]
        n56["LIT_form_the_lithuanian_security_police"]
        n57["LIT_form_the_youth_branch"]
        n58{"LIT_hold_the_lnp_commission"}
        n59["LIT_launch_the_revolution"]
        n60{"LIT_reconvene_the_council_of_lithuania"}
        n61["LIT_subsidize_food_industry"]
        n62["LIT_the_4th_president"]
    end
    subgraph tier_4["Tier 4"]
        n63["LIT_adopt_a_new_constitution"]
        n64["LIT_amnesty_to_political_prisoners"]
        n65["LIT_banish_smetonists"]
        n66["LIT_break_nationalist_union"]
        n67["LIT_contact_the_aurininkai"]
        n68["LIT_empower_patriots"]
        n69["LIT_empower_radicals"]
        n70["LIT_ensure_german_support"]
        n71["LIT_exile_voldemaras"]
        n72["LIT_expand_riflemans_union"]
        n73["LIT_intervene_in_the_german_civil_war"]
        n74["LIT_liberalization_of_trade_policies"]
        n75["LIT_nationalist_education"]
        n76["LIT_new_lithuania"]
        n77["LIT_peoples_army"]
        n78["LIT_reinforce_czechoslovak_ties"]
        n79["LIT_remove_cencorship"]
        n80["LIT_remove_martial_law"]
        n81["LIT_social_welfare_focus"]
        n82["LIT_subsidize_farmers"]
    end
    subgraph tier_5["Tier 5"]
        n83["LIT_academy_of_sciences"]
        n84["LIT_collectivisation"]
        n85["LIT_draw_closer_to_finland"]
        n86{"LIT_draw_closer_to_sweden"}
        n87["LIT_empower_litvak_community"]
        n88["LIT_empower_smetona"]
        n89["LIT_enforce_lithuaniazation"]
        n90["LIT_invest_in_public_education"]
        n91["LIT_join_comintern"]
        n92["LIT_lead_by_example"]
        n93["LIT_militarise_the_iron_wolf"]
        n94["LIT_privatise_lithuanian_railroads"]
        n95["LIT_promote_lithuanian_aryanism"]
        n96["LIT_propose_a_baltic_union"]
        n97["LIT_red_volunteers"]
        n98["LIT_seize_minority_assets"]
        n99["LIT_spread_the_revolution"]
        n100["LIT_syndicalize_agriculture"]
        n101{"LIT_vote_on_monarchy"}
    end
    subgraph tier_6["Tier 6"]
        n102{"LIT_arrest_nazi_sympathizers"}
        n103["LIT_battle_for_lithuania"]
        n104["LIT_cooperate_with_the_conservatives"]
        n105["LIT_form_a_baltic_alliance"]
        n106["LIT_germanlithuanian_credit_agreement"]
        n107["LIT_industrialisation"]
        n108["LIT_join_allies"]
        n109["LIT_join_northern_lights"]
        n110["LIT_join_ussr"]
        n111["LIT_kings_party"]
        n112{"LIT_lithuanian_irridentism"}
        n113["LIT_preparing_for_the_inevitable"]
        n114["LIT_red_estonia"]
        n115["LIT_red_latvia"]
        n116["LIT_reintegrate_lit_minor"]
        n117["LIT_restore_constitutionalism"]
        n118{"LIT_root_out_communists"}
        n119["LIT_socialist_science"]
        n120["LIT_urbanisation"]
    end
    subgraph tier_7["Tier 7"]
        n121["LIT_accept_opposition_in_the_government"]
        n122{"LIT_contain_german_agression"}
        n123["LIT_dissolve_the_klaipda_directorate"]
        n124{"LIT_german_capital"}
        n125["LIT_german_industrial_aid"]
        n126["LIT_join_central_powers"]
        n127["LIT_lithuanian_autarky"]
        n128["LIT_northern_intervention"]
        n129["LIT_research_cooperative"]
        n130["LIT_roman_recognition"]
        n131["LIT_royal_adress"]
        n132["LIT_seek_accommodation_with_germany"]
        n133["LIT_support_the_lkma"]
        n134["LIT_unify_baltics_communist"]
    end
    subgraph tier_8["Tier 8"]
        n135["LIT_ally_france"]
        n136["LIT_ally_italy"]
        n137["LIT_expand_to_markets"]
        n138["LIT_fortify_klaipda"]
        n139["LIT_integrate_lithuanian_rail_network"]
        n140["LIT_join_axis"]
        n141{"LIT_kaunas_conference"}
        n142["LIT_lithuanian_antibolshevik_legions"]
        n143{"LIT_offer_our_enemies_support"}
        n144["LIT_redraft_the_twelve_point_proposal"]
        n145["LIT_reinforce_kaunas_fortress"]
    end
    subgraph tier_9["Tier 9"]
        n146["LIT_germanlithuanian_mutual_assistance_treaty"]
        n147{"LIT_mercedes_benz_engine_plant"}
        n148["LIT_new_noble_class"]
        n149{"LIT_operation_mindaugas"}
        n150{"LIT_r56_demand_vilnius"}
        n151["LIT_sovietlithuanian_mutual_assistance_treaty"]
        n152["LIT_support_domestic_entrepreneurs"]
        n153["LIT_vilnius_procession"]
    end
    subgraph tier_10["Tier 10"]
        n154["LIT_db_six_hundred"]
        n155["LIT_greater_lithuania"]
        n156["LIT_model_capitalist_society"]
        n157["LIT_restore_the_gdl"]
        n158{"LIT_royal_legacy"}
        n159["LIT_skirpas_coup"]
        n160["LIT_three_thousand"]
        n161["LIT_unify_baltics_fascist"]
    end
    subgraph tier_11["Tier 11"]
        n162["LIT_cult_of_vytautas_the_great"]
        n163["LIT_gediminas_heritage"]
        n164["LIT_legacy_of_mindaugas"]
    end
    n76 --> n83
    n118 --> n121
    n55 --> n63
    n57 --> n63
    n122 --> n135
    n122 --> n136
    n42 --> n46
    n62 --> n64
    n54 --> n64
    n88 --> n102
    n60 --> n65
    n89 --> n103
    n100 --> n103
    n60 --> n66
    n76 --> n84
    n54 --> n67
    n112 --> n122
    n49 --> n54
    n101 --> n104
    n158 --> n162
    n147 --> n154
    n42 --> n47
    n102 --> n123
    n44 --> n48
    n82 --> n85
    n82 --> n86
    n46 --> n55
    n76 --> n87
    n58 --> n68
    n58 --> n69
    n71 --> n88
    n63 --> n88
    n68 --> n89
    n60 --> n70
    n55 --> n71
    n57 --> n71
    n57 --> n72
    n124 --> n137
    n41 --> n42
    n86 --> n105
    n51 --> n56
    n47 --> n57
    n123 --> n138
    n158 --> n163
    n74 --> n124
    n111 --> n124
    n104 --> n124
    n117 --> n124
    n106 --> n125
    n95 --> n106
    n98 --> n106
    n143 --> n146
    n150 --> n155
    n149 --> n155
    n44 --> n49
    n53 --> n58
    n52 --> n58
    n51 --> n58
    n84 --> n107
    n124 --> n139
    n60 --> n73
    n64 --> n90
    n79 --> n90
    n86 --> n108
    n132 --> n140
    n111 --> n126
    n104 --> n126
    n76 --> n91
    n77 --> n91
    n86 --> n109
    n91 --> n110
    n131 --> n141
    n126 --> n141
    n101 --> n111
    n50 --> n59
    n41 --> n43
    n75 --> n92
    n158 --> n164
    n62 --> n74
    n93 --> n142
    n126 --> n142
    n103 --> n127
    n93 --> n112
    n139 --> n147
    n69 --> n93
    n68 --> n93
    n152 --> n156
    n94 --> n156
    n55 --> n75
    n58 --> n75
    n59 --> n76
    n144 --> n148
    n112 --> n128
    n121 --> n143
    n123 --> n143
    n112 --> n149
    n141 --> n149
    n59 --> n77
    n86 --> n113
    n78 --> n113
    n43 --> n50
    n74 --> n94
    n69 --> n95
    n78 --> n96
    n112 --> n150
    n141 --> n150
    n48 --> n60
    n99 --> n114
    n99 --> n115
    n77 --> n97
    n131 --> n144
    n130 --> n144
    n45 --> n51
    n45 --> n52
    n62 --> n78
    n121 --> n145
    n99 --> n116
    n62 --> n79
    n54 --> n79
    n62 --> n80
    n54 --> n80
    n108 --> n129
    n105 --> n129
    n109 --> n129
    n101 --> n117
    n150 --> n157
    n149 --> n157
    n45 --> n53
    n111 --> n130
    n104 --> n130
    n117 --> n130
    n88 --> n118
    n111 --> n131
    n104 --> n131
    n117 --> n131
    n153 --> n158
    n148 --> n158
    n112 --> n132
    n69 --> n98
    n146 --> n159
    n54 --> n81
    n83 --> n119
    n41 --> n44
    n143 --> n151
    n77 --> n99
    n54 --> n82
    n46 --> n61
    n47 --> n61
    n137 --> n152
    n111 --> n133
    n104 --> n133
    n117 --> n133
    n68 --> n100
    n49 --> n62
    n147 --> n160
    n114 --> n134
    n115 --> n134
    n150 --> n161
    n149 --> n161
    n84 --> n120
    n141 --> n153
    n41 --> n45
    n66 --> n101
    n65 --> n101
    n121 x--x n123
    n135 x--x n136
    n65 x--x n66
    n122 x--x n132
    n54 x--x n62
    n104 x--x n111
    n104 x--x n117
    n162 x--x n163
    n162 x--x n164
    n154 x--x n160
    n48 x--x n49
    n68 x--x n69
    n137 x--x n139
    n42 x--x n43
    n42 x--x n44
    n42 x--x n45
    n105 x--x n108
    n105 x--x n109
    n163 x--x n164
    n146 x--x n151
    n155 x--x n157
    n155 x--x n161
    n108 x--x n109
    n111 x--x n117
    n43 x--x n44
    n43 x--x n45
    n149 x--x n150
    n157 x--x n161
    n44 x--x n45
```

# LIT_finish_marshalls_reforms

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n165(("LIT_finish_marshalls_reforms"))
    end
    subgraph tier_1["Tier 1"]
        n166["LIT_army_expansion"]
    end
    subgraph tier_2["Tier 2"]
        n167["LIT_army_modernization"]
        n168["LIT_doctrine_effort"]
        n169["LIT_equipment_effort"]
        n170["LIT_fortify_the_border"]
        n171["LIT_prepare_the_mobilization_plans"]
    end
    subgraph tier_3["Tier 3"]
        n172["LIT_doctrine_effort_2"]
        n173["LIT_equipment_effort_2"]
        n174["LIT_equipment_effort_3"]
        n175["LIT_establish_a_armor_corp"]
        n176["LIT_motorization_effort"]
    end
    subgraph tier_4["Tier 4"]
        n177["LIT_expand_the_MAL"]
        n178["LIT_field_hospitals"]
        n179["LIT_mechanization_effort"]
        n180["LIT_signal_companies"]
        n181["LIT_special_forces"]
    end
    subgraph tier_5["Tier 5"]
        n182["LIT_modern_logistics"]
    end
    n165 --> n166
    n166 --> n167
    n166 --> n168
    n168 --> n172
    n166 --> n169
    n169 --> n173
    n169 --> n174
    n167 --> n175
    n172 --> n177
    n176 --> n178
    n166 --> n170
    n175 --> n179
    n176 --> n179
    n178 --> n182
    n179 --> n182
    n180 --> n182
    n167 --> n176
    n166 --> n171
    n175 --> n180
    n174 --> n181
    n172 --> n181
    n173 --> n181
```

# LIT_revive_the_trade_sector

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n183(("LIT_revive_the_trade_sector"))
    end
    subgraph tier_1["Tier 1"]
        n184["LIT_develop_the_fledgling_industry"]
        n185["LIT_long_term_investments"]
        n186["LIT_prepare_the_military_industry"]
        n187["LIT_prepare_the_nations_defences"]
    end
    subgraph tier_2["Tier 2"]
        n188["LIT_all_in"]
        n189["LIT_control_the_exports"]
        n190["LIT_develop_coastal_regions"]
        n191["LIT_develop_the_banks_holdings"]
        n192["LIT_increase_commercialism"]
    end
    subgraph tier_3["Tier 3"]
        n193["LIT_increase_the_currency_value"]
        n194["LIT_lithuanian_industrial_boom"]
    end
    n187 --> n188
    n186 --> n188
    n185 --> n189
    n184 --> n190
    n184 --> n191
    n183 --> n184
    n185 --> n192
    n189 --> n193
    n192 --> n193
    n191 --> n194
    n190 --> n194
    n183 --> n185
    n183 --> n186
    n183 --> n187
```
