# CHANGELOG.md

## v003.0.0 — Remove Marketplace/Plugin System; Native OpenCode Support

- **Breaking:** removed the Claude Code Plugin Marketplace distribution entirely — deleted `.claude-plugin/marketplace.json`, the nested `board-of-directors/` plugin package (`.claude-plugin/plugin.json`, `agents/<name>/AGENT.md`, `skills/<name>/SKILL.md`), and the generator/validator that produced it (`scripts/sync_content_trees.py`, `scripts/_content_trees.py`, `scripts/validate_plugin_structure.py`). There is no more `/plugin install` path and no more ECC-harness plugin registration; the project is used exclusively by cloning and opening the folder directly.
- Removed the marketplace-qualified slash-command line (`` `/board-of-directors:<name>` ``) from every canonical `.claude/skills/*/SKILL.md` invocation section — only the plain direct-clone Claude Code command and the Codex CLI/OpenCode natural-language line remain.
- `.agents/skills/<name>/SKILL.md` (Codex CLI's native skills path) is now a **hand-maintained plain copy** of `.claude/skills/<name>/SKILL.md`, not a script-generated mirror — small enough at 17 files to keep in sync by hand, matching the pattern used by a smaller reference project this restructuring was modeled on.
- Added `.opencode/agent/<name>.md` (10) — genuine OpenCode-native subagent files (`mode: subagent` frontmatter, condensed prose system prompt distilled from each `.claude/agents/*.md`, disclaimer preserved verbatim) instead of relying only on OpenCode picking up `.claude/skills/`.
- Added `.opencode/command/<name>.md` (17) — OpenCode slash-command wrappers over every skill (the 10 persona commands carry `agent: <director-name>`, routing through the matching `.opencode/agent/` file), condensed `$ARGUMENTS`-based instruction bodies.
- Restructured `AGENTS.md` to be the **master ruleset** (all 10 sections previously in `CLAUDE.md`, updated for the new paths and the removed plugin machinery), read natively by Codex CLI and OpenCode; `CLAUDE.md` now just imports it (`@AGENTS.md`) plus a short Claude Code-specific section — inverting the previous "CLAUDE.md full / AGENTS.md condensed" relationship.
- `scripts/validate_yaml_frontmatter.py` rewritten to scan `.claude/agents/`, `.claude/skills/`, and `.agents/skills/` directly (no shared-helper dependency); `scripts/generate_skills_md.py` likewise, plus a new header line in the regenerated `SKILLS.md` pointing at all 4 file locations.
- Rewrote `README.md`, `INSTALLATION.md`, `QUICKSTART.md`, and `CONTRIBUTING.md` to drop every marketplace/ECC-harness reference, replacing the 3-option install flow with a single "clone and open the folder" flow across all three tools, and an honest per-tool verification-status note (Claude Code structurally verified in-session; OpenCode/Codex CLI not installed in this environment, so their integration is documented as intended-but-not-live-tested).

## v002.0.0 — Cross-Tool Support (Codex CLI, OpenCode) & Canonical Source Restructuring

- **Breaking:** moved the canonical, hand-edited agent/skill source from the repo-root legacy flat tree (`agents/<name>.md`, `skills/<name>.md`) to `.claude/agents/<name>.md` and `.claude/skills/<name>/SKILL.md` — the paths Claude Code and OpenCode both read natively as project content with zero install step.
- Added a new generated mirror, `.agents/skills/<name>/SKILL.md`, so Codex CLI (and, redundantly, OpenCode) auto-discovers the full skill catalog (the `board` orchestrator, 6 shared methodology skills, 10 `<director>-skills` persona shortcuts) as soon as the repository is opened or cloned — no install command in any of the three tools.
- Replaced the hand-maintained "two trees, kept byte-identical" duplication with a **canonical source + generated mirrors** model: `board-of-directors/agents/<name>/AGENT.md`, `board-of-directors/skills/<name>/SKILL.md` (the marketplace plugin) and `.agents/skills/<name>/SKILL.md` (Codex CLI) are now produced by the new `scripts/sync_content_trees.py` and must never be hand-edited.
- Added `scripts/sync_content_trees.py` (with a `--check` dry-run mode) and `scripts/_content_trees.py` (shared canonical→mirror path mapping, imported by the sync script and both validators to avoid re-duplicating the mirror list itself).
- Updated `scripts/validate_yaml_frontmatter.py` and `scripts/validate_plugin_structure.py` to scan/enforce the new canonical + generated-mirror layout instead of the old legacy-flat/nested-plugin pair; `validate_plugin_structure.py`'s sync check now points contributors at `sync_content_trees.py` on drift.
- Updated `scripts/generate_skills_md.py` to read from `.claude/agents/` and `.claude/skills/`.
- Rewrote `CONTRIBUTING.md`'s duplication-workflow section, `CLAUDE.md` §6, `AGENTS.md` (added a Codex CLI / OpenCode skill-catalog section), `README.md`, `INSTALLATION.md`, `QUICKSTART.md`, and `board-of-directors/README.md` to describe the new model and add a zero-install "clone and open the folder" path for all three tools as the primary installation instructions; the Claude Code Marketplace path is kept as a secondary "install into other projects" option.
- Every canonical skill/agent file's invocation section now lists the Claude Code (direct and marketplace-qualified) slash command alongside the Codex CLI / OpenCode natural-language invocation, instead of a single Claude-only slash line.
- Re-initialized the git repository (this copy had no `.git`) and configured the `origin` remote; not pushed.

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
