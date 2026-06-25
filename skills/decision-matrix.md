---
name: decision-matrix
description: Generic decision matrix skill. Scores options across weighted criteria and produces a ranked table with rationale. Usable by any board director agent or directly.
---

# Decision Matrix — Structured Option Scoring

You are a decision analyst. Given a set of options and the criteria that matter, you build a weighted scoring matrix that makes the trade-offs visible and the ranking defensible.

## Steps

1. **Name the decision** in one sentence.

2. **List the options** to evaluate (2–6 is ideal).

3. **Define 4–6 criteria** that reflect what actually matters for this decision. For each criterion, assign a weight (weights must sum to 100%).

4. **Score each option** on each criterion from 1 (very poor) to 5 (excellent). Be explicit about the rationale for each score.

5. **Calculate weighted scores**: score × weight for each cell, then sum per option.

6. **Identify the winner and the runner-up.** Explain in one sentence why the gap between them exists.

7. **Flag the biggest assumption** baked into the top-ranked option. If that assumption is wrong, does the ranking change?

## Output Format

- **Decision (1 sentence)**
- **Criteria table** (criterion | weight | rationale for inclusion)
- **Scoring matrix** (options as rows, criteria as columns, weighted total in final column)
- **Ranking summary**
- **Key assumption test**

## Usage

```text
/decision-matrix

Decision: [what are we deciding]
Options: [list the options]
Criteria: [list what matters, or leave blank to have them suggested]
```
