# 00: spec - the 2026-11-08 Rt56 update leaves three gaps

**Status:** reference

Rt56 released on 2026-11-08 (workshop commit `36308183`, 226 files, +23 052 /
-8 493). Two of this overlay's patch files broke and were adapted; the
adaptation itself is committed. What this spec covers is what the update left
**uncovered**, found while making the compile pass.

## Findings

### 1. Two focus files and two AI-plan sets are new and unadapted

Rt56 added focus trees and strategy plans for El Salvador, reworked central
America, and added plans for Guangxi. Six files in this overlay's domain have no
counterpart:

| Rt56 file | What it needs |
| --------- | ------------- |
| `common/national_focus/el_salvador.txt` | AI weighting splices on 134 focuses |
| `common/national_focus/r56_central_american_military_shared.txt` | same |
| `common/ai_strategy_plans/ELS_alternate_strategy_plan.txt` | the plan is switched off in sandbox mode |
| `common/ai_strategy_plans/ELS_historical_strategy_plan.txt` | same |
| `common/ai_strategy_plans/GXC_historical_strategy_plan.txt` | same |

Measured: `el_salvador.txt` carries 134 `ai_will_do` blocks, all bare
`factor = 5` / `factor = 3`, none with `$ai_sandbox_modifier()`. The ELS plan
files declare three plan blocks (`ELS_democratic_plan`, `ELS_communist_plan`,
`ELS_historical_plan`), GXC one (`GXC_hist_plan`).

Uruguay is **not** a gap: both its plan files are empty (0 bytes, 0 blocks), so
there is nothing to switch off.

### 2. Running the focus generator rewrites 201 unrelated files

`generate_focus_includes.py` regenerates every include from the current Rt56
tree. Beyond producing the two new files it needs, it changes 75 existing
includes by adding

```
modifier:
  factor(0)
  sandbox_civil_war_cap_reached()
```

inside `+ai_will_do:` of focuses that also carry
`$ai_civil_war_ignition_modifier()`. That is the defect `03` covers.

### 3. Eleven focus files are uncovered and mostly untriggered

`generic`, `japan_old`, `r56_arab_minor`, `r56_arctic_minor`, `r56_celtic_minor`,
`r56_china_warlord_shared`, `r56_microstate`, `r56_nationalist_spain`,
`r56_polynesia_shared`, `r56_turkestan_minor`, `silesia`.

Checked each tree for a `country = { tag ... }` assignment or `default = yes`:

| file | trees | live |
| ---- | ----- | ---- |
| `generic` | 1 | yes (`default = yes`) |
| `japan_old` | 3 | yes (`japan_wtt_focus`, 3 tags) |
| `r56_nationalist_spain` | 1 | yes (1 tag) |
| `silesia` | 1 | yes (1 tag) |
| `r56_arab_minor` | 1 | **no tag, not default** |
| `r56_arctic_minor` | 1 | **no tag, not default** |
| `r56_celtic_minor` | 1 | **no tag, not default** |
| `r56_microstate` | 1 | **no tag, not default** |
| `r56_polynesia_shared` | 1 | **no tag, not default** |
| `r56_turkestan_minor` | 1 | **no tag, not default** |
| `r56_china_warlord_shared` | 0 | shared focuses only |

All eleven predate this release, so none is a regression. Four are live and
worth covering; six are reachable only if something assigns them at runtime,
which nothing in `history/countries` does; one carries shared focuses only.

## Tickets

- `01` - close the three new gaps and revert the generator's side effects.
- `02` - drop the cap modifier the generator adds to ignition focuses.
- `03` - decide what the eleven uncovered focus files are worth.

## Not a finding

`URG` has no sandbox plan because Rt56's URG plans are empty files.
