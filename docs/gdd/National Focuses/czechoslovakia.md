# CZE_access_to_the_sea

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CZE_access_to_the_sea"))
    end
    subgraph tier_1["Tier 1"]
        n2["CZE_shipbuilding_legacy"]
        n3["CZE_sudden_shipyard"]
    end
    subgraph tier_2["Tier 2"]
        n4{"CZE_battleship_catchup_1"}
        n5{"CZE_cruiser__catchup_1"}
        n6{"CZE_destroyer_catchup_1"}
    end
    subgraph tier_3["Tier 3"]
        n7["CZE_capital_focus"]
        n8["CZE_raiding_focus"]
    end
    n2 --> n4
    n5 --> n7
    n4 --> n7
    n2 --> n5
    n2 --> n6
    n6 --> n8
    n5 --> n8
    n1 --> n2
    n1 --> n3
    n7 x--x n8
```

# CZE_fortification_studies

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n9(("CZE_fortification_studies"))
    end
    subgraph tier_1["Tier 1"]
        n10["CZE_fallback_line"]
        n11["CZE_internal_redoubts"]
        n12["CZE_sudeten_1"]
    end
    subgraph tier_2["Tier 2"]
        n13["CZE_sudeten_2"]
    end
    subgraph tier_3["Tier 3"]
        n14["CZE_hungarian_line"]
        n15["CZE_polish_line"]
        n16["CZE_sudeten_3"]
    end
    n9 --> n10
    n13 --> n14
    n9 --> n11
    n13 --> n15
    n9 --> n12
    n12 --> n13
    n13 --> n16
```

# CZE_industrial_legacy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"CZE_industrial_legacy"}
    end
    subgraph tier_1["Tier 1"]
        n18["CZE_arms_exports_1"]
        n19["CZE_balanced_1"]
        n20["CZE_favor_czechs_1"]
    end
    subgraph tier_2["Tier 2"]
        n21["CZE_arms_exports_2"]
        n22["CZE_balanced_2"]
        n23["CZE_favor_czechs_2"]
    end
    subgraph tier_3["Tier 3"]
        n24["CZE_arms_exports_3"]
        n25["CZE_balanced_3"]
        n26["CZE_favor_czechs_3"]
    end
    subgraph tier_4["Tier 4"]
        n27["CZE_united_population"]
    end
    n17 --> n18
    n18 --> n21
    n21 --> n24
    n17 --> n19
    n19 --> n22
    n22 --> n25
    n17 --> n20
    n20 --> n23
    n23 --> n26
    n25 --> n27
    n19 x--x n20
```

# CZE_military_aeronautical_institute

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28["CZE_cas_focus"]
        n29(("CZE_military_aeronautical_institute"))
    end
    subgraph tier_1["Tier 1"]
        n30["CZE_air_is_our_sea"]
        n31["CZE_import_foreign_bombers"]
        n32{"CZE_import_foreign_fighters"}
    end
    subgraph tier_2["Tier 2"]
        n33["CZE_heavy_fighter_focus"]
        n34["CZE_light_fighter_focus"]
        n35["CZE_tac_focus"]
    end
    subgraph tier_3["Tier 3"]
        n36["CZE_rule_the_air"]
    end
    n29 --> n30
    n32 --> n33
    n29 --> n31
    n29 --> n32
    n32 --> n34
    n30 --> n36
    n34 --> n36
    n33 --> n36
    n35 --> n36
    n28 --> n36
    n31 --> n35
    n33 x--x n34
```

# CZE_military_research_institute

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n37(("CZE_military_research_institute"))
    end
    subgraph tier_1["Tier 1"]
        n38["CZE_armour_bonus_1"]
        n39["CZE_inf_and_artillery_advancement"]
        n40["CZE_motorization_scheme"]
        n41["CZE_mountain_bonus"]
    end
    subgraph tier_2["Tier 2"]
        n42["CZE_armour_bonus_ii"]
        n43["CZE_inf_and_artillery_advancement_2"]
        n44["CZE_mechanization"]
        n45["CZE_support_bonus"]
    end
    subgraph tier_3["Tier 3"]
        n46["CZE_doctrine_bonus"]
        n47["CZE_doctrine_bonus_2"]
    end
    subgraph tier_4["Tier 4"]
        n48["CZE_war_college"]
    end
    n37 --> n38
    n38 --> n42
    n45 --> n46
    n43 --> n46
    n44 --> n47
    n42 --> n47
    n37 --> n39
    n39 --> n43
    n40 --> n44
    n37 --> n40
    n37 --> n41
    n41 --> n45
    n46 --> n48
    n47 --> n48
