@AGENTS.md

## Claude Code specifics

Ten director subagents live under `.claude/agents/`: `elon-musk`, `sam-altman`, `demis-hassabis`, `feifei-li`, `satya-nadella`, `jensen-huang`, `sundar-pichai`, `reid-hoffman`, `andrew-ng`, `steve-jobs`. Seventeen skills live under `.claude/skills/` and trigger automatically based on the user's request: the `board` orchestrator, 6 shared methodology skills (`analyze`, `brainstorm`, `decision-matrix`, `risk-assess`, `synthesize`, `report`), and 10 `<director>-skills` persona-invocation shortcuts.

This project is a shared Git repo — see `README.md` for the overview and `INSTALLATION.md` for the full clone/usage guide across all three supported tools (Claude Code, Codex CLI, OpenCode).
