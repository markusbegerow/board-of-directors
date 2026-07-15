# CHANGELOG.md

## v001.1.0 — Marketplace Installation & Structure Fixes

- Added a Claude Code Plugin Marketplace installation path (`/plugin marketplace add markusbegerow/board-of-directors`, `/plugin install board-of-directors@board-of-directors`) to `README.md` and `INSTALLATION.md` as "Option C", mirroring the working pattern from the sibling `claude-fuer-oeffentliche-verwaltung` repository.
- Fixed `scripts/validate_plugin_structure.py`, which had been broken by the prior ECC-compatible restructuring commit: it now checks the actual nested layout (`agents/<name>/AGENT.md`, `skills/<name>/SKILL.md`) instead of a flat `*.md` glob, and adds an automated check that the legacy flat tree (`agents/<name>.md`, `skills/<name>.md`) stays byte-identical to the nested plugin tree.
- Extended `scripts/validate_yaml_frontmatter.py` to also validate the nested plugin tree (previously it only checked the legacy flat tree, leaving the shipped plugin content unvalidated).
- Added the previously-missing `board-of-directors/README.md`, required by `CONTRIBUTING.md`'s own "Adding a New Plugin" checklist.
- Removed the orphaned root `.claude-plugin/plugin.json`, superseded by `board-of-directors/.claude-plugin/plugin.json` since `marketplace.json`'s `source` now points at `./board-of-directors`.
- Updated `CONTRIBUTING.md` to document the dual-tree (legacy flat + nested plugin) workflow and the new sync enforcement.
- Corrected a stale troubleshooting reference in `INSTALLATION.md` that only covered the legacy flat agent path.

## v001.0.0 — Initial Release (MVP)

- Repository scaffolding created: `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `QUICKSTART.md`, `INSTALLATION.md`, `EVAL_RESULTS.md`, `SKILLS.md`, `README.md`.
- License files `LICENSE-APACHE`, `LICENSE-MIT` (Apache-2.0 OR MIT, Author Markus Begerow).
- Core references under `references/`: `methodik-board.md`, `archetype-guidelines.md`, `source-hygiene.md`.
- Plugin `board-of-directors` with 10 director agent profiles and 17 skills.
  - 10 director agents: elon-musk, sam-altman, demis-hassabis, feifei-li, satya-nadella, jensen-huang, sundar-pichai, reid-hoffman, andrew-ng, steve-jobs.
  - 7 generic methodology skills: analyze, brainstorm, decision-matrix, risk-assess, synthesize, report, board (orchestrator).
  - 10 director persona invocation shortcuts: elon-skills, sam-skills, demis-skills, feifei-skills, satya-skills, jensen-skills, sundar-skills, reid-skills, andrew-skills, steve-skills.
- `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`.
- `scripts/` with validation and generation scripts.
