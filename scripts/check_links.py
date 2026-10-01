"""Check relative links and heading anchors in the repo's Markdown files.

Links to other sites are not fetched; only links that point inside the repo
are verified. A link fails when its target file does not exist, or when it
carries a ``#fragment`` that matches no heading in the target Markdown file.
Anchors follow GitHub's slug rules (lowercase, punctuation dropped, spaces
become hyphens, repeated headings get ``-1``, ``-2``, ...).

Usage
-----
    python scripts/check_links.py

Exits with status 1 when any link is broken, so it can be used in CI.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", ".ipynb_checkpoints"}

FENCE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.DOTALL | re.MULTILINE)
INLINE_CODE = re.compile(r"`[^`\n]*`")
HEADING = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HAS_SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans from Markdown."""
    return INLINE_CODE.sub("", FENCE.sub("", text))


def slugify(heading: str) -> str:
    """Convert a heading to its GitHub anchor (before duplicate numbering)."""
    heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # keep link text
    heading = re.sub(r"[`*_~]", lambda m: "_" if m.group() == "_" else "", heading)
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


def anchors(markdown: str) -> set[str]:
    """Return every anchor GitHub generates for the headings in ``markdown``."""
    seen: dict[str, int] = {}
    found: set[str] = set()
    for match in HEADING.finditer(FENCE.sub("", markdown)):
        slug = slugify(match.group(1))
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        found.add(slug if count == 0 else f"{slug}-{count}")
    return found


def markdown_files(root: Path) -> list[Path]:
    """List the Markdown files under ``root``, skipping tool directories."""
    return sorted(p for p in root.rglob("*.md") if not SKIP_DIRS.intersection(p.parts))


def check_file(path: Path, root: Path, cache: dict[Path, set[str]]) -> list[str]:
    """Return one error message per broken link in ``path``."""
    errors: list[str] = []
    text = strip_code(path.read_text(encoding="utf-8"))
    for match in LINK.finditer(text):
        url = match.group(1)
        if HAS_SCHEME.match(url):
            continue
        target_part, _, fragment = url.partition("#")
        target = (
            (path.parent / urllib.parse.unquote(target_part)).resolve()
            if target_part
            else path
        )
        shown = f"{path.relative_to(root)}: {url}"
        if not target.exists():
            errors.append(f"missing file   {shown}")
        elif fragment and target.suffix == ".md":
            if target not in cache:
                cache[target] = anchors(target.read_text(encoding="utf-8"))
            if urllib.parse.unquote(fragment) not in cache[target]:
                errors.append(f"missing anchor {shown}")
    return errors


def main() -> int:
    """Check every Markdown file and return the process exit code."""
    files = markdown_files(REPO_ROOT)
    cache: dict[Path, set[str]] = {}
    errors = [e for f in files for e in check_file(f, REPO_ROOT, cache)]
    for error in errors:
        print(error)
    print(f"Checked {len(files)} Markdown files: {len(errors)} broken link(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
