# COL_industrial_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"COL_industrial_effort"}
    end
    subgraph tier_1["Tier 1"]
        n2["COL_acerias_pdr"]
        n3["COL_coffe_growth"]
    end
    subgraph tier_2["Tier 2"]
        n4["COL_indumil"]
        n5["COL_industry_effort_2"]
        n6["COL_intensify_exports"]
        n7["COL_minning"]
        n8["COL_puerto_buenaventura"]
    end
    subgraph tier_3["Tier 3"]
        n9["COL_explore_amazonia"]
        n10["COL_hidroelectrics"]
        n11["COL_infrastructure_caribe"]
        n12["COL_infrastructure_harsh"]
    end
    subgraph tier_4["Tier 4"]
        n13["COL_altillanura_ress"]
        n14["COL_extra_tech_slot"]
        n15["COL_extra_tech_slot_2"]
        n16["COL_fortify_caribe"]
        n17["COL_indumil_2"]
    end
    subgraph tier_5["Tier 5"]
        n18["COL_fortify_caribe_aa"]
        n19["COL_secret_weapons"]
    end
    subgraph tier_6["Tier 6"]
        n20["COL_nuclear_effort"]
    end
    n1 --> n2
    n9 --> n13
    n12 --> n13
    n1 --> n3
    n6 --> n9
    n7 --> n9
    n11 --> n14
    n12 --> n15
    n10 --> n15
    n11 --> n16
    n16 --> n18
    n5 --> n10
    n2 --> n4
    n4 --> n17
    n11 --> n17
    n3 --> n5
    n2 --> n5
    n8 --> n11
    n4 --> n11
    n5 --> n12
    n3 --> n6
    n3 --> n7
    n19 --> n20
    n2 --> n8
    n15 --> n19
    n2 x--x n3
```

# COL_political_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n21{"COL_political_effort"}
    end
    subgraph tier_1["Tier 1"]
        n22{"COL_collectivist_ethos"}
        n23["COL_liberty_ethos"]
    end
    subgraph tier_2["Tier 2"]
        n24["COL_affirm_state_role_in_the_economy"]
        n25["COL_continue_constitutional_reforms"]
        n26["COL_internationalism_focus"]
        n27["COL_nationalism_focus"]
        n28["COL_spanish_civil_war_involvement"]
    end
    subgraph tier_3["Tier 3"]
        n29["COL_axis_leanings_focus"]
        n30["COL_educational_reform"]
        n31["COL_gran_colombia"]
        n32["COL_join_the_comintern"]
        n33["COL_militarism"]
        n34["COL_political_correctness"]
        n35["COL_workers_protection"]
    end
    subgraph tier_4["Tier 4"]
        n36["COL_axis_leanings_focus_2"]
        n37["COL_axis_leanings_focus_3"]
        n38["COL_embrace_our_catholic_heritage"]
        n39["COL_hermano_bolivariano"]
        n40["COL_indoctrination_focus"]
        n41["COL_legalize_the_pcc"]
        n42["COL_paramilitarism"]
        n43["COL_soviet_technological_cooperation"]
        n44["COL_why_we_fight"]
    end
    subgraph tier_5["Tier 5"]
        n45["COL_ideological_fanaticism"]
        n46["COL_join_the_allies"]
        n47["COL_mosquitos"]
        n48["COL_war_with_andeans"]
    end
    subgraph tier_6["Tier 6"]
        n49["COL_etnocacerismo"]
    end
    subgraph tier_7["Tier 7"]
        n50["COL_etnocacerismo_2"]
    end
    n23 --> n24
    n27 --> n29
    n29 --> n36
    n33 --> n36
    n29 --> n37
    n21 --> n22
    n23 --> n25
    n25 --> n30
    n33 --> n38
    n42 --> n49
    n48 --> n49
    n49 --> n50
    n45 --> n50
    n27 --> n31
    n26 --> n31
    n31 --> n39
    n42 --> n45
    n40 --> n45
    n34 --> n40
    n22 --> n26
    n44 --> n46
    n26 --> n32
    n35 --> n41
    n21 --> n23
    n27 --> n33
    n39 --> n47
    n22 --> n27
    n33 --> n42
    n26 --> n34
    n32 --> n43
    n22 --> n28
    n23 --> n28
    n39 --> n48
    n30 --> n44
    n35 --> n44
    n24 --> n35
    n22 x--x n23
    n26 x--x n27
```
