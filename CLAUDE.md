# CLAUDE.md — Binding Ruleset

This document applies to every model and agent (Claude, Codex, other LLM tools) that uses, extends, or maintains skills in this repository. It is a standalone ruleset for the **Board of Directors strategic decision framework** and is not derived from any other project's ruleset.

## 1. Scope and Purpose

This repository provides Claude Code agents and skills that support **structured multi-perspective strategic decision-making**. The director profiles are archetypes inspired by publicly known topics, working methods, and leadership principles of the named individuals. They **do not simulate private views and do not speak on anyone's behalf**.

This framework is NOT a substitute for:
- Professional management consulting
- Legal or financial advice
- Any form of licensed professional advisory service

All outputs are analytical work aids. Users bear sole responsibility for how they use or act upon any output.

## 2. Language

- All skill and agent content, READMEs, and outputs are in **English**, unless the user explicitly requests another language.
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

Each agent lives under `agents/<name>.md` and each skill under `skills/<name>.md`. Required YAML frontmatter:

```yaml
---
name: <kebab-case-name, max 64 characters>
description: "<purpose, max 1024 characters>"
---
```

Agent files may additionally include `tools: [...]` listing the Claude Code tools the agent is permitted to use.

The markdown body of every agent or skill must begin with the archetype disclaimer block (see §7) and include at minimum:
1. **Purpose / Use Case** — when is this agent or skill invoked?
2. **Inputs** — what does the user need to provide?
3. **Working Method / Checklist** — step-by-step process.
4. **Output Format** — structure of the response, recommendation label required.

## 7. Disclaimer Mandate

Every agent file and skill file must begin with this clearly visible disclaimer:

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
- Before every merge: `python scripts/validate_yaml_frontmatter.py` and `python scripts/validate_plugin_structure.py` must pass without errors.
