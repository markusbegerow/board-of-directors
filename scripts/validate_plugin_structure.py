#!/usr/bin/env python3
"""Validate that the board-of-directors plugin is correctly structured.

Checks:
- .claude-plugin/marketplace.json exists and is valid JSON
- .claude-plugin/plugin.json exists and contains required fields
- agents/<name>/AGENT.md and skills/<name>/SKILL.md exist and are non-empty
- every file listed in marketplace plugins has a resolvable source directory
- if a legacy flat tree (ROOT/agents/*.md, ROOT/skills/*.md) also exists,
  its content stays byte-identical to the corresponding nested plugin file
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_PLUGIN_FIELDS = ["name", "version", "description", "license", "author"]


def check_legacy_tree_sync(plugin_dir: Path, errors: list) -> None:
    """If a legacy flat tree exists alongside the nested plugin tree, they must match.

    board-of-directors keeps ROOT/agents/<name>.md + ROOT/skills/<name>.md around
    for the "open as project directory" CLAUDE.md workflow, alongside the nested
    agents/<name>/AGENT.md + skills/<name>/SKILL.md that the plugin actually ships.
    Nothing else enforces these stay identical, so drift would go unnoticed.
    """
    if plugin_dir == ROOT:
        return

    for kind, nested_filename in (("agents", "AGENT.md"), ("skills", "SKILL.md")):
        legacy_dir = ROOT / kind
        if not legacy_dir.is_dir():
            continue
        for legacy_file in sorted(legacy_dir.glob("*.md")):
            nested_file = plugin_dir / kind / legacy_file.stem / nested_filename
            if not nested_file.exists():
                errors.append(f"{legacy_file}: no matching nested file at {nested_file}")
                continue
            if legacy_file.read_text(encoding="utf-8") != nested_file.read_text(encoding="utf-8"):
                errors.append(f"{legacy_file} and {nested_file} have drifted out of sync")


def main() -> int:
    errors = []

    manifest_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not manifest_path.exists():
        print(f"marketplace.json not found: {manifest_path}")
        return 1

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"marketplace.json is not valid JSON: {exc}")
        return 1

    plugins = manifest.get("plugins", [])
    if not plugins:
        errors.append("marketplace.json contains no plugins")

    for plugin_entry in plugins:
        source = plugin_entry.get("source", "")
        plugin_dir = (ROOT / source).resolve() if source else None

        if plugin_dir is None or not plugin_dir.is_dir():
            errors.append(f"Plugin source directory not found for source={source!r}")
            continue

        plugin_json_path = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json_path.exists():
            errors.append(f"{plugin_dir}: .claude-plugin/plugin.json missing")
        else:
            try:
                plugin_data = json.loads(plugin_json_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{plugin_json_path}: invalid JSON ({exc})")
                plugin_data = {}
            for field in REQUIRED_PLUGIN_FIELDS:
                if field not in plugin_data:
                    errors.append(f"{plugin_json_path}: required field '{field}' missing")

        agents_dir = plugin_dir / "agents"
        if not agents_dir.is_dir() or not any(agents_dir.glob("*/AGENT.md")):
            errors.append(f"{plugin_dir}: 'agents/' directory missing or contains no <name>/AGENT.md files")

        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir() or not any(skills_dir.glob("*/SKILL.md")):
            errors.append(f"{plugin_dir}: 'skills/' directory missing or contains no <name>/SKILL.md files")

        check_legacy_tree_sync(plugin_dir, errors)

    if errors:
        print(f"{len(errors)} error(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(plugins)} plugin(s) correctly structured.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
