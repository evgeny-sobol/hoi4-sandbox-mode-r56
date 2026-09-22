# CZE_access_to_the_sea

```mermaid
flowchart TD
    n1(("CZE_access_to_the_sea"))
    n2{"CZE_battleship_catchup_1"}
    n3["CZE_capital_focus"]
    n4{"CZE_cruiser__catchup_1"}
    n5{"CZE_destroyer_catchup_1"}
    n6["CZE_raiding_focus"]
    n7["CZE_shipbuilding_legacy"]
    n8["CZE_sudden_shipyard"]
    n7 --> n2
    n4 --> n3
    n2 --> n3
    n7 --> n4
    n7 --> n5
    n5 --> n6
    n4 --> n6
    n1 --> n7
    n1 --> n8
    n3 x--x n6
```

# CZE_fortification_studies

```mermaid
flowchart TD
    n9["CZE_fallback_line"]
    n10(("CZE_fortification_studies"))
    n11["CZE_hungarian_line"]
    n12["CZE_internal_redoubts"]
    n13["CZE_polish_line"]
    n14["CZE_sudeten_1"]
    n15["CZE_sudeten_2"]
    n16["CZE_sudeten_3"]
    n10 --> n9
    n15 --> n11
    n10 --> n12
    n15 --> n13
    n10 --> n14
    n14 --> n15
    n15 --> n16
```

# CZE_industrial_legacy

```mermaid
flowchart TD
    n17["CZE_arms_exports_1"]
    n18["CZE_arms_exports_2"]
    n19["CZE_arms_exports_3"]
    n20["CZE_balanced_1"]
    n21["CZE_balanced_2"]
    n22["CZE_balanced_3"]
    n23["CZE_favor_czechs_1"]
    n24["CZE_favor_czechs_2"]
    n25["CZE_favor_czechs_3"]
    n26{"CZE_industrial_legacy"}
    n27["CZE_united_population"]
    n26 --> n17
    n17 --> n18
    n18 --> n19
    n26 --> n20
    n20 --> n21
    n21 --> n22
    n26 --> n23
    n23 --> n24
    n24 --> n25
    n22 --> n27
    n20 x--x n23
```

# CZE_military_aeronautical_institute

```mermaid
flowchart TD
    n28["CZE_air_is_our_sea"]
    n29["CZE_cas_focus"]
    n30["CZE_heavy_fighter_focus"]
    n31["CZE_import_foreign_bombers"]
    n32{"CZE_import_foreign_fighters"}
    n33["CZE_light_fighter_focus"]
    n34(("CZE_military_aeronautical_institute"))
    n35["CZE_rule_the_air"]
    n36["CZE_tac_focus"]
    n34 --> n28
    n32 --> n30
    n34 --> n31
    n34 --> n32
    n32 --> n33
    n28 --> n35
    n33 --> n35
    n30 --> n35
    n36 --> n35
    n29 --> n35
    n31 --> n36
    n30 x--x n33
```

# CZE_military_research_institute

```mermaid
flowchart TD
    n37["CZE_armour_bonus_1"]
    n38["CZE_armour_bonus_ii"]
    n39["CZE_doctrine_bonus"]
    n40["CZE_doctrine_bonus_2"]
    n41["CZE_inf_and_artillery_advancement"]
    n42["CZE_inf_and_artillery_advancement_2"]
    n43["CZE_mechanization"]
    n44(("CZE_military_research_institute"))
    n45["CZE_motorization_scheme"]
    n46["CZE_mountain_bonus"]
    n47["CZE_support_bonus"]
    n48["CZE_war_college"]
    n44 --> n37
    n37 --> n38
    n47 --> n39
    n42 --> n39
    n43 --> n40
    n38 --> n40
    n44 --> n41
    n41 --> n42
    n45 --> n43
    n44 --> n45
    n44 --> n46
    n46 --> n47
    n39 --> n48
    n40 --> n48
```

