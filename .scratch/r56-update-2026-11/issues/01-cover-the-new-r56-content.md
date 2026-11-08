# 01: Cover what the November update added, and nothing else

**What to build:** El Salvador, central America and Guangxi behave in sandbox
mode the way every other country already does. Their focus trees weight sandbox
priorities, and their Rt56 strategy plans switch off when sandbox mode is on.

**Blocked by:** None (can start immediately).

**Status:** ready-for-agent

## Problem

The 2026-11-08 Rt56 update added content this overlay has no counterpart for.
Without it, an AI El Salvador follows vanilla focus weighting inside a sandbox
session, and its historical and alternate plans keep driving it while every
other covered country has those plans disabled.

Measured on the current workshop tree:

- `common/national_focus/el_salvador.txt` - 134 focuses, 134 `ai_will_do`
  blocks, every one a bare `factor = 5` or `factor = 3`, none carrying
  `$ai_sandbox_modifier()`;
- `common/national_focus/r56_central_american_military_shared.txt` - new, no
  splices;
- `common/ai_strategy_plans/ELS_alternate_strategy_plan.txt` - declares
  `ELS_democratic_plan` and `ELS_communist_plan`;
- `common/ai_strategy_plans/ELS_historical_strategy_plan.txt` - declares
  `ELS_historical_plan`;
- `common/ai_strategy_plans/GXC_historical_strategy_plan.txt` - declares
  `GXC_hist_plan`.

For contrast, a covered country's plan include is:

```
ALB_historical_plan:
  enable:
    is_sandbox_mode_on(no)
  abort:
    OR:
      is_sandbox_mode_on(yes)
```

## What to do

1. Produce `common/national_focus/el_salvador.include` and
   `common/national_focus/r56_central_american_military_shared.include`.
   `.scratch/scripts/generate_focus_includes.py` already emits both correctly;
   take these two files from its output.
2. Add `common/ai_strategy_plans/` includes switching off the four plan blocks
   above, one include per Rt56 plan file, matching the existing pattern and
   listing every plan block the Rt56 file declares.
3. Revert the generator's changes to the other 201 includes. They are the
   subject of ticket 02 and must not be carried in by this one.

## Acceptance

- [ ] `el_salvador.include` exists and every one of its 134 focuses carries
      `+modifier: $ai_sandbox_modifier()`, with `$root_modifier()` on those
      without a prerequisite.
- [ ] `r56_central_american_military_shared.include` exists and carries the same
      splices for its focuses.
- [ ] Four plan includes exist, one per Rt56 plan file, and every plan block
      declared upstream appears in exactly one of them.
- [ ] Nothing else in `common/national_focus/` differs from `HEAD`: the working
      tree carries these files and no others.
- [ ] `_sandbox-r56` compiles with zero errors against the workshop root.
- [ ] A hands-off session run shows no `error.log` line attributable to the mod,
      and no `shared_focus` or `focus_tree` complaint.

## Out of scope

- The cap modifier the generator adds to 75 existing includes - ticket 02.
- The eleven focus files that were uncovered before this release - ticket 03.
- Uruguay: its Rt56 plan files are empty, so there is nothing to switch off.
