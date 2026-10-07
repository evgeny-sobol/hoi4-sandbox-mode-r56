# ITA_army_primacy_bba

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"ITA_army_primacy_bba"}
        n2["ITA_fiocchi_munizioni"]
        n3["ITA_milan_comms_industry"]
    end
    subgraph tier_1["Tier 1"]
        n4["ITA_a_bandits_war"]
        n5["ITA_follow_pariani_plan"]
        n6["ITA_increase_artillery_production"]
        n7["ITA_preserve_army_traditions"]
    end
    subgraph tier_2["Tier 2"]
        n8["ITA_army_leaders"]
        n9["ITA_carica_di_isbuscenskij"]
        n10["ITA_focus_on_mobilization"]
        n11["ITA_italian_tankettes"]
        n12["ITA_moschettieri_del_duce"]
        n13["ITA_superesercito"]
        n14["ITA_vallo_alpino_del_littorio"]
    end
    subgraph tier_3["Tier 3"]
        n15["ITA_bersaglieri"]
        n16["ITA_high_command_loyalty"]
        n17{"ITA_self_propelled_guns"}
    end
    subgraph tier_4["Tier 4"]
        n18["ITA_divisioni_alpine"]
        n19["ITA_end_fiat_ansaldo_duopoly"]
        n20["ITA_fanti_dell_aria"]
        n21["ITA_modernize_ansaldo_facilities"]
        n22["ITA_the_new_arditi"]
    end
    subgraph tier_5["Tier 5"]
        n23["ITA_ferrea_mole_ferreo_cuore"]
        n24["ITA_winter_training_in_finland"]
    end
    n1 --> n4
    n7 --> n8
    n4 --> n8
    n5 --> n8
    n8 --> n15
    n13 --> n15
    n4 --> n9
    n15 --> n18
    n17 --> n19
    n15 --> n20
    n19 --> n23
    n21 --> n23
    n7 --> n10
    n4 --> n10
    n5 --> n10
    n1 --> n5
    n13 --> n16
    n11 --> n16
    n2 --> n6
    n1 --> n6
    n7 --> n11
    n4 --> n11
    n5 --> n11
    n17 --> n21
    n7 --> n12
    n1 --> n7
    n13 --> n17
    n11 --> n17
    n7 --> n13
    n4 --> n13
    n5 --> n13
    n15 --> n22
    n3 --> n14
    n6 --> n14
    n18 --> n24
    n12 --> n24
    n4 x--x n5
    n4 x--x n7
    n19 x--x n21
    n5 x--x n7
```

# ITA_ethiopian_war_logistics_bba

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25(("ITA_ethiopian_war_logistics_bba"))
        n26["ITA_italian_highways_bba"]
    end
    subgraph tier_1["Tier 1"]
        n27["ITA_ministry_of_italian_africa"]
    end
    subgraph tier_2["Tier 2"]
        n28["ITA_develop_eritrea"]
        n29["ITA_develop_ethiopia"]
        n30["ITA_develop_libya"]
        n31["ITA_develop_somaliland"]
    end
    subgraph tier_3["Tier 3"]
        n32["ITA_colonial_rifles_production"]
        n33["ITA_eritrean_coast_oil_extraction"]
        n34["ITA_establish_the_sme"]
        n35["ITA_expand_libyan_oil_production"]
        n36["ITA_finish_the_litoranea_libica"]
        n37["ITA_modernize_ethiopian_roads"]
        n38{"ITA_regional_development"}
        n39["ITA_tripoli_explosives_factory"]
    end
    subgraph tier_4["Tier 4"]
        n40["ITA_cementerie_d_etiopia"]
        n41["ITA_expand_libyan_manufactures"]
        n42["ITA_imperial_line"]
        n43["ITA_libyan_railway"]
        n44["ITA_libyan_refineries"]
        n45["ITA_polizia_dell_africa_italiana"]
        n46["ITA_strengthen_ascari_corps"]
        n47["ITA_via_della_vittoria"]
    end
    subgraph tier_5["Tier 5"]
        n48["ITA_comandante_diavolo"]
        n49["ITA_compagnia_etiopica_degli_esplosivi"]
        n50["ITA_expand_addis_ababa"]
    end
    n37 --> n40
    n30 --> n32
    n31 --> n32
    n29 --> n32
    n45 --> n48
    n46 --> n48
    n40 --> n49
    n27 --> n28
    n27 --> n29
    n27 --> n30
    n27 --> n31
    n28 --> n33
    n28 --> n34
    n42 --> n50
    n40 --> n50
    n36 --> n41
    n30 --> n35
    n30 --> n36
    n37 --> n42
    n36 --> n43
    n35 --> n43
    n35 --> n44
    n26 --> n27
    n25 --> n27
    n29 --> n37
    n28 --> n37
    n38 --> n45
    n28 --> n38
    n30 --> n38
    n31 --> n38
    n29 --> n38
    n38 --> n46
    n30 --> n39
    n36 --> n47
    n45 x--x n46
```

# ITA_italian_highways_bba

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ITA_army_primacy_bba"]
        n25["ITA_ethiopian_war_logistics_bba"]
        n26{"ITA_italian_highways_bba"}
    end
    subgraph tier_1["Tier 1"]
        n2["ITA_fiocchi_munizioni"]
        n27["ITA_ministry_of_italian_africa"]
        n51["ITA_power_plants_in_terni"]
        n52["ITA_railway_innovations"]
        n53["ITA_steel_industry_in_terni"]
    end
    subgraph tier_2["Tier 2"]
        n54["ITA_brescia_small_arms_industry"]
        n28["ITA_develop_eritrea"]
        n29["ITA_develop_ethiopia"]
        n30["ITA_develop_libya"]
        n31["ITA_develop_somaliland"]
        n55["ITA_expand_foggia_farm_fields"]
        n56{"ITA_finance_anic"}
        n6["ITA_increase_artillery_production"]
        n57["ITA_investments_in_edison"]
        n3["ITA_milan_comms_industry"]
    end
    subgraph tier_3["Tier 3"]
        n32["ITA_colonial_rifles_production"]
        n33["ITA_eritrean_coast_oil_extraction"]
        n34["ITA_establish_the_sme"]
        n35["ITA_expand_libyan_oil_production"]
        n58{"ITA_expand_national_universities"}
        n36["ITA_finish_the_litoranea_libica"]
        n37["ITA_modernize_ethiopian_roads"]
        n59["ITA_modernize_the_mezzogiorno"]
        n60{"ITA_redirect_alfa_romeo_production"}
        n38{"ITA_regional_development"}
        n61["ITA_strengthen_northern_industry"]
        n39["ITA_tripoli_explosives_factory"]
        n14["ITA_vallo_alpino_del_littorio"]
    end
    subgraph tier_4["Tier 4"]
        n40["ITA_cementerie_d_etiopia"]
        n41["ITA_expand_libyan_manufactures"]
        n42["ITA_imperial_line"]
        n62["ITA_incease_fiat_presence_in_the_south"]
        n63["ITA_increase_production"]
        n64["ITA_keep_specialization"]
        n43["ITA_libyan_railway"]
        n44["ITA_libyan_refineries"]
        n65["ITA_new_industrialization_program"]
        n66["ITA_po_valley_mettalurgy"]
        n45["ITA_polizia_dell_africa_italiana"]
        n46["ITA_strengthen_ascari_corps"]
        n47["ITA_via_della_vittoria"]
    end
    subgraph tier_5["Tier 5"]
        n48["ITA_comandante_diavolo"]
        n49["ITA_compagnia_etiopica_degli_esplosivi"]
        n67["ITA_crocco_mission"]
        n50["ITA_expand_addis_ababa"]
    end
    n2 --> n54
    n37 --> n40
    n30 --> n32
    n31 --> n32
    n29 --> n32
    n45 --> n48
    n46 --> n48
    n40 --> n49
    n63 --> n67
    n64 --> n67
    n27 --> n28
    n27 --> n29
    n27 --> n30
    n27 --> n31
    n28 --> n33
    n28 --> n34
    n42 --> n50
    n40 --> n50
    n52 --> n55
    n36 --> n41
    n30 --> n35
    n57 --> n58
    n53 --> n56
    n51 --> n56
    n30 --> n36
    n26 --> n2
    n37 --> n42
    n59 --> n62
    n2 --> n6
    n1 --> n6
    n58 --> n63
    n60 --> n63
    n52 --> n57
    n58 --> n64
    n60 --> n64
    n36 --> n43
    n35 --> n43
    n35 --> n44
    n2 --> n3
    n26 --> n27
    n25 --> n27
    n29 --> n37
    n28 --> n37
    n56 --> n59
    n61 --> n65
    n59 --> n65
    n58 --> n65
    n61 --> n66
    n38 --> n45
    n26 --> n51
    n26 --> n52
    n54 --> n60
    n3 --> n60
    n28 --> n38
    n30 --> n38
    n31 --> n38
    n29 --> n38
    n26 --> n53
    n38 --> n46
    n56 --> n61
    n30 --> n39
    n3 --> n14
    n6 --> n14
    n36 --> n47
    n63 x--x n64
    n59 x--x n61
    n45 x--x n46
    n51 x--x n53
