# Board of Directors (Plugin)

> **Disclaimer:** All director profiles are strategic archetypes inspired by publicly known topics, working methods, and leadership principles of the named individuals. They do not simulate private views and do not speak on anyone's behalf.

This is the Claude Code plugin source for **Board of Directors** — a structured, multi-perspective strategic decision framework. It is installed via the repository's `.claude-plugin/marketplace.json`. See the [repository root README](../README.md) and [`INSTALLATION.md`](../INSTALLATION.md) for full installation instructions, including the Claude Code Plugin Marketplace flow.

## Contents

- `agents/` — 10 director agent profiles (`<name>/AGENT.md`), each a distinct strategic perspective (e.g. Elon Musk for first-principles thinking, Steve Jobs for design and simplicity).
- `skills/` — 17 skills (`<name>/SKILL.md`): the `board` orchestrator, 6 shared methodology skills (analyze, brainstorm, decision-matrix, risk-assess, synthesize, report), and 10 persona invocation shortcuts.

See [`SKILLS.md`](../SKILLS.md) for the full flat index and [`README.md`](../README.md#the-directors) for the director table.

## Usage

Once the plugin is installed, invoke the orchestrator or a single director as a slash command:

```
/board-of-directors:board [your decision question]
```

```
/board-of-directors:elon-skills [your question]
```

## Content Source of Truth

This directory's `agents/<name>/AGENT.md` and `skills/<name>/SKILL.md` files are kept byte-identical to the legacy flat `agents/<name>.md` / `skills/<name>.md` files at the repository root (kept there for the "open repo as project directory" workflow described in `CLAUDE.md`). `python scripts/validate_plugin_structure.py` enforces this — see [`CONTRIBUTING.md`](../CONTRIBUTING.md) before editing either tree.
