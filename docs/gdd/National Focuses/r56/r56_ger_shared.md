# GERK_legacy_of_the_zollverein

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("GERK_legacy_of_the_zollverein"))
        n2["GERK_move_towards_german_reunification"]
    end
    n1 x--x n2
```

# GERK_move_towards_german_reunification

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["GERK_legacy_of_the_zollverein"]
        n2(("GERK_move_towards_german_reunification"))
    end
    n1 x--x n2
```

# GERK_revitalize_old_traditions

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n3(("GERK_revitalize_old_traditions"))
    end
    subgraph tier_1["Tier 1"]
        n4["GERK_continue_motorization"]
        n5["GERK_rifle_modernization"]
        n6["GERK_root_militarism"]
    end
    subgraph tier_2["Tier 2"]
        n7["GERK_field_piece_research"]
        n8["GERK_gott_mit_uns"]
        n9["GERK_panzer_armies"]
    end
    subgraph tier_3["Tier 3"]
        n10["GERK_army_with_a_state"]
        n11["GERK_factory_of_europe"]
        n12["GERK_shocktroops"]
    end
    subgraph tier_4["Tier 4"]
        n13["GERK_all_terrain_military_motorcycle"]
        n14["GERK_train_panzergrenadiers"]
    end
    n12 --> n13
    n8 --> n10
    n3 --> n4
    n9 --> n11
    n8 --> n11
    n5 --> n7
    n6 --> n8
    n4 --> n9
    n3 --> n5
    n3 --> n6
    n7 --> n12
    n4 --> n12
    n12 --> n14
```
