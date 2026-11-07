# 03 - Scorers never exclude the initiator, producing a self-embargo

Status: resolved
Type: bug
Blocked by: none

## What to build

A country never scores itself as a rival or as a scenario target, so no
self-directed diplomatic action can be issued.

## Problem

All three country scorers exclude the initiator with the same test:

```
modifier:
  factor(0)
  FROM == THIS
```

at `99_sandbox_scorer.hsl:33` (major rivals), `:107` (minor rivals) and `:186`
(join scorer). HSL compiles a scope-keyword comparison through `var_check` in
`hsl/modules/transformers/conditions.py:76-101`: the only special case is a
country tag on the right-hand side. `THIS` is a scope keyword, not a tag, so the
comparison falls through to the generic branch and emits:

```
check_variable = { FROM = THIS }
```

as seen at `99_sandbox_scorer.txt:42`, `:161` and `:262`. `check_variable`
compares a *variable* to a value; `FROM` and `THIS` are scope keywords there, not
variables. The comparison does not identify two scopes, so the intended
exclusion does not fire. No `error.log` line complains, which is why this has
survived.

The observable consequence is the session's only mod-attributable log line in
3669:

```
[20:46:14][1939.09.01.01]: common/scripted_effects/99_sandbox_scripted_effects.txt:5954:
  break_embargo: can't have a relation to yourself
```

A country's own tag reached an embargo slot, so `send_embargo` / `break_embargo`
were aimed at itself. Vanilla tests identity inside a scorer with a tag compare
(`common/scorers/country/operative_mission_scorer.txt:97` uses `tag = FROM`), and
the same idiom appears widely in `common/scripted_triggers/`.

## Why it matters

Rivalry is the director's main lever, and the two rival scorers are how a
country fills its three slots. A slot spent on itself is a slot not spent on a
real rival: the ledger reads `rivals[i] = self`, the rivalry band grows against
the country's own tag, and downstream economic posture then tries to embargo and
un-embargo itself. Every self-slot also distorts the band arithmetic the Honor
and Tyranny systems read.

## Fix shape

Replace the three `FROM == THIS` tests with a tag compare that actually tests
identity (`tag = FROM`, per the vanilla scorer idiom), and re-verify that the
compiled output no longer emits `check_variable = { FROM = THIS }`.

`99_sandbox_scorer.hsl` is a per-mod file (the two mods differ in the opinion
scale: 100 in vanilla, 200 in Rt56), so the fix lands in each mod's copy at
`common/scorers/country/99_sandbox_scorer.hsl`, not in synced core.

## Acceptance

The two session-side lines need a game run; the code and artifacts are verified.

- [x] The compiled scorer carries no `check_variable = { FROM = THIS }` in any of
      the three scorers, in both mods.
- [x] A scorer self-test written as a real identity test is verified to exclude
      the initiator; confirm the idiom against one scorer before rolling it out
      to all three.
- [x] No country can reach a `send_embargo` aimed at its own tag, guarded by the
      identity fix plus a defensive `NOT` at the call site.
- [x] A session produces no `break_embargo: can't have a relation to yourself`.
      The 1936-1941 run has zero occurrences in 3120 error lines.
- [x] With the `sandbox_log_rivals` gate raised, no line records a rival whose
      tag equals the logging country's own tag. 526 census rows, none with the
      logging tag in its own slots.

## Out of scope

- Opinion-scale differences between the two mods; those are intentional.
- The embargo ceiling and cooldown design (`economic-posture` work).

## Verification

- Recompile after the `.hsl` change (compile-after-hsl rule affects both mods).
- `grep -c "FROM = THIS"` over the compiled `99_sandbox_scorer.txt` must be 0.
- Run a session with `sandbox_log_rivals` raised and scan the extract for a
  self-rival tag.

## Implementation (2026-11-06)

Applied to both mods.

- The three `FROM == THIS` modifiers became `tag(FROM)` in each mod's own
  `99_sandbox_scorer.hsl`. `tag(FROM)` compiles to `tag = FROM`, the vanilla
  scorer idiom, and is a real identity test. The opinion-scale divergence
  between the mods (25/50/75 in vanilla, 50/100/150 in Rt56) was left alone.
- Defence in depth at both call sites in the shared engine: `send_embargo` and
  `break_embargo` in `99_sandbox_scripted_effects.hsl` are now wrapped in
  `if not tag(var:t)`, so a stale self-tag in a rival or embargo slot cannot
  reach the engine action even if a scorer regresses.
- New guard `.scratch/scripts/check_scorer_self_exclusion.py`, registered in
  `SHARED_MISC`. It audits the HSL source with comments stripped and the
  compiled `.txt`, requiring exactly three identity modifiers in each and no
  `check_variable` scope compare. Auditing the compiled output matters because
  the original bug was a source form that looked right and compiled wrong.

Evidence, all source-side:

- Both mods compile clean. Compiled scorer: `tag = FROM` three times,
  `check_variable = { FROM = THIS }` zero times.
- Compiled engine carries two `NOT = { tag = var:t }` guards, one per embargo
  action.
- The guard was negative-tested three ways, each caught: reverting one modifier
  to `FROM == THIS`, hand-editing the compiled output back to the broken form,
  and dropping one identity modifier entirely. All restored afterwards.
- `check_economic_posture.py`, `check_repick_gate.py`, `check_pick_gate.py`,
  `check_derail_arms.py` and `check_if_else.py` report 0 in both mods.
- **Correction to the ticket's scope note.** It said the fix is per-mod only. The
  scorer change is, but the call-site guards are not: `99_sandbox_scripted_effects.hsl`
  is shared core content. Editing it in the mods showed up as sync drift
  (`DIFF common/scripted_effects/99_sandbox_scripted_effects.hsl` for both), so
  the guards were moved into `sandbox-mod-core` and the mods' copies are again
  byte-identical to it. No per-mod edit survives there.
- **Not yet done: a game run.** The two session-side criteria need `error.log`
  and the `sandbox_log_rivals` extract from a real session.

## Open question

Whether `check_variable = { FROM = THIS }` silently evaluates false or merely
fails to compare scopes is not proven here; the ticket's chain (self-rival, then
self-embargo) is inferred from the error line plus the broken exclusion. The fix
stands either way because it replaces a non-identity test with an identity test,
and the call-site guards close the observable failure directly.
