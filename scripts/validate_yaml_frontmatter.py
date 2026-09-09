#!/usr/bin/env python3
"""Validate that every agent and skill file has well-formed YAML frontmatter.

Checks performed for each .claude/agents/<name>.md, .claude/skills/<name>/SKILL.md,
and .agents/skills/<name>/SKILL.md file:
- starts with '---' frontmatter block containing 'name' and 'description'
- name is kebab-case, <= 64 ASCII characters, matches the expected name
  (the filename without .md for flat agent files, the parent directory name
  for nested SKILL.md files)
- description is a non-empty string, <= 1024 characters
- no unexpected frontmatter-only fields (tools: is allowed for agent files)

`.opencode/agent/*.md` and `.opencode/command/*.md` use OpenCode's own
frontmatter schema (`mode`, `agent`) and are intentionally out of scope here.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install -r requirements.txt")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
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
    """Return (path, expected_name) pairs for .claude/agents, .claude/skills, .agents/skills."""
    files = []

    agents_dir = ROOT / ".claude" / "agents"
    if agents_dir.is_dir():
        for md_file in sorted(agents_dir.glob("*.md")):
            files.append((md_file, md_file.stem))

    for skills_dir in (ROOT / ".claude" / "skills", ROOT / ".agents" / "skills"):
        if skills_dir.is_dir():
            for md_file in sorted(skills_dir.glob("*/SKILL.md")):
                files.append((md_file, md_file.parent.name))

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
