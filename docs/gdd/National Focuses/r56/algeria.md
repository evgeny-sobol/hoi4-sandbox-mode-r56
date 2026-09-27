# ALG_algeria_liberated

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"ALG_algeria_liberated"}
    end
    subgraph tier_1["Tier 1"]
        n2{"ALG_election"}
        n3{"ALG_peasant_strike"}
    end
    subgraph tier_2["Tier 2"]
        n4["ALG_abbas_victory"]
        n5["ALG_hadj_victory"]
        n6["ALG_new_type_of_nationalism"]
        n7["ALG_the_peasants_republic"]
    end
    subgraph tier_3["Tier 3"]
        n8["ALG_army_loyalty"]
        n9["ALG_depoliticize_the_army"]
        n10["ALG_expand_conscription"]
        n11["ALG_federalize_nation"]
        n12["ALG_german_industries"]
        n13["ALG_seize_production"]
    end
    subgraph tier_4["Tier 4"]
        n14["ALG_british_industrial_investments"]
        n15["ALG_crack_down_on_extremist_groups"]
        n16["ALG_deport_pieds_noir"]
        n17["ALG_malg"]
        n18["ALG_mobolize_reserves"]
        n19["ALG_new_heavy_industries"]
        n20["ALG_promote_atheism"]
        n21["ALG_seize_arms"]
    end
    subgraph tier_5["Tier 5"]
        n22["ALG_algiers_university"]
        n23{"ALG_expand_algeirs_university"}
        n24["ALG_religious_freedom"]
        n25{"ALG_reorginize_industries"}
        n26["ALG_seize_french_guns"]
        n27{"ALG_socialist_science"}
        n28{"ALG_western_technological_learnings"}
    end
    subgraph tier_6["Tier 6"]
        n29["ALG_britain_trade"]
        n30["ALG_comintern_membership"]
        n31{"ALG_hadjs_guidance"}
        n32["ALG_italy_trade"]
        n33["ALG_join_axis"]
        n34["ALG_our_own_path"]
        n35{"ALG_united_under_abbas"}
    end
    subgraph tier_7["Tier 7"]
        n36["ALG_arab_independence"]
        n37["ALG_collaboration_with_allies"]
        n38["ALG_liberate_libya"]
        n39["ALG_liberate_morocco"]
        n40["ALG_turkish_relations"]
    end
    subgraph tier_8["Tier 8"]
        n41["ALG_aid_nuclear_programs"]
        n42["ALG_deterrence"]
        n43["ALG_interventionist_foreign_policy"]
        n44["ALG_secure_suez"]
    end
    subgraph tier_9["Tier 9"]
        n45["ALG_end_france"]
    end
    n2 --> n4
    n37 --> n41
    n17 --> n22
    n31 --> n36
    n35 --> n36
    n4 --> n8
    n25 --> n29
    n28 --> n29
    n9 --> n14
    n31 --> n37
    n35 --> n37
    n27 --> n30
    n9 --> n15
    n5 --> n9
    n8 --> n16
    n40 --> n42
    n1 --> n2
    n44 --> n45
    n43 --> n45
    n42 --> n45
    n19 --> n23
    n18 --> n23
    n6 --> n10
    n7 --> n11
    n6 --> n12
    n2 --> n5
    n24 --> n31
    n28 --> n31
    n36 --> n43
    n25 --> n32
    n28 --> n32
    n23 --> n33
    n30 --> n38
    n33 --> n38
    n34 --> n38
    n30 --> n39
    n33 --> n39
    n34 --> n39
    n8 --> n17
    n10 --> n18
    n12 --> n19
    n3 --> n6
    n27 --> n34
    n23 --> n34
    n1 --> n3
    n11 --> n20
    n15 --> n24
    n16 --> n25
    n39 --> n44
    n38 --> n44
    n13 --> n21
    n21 --> n26
    n18 --> n26
    n7 --> n13
    n21 --> n27
    n20 --> n27
    n3 --> n7
    n31 --> n40
    n35 --> n40
    n25 --> n35
    n22 --> n35
    n14 --> n28
    n4 x--x n5
    n36 x--x n37
    n36 x--x n40
    n29 x--x n32
    n37 x--x n40
    n30 x--x n34
    n2 x--x n3
    n33 x--x n34
    n6 x--x n7
