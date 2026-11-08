# 02: The cap modifier must not land on a focus ignition

**What to build:** an AI country is never steered off a civil-war focus by the
cap. Ignition focuses carry the ignition modifier alone, as the design says.

**Blocked by:** None (can start immediately). Ticket 01 reverts the 75 files
this ticket's defect last touched, so the two land together.

**Status:** ready-for-agent

## Problem

`docs/gdd/Civil Wars.md` is explicit:

> A war that starts from a national-focus completion reward, directly or through
> a script the focus always calls, is a **focus ignition**. It is exempt from both
> the cap and the cooldown [...] Do not add a cap modifier to an ignition focus's
> `ai_will_do`; keep `$ai_civil_war_ignition_modifier()` (0.25) alone.

The current `generate_focus_includes.py` does exactly what the doc forbids. On
regeneration it adds, to 75 existing includes:

```
+    +ai_will_do:
       modifier:
         $ai_sandbox_modifier()
       modifier:
         $ai_civil_war_ignition_modifier()
+      modifier:
+        factor(0)
+        sandbox_civil_war_cap_reached()
       modifier:
         $ai_high_tyranny_tilt()
```

Confirmed on `common/national_focus/Cuba.include`, focus
`CUB_overthrow_the_menocal_government` (line 143), which carries
`$sandbox_log_cw_ignition(...)` in its completion reward - it is an ignition
focus by the doc's own definition.

Consequence: while any civil war is running, every AI country's focus ignitions
are weighted to zero. The exemption the design grants them is silently gone, so
focus-driven civil wars stop happening after the first one - the opposite of the
behaviour the doc describes.

Note the distinction the same document draws two paragraphs later: the cap
belongs on `ai_will_do` of **decisions** (`$ai_civil_war_decision_cap()`,
Pattern D) and on the `ai_chance` of event options (Pattern B). Only focus
ignitions are exempt.

## What to do

Fix the generator so focus ignitions never receive the cap modifier. The
decision is already encoded in the doc; the code has to agree with it.

## Acceptance

- [ ] `generate_focus_includes.py` emits no `sandbox_civil_war_cap_reached()` on
      a focus whose `ai_will_do` also carries
      `$ai_civil_war_ignition_modifier()`, checked by regenerating and
      diffing.
- [ ] Regenerating from the current Rt56 tree produces no cap modifier in any
      include that already exists in `HEAD`.
- [ ] A focus that ignites a civil war indirectly - its reward calls a script
      that calls `start_civil_war` - is still treated as an ignition.
- [ ] Decision-side and event-side cap gating is unchanged
      (`$ai_civil_war_decision_cap()`, Pattern B `ai_chance`).
- [ ] `docs/gdd/Civil Wars.md` needs no edit: the code now matches it.
- [ ] The mod compiles with zero errors after regeneration.

## Out of scope

- Whether the cap itself is the right design. This ticket restores the doc's
  stated exemption; retuning the cap is a separate decision.
