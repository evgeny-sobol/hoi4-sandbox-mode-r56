# SLO_army_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SLO_army_effort"))
    end
    subgraph tier_1["Tier 1"]
        n2{"SLO_doctrine_effort"}
        n3["SLO_equipment_effort"]
        n4["SLO_motorization_effort"]
        n5["SLO_mountain_brigades"]
    end
    subgraph tier_2["Tier 2"]
        n6["SLO_armor_effort"]
        n7["SLO_firepower_focus"]
        n8["SLO_guerilla_tactics_focus"]
        n9["SLO_invite_german_military_mission"]
        n10["SLO_mass_assault_focus"]
        n11["SLO_mobile_warfare_focus"]
        n12["SLO_planning_focus"]
        n13["SLO_recon_companies"]
        n14["SLO_support_bonus"]
    end
    subgraph tier_3["Tier 3"]
        n15["SLO_artillery_regiments"]
        n16["SLO_mechanization_effort"]
        n17["SLO_modern_artillery"]
        n18["SLO_planning_focus_2"]
        n19["SLO_rapid_deployment_focus"]
        n20["SLO_transfer_german_tanks"]
    end
    subgraph tier_4["Tier 4"]
        n21["SLO_committee_for_military_innovations"]
    end
    subgraph tier_unplaced["Unplaced (cycle)"]
        n22["SLO_special_forces"]
    end
    n4 --> n6
    n7 --> n15
    n22 --> n21
    n17 --> n21
    n18 --> n21
    n15 --> n21
    n16 --> n21
    n19 --> n21
    n1 --> n2
    n1 --> n3
    n2 --> n7
    n2 --> n8
    n2 --> n9
    n2 --> n10
    n6 --> n16
    n9 --> n16
    n11 --> n16
    n2 --> n11
    n14 --> n17
    n1 --> n4
    n1 --> n5
    n2 --> n12
    n12 --> n18
    n10 --> n19
    n8 --> n19
    n5 --> n13
    n4 --> n13
    n5 --> n13
    n5 --> n13
    n13 --> n22
    n3 --> n14
    n5 --> n14
    n6 --> n20
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

# SLO_aviation_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n23{"SLO_aviation_effort"}
    end
    subgraph tier_1["Tier 1"]
        n24["SLO_bomber_focus"]
        n25["SLO_fighter_focus"]
    end
    subgraph tier_2["Tier 2"]
        n26{"SLO_aviation_effort_2"}
        n27{"SLO_form_mechanics"}
    end
    subgraph tier_3["Tier 3"]
        n28["SLO_CAS_effort"]
        n29["SLO_a_new_bomber_focus"]
        n30["SLO_a_new_fighter_focus"]
    end
    n27 --> n28
    n26 --> n28
    n26 --> n29
    n27 --> n29
    n27 --> n30
    n26 --> n30
    n24 --> n26
    n25 --> n26
    n23 --> n24
    n23 --> n25
    n25 --> n27
    n24 --> n27
    n29 x--x n30
    n24 x--x n25
```

# SLO_found_the_nation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n31(("SLO_found_the_nation"))
    end
    subgraph tier_1["Tier 1"]
        n32["SLO_assert_control_over_southern_slovakia"]
        n33["SLO_purge_fascists"]
        n34["SLO_reinforce_hlinka_guard"]
    end
    subgraph tier_2["Tier 2"]
        n35["SLO_agrarian_reforms"]
        n36["SLO_catholic_dominance"]
        n37["SLO_communist_influence"]
        n38["SLO_establish_pluralism"]
        n39["SLO_militarize_the_hlinka_guard"]
        n40["SLO_outlaw_the_communist_party"]
    end
    subgraph tier_3["Tier 3"]
        n41["SLO_crush_dissent"]
        n42["SLO_defensive_preparation"]
        n43["SLO_hlinka_youth"]
        n44["SLO_integrate_german_army_structure"]
        n45["SLO_nationalize_factories"]
        n46["SLO_seek_trading_partners"]
        n47["SLO_state_security_ministry"]
        n48["SLO_supress_the_church"]
    end
    subgraph tier_4["Tier 4"]
        n49["SLO_attract_investors"]
        n50["SLO_efficient_economy"]
        n51["SLO_faithful_ally"]
        n52["SLO_ideological_fanaticism"]
        n53["SLO_indoctrinate_the_proletariat"]
        n54["SLO_purge_the_army"]
        n55["SLO_why_we_fight"]
    end
    subgraph tier_5["Tier 5"]
        n56["SLO_central_planning"]
        n57["SLO_new_army"]
    end
    subgraph tier_6["Tier 6"]
        n58["SLO_technology_sharing"]
    end
    n33 --> n35
    n34 --> n35
    n31 --> n32
    n46 --> n49
    n34 --> n36
    n53 --> n56
    n33 --> n37
    n40 --> n41
    n38 --> n42
    n46 --> n50
    n33 --> n38
    n43 --> n51
    n39 --> n43
    n36 --> n43
    n43 --> n52
    n45 --> n53
    n39 --> n44
    n34 --> n39
    n37 --> n45
    n54 --> n57
    n34 --> n40
    n31 --> n33
    n47 --> n54
    n31 --> n34
    n38 --> n46
    n37 --> n47
    n37 --> n48
    n52 --> n58
    n55 --> n58
    n57 --> n58
    n42 --> n55
```

# SLO_industrial_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n59(("SLO_industrial_effort"))
    end
    subgraph tier_1["Tier 1"]
        n60["SLO_transslovak_railways"]
    end
    subgraph tier_2["Tier 2"]
        n61["SLO_bratislava_industrial_area"]
        n62["SLO_extraction_focus"]
        n63["SLO_small_arms_manufacturing"]
    end
    subgraph tier_3["Tier 3"]
        n64["SLO_apollo_oil_refinery"]
        n65["SLO_support_innovations"]
        n66["SLO_zvolen_railway_factory"]
    end
    subgraph tier_4["Tier 4"]
        n67["SLO_continue_industrialization"]
        n68["SLO_develop_kosice"]
        n69["SLO_uranium_mining"]
    end
    subgraph tier_5["Tier 5"]
        n70["SLO_civilian_developments"]
        n71["SLO_military_developments"]
    end
    n61 --> n64
    n62 --> n64
    n60 --> n61
    n67 --> n70
    n65 --> n67
    n66 --> n67
    n65 --> n68
    n60 --> n62
    n67 --> n71
    n60 --> n63
    n61 --> n65
    n63 --> n65
    n62 --> n65
    n59 --> n60
    n65 --> n69
    n62 --> n69
    n63 --> n66
```

# SLO_naval_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n72{"SLO_naval_effort"}
    end
    subgraph tier_1["Tier 1"]
        n73["SLO_flexible_navy"]
        n74["SLO_large_navy"]
    end
    subgraph tier_2["Tier 2"]
        n75["SLO_cruiser_effort"]
        n76["SLO_submarine_effort"]
    end
    subgraph tier_3["Tier 3"]
        n77["SLO_capital_ships_effort"]
        n78["SLO_destroyer_effort"]
    end
    n75 --> n77
    n74 --> n75
    n73 --> n75
    n76 --> n78
    n72 --> n73
    n72 --> n74
    n73 --> n76
    n74 --> n76
    n73 x--x n74
```
