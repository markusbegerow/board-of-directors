# Contributing

Thank you for your interest in this repository. Please review the following checklist before submitting a pull request.

## PR Checklist

- [ ] Content in English (see `CLAUDE.md` §2).
- [ ] Archetype discipline followed per `references/archetype-guidelines.md`.
- [ ] Methodology followed per `references/methodik-board.md`.
- [ ] YAML frontmatter complete (`name`, `description`) and valid per `CLAUDE.md` §6.
- [ ] Archetype disclaimer present at the top of any new or modified agent/skill file (see `CLAUDE.md` §7).
- [ ] No real client data, personal information, confidential business details, or API keys.
- [ ] `python scripts/validate_yaml_frontmatter.py` passes without errors.
- [ ] `python scripts/validate_plugin_structure.py` passes without errors.
- [ ] For new agents or skills: entry added to `SKILLS.md` (or regenerated via `python scripts/generate_skills_md.py`).

## Two Trees, Kept in Sync

This repository ships agent and skill content in **two places** that must stay byte-identical:

- **Legacy flat tree** — `agents/<name>.md` and `skills/<name>.md` at the repo root. Used when someone opens the repo directly as a Claude Code project directory; `CLAUDE.md` loads automatically from the root, and these files are what natural-language start prompts reference.
- **Nested plugin tree** — `board-of-directors/agents/<name>/AGENT.md` and `board-of-directors/skills/<name>/SKILL.md`. This is the ECC-compatible layout actually shipped to `.claude-plugin/marketplace.json` (`source: "./board-of-directors"`) and installed via the Claude Code Plugin Marketplace.

**Whenever you add or edit an agent or skill, update both copies identically.** `python scripts/validate_plugin_structure.py` diffs the two trees and fails the build if they drift apart — treat that failure as "you forgot to update the other copy," not as a script bug.

## Adding a New Director Agent

1. Create `agents/<director-name>.md` following the pattern of an existing agent file, **and** an identical copy at `board-of-directors/agents/<director-name>/AGENT.md`.
2. Required YAML frontmatter (identical in both copies):
   ```yaml
   ---
   name: <kebab-case-director-name, max 64 characters>
   description: "<one-line purpose, max 1024 characters>"
   tools: [WebSearch, WebFetch, Read]
   ---
   ```
3. Required sections in the markdown body (in order):
   - Disclaimer block (see `CLAUDE.md` §7)
   - Role and Mission
   - When to Use
   - Guiding Principles
   - Key Questions
   - Working Method
   - Output Format (must include one of: Act Now / Pilot / Investigate Further / Discard)
   - Decision Logic
   - Boundaries
   - Generic Skills Available
   - Start Prompt (copy-paste template for users)
   - Short Command
4. Create a matching `skills/<director-name>-skills.md` invocation shortcut, plus its `board-of-directors/skills/<director-name>-skills/SKILL.md` counterpart.
5. Run validation scripts and update `SKILLS.md` (`python scripts/generate_skills_md.py`).

## Adding a New Generic Skill

1. Create `skills/<skill-name>.md` following the pattern of an existing generic skill, **and** an identical copy at `board-of-directors/skills/<skill-name>/SKILL.md`.
2. Required YAML frontmatter: `name` and `description` (identical in both copies).
3. Include the archetype disclaimer and a clear description of inputs and output format.
4. Run validation scripts and update `SKILLS.md`.

## Adding a New Plugin

The repository currently ships a single plugin, `board-of-directors/`, as a concrete example of the required layout:

1. Create a subdirectory `<plugin-name>/` with `.claude-plugin/plugin.json`, `README.md`, `agents/`, and/or `skills/` (director/skill files nested as `agents/<name>/AGENT.md` and `skills/<name>/SKILL.md`).
2. Add an entry to `.claude-plugin/marketplace.json` with `source: "./<plugin-name>"`.

## Code of Conduct

See `CODE_OF_CONDUCT.md`.
