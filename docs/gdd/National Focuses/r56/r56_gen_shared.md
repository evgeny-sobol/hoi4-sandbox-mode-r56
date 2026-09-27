# GEN_Aviation_Effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"GEN_Aviation_Effort"}
    end
    subgraph tier_1["Tier 1"]
        n2{"GEN_Foreign_Design"}
        n3["GEN_Own_Design"]
    end
    subgraph tier_2["Tier 2"]
        n4["GEN_Own_Bomber"]
        n5["GEN_Own_Fighter"]
        n6["GEN_Own_Naval_Bomber"]
        n7{"GEN_aircraft_american"}
        n8{"GEN_aircraft_england"}
        n9{"GEN_aircraft_german"}
        n10{"GEN_aircraft_italian"}
        n11{"GEN_aircraft_japanese"}
        n12{"GEN_aircraft_soviet"}
    end
    subgraph tier_3["Tier 3"]
        n13["GEN_Bomber_Competition"]
        n14["GEN_Fighter_Competition"]
        n15["GEN_German_Rocketry"]
        n16["GEN_Own_Air_Doctrine"]
    end
    subgraph tier_4["Tier 4"]
        n17["GEN_Close_Air_Support"]
        n18["GEN_Shared_Air_Doctrine"]
        n19["GEN_aircraft_design_cooperation"]
    end
    n9 --> n13
    n8 --> n13
    n7 --> n13
    n12 --> n13
    n10 --> n13
    n11 --> n13
    n14 --> n17
    n9 --> n14
    n8 --> n14
    n7 --> n14
    n12 --> n14
    n10 --> n14
    n11 --> n14
    n1 --> n2
    n9 --> n15
    n5 --> n16
    n4 --> n16
    n6 --> n16
    n3 --> n4
    n1 --> n3
    n3 --> n5
    n3 --> n6
    n14 --> n18
    n13 --> n18
    n2 --> n7
    n14 --> n19
    n13 --> n19
    n2 --> n8
    n2 --> n9
    n2 --> n10
    n2 --> n11
    n2 --> n12
    n13 x--x n14
    n2 x--x n3
    n7 x--x n8
    n7 x--x n9
    n7 x--x n10
    n7 x--x n11
    n7 x--x n12
    n8 x--x n9
    n8 x--x n10
    n8 x--x n11
    n8 x--x n12
    n9 x--x n10
    n9 x--x n11
    n9 x--x n12
    n10 x--x n11
    n10 x--x n12
    n11 x--x n12
```

# GEN_Naval_Effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20{"GEN_Naval_Effort"}
    end
    subgraph tier_1["Tier 1"]
        n21["GEN_Sea_Dominance"]
        n22["GEN_Small_Navy"]
    end
    subgraph tier_2["Tier 2"]
        n23["GEN_Dockyards"]
        n24["GEN_Study_Ships"]
        n25["GEN_Submarine"]
    end
    subgraph tier_3["Tier 3"]
        n26["GEN_Battleship"]
        n27["GEN_Carrier"]
        n28["GEN_Ships_American"]
        n29["GEN_Ships_England"]
        n30["GEN_stealth_upgrades"]
    end
    subgraph tier_4["Tier 4"]
        n31["GEN_Cruisers"]
        n32["GEN_Destroyer"]
        n33["GEN_Navy_Aircrafts"]
    end
    subgraph tier_5["Tier 5"]
        n34["GEN_Naval_Doctrine"]
    end
    n23 --> n26
    n23 --> n27
    n26 --> n31
    n27 --> n31
    n26 --> n32
    n27 --> n32
    n22 --> n23
    n21 --> n23
    n31 --> n34
    n32 --> n34
    n26 --> n34
    n27 --> n33
    n20 --> n21
    n24 --> n28
    n24 --> n29
    n20 --> n22
    n21 --> n24
    n22 --> n25
    n25 --> n30
    n21 x--x n22
```

