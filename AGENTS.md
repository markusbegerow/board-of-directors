# AGENTS.md — Board of Directors Ruleset

This is the master ruleset for the **Board of Directors strategic decision framework**, read natively by Codex CLI and OpenCode, and imported into `CLAUDE.md` for Claude Code. It applies to every model and agent (Claude, Codex, OpenCode, other LLM tools) that uses, extends, or maintains agents/skills in this repository, and is not derived from any other project's ruleset.

## 1. Scope and Purpose

This repository provides agents and skills that support **structured multi-perspective strategic decision-making**. The director profiles are archetypes inspired by publicly known topics, working methods, and leadership principles of the named individuals. They **do not simulate private views and do not speak on anyone's behalf**.

This framework is NOT a substitute for:
- Professional management consulting
- Legal or financial advice
- Any form of licensed professional advisory service

All outputs are analytical work aids. Users bear sole responsibility for how they use or act upon any output.

## 2. Language

- All agent/skill content, READMEs, and outputs are in **English**, unless the user explicitly requests another language.
- Technical terms (e.g., "blitzscaling", "TCO", "first principles") are used in their established forms and explained in context where needed.

## 3. Methodology

- Every board session follows the methodology in `references/methodik-board.md`:
  1. Frame the decision question clearly.
  2. Select 3–5 directors based on the decision type table.
  3. Collect independent votes from each director (thesis + argument + risk + next step).
  4. Surface conflicts and areas of consensus explicitly.
  5. Synthesize an integrated, prioritized decision proposal.
- Intermediate results are clearly marked as such.
- Uncertainties in the problem framing are resolved by asking the user, not by silent assumption.

## 4. Archetype and Source Discipline

- Binding rules are in `references/archetype-guidelines.md`. Director outputs must never be framed as real statements by the named individuals.
- Every output must clearly separate **robust findings**, **hypotheses**, and **speculative options**.
- Where a recommendation depends on an unverified assumption, that assumption is stated explicitly.

## 5. Output Structure and Formatting

- Board outputs are written in complete sentences, not as bare bullet skeletons.
- Numerical structure (1., 1.1, 1.2, …) is used for longer analyses; short answers may omit it.
- Tables are allowed where they improve readability (e.g., conflict matrices, decision scoring).
- Every recommendation is labelled as one of: **Act Now / Pilot / Investigate Further / Discard**.

## 6. Skill and Agent Convention

Every director agent and skill is hand-maintained in two places (see `CONTRIBUTING.md` for the full workflow — there is no generator script, both are edited directly):

- `.claude/agents/<name>.md` (10) — Claude Code's Task-spawnable subagent format, and `.opencode/agent/<name>.md` (10) — OpenCode's native subagent format (`mode: subagent`, condensed body). No Codex CLI equivalent exists; Codex reaches directors via the matching skill instead.
- `.claude/skills/<name>/SKILL.md` (17) and `.agents/skills/<name>/SKILL.md` (17) — identical [SKILL.md](https://agentskills.io)-standard content, read natively by Claude Code and OpenCode from `.claude/skills/`, and by Codex CLI from `.agents/skills/` (its project-local skill discovery root). OpenCode additionally has native `.opencode/command/<name>.md` slash-command wrappers (17) over the same skills, condensed and pointing at `agent: <director-name>` for the 10 persona commands.

Required YAML frontmatter for `.claude/`/`.agents/skills/` files:

```yaml
---
name: <kebab-case-name, max 64 characters>
description: "<purpose, max 1024 characters>"
---
```

Agent files (`.claude/agents/*.md`) may additionally include `tools: [...]` listing the Claude Code tools the agent is permitted to use — this field is Claude-Code-only and safely ignored elsewhere. `.opencode/agent/*.md` and `.opencode/command/*.md` use OpenCode's own frontmatter (`mode`, `agent`) and are out of scope for `scripts/validate_yaml_frontmatter.py`.

The markdown body of every agent or skill must begin with the archetype disclaimer block (see §7) and include at minimum:
1. **Purpose / Use Case** — when is this agent or skill invoked?
2. **Inputs** — what does the user need to provide?
3. **Working Method / Checklist** — step-by-step process.
4. **Output Format** — structure of the response, recommendation label required.

## 7. Disclaimer Mandate

Every agent file and skill file must begin with this clearly visible disclaimer (a full blockquote in `.claude/`/`.agents/skills/` files and in every `.opencode/agent/*.md`; at minimum a one-line pointer to it in `.opencode/command/*.md`, which are short instruction wrappers):

> **Disclaimer:** All director profiles are strategic archetypes inspired by publicly known topics, working methods, and leadership principles of the named individuals. They do not simulate private views and do not speak on anyone's behalf.

In addition, every output must:
- Clearly mark speculation as speculation and evidence as evidence.
- Not attribute any statement to a named individual as if it were their actual opinion.
- Include a note when a recommendation is highly contingent on unverified assumptions.

## 8. Privacy and Data Handling

- No real client data, confidential business information, personal data, or proprietary internal details in examples or commits.
- All examples use clearly fictionalised, anonymised scenarios.
- No API keys, secrets, or credentials in any file.

## 9. Versioning

- Version scheme `MAJOR.MINOR.PATCH`, starting at `001.0.0` for this project.
- All changes are documented in `CHANGELOG.md`.

## 10. Git Workflow

- Meaningful English commit messages.
- No force-push to the main branch.
- Before every merge: `python scripts/validate_yaml_frontmatter.py` must pass without errors, and any change to a `.claude/agents/`, `.claude/skills/`, `.agents/skills/`, or `.opencode/` file must be checked against its counterpart(s) per §6 (no automated sync — see `CONTRIBUTING.md`).

## Tool Compatibility

- **Claude Code**: reads this file via `CLAUDE.md`'s `@AGENTS.md` import; skills in `.claude/skills/*/SKILL.md` auto-trigger; subagents in `.claude/agents/*.md` are callable directly (`Use the <name> agent and evaluate: ...`).
- **OpenCode**: reads `AGENTS.md` natively; discovers `.claude/skills/*/SKILL.md` directly (no adapter needed) and also `.agents/skills/*/SKILL.md`; picks up `.opencode/agent/*.md` as subagents and `.opencode/command/*.md` for explicit `/command-name argument` invocation.
- **Codex CLI**: reads `AGENTS.md` natively (falls back to `CLAUDE.md` if present); its project-local skills discovery reads `.agents/skills/<name>/SKILL.md`.

Only `name` and `description` are portable skill frontmatter fields across all three tools. Live behavior has not been independently verified against installed Codex CLI / OpenCode binaries in this repository's own development environment — treat the above as the intended, structurally-correct integration, and confirm locally (see `README.md`).
