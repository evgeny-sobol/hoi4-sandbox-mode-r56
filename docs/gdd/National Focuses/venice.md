# VNZ_army_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("VNZ_army_effort"))
        n2["VNZ_reorganize_the_arsenals"]
    end
    subgraph tier_1["Tier 1"]
        n3["VNZ_doctrine_effort"]
        n4["VNZ_equipment_effort"]
        n5["VNZ_motorization_effort"]
    end
    subgraph tier_2["Tier 2"]
        n6["VNZ_armor_effort"]
        n7["VNZ_doctrine_effort_2"]
        n8["VNZ_equipment_effort_2"]
        n9["VNZ_field_hospitals"]
        n10["VNZ_military_intelligence"]
        n11["VNZ_naval_infantry"]
    end
    subgraph tier_3["Tier 3"]
        n12["VNZ_equipment_effort_3"]
        n13["VNZ_mechanization_effort"]
        n14["VNZ_military_academy"]
        n15["VNZ_modern_logistics"]
    end
    subgraph tier_4["Tier 4"]
        n16["VNZ_alpini"]
    end
    subgraph tier_5["Tier 5"]
        n17["VNZ_special_forces"]
    end
    n14 --> n16
    n5 --> n6
    n1 --> n3
    n3 --> n7
    n1 --> n4
    n4 --> n8
    n8 --> n12
    n5 --> n9
    n6 --> n13
    n8 --> n14
    n4 --> n10
    n9 --> n15
    n1 --> n5
    n2 --> n11
    n4 --> n11
    n16 --> n17
    n11 --> n17
```

# VNZ_aviation_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18(("VNZ_aviation_effort"))
    end
    subgraph tier_1["Tier 1"]
        n19{"VNZ_NAV_effort"}
        n20["VNZ_fighter_focus"]
    end
    subgraph tier_2["Tier 2"]
        n21["VNZ_aviation_effort_2"]
        n22["VNZ_bomber_focus"]
        n23["VNZ_long_range_naval_bomber"]
        n24["VNZ_production_effort_3"]
    end
    subgraph tier_3["Tier 3"]
        n25["VNZ_CAS_effort"]
        n26["VNZ_form_mechanics"]
    end
    subgraph tier_4["Tier 4"]
        n27["VNZ_jet_focus"]
    end
    n21 --> n25
    n18 --> n19
    n20 --> n21
    n19 --> n21
    n19 --> n22
    n18 --> n20
    n24 --> n26
    n21 --> n27
    n26 --> n27
    n22 --> n27
    n23 --> n27
    n19 --> n23
    n20 --> n24
    n19 --> n24
    n22 x--x n23
```

# VNZ_industrial_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28(("VNZ_industrial_effort"))
        n29["VNZ_political_effort"]
    end
    subgraph tier_1["Tier 1"]
        n30["VNZ_construction_effort"]
        n31["VNZ_deterrence_policy"]
        n32["VNZ_infrastructure_effort"]
        n33["VNZ_production_effort"]
    end
    subgraph tier_2["Tier 2"]
        n34{"VNZ_construction_effort_2"}
    end
    subgraph tier_3["Tier 3"]
        n35["VNZ_Invite_American"]
        n36["VNZ_Invite_German"]
        n37["VNZ_Invite_Soviets"]
        n38["VNZ_coastal_defense"]
        n39["VNZ_construction_effort_3"]
        n40["VNZ_marghera_chemical_industry"]
    end
    subgraph tier_4["Tier 4"]
        n41["VNZ_American_Air"]
        n42["VNZ_Automobile"]
        n43["VNZ_Futher_Investments"]
        n44["VNZ_German_Heavy"]
        n45["VNZ_Soviet_Heavy_Industry"]
        n46["VNZ_extra_tech_slot"]
        n47["VNZ_nuclear_effort"]
        n48["VNZ_secret_weapons"]
    end
    subgraph tier_5["Tier 5"]
        n49["VNZ_Licences"]
        n50["VNZ_expand_mining"]
        n51["VNZ_extra_tech_slot_2"]
    end
    n35 --> n41
    n35 --> n42
    n36 --> n42
    n37 --> n42
    n35 --> n43
    n36 --> n43
    n37 --> n43
    n36 --> n44
    n34 --> n35
    n34 --> n36
    n34 --> n37
    n41 --> n49
    n44 --> n49
    n45 --> n49
    n37 --> n45
    n34 --> n38
    n28 --> n30
    n32 --> n34
    n30 --> n34
    n33 --> n34
    n34 --> n39
    n29 --> n31
    n28 --> n31
    n46 --> n50
    n39 --> n46
    n46 --> n51
    n28 --> n32
    n34 --> n40
    n39 --> n47
    n28 --> n33
    n39 --> n48
    n35 x--x n36
    n35 x--x n37
    n36 x--x n37