```

# ITA_naval_power_projection

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n68["ITA_expand_rome_flying_school"]
        n69(("ITA_naval_power_projection"))
        n70["ITA_supremacy_in_the_skies"]
    end
    subgraph tier_1["Tier 1"]
        n71["ITA_expand_naval_facilities"]
        n72["ITA_intensify_torpedo_manufacturing"]
        n73["ITA_oto_naval_guns"]
    end
    subgraph tier_2["Tier 2"]
        n74["ITA_forza_navale_especiale"]
        n75["ITA_improve_overseas_naval_bases"]
        n76["ITA_milizia_marittima_di_artiglieria"]
        n77["ITA_stockpile_fuel"]
        n78{"ITA_supermarina"}
    end
    subgraph tier_3["Tier 3"]
        n79{"ITA_appoint_campioni"}
        n80{"ITA_cavagnari_plan"}
        n81["ITA_cooperation_programs"]
        n82["ITA_decima_flottiglia_mas"]
        n83["ITA_expand_naval_intelligence"]
        n84["ITA_naval_air_coordination"]
    end
    subgraph tier_4["Tier 4"]
        n85["ITA_cacciatorpediniere_di_scorta"]
        n86["ITA_cruiser_submarines"]
        n87["ITA_ispettorato_dei_mezzi_antisommergibili"]
        n88["ITA_midget_submarines"]
        n89["ITA_naval_guerilla"]
        n90["ITA_navi_da_battaglia"]
        n91["ITA_proper_carriers"]
        n92["ITA_refit_civilian_ships"]
        n93["ITA_shift_toward_an_offensive_force"]
    end
    subgraph tier_5["Tier 5"]
        n94["ITA_flotta_d_evasione"]
    end
    subgraph tier_6["Tier 6"]
        n95["ITA_satisfy_the_branches_needs"]
    end
    n78 --> n79
    n80 --> n85
    n78 --> n80
    n78 --> n81
    n80 --> n86
    n78 --> n82
    n69 --> n71
    n78 --> n83
    n87 --> n94
    n85 --> n94
    n90 --> n94
    n71 --> n74
    n71 --> n75
    n69 --> n72
    n80 --> n87
    n79 --> n87
    n80 --> n88
    n71 --> n76
    n78 --> n84
    n68 --> n84
    n80 --> n89
    n79 --> n90
    n69 --> n73
    n79 --> n91
    n79 --> n92
    n94 --> n95
    n70 --> n95
    n79 --> n93
    n71 --> n77
    n71 --> n78
    n79 x--x n80
    n86 x--x n88
    n91 x--x n92
```

# ITA_regia_aeronautica_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n94["ITA_flotta_d_evasione"]
        n96(("ITA_regia_aeronautica_focus"))
        n78["ITA_supermarina"]
    end
    subgraph tier_1["Tier 1"]
        n97["ITA_citta_dell_aria"]
        n68["ITA_expand_rome_flying_school"]
    end
    subgraph tier_2["Tier 2"]
        n98["ITA_diving_bombers"]
        n84["ITA_naval_air_coordination"]
        n99["ITA_reggianes_exports"]
        n100{"ITA_superaereo"}
    end
    subgraph tier_3["Tier 3"]
        n101["ITA_officers_of_the_service_role"]
        n102["ITA_specialization"]
        n103["ITA_standardization"]
    end
    subgraph tier_4["Tier 4"]
        n104["ITA_ba_65"]
        n105["ITA_cant_z_1011"]
        n106["ITA_g_50"]
        n107["ITA_sm_79"]
    end
    subgraph tier_5["Tier 5"]
        n70["ITA_supremacy_in_the_skies"]
    end
    subgraph tier_6["Tier 6"]
        n95["ITA_satisfy_the_branches_needs"]
    end
    n102 --> n104
    n103 --> n105
    n96 --> n97
    n97 --> n98
    n68 --> n98
    n96 --> n68
    n103 --> n106
    n102 --> n106
    n78 --> n84
    n68 --> n84
    n100 --> n101
    n68 --> n101
    n97 --> n99
    n94 --> n95
    n70 --> n95
    n103 --> n107
    n102 --> n107
    n100 --> n102
    n100 --> n103
    n97 --> n100
    n104 --> n70
    n105 --> n70
    n106 --> n70
    n107 --> n70
    n102 x--x n103
