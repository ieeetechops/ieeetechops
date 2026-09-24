#!/usr/bin/env python3
"""Validate the repository's local Markdown links and documentation structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"

REQUIRED_PATHS = (
    ROOT / "README.md",
    ROOT / "ROADMAP.md",
    ROOT / "PROJECTS.md",
    ROOT / "STATUS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "GOVERNANCE.md",
    ROOT / "mkdocs.yml",
    DOCS_DIR / "index.md",
)

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MKDOCS_NAV_ITEM = re.compile(r"^\s*-\s+.+:\s+([^#]+\.md)\s*$")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not {".git", ".venv", "site", "__pycache__"}.intersection(path.parts)
    )


def clean_link(raw_target: str) -> str:
    target = raw_target.strip().strip("<>")
    if " " in target and not target.startswith(EXTERNAL_PREFIXES):
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def check_local_links(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for source in files:
        text = source.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw_target = match.group(1).strip()
            if not raw_target or raw_target.startswith("#"):
                continue
            if raw_target.startswith(EXTERNAL_PREFIXES):
                continue

            target = clean_link(raw_target)
            if not target:
                continue

            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                relative_source = source.relative_to(ROOT)
                errors.append(f"{relative_source}: broken local link -> {raw_target}")
    return errors


def check_mkdocs_nav() -> list[str]:
    errors: list[str] = []
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    for line_number, line in enumerate(config.splitlines(), start=1):
        match = MKDOCS_NAV_ITEM.match(line)
        if not match:
            continue
        target = DOCS_DIR / match.group(1).strip().strip('"\'')
        if not target.exists():
            errors.append(
                f"mkdocs.yml:{line_number}: nav target does not exist -> "
                f"{target.relative_to(ROOT)}"
            )
    return errors


def check_required_paths() -> list[str]:
    return [
        f"required path is missing -> {path.relative_to(ROOT)}"
        for path in REQUIRED_PATHS
        if not path.exists()
    ]


def main() -> int:
    files = markdown_files()
    errors = check_required_paths()
    errors.extend(check_local_links(files))
    errors.extend(check_mkdocs_nav())

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation checks passed ({len(files)} Markdown files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
