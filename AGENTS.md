# AGENTS.md — Short Rules for All Tools

This document is a condensed extract of `CLAUDE.md` for tools (e.g., Codex, ChatGPT, Gemini) that do not load the full ruleset. It applies in addition to, not instead of, `CLAUDE.md`.

## Mandatory Rules

1. **Language:** English, unless the user explicitly requests otherwise.
2. **Structure:** Numerical structure (1., 1.1, 1.2, …) for longer analyses; no bare bullet-point conclusions.
3. **Disclaimer:** Every agent or skill output begins with the archetype disclaimer from `CLAUDE.md` §7. Director outputs must not be presented as real statements by the named individuals.
4. **Source discipline:** Clearly separate robust findings, hypotheses, and speculative options. See `references/archetype-guidelines.md`.
5. **Recommendation labels:** Every recommendation is labelled as one of: **Act Now / Pilot / Investigate Further / Discard**.
6. **No real client or confidential data** in examples or commits.
7. **YAML frontmatter:** `name` (kebab-case, max 64 characters) and `description` (max 1024 characters); agent files may add `tools: [...]`.

## Skill Catalog (Codex CLI / OpenCode)

This repository's director personas and methodology skills are authored as [SKILL.md](https://agentskills.io) — the open, cross-tool skill standard. When this repository is your working directory:

- **Codex CLI** auto-discovers the catalog at `.agents/skills/<name>/SKILL.md` (17 skills: the `board` orchestrator, 6 shared methodology skills, and 10 `<director>-skills` persona shortcuts).
- **OpenCode** auto-discovers the same catalog from `.claude/skills/` and/or `.agents/skills/`.

Only `name` and `description` are portable frontmatter fields — this repo's `tools:` field on agent files is a Claude-Code-only extra that other tools safely ignore. Director *agents* (`.claude/agents/<name>.md`, Claude Code's Task-spawnable subagent format) have no equivalent in Codex CLI or OpenCode; reach a director's persona there via its `<name>-skills` skill instead. See `SKILLS.md` for the full index, and `CONTRIBUTING.md` for how canonical `.claude/` content is mirrored to `.agents/skills/` via `scripts/sync_content_trees.py`.

## Before Every Commit

```bash
python scripts/sync_content_trees.py
python scripts/validate_yaml_frontmatter.py
python scripts/validate_plugin_structure.py
```

All three commands must succeed (the first two with no drift/errors reported) before any commit or PR is created.
