# BRA_R56_coffee_crisis_aftermath

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("BRA_R56_coffee_crisis_aftermath"))
    end
    subgraph tier_1["Tier 1"]
        n2["BRA_R56_council_for_economics_and_finances"]
        n3["BRA_R56_federal_institutes"]
        n4["BRA_R56_technical_schools"]
    end
    subgraph tier_2["Tier 2"]
        n5["BRA_R56_expand_the_private_industry"]
        n6["BRA_R56_national_institutes"]
        n7["BRA_R56_nationalize_major_infrastructure_hubs"]
        n8["BRA_R56_polytechnical_colleges"]
        n9["BRA_R56_support_the_itabira_mines"]
    end
    subgraph tier_3["Tier 3"]
        n10["BRA_R56_federal_universities"]
        n11["BRA_R56_legacy_of_martinelli"]
        n12["BRA_R56_modernize_the_madeira_mamore_br230"]
        n13["BRA_R56_plan_salte"]
        n14["BRA_R56_usiminas"]
    end
    subgraph tier_4["Tier 4"]
        n15["BRA_R56_establish_the_commerce_ministry"]
        n16["BRA_R56_federal_economic_bank"]
        n17["BRA_R56_lobato"]
        n18["BRA_R56_matarazzo_united_industries"]
        n19["BRA_R56_modernize_the_sorocabana"]
        n20["BRA_R56_vale_do_rio_doce"]
    end
    subgraph tier_5["Tier 5"]
        n21{"BRA_R56_bndes"}
        n22["BRA_R56_expand_the_universities"]
        n23["BRA_R56_modernize_the_electrical_infrastructure"]
        n24["BRA_R56_national_petroleum_council"]
        n25["BRA_R56_support_heavy_industry_in_sao_paulo"]
    end
    subgraph tier_6["Tier 6"]
        n26["BRA_R56_expand_the_high_voltage_grid"]
        n27["BRA_R56_fiesp"]
        n28["BRA_R56_gerdau"]
        n29["BRA_R56_petrobras"]
        n30["BRA_R56_secret_research_department"]
        n31["BRA_R56_tenenge"]
    end
    subgraph tier_7["Tier 7"]
        n32["BRA_R56_duty_free_zone_of_manaus"]
        n33["BRA_R56_federal_centre_for_nuclear_research"]
        n34["BRA_R56_grande_valley_military_complex"]
        n35["BRA_R56_industrial_innovations"]
    end
    subgraph tier_8["Tier 8"]
        n36["BRA_R56_federal_installations_in_the_amazon"]
        n37["BRA_R56_military_complex_of_the_parana_valley"]
        n38["BRA_R56_the_sugar_belt"]
    end
    subgraph tier_9["Tier 9"]
        n39["BRA_R56_military_complex_of_the_parnaiba_valley"]
        n40["BRA_R56_the_soy_belt"]
    end
    n20 --> n21
    n16 --> n21
    n1 --> n2
    n31 --> n32
    n28 --> n32
    n10 --> n15
    n23 --> n26
    n2 --> n5
    n15 --> n22
    n30 --> n33
    n13 --> n16
    n32 --> n36
    n1 --> n3
    n6 --> n10
    n8 --> n10
    n25 --> n27
    n21 --> n28
    n26 --> n34
    n27 --> n34
    n31 --> n35
    n28 --> n35
    n27 --> n35
    n26 --> n35
    n5 --> n11
    n10 --> n17
    n11 --> n18
    n34 --> n37
    n37 --> n39
    n19 --> n23
    n7 --> n12
    n12 --> n19
    n3 --> n6
    n17 --> n24
    n2 --> n7
    n24 --> n29
    n9 --> n13
    n4 --> n8
    n22 --> n30
    n18 --> n25
    n2 --> n9
    n1 --> n4
    n21 --> n31
    n38 --> n40
    n34 --> n38
    n9 --> n14
    n14 --> n20
    n28 x--x n31
