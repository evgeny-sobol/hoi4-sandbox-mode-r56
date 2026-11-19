v0.4.4:
* feat: the mod now runs on Hearts of Iron IV 1.20, so the game no longer flags it as outdated
* fix: the Siamese and Australian focus trees carried a gate that never actually blocked anything - it asked whether a country may attack itself, which is always allowed, so the AI was steered by an empty condition and a nonsense line in the tooltip. The gates now name the real rival or are gone, and every remaining focus in both trees is weighed again
* fix: 26 Siamese and 9 Australian focuses were never gated at all, so their AI took them at vanilla priority; they now weigh like the rest of their trees

v0.4.3:
* feat: El Salvador now plays by sandbox rules - its focus tree and its AI plans are wired in like every other country's, so the AI stops following vanilla priorities and its old plans no longer run alongside them
* feat: the new central American military branch gets the same treatment, and Guangxi's plan is switched off in sandbox mode too
* fix: AI countries stopped starting civil wars through national focuses once the first one was running - the civil-war cap was being applied to focuses the design exempts, so those war paths went quiet for the rest of the game
* fix: the Chinese focus tree stays weighted correctly after the Road to 56 update moved 47 of its focuses, so Chinese AI keeps choosing them on purpose

v0.4.2:
* feat: the mod now carries the November Road to 56 update, so El Salvador arrives with a full tree and Siam, Australia, the Philippines and Germany get reworked branches
* fix: after a scenario's war broke out, the scenario system went quiet for the rest of the game - it now records the finished arc and picks a fresh one, so the next crisis still comes
* fix: the scenario pick could hand a whole arc to the country you were playing, which no AI lever can move - a demand you never press just sits there until it times out. Your country is no longer drawn as the aggressor, though it can still be a target
* fix: a scenario could be handed an aggressor already at war with the country it was meant to threaten, so the war declared itself and the arc was spent in a month. A spent pair is now skipped and stays available for a later pick
* fix: countries were growing a rivalry out of nothing - every pair took a permanent +2 a month, so a neighbour you had never fought climbed to Feud on its own and stayed there for years. Rivalries that nothing feeds now cool down
* fix: a country could hold the same rival in two of its three slots, and could even count itself as one, which made a grudge grow twice as fast and had the AI embargoing itself. Each rival now holds one slot, and a country never holds itself
* fix: the Chinese focus tree is patched again after the Road to 56 update moved 47 of its focuses, so Chinese AI keeps weighting them as intended
