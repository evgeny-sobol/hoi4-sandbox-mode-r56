# SAF_air_expansion_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SAF_air_expansion_plan"))
        n2["SAF_expand_cape_town_yards"]
        n3["SAF_expand_durban_yards"]
        n4["SAF_organize_district_commands"]
    end
    subgraph tier_1["Tier 1"]
        n5["SAF_appoint_new_commander"]
    end
    subgraph tier_2["Tier 2"]
        n6{"SAF_formalize_air_doctrine"}
        n7["SAF_patrol_the_sea"]
        n8["SAF_replace_imperial_airways"]
    end
    subgraph tier_3["Tier 3"]
        n9["SAF_air_training_scheme"]
        n10["SAF_mobilize_the_bernard_institute"]
        n11["SAF_national_air_training"]
        n12["SAF_naval_aviation"]
        n13["SAF_seize_south_african_airways_aircrafts"]
    end
    subgraph tier_4["Tier 4"]
        n14["SAF_aircraft_modernization"]
        n15["SAF_the_prides_of_the_nation"]
    end
    n6 --> n9
    n6 --> n14
    n13 --> n14
    n1 --> n5
    n4 --> n5
    n5 --> n6
    n7 --> n10
    n6 --> n11
    n2 --> n12
    n3 --> n12
    n7 --> n12
    n5 --> n7
    n5 --> n8
    n8 --> n13
    n11 --> n15
    n9 --> n15
    n9 x--x n11
```

# SAF_cadets_of_the_general_botha

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n16(("SAF_cadets_of_the_general_botha"))
        n7["SAF_patrol_the_sea"]
    end
    subgraph tier_1["Tier 1"]
        n17{"SAF_establish_seaward_defense_force"}
    end
    subgraph tier_2["Tier 2"]
        n18["SAF_anti_submarine_equipment"]
        n19["SAF_torpedo_development"]
    end
    subgraph tier_3["Tier 3"]
        n2["SAF_expand_cape_town_yards"]
        n3["SAF_expand_durban_yards"]
    end
    subgraph tier_4["Tier 4"]
        n20["SAF_a_true_navy"]
        n12["SAF_naval_aviation"]
    end
    subgraph tier_5["Tier 5"]
        n21["SAF_naval_ambition"]
        n22["SAF_salisbury_island_base"]
    end
    n2 --> n20
    n3 --> n20
    n17 --> n18
    n16 --> n17
    n19 --> n2
    n18 --> n2
    n19 --> n3
    n18 --> n3
    n20 --> n21
    n2 --> n12
    n3 --> n12
    n7 --> n12
    n20 --> n22
    n17 --> n19
    n18 x--x n19
```

# SAF_ethnic_legislation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n23{"SAF_ethnic_legislation"}
        n24["SAF_sensibilize_the_africans"]
    end
    subgraph tier_1["Tier 1"]
        n25["SAF_policy_of_cooperation"]
        n26["SAF_push_the_unp_towards_independence"]
        n27["SAF_radicalize_the_afrikaner_broederbond"]
    end
    subgraph tier_2["Tier 2"]
        n28{"SAF_celebrate_the_voortrekkers"}
        n29["SAF_finance_legislation"]
        n30["SAF_guard_the_cape"]
        n31["SAF_research_cooperation"]
    end
    subgraph tier_3["Tier 3"]
        n32["SAF_commonwealth_industrial_cooperation"]
        n33["SAF_crush_ossewabrandwag"]
        n34["SAF_form_the_ossewabrandwag"]
        n35["SAF_remobilize_the_cape_corps"]
        n36["SAF_return_to_republicanism"]
        n37["SAF_the_aliens_act"]
    end
    subgraph tier_4["Tier 4"]
        n38{"SAF_build_a_new_state"}
        n39["SAF_expand_the_union"]
        n40["SAF_solidify_german_contacts"]
    end
    subgraph tier_5["Tier 5"]
        n41["SAF_axis_alliance"]
        n42["SAF_get_rid_of_the_british"]
        n43["SAF_laager_doctrine"]
        n44["SAF_relax_racial_laws"]
        n45["SAF_separation_policy"]
        n46["SAF_stormjaers_militias"]
    end
    subgraph tier_6["Tier 6"]
        n47["SAF_contact_rhodesian_afrikaners"]
        n48["SAF_sharpshooting_tradition"]
    end
    n40 --> n41
    n36 --> n38
    n27 --> n28
    n26 --> n28
    n31 --> n32
    n42 --> n47
    n30 --> n33
    n35 --> n39
    n33 --> n39
    n25 --> n29
    n28 --> n34
    n40 --> n42
    n25 --> n30
    n38 --> n43
    n23 --> n25
    n23 --> n26
    n23 --> n27
    n38 --> n44
    n30 --> n35
    n25 --> n31
    n28 --> n36
    n38 --> n45
    n46 --> n48
    n34 --> n40
    n40 --> n46
    n29 --> n37
    n23 x--x n24
    n34 x--x n36
    n25 x--x n26
    n25 x--x n27
    n26 x--x n27
    n44 x--x n45
