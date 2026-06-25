---
name: methodik-board
description: 5-step methodology for all Board of Directors sessions. Defines how to frame a decision, select directors, collect votes, surface conflicts, and synthesise an integrated recommendation.
---

# Board of Directors — Decision Methodology

This methodology applies to every board session and is referenced by `CLAUDE.md` §3. It governs both the `/board` orchestrator skill and any individual director agent working within a board context.

## Step 1: Frame the Decision Question

1. State the core decision in one clear sentence.
2. List the available options (if known); if options are open, say so explicitly.
3. Identify hard constraints (budget, timeline, regulation, technology limits).
4. Identify soft constraints (preferences, conventions, inherited habits — these can be challenged).
5. State the decision horizon: reversible short-term action, or long-term strategic commitment?

## Step 2: Select Directors

Use this table to select 3–5 directors. For questions spanning multiple categories, combine the relevant sets and cap at 5.

| Decision type | Directors to convene |
|---|---|
| New business model | elon-musk + reid-hoffman + sundar-pichai |
| AI product | sam-altman + andrew-ng + feifei-li + sundar-pichai |
| Research or technology decision | demis-hassabis + jensen-huang + andrew-ng |
| Enterprise transformation | satya-nadella + sundar-pichai + feifei-li |
| Pitch or product presentation | steve-jobs + reid-hoffman + sam-altman |
| Infrastructure decision | jensen-huang + satya-nadella + demis-hassabis |
| Governance and Responsible AI | feifei-li + demis-hassabis + satya-nadella |

Document why each director was selected. Justify inclusions and exclusions.

## Step 3: Collect Independent Votes

Spawn selected directors **in parallel** — each works independently to avoid anchoring effects. Each director produces:

- **Central thesis** (1 sentence)
- **Strongest argument** for their recommendation
- **Biggest risk** they see
- **Recommended next step**

Directors must not read each other's votes before completing their own.

## Step 4: Surface Conflicts

Construct a conflict matrix:

| Topic | Perspective A | Perspective B | Resolution |
|---|---|---|---|

Identify:
- Areas of genuine **consensus** (all or most directors agree).
- **Dissent** (significant disagreement on direction, priority, or risk).
- **Open assumptions** (recommendations that depend on unverified premises).

Clearly mark which conflicts are resolvable with more data and which are fundamental value trade-offs.

## Step 5: Synthesise

Using `/synthesize`, produce an integrated recommendation that:

1. States the board consensus (what most directors agree on).
2. Preserves the minority view with its rationale.
3. Gives a single prioritised recommendation labelled as one of:
   - **Act Now** — implement immediately
   - **Pilot** — test in controlled scope first
   - **Investigate Further** — more data needed before committing
   - **Discard** — not worth pursuing
4. Defines the prerequisites, abort criteria, and responsible role.
5. Proposes a concrete, reversible next step within 30 days.

## Output Formatting Rules

- Complete sentences throughout; no bare bullet skeletons as the final output.
- Intermediate conclusions are clearly marked: "Interim finding: …"
- Speculative options are marked as speculative: "Hypothesis (unverified): …"
- All outputs begin with the archetype disclaimer per `CLAUDE.md` §7.
