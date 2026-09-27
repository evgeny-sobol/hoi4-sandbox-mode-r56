# SER_build_the_nation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SER_build_the_nation"))
    end
    subgraph tier_1["Tier 1"]
        n2["SER_construction_effort"]
        n3["SER_infrastructure_effort"]
        n4["SER_research_collaboration"]
    end
    subgraph tier_2["Tier 2"]
        n5["SER_production_effort"]
        n6["SER_prospect_for_resources"]
    end
    subgraph tier_3["Tier 3"]
        n7["SER_develop_steel_deposits"]
        n8["SER_expand_the_university_of_belgrade"]
        n9["SER_extract_aluminium"]
        n10["SER_production_effort_2"]
    end
    subgraph tier_4["Tier 4"]
        n11["SER_develop_macedonia"]
        n12["SER_extra_tech_slot_2"]
        n13["SER_industrial_planning"]
    end
    subgraph tier_5["Tier 5"]
        n14["SER_construction_effort_2"]
        n15["SER_create_skopje_arsenals"]
    end
    subgraph tier_6["Tier 6"]
        n16["SER_nuclear_effort"]
    end
    n1 --> n2
    n13 --> n14
    n11 --> n15
    n13 --> n15
    n8 --> n11
    n6 --> n7
    n3 --> n8
    n5 --> n8
    n8 --> n12
    n6 --> n9
    n8 --> n13
    n1 --> n3
    n14 --> n16
    n2 --> n5
    n5 --> n10
    n3 --> n6
    n1 --> n4
```

# SER_political_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17(("SER_political_effort"))
    end
    subgraph tier_1["Tier 1"]
        n18["SER_form_peasant_councils"]
        n19{"SER_liberty_ethos"}
        n20["SER_nationalism_focus"]
    end
    subgraph tier_2["Tier 2"]
        n21{"SER_belgrade_investments_focus"}
        n22["SER_economic_centralization"]
        n23["SER_local_militias"]
        n24["SER_militarism"]
        n25["SER_recreate_yugoslavia"]
        n26["SER_saviour_of_serbia"]
        n27{"SER_trading_infrastructures"}
    end
    subgraph tier_3["Tier 3"]
        n28{"SER_economic_optimization"}
        n29{"SER_industrial_support"}
        n30["SER_join_axis"]
        n31["SER_military_youth"]
        n32["SER_nationalize_factories"]
        n33["SER_political_commissars"]
        n34["SER_secure_flanks"]
    end
    subgraph tier_4["Tier 4"]
        n35["SER_advance_north"]
        n36["SER_anti_partizan_tactics"]
        n37["SER_deterrence"]
        n38["SER_ideological_fanaticism"]
        n39["SER_ideological_fanaticism_communism"]
        n40["SER_local_steel_production"]
        n41["SER_organized_partizans"]
        n42["SER_research_grants"]
    end
    subgraph tier_5["Tier 5"]
        n43["SER_why_we_fight"]
    end
    subgraph tier_6["Tier 6"]
        n44["SER_technology_sharing"]
    end
    n34 --> n35
    n31 --> n36
    n19 --> n21
    n28 --> n37
    n29 --> n37
    n18 --> n22
    n21 --> n28
    n17 --> n18
    n31 --> n38
    n33 --> n39
    n27 --> n29
    n21 --> n29
    n26 --> n30
    n17 --> n19
    n18 --> n23
    n32 --> n40
    n20 --> n24
    n24 --> n31
    n17 --> n20
    n22 --> n32
    n33 --> n41
    n22 --> n33
    n23 --> n33
    n18 --> n25
    n28 --> n42
    n29 --> n42
    n20 --> n26
    n26 --> n34
    n39 --> n44
    n38 --> n44
    n43 --> n44
    n19 --> n27
    n37 --> n43
    n42 --> n43
    n21 x--x n27
    n37 x--x n42
    n28 x--x n29
```

# SER_state_guard

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n45(("SER_state_guard"))
    end
    subgraph tier_1["Tier 1"]
        n46{"SER_army_maneuvers"}
        n47{"SER_aviation_effort"}
        n48["SER_expand_the_split_shipyards"]
        n49["SER_mountain_brigades"]
        n50["SER_small_arms"]
    end
    subgraph tier_2["Tier 2"]
        n51["SER_airplanes_licenses"]
        n52["SER_coastal_defense"]
        n53["SER_contest_the_adriatic"]
        n54["SER_domestic_artillery_production"]
        n55["SER_local_developers"]
        n56["SER_motorization_effort"]
        n57["SER_supremacy_of_defense"]
        n58["SER_supremacy_of_offense"]
    end
    subgraph tier_3["Tier 3"]
        n59["SER_anti_tank_defenses"]
        n60{"SER_armored_cavalry"}
        n61{"SER_artillery_regiments"}
        n62{"SER_ikarus"}
        n63["SER_kraljevo_state_airlines_factory"]
        n64["SER_light_cruiser"]
        n65{"SER_modern_destroyers"}
        n66{"SER_rogozarski"}
        n67["SER_special_forces"]
        n68["SER_structured_logistics"]
        n69{"SER_zmaj"}
    end
    subgraph tier_4["Tier 4"]
        n70["SER_bomber_focus"]
        n71["SER_fighter_focus"]
        n72["SER_form_mechanics"]
        n73{"SER_heavy_cruiser_project"}
        n74["SER_modern_tanks"]
        n75["SER_recovery_teams"]
        n76["SER_tank_conversions"]
    end
    subgraph tier_5["Tier 5"]
        n77["SER_adriatic_specialization"]
        n78["SER_aviation_effort_2"]
        n79["SER_expanded_repair_facilities"]
        n80["SER_skilled_pilots"]
    end
    subgraph tier_6["Tier 6"]
        n81["SER_CAS_effort"]
        n82["SER_naval_bombers"]
    end
    n78 --> n81
    n65 --> n77
    n73 --> n77
    n47 --> n51
    n54 --> n59
    n56 --> n60
    n45 --> n46
    n58 --> n61
    n57 --> n61
    n54 --> n61
    n45 --> n47
    n70 --> n78
    n71 --> n78
    n72 --> n78
    n62 --> n70
    n66 --> n70
    n69 --> n70
    n48 --> n52
    n48 --> n53
    n50 --> n54
    n45 --> n48
    n63 --> n79
    n72 --> n79
    n62 --> n71
    n66 --> n71
    n69 --> n71
    n51 --> n72
    n62 --> n72
    n66 --> n72
    n69 --> n72
    n64 --> n73
    n55 --> n62
    n51 --> n63
    n52 --> n64
    n47 --> n55
    n53 --> n65
    n60 --> n74
    n61 --> n74
    n46 --> n56
    n45 --> n49
    n78 --> n82
    n68 --> n75
    n60 --> n75
    n55 --> n66
    n65 --> n80
    n73 --> n80
    n45 --> n50
    n49 --> n67
    n50 --> n67
    n57 --> n67
    n58 --> n67
    n56 --> n68
    n46 --> n57
    n46 --> n58
    n60 --> n76
    n55 --> n69
    n77 x--x n80
    n51 x--x n55
    n70 x--x n71
    n74 x--x n76
    n57 x--x n58
```