```

# BRA_R56_end_the_occupation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n41(("BRA_R56_end_the_occupation"))
    end
    subgraph tier_1["Tier 1"]
        n42["BRA_R56_national_defense_council"]
    end
    subgraph tier_2["Tier 2"]
        n43["BRA_R56_analyze_the_paulista_war"]
        n44["BRA_R56_construct_the_belem_naval_dockyard"]
        n45["BRA_R56_the_brazilian_air_force"]
    end
    subgraph tier_3["Tier 3"]
        n46["BRA_R56_a_revolta_da_armada"]
        n47["BRA_R56_close_air_support"]
        n48["BRA_R56_eduardo_gomes_doctrine"]
        n49["BRA_R56_florianismo"]
        n50{"BRA_R56_improve_military_education"}
    end
    subgraph tier_4["Tier 4"]
        n51["BRA_R56_encouracados"]
        n52["BRA_R56_minas_gerais_war_doctrine"]
        n53["BRA_R56_ministry_of_aeronautics"]
        n54["BRA_R56_sao_paulos_war_doctrine"]
        n55["BRA_R56_submarines"]
    end
    subgraph tier_5["Tier 5"]
        n56["BRA_R56_imbel"]
        n57["BRA_R56_motorize_the_army"]
        n58["BRA_R56_natal_naval_dockyard"]
    end
    subgraph tier_6["Tier 6"]
        n59["BRA_R56_heavy_artillery"]
        n60["BRA_R56_roll_out_mechanized_vehicles"]
    end
    subgraph tier_7["Tier 7"]
        n61["BRA_R56_shock_and_awe"]
        n62["BRA_R56_stufy_the_war_of_attrition"]
    end
    n44 --> n46
    n42 --> n43
    n45 --> n47
    n42 --> n44
    n45 --> n48
    n46 --> n51
    n49 --> n51
    n44 --> n49
    n56 --> n59
    n52 --> n56
    n43 --> n50
    n50 --> n52
    n48 --> n53
    n47 --> n53
    n54 --> n57
    n51 --> n58
    n55 --> n58
    n41 --> n42
    n57 --> n60
    n50 --> n54
    n60 --> n61
    n59 --> n62
    n46 --> n55
    n49 --> n55
    n42 --> n45
    n52 x--x n54
```

# BRA_R56_the_voice_of_brazil

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n63(("BRA_R56_the_voice_of_brazil"))
    end
    subgraph tier_1["Tier 1"]
        n64["BRA_R56_national_security_law"]
    end
    subgraph tier_2["Tier 2"]
        n65{"BRA_R56_institute_the_polaca"}
    end
    subgraph tier_3["Tier 3"]
        n66{"BRA_R56_embrace_populism"}
        n67["BRA_R56_restore_the_empire"]
        n68{"BRA_R56_strengthen_local_governments"}
    end
    subgraph tier_4["Tier 4"]
        n69["BRA_R56_a_collection_of_states"]
        n70["BRA_R56_department_of_press_and_propaganda"]
        n71["BRA_R56_the_brazilian_action"]
        n72["BRA_R56_the_second_communist_putsch"]
    end
    subgraph tier_5["Tier 5"]
        n73["BRA_R56_non_dvcor_dvco"]
        n74["BRA_R56_skewer_the_green_hens"]
        n75["BRA_R56_the_estado_novo"]
        n76["BRA_R56_the_october_manifesto"]
    end
    subgraph tier_6["Tier 6"]
        n77["BRA_R56_embolden_patriotism"]
        n78["BRA_R56_reinstituite_the_technocratic_system"]
        n79["BRA_R56_the_integral_state"]
        n80["BRA_R56_under_a_single_banner"]
    end
    subgraph tier_7["Tier 7"]
        n81["BRA_R56_tire_de_guerra"]
    end
    subgraph tier_8["Tier 8"]
        n82["BRA_R56_a_new_federal_capital_brasilia"]
        n83["BRA_R56_the_brazilian_expeditionary_force"]
    end
    n68 --> n69
    n81 --> n82
    n79 --> n82
    n66 --> n70
    n75 --> n77
    n65 --> n66
    n64 --> n65
    n63 --> n64
    n69 --> n73
    n73 --> n78
    n65 --> n67
    n72 --> n74
    n65 --> n68
    n68 --> n71
    n81 --> n83
    n70 --> n75
    n76 --> n79
    n71 --> n76
    n66 --> n72
    n77 --> n81
    n78 --> n81
    n67 --> n81
    n79 --> n81
    n80 --> n81
    n74 --> n80
    n69 x--x n71
    n70 x--x n72
    n66 x--x n67
    n66 x--x n68
    n67 x--x n68