```

# ALG_armed_forces

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46(("ALG_armed_forces"))
    end
    subgraph tier_1["Tier 1"]
        n47["ALG_ANN"]
        n48["ALG_APNAF"]
        n49["ALG_first_air_force"]
    end
    subgraph tier_2["Tier 2"]
        n50["ALG_algiers_port"]
        n51["ALG_develop_air_doctrines"]
        n52["ALG_doctrine_effort"]
        n53["ALG_naval_effort"]
    end
    subgraph tier_3["Tier 3"]
        n54["ALG_air_bases"]
        n55["ALG_bejaia_port"]
        n56["ALG_bousfer_air_factory"]
        n57["ALG_destroyer_effort"]
        n58["ALG_guns_focus"]
        n59["ALG_motorized"]
        n60["ALG_oran_port"]
        n61["ALG_study_ships"]
    end
    subgraph tier_4["Tier 4"]
        n62["ALG_artillery_focus"]
        n63["ALG_cas_focus"]
        n64{"ALG_cruiser_focus"}
        n65["ALG_field_hospitals"]
        n66["ALG_fighter_focus"]
        n67["ALG_french_tanks"]
        n68["ALG_mediterranean_baiston"]
        n69["ALG_signal_companies"]
        n70{"ALG_submarine_focus"}
    end
    subgraph tier_5["Tier 5"]
        n71["ALG_battleship_focus"]
        n72["ALG_bomber_focus"]
        n73["ALG_carrier_focus"]
        n74["ALG_mechanized_focus"]
        n75["ALG_modern_logistics"]
        n76["ALG_radar_focus"]
    end
    subgraph tier_6["Tier 6"]
        n77["ALG_general_staff"]
        n78["ALG_marines"]
        n79["ALG_naval_bomber_focus"]
    end
    subgraph tier_7["Tier 7"]
        n80["ALG_special_forces"]
    end
    n46 --> n47
    n46 --> n48
    n51 --> n54
    n47 --> n50
    n58 --> n62
    n70 --> n71
    n64 --> n71
    n50 --> n55
    n63 --> n72
    n66 --> n72
    n51 --> n56
    n70 --> n73
    n64 --> n73
    n56 --> n63
    n54 --> n63
    n57 --> n64
    n61 --> n64
    n53 --> n57
    n49 --> n51
    n48 --> n52
    n59 --> n65
    n56 --> n66
    n54 --> n66
    n46 --> n49
    n58 --> n67
    n75 --> n77
    n74 --> n77
    n52 --> n58
    n73 --> n78
    n71 --> n78
    n67 --> n74
    n62 --> n74
    n60 --> n68
    n55 --> n68
    n69 --> n75
    n65 --> n75
    n52 --> n59
    n63 --> n79
    n66 --> n79
    n73 --> n79
    n47 --> n53
    n50 --> n60
    n63 --> n76
    n66 --> n76
    n59 --> n69
    n77 --> n80
    n53 --> n61
    n61 --> n70
    n57 --> n70
    n71 x--x n73
```

# ALG_trade_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n81(("ALG_trade_focus"))
    end
    subgraph tier_1["Tier 1"]
        n82["ALG_civ_focus"]
        n83["ALG_mil_focus"]
    end
    subgraph tier_2["Tier 2"]
        n84["ALG_electronics_focus"]
        n85["ALG_infrastructure_focus"]
        n86["ALG_oil_focus"]
        n87["ALG_steel_focus"]
    end
    subgraph tier_3["Tier 3"]
        n88["ALG_civ_focus2"]
        n89["ALG_mil_focus2"]
    end
    subgraph tier_4["Tier 4"]
        n90["ALG_reform_education"]
    end
    n81 --> n82
    n85 --> n88
    n86 --> n88
    n83 --> n84
    n82 --> n85
    n81 --> n83
    n84 --> n89
    n87 --> n89
    n82 --> n86
    n88 --> n90
    n89 --> n90
    n83 --> n87
```