```

# ITA_solid_progress

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n108{"ITA_conspiracies_in_the_shadows"}
        n109{"ITA_organize_strikes_in_the_north"}
        n110(("ITA_solid_progress"))
        n111["ITA_struggle_in_ethiopia"]
        n112["ITA_the_abyssinian_fiasco"]
        n113{"ITA_the_southern_farmlands"}
        n114["ITA_unite_the_opposition"]
    end
    subgraph tier_1["Tier 1"]
        n115["ITA_servizio_informazione_militare"]
    end
    subgraph tier_2["Tier 2"]
        n116{"ITA_triumph_in_africa_bba"}
    end
    subgraph tier_3["Tier 3"]
        n117["ITA_anglo_italian_agreements"]
        n118["ITA_convene_the_grand_council"]
        n119{"ITA_culto_del_duce"}
        n120["ITA_defy_the_duce"]
        n121["ITA_devaluate_the_lire"]
        n122{"ITA_foreign_affairs"}
        n123["ITA_liberate_gramsci"]
        n124{"ITA_royal_intervention"}
        n125["ITA_the_new_emperor_of_ethiopia"]
        n126["ITA_topple_amhara_rulers"]
    end
    subgraph tier_4["Tier 4"]
        n127{"ITA_ally_yugoslavia"}
        n128["ITA_appeal_to_the_bourgeoisie"]
        n129{"ITA_balkan_ambition"}
        n130{"ITA_corpo_di_truppe_volontarie"}
        n131{"ITA_depose_mussolini"}
        n132{"ITA_empower_the_monarchists"}
        n133["ITA_la_battaglia_del_grano"]
        n134["ITA_la_battaglia_per_la_terra"]
        n135["ITA_ministero_della_cultura_popolare"]
        n136{"ITA_security_militias"}
        n137["ITA_seize_old_equipment"]
        n138["ITA_strengthen_the_coalition"]
        n139{"ITA_the_ethiopian_question"}
        n140{"ITA_the_italian_republic"}
        n141{"ITA_the_man_of_providence"}
    end
    subgraph tier_5["Tier 5"]
        n142["ITA_abolish_the_colonies"]
        n143["ITA_albanian_occupation"]
        n144["ITA_battaglioni_d_assalto"]
        n145["ITA_believe_obey_fight"]
        n146["ITA_boost_the_grand_council_of_fascism"]
        n147["ITA_demand_balearic_islands_bba"]
        n148{"ITA_dino_grandi_focus"}
        n149["ITA_expand_ond_membership"]
        n150["ITA_formalize_the_albanian_protectorate"]
        n151["ITA_guarantee_austrian_independence"]
        n152{"ITA_italian_socialism"}
        n153{"ITA_italo_balbo_focus"}
        n154["ITA_la_battaglia_per_le_nascite"]
        n155["ITA_legge_bottai"]
        n156{"ITA_militarize_the_rome_protocols"}
        n157["ITA_mobilize_womens"]
        n158{"ITA_monarchia_d_italia"}
        n159["ITA_move_toward_autarky"]
        n160["ITA_new_colonial_policies"]
        n161{"ITA_pact_of_steel"}
        n162["ITA_potential_allies_in_the_balkans"]
        n163["ITA_rebuild_the_north"]
        n164["ITA_referendum_on_the_monarchy"]
        n165["ITA_restore_the_statuto_albertino"]
        n166["ITA_revive_the_opera_nazionale_balilla"]
        n167["ITA_secure_control_over_parliament"]
        n168["ITA_strengthen_the_blackshirts"]
        n169["ITA_study_the_spanish_civil_war"]
        n170{"ITA_the_popular_front"}
        n171["ITA_to_live_as_a_lion"]
    end
    subgraph tier_6["Tier 6"]
        n172["ITA_a_leader_steps_forward"]
        n173["ITA_aid_for_the_spanish_republic"]
        n174["ITA_albanian_oil"]
        n175["ITA_banda_carita"]
        n176{"ITA_befriend_greece"}
        n177["ITA_befriend_japan"]
        n178["ITA_christian_democracy_r56"]
        n179{"ITA_common_ground"}
        n180["ITA_consolidate_power"]
        n181["ITA_cooperate_with_the_mafia"]
        n182["ITA_cooperatives_for_intensive_exploitation"]
        n183{"ITA_crush_the_mafia"}
        n184["ITA_disband_the_partisans"]
        n185["ITA_empower_the_unions"]
        n186["ITA_extraction_industry"]
        n187["ITA_german_military_assistance"]
        n188["ITA_giannini_sarnow_protocols"]
        n189{"ITA_industrial_socialization"}
        n190["ITA_invite_croatia"]
        n191["ITA_invite_france_to_military_partnership"]
        n192{"ITA_italian_irredentism"}
        n193["ITA_milizia_coloniale"]
        n194["ITA_negotiate_italian_claims"]
        n195["ITA_negotiations_with_albania"]
        n196["ITA_operazione_trajan"]
        n197{"ITA_power_to_the_king"}
        n198["ITA_reopen_the_markets"]
        n199{"ITA_revoke_the_acerbo_law"}
        n200["ITA_royal_militarism"]
        n201["ITA_seek_british_military_cooperation"]
        n202["ITA_spanish_italian_alliance"]
        n203{"ITA_stop_the_squandering"}
        n204{"ITA_strengthen_the_regime"}
        n205["ITA_support_albanian_irredentism"]
        n206["ITA_the_garibaldi_legion"]
        n207["ITA_the_italian_confederation"]
        n208["ITA_the_republics_leadership"]
    end
    subgraph tier_7["Tier 7"]
        n209["ITA_a_new_era_for_the_red_shirts"]
        n210["ITA_albanian_fascist_militia"]
        n211["ITA_anglo_italian_pact"]
        n212["ITA_appease_the_military"]
        n213["ITA_banda_koch"]
        n214["ITA_befriend_portugal"]
        n215["ITA_bring_back_exiled_intellectuals"]
        n216["ITA_christian_democracy"]
        n217["ITA_condemn_colonialism"]
        n218["ITA_control_the_industrial_elites"]
        n219["ITA_democratic_king"]
        n220{"ITA_devotion"}
        n221["ITA_disband_the_blackshirts"]
        n222["ITA_empower_the_carabinieri"]
        n223["ITA_enlist_the_bashkimi_kombetar"]
        n224["ITA_expand_the_romanian_oil_fields"]
        n225["ITA_franco_italian_pact"]
        n226["ITA_gruppi_di_difesa_della_donna"]
        n227["ITA_institute_the_five_year_plan"]
        n228["ITA_invite_andorra"]
        n229["ITA_liberalize_our_industries"]
        n230["ITA_mafia_abroad"]
        n231["ITA_new_corporations"]
        n232["ITA_operazione_tiberio"]
        n233["ITA_planned_economy"]
        n234["ITA_political_commissars"]
        n235["ITA_prepare_for_the_coming_wars"]
        n236["ITA_production_lines"]
        n237["ITA_purge_the_party"]
        n238["ITA_ratify_the_stresa_front"]
        n239["ITA_reinforce_regia_aeronautica"]
        n240["ITA_reorganize_regio_esercito"]
        n241["ITA_reorganize_the_party"]
        n242["ITA_request_control_of_french_territories"]
        n243["ITA_scientific_cooperation_r56"]
        n244["ITA_sea_wolves_bba"]
        n245["ITA_seek_papal_support"]
        n246["ITA_the_fight_overseas"]
        n247{"ITA_the_fourth_shore"}
        n248["ITA_the_path_to_progress"]
        n249["ITA_the_spanish_question"]
        n250["ITA_utilize_the_blackshirts"]
        n251["ITA_war_with_france"]
        n252{"ITA_war_with_greece"}
        n253["ITA_war_with_the_uk"]
    end
    subgraph tier_8["Tier 8"]
        n254["ITA_agents_of_the_church"]
        n255["ITA_army_modernization"]
        n256["ITA_ascari"]
        n257["ITA_befriend_turkey"]
        n258["ITA_bring_back_old_glories"]
        n259["ITA_claims_on_turkey_bba"]
        n260["ITA_compagnie_auto_avio_sahariane"]
        n261["ITA_cooperate_with_moderates"]
        n262["ITA_demand_dalmatia"]
        n263["ITA_demand_ticino"]
        n264["ITA_economic_reforms"]
        n265["ITA_expand_intelligence_services"]
        n266["ITA_expand_the_royal_guard"]
        n267["ITA_irregulars"]
        n268["ITA_joint_military_programs"]
        n269["ITA_liberate_the_workers_of_africa"]
        n270["ITA_meritocracy"]
        n271["ITA_mobilize_the_railway_guns"]
        n272["ITA_new_forms_of_weaponry"]
        n273["ITA_new_ricostruzione_industriale"]
        n274["ITA_oil_in_tripoli"]
        n275["ITA_proclaim_the_italian_empire"]
        n276["ITA_pugno_alzato"]
        n277["ITA_resume_food_importation"]
        n278{"ITA_social_stability"}
        n279["ITA_steel_in_tripoli"]
        n280{"ITA_the_fate_of_mussolini"}
        n281["ITA_the_italian_tiger"]
        n282{"ITA_union_in_the_party"}
    end
    subgraph tier_9["Tier 9"]
        n283["ITA_a_greater_purpose"]
        n284["ITA_combined_land_and_air_warfare"]
        n285{"ITA_crush_opposition"}
        n286["ITA_decrease_tariffs"]
        n287["ITA_defend_the_land"]
        n288["ITA_divino_duce"]
        n289["ITA_follow_the_soviet_union"]
        n290{"ITA_gloria_al_regno_d_italia"}
        n291["ITA_improve_the_industries"]
        n292["ITA_italia_libera"]
        n293["ITA_italys_destiny"]
        n294["ITA_novus_ordo"]
        n295["ITA_operazione_costantino"]
        n296["ITA_operazione_druso"]
        n297["ITA_paramilitary_training"]
        n298["ITA_reestablish_old_alliances"]
        n299{"ITA_strengthen_the_papacy"}
    end
    subgraph tier_10["Tier 10"]
        n300{"ITA_blackshirt_loyalty"}
        n301["ITA_european_democracies"]
        n302["ITA_expanded_corporatism"]
        n303["ITA_military_agreements"]
        n304["ITA_military_cooperation"]
        n305["ITA_prevent_the_spread_of_communism"]
        n306["ITA_preventive_intervention"]
        n307["ITA_raise_the_peoples"]
        n308["ITA_request_soviet_aid_alternative"]
        n309["ITA_sanction_mafia_killings"]
        n310["ITA_scientific_cooperation"]
        n311{"ITA_setting_course"}
        n312["ITA_special_brigades"]
        n313["ITA_spreading_the_eagles_wings"]
        n314["ITA_the_fight_against_stalinism"]
        n315["ITA_the_papacy_reborn"]
        n316["ITA_united_anarchist_confederations"]
    end
    subgraph tier_11["Tier 11"]
        n317["ITA_bring_down_fascist_strongholds"]
        n318["ITA_catholic_action"]
        n319["ITA_combined_research_effort"]
        n320["ITA_defense_against_capitalism"]
        n321["ITA_deus_vult"]
        n322["ITA_italian_hegemony"]
        n323["ITA_mare_nostrum_bba"]
        n324["ITA_peace_preservation"]
        n325["ITA_request_civil_war_support"]
        n326["ITA_secure_the_borders"]
        n327["ITA_the_enemies_of_capitalism"]
        n328{"ITA_towards_a_greater_italy"}
    end
    subgraph tier_12["Tier 12"]
        n329["ITA_a_time_for_war"]
        n330["ITA_auxiliaries"]
        n331["ITA_bend_the_bars"]
        n332["ITA_capo_supremo"]
        n333["ITA_heroes_of_the_nation"]
        n334["ITA_iberian_protection"]
        n335["ITA_il_sol_dell_avvenire"]
        n336["ITA_il_vento_aureo"]
        n337["ITA_new_roman_citizens"]
        n338["ITA_the_holy_lands"]
        n339["ITA_the_italian_legions"]
    end
    subgraph tier_13["Tier 13"]
        n340["ITA_all_roads_lead_to_rome"]
        n341["ITA_masters_of_the_aegean"]
        n342["ITA_south_american_alliances"]
        n343["ITA_subdue_the_sentinels"]
        n344["ITA_the_catholic_dominion"]
    end
    subgraph tier_14["Tier 14"]
        n345["ITA_a_colonial_empire"]
        n346["ITA_caligulas_pride"]
        n347["ITA_masters_of_the_mediterranean"]
        n348["ITA_modern_musculus"]
        n349["ITA_the_king_of_the_skies"]
    end
    subgraph tier_15["Tier 15"]
        n350["ITA_by_blood_alone"]
    end
    n343 --> n345
    n280 --> n283
    n170 --> n172
    n206 --> n209
    n321 --> n329
    n139 --> n142
    n245 --> n254
    n152 --> n173
    n205 --> n210
    n127 --> n143
    n129 --> n143
    n143 --> n174
    n150 --> n174
    n339 --> n340
    n122 --> n127
    n116 --> n117
    n201 --> n211
    n120 --> n128
    n179 --> n212
    n212 --> n255
    n234 --> n255
    n222 --> n255
    n246 --> n256
    n323 --> n330
    n122 --> n129
    n145 --> n175
    n175 --> n213
    n136 --> n144
    n156 --> n176
    n161 --> n177
    n156 --> n177
    n202 --> n214
    n147 --> n214
    n252 --> n257
    n176 --> n257
    n135 --> n145
    n328 --> n331
    n288 --> n300
    n141 --> n146
    n208 --> n215
    n235 --> n258
    n310 --> n317
    n345 --> n350
    n340 --> n346
    n328 --> n332
    n220 --> n332
    n315 --> n318
    n199 --> n216
    n164 --> n178
    n252 --> n259
    n176 --> n259
    n260 --> n284
    n304 --> n319
    n170 --> n179
    n152 --> n179
    n240 --> n260
    n239 --> n260
    n182 --> n217
    n153 --> n180
    n148 --> n180
    n200 --> n218
    n116 --> n118
    n108 --> n118
    n216 --> n261
    n219 --> n261
    n152 --> n181
    n142 --> n182
    n122 --> n130
    n261 --> n285
    n265 --> n285
    n170 --> n183
    n152 --> n183
    n116 --> n119
    n277 --> n286
    n282 --> n287
    n304 --> n320
    n109 --> n120
    n113 --> n120
    n116 --> n120
    n130 --> n147
    n238 --> n262
    n251 --> n263
    n242 --> n263
    n199 --> n219
    n118 --> n131
    n315 --> n321
    n116 --> n121
    n171 --> n220
    n146 --> n220
    n204 --> n220
    n131 --> n148
    n197 --> n221
    n199 --> n221
    n164 --> n184
    n280 --> n288
    n241 --> n264
    n183 --> n222
    n124 --> n132
    n152 --> n185
    n195 --> n223
    n292 --> n301
    n219 --> n265
    n216 --> n265
    n135 --> n149
    n196 --> n224
    n221 --> n266
    n250 --> n266
    n270 --> n302
    n291 --> n302
    n158 --> n186
    n282 --> n289
    n116 --> n122
    n108 --> n122
    n127 --> n150
    n129 --> n150
    n191 --> n225
    n161 --> n187
    n161 --> n188
    n266 --> n290
    n219 --> n290
    n206 --> n226
    n127 --> n151
    n129 --> n151
    n328 --> n333
    n220 --> n333
    n323 --> n334
    n321 --> n334
    n319 --> n335
    n307 --> n335
    n321 --> n336
    n264 --> n291
    n170 --> n189
    n189 --> n227
    n202 --> n228
    n156 --> n190
    n148 --> n191
    n158 --> n191
    n246 --> n267
    n278 --> n292
    n313 --> n322
    n161 --> n192
    n156 --> n192
    n140 --> n152
    n131 --> n153
    n262 --> n293
    n238 --> n268
    n119 --> n133
    n119 --> n134
    n133 --> n154
    n134 --> n154
    n141 --> n155
    n184 --> n229
    n178 --> n229
    n114 --> n123
    n116 --> n123
    n246 --> n269
    n181 --> n230
    n311 --> n323
    n204 --> n323
    n300 --> n323
    n331 --> n341
    n341 --> n347
    n241 --> n270
    n237 --> n270
    n127 --> n156
    n129 --> n156
    n298 --> n303
    n289 --> n304
    n144 --> n193
    n168 --> n193
    n119 --> n135
    n118 --> n135
    n235 --> n271
    n135 --> n157
    n340 --> n348
    n131 --> n158
    n133 --> n159
    n134 --> n159
    n151 --> n194
    n142 --> n195
    n160 --> n195
    n139 --> n160
    n186 --> n231
    n235 --> n272
    n227 --> n273
    n323 --> n337
    n279 --> n294
    n274 --> n294
    n247 --> n274
    n259 --> n295
    n257 --> n295
    n263 --> n296
    n192 --> n232
    n156 --> n196
    n127 --> n161
    n129 --> n161
    n266 --> n297
    n250 --> n297
    n301 --> n324
    n207 --> n233
    n189 --> n234
    n129 --> n162
    n127 --> n162
    n158 --> n197
    n186 --> n235
    n293 --> n305
    n293 --> n306
    n211 --> n275
    n225 --> n275
    n185 --> n236
    n226 --> n276
    n209 --> n276
    n180 --> n237
    n203 --> n237
    n287 --> n307
    n194 --> n238
    n132 --> n163
    n138 --> n163
    n278 --> n298
    n138 --> n164
    n153 --> n239
    n203 --> n239
    n163 --> n198
    n153 --> n240
    n203 --> n240
    n148 --> n241
    n180 --> n241
    n308 --> n325
    n161 --> n242
    n192 --> n242
    n290 --> n308
    n285 --> n308
    n299 --> n308
    n132 --> n165
    n238 --> n277
    n136 --> n166
    n158 --> n199
    n116 --> n124
    n167 --> n200
    n165 --> n200
    n290 --> n309
    n285 --> n309
    n299 --> n309
    n292 --> n310
    n298 --> n310
    n187 --> n243
    n188 --> n243
    n187 --> n244
    n132 --> n167
    n310 --> n326
    n119 --> n136
    n118 --> n136
    n148 --> n201
    n158 --> n201
    n197 --> n245
    n120 --> n137
    n110 --> n115
    n112 --> n115
    n111 --> n115
    n290 --> n311
    n285 --> n311
    n299 --> n311
    n215 --> n278
    n334 --> n342
    n130 --> n202
    n156 --> n202
    n289 --> n312
    n287 --> n312
    n283 --> n313
    n247 --> n279
    n153 --> n203
    n148 --> n203
    n136 --> n168
    n124 --> n138
    n254 --> n299
    n154 --> n204
    n130 --> n169
    n331 --> n343
    n143 --> n205
    n150 --> n205
    n329 --> n344
    n338 --> n344
    n303 --> n327
    n120 --> n139
    n237 --> n280
    n287 --> n314
    n182 --> n246
    n207 --> n246
    n153 --> n247
    n203 --> n247
    n170 --> n206
    n321 --> n338
    n160 --> n207
    n323 --> n339
    n120 --> n140
    n243 --> n281
    n340 --> n349
    n119 --> n141
    n116 --> n125
    n299 --> n315
    n172 --> n248
    n140 --> n170
    n152 --> n208
    n202 --> n249
    n147 --> n249
    n141 --> n171
    n116 --> n126
    n204 --> n328
    n300 --> n328
    n311 --> n328
    n115 --> n116
    n248 --> n282
    n287 --> n316
    n197 --> n250
    n192 --> n251
    n192 --> n252
    n156 --> n253
    n192 --> n253
    n283 x--x n288
    n142 x--x n160
    n143 x--x n150
    n127 x--x n129
    n212 x--x n222
    n212 x--x n234
    n144 x--x n168
    n176 x--x n252
    n257 x--x n259
    n146 x--x n171
    n332 x--x n333
    n216 x--x n219
    n118 x--x n119
    n118 x--x n120
    n181 x--x n183
    n119 x--x n120
    n119 x--x n124
    n287 x--x n289
    n147 x--x n202
    n148 x--x n153
    n148 x--x n158
    n221 x--x n250
    n222 x--x n234
    n132 x--x n138
    n151 x--x n156
    n151 x--x n161
    n191 x--x n201
    n292 x--x n298
    n152 x--x n170
    n153 x--x n158
    n133 x--x n134
    n323 x--x n328
    n156 x--x n161
    n274 x--x n279
    n197 x--x n199
    n239 x--x n240
    n242 x--x n251
    n308 x--x n309
    n165 x--x n167
    n110 x--x n111
    n110 x--x n112
```