```

# VNZ_naval_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n16["VNZ_alpini"]
        n4["VNZ_equipment_effort"]
        n52{"VNZ_naval_effort"}
    end
    subgraph tier_1["Tier 1"]
        n53["VNZ_flexible_navy"]
        n54["VNZ_large_navy"]
        n55["VNZ_reorient_towards_land_artillery"]
    end
    subgraph tier_2["Tier 2"]
        n56["VNZ_cruiser_effort"]
        n57["VNZ_naval_mine_warfare"]
        n2["VNZ_reorganize_the_arsenals"]
        n58["VNZ_submarine_effort"]
    end
    subgraph tier_3["Tier 3"]
        n59["VNZ_capital_ships_effort"]
        n60["VNZ_destroyer_effort"]
        n61["VNZ_naval_gunnery"]
        n11["VNZ_naval_infantry"]
        n62["VNZ_skilled_pilots"]
        n63["VNZ_stealth_upgrades"]
    end
    subgraph tier_4["Tier 4"]
        n64["VNZ_a_new_grand_fleet"]
        n17["VNZ_special_forces"]
    end
    n62 --> n64
    n56 --> n59
    n54 --> n56
    n53 --> n56
    n58 --> n60
    n52 --> n53
    n52 --> n54
    n56 --> n61
    n2 --> n11
    n4 --> n11
    n53 --> n57
    n55 --> n2
    n52 --> n55
    n58 --> n62
    n56 --> n62
    n16 --> n17
    n11 --> n17
    n58 --> n63
    n53 --> n58
    n54 --> n58
    n53 x--x n54
```

# VNZ_political_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28["VNZ_industrial_effort"]
        n29{"VNZ_political_effort"}
    end
    subgraph tier_1["Tier 1"]
        n31["VNZ_deterrence_policy"]
        n65["VNZ_leone_di_san_marco_party"]
        n66["VNZ_power_to_the_people"]
        n67["VNZ_union_with_italy"]
        n68["VNZ_venitian_fascism"]
    end
    subgraph tier_2["Tier 2"]
        n69["VNZ_defenders_of_saint_marc"]
        n70{"VNZ_internal_security_initiative"}
        n71["VNZ_rally_the_industrialists"]
        n72{"VNZ_strikes_for_democracy"}
    end
    subgraph tier_3["Tier 3"]
        n73["VNZ_economic_mobilisation"]
        n74["VNZ_expand_the_terra_ferma"]
        n75{"VNZ_neutrality_focus"}
        n76{"VNZ_representative_grand_council"}
        n77{"VNZ_secure_security_ministry"}
    end
    subgraph tier_4["Tier 4"]
        n78["VNZ_Anti_Invasion"]
        n79["VNZ_absolute_dedication"]
        n80["VNZ_find_fascist_allies"]
        n81["VNZ_industrial_modernization"]
        n82{"VNZ_interventionism_focus"}
        n83["VNZ_reintegrate_dalmatia"]
        n84["VNZ_republic_army"]
        n85["VNZ_secure_international_protection"]
        n86["VNZ_take_over_the_government"]
    end
    subgraph tier_5["Tier 5"]
        n87["VNZ_Brigades"]
        n88["VNZ_Collectivist_Propaganda"]
        n89["VNZ_Military_Build"]
        n90["VNZ_enforce_atheism"]
        n91["VNZ_steel_production_plan"]
    end
    subgraph tier_6["Tier 6"]
        n92["VNZ_why_we_fight"]
    end
    n75 --> n78
    n82 --> n87
    n86 --> n88
    n75 --> n89
    n82 --> n89
    n74 --> n79
    n73 --> n79
    n65 --> n69
    n68 --> n69
    n29 --> n31
    n28 --> n31
    n71 --> n73
    n68 --> n73
    n86 --> n90
    n69 --> n74
    n73 --> n80
    n77 --> n81
    n76 --> n81
    n65 --> n70
    n70 --> n82
    n76 --> n82
    n77 --> n82
    n29 --> n65
    n70 --> n75
    n29 --> n66
    n68 --> n71
    n65 --> n71
    n74 --> n83
    n72 --> n76
    n76 --> n84
    n76 --> n85
    n72 --> n77
    n81 --> n91
    n66 --> n72
    n77 --> n86
    n29 --> n67
    n29 --> n68
    n78 --> n92
    n89 --> n92
    n87 --> n92
    n78 x--x n89
    n82 x--x n75
    n65 x--x n68
    n76 x--x n77
```
