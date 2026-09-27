# CHI_sea_develop_capital

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CHI_sea_develop_capital"))
    end
    subgraph tier_1["Tier 1"]
        n2["CHI_sea_develop_capital_arsenal"]
        n3["CHI_sea_further_industrial_investment"]
    end
    subgraph tier_2["Tier 2"]
        n4["CHI_sea_expand_public_education"]
        n5["CHI_sea_long_term_economic_planning"]
        n6["CHI_sea_small_arms_production"]
    end
    subgraph tier_3["Tier 3"]
        n7{"CHI_sea_fund_research_projects"}
        n8["CHI_sea_heavy_weapons_development"]
        n9["CHI_sea_industrial_research_projects"]
    end
    subgraph tier_4["Tier 4"]
        n10["CHI_sea_modern_warfare"]
        n11["CHI_sea_rely_on_our_infantry"]
    end
    n1 --> n2
    n3 --> n4
    n2 --> n4
    n4 --> n7
    n1 --> n3
    n6 --> n8
    n5 --> n9
    n3 --> n5
    n7 --> n10
    n7 --> n11
    n2 --> n6
    n10 x--x n11
```

# CHI_sea_secure_internal_politics

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12{"CHI_sea_secure_internal_politics"}
    end
    subgraph tier_1["Tier 1"]
        n13["CHI_sea_cooperation_with_the_communists"]
        n14["CHI_sea_cooperation_with_the_nationalists"]
        n15["CHI_sea_opposition"]
    end
    subgraph tier_2["Tier 2"]
        n16["CHI_sea_anti_opposition_campaigns"]
        n17["CHI_sea_institute_cross_border_raids"]
        n18["CHI_sea_land_redistribution"]
        n19{"CHI_sea_new_model_province"}
        n20["CHI_sea_public_works"]
        n21["CHI_sea_technological_cooperation"]
        n22["CHI_sea_war_taxes"]
    end
    subgraph tier_3["Tier 3"]
        n23["CHI_sea_cult_of_personality"]
        n24["CHI_sea_embrace_the_illicit_trade"]
        n25["CHI_sea_ideological_education"]
        n26["CHI_sea_labor_reform"]
        n27["CHI_sea_land_value_tax"]
        n28{"CHI_sea_personal_leadership"}
        n29["CHI_sea_root_out_corruption"]
        n30["CHI_sea_rural_militias"]
        n31["CHI_sea_seek_japanese_support"]
    end
    subgraph tier_4["Tier 4"]
        n32["CHI_sea_communist_administrators"]
        n33["CHI_sea_defensive_posture"]
        n34["CHI_sea_judiciary_reforms"]
        n35{"CHI_sea_land_reform"}
        n36["CHI_sea_provoke_border_clashes"]
        n37{"CHI_sea_reform_the_administration"}
    end
    subgraph tier_5["Tier 5"]
        n38["CHI_sea_battle_for_china"]
        n39["CHI_sea_join_the_chinese_soviet"]
        n40["CHI_sea_join_the_republican_government"]
        n41["CHI_sea_rapid_mobilization"]
    end
    subgraph tier_6["Tier 6"]
        n42["CHI_sea_a_new_expedition"]
        n43["CHI_sea_gain_warlord_support"]
        n44["CHI_sea_proclaim_rival_government"]
        n45["CHI_sea_propaganda_campaigns"]
        n46["CHI_sea_rally_the_warlords"]
        n47["CHI_sea_unified_army_structure"]
    end
    subgraph tier_7["Tier 7"]
        n48["CHI_sea_power_struggle"]
        n49["CHI_sea_the_yanan_incident"]
    end
    n38 --> n42
    n14 --> n16
    n13 --> n16
    n35 --> n38
    n37 --> n38
    n27 --> n32
    n12 --> n13
    n12 --> n14
    n22 --> n23
    n28 --> n33
    n19 --> n24
    n40 --> n43
    n18 --> n25
    n15 --> n17
    n34 --> n39
    n32 --> n39
    n35 --> n40
    n37 --> n40
    n25 --> n34
    n20 --> n26
    n13 --> n18
    n29 --> n35
    n18 --> n27
    n14 --> n19
    n12 --> n15
    n22 --> n28
    n43 --> n48
    n45 --> n48
    n42 --> n48
    n46 --> n48
    n30 --> n44
    n41 --> n44
    n40 --> n45
    n28 --> n36
    n13 --> n20
    n15 --> n20
    n38 --> n46
    n36 --> n41
    n33 --> n41
    n29 --> n37
    n24 --> n37
    n19 --> n29
    n20 --> n30
    n22 --> n31
    n14 --> n21
    n47 --> n49
    n39 --> n47
    n15 --> n22
    n38 x--x n40
    n13 x--x n14
    n13 x--x n15
    n14 x--x n15
    n33 x--x n36
    n24 x--x n29
```

# CHI_sea_strenghten_warlord_authority

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n50{"CHI_sea_strenghten_warlord_authority"}
    end
    subgraph tier_1["Tier 1"]
        n51["CHI_sea_uplift_the_cavalry_regiments"]
        n52["CHI_sea_uplift_the_mountain_brigades"]
    end
    subgraph tier_2["Tier 2"]
        n53["CHI_sea_consolidate_our_rule"]
    end
    subgraph tier_3["Tier 3"]
        n54["CHI_sea_brigade_specialization"]
        n55["CHI_sea_fortification_efforts"]
        n56["CHI_sea_infantry_efforts"]
    end
    subgraph tier_4["Tier 4"]
        n57["CHI_sea_the_army"]
    end
    subgraph tier_5["Tier 5"]
        n58["CHI_crackdown_on_looting"]
    end
    n57 --> n58
    n53 --> n54
    n52 --> n53
    n51 --> n53
    n53 --> n55
    n53 --> n56
    n54 --> n57
    n56 --> n57
    n50 --> n51
    n50 --> n52
    n51 x--x n52
```

# KUM_victory_in_tihwa

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n59(("KUM_victory_in_tihwa"))
    end
    subgraph tier_1["Tier 1"]
        n60["KUM_restore_yettishar"]
    end
    n59 --> n60
```

# XIC_northwest_bandit_suppression_headquarters

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61(("XIC_northwest_bandit_suppression_headquarters"))
    end
```

# XSM_sideline_family_conflicts

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n62(("XSM_sideline_family_conflicts"))
    end
    subgraph tier_1["Tier 1"]
        n63{"XSM_strengthening_our_position"}
    end
    subgraph tier_2["Tier 2"]
        n64["XSM_demand_submission"]
        n65["XSM_strike_at_the_detractors"]
    end
    subgraph tier_3["Tier 3"]
        n66["XSM_a_united_ma_state"]
    end
    n64 --> n66
    n65 --> n66
    n63 --> n64
    n62 --> n63
    n63 --> n65
    n64 x--x n65
```