# ITA_struggle_in_ethiopia

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n109{"ITA_organize_strikes_in_the_north"}
        n110["ITA_solid_progress"]
        n111(("ITA_struggle_in_ethiopia"))
        n112["ITA_the_abyssinian_fiasco"]
        n113{"ITA_the_southern_farmlands"}
        n114["ITA_unite_the_opposition"]
    end
    subgraph tier_1["Tier 1"]
        n115["ITA_servizio_informazione_militare"]
        n351["ITA_undermine_the_duce"]
    end
    subgraph tier_2["Tier 2"]
        n108{"ITA_conspiracies_in_the_shadows"}
        n116{"ITA_triumph_in_africa_bba"}
    end
    subgraph tier_3["Tier 3"]
        n117["ITA_anglo_italian_agreements"]
        n118["ITA_convene_the_grand_council"]
        n119{"ITA_culto_del_duce"}
        n120["ITA_defy_the_duce"]
        n121["ITA_devaluate_the_lire"]
        n122{"ITA_foreign_affairs"}
        n123["ITA_liberate_gramsci"]
        n124{"ITA_royal_intervention"}
        n125["ITA_the_new_emperor_of_ethiopia"]
        n126["ITA_topple_amhara_rulers"]
    end
    subgraph tier_4["Tier 4"]
        n127{"ITA_ally_yugoslavia"}
        n128["ITA_appeal_to_the_bourgeoisie"]
        n129{"ITA_balkan_ambition"}
        n130{"ITA_corpo_di_truppe_volontarie"}
        n131{"ITA_depose_mussolini"}
        n132{"ITA_empower_the_monarchists"}
        n133["ITA_la_battaglia_del_grano"]
        n134["ITA_la_battaglia_per_la_terra"]
        n135["ITA_ministero_della_cultura_popolare"]
        n136{"ITA_security_militias"}
        n137["ITA_seize_old_equipment"]
        n138["ITA_strengthen_the_coalition"]
        n139{"ITA_the_ethiopian_question"}
        n140{"ITA_the_italian_republic"}
        n141{"ITA_the_man_of_providence"}
    end
    subgraph tier_5["Tier 5"]
        n142["ITA_abolish_the_colonies"]
        n143["ITA_albanian_occupation"]
        n144["ITA_battaglioni_d_assalto"]
        n145["ITA_believe_obey_fight"]
        n146["ITA_boost_the_grand_council_of_fascism"]
        n147["ITA_demand_balearic_islands_bba"]
        n148{"ITA_dino_grandi_focus"}
        n149["ITA_expand_ond_membership"]
        n150["ITA_formalize_the_albanian_protectorate"]
        n151["ITA_guarantee_austrian_independence"]
        n152{"ITA_italian_socialism"}
        n153{"ITA_italo_balbo_focus"}
        n154["ITA_la_battaglia_per_le_nascite"]
        n155["ITA_legge_bottai"]
        n156{"ITA_militarize_the_rome_protocols"}
        n157["ITA_mobilize_womens"]
        n158{"ITA_monarchia_d_italia"}
        n159["ITA_move_toward_autarky"]
        n160["ITA_new_colonial_policies"]
        n161{"ITA_pact_of_steel"}
        n162["ITA_potential_allies_in_the_balkans"]
        n163["ITA_rebuild_the_north"]
        n164["ITA_referendum_on_the_monarchy"]
        n165["ITA_restore_the_statuto_albertino"]
        n166["ITA_revive_the_opera_nazionale_balilla"]
        n167["ITA_secure_control_over_parliament"]
        n168["ITA_strengthen_the_blackshirts"]
        n169["ITA_study_the_spanish_civil_war"]
        n170{"ITA_the_popular_front"}
        n171["ITA_to_live_as_a_lion"]
    end
    subgraph tier_6["Tier 6"]
        n172["ITA_a_leader_steps_forward"]
        n173["ITA_aid_for_the_spanish_republic"]
        n174["ITA_albanian_oil"]
        n175["ITA_banda_carita"]
        n176{"ITA_befriend_greece"}
        n177["ITA_befriend_japan"]
        n178["ITA_christian_democracy_r56"]
        n179{"ITA_common_ground"}
        n180["ITA_consolidate_power"]
        n181["ITA_cooperate_with_the_mafia"]
        n182["ITA_cooperatives_for_intensive_exploitation"]
        n183{"ITA_crush_the_mafia"}
        n184["ITA_disband_the_partisans"]
        n185["ITA_empower_the_unions"]
        n186["ITA_extraction_industry"]
        n187["ITA_german_military_assistance"]
        n188["ITA_giannini_sarnow_protocols"]
        n189{"ITA_industrial_socialization"}
        n190["ITA_invite_croatia"]
        n191["ITA_invite_france_to_military_partnership"]
        n192{"ITA_italian_irredentism"}
        n193["ITA_milizia_coloniale"]
        n194["ITA_negotiate_italian_claims"]
        n195["ITA_negotiations_with_albania"]
        n196["ITA_operazione_trajan"]
        n197{"ITA_power_to_the_king"}
        n198["ITA_reopen_the_markets"]
        n199{"ITA_revoke_the_acerbo_law"}
        n200["ITA_royal_militarism"]
        n201["ITA_seek_british_military_cooperation"]
        n202["ITA_spanish_italian_alliance"]
        n203{"ITA_stop_the_squandering"}
        n204{"ITA_strengthen_the_regime"}
        n205["ITA_support_albanian_irredentism"]
        n206["ITA_the_garibaldi_legion"]
        n207["ITA_the_italian_confederation"]
        n208["ITA_the_republics_leadership"]
    end
    subgraph tier_7["Tier 7"]
        n209["ITA_a_new_era_for_the_red_shirts"]
        n210["ITA_albanian_fascist_militia"]
        n211["ITA_anglo_italian_pact"]
        n212["ITA_appease_the_military"]
        n213["ITA_banda_koch"]
        n214["ITA_befriend_portugal"]
        n215["ITA_bring_back_exiled_intellectuals"]
        n216["ITA_christian_democracy"]
        n217["ITA_condemn_colonialism"]
        n218["ITA_control_the_industrial_elites"]
        n219["ITA_democratic_king"]
        n220{"ITA_devotion"}
        n221["ITA_disband_the_blackshirts"]
        n222["ITA_empower_the_carabinieri"]
        n223["ITA_enlist_the_bashkimi_kombetar"]
        n224["ITA_expand_the_romanian_oil_fields"]
        n225["ITA_franco_italian_pact"]
        n226["ITA_gruppi_di_difesa_della_donna"]
        n227["ITA_institute_the_five_year_plan"]
        n228["ITA_invite_andorra"]
        n229["ITA_liberalize_our_industries"]
        n230["ITA_mafia_abroad"]
        n231["ITA_new_corporations"]
        n232["ITA_operazione_tiberio"]
        n233["ITA_planned_economy"]
        n234["ITA_political_commissars"]
        n235["ITA_prepare_for_the_coming_wars"]
        n236["ITA_production_lines"]
        n237["ITA_purge_the_party"]
        n238["ITA_ratify_the_stresa_front"]
        n239["ITA_reinforce_regia_aeronautica"]
        n240["ITA_reorganize_regio_esercito"]
        n241["ITA_reorganize_the_party"]
        n242["ITA_request_control_of_french_territories"]
        n243["ITA_scientific_cooperation_r56"]
        n244["ITA_sea_wolves_bba"]
        n245["ITA_seek_papal_support"]
        n246["ITA_the_fight_overseas"]
        n247{"ITA_the_fourth_shore"}
        n248["ITA_the_path_to_progress"]
        n249["ITA_the_spanish_question"]
        n250["ITA_utilize_the_blackshirts"]
        n251["ITA_war_with_france"]
        n252{"ITA_war_with_greece"}
        n253["ITA_war_with_the_uk"]
    end
    subgraph tier_8["Tier 8"]
        n254["ITA_agents_of_the_church"]
        n255["ITA_army_modernization"]
        n256["ITA_ascari"]
        n257["ITA_befriend_turkey"]
        n258["ITA_bring_back_old_glories"]
        n259["ITA_claims_on_turkey_bba"]
        n260["ITA_compagnie_auto_avio_sahariane"]
        n261["ITA_cooperate_with_moderates"]
        n262["ITA_demand_dalmatia"]
        n263["ITA_demand_ticino"]
        n264["ITA_economic_reforms"]
        n265["ITA_expand_intelligence_services"]
        n266["ITA_expand_the_royal_guard"]
        n267["ITA_irregulars"]
        n268["ITA_joint_military_programs"]
        n269["ITA_liberate_the_workers_of_africa"]
        n270["ITA_meritocracy"]
        n271["ITA_mobilize_the_railway_guns"]
        n272["ITA_new_forms_of_weaponry"]
        n273["ITA_new_ricostruzione_industriale"]
        n274["ITA_oil_in_tripoli"]
        n275["ITA_proclaim_the_italian_empire"]
        n276["ITA_pugno_alzato"]
        n277["ITA_resume_food_importation"]
        n278{"ITA_social_stability"}
        n279["ITA_steel_in_tripoli"]
        n280{"ITA_the_fate_of_mussolini"}
        n281["ITA_the_italian_tiger"]
        n282{"ITA_union_in_the_party"}
    end
    subgraph tier_9["Tier 9"]
        n283["ITA_a_greater_purpose"]
        n284["ITA_combined_land_and_air_warfare"]
        n285{"ITA_crush_opposition"}
        n286["ITA_decrease_tariffs"]
        n287["ITA_defend_the_land"]
        n288["ITA_divino_duce"]
        n289["ITA_follow_the_soviet_union"]
        n290{"ITA_gloria_al_regno_d_italia"}
        n291["ITA_improve_the_industries"]
        n292["ITA_italia_libera"]
        n293["ITA_italys_destiny"]
        n294["ITA_novus_ordo"]
        n295["ITA_operazione_costantino"]
        n296["ITA_operazione_druso"]
        n297["ITA_paramilitary_training"]
        n298["ITA_reestablish_old_alliances"]
        n299{"ITA_strengthen_the_papacy"}
    end
    subgraph tier_10["Tier 10"]
        n300{"ITA_blackshirt_loyalty"}
        n301["ITA_european_democracies"]
        n302["ITA_expanded_corporatism"]
        n303["ITA_military_agreements"]
        n304["ITA_military_cooperation"]
        n305["ITA_prevent_the_spread_of_communism"]
        n306["ITA_preventive_intervention"]
        n307["ITA_raise_the_peoples"]
        n308["ITA_request_soviet_aid_alternative"]
        n309["ITA_sanction_mafia_killings"]
        n310["ITA_scientific_cooperation"]
        n311{"ITA_setting_course"}
        n312["ITA_special_brigades"]
        n313["ITA_spreading_the_eagles_wings"]
        n314["ITA_the_fight_against_stalinism"]
        n315["ITA_the_papacy_reborn"]
        n316["ITA_united_anarchist_confederations"]
    end
    subgraph tier_11["Tier 11"]
        n317["ITA_bring_down_fascist_strongholds"]
        n318["ITA_catholic_action"]
        n319["ITA_combined_research_effort"]
        n320["ITA_defense_against_capitalism"]
        n321["ITA_deus_vult"]
        n322["ITA_italian_hegemony"]
        n323["ITA_mare_nostrum_bba"]
        n324["ITA_peace_preservation"]
        n325["ITA_request_civil_war_support"]
        n326["ITA_secure_the_borders"]
        n327["ITA_the_enemies_of_capitalism"]
        n328{"ITA_towards_a_greater_italy"}
    end
    subgraph tier_12["Tier 12"]
        n329["ITA_a_time_for_war"]
        n330["ITA_auxiliaries"]
        n331["ITA_bend_the_bars"]
        n332["ITA_capo_supremo"]
        n333["ITA_heroes_of_the_nation"]
        n334["ITA_iberian_protection"]
        n335["ITA_il_sol_dell_avvenire"]
        n336["ITA_il_vento_aureo"]
        n337["ITA_new_roman_citizens"]
        n338["ITA_the_holy_lands"]
        n339["ITA_the_italian_legions"]
    end
    subgraph tier_13["Tier 13"]
        n340["ITA_all_roads_lead_to_rome"]
        n341["ITA_masters_of_the_aegean"]
        n342["ITA_south_american_alliances"]
        n343["ITA_subdue_the_sentinels"]
        n344["ITA_the_catholic_dominion"]
    end
    subgraph tier_14["Tier 14"]
        n345["ITA_a_colonial_empire"]
        n346["ITA_caligulas_pride"]
        n347["ITA_masters_of_the_mediterranean"]
        n348["ITA_modern_musculus"]
        n349["ITA_the_king_of_the_skies"]
    end
    subgraph tier_15["Tier 15"]
        n350["ITA_by_blood_alone"]
    end
    n343 --> n345
    n280 --> n283
    n170 --> n172
    n206 --> n209
    n321 --> n329
    n139 --> n142
    n245 --> n254
    n152 --> n173
    n205 --> n210
    n127 --> n143
    n129 --> n143
    n143 --> n174
    n150 --> n174
    n339 --> n340
    n122 --> n127
    n116 --> n117
    n201 --> n211
    n120 --> n128
    n179 --> n212
    n212 --> n255
    n234 --> n255
    n222 --> n255
    n246 --> n256
    n323 --> n330
    n122 --> n129
    n145 --> n175
    n175 --> n213
    n136 --> n144
    n156 --> n176
    n161 --> n177
    n156 --> n177
    n202 --> n214
    n147 --> n214
    n252 --> n257
    n176 --> n257
    n135 --> n145
    n328 --> n331
    n288 --> n300
    n141 --> n146
    n208 --> n215
    n235 --> n258
    n310 --> n317
    n345 --> n350
    n340 --> n346
    n328 --> n332
    n220 --> n332
    n315 --> n318
    n199 --> n216
    n164 --> n178
    n252 --> n259
    n176 --> n259
    n260 --> n284
    n304 --> n319
    n170 --> n179
    n152 --> n179
    n240 --> n260
    n239 --> n260
    n182 --> n217
    n153 --> n180
    n148 --> n180
    n351 --> n108
    n200 --> n218
    n116 --> n118
    n108 --> n118
    n216 --> n261
    n219 --> n261
    n152 --> n181
    n142 --> n182
    n122 --> n130
    n261 --> n285
    n265 --> n285
    n170 --> n183
    n152 --> n183
    n116 --> n119
    n277 --> n286
    n282 --> n287
    n304 --> n320
    n109 --> n120
    n113 --> n120
    n116 --> n120
    n130 --> n147
    n238 --> n262
    n251 --> n263
    n242 --> n263
    n199 --> n219
    n118 --> n131
    n315 --> n321
    n116 --> n121
    n171 --> n220
    n146 --> n220
    n204 --> n220
    n131 --> n148
    n197 --> n221
    n199 --> n221
    n164 --> n184
    n280 --> n288
    n241 --> n264
    n183 --> n222
    n124 --> n132
    n152 --> n185
    n195 --> n223
    n292 --> n301
    n219 --> n265
    n216 --> n265
    n135 --> n149
    n196 --> n224
    n221 --> n266
    n250 --> n266
    n270 --> n302
    n291 --> n302
    n158 --> n186
    n282 --> n289
    n116 --> n122
    n108 --> n122
    n127 --> n150
    n129 --> n150
    n191 --> n225
    n161 --> n187
    n161 --> n188
    n266 --> n290
    n219 --> n290
    n206 --> n226
    n127 --> n151
    n129 --> n151
    n328 --> n333
    n220 --> n333
    n323 --> n334
    n321 --> n334
    n319 --> n335
    n307 --> n335
    n321 --> n336
    n264 --> n291
    n170 --> n189
    n189 --> n227
    n202 --> n228
    n156 --> n190
    n148 --> n191
    n158 --> n191
    n246 --> n267
    n278 --> n292
    n313 --> n322
    n161 --> n192
    n156 --> n192
    n140 --> n152
    n131 --> n153
    n262 --> n293
    n238 --> n268
    n119 --> n133
    n119 --> n134
    n133 --> n154
    n134 --> n154
    n141 --> n155
    n184 --> n229
    n178 --> n229
    n114 --> n123
    n116 --> n123
    n246 --> n269
    n181 --> n230
    n311 --> n323
    n204 --> n323
    n300 --> n323
    n331 --> n341
    n341 --> n347
    n241 --> n270
    n237 --> n270
    n127 --> n156
    n129 --> n156
    n298 --> n303
    n289 --> n304
    n144 --> n193
    n168 --> n193
    n119 --> n135
    n118 --> n135
    n235 --> n271
    n135 --> n157
    n340 --> n348
    n131 --> n158
    n133 --> n159
    n134 --> n159
    n151 --> n194
    n142 --> n195
    n160 --> n195
    n139 --> n160
    n186 --> n231
    n235 --> n272
    n227 --> n273
    n323 --> n337
    n279 --> n294
    n274 --> n294
    n247 --> n274
    n259 --> n295
    n257 --> n295
    n263 --> n296
    n192 --> n232
    n156 --> n196
    n127 --> n161
    n129 --> n161
    n266 --> n297
    n250 --> n297
    n301 --> n324
    n207 --> n233
    n189 --> n234
    n129 --> n162
    n127 --> n162
    n158 --> n197
    n186 --> n235
    n293 --> n305
    n293 --> n306
    n211 --> n275
    n225 --> n275
    n185 --> n236
    n226 --> n276
    n209 --> n276
    n180 --> n237
    n203 --> n237
    n287 --> n307
    n194 --> n238
    n132 --> n163
    n138 --> n163
    n278 --> n298
    n138 --> n164
    n153 --> n239
    n203 --> n239
    n163 --> n198
    n153 --> n240
    n203 --> n240
    n148 --> n241
    n180 --> n241
    n308 --> n325
    n161 --> n242
    n192 --> n242
    n290 --> n308
    n285 --> n308
    n299 --> n308
    n132 --> n165
    n238 --> n277
    n136 --> n166
    n158 --> n199
    n116 --> n124
    n167 --> n200
    n165 --> n200
    n290 --> n309
    n285 --> n309
    n299 --> n309
    n292 --> n310
    n298 --> n310
    n187 --> n243
    n188 --> n243
    n187 --> n244
    n132 --> n167
    n310 --> n326
    n119 --> n136
    n118 --> n136
    n148 --> n201
    n158 --> n201
    n197 --> n245
    n120 --> n137
    n110 --> n115
    n112 --> n115
    n111 --> n115
    n290 --> n311
    n285 --> n311
    n299 --> n311
    n215 --> n278
    n334 --> n342
    n130 --> n202
    n156 --> n202
    n289 --> n312
    n287 --> n312
    n283 --> n313
    n247 --> n279
    n153 --> n203
    n148 --> n203
    n136 --> n168
    n124 --> n138
    n254 --> n299
    n154 --> n204
    n130 --> n169
    n331 --> n343
    n143 --> n205
    n150 --> n205
    n329 --> n344
    n338 --> n344
    n303 --> n327
    n120 --> n139
    n237 --> n280
    n287 --> n314
    n182 --> n246
    n207 --> n246
    n153 --> n247
    n203 --> n247
    n170 --> n206
    n321 --> n338
    n160 --> n207
    n323 --> n339
    n120 --> n140
    n243 --> n281
    n340 --> n349
    n119 --> n141
    n116 --> n125
    n299 --> n315
    n172 --> n248
    n140 --> n170
    n152 --> n208
    n202 --> n249
    n147 --> n249
    n141 --> n171
    n116 --> n126
    n204 --> n328
    n300 --> n328
    n311 --> n328
    n115 --> n116
    n111 --> n351
    n248 --> n282
    n287 --> n316
    n197 --> n250
    n192 --> n251
    n192 --> n252
    n156 --> n253
    n192 --> n253
    n283 x--x n288
    n142 x--x n160
    n143 x--x n150
    n127 x--x n129
    n212 x--x n222
    n212 x--x n234
    n144 x--x n168
    n176 x--x n252
    n257 x--x n259
    n146 x--x n171
    n332 x--x n333
    n216 x--x n219
    n118 x--x n119
    n118 x--x n120
    n181 x--x n183
    n119 x--x n120
    n119 x--x n124
    n287 x--x n289
    n147 x--x n202
    n148 x--x n153
    n148 x--x n158
    n221 x--x n250
    n222 x--x n234
    n132 x--x n138
    n151 x--x n156
    n151 x--x n161
    n191 x--x n201
    n292 x--x n298
    n152 x--x n170
    n153 x--x n158
    n133 x--x n134
    n323 x--x n328
    n156 x--x n161
    n274 x--x n279
    n197 x--x n199
    n239 x--x n240
    n242 x--x n251
    n308 x--x n309
    n165 x--x n167
    n110 x--x n111
    n111 x--x n112
