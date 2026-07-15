# Quickstart (2 minutes)

1. Open this repository in Claude Code (select the folder as your project directory), or install it via the Claude Code Plugin Marketplace: `/plugin marketplace add markusbegerow/board-of-directors` then `/plugin install board-of-directors@board-of-directors` (see `INSTALLATION.md` Option C).
2. If you opened the folder directly, `CLAUDE.md` loads automatically. If you installed via the marketplace, the plugin's `.claude-plugin/marketplace.json` entry is what Claude Code detects.
3. Invoke the board orchestrator: `/board [your decision question]` (project directory) or `/board-of-directors:board [your decision question]` (marketplace install).
4. Or invoke a single director directly:
   - `Use the elon-musk agent and evaluate: [question]`
   - `Use the sam-altman agent and evaluate: [question]`
5. Receive structured output — always with the archetype disclaimer and clearly labelled recommendations.

## Before Your First Use

- Read `CLAUDE.md` and `AGENTS.md` once — they define how outputs are structured and what disclaimers must be present.
- Do not input real client data, confidential business details, or personal information.
- All outputs are analytical work aids — not professional management consulting, not legal or financial advice.

## Typical Session

```text
/board [decision question]
```

The orchestrator:
1. Selects 3–5 directors based on the decision type.
2. Collects independent votes from each director.
3. Surfaces conflicts and consensus.
4. Synthesises an integrated, prioritised decision proposal.

## Individual Director Shortcut

```text
Use the `elon-musk` agent and evaluate:
[question]
```

## Available Generic Skills

- `/analyze` — decompose the problem into sub-problems and classify assumptions
- `/brainstorm` — generate a wide option space across conventional, adjacent, and radical tiers
- `/decision-matrix` — score options across weighted criteria
- `/risk-assess` — enumerate risks by likelihood × impact
- `/synthesize` — merge multiple perspectives into an integrated recommendation
- `/report` — format findings into a clean, executive-ready output

Full installation guide for beginners: `INSTALLATION.md`.