```

# SAF_organize_district_commands

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["SAF_air_expansion_plan"]
        n2["SAF_expand_cape_town_yards"]
        n3["SAF_expand_durban_yards"]
        n49["SAF_magazine_hill_ammunition_plant"]
        n4(("SAF_organize_district_commands"))
    end
    subgraph tier_1["Tier 1"]
        n5["SAF_appoint_new_commander"]
        n50{"SAF_mission_to_europe"}
    end
    subgraph tier_2["Tier 2"]
        n6{"SAF_formalize_air_doctrine"}
        n7["SAF_patrol_the_sea"]
        n51["SAF_prepare_for_bush_warfare"]
        n52["SAF_prioritize_q_service_corps"]
        n53["SAF_prioritize_t_service_corps"]
        n8["SAF_replace_imperial_airways"]
    end
    subgraph tier_3["Tier 3"]
        n54["SAF_SAR_and_H_brigade"]
        n9["SAF_air_training_scheme"]
        n55["SAF_desert_specialization"]
        n56["SAF_jungle_specialization"]
        n57["SAF_local_tank_program"]
        n58["SAF_locally_built_armored_cars"]
        n10["SAF_mobilize_the_bernard_institute"]
        n11["SAF_national_air_training"]
        n12["SAF_naval_aviation"]
        n59["SAF_reform_staff_officers_training"]
        n13["SAF_seize_south_african_airways_aircrafts"]
    end
    subgraph tier_4["Tier 4"]
        n14["SAF_aircraft_modernization"]
        n60["SAF_elite_training"]
        n61["SAF_modernize_infantry_equipment"]
        n15["SAF_the_prides_of_the_nation"]
    end
    subgraph tier_5["Tier 5"]
        n62["SAF_military_innovations"]
    end
    n53 --> n54
    n52 --> n54
    n6 --> n9
    n6 --> n14
    n13 --> n14
    n1 --> n5
    n4 --> n5
    n51 --> n55
    n55 --> n60
    n56 --> n60
    n59 --> n60
    n5 --> n6
    n51 --> n56
    n53 --> n57
    n52 --> n57
    n53 --> n58
    n52 --> n58
    n58 --> n62
    n57 --> n62
    n54 --> n62
    n60 --> n62
    n4 --> n50
    n7 --> n10
    n59 --> n61
    n49 --> n61
    n6 --> n11
    n2 --> n12
    n3 --> n12
    n7 --> n12
    n5 --> n7
    n50 --> n51
    n50 --> n52
    n50 --> n53
    n51 --> n59
    n5 --> n8
    n8 --> n13
    n11 --> n15
    n9 --> n15
    n9 x--x n11
    n52 x--x n53
```

# SAF_railway_development

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n63(("SAF_railway_development"))
        n59["SAF_reform_staff_officers_training"]
    end
    subgraph tier_1["Tier 1"]
        n64["SAF_mining_development"]
    end
    subgraph tier_2["Tier 2"]
        n65["SAF_amcor_thabazimbi_iron_mine"]
        n66["SAF_develop_gold_extraction"]
    end
    subgraph tier_3["Tier 3"]
        n67["SAF_amcor_plate_mill"]
        n68["SAF_economic_expansion"]
        n69["SAF_transvaal_urbanization"]
    end
    subgraph tier_4["Tier 4"]
        n70["SAF_expand_iscor_pretoria_works"]
        n49["SAF_magazine_hill_ammunition_plant"]
    end
    subgraph tier_5["Tier 5"]
        n71["SAF_industrial_innovations"]
        n61["SAF_modernize_infantry_equipment"]
        n72["SAF_reorganize_the_artillery"]
    end
    subgraph tier_6["Tier 6"]
        n73["SAF_expand_around_magazine_hill"]
        n74["SAF_local_manufacturing_industry"]
        n75["SAF_sasol_synthetic_fuel_researches"]
    end
    subgraph tier_7["Tier 7"]
        n76["SAF_lenz_bomb_factory"]
    end
    subgraph tier_8["Tier 8"]
        n77["SAF_atomic_energy_board"]
        n78["SAF_war_technologies"]
    end
    subgraph tier_9["Tier 9"]
        n79["SAF_uranium_mining"]
    end
    n65 --> n67
    n64 --> n65
    n76 --> n77
    n74 --> n77
    n64 --> n66
    n66 --> n68
    n71 --> n73
    n69 --> n70
    n68 --> n70
    n70 --> n71
    n49 --> n71
    n73 --> n76
    n71 --> n74
    n68 --> n49
    n63 --> n64
    n59 --> n61
    n49 --> n61
    n49 --> n72
    n71 --> n75
    n66 --> n69
    n78 --> n79
    n77 --> n79
    n76 --> n78
    n74 --> n78
```

# SAF_sensibilize_the_africans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n23["SAF_ethnic_legislation"]
        n24(("SAF_sensibilize_the_africans"))
    end
    subgraph tier_1["Tier 1"]
        n80["SAF_organize_the_party"]
    end
    subgraph tier_2["Tier 2"]
        n81{"SAF_paralyze_the_country"}
        n82["SAF_rally_the_indians"]
    end
    subgraph tier_3["Tier 3"]
        n83["SAF_alliance_with_ussr"]
        n84["SAF_black_republic"]
        n85["SAF_liberation_revolution"]
    end
    subgraph tier_4["Tier 4"]
        n86["SAF_control_former_exploiters"]
        n87["SAF_redistribute_the_land"]
        n88["SAF_side_by_side_as_equals"]
    end
    subgraph tier_5["Tier 5"]
        n89["SAF_support_african_seperatists"]
    end
    n81 --> n83
    n81 --> n84
    n84 --> n86
    n81 --> n85
    n24 --> n80
    n80 --> n81
    n80 --> n82
    n85 --> n87
    n84 --> n87
    n85 --> n88
    n87 --> n89
    n88 --> n89
    n86 --> n89
    n84 x--x n85
    n23 x--x n24
```
