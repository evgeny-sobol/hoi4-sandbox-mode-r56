# CRO_build_the_nation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CRO_build_the_nation"))
        n2["CRO_motorization_effort"]
    end
    subgraph tier_1["Tier 1"]
        n3["CRO_construction_effort"]
        n4["CRO_infrastructure_effort"]
        n5["CRO_research_collaboration"]
    end
    subgraph tier_2["Tier 2"]
        n6["CRO_production_effort"]
        n7["CRO_prospect_for_resources"]
    end
    subgraph tier_3["Tier 3"]
        n8["CRO_expand_the_university_of_zagreb"]
        n9["CRO_extract_chromium"]
        n10["CRO_extract_oil"]
        n11["CRO_production_effort_2"]
    end
    subgraph tier_4["Tier 4"]
        n12["CRO_develop_bosnia"]
        n13["CRO_extra_tech_slot_2"]
        n14["CRO_industrial_planning"]
    end
    subgraph tier_5["Tier 5"]
        n15["CRO_construction_effort_2"]
        n16["CRO_expand_the_sarajevo_arsenals"]
    end
    subgraph tier_6["Tier 6"]
        n17["CRO_nuclear_effort"]
    end
    n1 --> n3
    n14 --> n15
    n8 --> n12
    n12 --> n16
    n14 --> n16
    n4 --> n8
    n6 --> n8
    n8 --> n13
    n7 --> n9
    n7 --> n10
    n2 --> n10
    n8 --> n14
    n1 --> n4
    n15 --> n17
    n3 --> n6
    n6 --> n11
    n4 --> n7
    n1 --> n5
```

# CRO_home_guard

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18(("CRO_home_guard"))
        n7["CRO_prospect_for_resources"]
    end
    subgraph tier_1["Tier 1"]
        n19{"CRO_army_maneuvers"}
        n20{"CRO_aviation_effort"}
        n21["CRO_expand_the_split_shipyards"]
        n22["CRO_mountain_brigades"]
        n23["CRO_small_arms"]
    end
    subgraph tier_2["Tier 2"]
        n24["CRO_airplanes_licenses"]
        n25["CRO_bomber_focus"]
        n26["CRO_coastal_defense"]
        n27["CRO_contest_the_adriatic"]
        n28["CRO_domestic_artillery_production"]
        n29["CRO_fighter_focus"]
        n2["CRO_motorization_effort"]
        n30["CRO_supremacy_of_defense"]
        n31["CRO_supremacy_of_offense"]
    end
    subgraph tier_3["Tier 3"]
        n32["CRO_anti_tank_defenses"]
        n33{"CRO_armored_cavalry"}
        n34{"CRO_artillery_regiments"}
        n35["CRO_aviation_effort_2"]
        n10["CRO_extract_oil"]
        n36["CRO_form_mechanics"]
        n37["CRO_light_cruiser"]
        n38{"CRO_modern_destroyers"}
        n39["CRO_special_forces"]
        n40["CRO_structured_logistics"]
    end
    subgraph tier_4["Tier 4"]
        n41["CRO_CAS_effort"]
        n42{"CRO_heavy_cruiser_project"}
        n43["CRO_modern_tanks"]
        n44["CRO_naval_bombers"]
        n45["CRO_recovery_teams"]
        n46["CRO_tank_conversions"]
    end
    subgraph tier_5["Tier 5"]
        n47["CRO_adriatic_specialization"]
        n48["CRO_skilled_pilots"]
    end
    n35 --> n41
    n38 --> n47
    n42 --> n47
    n20 --> n24
    n28 --> n32
    n2 --> n33
    n18 --> n19
    n31 --> n34
    n30 --> n34
    n28 --> n34
    n18 --> n20
    n25 --> n35
    n29 --> n35
    n24 --> n35
    n20 --> n25
    n21 --> n26
    n21 --> n27
    n23 --> n28
    n18 --> n21
    n7 --> n10
    n2 --> n10
    n20 --> n29
    n24 --> n36
    n29 --> n36
    n25 --> n36
    n37 --> n42
    n26 --> n37
    n27 --> n38
    n33 --> n43
    n34 --> n43
    n19 --> n2
    n18 --> n22
    n27 --> n44
    n26 --> n44
    n35 --> n44
    n40 --> n45
    n33 --> n45
    n38 --> n48
    n42 --> n48
    n18 --> n23
    n22 --> n39
    n23 --> n39
    n30 --> n39
    n31 --> n39
    n2 --> n40
    n19 --> n30
    n19 --> n31
    n33 --> n46
    n47 x--x n48
    n24 x--x n25
    n24 x--x n29
    n25 x--x n29
    n43 x--x n46
    n30 x--x n31
```

