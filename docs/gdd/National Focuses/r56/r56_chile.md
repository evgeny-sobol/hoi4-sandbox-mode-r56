# CHL_consolidate_the_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CHL_consolidate_the_government"))
        n2["CHL_expand_private_sector"]
        n3["CHL_the_popular_front"]
        n4["CHL_the_spread_of_fascism"]
    end
    subgraph tier_1["Tier 1"]
        n5["CHL_supress_the_nacistas"]
        n6["CHL_win_the_liberals"]
    end
    subgraph tier_2["Tier 2"]
        n7["CHL_crackdown"]
    end
    subgraph tier_3["Tier 3"]
        n8["CHL_central_bank"]
    end
    subgraph tier_4["Tier 4"]
        n9["CHL_argentine_alliance"]
        n10["CHL_reestablish_the_republican_guard_r56"]
    end
    subgraph tier_5["Tier 5"]
        n11["CHL_expand_alliance"]
        n12["CHL_preemptive_measures"]
    end
    subgraph tier_6["Tier 6"]
        n13["CHL_preemptive_strike"]
    end
    n8 --> n9
    n7 --> n8
    n6 --> n7
    n9 --> n11
    n10 --> n12
    n12 --> n13
    n8 --> n10
    n2 --> n10
    n3 --> n5
    n1 --> n5
    n1 --> n6
    n1 x--x n3
    n1 x--x n4
```

# CHL_establish_the_airforce

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14{"CHL_establish_the_airforce"}
        n15["CHL_reform_the_army"]
        n16["CHL_universities"]
    end
    subgraph tier_1["Tier 1"]
        n17["CHL_bomber_focus"]
        n18["CHL_cas_focus"]
        n19["CHL_paratroopers"]
    end
    subgraph tier_2["Tier 2"]
        n20["CHL_air_doctrine"]
        n21["CHL_bomber_focus_2"]
        n22["CHL_fighter"]
        n23["CHL_heavy_bomber_focus"]
        n24["CHL_heavy_fighter_focus"]
    end
    subgraph tier_3["Tier 3"]
        n25["CHL_jet_focus"]
    end
    subgraph tier_4["Tier 4"]
        n26["CHL_rockets"]
    end
    n18 --> n20
    n17 --> n20
    n14 --> n17
    n17 --> n21
    n14 --> n18
    n18 --> n22
    n17 --> n23
    n18 --> n24
    n20 --> n25
    n15 --> n19
    n14 --> n19
    n25 --> n26
    n16 --> n26
    n17 x--x n18
```

# CHL_isi_idea

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n27(("CHL_isi_idea"))
        n25["CHL_jet_focus"]
    end
    subgraph tier_1["Tier 1"]
        n28["CHL_establish_corfo_r56"]
    end
    subgraph tier_2["Tier 2"]
        n29["CHL_cap_steel"]
        n30["CHL_mining_technologies"]
    end
    subgraph tier_3["Tier 3"]
        n31["CHL_famae"]
        n32["CHL_invest_further_in_electronics"]
        n33["CHL_public_works_r56"]
    end
    subgraph tier_4["Tier 4"]
        n34["CHL_efe_rail"]
        n35["CHL_expand_our_arsenal"]
        n16["CHL_universities"]
        n36{"CHL_urbanisation_focus"}
    end
    subgraph tier_5["Tier 5"]
        n37["CHL_land_reform"]
        n38["CHL_land_reform_auth"]
        n26["CHL_rockets"]
        n39["CHL_steel"]
    end
    subgraph tier_6["Tier 6"]
        n40["CHL_full_recovery"]
    end
    subgraph tier_7["Tier 7"]
        n41["CHL_nuclear_focus"]
        n42["CHL_oil_in_the_tierra_del_fuego"]
    end
    subgraph tier_8["Tier 8"]
        n43["CHL_military_research_institute"]
    end
    n28 --> n29
    n32 --> n34
    n27 --> n28
    n31 --> n35
    n29 --> n31
    n37 --> n40
    n38 --> n40
    n30 --> n32
    n36 --> n37
    n36 --> n38
    n41 --> n43
    n42 --> n43
    n28 --> n30
    n40 --> n41
    n39 --> n41
    n34 --> n42
    n40 --> n42
    n30 --> n33
    n29 --> n33
    n25 --> n26
    n16 --> n26
    n35 --> n39
    n32 --> n16
    n33 --> n36
    n37 x--x n38
```

# CHL_reform_the_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14["CHL_establish_the_airforce"]
        n44["CHL_naval_doctrine"]
        n15{"CHL_reform_the_army"}
    end
    subgraph tier_1["Tier 1"]
        n45["CHL_andean_warfare"]
        n46["CHL_infantry_focus"]
        n47["CHL_mobility_focus"]
        n19["CHL_paratroopers"]
    end
    subgraph tier_2["Tier 2"]
        n48["CHL_armour_effort"]
        n49["CHL_artillery_f"]
        n50["CHL_marines_focus"]
        n51["CHL_mechanized"]
        n52["CHL_support"]
    end
    subgraph tier_3["Tier 3"]
        n53["CHL_armour_more"]
        n54["CHL_doctrine"]
    end
    n15 --> n45
    n47 --> n48
    n51 --> n53
    n48 --> n53
    n46 --> n49
    n49 --> n54
    n48 --> n54
    n52 --> n54
    n51 --> n54
    n15 --> n46
    n44 --> n50
    n45 --> n50
    n47 --> n51
    n15 --> n47
    n15 --> n19
    n14 --> n19
    n46 --> n52
    n46 x--x n47
```

