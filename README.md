# Board of Directors

<p align="center">
  <img src="assets/images/board-of-directors.webp" alt="Board of Directors"/>
</p>

> **Important Notice:** This repository is an experimental collection of Claude Code agents and skills for multi-perspective strategic decision-making. The director profiles are archetypes inspired by publicly known topics, working methods, and leadership principles of the named individuals. They **do not simulate private views and do not speak on anyone's behalf**. All outputs are analytical work aids. This framework is **not** a substitute for professional management consulting, legal advice, or financial advice. Users bear sole responsibility for how they use or act upon any output.

## How to Use

There is no one-command install required. Just cloning and opening the folder already works in all three supported tools — Claude Code, Codex CLI, and OpenCode — with zero setup. Two extra options exist for Claude Code users who want the plugin available outside this folder.

### Option A — Clone and open the folder (Claude Code, Codex CLI, or OpenCode — zero setup)

1. Clone the repository: `git clone https://github.com/markusbegerow/board-of-directors`
2. Open the cloned folder in your tool:
   - **Claude Code** — select it as the working directory. `CLAUDE.md` loads automatically, and `.claude/agents/` / `.claude/skills/` are discovered as project agents/skills.
   - **Codex CLI** — open it as the project. `AGENTS.md` loads automatically, and `.agents/skills/` is discovered as the project skill catalog.
   - **OpenCode** — open it as the project. It discovers `.claude/skills/` (and `.agents/skills/`) automatically.
3. Invoke the board:
   - Claude Code: `/board [your decision question]`, or natural language.
   - Codex CLI / OpenCode: describe the task in natural language — the `board` skill auto-loads. There is no slash-command syntax in these tools.

Or ask a specific director — Claude Code: "Use the elon-musk agent and evaluate: [question]"; any tool: reference the matching `<director>-skills` skill (e.g. `elon-skills`) in natural language.

### Option B — ECC harness users (Claude Code)

If you are running Claude Code with the ECC harness (you'll see `/ecc:*` skills available):

1. Clone the repository as above.
2. Run `/ecc:projects` inside Claude Code and register the cloned folder.
3. Skills become available as slash commands, e.g.:

```
/board-of-directors:board Should we build or buy our data infrastructure?
```

### Option C — Claude Code Plugin Marketplace (Claude Code only, no clone needed)

Use this if you want the plugin available in *other* Claude Code projects, not just this folder: register the marketplace once, then install the plugin.

```
/plugin marketplace add markusbegerow/board-of-directors
/plugin install board-of-directors@board-of-directors
```

Skills are then available with the plugin name as a prefix, e.g.:

```
/board-of-directors:board Should we build or buy our data infrastructure?
```

Update later with:

```
/plugin marketplace update board-of-directors
```

> **Note:** The shipped plugin content (`board-of-directors/agents/`, `board-of-directors/skills/`) is machine-generated and validated byte-identical to its canonical source, so hand-copy transcription errors are ruled out — but a live end-to-end `/plugin install` from the Marketplace has not yet been confirmed in this session. Please confirm it works for you after installing, and open an issue if `/plugin install` rejects the plugin source.

See `INSTALLATION.md` for a step-by-step guide.

---

## What Is This?

This repository provides 10 director agent profiles and 7 shared methodology skills that support structured multi-perspective decision-making — usable directly in Claude Code, Codex CLI, and OpenCode, and additionally packaged as a Claude Code plugin.

| Type | Count | Canonical source | Purpose |
|---|---|---|---|
| Director agents | 10 | `.claude/agents/` | Individual strategic perspectives, each with distinct focus and working method (Claude Code Task-spawnable subagent) |
| Shared skills | 17 | `.claude/skills/` | Methodology skills (analyze, brainstorm, risk-assess, decision-matrix, synthesize, report) + persona invocation shortcuts + orchestrator — the cross-tool invocation surface for Claude Code, Codex CLI, and OpenCode |

## The Directors

| Agent | Director | Primary Perspective |
|---|---|---|
| `elon-musk` | Elon Musk | First principles, radical innovation, 10x scaling |
| `sam-altman` | Sam Altman | AI strategy, platform thinking, capital, ecosystem |
| `demis-hassabis` | Demis Hassabis | Research, hypotheses, evidence, scientific rigor |
| `feifei-li` | Fei-Fei Li | Human-centered AI, ethics, fairness, governance |
| `satya-nadella` | Satya Nadella | Enterprise, cloud, partnerships, transformation |
| `jensen-huang` | Jensen Huang | Hardware, compute, infrastructure, TCO |
| `sundar-pichai` | Sundar Pichai | Product, user value, ecosystem, scale |
| `reid-hoffman` | Reid Hoffman | Growth, network effects, venture, relationships |
| `andrew-ng` | Andrew Ng | Applied AI, data quality, pilots, learning |
| `steve-jobs` | Steve Jobs | Product vision, simplicity, UX, storytelling |

## Quick Start

1. Read `QUICKSTART.md` (2 minutes).
2. Open this repository in Claude Code as the project directory.
3. Run `/board [your decision question]` — the orchestrator selects the right directors automatically.
4. Or invoke a single director: use the `elon-musk` agent and evaluate: [question].

See `SKILLS.md` for a flat index of all skills, and `INSTALLATION.md` for a beginner-friendly setup guide.

## Ruleset

All agents and skills follow the ruleset in `CLAUDE.md` (full) and `AGENTS.md` (condensed for other tools). Core reference documents:

- `references/methodik-board.md` — 5-step board decision methodology.
- `references/archetype-guidelines.md` — Rules for how archetypes are defined and used responsibly.
- `references/source-hygiene.md` — How to separate speculation from evidence in outputs.

## Director Selection Guide

| Decision type | Directors to convene |
|---|---|
| New business model | elon-musk + reid-hoffman + sundar-pichai |
| AI product | sam-altman + andrew-ng + feifei-li + sundar-pichai |
| Research or technology decision | demis-hassabis + jensen-huang + andrew-ng |
| Enterprise transformation | satya-nadella + sundar-pichai + feifei-li |
| Pitch or product presentation | steve-jobs + reid-hoffman + sam-altman |
| Infrastructure decision | jensen-huang + satya-nadella + demis-hassabis |
| Governance and Responsible AI | feifei-li + demis-hassabis + satya-nadella |

## License

Apache-2.0 OR MIT — see `LICENSE`.

## Further Documents

- `CONTRIBUTING.md` — Contribution guidelines and PR checklist.
- `CODE_OF_CONDUCT.md` — Community code of conduct.
- `CHANGELOG.md` — Version history.
- `EVAL_RESULTS.md` — Quality evaluation status.
- `SKILLS.md` — Flat index of all skills and agents.

## Contact

- [Markus Begerow on LinkedIn](https://linkedin.com/in/markusbegerow)
- [GitHub](https://github.com/markusbegerow)
