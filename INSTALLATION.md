# Installation Guide (Mac / Windows)

This guide is for people without a development background who want to use this repository with Claude Code.

## Option A — Open as Project Directory (Works Today)

No plugin command needed. Open the cloned folder as your Claude Code working directory.
`CLAUDE.md` loads automatically and gives Claude the full board methodology and ruleset.

Invoke the framework by natural language or by pasting the start prompt from `skills/board.md`:

```
Use the Board of Directors orchestrator.
Decision question: Should we build or buy our data infrastructure?
```

Or ask a single director: "Use the elon-musk agent and evaluate: [question]"

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
5. Open Claude Code and select the extracted folder as the working directory.
6. `CLAUDE.md` loads automatically — Claude now has the full board context. Use the natural language start prompt from `skills/board.md` to begin.

### Steps on macOS

1. Open Terminal.
2. Git is usually pre-installed on macOS; alternatively install it via Homebrew (`brew install git`).
3. Navigate to your desired working folder and clone or extract the repository.
4. Open Claude Code and select the folder as the working directory.

### First Test

1. Follow `QUICKSTART.md`.
2. Run a simple decision question using natural language: "Use the Board of Directors orchestrator. Decision question: Should we build or buy our data infrastructure?" — or use `/board-of-directors:board [question]` if you are on the ECC harness.
3. Check that the output includes:
   - The archetype disclaimer at the top.
   - A list of the selected directors and why they were chosen.
   - Individual director votes (thesis, argument, risk, next step).
   - A conflict matrix.
   - A synthesised decision proposal with a labelled recommendation (Act Now / Pilot / Investigate Further / Discard).

### Common Issues

- **Context not active:** Check that the top-level selected folder actually contains `CLAUDE.md`. Claude Code loads this automatically as the project system prompt.
- **Skill not found:** Use the skill name exactly as listed in `SKILLS.md`. Names are kebab-case, lowercase.
- **Agent not loading:** Confirm the agent file exists in `agents/<name>.md` and the YAML frontmatter is valid (`python scripts/validate_yaml_frontmatter.py`).

For further issues: open an issue in the repository.