# CRO_political_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n49{"CRO_political_effort"}
    end
    subgraph tier_1["Tier 1"]
        n50["CRO_catholic_dominance_focus"]
        n51["CRO_form_peasant_councils"]
        n52{"CRO_liberty_ethos"}
        n53{"CRO_nationalism_focus"}
        n54["CRO_reclaim_the_coast"]
        n55["CRO_secularism_focus"]
    end
    subgraph tier_2["Tier 2"]
        n56["CRO_economic_centralization"]
        n57{"CRO_enforce_pavelic_rule"}
        n58["CRO_integrate_muslim_croats_focus"]
        n59["CRO_integrate_religious_minorities_focus"]
        n60{"CRO_italian_influence_focus"}
        n61["CRO_join_yugoslavia"]
        n62["CRO_local_militias"]
        n63["CRO_militarism"]
        n64{"CRO_trading_infrastructures"}
        n65{"CRO_zagreb_investments_focus"}
    end
    subgraph tier_3["Tier 3"]
        n66["CRO_a_king_for_our_people_focus"]
        n67["CRO_bosnian_muslim_conscription_focus"]
        n68["CRO_dalmatian_question_focus"]
        n69{"CRO_economic_optimization"}
        n70{"CRO_industrial_support"}
        n71["CRO_integrate_orthodox_croats_focus"]
        n72["CRO_italo_croat_legion"]
        n73["CRO_military_youth"]
        n74["CRO_nationalize_factories"]
        n75["CRO_political_commissars"]
    end
    subgraph tier_4["Tier 4"]
        n76["CRO_anti_partizan_tactics"]
        n77["CRO_deterrence"]
        n78["CRO_ideological_fanaticism_communism"]
        n79["CRO_ideological_fanaticism_ustasha"]
        n80["CRO_liberate_bosnian_croats"]
        n81["CRO_local_steel_production"]
        n82["CRO_organized_partizans"]
        n83["CRO_research_grants"]
    end
    subgraph tier_5["Tier 5"]
        n84["CRO_faithful_ally"]
        n85["CRO_why_we_fight"]
    end
    subgraph tier_6["Tier 6"]
        n86["CRO_technology_sharing"]
    end
    n60 --> n66
    n57 --> n66
    n73 --> n76
    n58 --> n67
    n59 --> n67
    n49 --> n50
    n57 --> n68
    n69 --> n77
    n70 --> n77
    n51 --> n56
    n65 --> n69
    n53 --> n57
    n76 --> n84
    n49 --> n51
    n75 --> n78
    n73 --> n79
    n64 --> n70
    n65 --> n70
    n50 --> n58
    n58 --> n71
    n55 --> n59
    n53 --> n60
    n60 --> n72
    n51 --> n61
    n73 --> n80
    n49 --> n52
    n51 --> n62
    n74 --> n81
    n53 --> n63
    n63 --> n73
    n49 --> n53
    n56 --> n74
    n75 --> n82
    n56 --> n75
    n62 --> n75
    n49 --> n54
    n69 --> n83
    n70 --> n83
    n49 --> n55
    n78 --> n86
    n79 --> n86
    n85 --> n86
    n52 --> n64
    n77 --> n85
    n83 --> n85
    n52 --> n65
    n66 x--x n68
    n50 x--x n55
    n77 x--x n83
    n69 x--x n70
    n57 x--x n60
    n64 x--x n65
```
