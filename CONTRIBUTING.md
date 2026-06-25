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

## Adding a New Director Agent

1. Create `agents/<director-name>.md` following the pattern of an existing agent file.
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
   - Short Command
4. Create a matching `skills/<director-name>-skills.md` invocation shortcut.
5. Run validation scripts and update `SKILLS.md`.

## Adding a New Generic Skill

1. Create `skills/<skill-name>.md` following the pattern of an existing generic skill.
2. Required YAML frontmatter: `name` and `description`.
3. Include the archetype disclaimer and a clear description of inputs and output format.
4. Run validation scripts and update `SKILLS.md`.

## Adding a New Plugin

1. Create a subdirectory `<plugin-name>/` with `.claude-plugin/plugin.json`, `README.md`, `agents/`, and/or `skills/`.
2. Add an entry to `.claude-plugin/marketplace.json`.

## Code of Conduct

See `CODE_OF_CONDUCT.md`.
