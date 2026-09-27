# MAL_RND

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("MAL_RND"))
    end
    subgraph tier_1["Tier 1"]
        n2["MAL_RND_1"]
        n3["MAL_RND_2"]
        n4["MAL_RND_3"]
    end
    subgraph tier_2["Tier 2"]
        n5["MAL_RND_4"]
        n6["MAL_RND_5"]
        n7["MAL_RND_6"]
    end
    subgraph tier_3["Tier 3"]
        n8["MAL_RND_7"]
        n9["MAL_RND_8"]
        n10["MAL_RND_9"]
    end
    subgraph tier_4["Tier 4"]
        n11["MAL_RND_10"]
    end
    n1 --> n2
    n8 --> n11
    n9 --> n11
    n10 --> n11
    n1 --> n3
    n1 --> n4
    n2 --> n5
    n3 --> n6
    n4 --> n7
    n5 --> n8
    n6 --> n9
    n7 --> n10
```

# MAL_japanese_puppet

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12(("MAL_japanese_puppet"))
    end
    subgraph tier_1["Tier 1"]
        n13["MAL_japanese_puppet_1"]
    end
    n12 --> n13
```

# MAL_state_of_malaya

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14{"MAL_state_of_malaya"}
    end
    subgraph tier_1["Tier 1"]
        n15{"MAL_centralisation"}
        n16{"MAL_decentralisation"}
    end
    subgraph tier_2["Tier 2"]
        n17["MAL_centralisation_1"]
        n18["MAL_decentralisation_1"]
        n19["MAL_seek_investors"]
        n20["MAL_the_empire"]
        n21{"MAL_the_nation"}
        n22["MAL_the_princes"]
        n23["MAL_the_workers"]
    end
    subgraph tier_3["Tier 3"]
        n24["MAL_centralisation_2"]
        n25["MAL_decentralisation_2"]
        n26["MAL_deslashcentralisation"]
        n27["MAL_deslashcentralisation_1"]
        n28{"MAL_the_empire_1"}
        n29["MAL_the_nation_1"]
        n30["MAL_the_nation_2"]
        n31["MAL_the_princes_1"]
        n32["MAL_the_princes_2"]
        n33{"MAL_the_workers_1"}
    end
    subgraph tier_4["Tier 4"]
        n34["MAL_centralisation_3"]
        n35["MAL_decentralisation_3"]
        n36["MAL_the_empire_2"]
        n37["MAL_the_empire_3"]
        n38{"MAL_the_nation_3"}
        n39{"MAL_the_princes_3"}
        n40["MAL_the_workers_2"]
        n41["MAL_the_workers_3"]
    end
    subgraph tier_5["Tier 5"]
        n42["MAL_deslashcentralisation_2"]
        n43["MAL_the_empire_4"]
        n44["MAL_the_nation_4"]
        n45["MAL_the_nation_5"]
        n46["MAL_the_princes_4"]
        n47["MAL_the_princes_4_a"]
        n48["MAL_the_princes_5"]
        n49["MAL_the_workers_4"]
    end
    subgraph tier_6["Tier 6"]
        n50["MAL_the_empire_5"]
        n51["MAL_the_empire_6"]
        n52["MAL_the_empire_7"]
        n53["MAL_the_nation_6"]
        n54["MAL_the_princes_6"]
        n55{"MAL_the_workers_5"}
    end
    subgraph tier_7["Tier 7"]
        n56["MAL_expand_the_realm"]
        n57["MAL_the_nation_7"]
        n58["MAL_the_workers_6"]
        n59["MAL_the_workers_7"]
    end
    n14 --> n15
    n15 --> n17
    n17 --> n24
    n24 --> n34
    n14 --> n16
    n16 --> n18
    n18 --> n25
    n25 --> n35
    n18 --> n26
    n17 --> n26
    n18 --> n27
    n17 --> n27
    n35 --> n42
    n34 --> n42
    n26 --> n42
    n27 --> n42
    n54 --> n56
    n15 --> n19
    n16 --> n19
    n15 --> n20
    n20 --> n28
    n28 --> n36
    n28 --> n37
    n36 --> n43
    n37 --> n43
    n43 --> n50
    n43 --> n51
    n43 --> n52
    n15 --> n21
    n21 --> n29
    n21 --> n30
    n29 --> n38
    n30 --> n38
    n38 --> n44
    n38 --> n45
    n45 --> n53
    n44 --> n53
    n53 --> n57
    n16 --> n22
    n22 --> n31
    n22 --> n32
    n32 --> n39
    n31 --> n39
    n39 --> n46
    n39 --> n47
    n39 --> n48
    n48 --> n54
    n46 --> n54
    n16 --> n23
    n23 --> n33
    n33 --> n40
    n33 --> n41
    n41 --> n49
    n40 --> n49
    n49 --> n55
    n55 --> n58
    n55 --> n59
    n15 x--x n16
    n20 x--x n21
    n36 x--x n37
    n29 x--x n30
    n44 x--x n45
    n22 x--x n23
    n46 x--x n47
    n46 x--x n48
    n47 x--x n48
    n40 x--x n41
    n58 x--x n59
