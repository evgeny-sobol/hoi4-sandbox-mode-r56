# 03: Close out the eleven uncovered focus files, none of which needs an include

**What to build:** nothing in code. The eleven Rt56 focus files this overlay does
not include are all edges of files it already covers, so the deliverable is a
written record: why each one needs no include, so the next audit does not repeat
the work or - worse - emit an include that fails the compile.

**Blocked by:** Ticket 01 (committed).

**Status:** resolved

## What the eleven actually are

Two earlier drafts of this ticket guessed wrong. The file was re-read with
comments stripped, then each `shared_focus = ID` reference was resolved to the
file that declares it:

| file | what it holds | needs an include? |
| ---- | ------------- | ----------------- |
| `generic` | 21 `shared_focus` references into 17 files the overlay covers | no |
| `japan_old` | tree is **commented out** | no |
| `r56_arab_minor` | 8 refs, all into covered files | no |
| `r56_arctic_minor` | 6 refs, all into covered files | no |
| `r56_celtic_minor` | 10 refs, all into covered files | no |
| `r56_china_warlord_shared` | no tree, no focuses, no shared refs | no |
| `r56_microstate` | 5 refs, all into covered files | no |
| `r56_nationalist_spain` | 6 refs, all into covered files | no |
| `r56_polynesia_shared` | 7 refs, all into covered files | no |
| `r56_turkestan_minor` | 7 refs, all into covered files | no |
| `silesia` | tree is **commented out** | no |

None of the eleven declares a single `focus` or `shared_focus` block of its own.
Every one either holds references into a file the overlay already covers, or is
dead text. That is why `generate_focus_includes.py` skips them: it walks `focus`
and `shared_focus = {` declarations, and finds no block to rewrite.

Corrections against the earlier drafts:

- The first draft called `generic`, `japan_old`, `r56_nationalist_spain` and
  `silesia` "live" because `focus_tree = {` appeared in them. Two of those
  occurrences are inside comments. `japan_old` and `silesia` are dead upstream.
- The second draft planned to emit `shared_focus[id = X]:` includes for eight of
  them. That is the wrong layer: the ids those files reference are declared in
  `*_shared.txt` files the overlay already patches. An include for the referring
  file would either be empty or fail the compile with "block path segment not
  found".

The one reference that looked undeclared, `HABSBURG_part_of_something_bigger`, is
declared in `habsburg_joint.txt` as a `joint_focus`, and the overlay already
covers that file (`habsburg_joint.include`).

## Resolution

No code change. Everything the eleven trees pull in is covered at the point where
it is declared. Recorded here and in `docs/gdd/Road to 56.md` so the next audit
stops at the same conclusion instead of chasing eleven empty includes.

## Acceptance

- [x] Each of the eleven files is checked for `focus` and `shared_focus`
      declarations of its own: none has one.
- [x] Each `shared_focus` reference is resolved to its declaring file, and that
      file is verified to have an include in the overlay.
- [x] The two files whose trees are commented out (`japan_old`, `silesia`) are
      identified as dead rather than live.
- [x] The one unresolvable reference (`HABSBURG_part_of_something_bigger`) is
      traced to `habsburg_joint.txt` as a `joint_focus`, covered by
      `habsburg_joint.include`.
- [x] `docs/gdd/Road to 56.md` records the conclusion.
- [x] The mod compiles with no errors, with no include added for any of the
      eleven.

## Out of scope

- Asking Rt56 to un-comment the dead trees. That is upstream's call.
- `el_salvador` and `r56_central_american_military_shared` - closed by ticket 01.
