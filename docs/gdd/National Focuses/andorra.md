# ADR_abandon_the_policy_of_neutrality

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"ADR_abandon_the_policy_of_neutrality"}
        n2["ADR_continue_the_policy_of_neutrality"]
    end
    subgraph tier_1["Tier 1"]
        n3["ADR_a_flexible_foreign_policy"]
        n4["ADR_accept_french_potectorate"]
    end
    n1 --> n3
    n1 --> n4
    n3 x--x n4
    n1 x--x n2
```

# ADR_continue_the_policy_of_neutrality

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ADR_abandon_the_policy_of_neutrality"]
        n2(("ADR_continue_the_policy_of_neutrality"))
    end
    subgraph tier_1["Tier 1"]
        n5["ADR_accept_spanish_refugees"]
    end
    subgraph tier_2["Tier 2"]
        n6["ADR_expand_the_tourist_industry"]
        n7["ADR_normalize_spanish_relations"]
    end
    subgraph tier_3["Tier 3"]
        n8["ADR_encourage_foreign_investment"]
    end
    n2 --> n5
    n6 --> n8
    n5 --> n6
    n5 --> n7
    n1 x--x n2
```
