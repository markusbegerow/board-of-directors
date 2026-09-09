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

This directory's `agents/<name>/AGENT.md` and `skills/<name>/SKILL.md` files are **generated** — never hand-edit them. The canonical, hand-edited source lives at the repository root in `.claude/agents/<name>.md` and `.claude/skills/<name>/SKILL.md` (the same paths Claude Code and OpenCode read natively when the repo is opened or cloned directly). Run `python scripts/sync_content_trees.py` from the repository root after any canonical edit to regenerate this directory's content, along with the `.agents/skills/` mirror used by Codex CLI. `python scripts/validate_plugin_structure.py` enforces that this directory stays in sync with the canonical source — see [`CONTRIBUTING.md`](../CONTRIBUTING.md).
