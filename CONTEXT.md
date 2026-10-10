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
