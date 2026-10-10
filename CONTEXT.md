# Sandbox Mode Overhaul (Rt56)

An adaptation of the vanilla Sandbox Mode Overhaul for Road to 56: the same
sandbox-only AI rebuild against Rt56 content. This file is the shared
vocabulary; it is not a spec.

## Language

**Character**:
A person record: name, portraits, and one or more roles.
_Avoid_: advisor (a role, not the person)

**Advisor**:
A hireable role of a character in a slot (political advisor, army chief):
the player or AI spends political power to hire it. Hiring is gated by
`available` (hard gate) and weighted for the AI by `ai_will_do`.
_Avoid_: character, minister

**Opinion**:
The engine-tracked country-to-country total: individual modifiers add into
it and the clamp cuts the sum, [-100, 100] in vanilla and [-200, 200]
in Rt56.
_Avoid_: rivalry, relation

**Rivalry**:
The mod's own 0-100 per-slot intensity toward a declared rival; it feeds
opinion through fixed modifiers and never reads it.
_Avoid_: opinion, hostility

**Civil-war backing**:
The rule that a major power backs one side of every ongoing civil war: the
side whose ruling government matches the major's own.
_Avoid_: support (the scenario join lever), intervention

**Backer**:
A major power that backs a side of a civil war. Backing is AI-only.
_Avoid_: patron, sponsor

**Kin side**:
The civil-war side whose ruling government matches the backer's. The backer
gives it opinion, military access, equipment and AI pressure.
_Avoid_: ally side, friendly side

**Rival side**:
The other side of the same civil war; the backer gives it a negative opinion
modifier.
_Avoid_: enemy side, opposing side

**Major power**:
Any country where the engine's `is_major = yes` holds, so Rt56 `set_major`
grants (e.g. China later) count.
_Avoid_: great power, big country (a major is not a world power)

**Civil-war cap**:
The limit of one concurrent civil war for the AI: while one war runs, the AI
starts no new event/mission ignition. A focus ignition is exempt, but a
running focus ignition still occupies the slot.
_Avoid_: limit, threshold

**Focus ignition**:
A civil war that starts from a national-focus completion reward, directly or
through a script the focus always calls. Exempt from the civil-war cap and
its cooldown.
_Avoid_: ignition (that is the scenario term), focus war

**Event/mission ignition**:
A civil war that starts from a non-focus script (event, mission, decision,
on_action, balance of power). Subject to the civil-war cap.
_Avoid_: scripted war, event war

**Civil-war cooldown**:
The random wait of 0 to 12 months after a capped civil war ends, before the
AI may start another event/mission ignition. A focus ignition ignores it.
_Avoid_: delay, pause

**Civil-war fuse**:
A script that can start a civil war for a country: a focus reward, an event, a
mission timeout, a decision, an on_action, or a balance of power. A focus fuse
is a focus ignition (exempt from the cap); every other fuse is an event/mission
ignition (capped).
_Avoid_: trigger, source, spark

**Ignition overlay**:
The mod's gate on a civil-war fuse: an `sandbox_civil_war_ai_allowed()` check
added to the fuse, so a capped AI defers it instead of losing it.
_Avoid_: block, filter, patch
