# PAK_Birth_of_a_Nation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"PAK_Birth_of_a_Nation"}
    end
    subgraph tier_1["Tier 1"]
        n2{"PAK_General_Election"}
        n3{"PAK_Organize_a_Coup"}
    end
    subgraph tier_2["Tier 2"]
        n4["PAK_Cement_Leaders_Rule"]
        n5["PAK_Communist_Revolution"]
        n6["PAK_Fascist_Coup_d_etat"]
        n7["PAK_Multipartism"]
    end
    subgraph tier_3["Tier 3"]
        n8["PAK_Allah_and_State"]
        n9["PAK_Crack_down_on_Socialist_Protests"]
        n10["PAK_Encourage_Protectionism"]
        n11["PAK_Land_Reform"]
        n12["PAK_Secularism"]
        n13["PAK_Unite_the_Proletariat"]
    end
    subgraph tier_4["Tier 4"]
        n14{"PAK_A_Federal_Pakistan"}
        n15["PAK_Ally_the_High_Command"]
        n16{"PAK_Assure_Loyalty_in_the_Army"}
        n17["PAK_Cement_Freedom_of_Speech"]
        n18["PAK_Collectivisation"]
        n19["PAK_Family_Programs"]
        n20{"PAK_Militarism"}
        n21["PAK_Pakistani_Nationalism"]
        n22{"PAK_Seize_Royal_Assets"}
    end
    subgraph tier_5["Tier 5"]
        n23["PAK_Align_Japan"]
        n24["PAK_Align_the_Soviet_Union"]
        n25["PAK_Attract_Foreign_Investement"]
        n26["PAK_Economic_Planning"]
        n27["PAK_Increase_Police_Budget"]
        n28["PAK_Our_Own_Path"]
        n29["PAK_Rebalance_the_Military_Budget"]
        n30["PAK_Rely_on_the_Trade_Unions"]
        n31["PAK_War_Propaganda"]
        n32["PAK_Work_for_Pakistan"]
    end
    subgraph tier_6["Tier 6"]
        n33["PAK_Centralise_Power"]
        n34["PAK_Curb_Extremists_Influence"]
        n35["PAK_Economic_Cooperation"]
        n36["PAK_International_Diplomcay"]
        n37["PAK_Ministry_of_Truth"]
        n38["PAK_Muslim_Diplomacy"]
        n39["PAK_Muslim_Unity"]
        n40["PAK_The_Graveyard_of_Empires"]
        n41["PAK_Workers_Culture"]
    end
    subgraph tier_7["Tier 7"]
        n42["PAK_Down_with_Persia"]
        n43["PAK_Into_India"]
    end
    subgraph tier_8["Tier 8"]
        n44["PAK_Into_the_Steppes"]
    end
    n13 --> n14
    n20 --> n23
    n16 --> n23
    n14 --> n24
    n22 --> n24
    n4 --> n8
    n8 --> n15
    n9 --> n16
    n17 --> n25
    n12 --> n17
    n2 --> n4
    n27 --> n33
    n11 --> n18
    n3 --> n5
    n6 --> n9
    n25 --> n34
    n29 --> n34
    n40 --> n42
    n24 --> n35
    n23 --> n35
    n28 --> n35
    n18 --> n26
    n6 --> n10
    n12 --> n19
    n3 --> n6
    n1 --> n2
    n16 --> n27
    n20 --> n27
    n25 --> n36
    n29 --> n36
    n40 --> n43
    n43 --> n44
    n42 --> n44
    n5 --> n11
    n10 --> n20
    n26 --> n37
    n30 --> n37
    n2 --> n7
    n32 --> n38
    n31 --> n38
    n32 --> n39
    n31 --> n39
    n1 --> n3
    n20 --> n28
    n14 --> n28
    n8 --> n21
    n19 --> n29
    n22 --> n30
    n18 --> n30
    n7 --> n12
    n13 --> n22
    n24 --> n40
    n23 --> n40
    n28 --> n40
    n5 --> n13
    n15 --> n31
    n21 --> n31
    n21 --> n32
    n30 --> n41
    n23 x--x n28
    n24 x--x n28
    n4 x--x n7
    n5 x--x n6
    n2 x--x n3
