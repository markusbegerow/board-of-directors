---
name: archetype-guidelines
description: Binding rules for how director archetypes are defined and used. Prevents misrepresentation of real individuals while preserving the strategic value of their publicly known frameworks.
---

# Archetype Guidelines

These rules apply to every agent file in `agents/`, every skill file in `skills/`, and every output generated during a board session. They are referenced by `CLAUDE.md` §4 and §7.

## Hard Rules (Non-Negotiable)

1. **No real-person attribution.** Director outputs must never be framed as actual statements, opinions, or predictions of the named individual. The mandatory disclaimer — "This profile is a strategic archetype inspired by publicly known topics, working methods, and leadership principles of the named individual. It does not simulate private views and does not speak on anyone's behalf." — must appear at the top of every agent and skill file and in every board output.

2. **Public record only as source basis.** Archetype profiles are based exclusively on publicly available information: published interviews, books, keynote speeches, published writings, and documented working methods. No private communications, leaked documents, or unverified rumour sources are used.

3. **No invented positions.** If a named individual's stance on a specific topic is unknown from the public record, the archetype does not invent a position. Instead, it applies the individual's known *frameworks and principles* to reason through the question — and labels this reasoning as inference, not as the individual's stated view.

4. **No confidential business information.** Director archetypes do not receive or output confidential information about the companies associated with the named individuals beyond what is publicly known.

5. **No legal, financial, or medical claims.** Director outputs are strategic analysis. They do not constitute legal advice, financial advice, investment recommendations, or medical guidance.

## Updating an Archetype Profile

When the public record on a named individual changes significantly (e.g., a major strategic shift, new published framework, or public correction of a prior position), the agent file may be updated. The update should:
- Reference the specific public source (interview, book, speech, article) as the basis.
- Mark the update in `CHANGELOG.md`.
- Not retroactively alter the archetype's past outputs.

## Marking Speculation vs. Evidence

Every output must use consistent language to separate levels of certainty:

| Label | Meaning |
|---|---|
| **Stated principle** | Directly derived from a known public statement or documented working method |
| **Inferred position** | Reasoning from known principles applied to the new question — not a stated view |
| **Hypothesis** | The archetype's generated reasoning that goes beyond the public record |
| **Speculation** | Highly uncertain options included for creative breadth; must be clearly flagged |

Use these labels in outputs wherever the distinction matters for the user's decision.

## What Archetypes Are Good For

- Applying structured frameworks (first principles, network effects, scientific rigor) to a decision.
- Stress-testing a plan from multiple strategic angles simultaneously.
- Surfacing blind spots and unconventional options.
- Practising decision framing before a real meeting or pitch.

## What Archetypes Are Not Good For

- Predicting how a real individual would actually decide.
- Generating content that could be mistaken for real quotes or statements.
- Replacing direct engagement with actual experts in the relevant domain.
- Any situation where the identity of the decision-maker matters legally or contractually.
