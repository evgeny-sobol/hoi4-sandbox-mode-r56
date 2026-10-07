# URG_review_the_military_budget

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("URG_review_the_military_budget"))
    end
    subgraph tier_1["Tier 1"]
        n2["URG_expand_the_escuela_militar"]
    end
    subgraph tier_2["Tier 2"]
        n3["URG_buy_czech_weapons"]
        n4["URG_purchase_bofors_cannons"]
    end
    subgraph tier_3["Tier 3"]
        n5{"URG_study_the_new_weaponry"}
    end
    subgraph tier_4["Tier 4"]
        n6["URG_an_oriental_rifle"]
        n7["URG_create_the_marine_corps"]
        n8["URG_invite_ford"]
        n9["URG_invite_vickers"]
        n10["URG_renovate_the_colonial_forts"]
    end
    subgraph tier_5["Tier 5"]
        n11["URG_create_the_military_engineering_school"]
        n12["URG_expand_the_CIACA"]
        n13["URG_mechanize_the_troops"]
    end
    subgraph tier_6["Tier 6"]
        n14["URG_create_the_direccion_de_sanidad"]
        n15["URG_modernize_the_arsenal"]
    end
    n5 --> n6
    n2 --> n3
    n11 --> n14
    n13 --> n14
    n5 --> n7
    n6 --> n11
    n10 --> n12
    n7 --> n12
    n1 --> n2
    n5 --> n8
    n5 --> n9
    n8 --> n13
    n9 --> n13
    n11 --> n15
    n12 --> n15
    n2 --> n4
    n5 --> n10
    n3 --> n5
    n4 --> n5
    n8 x--x n9