```

# ITA_the_abyssinian_fiasco

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n108{"ITA_conspiracies_in_the_shadows"}
        n110["ITA_solid_progress"]
        n111["ITA_struggle_in_ethiopia"]
        n112(("ITA_the_abyssinian_fiasco"))
    end
    subgraph tier_1["Tier 1"]
        n115["ITA_servizio_informazione_militare"]
        n114{"ITA_unite_the_opposition"}
    end
    subgraph tier_2["Tier 2"]
        n109{"ITA_organize_strikes_in_the_north"}
        n113{"ITA_the_southern_farmlands"}
        n116{"ITA_triumph_in_africa_bba"}
    end
    subgraph tier_3["Tier 3"]
        n117["ITA_anglo_italian_agreements"]
        n118["ITA_convene_the_grand_council"]
        n119{"ITA_culto_del_duce"}
        n120["ITA_defy_the_duce"]
        n121["ITA_devaluate_the_lire"]
        n122{"ITA_foreign_affairs"}
        n123["ITA_liberate_gramsci"]
        n124{"ITA_royal_intervention"}
        n125["ITA_the_new_emperor_of_ethiopia"]
        n126["ITA_topple_amhara_rulers"]
    end
    subgraph tier_4["Tier 4"]
        n127{"ITA_ally_yugoslavia"}
        n128["ITA_appeal_to_the_bourgeoisie"]
        n129{"ITA_balkan_ambition"}
        n130{"ITA_corpo_di_truppe_volontarie"}
        n131{"ITA_depose_mussolini"}
        n132{"ITA_empower_the_monarchists"}
        n133["ITA_la_battaglia_del_grano"]
        n134["ITA_la_battaglia_per_la_terra"]
        n135["ITA_ministero_della_cultura_popolare"]
        n136{"ITA_security_militias"}
        n137["ITA_seize_old_equipment"]
        n138["ITA_strengthen_the_coalition"]
        n139{"ITA_the_ethiopian_question"}
        n140{"ITA_the_italian_republic"}
        n141{"ITA_the_man_of_providence"}
    end
    subgraph tier_5["Tier 5"]
        n142["ITA_abolish_the_colonies"]
        n143["ITA_albanian_occupation"]
        n144["ITA_battaglioni_d_assalto"]
        n145["ITA_believe_obey_fight"]
        n146["ITA_boost_the_grand_council_of_fascism"]
        n147["ITA_demand_balearic_islands_bba"]
        n148{"ITA_dino_grandi_focus"}
        n149["ITA_expand_ond_membership"]
        n150["ITA_formalize_the_albanian_protectorate"]
        n151["ITA_guarantee_austrian_independence"]
        n152{"ITA_italian_socialism"}
        n153{"ITA_italo_balbo_focus"}
        n154["ITA_la_battaglia_per_le_nascite"]
        n155["ITA_legge_bottai"]
        n156{"ITA_militarize_the_rome_protocols"}
        n157["ITA_mobilize_womens"]
        n158{"ITA_monarchia_d_italia"}
        n159["ITA_move_toward_autarky"]
        n160["ITA_new_colonial_policies"]
        n161{"ITA_pact_of_steel"}
        n162["ITA_potential_allies_in_the_balkans"]
        n163["ITA_rebuild_the_north"]
        n164["ITA_referendum_on_the_monarchy"]
        n165["ITA_restore_the_statuto_albertino"]
        n166["ITA_revive_the_opera_nazionale_balilla"]
        n167["ITA_secure_control_over_parliament"]
        n168["ITA_strengthen_the_blackshirts"]
        n169["ITA_study_the_spanish_civil_war"]
        n170{"ITA_the_popular_front"}
        n171["ITA_to_live_as_a_lion"]
    end
    subgraph tier_6["Tier 6"]
        n172["ITA_a_leader_steps_forward"]
        n173["ITA_aid_for_the_spanish_republic"]
        n174["ITA_albanian_oil"]
        n175["ITA_banda_carita"]
        n176{"ITA_befriend_greece"}
        n177["ITA_befriend_japan"]
        n178["ITA_christian_democracy_r56"]
        n179{"ITA_common_ground"}
        n180["ITA_consolidate_power"]
        n181["ITA_cooperate_with_the_mafia"]
        n182["ITA_cooperatives_for_intensive_exploitation"]
        n183{"ITA_crush_the_mafia"}
        n184["ITA_disband_the_partisans"]
        n185["ITA_empower_the_unions"]
        n186["ITA_extraction_industry"]
        n187["ITA_german_military_assistance"]
        n188["ITA_giannini_sarnow_protocols"]
        n189{"ITA_industrial_socialization"}
        n190["ITA_invite_croatia"]
        n191["ITA_invite_france_to_military_partnership"]
        n192{"ITA_italian_irredentism"}
        n193["ITA_milizia_coloniale"]
        n194["ITA_negotiate_italian_claims"]
        n195["ITA_negotiations_with_albania"]
        n196["ITA_operazione_trajan"]
        n197{"ITA_power_to_the_king"}
        n198["ITA_reopen_the_markets"]
        n199{"ITA_revoke_the_acerbo_law"}
        n200["ITA_royal_militarism"]
        n201["ITA_seek_british_military_cooperation"]
        n202["ITA_spanish_italian_alliance"]
        n203{"ITA_stop_the_squandering"}
        n204{"ITA_strengthen_the_regime"}
        n205["ITA_support_albanian_irredentism"]
        n206["ITA_the_garibaldi_legion"]
        n207["ITA_the_italian_confederation"]
        n208["ITA_the_republics_leadership"]
    end
    subgraph tier_7["Tier 7"]
        n209["ITA_a_new_era_for_the_red_shirts"]
        n210["ITA_albanian_fascist_militia"]
        n211["ITA_anglo_italian_pact"]
        n212["ITA_appease_the_military"]
        n213["ITA_banda_koch"]
        n214["ITA_befriend_portugal"]
        n215["ITA_bring_back_exiled_intellectuals"]
        n216["ITA_christian_democracy"]
        n217["ITA_condemn_colonialism"]
        n218["ITA_control_the_industrial_elites"]
        n219["ITA_democratic_king"]
        n220{"ITA_devotion"}
        n221["ITA_disband_the_blackshirts"]
        n222["ITA_empower_the_carabinieri"]
        n223["ITA_enlist_the_bashkimi_kombetar"]
        n224["ITA_expand_the_romanian_oil_fields"]
        n225["ITA_franco_italian_pact"]
        n226["ITA_gruppi_di_difesa_della_donna"]
        n227["ITA_institute_the_five_year_plan"]
        n228["ITA_invite_andorra"]
        n229["ITA_liberalize_our_industries"]
        n230["ITA_mafia_abroad"]
        n231["ITA_new_corporations"]
        n232["ITA_operazione_tiberio"]
        n233["ITA_planned_economy"]
        n234["ITA_political_commissars"]
        n235["ITA_prepare_for_the_coming_wars"]
        n236["ITA_production_lines"]
        n237["ITA_purge_the_party"]
        n238["ITA_ratify_the_stresa_front"]
        n239["ITA_reinforce_regia_aeronautica"]
        n240["ITA_reorganize_regio_esercito"]
        n241["ITA_reorganize_the_party"]
        n242["ITA_request_control_of_french_territories"]
        n243["ITA_scientific_cooperation_r56"]
        n244["ITA_sea_wolves_bba"]
        n245["ITA_seek_papal_support"]
        n246["ITA_the_fight_overseas"]
        n247{"ITA_the_fourth_shore"}
        n248["ITA_the_path_to_progress"]
        n249["ITA_the_spanish_question"]
        n250["ITA_utilize_the_blackshirts"]
        n251["ITA_war_with_france"]
        n252{"ITA_war_with_greece"}
        n253["ITA_war_with_the_uk"]
    end
    subgraph tier_8["Tier 8"]
        n254["ITA_agents_of_the_church"]
        n255["ITA_army_modernization"]
        n256["ITA_ascari"]
        n257["ITA_befriend_turkey"]
        n258["ITA_bring_back_old_glories"]
        n259["ITA_claims_on_turkey_bba"]
        n260["ITA_compagnie_auto_avio_sahariane"]
        n261["ITA_cooperate_with_moderates"]
        n262["ITA_demand_dalmatia"]
        n263["ITA_demand_ticino"]
        n264["ITA_economic_reforms"]
        n265["ITA_expand_intelligence_services"]
        n266["ITA_expand_the_royal_guard"]
        n267["ITA_irregulars"]
        n268["ITA_joint_military_programs"]
        n269["ITA_liberate_the_workers_of_africa"]
        n270["ITA_meritocracy"]
        n271["ITA_mobilize_the_railway_guns"]
        n272["ITA_new_forms_of_weaponry"]
        n273["ITA_new_ricostruzione_industriale"]
        n274["ITA_oil_in_tripoli"]
        n275["ITA_proclaim_the_italian_empire"]
        n276["ITA_pugno_alzato"]
        n277["ITA_resume_food_importation"]
        n278{"ITA_social_stability"}
        n279["ITA_steel_in_tripoli"]
        n280{"ITA_the_fate_of_mussolini"}
        n281["ITA_the_italian_tiger"]
        n282{"ITA_union_in_the_party"}
    end
    subgraph tier_9["Tier 9"]
        n283["ITA_a_greater_purpose"]
        n284["ITA_combined_land_and_air_warfare"]
        n285{"ITA_crush_opposition"}
        n286["ITA_decrease_tariffs"]
        n287["ITA_defend_the_land"]
        n288["ITA_divino_duce"]
        n289["ITA_follow_the_soviet_union"]
        n290{"ITA_gloria_al_regno_d_italia"}
        n291["ITA_improve_the_industries"]
        n292["ITA_italia_libera"]
        n293["ITA_italys_destiny"]
        n294["ITA_novus_ordo"]
        n295["ITA_operazione_costantino"]
        n296["ITA_operazione_druso"]
        n297["ITA_paramilitary_training"]
        n298["ITA_reestablish_old_alliances"]
        n299{"ITA_strengthen_the_papacy"}
    end
    subgraph tier_10["Tier 10"]
        n300{"ITA_blackshirt_loyalty"}
        n301["ITA_european_democracies"]
        n302["ITA_expanded_corporatism"]
        n303["ITA_military_agreements"]
        n304["ITA_military_cooperation"]
        n305["ITA_prevent_the_spread_of_communism"]
        n306["ITA_preventive_intervention"]
        n307["ITA_raise_the_peoples"]
        n308["ITA_request_soviet_aid_alternative"]
        n309["ITA_sanction_mafia_killings"]
        n310["ITA_scientific_cooperation"]
        n311{"ITA_setting_course"}
        n312["ITA_special_brigades"]
        n313["ITA_spreading_the_eagles_wings"]
        n314["ITA_the_fight_against_stalinism"]
        n315["ITA_the_papacy_reborn"]
        n316["ITA_united_anarchist_confederations"]
    end
    subgraph tier_11["Tier 11"]
        n317["ITA_bring_down_fascist_strongholds"]
        n318["ITA_catholic_action"]
        n319["ITA_combined_research_effort"]
        n320["ITA_defense_against_capitalism"]
        n321["ITA_deus_vult"]
        n322["ITA_italian_hegemony"]
        n323["ITA_mare_nostrum_bba"]
        n324["ITA_peace_preservation"]
        n325["ITA_request_civil_war_support"]
        n326["ITA_secure_the_borders"]
        n327["ITA_the_enemies_of_capitalism"]
        n328{"ITA_towards_a_greater_italy"}
    end
    subgraph tier_12["Tier 12"]
        n329["ITA_a_time_for_war"]
        n330["ITA_auxiliaries"]
        n331["ITA_bend_the_bars"]
        n332["ITA_capo_supremo"]
        n333["ITA_heroes_of_the_nation"]
        n334["ITA_iberian_protection"]
        n335["ITA_il_sol_dell_avvenire"]
        n336["ITA_il_vento_aureo"]
        n337["ITA_new_roman_citizens"]
        n338["ITA_the_holy_lands"]
        n339["ITA_the_italian_legions"]
    end
    subgraph tier_13["Tier 13"]
        n340["ITA_all_roads_lead_to_rome"]
        n341["ITA_masters_of_the_aegean"]
        n342["ITA_south_american_alliances"]
        n343["ITA_subdue_the_sentinels"]
        n344["ITA_the_catholic_dominion"]
    end
    subgraph tier_14["Tier 14"]
        n345["ITA_a_colonial_empire"]
        n346["ITA_caligulas_pride"]
        n347["ITA_masters_of_the_mediterranean"]
        n348["ITA_modern_musculus"]
        n349["ITA_the_king_of_the_skies"]
    end
    subgraph tier_15["Tier 15"]
        n350["ITA_by_blood_alone"]
    end
    n343 --> n345
    n280 --> n283
    n170 --> n172
    n206 --> n209
    n321 --> n329
    n139 --> n142
    n245 --> n254
    n152 --> n173
    n205 --> n210
    n127 --> n143
    n129 --> n143
    n143 --> n174
    n150 --> n174
    n339 --> n340
    n122 --> n127
    n116 --> n117
    n201 --> n211
    n120 --> n128
    n179 --> n212
    n212 --> n255
    n234 --> n255
    n222 --> n255
    n246 --> n256
    n323 --> n330
    n122 --> n129
    n145 --> n175
    n175 --> n213
    n136 --> n144
    n156 --> n176
    n161 --> n177
    n156 --> n177
    n202 --> n214
    n147 --> n214
    n252 --> n257
    n176 --> n257
    n135 --> n145
    n328 --> n331
    n288 --> n300
    n141 --> n146
    n208 --> n215
    n235 --> n258
    n310 --> n317
    n345 --> n350
    n340 --> n346
    n328 --> n332
    n220 --> n332
    n315 --> n318
    n199 --> n216
    n164 --> n178
    n252 --> n259
    n176 --> n259
    n260 --> n284
    n304 --> n319
    n170 --> n179
    n152 --> n179
    n240 --> n260
    n239 --> n260
    n182 --> n217
    n153 --> n180
    n148 --> n180
    n200 --> n218
    n116 --> n118
    n108 --> n118
    n216 --> n261
    n219 --> n261
    n152 --> n181
    n142 --> n182
    n122 --> n130
    n261 --> n285
    n265 --> n285
    n170 --> n183
    n152 --> n183
    n116 --> n119
    n277 --> n286
    n282 --> n287
    n304 --> n320
    n109 --> n120
    n113 --> n120
    n116 --> n120
    n130 --> n147
    n238 --> n262
    n251 --> n263
    n242 --> n263
    n199 --> n219
    n118 --> n131
    n315 --> n321
    n116 --> n121
    n171 --> n220
    n146 --> n220
    n204 --> n220
    n131 --> n148
    n197 --> n221
    n199 --> n221
    n164 --> n184
    n280 --> n288
    n241 --> n264
    n183 --> n222
    n124 --> n132
    n152 --> n185
    n195 --> n223
    n292 --> n301
    n219 --> n265
    n216 --> n265
    n135 --> n149
    n196 --> n224
    n221 --> n266
    n250 --> n266
    n270 --> n302
    n291 --> n302
    n158 --> n186
    n282 --> n289
    n116 --> n122
    n108 --> n122
    n127 --> n150
    n129 --> n150
    n191 --> n225
    n161 --> n187
    n161 --> n188
    n266 --> n290
    n219 --> n290
    n206 --> n226
    n127 --> n151
    n129 --> n151
    n328 --> n333
    n220 --> n333
    n323 --> n334
    n321 --> n334
    n319 --> n335
    n307 --> n335
    n321 --> n336
    n264 --> n291
    n170 --> n189
    n189 --> n227
    n202 --> n228
    n156 --> n190
    n148 --> n191
    n158 --> n191
    n246 --> n267
    n278 --> n292
    n313 --> n322
    n161 --> n192
    n156 --> n192
    n140 --> n152
    n131 --> n153
    n262 --> n293
    n238 --> n268
    n119 --> n133
    n119 --> n134
    n133 --> n154
    n134 --> n154
    n141 --> n155
    n184 --> n229
    n178 --> n229
    n114 --> n123
    n116 --> n123
    n246 --> n269
    n181 --> n230
    n311 --> n323
    n204 --> n323
    n300 --> n323
    n331 --> n341
    n341 --> n347
    n241 --> n270
    n237 --> n270
    n127 --> n156
    n129 --> n156
    n298 --> n303
    n289 --> n304
    n144 --> n193
    n168 --> n193
    n119 --> n135
    n118 --> n135
    n235 --> n271
    n135 --> n157
    n340 --> n348
    n131 --> n158
    n133 --> n159
    n134 --> n159
    n151 --> n194
    n142 --> n195
    n160 --> n195
    n139 --> n160
    n186 --> n231
    n235 --> n272
    n227 --> n273
    n323 --> n337
    n279 --> n294
    n274 --> n294
    n247 --> n274
    n259 --> n295
    n257 --> n295
    n263 --> n296
    n192 --> n232
    n156 --> n196
    n114 --> n109
    n127 --> n161
    n129 --> n161
    n266 --> n297
    n250 --> n297
    n301 --> n324
    n207 --> n233
    n189 --> n234
    n129 --> n162
    n127 --> n162
    n158 --> n197
    n186 --> n235
    n293 --> n305
    n293 --> n306
    n211 --> n275
    n225 --> n275
    n185 --> n236
    n226 --> n276
    n209 --> n276
    n180 --> n237
    n203 --> n237
    n287 --> n307
    n194 --> n238
    n132 --> n163
    n138 --> n163
    n278 --> n298
    n138 --> n164
    n153 --> n239
    n203 --> n239
    n163 --> n198
    n153 --> n240
    n203 --> n240
    n148 --> n241
    n180 --> n241
    n308 --> n325
    n161 --> n242
    n192 --> n242
    n290 --> n308
    n285 --> n308
    n299 --> n308
    n132 --> n165
    n238 --> n277
    n136 --> n166
    n158 --> n199
    n116 --> n124
    n167 --> n200
    n165 --> n200
    n290 --> n309
    n285 --> n309
    n299 --> n309
    n292 --> n310
    n298 --> n310
    n187 --> n243
    n188 --> n243
    n187 --> n244
    n132 --> n167
    n310 --> n326
    n119 --> n136
    n118 --> n136
    n148 --> n201
    n158 --> n201
    n197 --> n245
    n120 --> n137
    n110 --> n115
    n112 --> n115
    n111 --> n115
    n290 --> n311
    n285 --> n311
    n299 --> n311
    n215 --> n278
    n334 --> n342
    n130 --> n202
    n156 --> n202
    n289 --> n312
    n287 --> n312
    n283 --> n313
    n247 --> n279
    n153 --> n203
    n148 --> n203
    n136 --> n168
    n124 --> n138
    n254 --> n299
    n154 --> n204
    n130 --> n169
    n331 --> n343
    n143 --> n205
    n150 --> n205
    n329 --> n344
    n338 --> n344
    n303 --> n327
    n120 --> n139
    n237 --> n280
    n287 --> n314
    n182 --> n246
    n207 --> n246
    n153 --> n247
    n203 --> n247
    n170 --> n206
    n321 --> n338
    n160 --> n207
    n323 --> n339
    n120 --> n140
    n243 --> n281
    n340 --> n349
    n119 --> n141
    n116 --> n125
    n299 --> n315
    n172 --> n248
    n140 --> n170
    n152 --> n208
    n114 --> n113
    n202 --> n249
    n147 --> n249
    n141 --> n171
    n116 --> n126
    n204 --> n328
    n300 --> n328
    n311 --> n328
    n115 --> n116
    n248 --> n282
    n112 --> n114
    n287 --> n316
    n197 --> n250
    n192 --> n251
    n192 --> n252
    n156 --> n253
    n192 --> n253
    n283 x--x n288
    n142 x--x n160
    n143 x--x n150
    n127 x--x n129
    n212 x--x n222
    n212 x--x n234
    n144 x--x n168
    n176 x--x n252
    n257 x--x n259
    n146 x--x n171
    n332 x--x n333
    n216 x--x n219
    n118 x--x n119
    n118 x--x n120
    n181 x--x n183
    n119 x--x n120
    n119 x--x n124
    n287 x--x n289
    n147 x--x n202
    n148 x--x n153
    n148 x--x n158
    n221 x--x n250
    n222 x--x n234
    n132 x--x n138
    n151 x--x n156
    n151 x--x n161
    n191 x--x n201
    n292 x--x n298
    n152 x--x n170
    n153 x--x n158
    n133 x--x n134
    n323 x--x n328
    n156 x--x n161
    n274 x--x n279
    n109 x--x n113
    n197 x--x n199
    n239 x--x n240
    n242 x--x n251
    n308 x--x n309
    n165 x--x n167
    n110 x--x n112
    n111 x--x n112
```