```

# MAL_the_air

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n60(("MAL_the_air"))
        n61["MAL_the_island"]
        n62["MAL_the_straits"]
    end
    subgraph tier_1["Tier 1"]
        n63["MAL_the_air_1"]
        n64["MAL_the_island_1"]
        n65["MAL_the_straits_1"]
    end
    subgraph tier_2["Tier 2"]
        n66["MAL_the_air_2"]
        n67["MAL_the_island_2"]
        n68["MAL_the_island_3"]
        n69["MAL_the_straits_2"]
    end
    subgraph tier_3["Tier 3"]
        n70["MAL_the_air_3"]
        n71["MAL_the_island_air_straits"]
        n72["MAL_the_straits_3"]
    end
    subgraph tier_4["Tier 4"]
        n73["MAL_the_island_air_straits_1"]
    end
    subgraph tier_5["Tier 5"]
        n74["MAL_the_island_air_straits_2"]
    end
    n60 --> n63
    n61 --> n63
    n62 --> n63
    n63 --> n66
    n66 --> n70
    n61 --> n64
    n60 --> n64
    n62 --> n64
    n64 --> n67
    n64 --> n68
    n68 --> n71
    n67 --> n71
    n66 --> n71
    n69 --> n71
    n71 --> n73
    n73 --> n74
    n61 --> n65
    n60 --> n65
    n62 --> n65
    n65 --> n69
    n69 --> n72
    n60 x--x n61
    n60 x--x n62
```

# MAL_the_island

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n60["MAL_the_air"]
        n61(("MAL_the_island"))
        n62["MAL_the_straits"]
    end
    subgraph tier_1["Tier 1"]
        n63["MAL_the_air_1"]
        n64["MAL_the_island_1"]
        n65["MAL_the_straits_1"]
    end
    subgraph tier_2["Tier 2"]
        n66["MAL_the_air_2"]
        n67["MAL_the_island_2"]
        n68["MAL_the_island_3"]
        n69["MAL_the_straits_2"]
    end
    subgraph tier_3["Tier 3"]
        n70["MAL_the_air_3"]
        n71["MAL_the_island_air_straits"]
        n72["MAL_the_straits_3"]
    end
    subgraph tier_4["Tier 4"]
        n73["MAL_the_island_air_straits_1"]
    end
    subgraph tier_5["Tier 5"]
        n74["MAL_the_island_air_straits_2"]
    end
    n60 --> n63
    n61 --> n63
    n62 --> n63
    n63 --> n66
    n66 --> n70
    n61 --> n64
    n60 --> n64
    n62 --> n64
    n64 --> n67
    n64 --> n68
    n68 --> n71
    n67 --> n71
    n66 --> n71
    n69 --> n71
    n71 --> n73
    n73 --> n74
    n61 --> n65
    n60 --> n65
    n62 --> n65
    n65 --> n69
    n69 --> n72
    n60 x--x n61
    n61 x--x n62
```

# MAL_the_straits

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n60["MAL_the_air"]
        n61["MAL_the_island"]
        n62(("MAL_the_straits"))
    end
    subgraph tier_1["Tier 1"]
        n63["MAL_the_air_1"]
        n64["MAL_the_island_1"]
        n65["MAL_the_straits_1"]
    end
    subgraph tier_2["Tier 2"]
        n66["MAL_the_air_2"]
        n67["MAL_the_island_2"]
        n68["MAL_the_island_3"]
        n69["MAL_the_straits_2"]
    end
    subgraph tier_3["Tier 3"]
        n70["MAL_the_air_3"]
        n71["MAL_the_island_air_straits"]
        n72["MAL_the_straits_3"]
    end
    subgraph tier_4["Tier 4"]
        n73["MAL_the_island_air_straits_1"]
    end
    subgraph tier_5["Tier 5"]
        n74["MAL_the_island_air_straits_2"]
    end
    n60 --> n63
    n61 --> n63
    n62 --> n63
    n63 --> n66
    n66 --> n70
    n61 --> n64
    n60 --> n64
    n62 --> n64
    n64 --> n67
    n64 --> n68
    n68 --> n71
    n67 --> n71
    n66 --> n71
    n69 --> n71
    n71 --> n73
    n73 --> n74
    n61 --> n65
    n60 --> n65
    n62 --> n65
    n65 --> n69
    n69 --> n72
    n60 x--x n62
    n61 x--x n62
```

# MAL_worldstage

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n75{"MAL_worldstage"}
    end
    subgraph tier_1["Tier 1"]
        n76["MAL_worldstage_1"]
        n77["MAL_worldstage_3"]
        n78["MAL_worldstage_5"]
        n79["MAL_worldstage_6"]
    end
    subgraph tier_2["Tier 2"]
        n80["MAL_worldstage_2"]
        n81["MAL_worldstage_4"]
        n82["MAL_worldstage_7"]
    end
    n75 --> n76
    n76 --> n80
    n75 --> n77
    n77 --> n81
    n78 --> n81
    n75 --> n78
    n75 --> n79
    n79 --> n82
    n77 x--x n78
```
