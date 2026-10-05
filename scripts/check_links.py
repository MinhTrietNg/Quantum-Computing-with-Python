"""Check relative links, images and heading anchors in the repo's Markdown files.

Links to other sites are not fetched; only links that point inside the repo
are verified. Markdown links and images (``[text](path)``, ``![alt](path)``)
and HTML ``<a href="...">`` / ``<img src="...">`` tags are checked. A link
fails when its target file does not exist, when the letter case differs from
the real file name (GitHub is case-sensitive even where Windows and macOS are
not), when it points outside the repo, or when it carries a ``#fragment``
that matches no heading in the target Markdown file. Anchors follow GitHub's
slug rules (lowercase, punctuation dropped, spaces become hyphens, repeated
headings get ``-1``, ``-2``, ...); ``<a id>`` / ``<a name>`` tags count too.

Usage
-----
    python scripts/check_links.py

Exits with status 1 when any link is broken, so it can be used in CI.
"""

from __future__ import annotations

import os
import re
import sys
import unicodedata
import urllib.parse
from collections.abc import Iterator
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    ".ipynb_checkpoints",
    ".pytest_cache",
    ".ruff_cache",
}

FENCE = re.compile(
    r"^[ \t]*(?P<fence>`{3,}|~{3,})[^\n]*\n.*?^[ \t]*(?P=fence)[ \t]*$",
    re.DOTALL | re.MULTILINE,
)
INLINE_CODE = re.compile(r"`[^`\n]*`")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
HEADING = re.compile(r"^ {0,3}#{1,6}[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*$", re.MULTILINE)
# Link text may hold one level of brackets, e.g. a badge image inside a link.
LINK = re.compile(
    r"!?\[(?P<text>(?:[^\[\]]|\[[^\[\]]*\])*)\]"
    r"\(\s*(?P<url><[^>\n]*>|[^)\s]+)(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
HTML_LINK = re.compile(
    r"<(?:a|img)\b[^>]*?\s(?:href|src)\s*=\s*"
    r"(?:\"(?P<dq>[^\"]*)\"|'(?P<sq>[^']*)'|(?P<bare>[^\s\"'>]+))",
    re.IGNORECASE,
)
HTML_ANCHOR = re.compile(
    r"<a\b[^>]*?\s(?:id|name)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE
)
HTML_TAG = re.compile(r"</?[A-Za-z][^>]*>")
HAS_SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def strip_code(text: str) -> str:
    """Remove fenced code blocks, inline code spans and HTML comments."""
    return INLINE_CODE.sub("", FENCE.sub("", HTML_COMMENT.sub("", text)))


def is_slug_char(ch: str) -> bool:
    """Return True if GitHub keeps ``ch`` in an anchor (its ``\\p{Word}``, -, space)."""
    category = unicodedata.category(ch)
    return ch in "- " or category[0] in "LMN" or category == "Pc"


def slugify(heading: str) -> str:
    """Convert a heading to its GitHub anchor (before duplicate numbering).

    GitHub slugs the heading's rendered text: link text is kept, images and
    HTML tags contribute nothing, and every character other than Unicode
    letters, marks, numbers, connector punctuation (``_``), ``-`` and spaces
    is dropped. Vietnamese and other non-ASCII letters are kept.
    """
    heading = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", heading)  # images have no text
    heading = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # keep link text
    heading = HTML_TAG.sub("", heading)
    slug = "".join(ch for ch in heading.strip().lower() if is_slug_char(ch))
    return slug.replace(" ", "-")


def anchors(markdown: str) -> set[str]:
    """Return every anchor GitHub generates for the headings in ``markdown``."""
    text = HTML_COMMENT.sub("", FENCE.sub("", markdown))
    seen: dict[str, int] = {}
    found: set[str] = set(HTML_ANCHOR.findall(INLINE_CODE.sub("", text)))
    for match in HEADING.finditer(text):
        slug = slugify(match.group(1))
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        found.add(slug if count == 0 else f"{slug}-{count}")
    return found


def iter_links(text: str) -> Iterator[str]:
    """Yield the URL of every Markdown or HTML link and image in ``text``.

    ``text`` must already be stripped of code. Links nested in the text of
    another link, such as a badge image wrapped in a link, are included.
    """
    for match in LINK.finditer(text):
        yield match.group("url").strip("<>")
        yield from iter_links(match.group("text"))
    for match in HTML_LINK.finditer(text):
        yield match.group("dq") or match.group("sq") or match.group("bare") or ""


def markdown_files(root: Path) -> list[Path]:
    """List the Markdown files under ``root``, skipping tool directories."""
    return sorted(p for p in root.rglob("*.md") if not SKIP_DIRS.intersection(p.parts))


def exists_exact(target: Path, root: Path, listings: dict[Path, set[str]]) -> bool:
    """Return True if ``target`` exists with exactly this letter case.

    Each path component below ``root`` is compared with the real directory
    listing, because ``Path.exists`` ignores case on Windows and macOS.
    """
    current = root
    for part in target.relative_to(root).parts:
        if current not in listings:
            listings[current] = set(os.listdir(current)) if current.is_dir() else set()
        if part not in listings[current]:
            return False
        current = current / part
    return True


def check_file(
    path: Path,
    root: Path,
    cache: dict[Path, set[str]],
    listings: dict[Path, set[str]] | None = None,
) -> list[str]:
    """Return one error message per broken link in ``path``."""
    listings = {} if listings is None else listings
    errors: list[str] = []
    text = strip_code(path.read_text(encoding="utf-8"))
    for url in iter_links(text):
        if not url or HAS_SCHEME.match(url) or url.startswith("//"):
            continue
        parts = urllib.parse.urlsplit(url)
        target_part, fragment = urllib.parse.unquote(parts.path), parts.fragment
        shown = f"{path.relative_to(root).as_posix()}: {url}"
        if not target_part:
            target = path
        else:
            # GitHub resolves "/path" from the repo root, like Markdown viewers.
            base = root if target_part.startswith("/") else path.parent
            target = Path(os.path.normpath(base / target_part.lstrip("/")))
        try:
            target.relative_to(root)
        except ValueError:
            errors.append(f"outside repo   {shown}")
            continue
        if not exists_exact(target, root, listings):
            kind = "wrong case    " if target.exists() else "missing file  "
            errors.append(f"{kind} {shown}")
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
    listings: dict[Path, set[str]] = {}
    errors = [e for f in files for e in check_file(f, REPO_ROOT, cache, listings)]
    for error in errors:
        print(error)
    print(f"Checked {len(files)} Markdown files: {len(errors)} broken link(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
