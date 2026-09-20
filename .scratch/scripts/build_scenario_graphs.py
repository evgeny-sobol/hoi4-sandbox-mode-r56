#!/usr/bin/env python3
"""Build Mermaid focus-path diagrams for every scenario arc.

Reads the pre-generated Mermaid focus graphs under gdd/National Focuses/
(one .md per country: `# <branch_root>` sections, each a `flowchart TD`
with `nN["ID"]` / `nN(("ID"))` / `nN{"ID"}` nodes and `nA --> nB`
(prerequisite) / `nA x--x nB` (mutually exclusive) edges).

For each scenario arc it emits a compact Mermaid subgraph: the arc's key
focuses (the ones the director boosts / logs) plus the prerequisite and
mutual-exclusion edges among them. Output is grouped per aggressor country
with one `subgraph` per arc, ready to paste into gdd/Scenarios.md.

Usage:
    python build_scenario_graphs.py
"""
from __future__ import annotations

import re
from pathlib import Path

GDD = Path(__file__).resolve().parents[2] / "gdd" / "National Focuses"

NODE_RE = re.compile(r'^\s*(n\d+)(?:\(\(|\[\{?|\{)(.*?)(?:\)\)|\]|\})\s*$')
EDGE_RE = re.compile(r"^\s*(n\d+)\s*(-->|x--x)\s*(n\d+)")


def load_graph(path: Path):
    """Return (prereq, excl) as {focus_id: {parent_id}} / {(a,b)} sets."""
    text = path.read_text(encoding="utf-8")
    id_by_node: dict[str, str] = {}
    for raw in text.splitlines():
        m = NODE_RE.match(raw)
        if m:
            id_by_node[m.group(1)] = m.group(2).strip().strip('"')
    prereq: dict[str, set[str]] = {}
    excl: set[tuple[str, str]] = set()
    for raw in text.splitlines():
        e = EDGE_RE.match(raw)
        if not e:
            continue
        a, kind, b = e.groups()
        fa, fb = id_by_node.get(a), id_by_node.get(b)
        if not fa or not fb:
            continue
        if kind == "-->":
            prereq.setdefault(fb, set()).add(fa)
        else:
            excl.add((fa, fb))
    return prereq, excl


def ancestors(fid, prereq, max_depth):
    """All prerequisite ancestors of fid, up to max_depth hops."""
    seen: set[str] = set()
    frontier = {fid}
    for _ in range(max_depth):
        nxt: set[str] = set()
        for f in frontier:
            for p in prereq.get(f, ()):
                if p not in seen and p != fid:
                    seen.add(p)
                    nxt.add(p)
        frontier = nxt
        if not frontier:
            break
    return seen


def render_arc(name, keys, prereq, excl, roots=(), depth=3):
    """Mermaid flowchart for one arc: key focuses plus their prerequisite
    paths (bounded depth). Keys are double-bordered, path roots are rounded,
    intermediate path focuses are plain."""
    keyset = set(keys)
    keep = set(keyset)
    for k in keys:
        keep |= ancestors(k, prereq, depth)

    kept_edges = [(p, b) for b in keep for p in prereq.get(b, ()) if p in keep]
    has_parent = {b for _, b in kept_edges}
    rootset = set(roots) | {f for f in keep if f not in has_parent}

    out = ["```mermaid", "flowchart TD", f"    subgraph {name}"]
    for fid in sorted(keep):
        if fid in rootset:
            out.append(f'        {fid}(["{fid}"])')
        elif fid in keyset:
            out.append(f'        {fid}[["{fid}"]]')
        else:
            out.append(f'        {fid}["{fid}"]')
    for p, b in sorted(set(kept_edges)):
        out.append(f"        {p} --> {b}")
    for a, b in sorted(excl):
        if a in keep and b in keep:
            out.append(f"        {a} x--x {b}")
    out.append("    end")
    out.append("```")
    return "\n".join(out)