# CZE_political_direction

```mermaid
flowchart TD
    n49["CZE_aggressive_wars"]
    n50["CZE_beacon_of_liberty"]
    n51["CZE_bonus_research_slot_1"]
    n52["CZE_communism_with_a_human_face"]
    n53["CZE_communist_support"]
    n54{"CZE_czech_fascism"}
    n55["CZE_czech_socialism"]
    n56["CZE_defensive_preparations"]
    n57["CZE_democratic_bastion"]
    n58{"CZE_exclude_the_slovaks"}
    n59["CZE_german_ally"]
    n60["CZE_german_minor_ally"]
    n61["CZE_german_puppet"]
    n62["CZE_go_left"]
    n63["CZE_go_right"]
    n64["CZE_hungarian_situation"]
    n65["CZE_join_comintern"]
    n66{"CZE_national_fascism"}
    n67{"CZE_political_direction"}
    n68["CZE_the_polish_division"]
    n69["CZE_the_polish_question"]
    n70["CZE_the_romanian_question"]
    n54 --> n49
    n57 --> n50
    n70 --> n51
    n56 --> n51
    n69 --> n51
    n55 --> n52
    n62 --> n53
    n63 --> n54
    n53 --> n55
    n50 --> n56
    n67 --> n57
    n54 --> n58
    n58 --> n59
    n66 --> n59
    n58 --> n60
    n66 --> n60
    n67 --> n62
    n67 --> n63
    n61 --> n64
    n49 --> n64
    n53 --> n65
    n54 --> n66
    n70 --> n68
    n49 --> n69
    n61 --> n69
    n65 --> n70
    n57 x--x n62
    n57 x--x n63
    n58 x--x n66
    n59 x--x n60
    n59 x--x n61
    n60 x--x n61
    n62 x--x n63
```

# CZE_strategy_decisions

```mermaid
flowchart TD
    n49["CZE_aggressive_wars"]
    n71["CZE_an_entente_of_our_own"]
    n51["CZE_bonus_research_slot_1"]
    n72{"CZE_bonus_research_slot_2"}
    n73["CZE_czechoslovak_legion"]
    n56["CZE_defensive_preparations"]
    n74{"CZE_deliver_sudetenland"}
    n75["CZE_doctrinal_innovation"]
    n59["CZE_german_ally"]
    n76["CZE_german_leanings"]
    n60["CZE_german_minor_ally"]
    n61["CZE_german_puppet"]
    n77["CZE_german_technology"]
    n64["CZE_hungarian_situation"]
    n78["CZE_nukes"]
    n79["CZE_secret_weapons"]
    n80{"CZE_strategy_decisions"}
    n69["CZE_the_polish_question"]
    n70["CZE_the_romanian_question"]
    n81["CZE_trust_in_the_west"]
    n80 --> n71
    n70 --> n51
    n56 --> n51
    n69 --> n51
    n75 --> n72
    n80 --> n73
    n76 --> n74
    n81 --> n75
    n80 --> n76
    n74 --> n61
    n74 --> n77
    n61 --> n64
    n49 --> n64
    n72 --> n78
    n72 --> n79
    n49 --> n69
    n61 --> n69
    n80 --> n81
    n71 x--x n76
    n71 x--x n81
    n59 x--x n61
    n76 x--x n81
    n60 x--x n61
    n78 x--x n79
```

# orphans

```mermaid
flowchart TD
    n82["CZE_deal_with_bulgaria"]
    n83["CZE_deal_with_hungary"]
    n84["CZE_faction_tech_sharing"]
    n85["CZE_invite_romania"]
    n86["CZE_invite_yugoslavia"]
    n87["CZE_rapprochement_with_hungary"]
    n88{"CZE_security_council"}
    n88 --> n82
    n88 --> n83
    n86 --> n84
    n85 --> n84
    n88 --> n87
    n86 --> n88
    n85 --> n88
    n83 x--x n87
```