```

# PAK_Infrastructure_Along_the_Indus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n45(("PAK_Infrastructure_Along_the_Indus"))
    end
    subgraph tier_1["Tier 1"]
        n46["PAK_Education_Reform"]
        n47["PAK_Expand_the_Cities"]
    end
    subgraph tier_2["Tier 2"]
        n48["PAK_Electrical_Research"]
        n49["PAK_Expand_Heavy_Industries"]
        n50["PAK_Expand_Industrial_Complexes"]
    end
    subgraph tier_3["Tier 3"]
        n51["PAK_Computer_Research"]
        n52["PAK_Construction_Research"]
        n53["PAK_Industrial_Research"]
        n54["PAK_Production_Research"]
        n55["PAK_Radio_Research"]
    end
    subgraph tier_4["Tier 4"]
        n56["PAK_Further_Expand_Heavy_Industries"]
        n57["PAK_Further_Expand_Industrial_Complexes"]
        n58["PAK_Nuclear_Research"]
    end
    subgraph tier_5["Tier 5"]
        n59["PAK_Build_Radar_Stations"]
        n60["PAK_Build_Refineries"]
    end
    n55 --> n59
    n56 --> n59
    n52 --> n60
    n57 --> n60
    n48 --> n51
    n50 --> n52
    n45 --> n46
    n46 --> n48
    n47 --> n49
    n47 --> n50
    n45 --> n47
    n49 --> n56
    n54 --> n56
    n52 --> n56
    n53 --> n57
    n52 --> n57
    n50 --> n57
    n49 --> n53
    n50 --> n53
    n51 --> n58
    n55 --> n58
    n49 --> n54
    n46 --> n54
    n48 --> n55
```

# PAK_Pakistan_Armed_Forces

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61(("PAK_Pakistan_Armed_Forces"))
    end
    subgraph tier_1["Tier 1"]
        n62["PAK_Form_the_Air_Force"]
        n63["PAK_Form_the_Navy"]
        n64["PAK_Reform_the_Army"]
    end
    subgraph tier_2["Tier 2"]
        n65["PAK_Airbase_Expansion"]
        n66{"PAK_Central_Planning_Commision"}
        n67["PAK_Coast_Protection"]
        n68{"PAK_New_Artillery_Foundries"}
        n69["PAK_New_Fighter_Designs"]
        n70["PAK_Think_Big"]
    end
    subgraph tier_3["Tier 3"]
        n71["PAK_Fall_back_on_the_Great_War"]
        n72{"PAK_Foreign_Equipment"}
        n73["PAK_Frigate_Based_Navy"]
        n74{"PAK_Ground_To_Air_Facilities"}
        n75{"PAK_Invite_International_Experts"}
        n76{"PAK_Local_Arms_Developement"}
        n77["PAK_Radically_Different_Tactics"]
        n78["PAK_Submarine_Support"]
    end
    subgraph tier_4["Tier 4"]
        n79["PAK_Bauxite_Mines"]
        n80["PAK_Dicipline_Training"]
        n81["PAK_Marines"]
        n82["PAK_Naval_Bombers"]
        n83["PAK_Steel_Mines"]
    end
    n62 --> n65
    n74 --> n79
    n75 --> n79
    n64 --> n66
    n63 --> n67
    n77 --> n80
    n71 --> n80
    n66 --> n71
    n68 --> n72
    n61 --> n62
    n61 --> n63
    n67 --> n73
    n65 --> n74
    n69 --> n75
    n68 --> n76
    n73 --> n81
    n75 --> n82
    n73 --> n82
    n64 --> n68
    n62 --> n69
    n66 --> n77
    n61 --> n64
    n76 --> n83
    n72 --> n83
    n70 --> n78
    n63 --> n70
    n79 x--x n83
    n71 x--x n77
    n72 x--x n76
```
