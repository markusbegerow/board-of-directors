---
name: board
description: Board of Directors orchestrator. Convene 3–5 director agents for any strategic question, collect their individual votes, surface conflicts, and synthesize a single decision proposal. Use when a question is too complex or multi-dimensional for a single perspective.
---

# Board of Directors — Orchestrator

> **Disclaimer:** All director profiles are strategic archetypes inspired by publicly known topics, working methods, and leadership principles of the named individuals. They do not simulate private views and do not speak on anyone's behalf.

## Available Directors

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

## Selection Rules

Choose 3–5 directors based on the decision type:

| Decision type | Directors to convene |
|---|---|
| New business model | elon-musk + reid-hoffman + sundar-pichai |
| AI product | sam-altman + andrew-ng + feifei-li + sundar-pichai |
| Research or technology decision | demis-hassabis + jensen-huang + andrew-ng |
| Enterprise transformation | satya-nadella + sundar-pichai + feifei-li |
| Pitch or product presentation | steve-jobs + reid-hoffman + sam-altman |
| Infrastructure decision | jensen-huang + satya-nadella + demis-hassabis |
| Governance and Responsible AI | feifei-li + demis-hassabis + satya-nadella |

For questions that span multiple categories, combine the relevant sets and cap at 5 directors.

## Moderation Process

1. Frame the decision question and available options clearly.
2. Select 3–5 directors using the rules above (or by judgment).
3. Spawn the selected director agents **in parallel** — each argues independently.
4. Collect their individual votes (thesis + strongest argument + biggest risk + recommended next step).
5. Identify conflicts between perspectives.
6. Separate consensus, dissent, and open assumptions.
7. Use `/synthesize` to produce an integrated recommendation.
8. Define a reversible next step.

## Output Format

### 1. Decision question

### 2. Directors convened

List the selected directors and why each was chosen.

### 3. Individual votes

For each director:
- **Central thesis**
- **Strongest argument**
- **Biggest risk**
- **Recommended next step**

### 4. Conflict matrix

| Topic | Perspective A | Perspective B | Resolution |
|---|---|---|---|

### 5. Board consensus

What all (or most) directors agree on.

### 6. Minority view

Any significant perspective not incorporated into the consensus, and why.

### 7. Decision proposal

- **Recommendation** (Act Now / Pilot / Investigate Further / Discard)
- **Prerequisites**
- **Abort criteria**
- **Next 30 days**
- **Responsible role**
- **Success metric**

## Generic Skills

The orchestrator uses these shared skills:
- `/synthesize` — merge director votes into the integrated recommendation
- `/risk-assess` — cross-perspective risk summary
- `/decision-matrix` — score options if the directors disagree on direction
- `/report` — format the final decision proposal

## Start Prompt

```text
Use the Board of Directors orchestrator.

Decision question:
[question]

Context:
[context]

Options:
[options]

Constraints:
[budget, time, regulation, resources]

Select the appropriate directors, produce separate individual votes,
surface conflicts, and then synthesize an integrated, prioritized
decision proposal.
```

## Short Command

```text
/board [decision question]
```