```

# URG_the_terra_dictatorship

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n16(("URG_the_terra_dictatorship"))
    end
    subgraph tier_1["Tier 1"]
        n17["URG_authoritarian_liberalism"]
        n18["URG_legalize_female_suffrage"]
        n19["URG_solidarismo"]
    end
    subgraph tier_2["Tier 2"]
        n20["URG_constitutional_reforms"]
    end
    subgraph tier_3["Tier 3"]
        n21["URG_axis_loans"]
        n22["URG_crackdown_on_the_revolutionaries"]
    end
    subgraph tier_4["Tier 4"]
        n23{"URG_1938_elections"}
    end
    subgraph tier_5["Tier 5"]
        n24["URG_blanco_victory"]
        n25["URG_colorado_victory"]
        n26{"URG_seize_the_opprotunity"}
        n27["URG_socialist_victory"]
    end
    subgraph tier_6["Tier 6"]
        n28["URG_americanismo"]
        n29{"URG_communist_revolution"}
        n30["URG_curtail_fascist_influence"]
        n31["URG_destroy_bipartidism"]
        n32["URG_education_reforms"]
        n33["URG_enshrine_worker_rights"]
        n34["URG_expand_the_ministerio_de_relaciones_exteriores"]
        n35["URG_further_batllist_reforms"]
        n36["URG_privatization_efforts"]
        n37["URG_revisionist_coup"]
        n38["URG_western_commercial_relations"]
        n39["URG_work_with_the_PCU"]
    end
    subgraph tier_7["Tier 7"]
        n40["URG_ban_the_partido_nacional"]
        n41["URG_cooperate_with_colorado_politicians"]
        n42["URG_cooperate_with_the_bonete_nazis"]
        n43["URG_embrace_our_catholic_heritage"]
        n44["URG_government_purges"]
        n45["URG_memories_of_the_council"]
        n46["URG_modify_the_terrist_constitution"]
        n47["URG_nationalize_foreign_monopolies"]
        n48["URG_reapproach_the_soviet_union"]
        n49["URG_reformism"]
        n50["URG_ruralismo"]
        n51["URG_sever_relations_with_the_axis"]
    end
    subgraph tier_8["Tier 8"]
        n52["URG_anti_statism"]
        n53["URG_create_the_JUP"]
        n54{"URG_empower_the_CGT"}
        n55["URG_execute_the_golpe_bueno"]
        n56["URG_militarize_the_society"]
        n57["URG_one_union_for_all_workers"]
        n58["URG_purge_batllist_influence"]
        n59["URG_traditionalism"]
        n60["URG_workers_militias"]
    end
    subgraph tier_9["Tier 9"]
        n61{"URG_glorify_the_gaucho"}
        n62["URG_public_works_projects"]
        n63{"URG_reorganise_the_economy"}
        n64["URG_social_reforms"]
        n65["URG_undo_batllist_reforms"]
        n66["URG_work_with_the_anarchists"]
        n67["URG_work_with_the_batllists"]
    end
    subgraph tier_10["Tier 10"]
        n68{"URG_champion_of_the_people"}
        n69{"URG_democracia_y_paz"}
        n70["URG_follow_moscow"]
        n71["URG_join_the_axis"]
        n72{"URG_legacy_of_saravia"}
        n73["URG_the_american_revolution"]
        n74["URG_we_stand_alone"]
    end
    subgraph tier_11["Tier 11"]
        n75["URG_expand_the_montevideo_treaty"]
        n76["URG_join_the_allies"]
        n77["URG_platine_ambitions"]
        n78["URG_switzerland_of_the_americas"]
        n79["URG_the_dream_of_artigas"]
    end
    subgraph tier_12["Tier 12"]
        n80["URG_across_the_uruguay_river"]
        n81["URG_libertad_o_muerte"]
        n82["URG_march_on_buenos_aires"]
        n83["URG_retake_the_misiones_orientales"]
        n84["URG_take_a_stance"]
    end
    subgraph tier_13["Tier 13"]
        n85["URG_cross_the_andes"]
        n86["URG_march_northwards"]
        n87["URG_repeat_the_paraguayan_war"]
        n88{"URG_tiranos_temblad"}
    end
    subgraph tier_14["Tier 14"]
        n89["URG_la_patria_o_la_tumba"]
        n90["URG_protect_the_revolution"]
        n91["URG_spread_the_revolution"]
    end
    n21 --> n23
    n22 --> n23
    n79 --> n80
    n24 --> n28
    n50 --> n52
    n16 --> n17
    n20 --> n21
    n29 --> n40
    n23 --> n24
    n67 --> n68
    n66 --> n68
    n23 --> n25
    n26 --> n29
    n18 --> n20
    n17 --> n20
    n19 --> n20
    n29 --> n41
    n37 --> n42
    n20 --> n22
    n42 --> n53
    n82 --> n85
    n25 --> n30
    n64 --> n69
    n62 --> n69
    n27 --> n31
    n25 --> n32
    n24 --> n32
    n37 --> n43
    n49 --> n54
    n48 --> n54
    n27 --> n33
    n46 --> n55
    n51 --> n55
    n25 --> n34
    n69 --> n75
    n72 --> n75
    n68 --> n75
    n63 --> n70
    n27 --> n35
    n58 --> n61
    n56 --> n61
    n53 --> n61
    n29 --> n44
    n69 --> n76
    n72 --> n76
    n68 --> n76
    n61 --> n71
    n87 --> n89
    n85 --> n89
    n86 --> n89
    n65 --> n72
    n16 --> n18
    n75 --> n81
    n78 --> n81
    n76 --> n81
    n82 --> n86
    n77 --> n82
    n32 --> n45
    n43 --> n56
    n30 --> n46
    n31 --> n47
    n44 --> n57
    n41 --> n57
    n71 --> n77
    n74 --> n77
    n24 --> n36
    n88 --> n90
    n55 --> n62
    n42 --> n58
    n43 --> n58
    n39 --> n48
    n35 --> n49
    n33 --> n49
    n60 --> n63
    n57 --> n63
    n82 --> n87
    n79 --> n83
    n26 --> n37
    n28 --> n50
    n36 --> n50
    n23 --> n26
    n30 --> n51
    n34 --> n51
    n55 --> n64
    n23 --> n27
    n16 --> n19
    n88 --> n91
    n69 --> n78
    n72 --> n78
    n68 --> n78
    n75 --> n84
    n76 --> n84
    n63 --> n73
    n70 --> n79
    n73 --> n79
    n83 --> n88
    n80 --> n88
    n50 --> n59
    n59 --> n65
    n52 --> n65
    n61 --> n74
    n25 --> n38
    n27 --> n39
    n54 --> n66
    n54 --> n67
    n44 --> n60
    n41 --> n60
    n40 --> n60
    n24 x--x n25
    n24 x--x n26
    n24 x--x n27
    n25 x--x n26
    n25 x--x n27
    n29 x--x n37
    n41 x--x n44
    n75 x--x n76
    n75 x--x n78
    n70 x--x n73
    n76 x--x n78
    n71 x--x n74
    n90 x--x n91
    n26 x--x n27
    n66 x--x n67
```
