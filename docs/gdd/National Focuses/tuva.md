# TAN_Industrial_Start

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("TAN_Industrial_Start"))
    end
    subgraph tier_1["Tier 1"]
        n2{"TAN_Military_Buildup"}
        n3["TAN_gold_mining"]
        n4["TAN_increase_sedentarization"]
    end
    subgraph tier_2["Tier 2"]
        n5["TAN_Civilian_One"]
        n6["TAN_Invite_American"]
        n7["TAN_Invite_Japanese"]
        n8["TAN_Invite_Soviets"]
        n9["TAN_exploit_the_ulugh_khem_coal_basin"]
    end
    subgraph tier_3["Tier 3"]
        n10["TAN_American_Air"]
        n11["TAN_Automobile"]
        n12["TAN_Civilian_Two"]
        n13["TAN_Futher_Investments"]
        n14["TAN_Japanese_Heavy"]
        n15["TAN_Soviet_Heavy_Industry"]
    end
    subgraph tier_4["Tier 4"]
        n16["TAN_Excavation"]
        n17["TAN_Licences"]
        n18["TAN_Research"]
    end
    subgraph tier_5["Tier 5"]
        n19["TAN_Autarky"]
        n20["TAN_Refinery"]
        n21["TAN_coal_based_industry"]
    end
    subgraph tier_6["Tier 6"]
        n22["TAN_uranium_discovery"]
    end
    n6 --> n10
    n16 --> n19
    n6 --> n11
    n7 --> n11
    n8 --> n11
    n4 --> n5
    n5 --> n12
    n12 --> n16
    n3 --> n16
    n6 --> n13
    n7 --> n13
    n8 --> n13
    n2 --> n6
    n2 --> n7
    n2 --> n8
    n7 --> n14
    n10 --> n17
    n14 --> n17
    n15 --> n17
    n1 --> n2
    n16 --> n20
    n18 --> n20
    n12 --> n18
    n8 --> n15
    n16 --> n21
    n9 --> n21
    n3 --> n9
    n1 --> n3
    n1 --> n4
    n19 --> n22
    n21 --> n22
    n6 x--x n7
    n6 x--x n8
    n7 x--x n8
