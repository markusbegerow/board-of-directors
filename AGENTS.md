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

## Before Every Commit

```bash
python scripts/validate_yaml_frontmatter.py
python scripts/validate_plugin_structure.py
```

Both scripts must pass without errors before any commit or PR is created.
