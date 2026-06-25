#!/usr/bin/env python3
"""Validate that every agent and skill file has well-formed YAML frontmatter.

Checks performed for each agents/<name>.md and skills/<name>.md:
- starts with '---' frontmatter block containing 'name' and 'description'
- name is kebab-case, <= 64 ASCII characters, matches the filename (without .md)
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


def validate_file(md_file: Path, errors: list) -> None:
    filename_stem = md_file.stem
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
    elif name != filename_stem:
        errors.append(
            f"{md_file}: 'name' ({name!r}) does not match filename ({filename_stem!r})"
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


def main() -> int:
    errors = []
    agent_files = sorted((ROOT / "agents").glob("*.md")) if (ROOT / "agents").is_dir() else []
    skill_files = sorted((ROOT / "skills").glob("*.md")) if (ROOT / "skills").is_dir() else []
    all_files = agent_files + skill_files

    if not all_files:
        print("No agent or skill .md files found.")
        return 1

    for md_file in all_files:
        validate_file(md_file, errors)

    if errors:
        print(f"{len(errors)} error(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(all_files)} file(s) valid ({len(agent_files)} agents, {len(skill_files)} skills).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
