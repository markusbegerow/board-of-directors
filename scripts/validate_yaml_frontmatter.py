#!/usr/bin/env python3
"""Validate that every agent and skill file has well-formed YAML frontmatter.

Checks performed for each canonical .claude/agents/<name>.md,
.claude/skills/<name>/SKILL.md file and every generated mirror
(.agents/skills/<name>/SKILL.md, board-of-directors/agents/<name>/AGENT.md,
board-of-directors/skills/<name>/SKILL.md -- see scripts/_content_trees.py):
- starts with '---' frontmatter block containing 'name' and 'description'
- name is kebab-case, <= 64 ASCII characters, matches the expected name
  (the filename without .md for flat files, the parent directory name for
  nested AGENT.md/SKILL.md files)
- description is a non-empty string, <= 1024 characters
- no unexpected frontmatter-only fields (tools: is allowed for agent files)
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install -r requirements.txt")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _content_trees import (  # noqa: E402
    canonical_agents,
    canonical_skills,
    iter_existing_agent_mirrors,
    iter_existing_skill_mirrors,
)

KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ALLOWED_FIELDS = {"name", "description", "tools"}


def extract_frontmatter(text: str):
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def validate_file(md_file: Path, expected_name: str, errors: list) -> None:
    text = md_file.read_text(encoding="utf-8")
    raw_frontmatter = extract_frontmatter(text)
    if raw_frontmatter is None:
        errors.append(f"{md_file}: no YAML frontmatter found")
        return
    try:
        data = yaml.safe_load(raw_frontmatter) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{md_file}: invalid YAML ({exc})")
        return

    name = data.get("name")
    description = data.get("description")

    if not name:
        errors.append(f"{md_file}: field 'name' missing")
    elif name != expected_name:
        errors.append(
            f"{md_file}: 'name' ({name!r}) does not match expected name ({expected_name!r})"
        )
    elif not KEBAB_RE.match(name) or len(name) > 64:
        errors.append(f"{md_file}: 'name' is not valid kebab-case (max 64 characters)")

    if not description:
        errors.append(f"{md_file}: field 'description' missing")
    elif len(str(description)) > 1024:
        errors.append(f"{md_file}: 'description' exceeds 1024 characters")

    unknown_fields = set(data.keys()) - ALLOWED_FIELDS
    if unknown_fields:
        errors.append(f"{md_file}: unexpected frontmatter fields: {sorted(unknown_fields)}")


def collect_files() -> list:
    """Return (path, expected_name) pairs for the canonical source and every generated mirror."""
    files = []

    for name, path in canonical_agents():
        files.append((path, name))
    for name, path in canonical_skills():
        files.append((path, name))

    for path in iter_existing_agent_mirrors():
        files.append((path, path.parent.name))
    for path in iter_existing_skill_mirrors():
        files.append((path, path.parent.name))

    return files


def main() -> int:
    errors = []
    all_files = collect_files()

    if not all_files:
        print("No agent or skill .md files found.")
        return 1

    for md_file, expected_name in all_files:
        validate_file(md_file, expected_name, errors)

    if errors:
        print(f"{len(errors)} error(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(all_files)} file(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
