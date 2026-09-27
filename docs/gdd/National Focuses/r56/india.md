# RAJ_Linlithgows_Reign

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("RAJ_Linlithgows_Reign"))
        n2["RAJ_Provincial_Elections"]
    end
    subgraph tier_1["Tier 1"]
        n3["RAJ_Assemble_our_Cabinet"]
        n4["RAJ_assert_control_over_lhoyu"]
        n5["r56_RAJ_revolt_against_the_oppressors_showcase"]
    end
    subgraph tier_2["Tier 2"]
        n6["RAJ_Meet_with_the_Judiciary"]
        n7["RAJ_Meet_with_the_Legislative"]
    end
    subgraph tier_3["Tier 3"]
        n8["RAJ_Our_First_Order_of_Business"]
    end
    subgraph tier_4["Tier 4"]
        n9["RAJ_Agricultural_Stabilisation_Act"]
        n10["RAJ_Railway_Expansion_Act"]
        n11["RAJ_War_Powers_Act"]
    end
    subgraph tier_5["Tier 5"]
        n12["RAJ_Arms_Industry_Expansion"]
        n13["RAJ_Drought_Prevention_Measures"]
        n14["RAJ_Expand_Urban_Centers"]
        n15["RAJ_New_Excavation_Companies"]
        n16["RAJ_New_Industrial_Centers"]
        n17["RAJ_The_August_Offer"]
        n18["RAJ_encourage_mass_recruitment_r56"]
    end
    subgraph tier_6["Tier 6"]
        n19["RAJ_Civil_Aviation_Expansion"]
        n20["RAJ_Wheat_Exports"]
    end
    subgraph tier_7["Tier 7"]
        n21["RAJ_Educational_Reform_Act"]
        n22["RAJ_Insurance_Act"]
    end
    subgraph tier_8["Tier 8"]
        n23["RAJ_Bolster_our_Security_Forces"]
        n24["RAJ_Healthcare_Investments"]
        n25["RAJ_His_Majesties_University"]
        n26["RAJ_Primary_Education"]
    end
    subgraph tier_9["Tier 9"]
        n27["RAJ_Department_of_War_Studies"]
        n28["RAJ_Open_for_Business"]
    end
    n8 --> n9
    n11 --> n12
    n1 --> n3
    n22 --> n23
    n15 --> n19
    n16 --> n19
    n26 --> n27
    n25 --> n27
    n9 --> n13
    n20 --> n21
    n9 --> n14
    n22 --> n24
    n21 --> n25
    n19 --> n22
    n3 --> n6
    n3 --> n7
    n10 --> n15
    n10 --> n16
    n23 --> n28
    n24 --> n28
    n6 --> n8
    n7 --> n8
    n21 --> n26
    n8 --> n10
    n11 --> n17
    n8 --> n11
    n14 --> n20
    n13 --> n20
    n1 --> n4
    n2 --> n4
    n11 --> n18
    n1 --> n5
    n1 x--x n2