```

# CZE_political_direction

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n49["CZE_german_puppet"]
        n50{"CZE_political_direction"}
    end
    subgraph tier_1["Tier 1"]
        n51["CZE_democratic_bastion"]
        n52["CZE_go_left"]
        n53["CZE_go_right"]
    end
    subgraph tier_2["Tier 2"]
        n54["CZE_beacon_of_liberty"]
        n55["CZE_communist_support"]
        n56{"CZE_czech_fascism"}
    end
    subgraph tier_3["Tier 3"]
        n57["CZE_aggressive_wars"]
        n58["CZE_czech_socialism"]
        n59["CZE_defensive_preparations"]
        n60{"CZE_exclude_the_slovaks"}
        n61["CZE_join_comintern"]
        n62{"CZE_national_fascism"}
    end
    subgraph tier_4["Tier 4"]
        n63["CZE_communism_with_a_human_face"]
        n64["CZE_german_ally"]
        n65["CZE_german_minor_ally"]
        n66["CZE_hungarian_situation"]
        n67["CZE_the_polish_question"]
        n68["CZE_the_romanian_question"]
    end
    subgraph tier_5["Tier 5"]
        n69["CZE_bonus_research_slot_1"]
        n70["CZE_the_polish_division"]
    end
    n56 --> n57
    n51 --> n54
    n68 --> n69
    n59 --> n69
    n67 --> n69
    n58 --> n63
    n52 --> n55
    n53 --> n56
    n55 --> n58
    n54 --> n59
    n50 --> n51
    n56 --> n60
    n60 --> n64
    n62 --> n64
    n60 --> n65
    n62 --> n65
    n50 --> n52
    n50 --> n53
    n49 --> n66
    n57 --> n66
    n55 --> n61
    n56 --> n62
    n68 --> n70
    n57 --> n67
    n49 --> n67
    n61 --> n68
    n51 x--x n52
    n51 x--x n53
    n60 x--x n62
    n64 x--x n65
    n64 x--x n49
    n65 x--x n49
    n52 x--x n53
```

# CZE_strategy_decisions

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n57["CZE_aggressive_wars"]
        n59["CZE_defensive_preparations"]
        n64["CZE_german_ally"]
        n65["CZE_german_minor_ally"]
        n71{"CZE_strategy_decisions"}
        n68["CZE_the_romanian_question"]
    end
    subgraph tier_1["Tier 1"]
        n72["CZE_an_entente_of_our_own"]
        n73["CZE_czechoslovak_legion"]
        n74["CZE_german_leanings"]
        n75["CZE_trust_in_the_west"]
    end
    subgraph tier_2["Tier 2"]
        n76{"CZE_deliver_sudetenland"}
        n77["CZE_doctrinal_innovation"]
    end
    subgraph tier_3["Tier 3"]
        n78{"CZE_bonus_research_slot_2"}
        n49["CZE_german_puppet"]
        n79["CZE_german_technology"]
    end
    subgraph tier_4["Tier 4"]
        n66["CZE_hungarian_situation"]
        n80["CZE_nukes"]
        n81["CZE_secret_weapons"]
        n67["CZE_the_polish_question"]
    end
    subgraph tier_5["Tier 5"]
        n69["CZE_bonus_research_slot_1"]
    end
    n71 --> n72
    n68 --> n69
    n59 --> n69
    n67 --> n69
    n77 --> n78
    n71 --> n73
    n74 --> n76
    n75 --> n77
    n71 --> n74
    n76 --> n49
    n76 --> n79
    n49 --> n66
    n57 --> n66
    n78 --> n80
    n78 --> n81
    n57 --> n67
    n49 --> n67
    n71 --> n75
    n72 x--x n74
    n72 x--x n75
    n64 x--x n49
    n74 x--x n75
    n65 x--x n49
    n80 x--x n81
```

# orphans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n82["CZE_invite_romania"]
        n83["CZE_invite_yugoslavia"]
    end
    subgraph tier_1["Tier 1"]
        n84["CZE_faction_tech_sharing"]
        n85{"CZE_security_council"}
    end
    subgraph tier_2["Tier 2"]
        n86["CZE_deal_with_bulgaria"]
        n87["CZE_deal_with_hungary"]
        n88["CZE_rapprochement_with_hungary"]
    end
    n85 --> n86
    n85 --> n87
    n83 --> n84
    n82 --> n84
    n85 --> n88
    n83 --> n85
    n82 --> n85
    n87 x--x n88
```
