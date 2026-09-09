"""Canonical-source -> generated-mirror path mapping for Board of Directors content.

Shared by sync_content_trees.py, validate_plugin_structure.py, validate_yaml_frontmatter.py,
and generate_skills_md.py so the list of mirror destinations lives in exactly one place.

Canonical (hand-edited) source:
    .claude/agents/<name>.md          -- Claude Code project subagent (also the only
                                          copy Claude Code and OpenCode need natively)
    .claude/skills/<name>/SKILL.md    -- Claude Code / OpenCode project skill

Generated mirrors (never hand-edited -- owned by scripts/sync_content_trees.py):
    .agents/skills/<name>/SKILL.md            -- Codex CLI's native skills path
                                                  (also a second OpenCode discovery path)
    board-of-directors/skills/<name>/SKILL.md -- Claude Code marketplace plugin + ECC harness
    board-of-directors/agents/<name>/AGENT.md -- Claude Code marketplace plugin
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CANONICAL_AGENTS_DIR = ROOT / ".claude" / "agents"
CANONICAL_SKILLS_DIR = ROOT / ".claude" / "skills"

PLUGIN_DIR = ROOT / "board-of-directors"

SKILL_MIRROR_ROOTS = [ROOT / ".agents" / "skills", PLUGIN_DIR / "skills"]
AGENT_MIRROR_ROOTS = [PLUGIN_DIR / "agents"]


def canonical_agents():
    """Yield (name, path) for every canonical agent file."""
    if not CANONICAL_AGENTS_DIR.is_dir():
        return
    for md_file in sorted(CANONICAL_AGENTS_DIR.glob("*.md")):
        yield md_file.stem, md_file


def canonical_skills():
    """Yield (name, path) for every canonical skill file."""
    if not CANONICAL_SKILLS_DIR.is_dir():
        return
    for md_file in sorted(CANONICAL_SKILLS_DIR.glob("*/SKILL.md")):
        yield md_file.parent.name, md_file


def agent_mirrors(name: str):
    """Return every mirror path a canonical agent file must be copied to."""
    return [root / name / "AGENT.md" for root in AGENT_MIRROR_ROOTS]


def skill_mirrors(name: str):
    """Return every mirror path a canonical skill file must be copied to."""
    return [root / name / "SKILL.md" for root in SKILL_MIRROR_ROOTS]


def iter_mirror_pairs():
    """Yield (canonical_path, mirror_path) for every required mirror."""
    for name, canonical in canonical_agents():
        for mirror in agent_mirrors(name):
            yield canonical, mirror
    for name, canonical in canonical_skills():
        for mirror in skill_mirrors(name):
            yield canonical, mirror


def iter_existing_skill_mirrors():
    """Yield every SKILL.md that currently exists under a skill mirror root."""
    for root in SKILL_MIRROR_ROOTS:
        if root.is_dir():
            yield from sorted(root.glob("*/SKILL.md"))


def iter_existing_agent_mirrors():
    """Yield every AGENT.md that currently exists under an agent mirror root."""
    for root in AGENT_MIRROR_ROOTS:
        if root.is_dir():
            yield from sorted(root.glob("*/AGENT.md"))
