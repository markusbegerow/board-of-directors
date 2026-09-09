#!/usr/bin/env python3
"""Generate mirror copies of canonical agent/skill content for Codex CLI,
OpenCode, and the Claude Code marketplace plugin.

Canonical (hand-edited) source:
    .claude/agents/<name>.md
    .claude/skills/<name>/SKILL.md

Generated mirrors (never hand-edit these -- this script owns them):
    .agents/skills/<name>/SKILL.md               (Codex CLI native path; extra OpenCode coverage)
    board-of-directors/skills/<name>/SKILL.md    (marketplace plugin + ECC harness)
    board-of-directors/agents/<name>/AGENT.md    (marketplace plugin)

Usage:
    python scripts/sync_content_trees.py          # write/update/remove mirrors
    python scripts/sync_content_trees.py --check  # dry run; exit 1 if anything is out of sync
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _content_trees import (  # noqa: E402
    iter_mirror_pairs,
    iter_existing_agent_mirrors,
    iter_existing_skill_mirrors,
    ROOT,
)


def main() -> int:
    check_only = "--check" in sys.argv[1:]

    created, updated, unchanged, removed = [], [], [], []
    valid_mirrors = set()

    for canonical, mirror in iter_mirror_pairs():
        valid_mirrors.add(mirror)
        canonical_text = canonical.read_text(encoding="utf-8")
        if mirror.exists():
            if mirror.read_text(encoding="utf-8") == canonical_text:
                unchanged.append(mirror)
                continue
            updated.append(mirror)
        else:
            created.append(mirror)
        if not check_only:
            mirror.parent.mkdir(parents=True, exist_ok=True)
            mirror.write_text(canonical_text, encoding="utf-8")

    # Orphan cleanup: mirror files whose canonical source no longer exists.
    for existing in list(iter_existing_skill_mirrors()) + list(iter_existing_agent_mirrors()):
        if existing not in valid_mirrors:
            removed.append(existing)
            if not check_only:
                existing.unlink()
                try:
                    existing.parent.rmdir()
                except OSError:
                    pass

    print(f"created={len(created)} updated={len(updated)} unchanged={len(unchanged)} removed={len(removed)}")
    for label, items in (("created", created), ("updated", updated), ("removed", removed)):
        for item in items:
            print(f"  {label}: {item.relative_to(ROOT)}")

    if check_only and (created or updated or removed):
        print("Drift detected. Run `python scripts/sync_content_trees.py` to fix.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
