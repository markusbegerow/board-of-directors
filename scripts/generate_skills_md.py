#!/usr/bin/env python3
"""Regenerate SKILLS.md from the name/description frontmatter of every
canonical agent and skill file. Run after adding or renaming an agent or skill."""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install -r requirements.txt")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _content_trees import ROOT, canonical_agents, canonical_skills  # noqa: E402


def extract_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def first_sentence(text: str) -> str:
    return text.split(".")[0].strip() if text else ""


def main() -> int:
    agents = list(canonical_agents())
    skills = list(canonical_skills())

    lines = [
        "# SKILLS.md — Flat Index of All Agents and Skills",
        "",
        "Format: `<type>:<name>` — Description",
        "",
    ]

    if agents:
        lines.append("## Director Agents (`.claude/agents/`)")
        lines.append("")
        for name, agent_file in agents:
            data = extract_frontmatter(agent_file.read_text(encoding="utf-8"))
            description = first_sentence(str(data.get("description") or ""))
            lines.append(f"- `agent:{name}` — {description}")
        lines.append("")

    if skills:
        generic_skills = []
        persona_skills = []
        orchestrator = []

        for name, skill_file in skills:
            data = extract_frontmatter(skill_file.read_text(encoding="utf-8"))
            description = first_sentence(str(data.get("description") or ""))
            entry = f"- `skill:{name}` — {description}"
            if name == "board":
                orchestrator.append(entry)
            elif name.endswith("-skills"):
                persona_skills.append(entry)
            else:
                generic_skills.append(entry)

        if orchestrator or generic_skills:
            lines.append("## Generic Methodology Skills (`.claude/skills/`)")
            lines.append("")
            for entry in orchestrator + generic_skills:
                lines.append(entry)
            lines.append("")

        if persona_skills:
            lines.append("## Director Persona Invocation Shortcuts (`.claude/skills/`)")
            lines.append("")
            for entry in persona_skills:
                lines.append(entry)
            lines.append("")

    output_path = ROOT / "SKILLS.md"
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"SKILLS.md updated ({output_path}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
