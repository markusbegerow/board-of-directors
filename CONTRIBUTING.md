# Contributing

Thank you for your interest in this repository. Please review the following checklist before submitting a pull request.

## PR Checklist

- [ ] Content in English (see `CLAUDE.md` §2).
- [ ] Archetype discipline followed per `references/archetype-guidelines.md`.
- [ ] Methodology followed per `references/methodik-board.md`.
- [ ] YAML frontmatter complete (`name`, `description`) and valid per `CLAUDE.md` §6.
- [ ] Archetype disclaimer present at the top of any new or modified agent/skill file (see `CLAUDE.md` §7).
- [ ] No real client data, personal information, confidential business details, or API keys.
- [ ] `python scripts/sync_content_trees.py` has been run after any canonical `.claude/agents/` or `.claude/skills/` edit.
- [ ] `python scripts/validate_yaml_frontmatter.py` passes without errors.
- [ ] `python scripts/validate_plugin_structure.py` passes without errors.
- [ ] For new agents or skills: entry added to `SKILLS.md` (or regenerated via `python scripts/generate_skills_md.py`).

## Canonical Source + Generated Mirrors

This repository ships every agent and skill from **one hand-edited canonical location**, mirrored automatically into the paths each tool/distribution channel actually needs:

- **Canonical source** — `.claude/agents/<name>.md` and `.claude/skills/<name>/SKILL.md`. These are the *only* files you hand-edit. Claude Code and OpenCode both read them natively the moment the repo is opened or cloned — no build step needed for those two tools.
- **Generated mirrors** — never hand-edit these; `python scripts/sync_content_trees.py` produces and owns them:
  - `.agents/skills/<name>/SKILL.md` — Codex CLI's native skills path (also a second discovery path for OpenCode).
  - `board-of-directors/skills/<name>/SKILL.md` and `board-of-directors/agents/<name>/AGENT.md` — the Claude Code marketplace plugin layout shipped via `.claude-plugin/marketplace.json` (`source: "./board-of-directors"`), also what the ECC harness reads when this project is registered.

**Whenever you add or edit a canonical `.claude/agents/` or `.claude/skills/` file, run `python scripts/sync_content_trees.py` before committing.** `python scripts/validate_plugin_structure.py` diffs every mirror against its canonical source and fails the build if they drift — treat that failure as "you forgot to run the sync script," not as a script bug. See `scripts/_content_trees.py` for the exact canonical→mirror mapping.

## Adding a New Director Agent

1. Create `.claude/agents/<director-name>.md` following the pattern of an existing agent file.
2. Required YAML frontmatter:
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
   - Short Command (note that Codex CLI / OpenCode reach this persona via the matching `<director-name>-skills` skill instead — see the `elon-musk` / `elon-skills` pair for the exact wording pattern)
4. Create a matching `.claude/skills/<director-name>-skills/SKILL.md` invocation shortcut.
5. Run `python scripts/sync_content_trees.py`, then the validation scripts, then update `SKILLS.md` (`python scripts/generate_skills_md.py`).

## Adding a New Generic Skill

1. Create `.claude/skills/<skill-name>/SKILL.md` following the pattern of an existing generic skill.
2. Required YAML frontmatter: `name` and `description`.
3. Include the archetype disclaimer and a clear description of inputs and output format.
4. Run `python scripts/sync_content_trees.py`, then the validation scripts, then update `SKILLS.md`.

## Adding a New Plugin

The repository currently ships a single plugin, `board-of-directors/`, as a concrete example of the required layout:

1. Create a subdirectory `<plugin-name>/` with `.claude-plugin/plugin.json` and `README.md`. Its `agents/` and `skills/` directories (`agents/<name>/AGENT.md`, `skills/<name>/SKILL.md`) are populated by `scripts/sync_content_trees.py`, not hand-authored — extend `scripts/_content_trees.py`'s mirror lists if you add a second plugin.
2. Add an entry to `.claude-plugin/marketplace.json` with `source: "./<plugin-name>"`.

## Code of Conduct

See `CODE_OF_CONDUCT.md`.
