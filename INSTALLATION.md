# Installation Guide (Mac / Windows)

This guide is for people without a development background who want to use this repository with Claude Code.

## Option A — Open as Project Directory (Claude Code, Codex CLI, or OpenCode — Works Today)

No install command needed in any of the three tools. Open the cloned folder as the working directory:

- **Claude Code** — `CLAUDE.md` loads automatically and gives Claude the full board methodology and ruleset; `.claude/agents/` and `.claude/skills/` are discovered as project agents/skills.
- **Codex CLI** — `AGENTS.md` loads automatically; `.agents/skills/` is discovered as the project skill catalog.
- **OpenCode** — `.claude/skills/` (and `.agents/skills/`) is discovered automatically as the project skill catalog.

Invoke the framework by natural language or by pasting the start prompt from `.claude/skills/board/SKILL.md`:

```
Use the Board of Directors orchestrator.
Decision question: Should we build or buy our data infrastructure?
```

Or ask a single director — Claude Code: "Use the elon-musk agent and evaluate: [question]"; Codex CLI / OpenCode: reference the `elon-skills` skill in natural language (no equivalent Task-spawnable subagent exists in those tools).

---

## Option B — Manual Setup (Git Clone)

### Prerequisites

- An Anthropic account with access to Claude Code.
- Git (to clone the repository), or use the ZIP download option on the repository page.

### Steps on Windows

1. Install Git if not already present: download from the official Git website and run the installer.
2. Open Command Prompt or PowerShell.
3. Navigate to your desired working folder.
4. Clone the repository:
   ```
   git clone https://github.com/markusbegerow/board-of-directors
   ```
   Alternatively: click "Code" → "Download ZIP" on the repository page, then extract the ZIP.
5. Open Claude Code (or Codex CLI, or OpenCode) and select the extracted folder as the working directory.
6. The project ruleset loads automatically — Claude now has the full board context. Use the natural language start prompt from `.claude/skills/board/SKILL.md` to begin.

### Steps on macOS

1. Open Terminal.
2. Git is usually pre-installed on macOS; alternatively install it via Homebrew (`brew install git`).
3. Navigate to your desired working folder and clone or extract the repository.
4. Open Claude Code and select the folder as the working directory.

---

## Option C — Claude Code Plugin Marketplace (Claude Code Only, No Clone Needed)

Use this if you want the plugin available in *other* Claude Code projects, not just a local clone: register the marketplace and install the plugin directly inside Claude Code:

```
/plugin marketplace add markusbegerow/board-of-directors
/plugin install board-of-directors@board-of-directors
```

Then invoke skills with the plugin name as a prefix:

```
/board-of-directors:board [your decision question]
```

Update later with `/plugin marketplace update board-of-directors`.

> **Note:** The shipped plugin content (`board-of-directors/agents/`, `board-of-directors/skills/`) is machine-generated and validated byte-identical to its canonical `.claude/` source, so hand-copy transcription errors are ruled out — but a live end-to-end `/plugin install` from the Marketplace has not yet been confirmed. If `/plugin install` fails, fall back to Option A or B and open an issue in the repository.

### First Test

1. Follow `QUICKSTART.md`.
2. Run a simple decision question using natural language: "Use the Board of Directors orchestrator. Decision question: Should we build or buy our data infrastructure?" — or use `/board-of-directors:board [question]` if you are on the ECC harness or installed via Option C.
3. Check that the output includes:
   - The archetype disclaimer at the top.
   - A list of the selected directors and why they were chosen.
   - Individual director votes (thesis, argument, risk, next step).
   - A conflict matrix.
   - A synthesised decision proposal with a labelled recommendation (Act Now / Pilot / Investigate Further / Discard).

### Common Issues

- **Context not active:** Check that the top-level selected folder actually contains `CLAUDE.md`. Claude Code loads this automatically as the project system prompt.
- **Skill not found:** Use the skill name exactly as listed in `SKILLS.md`. Names are kebab-case, lowercase.
- **Agent not loading:** Confirm the agent file exists — `.claude/agents/<name>.md` for Options A/B (project directory / ECC harness), or `board-of-directors/agents/<name>/AGENT.md` for Option C (Marketplace install) — and that the YAML frontmatter is valid (`python scripts/validate_yaml_frontmatter.py`).
- **Codex CLI / OpenCode not finding a skill:** Confirm `.agents/skills/<name>/SKILL.md` (Codex CLI) or `.claude/skills/<name>/SKILL.md` (OpenCode) exists and run `python scripts/sync_content_trees.py --check` to confirm it is in sync with its canonical source.

For further issues: open an issue in the repository.
