# EVAL_RESULTS.md — Quality Evaluation Status

## Status

This repository is at MVP stage (Version 001.0.0). No systematic, repeated evaluation of skill and agent outputs has been conducted yet.

## Planned Evaluation Criteria (for future versions)

1. **Disclaimer presence:** Does every output begin with the archetype disclaimer per `CLAUDE.md` §7?
2. **Archetype discipline:** Does the output strictly avoid attributing statements to named individuals as if real?
3. **Speculation labelling:** Are speculative options clearly marked as speculation, separated from robust findings?
4. **Methodology compliance:** Does the board session follow the 5-step process from `references/methodik-board.md`?
5. **Recommendation label:** Is every recommendation labelled as Act Now / Pilot / Investigate Further / Discard?
6. **Completeness of required sections:** Are all mandatory sections (Purpose, Inputs, Working Method, Output Format) present per `CLAUDE.md` §6?

## Next Steps

- Manual spot-checks of new and revised agents/skills before each release.
- Build a simple script-based completeness check (see `scripts/validate_yaml_frontmatter.py` and `scripts/validate_plugin_structure.py`) as the foundation for formal section-presence checks.
- As the skill set grows: build an LLM-based evaluation harness with a dedicated scoring rubric for archetype discipline and recommendation quality.
