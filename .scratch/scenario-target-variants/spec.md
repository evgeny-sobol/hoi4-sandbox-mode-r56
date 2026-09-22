## Problem Statement

The scenario system currently hard-codes each arc's targets into its own `sandbox_seed_*_actors()` and every mechanic that reads them: seed, crises, peak ultimatums, derail checks, `sc_target`/`sc_goal`/`sc_justify` telemetry. The focus-tree catalog (gdd/Scenarios Catalog.md) defines ~28 arcs, each with two interchangeable target variants (A/B, rolled 50/50), and eight existing arcs need target variants added while many more arcs will follow. With hard-coded pairs, every arc duplicates seeding and derail logic six times over, and adding a target variant means editing seed + crises + peak + derail + telemetry for that arc. The schema needs a single per-session representation of "this arc's chosen targets" that all mechanics read, so the catalog can grow without per-arc code duplication.

## Solution

Introduce a single per-session array `sandbox_targets[]` (persistent, holds the chosen target tags for the active arc). At pick time (pinned or random), after an arc is chosen, the director rolls the A/B variant for that arc and writes the two target tags into `sandbox_targets[]`; the log line carries the variant. Every mechanism that today reads hard-coded target tags (`sandbox_seed_*_actors`, crisis/peak fire functions, derail checks, `sc_target`/`sc_goal`/`sc_justify` telemetry, `on_justifying_wargoal_pulse` and `on_wargoal_expire` tag guards) instead iterates `sandbox_targets[]` or compares `THIS in sandbox_targets[]`. New arcs declare only their two target variants (data), not new code paths for seed/derail/telemetry.

The pool becomes the full catalog: every arc in gdd/Scenarios Catalog.md is eligible when its aggressor exists. Existing arcs 1-8 keep their ids and gain a B variant; new arcs 9-28 follow the same data shape.

Seam for testing: the telemetry and ladder have no unit-test harness (this is a HoI4 script compiler, no in-game test runner available in CI). The observable external behavior is the `game.log` `#sandbox` telemetry lines from `extract_sandbox.py`. The seam to validate a target-variant change is an observer session grepping those lines: pin an arc, verify `sc_pick` carries the variant, `sc_seed` name-lists both chosen targets, and the derail/peak lines reference only the chosen pair. This is the same discipline as the existing acceptance checklist in gdd/Scenarios.md ("Log-first. Observer sandbox. Tick only when the grep holds.").

## User Stories

1. As a scenario player, I want the pool to include the full focus-tree catalog (28 arcs), so that sessions vary across all wars the seven majors can actually fight.
2. As a scenario player, I want every arc to have two interchangeable target variants, so that a pinned arc can still surprise me in a rerun.
3. As a scenario player, I want the target variant to be decided at startup and fixed for the session, so that the arc does not flip targets mid-game.
4. As a scenario designer, I want targets to live in a single array read by seed/crises/peak/derail/telemetry, so that adding a variant is a data change, not a code clone.
5. As a scenario observer, I want `sc_pick` to log the chosen variant, so that I can tell which target set a session ran without digging into focus state.
6. As a scenario observer, I want `sc_seed`, `sc_target`, `sc_goal` and `sc_justify` to emit only the chosen pair, so that telemetry stays minimal and unambiguous.
7. As a mod maintainer, I want new arcs (flip, imperial, historical) to require no new mechanics, macros, or hooks, so that the "no-new-mechanics per arc" acceptance rule in gdd/Scenarios.md stays true.
8. As a mod maintainer, I want the derail check to follow the chosen pair, so that an arc cannot park on targets that the rolled variant does not use.
9. As a mod maintainer, I want the existing 8 arcs to keep working when moved onto the array (same ids, same defaults as variant A), so that the change is backward compatible.
10. As a mod maintainer, I want the random pool to default to all arcs whose aggressor exists, so that the surprise pick covers the catalog automatically.

## Implementation Decisions