# GEN_State_Matter

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35{"GEN_State_Matter"}
    end
    subgraph tier_1["Tier 1"]
        n36{"GEN_Collectivist_Ethos"}
        n37{"GEN_Liberty_Ethos"}
    end
    subgraph tier_2["Tier 2"]
        n38["GEN_Strenghten_Democracy"]
        n39["GEN_Strenghten_Monarchy"]
        n40["internationalism_focus"]
        n41["nationalism_focus"]
    end
    subgraph tier_3["Tier 3"]
        n42{"GEN_Collectivist_Propaganda"}
        n43["GEN_Com_Generals"]
        n44{"GEN_Defence_Act"}
        n45["GEN_Organise_Youth"]
        n46{"militarism"}
    end
    subgraph tier_4["Tier 4"]
        n47["GEN_Conquer"]
        n48["GEN_Intervene"]
        n49["GEN_Isolated"]
        n50["SMI_ideological_consensus"]
        n51["SMI_sideline_the_council"]
        n52{"interventionism_focus"}
        n53{"neutrality_focus"}
    end
    subgraph tier_5["Tier 5"]
        n54["GEN_Anti_Invasion"]
        n55["GEN_Brigades"]
        n56["GEN_Fanaticism"]
        n57["GEN_Forced_Conscription"]
        n58["GEN_Military_Build"]
    end
    subgraph tier_6["Tier 6"]
        n59["why_we_fight"]
    end
    n53 --> n54
    n52 --> n55
    n35 --> n36
    n40 --> n42
    n40 --> n43
    n46 --> n47
    n42 --> n47
    n39 --> n44
    n38 --> n44
    n49 --> n56
    n48 --> n56
    n47 --> n56
    n47 --> n57
    n48 --> n57
    n46 --> n48
    n42 --> n48
    n46 --> n49
    n42 --> n49
    n35 --> n37
    n53 --> n58
    n52 --> n58
    n41 --> n45
    n40 --> n45
    n37 --> n38
    n37 --> n39
    n46 --> n50
    n46 --> n51
    n36 --> n40
    n44 --> n52
    n41 --> n46
    n36 --> n41
    n44 --> n53
    n54 --> n59
    n58 --> n59
    n55 --> n59
    n54 x--x n58
    n36 x--x n37
    n47 x--x n48
    n47 x--x n49
    n48 x--x n49
    n38 x--x n39
    n50 x--x n51
    n40 x--x n41
    n52 x--x n53
```

# GEN_begin_industrial_buildup

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n60(("GEN_begin_industrial_buildup"))
    end
    subgraph tier_1["Tier 1"]
        n61{"GEN_expand_military_capacity"}
        n62["GEN_improve_state_infrastructure"]
    end
    subgraph tier_2["Tier 2"]
        n63["GEN_expand_civilian_manufacturers"]
        n64["GEN_invite_american_investors"]
        n65["GEN_invite_german_investors"]
        n66["GEN_invite_soviet_planners"]
    end
    subgraph tier_3["Tier 3"]
        n67["GEN_american_air_industry_expansion"]
        n68["GEN_automobile_industry"]
        n69["GEN_encorage_foreign_investors"]
        n70["GEN_german_heavy_industry_expansion"]
        n71["GEN_improve_civilian_industry_capacity"]
        n72["GEN_soviet_heavy_industry"]
    end
    subgraph tier_4["Tier 4"]
        n73["GEN_new_schools_and_modern_teaching"]
        n74["GEN_purchase_foreign_licenses"]
        n75["GEN_reveal_mineral_wealth"]
    end
    subgraph tier_5["Tier 5"]
        n76["GEN_focus_on_synthetic_processing"]
        n77["GEN_reform_the_taxes"]
    end
    n64 --> n67
    n64 --> n68
    n65 --> n68
    n66 --> n68
    n64 --> n69
    n65 --> n69
    n66 --> n69
    n62 --> n63
    n60 --> n61
    n75 --> n76
    n73 --> n76
    n65 --> n70
    n63 --> n71
    n60 --> n62
    n61 --> n64
    n61 --> n65
    n61 --> n66
    n71 --> n73
    n67 --> n74
    n70 --> n74
    n72 --> n74
    n75 --> n77
    n71 --> n75
    n66 --> n72
    n64 x--x n65
    n64 x--x n66
    n65 x--x n66
```

# GEN_industrial_boom

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n78(("GEN_industrial_boom"))
    end
    subgraph tier_1["Tier 1"]
        n79["GEN_modernize_railway_system"]
        n80["GEN_nation_wide_industrial_expansion"]
    end
    subgraph tier_2["Tier 2"]
        n81["GEN_modern_electronic_devices"]
    end
    subgraph tier_3["Tier 3"]
        n82["GEN_new_research_complex"]
    end
    n79 --> n81
    n80 --> n81
    n78 --> n79
    n78 --> n80
    n81 --> n82
```
