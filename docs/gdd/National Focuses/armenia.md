# ARM_improve_construction_methods

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ARM_improve_construction_methods"))
    end
    subgraph tier_1["Tier 1"]
        n2["ARM_develop_hydroelectric_power"]
        n3["ARM_expand_the_railway_network"]
        n4["ARM_small_arms_workshops"]
        n5["ARM_start_the_rare_minerals_program"]
    end
    subgraph tier_2["Tier 2"]
        n6["ARM_domestic_artillery_production"]
        n7["ARM_expand_ararat_cement"]
        n8["ARM_expand_zangezur_copper_mine"]
        n9["ARM_increase_munition_production"]
        n10["ARM_plan_the_kajaran_mine"]
        n11["ARM_reinforce_gold_mining"]
    end
    subgraph tier_3["Tier 3"]
        n12["ARM_industrial_advancements"]
        n13["ARM_support_chemical_factories"]
    end
    subgraph tier_4["Tier 4"]
        n14["ARM_expand_the_yerevan_university"]
        n15["ARM_irrigate_the_ararat_valley"]
        n16["ARM_synthetic_rubber_expertise"]
    end
    n1 --> n2
    n4 --> n6
    n3 --> n7
    n2 --> n7
    n1 --> n3
    n12 --> n14
    n5 --> n8
    n4 --> n9
    n7 --> n12
    n13 --> n15
    n5 --> n10
    n5 --> n11
    n1 --> n4
    n1 --> n5
    n7 --> n13
    n13 --> n16
    n12 --> n16
```

# ARM_return_from_exile

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17(("ARM_return_from_exile"))
        n18["ARM_socialist_governmental_autonomy"]
    end
    subgraph tier_1["Tier 1"]
        n19["ARM_reunify_the_armenian_people"]
    end
    subgraph tier_2["Tier 2"]
        n20{"ARM_ensure_church_support"}
        n21{"ARM_utilize_the_diaspora"}
    end
    subgraph tier_3["Tier 3"]
        n22{"ARM_reestablish_the_republic"}
        n23{"ARM_the_triumph_over_communism"}
    end
    subgraph tier_4["Tier 4"]
        n24["ARM_armenian_youth_federation"]
        n25["ARM_empower_the_nationalists"]
        n26["ARM_implement_liberal_reforms"]
        n27["ARM_organize_the_institutions"]
        n28["ARM_the_last_claimant"]
        n29["ARM_war_propaganda"]
    end
    subgraph tier_5["Tier 5"]
        n30["ARM_acquire_diaspora_funding"]
        n31["ARM_hayk_youth"]
        n32{"ARM_mend_the_split"}
        n33["ARM_nakhchivan_population_exchange"]
        n34["ARM_planned_defense_policy"]
        n35["ARM_repression_apparatus"]
        n36["ARM_resettle_trabzon"]
        n37["ARM_resettle_van"]
        n38["ARM_royal_guards"]
        n39["ARM_transfer_officers_of_armenian_descent"]
    end
    subgraph tier_6["Tier 6"]
        n40["ARM_build_the_bek_line"]
        n41["ARM_cherish_what_we_have"]
        n42{"ARM_faith_resilience_heritage"}
        n43["ARM_join_the_allies"]
        n44["ARM_the_transcaucasian_accords"]
        n45["ARM_the_wilsonian_promise"]
    end
    subgraph tier_7["Tier 7"]
        n46["ARM_an_open_hand_to_turkey"]
        n47["ARM_extend_the_line_eastwards"]
        n48["ARM_irano_persian_diplomats"]
        n49["ARM_join_the_axis"]
        n50{"ARM_operation_nemesis_wasn_t_enough"}
        n51["ARM_saint_gregory_protects_our_skies"]
    end
    subgraph tier_8["Tier 8"]
        n52["ARM_dominate_the_caucasus"]
        n53["ARM_the_10th_crusade"]
    end
    subgraph tier_9["Tier 9"]
        n54["ARM_liberate_nagorno_karabakh"]
        n55["ARM_recapture_the_holy_land"]
        n56["ARM_reclaim_antiochia"]
        n57["ARM_vengeance_for_the_war_of_1918"]
    end
    subgraph tier_10["Tier 10"]
        n58["ARM_crush_the_soviet_yoke"]
        n59["ARM_defenders_of_jersualem_servants_of_god"]
    end
    n27 --> n30
    n41 --> n46
    n22 --> n24
    n34 --> n40
    n34 --> n41
    n57 --> n58
    n54 --> n58
    n56 --> n59
    n55 --> n59
    n50 --> n52
    n23 --> n25
    n19 --> n20
    n40 --> n47
    n38 --> n42
    n31 --> n42
    n25 --> n31
    n22 --> n26
    n41 --> n48
    n32 --> n43
    n42 --> n49
    n52 --> n54
    n24 --> n32
    n26 --> n32
    n29 --> n33
    n45 --> n50
    n22 --> n27
    n27 --> n34
    n53 --> n55
    n53 --> n56
    n21 --> n22
    n20 --> n22
    n28 --> n35
    n25 --> n35
    n29 --> n36
    n29 --> n37
    n17 --> n19
    n28 --> n38
    n40 --> n51
    n50 --> n53
    n42 --> n53
    n23 --> n28
    n32 --> n44
    n20 --> n23
    n38 --> n45
    n31 --> n45
    n27 --> n39
    n29 --> n39
    n19 --> n21
    n52 --> n57
    n22 --> n29
    n23 --> n29
    n52 x--x n53
    n25 x--x n28
    n43 x--x n44
    n27 x--x n29
    n22 x--x n23
    n17 x--x n18
```

# ARM_socialist_governmental_autonomy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17["ARM_return_from_exile"]
        n18(("ARM_socialist_governmental_autonomy"))
    end
    subgraph tier_1["Tier 1"]
        n60{"ARM_party_involvement"}
        n61{"ARM_purge_the_trotskyist_dashnaks"}
    end
    subgraph tier_2["Tier 2"]
        n62["ARM_ambitious_production_quotas"]
        n63["ARM_enforce_state_atheism"]
        n64["ARM_mobilize_the_workers"]
        n65["ARM_reopen_etchmiadzin_seminary"]
        n66["ARM_utilize_the_nkvd"]
    end
    subgraph tier_3["Tier 3"]
        n67["ARM_fund_the_armenian_workers_union"]
    end
    subgraph tier_4["Tier 4"]
        n68{"ARM_build_the_kovkas_line"}
    end
    subgraph tier_5["Tier 5"]
        n69["ARM_join_the_comintern"]
        n70["ARM_the_transcaucasian_confederation"]
    end
    subgraph tier_6["Tier 6"]
        n71["ARM_armeno_soviet_research_program"]
        n72["ARM_keepers_of_the_south"]
    end
    n61 --> n62
    n69 --> n71
    n62 --> n68
    n67 --> n68
    n60 --> n63
    n61 --> n63
    n63 --> n67
    n65 --> n67
    n68 --> n69
    n69 --> n72
    n70 --> n72
    n60 --> n64
    n18 --> n60
    n18 --> n61
    n60 --> n65
    n68 --> n70
    n61 --> n66
    n63 x--x n65
    n69 x--x n70
    n17 x--x n18
```
