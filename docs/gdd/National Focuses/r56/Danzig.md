# DNZ_danzig_senate

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"DNZ_danzig_senate"}
    end
    subgraph tier_1["Tier 1"]
        n2["DNZ_maintain_status_quo"]
        n3["DNZ_remove_lester"]
    end
    subgraph tier_2["Tier 2"]
        n4["DNZ_reconcile_with_lester"]
        n5["DNZ_strenghten_the_security_apparatus"]
    end
    subgraph tier_3["Tier 3"]
        n6["DNZ_cooperate_with_league_of_nations"]
        n7["DNZ_dissolve_the_zentrum_party"]
    end
    subgraph tier_4["Tier 4"]
        n8["DNZ_prussia_legacy"]
    end
    n4 --> n6
    n3 --> n7
    n5 --> n7
    n1 --> n2
    n7 --> n8
    n2 --> n4
    n1 --> n3
    n3 --> n5
    n2 x--x n3
```

# DNZ_industrial_investments

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n9(("DNZ_industrial_investments"))
    end
    subgraph tier_1["Tier 1"]
        n10["DNZ_maintain_infrastructure"]
        n11["DNZ_workers_front"]
    end
    subgraph tier_2["Tier 2"]
        n12["DNZ_building_industry"]
    end
    subgraph tier_3["Tier 3"]
        n13["DNZ_modernize_the_port"]
        n14["DNZ_support_german_businesses"]
    end
    subgraph tier_4["Tier 4"]
        n15["DNZ_business_contacts_abroad"]
        n16["DNZ_german_industrial_ties"]
    end
    subgraph tier_5["Tier 5"]
        n17["DNZ_german_technology"]
    end
    subgraph tier_6["Tier 6"]
        n18["DNZ_deutsches_physik"]
        n19["DNZ_hanseatic_ingenuity"]
    end
    n11 --> n12
    n10 --> n12
    n13 --> n15
    n17 --> n18
    n14 --> n16
    n16 --> n17
    n15 --> n17
    n17 --> n19
    n9 --> n10
    n12 --> n13
    n12 --> n14
    n9 --> n11
```

# DNZ_modernize_the_police

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20(("DNZ_modernize_the_police"))
    end
    subgraph tier_1["Tier 1"]
        n21["DNZ_civic_guard"]
        n22["DNZ_danzig_military_institute"]
        n23["DNZ_planned_militarization"]
    end
    subgraph tier_2["Tier 2"]
        n24{"DNZ_aviation_effort"}
        n25["DNZ_doctrine_effort"]
        n26["DNZ_smuggle_weapons"]
    end
    subgraph tier_3["Tier 3"]
        n27["DNZ_bomber_focus"]
        n28["DNZ_equipment_effort"]
        n29["DNZ_equipment_effort_3"]
        n30["DNZ_fighter_focus"]
        n31["DNZ_motorization_effort"]
    end
    subgraph tier_4["Tier 4"]
        n32["DNZ_armor_effort"]
        n33["DNZ_aviation_effort_2"]
        n34["DNZ_special_forces"]
    end
    subgraph tier_5["Tier 5"]
        n35["DNZ_CAS_effort"]
    end
    subgraph tier_6["Tier 6"]
        n36{"DNZ_establish_the_danzig_navy"}
    end
    subgraph tier_7["Tier 7"]
        n37["DNZ_flexible_navy"]
        n38["DNZ_large_navy"]
    end
    subgraph tier_8["Tier 8"]
        n39["DNZ_cruiser_effort"]
        n40["DNZ_submarine_effort"]
    end
    subgraph tier_9["Tier 9"]
        n41["DNZ_capital_ships_effort"]
        n42["DNZ_destroyer_effort"]
    end
    n33 --> n35
    n31 --> n32
    n22 --> n24
    n27 --> n33
    n30 --> n33
    n24 --> n27
    n39 --> n41
    n20 --> n21
    n38 --> n39
    n37 --> n39
    n20 --> n22
    n40 --> n42
    n22 --> n25
    n26 --> n28
    n26 --> n29
    n34 --> n36
    n35 --> n36
    n24 --> n30
    n36 --> n37
    n36 --> n38
    n26 --> n31
    n20 --> n23
    n22 --> n26
    n28 --> n34
    n37 --> n40
    n38 --> n40
    n27 x--x n30
    n37 x--x n38
```