```

# bra_diplomacia

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n84{"bra_diplomacia"}
    end
    subgraph tier_1["Tier 1"]
        n85{"bra_amigo_eua"}
        n86{"bra_inimigo_eua"}
    end
    subgraph tier_2["Tier 2"]
        n87["BRA_take_uruguay"]
        n88{"bra_amigo_alemanha"}
        n89["bra_amigo_aliados"]
        n90["bra_amigo_urss"]
        n91["bra_mercosul_focus"]
        n92["bra_sem_urss"]
        n93{"bra_transatlantico"}
    end
    subgraph tier_3["Tier 3"]
        n94["bra_african_initiative"]
        n95["bra_amigo_argentina"]
        n96["bra_amigo_portugal"]
        n97["bra_amigo_uk"]
        n98["bra_carribean_diplomacy"]
        n99["bra_eixo"]
        n100["bra_invite_canada"]
        n101["bra_invite_south_africa"]
        n102["bra_mercosul_militar_focus"]
        n103["bra_naval_logistics"]
        n104["bra_pan_americano"]
        n105["bra_sem_eixo"]
        n106["bra_shared_naval_experience"]
    end
    subgraph tier_4["Tier 4"]
        n107["BRA_allies_in_the_north"]
        n108["BRA_invite_andean_countries"]
        n109["BRA_invite_platine_countries"]
        n110["bra_a_s_warfare"]
        n111["bra_foro_de_sao_paulo_focus"]
        n112["bra_liga_nacoes"]
        n113["bra_strike_dem_focus"]
    end
    subgraph tier_5["Tier 5"]
        n114["BRA_ideological_propaganda"]
        n115["BRA_international_volunteers"]
        n116["BRA_invite_central_american_countries"]
        n117["bra_cuba_rev"]
        n118["bra_mercosul_expansao_focus"]
        n119["bra_pan_americano_fascism"]
    end
    subgraph tier_6["Tier 6"]
        n120["bra_mex_rev"]
    end
    subgraph tier_7["Tier 7"]
        n121["bra_basta"]
    end
    n102 --> n107
    n111 --> n114
    n111 --> n115
    n113 --> n115
    n102 --> n108
    n107 --> n116
    n102 --> n109
    n86 --> n87
    n106 --> n110
    n93 --> n94
    n86 --> n88
    n85 --> n89
    n93 --> n95
    n84 --> n85
    n93 --> n96
    n89 --> n97
    n86 --> n90
    n120 --> n121
    n117 --> n121
    n93 --> n98
    n111 --> n117
    n88 --> n99
    n104 --> n111
    n84 --> n86
    n93 --> n100
    n93 --> n101
    n97 --> n112
    n109 --> n118
    n108 --> n118
    n107 --> n118
    n85 --> n91
    n91 --> n102
    n119 --> n120
    n93 --> n103
    n89 --> n103
    n92 --> n104
    n90 --> n104
    n113 --> n119
    n88 --> n105
    n86 --> n92
    n93 --> n106
    n105 --> n113
    n99 --> n113
    n85 --> n93
    n94 x--x n101
    n88 x--x n90
    n88 x--x n92
    n89 x--x n91
    n89 x--x n93
    n85 x--x n86
    n90 x--x n92
    n99 x--x n105
    n91 x--x n93
```
