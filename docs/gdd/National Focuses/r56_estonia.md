# EST_election_boycotts

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("EST_election_boycotts"))
        n2["EST_national_assembly_election"]
    end
    subgraph tier_1["Tier 1"]
        n3["EST_communist_victory"]
        n4["EST_constitutional_referendumm"]
        n5["EST_jaan_tonison"]
    end
    subgraph tier_2["Tier 2"]
        n6["EST_baltic_entente"]
        n7["EST_departmentalization"]
        n8["EST_free_education"]
        n9["EST_land_ownership"]
        n10["EST_remove_soviet_sympathizers"]
        n11["EST_social_security"]
    end
    subgraph tier_3["Tier 3"]
        n12["EST_agriculture_coopoeratives"]
        n13["EST_combat_unemployment"]
        n14["EST_democratization_of_the_army"]
        n15["EST_estonianization"]
        n16["EST_german_admiration"]
        n17["EST_salary_raise"]
    end
    subgraph tier_4["Tier 4"]
        n18["EST_estonian_volunteer_regiment"]
        n19["EST_military_assistance"]
        n20["EST_protect_trade"]
        n21["EST_reorganize_taxation"]
    end
    subgraph tier_5["Tier 5"]
        n22["EST_demmand_friendship"]
    end
    n10 --> n12
    n5 --> n6
    n11 --> n13
    n1 --> n3
    n1 --> n4
    n14 --> n22
    n21 --> n22
    n8 --> n14
    n4 --> n7
    n16 --> n18
    n10 --> n15
    n5 --> n15
    n3 --> n8
    n7 --> n16
    n9 --> n16
    n1 --> n5
    n4 --> n9
    n16 --> n19
    n15 --> n20
    n6 --> n20
    n5 --> n10
    n4 --> n10
    n17 --> n21
    n13 --> n21
    n11 --> n17
    n3 --> n11
    n1 x--x n2
```

# EST_national_assembly_election

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["EST_election_boycotts"]
        n2(("EST_national_assembly_election"))
    end
    subgraph tier_1["Tier 1"]
        n23["EST_adopt_the_third_constiution"]
        n24["EST_bypass_the_riigikogu"]
    end
    subgraph tier_2["Tier 2"]
        n25["EST_amnesty_for_opponents"]
        n26["EST_disband_student_councils"]
        n27["EST_economic_stimulous"]
    end
    subgraph tier_3["Tier 3"]
        n28["EST_appoint_fredrich_karl_akel"]
        n29["EST_under_representation"]
    end
    subgraph tier_4["Tier 4"]
        n30["EST_soviet_estonian_treaty"]
    end
    n2 --> n23
    n24 --> n25
    n23 --> n25
    n25 --> n28
    n26 --> n28
    n2 --> n24
    n24 --> n26
    n23 --> n26
    n24 --> n27
    n23 --> n27
    n28 --> n30
    n29 --> n30
    n25 --> n29
    n26 --> n29
    n1 x--x n2
```