# arc id -> (title, aggressor file, key focuses, root focuses among keys)
ARCS = [
    (1, "Axis expansion", "germany",
     ["GER_danzig_or_war", "GER_demand_sudetenland", "GER_war_with_france", "GER_around_maginot"], ()),
    (9, "German Atlantic", "germany",
     ["GER_crossing_the_atlantic", "GER_atlantic_naval_bases"], ()),
    (10, "German Middle East", "germany",
     ["GER_influence_the_middle_east", "GER_claim_old_colonies_in_the_east",
      "GER_wage_war_on_capitalism"], ()),
    (23, "Communist Germany", "germany",
     ["GER_root_out_imperialism", "GER_hegemony_over_europe",
      "GER_wage_war_on_capitalism", "GER_strike_at_the_rising_sun"], ()),
    (24, "Monarchist Germany", "germany",
     ["GER_soviet_invasion", "GER_restore_klein_venedig"], ()),

    (2, "Soviet expansion", "soviet",
     ["SOV_beaten_but_not_defeated", "SOV_imperial_legacy", "SOV_reclaim_polish_overlordship",
      "SOV_westward_bound", "SOV_secure_finland"], ()),
    (11, "Soviet South", "soviet",
     ["SOV_the_last_break_southward", "SOV_preemptive_invasion_of_iran", "SOV_into_the_plateau"], ()),
    (12, "Soviet East", "soviet",
     ["SOV_crush_our_eastern_rival", "SOV_our_american_holding",
      "SOV_restore_the_old_eastern_empire"], ()),
    (25, "White Russia", "soviet",
     ["SOV_beaten_but_not_defeated", "SOV_white_exiles", "SOV_imperial_legacy",
      "SOV_strike_the_eagle"], ()),

    (3, "Japanese expansion", "japan",
     ["JAP_reinforce_the_beijing_garrison", "JAP_strike_the_southern_road"], ()),
    (13, "Japanese North", "japan",
     ["JAP_hokushin_ron", "JAP_sea_establish_the_northern_resource_area",
      "JAP_strike_the_soviets"], ()),
    (14, "Japanese Old Oppressors", "japan",
     ["JAP_strike_the_old_oppressors", "JAP_ultimate_deterrence"], ()),
    (26, "Communist Japan", "japan",
     ["JAP_put_an_end_to_chinese_feudalism", "JAP_spread_the_revolutuon_south",
      "JAP_free_asians_from_soviet_opression", "JAP_go_after_the_capitalists"], ()),

    (4, "Italian expansion", "italy",
     ["ITA_italys_destiny", "ITA_war_with_greece"], ()),
    (15, "Italian West", "italy",
     ["ITA_war_with_france", "ITA_war_with_the_uk", "ITA_demand_ticino"], ()),
    (16, "Italian Mediterranean", "italy",
     ["ITA_a_time_for_war", "ITA_claims_on_turkey_bba", "ITA_all_roads_lead_to_rome"], ()),
    (27, "Communist Italy", "italy",
     ["ITA_pugno_alzato", "ITA_the_enemies_of_capitalism",
      "ITA_liberate_the_workers_of_africa"], ()),

    (5, "Fascist Britain", "uk",
     ["ENG_a_change_in_course", "ENG_organize_the_blackshirts", "ENG_war_france",
      "ENG_war_with_ussr"], ()),
    (17, "British Imperial Restoration", "uk",
     ["ENG_reclaim_the_jewel_in_the_crown", "ENG_bring_the_dominions_back_into_the_fold",
      "ENG_unite_the_anglosphere"], ()),
    (28, "Communist Britain", "uk",
     ["ENG_soviet_cooperation", "ENG_the_one_true_revolution",
      "ENG_liberate_the_home_of_marx", "ENG_liberate_the_american_workers"], ()),

    (6, "Red America", "usa",
     ["USA_continue_the_new_deal", "USA_suspend_the_presecution", "USA_end_monarchism",
      "USA_shatter_the_empires", "USA_us_ussr_economic_cooperation"], ()),
    (18, "American War Plan", "usa",
     ["USA_war_plan_orange", "USA_war_plan_black", "USA_defense_of_the_pacific",
      "USA_intervention_in_europe"], ()),
    (19, "American Global Hegemony", "usa",
     ["USA_end_monarchism", "USA_shatter_the_empires", "USA_global_hegemony"], ()),

    (7, "Napoleonic France", "france",
     ["FRA_action_francaise", "FRA_papal_rehabilitation", "FRA_repeal_the_law_of_exile",
      "FRA_brumaire_movement", "FRA_the_new_continental_system", "FRA_crush_germany",
      "FRA_nothern_italy_claim"], ("FRA_action_francaise",)),
    (20, "French Monarchist Revival", "france",
     ["FRA_secure_the_crown_of_spain", "FRA_claim_the_andorran_throne",
      "FRA_restore_the_mexican_monarchy", "FRA_second_march_on_moscow"], ()),
    (21, "French Revenge", "france",
     ["FRA_dismantle_germany", "FRA_crush_germany", "FRA_destroy_albion",
      "FRA_strike_empire"], ()),
    (22, "French Plan XIV", "france",
     ["FRA_plan_xiv", "FRA_return_to_dalmatia", "FRA_nothern_italy_claim"], ()),

    (8, "Habsburg restoration", "hungary",
     ["HUN_proclaim_the_restoration_of_austria_hungary", "HUN_claim_transylvania",
      "HUN_march_to_the_shore", "HUN_claim_galicia"], ()),
]


def main():
    graphs: dict[str, tuple] = {}
    for _, _, country, _, _ in ARCS:
        if country not in graphs:
            path = GDD / f"{country}.md"
            if not path.is_file():
                raise SystemExit(f"missing focus graph: {path}")
            graphs[country] = load_graph(path)

    by_country: dict[str, list] = {}
    for arc, title, country, keys, roots in ARCS:
        by_country.setdefault(country, []).append((arc, title, keys, roots))

    for country, arcs in by_country.items():
        prereq, excl = graphs[country]
        print(f"\n<!-- {country} -->")
        for arc, title, keys, roots in arcs:
            print(f"\n#### Arc {arc}: {title}\n")
            print(render_arc(f"arc{arc}", keys, prereq, excl, roots))


if __name__ == "__main__":
    main()
