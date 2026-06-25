#!/usr/bin/env python3
"""Validate that the board-of-directors plugin is correctly structured.

Checks:
- .claude-plugin/marketplace.json exists and is valid JSON
- .claude-plugin/plugin.json exists and contains required fields
- agents/ and skills/ directories exist and are non-empty
- every file listed in marketplace plugins has a resolvable source directory
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_PLUGIN_FIELDS = ["name", "version", "description", "license", "author"]


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
        if not agents_dir.is_dir() or not any(agents_dir.glob("*.md")):
            errors.append(f"{plugin_dir}: 'agents/' directory missing or contains no .md files")

        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir() or not any(skills_dir.glob("*.md")):
            errors.append(f"{plugin_dir}: 'skills/' directory missing or contains no .md files")

    if errors:
        print(f"{len(errors)} error(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(plugins)} plugin(s) correctly structured.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
