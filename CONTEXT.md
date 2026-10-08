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
