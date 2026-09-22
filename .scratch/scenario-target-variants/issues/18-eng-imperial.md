# 18: British imperial restoration arc (RAJ/dominions or USA/JAP)

**What to build:** a new imperial arc for Britain's monarchist/imperial branch (`ENG_god_save_the_king`: gate neutrality/fascism). Targets variant A (RAJ, dominions), variant B (USA, JAP), rolled 50/50. Arc data + crisis/ultimatum events, localisation, focus splices on `ENG_reclaim_the_jewel_in_the_crown` / `ENG_bring_the_dominions_back_into_the_fold` / `ENG_unite_the_anglosphere` with `$ai_scenario_focus_boost()`.

**Note:** this is `imperial` type (gate neutrality OR fascism). It needs the flip-gate helper ticket before it can be tested; see blocked-by.

**Blocked by:** 01 (target-array engine), 26 (flip-gate helper).

**Status:** ready-for-agent

- [ ] Pinned observer: `sc_pick` with variant, correct targets, gate holds (neutrality/fascism by crises).
- [ ] Derail `britain_not_imperial` when gate fails; otherwise ladder fires.
- [ ] Focus splices compile; `error.log` clean.