# ITA_the_italian_liberation_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n352(("ITA_the_italian_liberation_war"))
    end
    subgraph tier_1["Tier 1"]
        n353{"ITA_fronte_militare_clandestino"}
    end
    subgraph tier_2["Tier 2"]
        n354["ITA_corpo_volontari_della_liberta"]
        n355["ITA_the_carabinieri"]
    end
    subgraph tier_3["Tier 3"]
        n356["ITA_gappisti"]
        n357["ITA_partisan_republics"]
        n358["ITA_the_kings_finest"]
    end
    subgraph tier_4["Tier 4"]
        n359["ITA_grande_rivolta_rurale"]
    end
    subgraph tier_5["Tier 5"]
        n360["ITA_liberation_or_death"]
    end
    subgraph tier_6["Tier 6"]
        n361["ITA_independence_rds"]
    end
    n353 --> n354
    n352 --> n353
    n354 --> n356
    n357 --> n359
    n356 --> n359
    n358 --> n359
    n360 --> n361
    n359 --> n360
    n354 --> n357
    n355 --> n357
    n353 --> n355
    n355 --> n358
    n354 x--x n355
```

# ITA_the_italian_social_republic

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n362(("ITA_the_italian_social_republic"))
    end
    subgraph tier_1["Tier 1"]
        n363["ITA_guardia_nazionale_repubblicana"]
    end
    subgraph tier_2["Tier 2"]
        n364["ITA_all_within_the_state"]
        n365["ITA_battaglioni_m"]
        n366["ITA_integrate_polizia_dell_africa_italiana"]
    end
    subgraph tier_3["Tier 3"]
        n367["ITA_anti_partisan_measures"]
        n368["ITA_reinforce_the_gustav_line"]
    end
    subgraph tier_4["Tier 4"]
        n369["ITA_the_social_republic_prevails"]
    end
    subgraph tier_5["Tier 5"]
        n370["ITA_independence_rsi"]
    end
    n363 --> n364
    n366 --> n367
    n363 --> n365
    n362 --> n363
    n369 --> n370
    n363 --> n366
    n365 --> n368
    n367 --> n369
    n364 --> n369
    n368 --> n369
```
