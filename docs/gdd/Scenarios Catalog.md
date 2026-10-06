# Scenarios Catalog

Generated from `docs/scenarios/*.toml` by `core/tools/build_scenario_catalog.py` -
do not edit by hand. The arc schema lives in `docs/gdd/Scenarios.md`.

## Reading a diagram

- `([id])` rounded - a branch entry / path root.
- `[[id]]` double-bordered - a key focus the director boosts and logs.
- `[id]` plain - an intermediate prerequisite, boosted as part of the path closure.
- `A --> B` - B requires A.
- `A x--x B` - mutually exclusive: taking one hides the other.
