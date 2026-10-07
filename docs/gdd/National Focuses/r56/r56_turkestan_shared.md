# TRK_State_Matter

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"TRK_State_Matter"}
    end
    subgraph tier_1["Tier 1"]
        n2{"TRK_popular_will"}
        n3{"TRK_steppic_memories"}
    end
    subgraph tier_2["Tier 2"]
        n4{"TRK_Strenghten_Democracy"}
        n5{"TRK_internationalism_focus"}
        n6["TRK_nationalism_focus"]
        n7["TRK_restore_khanate"]
        n8{"TRK_tear_down_stalins_legacy"}
    end
    subgraph tier_3["Tier 3"]
        n9["TRK_Collectivist_Propaganda"]
        n10["TRK_Com_Generals"]
        n11["TRK_Conquer"]
        n12["TRK_Defence_Act"]
        n13["TRK_Militarism"]
        n14["TRK_comrpomise_with_soviet_settlers"]
        n15["TRK_form_the_turkestan_legion"]
        n16{"TRK_interventionism_focus"}
        n17["TRK_khanate_expansionism"]
        n18["TRK_khans_horde"]
        n19["TRK_military_government"]
        n20{"TRK_neutrality_focus"}
        n21["TRK_subdue_the_soviet_minority"]
    end
    subgraph tier_4["Tier 4"]
        n22["TRK_Anti_Invasion"]
        n23["TRK_Brigades"]
        n24["TRK_Fanaticism"]
        n25["TRK_Forced_Conscription"]
        n26["TRK_Military_Build"]
        n27["TRK_Organise_Youth"]
        n28["TRK_border_contest"]
        n29["TRK_integrate_the_settlers"]
        n30["TRK_invade_borderlands"]
        n31["TRK_provide_autonomy_to_settlers"]
    end
    subgraph tier_5["Tier 5"]
        n32["TRK_the_road_to_turkestan"]
        n33["TRK_war_cry"]
        n34["TRK_why_we_fight"]
    end
    n20 --> n22
    n16 --> n23
    n5 --> n9
    n5 --> n10
    n5 --> n11
    n4 --> n12
    n11 --> n24
    n11 --> n25
    n16 --> n25
    n6 --> n13
    n7 --> n13
    n20 --> n26
    n16 --> n26
    n11 --> n27
    n2 --> n4
    n17 --> n28
    n8 --> n14
    n6 --> n15
    n21 --> n29
    n14 --> n29
    n2 --> n5
    n4 --> n16
    n5 --> n16
    n17 --> n30
    n13 --> n30
    n7 --> n17
    n6 --> n17
    n7 --> n18
    n6 --> n19
    n3 --> n6
    n4 --> n20
    n1 --> n2
    n14 --> n31
    n3 --> n7
    n1 --> n3
    n8 --> n21
    n3 --> n8
    n2 --> n8
    n28 --> n32
    n30 --> n32
    n30 --> n33
    n22 --> n34
    n26 --> n34
    n23 --> n34
    n22 x--x n26
    n11 x--x n16
    n4 x--x n5
    n14 x--x n21
    n16 x--x n20
    n6 x--x n7
    n2 x--x n3
```

# TRK_reinvigorating_the_economy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35(("TRK_reinvigorating_the_economy"))
    end
    subgraph tier_1["Tier 1"]
        n36["TRK_agricultural_renewal"]
        n37["TRK_industrial_expansion"]
        n38["TRK_war_readiness"]
    end
    subgraph tier_2["Tier 2"]
        n39["TRK_MOVING_FILM_STUDIOS"]
        n40["TRK_accommodate_exiled_companies"]
        n41["TRK_agricultural_expansion"]
        n42["TRK_exploit_the_virgin_lands"]
        n43["TRK_military_industries"]
        n44{"TRK_new_plans_of_war"}
        n45["TRK_railway"]
    end
    subgraph tier_3["Tier 3"]
        n46["TRK_exportation_nazi_helpers"]
        n47["TRK_increase_armament_production"]
        n48["TRK_kun_project"]
        n49["TRK_lead_ammunition_production"]
        n50["TRK_mining_tech"]
        n51["TRK_secondary_roads"]
        n52["TRK_soviet_secret_weapons"]
    end
    subgraph tier_4["Tier 4"]
        n53["TRK_almati_lead_industry"]
        n54["TRK_emba_bassin_oil_infrastructure"]
        n55["TRK_khrouchtchev_memorandum"]
        n56["TRK_nuclear"]
        n57["TRK_space"]
        n58["TRK_temirtaw_steel_mill"]
    end
    subgraph tier_5["Tier 5"]
        n59["TRK_baikonour_launching_site"]
        n60["TRK_semipalatinsk_nuclear_site"]
    end
    n38 --> n39
    n37 --> n40
    n36 --> n41
    n35 --> n36
    n51 --> n53
    n57 --> n59
    n50 --> n54
    n36 --> n42
    n40 --> n46
    n43 --> n47
    n35 --> n37
    n46 --> n55
    n44 --> n48
    n43 --> n49
    n37 --> n43
    n38 --> n43
    n45 --> n50
    n38 --> n44
    n52 --> n56
    n48 --> n56
    n37 --> n45
    n45 --> n51
    n56 --> n60
    n44 --> n52
    n52 --> n57
    n48 --> n57
    n50 --> n58
    n35 --> n38
    n48 x--x n52
```

# TRK_turkestan_unification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n61["SIB_siberian_unification"]
        n62(("TRK_turkestan_unification"))
    end
    subgraph tier_1["Tier 1"]
        n63["TRK_connect_the_cities"]
        n64["TRK_defend_the_new_union"]
        n65["TRK_develop_mining"]
        n66["TRK_military_camelry"]
    end
    subgraph tier_2["Tier 2"]
        n67["TRK_emba_bassin_oil_infrastructure_shared"]
        n68["TRK_ethnic_collaboration"]
        n69["TRK_temirtaw_steel_mill_shared"]
        n70["TRK_united_armed_forces"]
    end
    subgraph tier_3["Tier 3"]
        n71["TRK_trans_turkestan_railway"]
    end
    n62 --> n63
    n62 --> n64
    n62 --> n65
    n65 --> n67
    n63 --> n68
    n62 --> n66
    n63 --> n69
    n68 --> n71
    n64 --> n70
    n61 x--x n62
```
