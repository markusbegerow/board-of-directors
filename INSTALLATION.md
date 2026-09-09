# Installation Guide (Mac / Windows)

This guide is for people without a development background who want to use this repository with Claude Code, Codex CLI, or OpenCode.

## Clone and Open the Folder

There is no plugin, no marketplace, and no install command — cloning the repository and opening it as your project directory is the whole setup, in any of the three tools.

### Prerequisites

- Access to Claude Code, Codex CLI, or OpenCode.
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
5. Open Claude Code, Codex CLI, or OpenCode and select the cloned/extracted folder as the working directory.
6. The project ruleset loads automatically:
   - **Claude Code** reads `CLAUDE.md` (which imports `AGENTS.md`); `.claude/agents/` and `.claude/skills/` become available immediately.
   - **Codex CLI** reads `AGENTS.md`; `.agents/skills/` becomes the project skill catalog.
   - **OpenCode** reads `AGENTS.md`; it picks up `.claude/skills/`, `.agents/skills/`, `.opencode/agent/`, and `.opencode/command/` automatically.

### Steps on macOS

1. Open Terminal.
2. Git is usually pre-installed on macOS; alternatively install it via Homebrew (`brew install git`).
3. Navigate to your desired working folder and clone or extract the repository.
4. Open your tool of choice and select the folder as the working directory — same automatic behavior as above.

---

## First Test

1. Follow `QUICKSTART.md`.
2. Run a simple decision question using natural language: "Use the Board of Directors orchestrator. Decision question: Should we build or buy our data infrastructure?" — or `/board [question]` in Claude Code / OpenCode.
3. Check that the output includes:
   - The archetype disclaimer at the top.
   - A list of the selected directors and why they were chosen.
   - Individual director votes (thesis, argument, risk, next step).
   - A conflict matrix.
   - A synthesised decision proposal with a labelled recommendation (Act Now / Pilot / Investigate Further / Discard).

## Common Issues

- **Context not active:** Check that the selected folder actually contains `CLAUDE.md` / `AGENTS.md` at its root.
- **Skill not found:** Use the skill name exactly as listed in `SKILLS.md`. Names are kebab-case, lowercase.
- **Agent not loading (Claude Code):** Confirm `.claude/agents/<name>.md` exists and its YAML frontmatter is valid (`python scripts/validate_yaml_frontmatter.py`).
- **Agent not loading (OpenCode):** Confirm `.opencode/agent/<name>.md` exists; run `opencode agent list` to check discovery.
- **Codex CLI / OpenCode not finding a skill:** Confirm `.agents/skills/<name>/SKILL.md` (Codex CLI) or `.claude/skills/<name>/SKILL.md` (OpenCode) exists; for OpenCode, `opencode debug skill` lists what it actually discovered.
- **Files out of sync:** `.claude/agents/` + `.claude/skills/` are hand-edited; `.agents/skills/`, `.opencode/agent/`, `.opencode/command/` are hand-mirrored from them (see `CONTRIBUTING.md`) — a mismatch means one of those mirrors wasn't updated after the source changed.

For further issues: open an issue in the repository.
