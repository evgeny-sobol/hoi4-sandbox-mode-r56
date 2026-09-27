# NIC_president_Somoza_Garcia

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("NIC_president_Somoza_Garcia"))
    end
    subgraph tier_1["Tier 1"]
        n2["NIC_begin_a_political_crackdown"]
        n3{"NIC_nicaraguan_diplomacy"}
        n4["NIC_reinstate_national_guard_control"]
    end
    subgraph tier_2["Tier 2"]
        n5["NIC_ally_the_champion_of_europe"]
        n6["NIC_expanded_national_guard_powers"]
        n7["NIC_judicial_control"]
        n8["NIC_look_to_washington_once_again"]
        n9["NIC_supervise_large_enterprises"]
        n10["NIC_the_strength_of_moscow"]
        n11["NIC_uproot_banditry"]
    end
    subgraph tier_3["Tier 3"]
        n12["NIC_control_immigration"]
        n13["NIC_health_services"]
        n14["NIC_lend_lease_for_docking_rights"]
        n15["NIC_local_intelligence_cooperation"]
        n16["NIC_marine_national_guard_cooperation"]
        n17["NIC_regulate_the_national_railroads"]
        n18["NIC_steel_trade"]
        n19["NIC_support_of_the_psn"]
        n20["NIC_take_over_the_national_radio"]
    end
    subgraph tier_4["Tier 4"]
        n21["NIC_begin_forcibly_annexing_nicaraguan_german_land"]
        n22["NIC_foreign_concessions_on_gold_exploitation"]
        n23["NIC_nkvd_assistance"]
        n24["NIC_push_south"]
        n25["NIC_soviet_economic_assistance"]
        n26["NIC_the_somoza_family_fortune"]
    end
    subgraph tier_5["Tier 5"]
        n27["NIC_combat_fruit_industries_influence"]
    end
    n3 --> n5
    n1 --> n2
    n19 --> n21
    n14 --> n21
    n23 --> n27
    n25 --> n27
    n11 --> n12
    n6 --> n12
    n4 --> n6
    n14 --> n22
    n16 --> n22
    n7 --> n13
    n2 --> n7
    n8 --> n14
    n5 --> n15
    n3 --> n8
    n8 --> n16
    n1 --> n3
    n19 --> n23
    n15 --> n24
    n18 --> n24
    n9 --> n17
    n1 --> n4
    n19 --> n25
    n5 --> n18
    n2 --> n9
    n10 --> n19
    n7 --> n20
    n9 --> n20
    n12 --> n26
    n17 --> n26
    n13 --> n26
    n3 --> n10
    n4 --> n11
    n5 x--x n8
    n5 x--x n10
    n8 x--x n10
```