```

# RAJ_Provincial_Elections

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["RAJ_Linlithgows_Reign"]
        n2{"RAJ_Provincial_Elections"}
    end
    subgraph tier_1["Tier 1"]
        n29["RAJ_Independent_Labour_Party"]
        n30["RAJ_Indian_National_Congress"]
        n31["RAJ_Unionist_Party"]
        n4["RAJ_assert_control_over_lhoyu"]
    end
    subgraph tier_2["Tier 2"]
        n32{"RAJ_Appeal_to_Anglo_Indians"}
        n33["RAJ_Gather_Industrial_Funds"]
        n34{"RAJ_National_Unity"}
        n35["RAJ_Nehrus_Candidacy"]
        n36["RAJ_New_Leadership"]
        n37["RAJ_Organize_a_Conference"]
        n38["RAJ_Prepare_the_Lucknow_Session"]
    end
    subgraph tier_3["Tier 3"]
        n39["RAJ_Ally_with_the_Muslim_League"]
        n40["RAJ_An_Offer_for_Rajagopalachari"]
        n41["RAJ_Appeal_to_the_Lower_Castes"]
        n42{"RAJ_Azads_Support"}
        n43["RAJ_Content_for_British_Rule"]
        n44{"RAJ_Danges_Influence"}
        n45["RAJ_Establish_a_Precense_in_Sindh"]
        n46["RAJ_Fight_the_Muslim_League"]
        n47{"RAJ_Nehrus_Campaign"}
        n48{"RAJ_Pillais_Influence"}
        n49["RAJ_Subvert_Stalinist_Influence"]
    end
    subgraph tier_4["Tier 4"]
        n50["RAJ_Appeal_to_the_Peasentry"]
        n51["RAJ_Broaden_our_Coalition"]
        n52["RAJ_Centralize_the_Party"]
        n53["RAJ_Local_Organization"]
        n54["RAJ_Secure_Rural_Hindus"]
        n55["RAJ_Siphon_Congress_Ministers"]
    end
    subgraph tier_5["Tier 5"]
        n56["RAJ_A_Society_of_All_Classes"]
        n57["RAJ_Democracy_and_Socialism"]
        n58["RAJ_India_United_under_Britain"]
    end
    subgraph tier_6["Tier 6"]
        n59{"RAJ_Assemble_the_Constitutional_Assembly"}
        n60["RAJ_Integrate_the_Princely_States"]
        n61["RAJ_Intervention_in_Pakistan"]
        n62["RAJ_Launch_The_Quit_India_Movement"]
        n63["RAJ_Offer_the_British_Concessions"]
        n64["RAJ_Seize_Influence_from_Upper_Castes"]
        n65["RAJ_Seize_the_Means"]
        n66["RAJ_Sit_Down_with_the_Farmers"]
        n67["RAJ_The_Liberation_of_South_Asia"]
    end
    subgraph tier_7["Tier 7"]
        n68["RAJ_Central_Bureau_of_Investigation"]
        n69["RAJ_Combat_Institutional_Corruption"]
        n70["RAJ_Dismantle_the_Judicial_System"]
        n71["RAJ_Establish_a_National_Government"]
        n72["RAJ_Expand_our_Ordance_Industry"]
        n73["RAJ_Implement_Equal_Education"]
        n74{"RAJ_Jinnahs_Kingdom"}
        n75["RAJ_Nehrus_Vision_for_India"]
        n76["RAJ_Overthrow_the_Rana_dynasty"]
        n77["RAJ_Reestablish_our_Armed_Forces"]
        n78["RAJ_Strengthen_Liberal_Elements"]
        n79["RAJ_The_Bhutanese_Revolt"]
        n80["RAJ_The_Ceylon_Emergency"]
        n81{"RAJ_The_Remaining_Ports"}
        n82["RAJ_Token_Social_Reform"]
        n83["RAJ_of_Distribution"]
        n84["RAJ_of_Production"]
    end
    subgraph tier_8["Tier 8"]
        n85["RAJ_A_New_Movement"]
        n86["RAJ_Abolish_the_Reservation_System"]
        n87["RAJ_Answer_The_Call"]
        n88["RAJ_Connect_the_Rural_Areas"]
        n89["RAJ_Cut_down_on_Tariffs"]
        n90["RAJ_Expand_Healthcare_Facilities"]
        n91["RAJ_Extensive_Agricultural_Subsidies"]
        n92["RAJ_Indo_Soviet_Friendship_Treaty"]
        n93["RAJ_Placate_the_Nobles"]
        n94["RAJ_Reform_our_Police_Force"]
        n95["RAJ_Reproachment_with_the_West"]
        n96{"RAJ_Revise_Taxation_Policies"}
        n97{"RAJ_Take_back_the_Ports"}
        n98["RAJ_The_Ones_Who_Got_Away"]
        n99["RAJ_The_Third_International"]
        n100["RAJ_Unity_in_India"]
        n101["RAJ_Want_Peace_Prepare_for_War"]
        n102{"RAJ_of_Exchange"}
    end
    subgraph tier_9["Tier 9"]
        n103["RAJ_A_New_Way_Forward"]
        n104["RAJ_Asian_Anti_Colonialism"]
        n105["RAJ_Bind_South_Asia_Closer"]
        n106{"RAJ_Establish_The_Revolutionary_Guard"}
        n107["RAJ_Federalize_Education"]
        n108["RAJ_Foster_Mining_Jobs"]
        n109["RAJ_Institute_The_Draft"]
        n110["RAJ_Internal_Security_Act"]
        n111["RAJ_Invite_International_Theorists"]
        n112["RAJ_Invite_Soviet_Planners"]
        n113["RAJ_Loosen_Rupee_Exchange"]
        n114["RAJ_No_Resentments"]
        n115["RAJ_Outwards_to_the_World"]
        n116["RAJ_Placate_the_British"]
        n117["RAJ_Socialist_Science"]
        n118["RAJ_The_Womens_Status"]
        n119["RAJ_Thorough_Corruption_Audits"]
    end
    subgraph tier_10["Tier 10"]
        n120["RAJ_A_Truly_Indian_Navy"]
        n121["RAJ_Agricultural_Collectivisation"]
        n122["RAJ_Aquire_War_Material"]
        n123["RAJ_Armed_Neutrality"]
        n124["RAJ_Bring_Democracy_to_South_Asia"]
        n125["RAJ_Caste_Reform"]
        n126["RAJ_Concessions_to_Princes"]
        n127["RAJ_Constitutional_Minority_Protections"]
        n128["RAJ_Emphasise_Anti_Colonialist_Sentiment"]
        n129["RAJ_Equal_Partners"]
        n130["RAJ_Establish_a_Central_Committee"]
        n131["RAJ_Expand_Delhi_University"]
        n132["RAJ_Expand_Soviet_Aid"]
        n133["RAJ_Federalisation"]
        n134["RAJ_Fighting_Tyranny_whereever_it_may_be"]
        n135["RAJ_Incentivize_Workplace_Democracy"]
        n136["RAJ_Military_Cooperation"]
        n137["RAJ_Mutual_Investments"]
        n138["RAJ_No_Compromises"]
        n139["RAJ_Protect_the_Arabian_Sea"]
        n140["RAJ_Reconect_broken_up_Industries"]
        n141["RAJ_Relieve_the_Administrative_Burden"]
        n142["RAJ_Technological_Cooperation"]
        n143["RAJ_The_Non_Aligned_Movement"]
    end
    subgraph tier_11["Tier 11"]
        n144["RAJ_Crackdown_on_Radicalism"]
        n145["RAJ_Rethink_Resource_Policy"]
    end
    n81 --> n85
    n74 --> n85
    n97 --> n103
    n96 --> n103
    n41 --> n56
    n53 --> n56
    n52 --> n56
    n109 --> n120
    n70 --> n86
    n112 --> n121
    n111 --> n121
    n32 --> n39
    n38 --> n40
    n72 --> n87
    n31 --> n32
    n37 --> n41
    n45 --> n50
    n46 --> n50
    n109 --> n122
    n103 --> n123
    n85 --> n104
    n99 --> n104
    n57 --> n59
    n38 --> n42
    n35 --> n42
    n99 --> n105
    n85 --> n105
    n114 --> n124
    n47 --> n51
    n42 --> n51
    n118 --> n125
    n107 --> n125
    n60 --> n68
    n48 --> n52
    n64 --> n69
    n106 --> n126
    n83 --> n88
    n107 --> n127
    n32 --> n43
    n131 --> n144
    n78 --> n89
    n36 --> n44
    n51 --> n57
    n54 --> n57
    n64 --> n70
    n103 --> n128
    n114 --> n129
    n90 --> n106
    n86 --> n106
    n69 --> n106
    n112 --> n130
    n60 --> n71
    n58 --> n71
    n34 --> n45
    n107 --> n131
    n73 --> n90
    n112 --> n132
    n66 --> n72
    n75 --> n91
    n116 --> n133
    n110 --> n133
    n100 --> n107
    n34 --> n46
    n109 --> n134
    n91 --> n108
    n31 --> n33
    n64 --> n73
    n111 --> n135
    n2 --> n29
    n43 --> n58
    n50 --> n58
    n55 --> n58
    n2 --> n30
    n75 --> n92
    n87 --> n109
    n93 --> n109
    n58 --> n60
    n57 --> n60
    n94 --> n110
    n93 --> n110
    n57 --> n61
    n102 --> n111
    n102 --> n112
    n67 --> n74
    n57 --> n62
    n44 --> n53
    n89 --> n113
    n105 --> n136
    n114 --> n137
    n115 --> n137
    n31 --> n34
    n35 --> n47
    n30 --> n35
    n59 --> n75
    n29 --> n36
    n106 --> n138
    n97 --> n114
    n96 --> n114
    n58 --> n63
    n29 --> n37
    n97 --> n115
    n96 --> n115
    n67 --> n76
    n36 --> n48
    n37 --> n48
    n93 --> n116
    n71 --> n93
    n66 --> n93
    n30 --> n38
    n114 --> n139
    n113 --> n140
    n60 --> n77
    n77 --> n94
    n71 --> n94
    n119 --> n141
    n78 --> n95
    n121 --> n145
    n111 --> n145
    n68 --> n96
    n47 --> n54
    n56 --> n64
    n56 --> n65
    n46 --> n55
    n39 --> n55
    n58 --> n66
    n99 --> n117
    n59 --> n78
    n37 --> n49
    n77 --> n97
    n105 --> n142
    n67 --> n79
    n67 --> n80
    n56 --> n67
    n103 --> n143
    n77 --> n98
    n67 --> n81
    n81 --> n99
    n74 --> n99
    n100 --> n118
    n89 --> n119
    n66 --> n82
    n2 --> n31
    n78 --> n100
    n75 --> n100
    n75 --> n101
    n1 --> n4
    n2 --> n4
    n65 --> n83
    n83 --> n102
    n84 --> n102
    n65 --> n84
    n85 x--x n99
    n103 x--x n114
    n103 x--x n115
    n39 x--x n46
    n51 x--x n54
    n52 x--x n53
    n126 x--x n138
    n29 x--x n30
    n29 x--x n31
    n30 x--x n31
    n111 x--x n112
    n1 x--x n2
    n75 x--x n78
    n114 x--x n115
```
