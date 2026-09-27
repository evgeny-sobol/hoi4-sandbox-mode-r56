# KAL_establishing_an_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"KAL_establishing_an_army"}
    end
    subgraph tier_1["Tier 1"]
        n2["KAL_moderate_cavalry_supremacy"]
        n3["KAL_our_equine_pride"]
        n4["KAL_winter_training"]
    end
    subgraph tier_2["Tier 2"]
        n5["KAL_establish_a_military_academy"]
        n6["KAL_scavenge_battlefield_equipment"]
    end
    subgraph tier_3["Tier 3"]
        n7["KAL_equipment_effort"]
        n8["KAL_establish_a_armor_corp"]
        n9["KAL_motorization_effort"]
    end
    subgraph tier_4["Tier 4"]
        n10["KAL_equipment_effort_2"]
        n11["KAL_equipment_effort_3"]
        n12["KAL_field_hospitals"]
        n13["KAL_mechanization_effort"]
        n14["KAL_signal_companies"]
    end
    subgraph tier_5["Tier 5"]
        n15["KAL_modern_logistics"]
        n16["KAL_special_forces"]
    end
    n5 --> n7
    n7 --> n10
    n7 --> n11
    n5 --> n8
    n3 --> n5
    n2 --> n5
    n9 --> n12
    n8 --> n13
    n9 --> n13
    n1 --> n2
    n12 --> n15
    n13 --> n15
    n14 --> n15
    n5 --> n9
    n1 --> n3
    n4 --> n6
    n3 --> n6
    n2 --> n6
    n8 --> n14
    n11 --> n16
    n10 --> n16
    n1 --> n4
    n2 x--x n3
```

# KAL_organize_the_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"KAL_organize_the_government"}
    end
    subgraph tier_1["Tier 1"]
        n18{"KAL_bring_in_exiled_nationalists"}
        n19{"KAL_internationalism"}
        n20["KAL_the_court_of_joinville_le_pont"]
        n21["KAL_trust_democratic_institutions"]
    end
    subgraph tier_2["Tier 2"]
        n22["KAL_finance_military_infrastructure"]
        n23["KAL_form_manufacturing_cooperatives"]
        n24["KAL_introduce_political_reforms"]
        n25["KAL_rally_behind_the_khan"]
        n26["KAL_reconcile_buddhism_and_socialism"]
        n27["KAL_reinstate_monasteries"]
        n28["KAL_state_atheism"]
        n29["KAL_the_kalmyk_flag_organization"]
    end
    subgraph tier_3["Tier 3"]
        n30["KAL_anti_revolutionary_decree"]
        n31["KAL_armament_production_plan"]
        n32["KAL_buddhist_society"]
        n33["KAL_building_a_kingdom"]
        n34["KAL_collectivist_propaganda"]
        n35["KAL_economic_optimization"]
        n36["KAL_form_a_royal_guard"]
        n37["KAL_revolutionary_pioneer_organizations"]
        n38["KAL_solidify_the_military_government"]
        n39["KAL_war_communism"]
    end
    subgraph tier_4["Tier 4"]
        n40["KAL_deterrence"]
        n41["KAL_five_year_plan"]
        n42["KAL_indoctrination_focus"]
        n43["KAL_prepare_the_youth_for_service"]
        n44["KAL_promote_militarism"]
        n45["KAL_promote_nichiren_buddhism"]
        n46["KAL_reinforce_the_security_apparatus"]
        n47["KAL_research_grants"]
        n48["KAL_royal_officer_corps"]
        n49["KAL_the_spirit_of_genghis"]
    end
    subgraph tier_5["Tier 5"]
        n50["KAL_claim_greater_mongolia"]
        n51["KAL_cult_of_personality"]
        n52["KAL_discipline_hierarchy_and_order"]
        n53["KAL_dominate_the_pontic_caspian_steppe"]
        n54["KAL_examplary_battle_leadership"]
        n55["KAL_propaganda_for_the_khagan_god"]
        n56["KAL_why_we_fight"]
    end
    subgraph tier_6["Tier 6"]
        n57["KAL_paramilitarism"]
        n58["KAL_red_army"]
        n59["KAL_stimulate_mongol_traditions_in_buryatia"]
        n60["KAL_stimulate_mongol_traditions_in_inner_mongolia"]
        n61["KAL_stimulate_mongol_traditions_in_mongolia"]
        n62["KAL_stimulate_mongol_traditions_in_tuva"]
        n63["KAL_take_leadership"]
    end
    subgraph tier_7["Tier 7"]
        n64["KAL_organize_our_alliance"]
    end
    n24 --> n30
    n20 --> n30
    n29 --> n31
    n25 --> n31
    n17 --> n18
    n27 --> n32
    n22 --> n33
    n49 --> n50
    n23 --> n34
    n42 --> n51
    n43 --> n51
    n35 --> n40
    n30 --> n40
    n44 --> n52
    n44 --> n53
    n45 --> n53
    n24 --> n35
    n44 --> n54
    n20 --> n22
    n34 --> n41
    n25 --> n36
    n20 --> n36
    n19 --> n23
    n37 --> n42
    n34 --> n42
    n17 --> n19
    n21 --> n24
    n63 --> n64
    n49 --> n64
    n52 --> n57
    n37 --> n43
    n31 --> n44
    n38 --> n44
    n31 --> n45
    n32 --> n55
    n49 --> n55
    n48 --> n55
    n18 --> n25
    n19 --> n26
    n51 --> n58
    n34 --> n46
    n29 --> n46
    n25 --> n46
    n20 --> n27
    n35 --> n47
    n26 --> n37
    n28 --> n37
    n36 --> n48
    n29 --> n38
    n19 --> n28
    n50 --> n59
    n50 --> n60
    n50 --> n61
    n50 --> n62
    n53 --> n63
    n17 --> n20
    n18 --> n29
    n36 --> n49
    n17 --> n21
    n23 --> n39
    n40 --> n56
    n18 x--x n19
    n18 x--x n20
    n18 x--x n21
    n19 x--x n20
    n19 x--x n21
    n25 x--x n29
    n26 x--x n28
    n20 x--x n21
```