# CHL_restore_the_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n45["CHL_andean_warfare"]
        n55{"CHL_restore_the_navy"}
    end
    subgraph tier_1["Tier 1"]
        n56["CHL_expand_magallanes_valparasio"]
        n57["CHL_expand_talcahuano"]
        n58["CHL_naval_aviation_focus"]
        n59["CHL_surface_fleet_focus"]
    end
    subgraph tier_2["Tier 2"]
        n60["CHL_cruiser_focus"]
        n61["CHL_destroyer_focus"]
        n62["CHL_naval_bomber_focus"]
        n63["CHL_naval_fighter_focus"]
    end
    subgraph tier_3["Tier 3"]
        n44["CHL_naval_doctrine"]
    end
    subgraph tier_4["Tier 4"]
        n50["CHL_marines_focus"]
    end
    n59 --> n60
    n58 --> n60
    n59 --> n61
    n55 --> n56
    n55 --> n57
    n44 --> n50
    n45 --> n50
    n55 --> n58
    n58 --> n62
    n61 --> n44
    n60 --> n44
    n58 --> n63
    n55 --> n59
    n58 x--x n59
```

# CHL_the_popular_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n64["CHL_axis"]
        n8["CHL_central_bank"]
        n1["CHL_consolidate_the_government"]
        n3(("CHL_the_popular_front"))
        n4["CHL_the_spread_of_fascism"]
    end
    subgraph tier_1["Tier 1"]
        n65["CHL_spanish_civil_war_involvement"]
        n5["CHL_supress_the_nacistas"]
        n66{"CHL_trade_deals"}
    end
    subgraph tier_2["Tier 2"]
        n67["CHL_a_truly_radical_party"]
        n68["CHL_liberalism_over_socialism"]
    end
    subgraph tier_3["Tier 3"]
        n2["CHL_expand_private_sector"]
        n69["CHL_nationalise_all"]
    end
    subgraph tier_4["Tier 4"]
        n70["CHL_ban_capitalism"]
        n71{"CHL_communist_militias"}
        n72["CHL_join_allies"]
        n10["CHL_reestablish_the_republican_guard_r56"]
    end
    subgraph tier_5["Tier 5"]
        n73{"CHL_comintern"}
        n74{"CHL_communist_faction"}
        n12["CHL_preemptive_measures"]
    end
    subgraph tier_6["Tier 6"]
        n75["CHL_anti_americanism"]
        n76["CHL_communist_argentina_alliance"]
        n77["CHL_communist_argentina_war"]
        n13["CHL_preemptive_strike"]
    end
    subgraph tier_7["Tier 7"]
        n78["CHL_growing_communist_faction"]
    end
    subgraph tier_8["Tier 8"]
        n79["CHL_ideological_propaganda"]
        n80["CHL_invite_red_bolivia"]
        n81["CHL_invite_red_paraguay"]
        n82["CHL_invite_red_uruguay"]
    end
    n66 --> n67
    n64 --> n75
    n73 --> n75
    n69 --> n70
    n71 --> n73
    n74 --> n76
    n73 --> n76
    n74 --> n77
    n73 --> n77
    n71 --> n74
    n69 --> n71
    n68 --> n2
    n77 --> n78
    n76 --> n78
    n78 --> n79
    n78 --> n80
    n78 --> n81
    n78 --> n82
    n2 --> n72
    n66 --> n68
    n67 --> n69
    n10 --> n12
    n12 --> n13
    n8 --> n10
    n2 --> n10
    n3 --> n65
    n4 --> n65
    n3 --> n5
    n1 --> n5
    n3 --> n66
    n67 x--x n68
    n73 x--x n74
    n76 x--x n77
    n1 x--x n3
    n3 x--x n4
```

# CHL_the_spread_of_fascism

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n73["CHL_comintern"]
        n1["CHL_consolidate_the_government"]
        n3["CHL_the_popular_front"]
        n4(("CHL_the_spread_of_fascism"))
    end
    subgraph tier_1["Tier 1"]
        n83["CHL_ban_communism"]
        n65["CHL_spanish_civil_war_involvement"]
        n84["CHL_the_leader"]
    end
    subgraph tier_2["Tier 2"]
        n85["CHL_fascist_constitution"]
        n86["CHL_patriotic_leagues"]
    end
    subgraph tier_3["Tier 3"]
        n87{"CHL_claims_on_argentina"}
        n88{"CHL_german_ties"}
        n89["CHL_northern_expansion"]
    end
    subgraph tier_4["Tier 4"]
        n64["CHL_axis"]
        n90["CHL_hispanic_pan_nationalism"]
    end
    subgraph tier_5["Tier 5"]
        n75["CHL_anti_americanism"]
        n91["CHL_claims_on_uruguay"]
    end
    n64 --> n75
    n73 --> n75
    n88 --> n64
    n4 --> n83
    n86 --> n87
    n85 --> n87
    n90 --> n91
    n64 --> n91
    n83 --> n85
    n84 --> n85
    n85 --> n88
    n87 --> n90
    n86 --> n89
    n84 --> n86
    n3 --> n65
    n4 --> n65
    n4 --> n84
    n64 x--x n90
    n1 x--x n4
    n3 x--x n4
```
