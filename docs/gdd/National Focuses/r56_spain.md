# SPR_Air_Officers

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SPR_Air_Officers"))
    end
    subgraph tier_1["Tier 1"]
        n2["SPR_Air_Factories"]
    end
    subgraph tier_2["Tier 2"]
        n3{"SPR_Fighters"}
    end
    subgraph tier_3["Tier 3"]
        n4["SPR_CAS"]
        n5["SPR_Strat"]
        n6["SPR_Tac_Bomber"]
    end
    subgraph tier_4["Tier 4"]
        n7["SPR_Air_Doctrine"]
        n8["SPR_Air_Doctrine_2"]
        n9["SPR_Air_Doctrine_3"]
    end
    n4 --> n7
    n6 --> n8
    n5 --> n9
    n1 --> n2
    n3 --> n4
    n2 --> n3
    n3 --> n5
    n3 --> n6
    n4 x--x n5
    n4 x--x n6
    n5 x--x n6
```

# SPR_Mil

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10(("SPR_Mil"))
    end
    subgraph tier_1["Tier 1"]
        n11["SPR_Equipment"]
        n12["SPR_Expand"]
    end
    subgraph tier_2["Tier 2"]
        n13["SPR_Fortify_Islands"]
        n14["SPR_Mot"]
    end
    subgraph tier_3["Tier 3"]
        n15["SPR_Doctrine"]
        n16{"SPR_Mech"}
    end
    subgraph tier_4["Tier 4"]
        n17["SPR_Doc_Bonus_2"]
        n18["SPR_Domestic_Tanks"]
        n19["SPR_Foreign_Tanks"]
    end
    subgraph tier_5["Tier 5"]
        n20["SPR_Doc_Wep"]
        n21["SPR_Exercises"]
    end
    n15 --> n17
    n17 --> n20
    n13 --> n15
    n16 --> n18
    n10 --> n11
    n18 --> n21
    n19 --> n21
    n10 --> n12
    n16 --> n19
    n12 --> n13
    n14 --> n16
    n11 --> n14
    n18 x--x n19
```

# SPR_Naval

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n22(("SPR_Naval"))
    end
    subgraph tier_1["Tier 1"]
        n23["SPR_Naval_2"]
    end
    subgraph tier_2["Tier 2"]
        n24["SPR_Capitals"]
        n25["SPR_Screens"]
        n26["SPR_Subs"]
    end
    subgraph tier_3["Tier 3"]
        n27["SPR_Carriers"]
    end
    subgraph tier_4["Tier 4"]
        n28["SPR_Nav_Air"]
    end
    n23 --> n24
    n24 --> n27
    n26 --> n27
    n25 --> n27
    n27 --> n28
    n22 --> n23
    n23 --> n25
    n23 --> n26
```

# SPR_back_the_ceda

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29(("SPR_back_the_ceda"))
        n30["SPR_maintain_the_popular_front"]
    end
    subgraph tier_1["Tier 1"]
        n31["SPR_establish_a_conspiracy"]
    end
    subgraph tier_2["Tier 2"]
        n32["SPR_the_army_of_africa_connection"]
    end
    subgraph tier_3["Tier 3"]
        n33["SPR_strike_first_nat"]
    end
    subgraph tier_4["Tier 4"]
        n34["SPR_unionify_the_faction_nat"]
    end
    subgraph tier_5["Tier 5"]
        n35["SPR_solidify_the_fronts_nat"]
    end
    subgraph tier_6["Tier 6"]
        n36["SPR_equipment_shipments_r56_nat"]
    end
    subgraph tier_7["Tier 7"]
        n37["SPR_new_approach_nat"]
        n38["SPR_tackle_the_weak_fronts_r56"]
    end
    subgraph tier_8["Tier 8"]
        n39["SPR_expand_axis_aide"]
    end
    n35 --> n36
    n29 --> n31
    n38 --> n39
    n37 --> n39
    n36 --> n37
    n34 --> n35
    n32 --> n33
    n36 --> n38
    n31 --> n32
    n33 --> n34
    n29 x--x n30
```

# SPR_maintain_the_popular_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29["SPR_back_the_ceda"]
        n30(("SPR_maintain_the_popular_front"))
    end
    subgraph tier_1["Tier 1"]
        n40["SPR_maintain_the_civil_guards_loyality"]
    end
    subgraph tier_2["Tier 2"]
        n41["SPR_proclaim_a_general_strike"]
    end
    subgraph tier_3["Tier 3"]
        n42["SPR_strike_first_spr"]
    end
    subgraph tier_4["Tier 4"]
        n43["SPR_unionify_the_faction_spr"]
    end
    subgraph tier_5["Tier 5"]
        n44["SPR_solidify_the_fronts_spr"]
    end
    subgraph tier_6["Tier 6"]
        n45["SPR_equipment_shipments_r56_spr"]
    end
    subgraph tier_7["Tier 7"]
        n46["SPR_international_brigdes_r56"]
        n47["SPR_new_approach_spr"]
    end
    subgraph tier_8["Tier 8"]
        n48["SPR_excavate_the_gold_reserves"]
    end
    n44 --> n45
    n46 --> n48
    n47 --> n48
    n45 --> n46
    n30 --> n40
    n45 --> n47
    n40 --> n41
    n43 --> n44
    n41 --> n42
    n42 --> n43
    n29 x--x n30
```

# SPR_post_depression_recovery

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n49(("SPR_post_depression_recovery"))
    end
    subgraph tier_1["Tier 1"]
        n50["SPR_increase_public_investments"]
        n51["SPR_surevaluate_the_peseta"]
    end
    subgraph tier_2["Tier 2"]
        n52["SPR_create_the_ini"]
        n53["SPR_repair_the_national_roads"]
        n54["SPR_save_the_education_budget"]
    end
    subgraph tier_3["Tier 3"]
        n55["SPR_create_instalaza"]
        n56["SPR_expand_the_mines"]
    end
    subgraph tier_4["Tier 4"]
        n57["SPR_support_the_heavy_industry"]
    end
    n52 --> n55
    n50 --> n52
    n53 --> n56
    n49 --> n50
    n51 --> n53
    n50 --> n54
    n51 --> n54
    n55 --> n57
    n56 --> n57
    n49 --> n51
```
