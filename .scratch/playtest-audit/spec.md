# Playtest audit 1936-1941 (Rt56 session)

## Problem Statement

A full hands-off session of `_sandbox-r56` under Road to 56 ran 1936.01.01 to
1941.02.14 with `historical=0`. The telemetry extract holds 223 `#sandbox`
lines, and they stop dead at 1939.08.01. The scenario host stayed alive for the
whole run (HAI), the `sandbox_log_scenarios` gate stayed up, and the game
continued for another 19 in-game months. So the silence is a defect, not a
configuration change or a dead host.

Five findings came out of the run. One is a hard defect that kills the director
for the rest of the session. One is a scripting defect that leaks a country into
its own rival list. One is a selection-policy defect that hands the arc to the
human player. One is a missing eligibility filter. One is an observability gap
that made the first four harder to read than they had to be.

## Findings

1. **The director parks permanently after the first ignition.** The monthly tick
   runs the ignition check before the derail check, and the derail check takes
   its phase snapshot after ignition has already moved the phase to `ended`. The
   repick gate therefore never opens on the ignition path. Evidence: the 1939.07
   derail repicked normally (phase set inside the derail check, snapshot still
   valid), the 1939.08 ignition produced `sc_ignite` + `sc_success` + `sc_end`
   and then nothing at all.

2. **The pick does not exclude the human player as the aggressor.** Arc 5
   (napoleonic France) was drawn while the human was playing France, which makes
   the director's whole war ladder depend on the human declaring. Design goal 2
   in the GDD says the director pushes AI, not the human. The generated peak gate
   carried an explicit `aggressor->is_ai(no)` arm that fired peak on schedule,
   so the case was half-supported. Decided 2026-11-04: exclude the human's
   country instead, and delete the arm (ADR-0009).

3. **A scorer never excludes the initiator, which produced a self-embargo.** The
   self test in all three country scorers compiles to a `check_variable` compare
   against a scope keyword, which is not an identity test. The session's only
   mod-attributable `error.log` line is `break_embargo: can't have a relation to
   yourself`.

4. **Repick eligibility ignores war state.** Every generated `eligible()` tests
   `country_exists` only. A freshly repicked arc can therefore ignite on its
   first tick, as observed (pick at t=42, ignite at t=43), and deliver zero
   ladder play. Variant `b` targets were FRA and ENG.

5. **The peak timeout cannot say why it fired.** The classic derail line carries
   the phase and the month count but not whether the aggressor was human, nor
   whether live wargoals were sitting unclaimed. In this run FRA held wargoals on
   HOL and LUX for 11 straight months before `peak_timeout`, and an observer
   cannot tell design-compliant passivity from a stuck AI.

## Solution

Tickets below, in dependency order. 01 gates 04 and 05; 02 and 03 are
independent.

Decision log: finding 2 was decided in favour of excluding the human's country
from the pool (variant a of three), recorded as
`docs/adr/0009-human-aggressor-is-never-drawn.md`.

Note on scope: findings 1, 3 and 4 touch files that exist in both mods
(`99_sandbox_scenarios.hsl` and the per-mod `99_sandbox_scorer.hsl` are per-mod
copies, not synced core content), so a fix must land in `_sandbox-r56` and be
mirrored in `_sandbox`. Finding 2 and 5 are selection and telemetry policy and
apply to both mods for the same reason.

## Verification

- Recompile after any `.hsl` change (the compile-after-hsl rule).
- Re-extract with `.scratch/scripts/extract_sandbox.py` and confirm `#sandbox`
  lines continue past the first ignition, with at least one `sc_repick` after a
  war ignition.
- `error.log` carries no `break_embargo` self-relation line and no new
  mod-attributable lines.
- `git -C core` is clean and `python core/tools/sync_core.py --check` reports
  `drifted=0` for the mod under edit before commit.