```

# TAN_State_Matter

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n23{"TAN_State_Matter"}
    end
    subgraph tier_1["Tier 1"]
        n24{"TAN_Collectivist_Ethos"}
        n25{"TAN_Liberty_Ethos"}
    end
    subgraph tier_2["Tier 2"]
        n26["TAN_Strenghten_Democracy"]
        n27["TAN_case_of_the_nine"]
        n28["TAN_gather_the_party_opposition"]
        n29["TAN_rehabilitate_pre_revolutionary_practices"]
        n30["TAN_tuvan_nationalism"]
    end
    subgraph tier_3["Tier 3"]
        n31["TAN_Collectivist_Propaganda"]
        n32["TAN_Com_Generals"]
        n33{"TAN_Defence_Act"}
        n34["TAN_Organise_Youth"]
        n35{"TAN_militarism"}
        n36["TAN_restore_monastic_prerogatives"]
        n37["TAN_restore_our_ways"]
    end
    subgraph tier_4["Tier 4"]
        n38{"TAN_interventionism_focus"}
        n39{"TAN_neutrality_focus"}
        n40["TAN_red_army"]
        n41{"TAN_the_basis_of_the_economy"}
        n42{"TAN_the_fifth_constitution"}
    end
    subgraph tier_5["Tier 5"]
        n43["TAN_Anti_Invasion"]
        n44["TAN_Brigades"]
        n45["TAN_Conquer"]
        n46["TAN_Intervene"]
        n47["TAN_Isolated"]
        n48["TAN_Military_Build"]
        n49["TAN_carry_the_altai_torch"]
        n50["TAN_indoctrination_focus"]
        n51["TAN_sovietization"]
    end
    subgraph tier_6["Tier 6"]
        n52["TAN_Fanaticism"]
        n53["TAN_Forced_Conscription"]
        n54["TAN_adopt_nichirenist_principles"]
        n55["TAN_bolster_altai_economy"]
        n56["TAN_refuge_for_the_tofalar"]
        n57["TAN_why_we_fight"]
    end
    subgraph tier_7["Tier 7"]
        n58["TAN_appropriate_the_gokturks"]
        n59["TAN_mobilize_for_a_holy_war"]
    end
    subgraph tier_8["Tier 8"]
        n60["TAN_rectify_the_darkhad_valley_transfer"]
    end
    n39 --> n43
    n38 --> n44
    n23 --> n24
    n27 --> n31
    n27 --> n32
    n28 --> n32
    n35 --> n45
    n42 --> n45
    n41 --> n45
    n29 --> n33
    n26 --> n33
    n47 --> n52
    n46 --> n52
    n45 --> n52
    n45 --> n53
    n46 --> n53
    n35 --> n46
    n42 --> n46
    n41 --> n46
    n35 --> n47
    n42 --> n47
    n41 --> n47
    n23 --> n25
    n39 --> n48
    n38 --> n48
    n30 --> n34
    n27 --> n34
    n28 --> n34
    n25 --> n26
    n36 --> n54
    n45 --> n54
    n52 --> n58
    n49 --> n55
    n26 --> n49
    n38 --> n49
    n24 --> n27
    n24 --> n28
    n42 --> n50
    n41 --> n50
    n33 --> n38
    n30 --> n35
    n54 --> n59
    n33 --> n39
    n45 --> n60
    n59 --> n60
    n32 --> n40
    n49 --> n56
    n25 --> n29
    n29 --> n36
    n26 --> n36
    n28 --> n37
    n42 --> n51
    n37 --> n41
    n31 --> n42
    n24 --> n30
    n43 --> n57
    n48 --> n57
    n44 --> n57
    n43 x--x n48
    n24 x--x n25
    n45 x--x n46
    n45 x--x n47
    n46 x--x n47
    n26 x--x n29
    n27 x--x n28
    n27 x--x n30
    n28 x--x n30
    n38 x--x n39
```

# TAN_call_for_army_readiness

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61(("TAN_call_for_army_readiness"))
    end
    subgraph tier_1["Tier 1"]
        n62["TAN_army_reform"]
        n63["TAN_cavalry_tradition"]
        n64["TAN_winter_training"]
    end
    subgraph tier_2["Tier 2"]
        n65["TAN_establish_the_ministry_of_war"]
    end
    subgraph tier_3["Tier 3"]
        n66{"TAN_army_modernization"}
        n67["TAN_equipment_effort"]
    end
    subgraph tier_4["Tier 4"]
        n68["TAN_equipment_effort_2"]
        n69["TAN_equipment_effort_3"]
        n70["TAN_establish_a_armor_corp"]
        n71["TAN_mechanization_effort"]
        n72["TAN_scavenge_battlefield_equipment"]
        n73["TAN_uphold_the_cavalry_primacy"]
    end
    subgraph tier_5["Tier 5"]
        n74["TAN_field_hospitals"]
        n75["TAN_signal_companies"]
        n76["TAN_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n77["TAN_improve_officer_training_formation"]
        n78["TAN_modern_logistics"]
    end
    subgraph tier_7["Tier 7"]
        n79["TAN_winter_readiness"]
    end
    n65 --> n66
    n61 --> n62
    n61 --> n63
    n65 --> n67
    n67 --> n68
    n67 --> n69
    n66 --> n70
    n62 --> n65
    n64 --> n65
    n63 --> n65
    n71 --> n74
    n73 --> n74
    n70 --> n74
    n75 --> n77
    n66 --> n71
    n74 --> n78
    n75 --> n78
    n67 --> n72
    n66 --> n72
    n70 --> n75
    n71 --> n75
    n73 --> n75
    n69 --> n76
    n68 --> n76
    n66 --> n73
    n76 --> n79
    n77 --> n79
    n78 --> n79
    n61 --> n64
    n70 x--x n71
    n70 x--x n73
    n71 x--x n73
```

# TAN_tuva_annex_ussr

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n80(("TAN_tuva_annex_ussr"))
    end
```