- **Target array**: persistent `sandbox_targets[]` (plus variant name string for logging, e.g. `sandbox_target_variant = a|b`). Written once at pick, cleared on derail/ignition.
- **Pick integration**: `sandbox_pick_scenario()` (and the repick path `sandbox_scenario_maybe_repick()`) resolves the chosen arc, rolls the variant, writes `sandbox_targets[]` and logs `sc_pick <arc> variant=<a|b>`. The variant is per-session.
- **Existing arcs move onto the array**: arcs 1-8 keep their current targets as variant A; their B variant comes from gdd/Scenarios Catalog.md (e.g. Arc 1 B = FRA/ENG, Arc 2 B = CZE/BUL, Arc 3 B = BRM/INS/MAL, Arc 4 B = FRA/ENG, Arc 5 B = GER/ITA, Arc 6 B = ENG/SOV, Arc 7 B = ENG, Arc 8 B = YUG/SLO).
- **New arcs are data**: arcs 9-28 declare `aggressor_tag`, `type` (historical/flip/imperial), `flip_ideology` (for flip/imperial), `variant_a[]`, `variant_b[]`, `block`, and key focuses. The engine derives seeding, crisis event routing, peak ultimatums, derail checks and telemetry from those fields.
- **Seed generalization**: `sandbox_seed_*_actors()` become one shared `sandbox_seed_actors(aggressor)` that iterates `sandbox_targets[]` (rival seed at 65, scenario_enemies symmetric), replacing eight nearly identical functions.
- **Crisis/peak generalization**: fire functions check `found_targets` presence via `sandbox_targets[]` instead of hard-coded tag pairs; each target gets its ultimatum event from a per-arc event id map.
- **Derail generalization**: the targets-gone / targets-neutralized arms iterate `sandbox_targets[]` (any target alive -> not derailed; all removed/neutralized -> derail).
- **Telemetry generalization**: `sc_target`/`sc_goal`/`sc_justify` guards compare `THIS in sandbox_targets[]` and `FROM in sandbox_targets[]`; `on_wargoal_expire` tag guards switch from `tag(GER|CZE|POL)` enumerations to the array membership.
- **Flip gates** (arcs 9, 10, 13, 16, 21, 23, 26 and EN/FRA imperial): resolved by `type` + `flip_ideology`; derail on crises if the aggressor is not on the ideology. Existing arcs 5/6 keep their current per-arc derail arms until unified, or are migrated to the same generic arm as part of this change (preferred: one generic flip-arm keyed by `flip_ideology`).
- **Data shape comes from the catalog**: gdd/Scenarios Catalog.md is the single source for arcs 9-28 variants; the engine must not re-hard-code what the catalog declares.
- **Scope of this spec**: full catalog (all 28 arcs), delivered as vertical-slice tickets under `.scratch/scenario-target-variants/issues/` (see `01`-`30`). Ticket 01 (target-array engine) is the single structural seam and gates every other ticket; tickets 02-09 add B variants to existing arcs; 10-23 add new historical arcs; 24-30 add flip/imperial arcs and the generic flip gate (ticket 26), which is intentionally deferred by user instruction. Start only on explicit user instruction ("start").

## Testing Decisions

- This repo has no in-game CI harness; the accepted verification seam is the observer-session grep of `game.log` via `scripts/extract_sandbox.py` (same as gdd/Scenarios.md acceptance).
- A good test is external behavior: run a pinned observer, extract telemetry, assert the `sc_pick` variant matches the rolled one, `sc_seed` lists exactly the two chosen targets, and no `sc_target`/`sc_goal`/`sc_justify` line references a target outside the chosen pair.
- Backward-compat check: pin each existing arc 1-8 with default (variant A) and verify the same telemetry shape as before the change (same target pairs, same event ids).
- Flip-gate check: pin a new flip arc (e.g. 9) and verify `sc_derail <arc>_not_<ideology>` fires on crises when the aggressor did not flip, matching the arcs 5/6 pattern.
- Prior art: the existing acceptance checklist items in gdd/Scenarios.md ("Joiners", "Derail", "Per-arc gates", "No error.log lines attributable to scenario files") and the `sc_*` telemetry greps already used for s7-s10 analysis.
- Out of scope for automated tests: anything the compiler cannot validate in CI (the game itself); we rely on clean HSL compilation plus observer greps.

## Out of Scope

- Building the full 28-arc content (events, localisation, focus splices) is not this spec's deliverable alone; it proceeds ticket by ticket, starting only on explicit instruction. The engine generalization + variant data for arcs 1-8 (A/B) and the first cohort (9-12) is the first milestone; arcs 13-28 are follow-up tickets once the shape is proven.
- New mechanics, macros, or hooks for individual arcs (the catalog rule: if an arc needs one, fix the schema).
- Changing the ladder calendar, join scorer, or block composition per arc (stays shared).
- The vanilla-port repo (`_sandbox`): this spec targets `_sandbox-r56`; porting after the shape stabilises.
- Russian GDD mirrors (per the gdd-russian-mirror rule they are only written on explicit request).

## Further Notes

- The catalog marks arcs 23 (ENG-communist) and 25 (USA global hegemony) as least plausible; whether they stay in the pool is an open design question tracked in the catalog. This spec does not decide it.
- A binary variant-A/B roll is the minimum; the array design does not prevent more variants later, but two is the current spec.
- The repick path must clear `sandbox_targets[]` before re-rolling, mirroring how `scenario_enemies[]` is cleared today.
- The compiler's macro system is the natural place for the shared seed/derail/telemetry helpers; concrete file layout is left to implementation (do not freeze paths in the spec).