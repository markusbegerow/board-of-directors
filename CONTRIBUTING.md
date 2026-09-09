# Contributing

Thank you for your interest in this repository. Please review the following checklist before submitting a pull request.

## PR Checklist

- [ ] Content in English (see `AGENTS.md` §2).
- [ ] Archetype discipline followed per `references/archetype-guidelines.md`.
- [ ] Methodology followed per `references/methodik-board.md`.
- [ ] YAML frontmatter complete (`name`, `description`) and valid per `AGENTS.md` §6.
- [ ] Archetype disclaimer present at the top of any new or modified agent/skill file (see `AGENTS.md` §7).
- [ ] No real client data, personal information, confidential business details, or API keys.
- [ ] Every hand-mirrored counterpart (see below) updated to match.
- [ ] `python scripts/validate_yaml_frontmatter.py` passes without errors.
- [ ] For new agents or skills: entry added to `SKILLS.md` (or regenerated via `python scripts/generate_skills_md.py`).

## Hand-Maintained, Not Generated

This repository has **no build/sync script and no plugin system**. Every agent and skill exists as plain, hand-edited files in up to 4 places, kept identical/equivalent by hand (small enough at 44 files total that this is a deliberate choice, not an oversight — see `README.md`'s directory table):

- `.claude/agents/<name>.md` (10) — the source of truth for a director's content; also what Claude Code reads directly.
- `.opencode/agent/<name>.md` (10) — OpenCode's native subagent format (`mode: subagent`, no `name`/`tools` fields), a condensed prose adaptation of the same director, not a byte-identical copy.
- `.claude/skills/<name>/SKILL.md` (17) — the source of truth for a skill's content; read directly by Claude Code and OpenCode.
- `.agents/skills/<name>/SKILL.md` (17) — Codex CLI's native skills discovery path; a **plain copy** of the matching `.claude/skills/` file (keep these two byte-identical).
- `.opencode/command/<name>.md` (17) — OpenCode's explicit slash-command wrapper over the same skill, condensed, with `agent: <director-name>` on the 10 persona commands.

**Whenever you change a director or skill, update every file above that represents it.** There is no script to catch drift — review carefully before committing.

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
   - Disclaimer block (see `AGENTS.md` §7)
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
   - Short Command (note that Codex CLI / OpenCode reach this persona via the matching `<director-name>-skills` skill instead)
4. Create `.opencode/agent/<director-name>.md`: frontmatter `description` (reuse from step 2) + `mode: subagent`; body is a condensed prose distillation of step 3's content (see any existing pair, e.g. `elon-musk.md` in both `.claude/agents/` and `.opencode/agent/`, for the expected compression level — roughly a third of the length, prose paragraphs instead of `##` subsections) — always keep the disclaimer blockquote verbatim.
5. Create `.claude/skills/<director-name>-skills/SKILL.md` (the invocation shortcut skill) and copy it to `.agents/skills/<director-name>-skills/SKILL.md`.
6. Create `.opencode/command/<director-name>-skills.md`: frontmatter `description` (reuse from the skill) + `agent: <director-name>`; body is a short instruction paragraph using `$ARGUMENTS`, with a one-line pointer to the disclaimer in `.opencode/agent/<director-name>.md`.
7. Run `python scripts/validate_yaml_frontmatter.py` and `python scripts/generate_skills_md.py`.

## Adding a New Generic Skill

1. Create `.claude/skills/<skill-name>/SKILL.md` following the pattern of an existing generic skill.
2. Required YAML frontmatter: `name` and `description`.
3. Include the archetype disclaimer and a clear description of inputs and output format.
4. Copy it to `.agents/skills/<skill-name>/SKILL.md`.
5. Create `.opencode/command/<skill-name>.md`: frontmatter `description` only (no `agent:` field for generic skills), short `$ARGUMENTS`-based instruction body.
6. Run `python scripts/validate_yaml_frontmatter.py` and `python scripts/generate_skills_md.py`.

## Code of Conduct

See `CODE_OF_CONDUCT.md`.
