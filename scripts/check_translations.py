"""Check that the English and Chinese guides mirror the Vietnamese originals.

Every Vietnamese Markdown guide (``README.md``, ``CONTRIBUTING.md``,
``ERRATA.md``, ``docs/*.md`` and ``chapters/*/README.md``) must have two
translations next to it: ``<name>.en.md`` and ``<name>.zh-CN.md``. A
translation may reword and merge sentences freely, but it must not drop or
change the parts that carry facts. The script compares the "skeleton" of each
translation with its original:

* the sequence of heading levels;
* the formulas (``$...$`` and ``$$...$$``), ignoring the words in ``\\text{}``;
* the fenced code blocks, ignoring comments (comments are translated); a block
  right after a ``<!-- translate-block -->`` line may be translated entirely;
* the images, in order;
* the link targets (anchors and language suffixes are ignored);
* per section: table rows, list items, fenced blocks, images, display
  formulas and blockquote blocks;
* one language-switcher line near the top of every file.

Usage
-----
    python scripts/check_translations.py
    python scripts/check_translations.py chapters/02_quantum_computing/README.md

Exits with status 1 when a translation is missing or differs, so it can be
used in CI.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("en", "zh-CN")
TRANSLATION_SUFFIXES = tuple(f".{lang}.md" for lang in LANGUAGES)
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", ".github"}

FENCE = re.compile(r"^([ \t]*)(```|~~~)([^\n]*)\n(.*?)^\1\2[ \t]*$", re.DOTALL | re.M)
DISPLAY_MATH = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
INLINE_MATH = re.compile(r"(?<![\\$])\$(?!\$)([^$\n]+?)(?<!\\)\$")
TEXT_COMMAND = re.compile(r"\\(?:text|mathrm|textbf|mbox)\{[^{}]*\}")
HEADING = re.compile(r"^(#{1,6})[ \t]+\S", re.M)
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)|<img\b[^>]*?\bsrc=[\"']([^\"']+)", re.I)
LINK = re.compile(
    r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|<a\b[^>]*?\bhref=[\"']([^\"']+)", re.I
)
LIST_ITEM = re.compile(r"^[ \t]*(?:[-*+]|\d+[.)])[ \t]+\S", re.M)
TABLE_SEPARATOR = re.compile(
    r"^[ \t]*\|?[ \t]*:?-{3,}:?[ \t]*(\|[ \t]*:?-{3,}:?[ \t]*)*\|?[ \t]*$"
)
SWITCHER = re.compile(
    r"^(?P<vi>\*\*Tiếng Việt\*\*|\[Tiếng Việt\]\([^)]+\))"
    r" · (?P<en>\*\*English\*\*|\[English\]\([^)]+\))"
    r" · (?P<zh>\*\*简体中文\*\*|\[简体中文\]\([^)]+\))[ 	]*$"
)
COMMENT_LANGS = {"", "python", "py", "bash", "sh", "shell", "powershell", "text"}
FREE_TEXT_LANGS = {"markdown", "md"}
# A fenced block right after this comment holds prose (a diagram with labels) that
# translations may translate; all other blocks must match the original exactly.
TRANSLATE_MARKER = "<!-- translate-block -->"


@dataclass
class Section:
    """Counts of the structural elements inside one heading section."""

    tables: list[int] = field(default_factory=list)
    list_items: int = 0
    fences: int = 0
    images: int = 0
    display_math: int = 0
    quotes: int = 0

    def key(self) -> tuple:
        """Return the comparable form of this section."""
        return (
            tuple(self.tables),
            self.list_items,
            self.fences,
            self.images,
            self.display_math,
            self.quotes,
        )


@dataclass
class Skeleton:
    """The comparable structure of one Markdown file."""

    headings: list[int] = field(default_factory=list)
    math: Counter = field(default_factory=Counter)
    code: list[tuple[str, str]] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    links: Counter = field(default_factory=Counter)
    raw_links: list[str] = field(default_factory=list)
    sections: list[tuple] = field(default_factory=list)
    switchers: int = 0


def original_guides(root: Path) -> list[Path]:
    """List the Vietnamese guides: every Markdown file that is not a translation."""
    found = []
    for path in sorted(root.rglob("*.md")):
        parts = set(path.relative_to(root).parts)
        if SKIP_DIRS & parts or path.name.endswith(TRANSLATION_SUFFIXES):
            continue
        found.append(path)
    return found


def translation_path(original: Path, lang: str) -> Path:
    """Return where the ``lang`` translation of ``original`` must live."""
    return original.with_name(f"{original.stem}.{lang}.md")


def strip_comments(code: str, lang: str) -> str:
    """Drop comments and whitespace so translated comments do not matter."""
    if lang not in COMMENT_LANGS:
        return re.sub(r"\s+", "", code)
    lines = []
    for line in code.splitlines():
        line = re.sub(r"(^|\s)#.*$", "", line)
        if line.strip():
            lines.append(re.sub(r"\s+", "", line))
    return "".join(lines)


def normalize_link(target: str) -> str:
    """Make a link comparable across languages: no anchor, no language suffix."""
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        return target
    path = target.split("#", 1)[0]
    for lang in LANGUAGES:
        path = path.replace(f".{lang}.md", ".md")
    return path or "#"


def normalize_math(expr: str) -> str:
    """Remove prose inside ``\\text{}`` and all whitespace from a formula."""
    return re.sub(r"\s+", "", TEXT_COMMAND.sub(r"\\text{}", expr))


def table_shapes(lines: list[str]) -> list[int]:
    """Return the number of rows of each table found in ``lines``."""
    shapes = []
    i = 0
    while i < len(lines):
        is_header = lines[i].lstrip().startswith("|")
        if is_header and i + 1 < len(lines) and TABLE_SEPARATOR.match(lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            shapes.append(j - i - 2)
            i = j
        else:
            i += 1
    return shapes


def blockquote_blocks(lines: list[str]) -> int:
    """Count runs of consecutive blockquote lines."""
    blocks, inside = 0, False
    for line in lines:
        starts = line.lstrip().startswith(">")
        blocks += starts and not inside
        inside = starts
    return blocks


def skeleton(text: str) -> Skeleton:
    """Extract the comparable structure of Markdown ``text``."""
    sk = Skeleton()
    for line in text.splitlines()[:8]:
        if SWITCHER.search(line):
            sk.switchers += 1
    text = "\n".join(line for line in text.splitlines() if not SWITCHER.search(line))
    fences: list[tuple[int, str]] = []
    for match in FENCE.finditer(text):
        lang = match.group(3).strip().split()[0] if match.group(3).strip() else ""
        translatable = text[: match.start()].rstrip().endswith(TRANSLATE_MARKER)
        free = lang in FREE_TEXT_LANGS or translatable
        body = "" if free else strip_comments(match.group(4), lang)
        sk.code.append((lang, body))
        fences.append((match.start(), lang))
    prose = FENCE.sub(lambda m: "\n" * m.group().count("\n"), text)

    for expr in DISPLAY_MATH.findall(prose):
        sk.math[normalize_math(expr)] += 1
    inline = DISPLAY_MATH.sub("", prose)
    for expr in INLINE_MATH.findall(inline):
        sk.math[normalize_math(expr)] += 1
    sk.images = [a or b for a, b in IMAGE.findall(prose)]
    for a, b in LINK.findall(prose):
        sk.links[normalize_link(a or b)] += 1
        sk.raw_links.append(a or b)

    # Split into sections at every heading; section 0 is the text before the first.
    lines = prose.splitlines()
    bounds = [i for i, line in enumerate(lines) if HEADING.match(line)]
    sk.headings = [len(HEADING.match(lines[i]).group(1)) for i in bounds]
    starts = [0, *bounds]
    ends = [*bounds, len(lines)]
    fence_starts = [text.count("\n", 0, pos) for pos, _ in fences]
    for start, end in zip(starts, ends, strict=True):
        chunk = lines[start:end]
        body = "\n".join(chunk)
        section = Section(
            tables=table_shapes(chunk),
            list_items=len(LIST_ITEM.findall(body)),
            fences=sum(start <= pos < end for pos in fence_starts),
            images=len(IMAGE.findall(body)),
            display_math=len(DISPLAY_MATH.findall(body)),
            quotes=blockquote_blocks(chunk),
        )
        sk.sections.append(section.key())
    return sk


def check_switcher(path: Path, lang: str | None) -> list[str]:
    """Check the language-switcher line of ``path`` (``lang`` None = Vietnamese)."""
    stem = path.name
    for suffix in TRANSLATION_SUFFIXES:
        stem = stem.removesuffix(suffix)
    stem = stem.removesuffix(".md")
    names = {"vi": f"{stem}.md", "en": f"{stem}.en.md", "zh": f"{stem}.zh-CN.md"}
    current = {None: "vi", "en": "en", "zh-CN": "zh"}[lang]
    for line in path.read_text("utf-8").splitlines()[:8]:
        match = SWITCHER.match(line)
        if not match:
            continue
        problems = []
        for key, name in names.items():
            part = match.group(key)
            if key == current:
                if not part.startswith("**"):
                    problems.append(
                        f"switcher: the current language ({key}) must be bold"
                    )
            elif not part.endswith(f"({name})"):
                problems.append(f"switcher: the {key} link must point to {name}")
        return problems
    return ["switcher: no language-switcher line in the first 8 lines"]


def emphasis_problems(text: str) -> list[str]:
    """Find ``**bold**`` spans that GitHub would show with literal asterisks.

    CommonMark only lets a ``**`` close when it is not preceded by punctuation
    or is followed by a space or punctuation (and mirror-image for opening).
    Text such as ``**注意：**这是`` therefore does not render as bold.
    """
    problems = []
    prose = FENCE.sub("", text)
    prose = re.sub(r"`[^`\n]*`", "``", prose)
    prose = re.sub(r"\$[^$\n]*\$", "$$", prose)
    for number, line in enumerate(prose.splitlines(), 1):
        marks = [m.start() for m in re.finditer(r"(?<!\*)\*\*(?!\*)", line)]
        for index, pos in enumerate(marks):
            before = line[pos - 1] if pos else " "
            after = line[pos + 2] if pos + 2 < len(line) else " "
            opening = index % 2 == 0
            inner, outer = (after, before) if opening else (before, after)
            inner_is_punctuation = unicodedata.category(inner).startswith("P")
            outer_is_word = not (
                outer.isspace() or unicodedata.category(outer).startswith("P")
            )
            if inner_is_punctuation and outer_is_word:
                kind = "opening" if opening else "closing"
                context = line[max(0, pos - 12) : pos + 14]
                problems.append(
                    f"emphasis: {kind} ** at line {number} touches punctuation and "
                    f"a letter, so it will not render as bold: ...{context}..."
                )
    return problems


def diff_counters(name: str, a: Counter, b: Counter) -> list[str]:
    """Describe how counter ``b`` differs from the original ``a``."""
    problems = []
    for item in sorted((a - b).keys()):
        problems.append(f"{name} missing in translation: {item!r} (x{(a - b)[item]})")
    for item in sorted((b - a).keys()):
        problems.append(f"{name} not in original: {item!r} (x{(b - a)[item]})")
    return problems


def compare(original: Path, translated: Path, lang: str) -> list[str]:
    """Return the problems found between a guide and one translation."""
    a = skeleton(original.read_text("utf-8"))
    b = skeleton(translated.read_text("utf-8"))
    problems = []
    if b.switchers > 1:
        problems.append("more than one language-switcher line")
    problems += check_switcher(translated, lang)
    problems += emphasis_problems(translated.read_text("utf-8"))
    if a.headings != b.headings:
        first = next(
            (
                i
                for i, (x, y) in enumerate(zip(a.headings, b.headings, strict=False))
                if x != y
            ),
            min(len(a.headings), len(b.headings)),
        )
        problems.append(
            f"headings differ: original has {len(a.headings)}, translation has "
            f"{len(b.headings)}; first mismatch at heading #{first + 1}"
        )
    problems += diff_counters("formula", a.math, b.math)
    if a.code != b.code:
        if len(a.code) != len(b.code):
            problems.append(f"code blocks: {len(a.code)} vs {len(b.code)}")
        for i, (x, y) in enumerate(zip(a.code, b.code, strict=False), 1):
            if x != y:
                problems.append(f"code block #{i} differs (ignoring comments)")
    if a.images != b.images:
        problems.append(f"images differ: {a.images} vs {b.images}")
    problems += diff_counters("link", a.links, b.links)
    stem = original.stem
    own_versions = {f"{stem}.md", *(f"{stem}.{code}.md" for code in LANGUAGES)}
    for target in b.raw_links:
        path = target.split("#", 1)[0]
        if path in own_versions:  # e.g. the "Languages" table lists every version
            continue
        if path.endswith(".md") and not path.endswith(f".{lang}.md"):
            problems.append(f"link to a Vietnamese guide, use the {lang} one: {target}")
    if a.headings == b.headings:
        for i, (x, y) in enumerate(zip(a.sections, b.sections, strict=True)):
            if x != y:
                problems.append(
                    f"section #{i} (tables, list items, fences, images, display "
                    f"formulas, quotes): original {x} vs translation {y}"
                )
    return problems


def main(argv: list[str]) -> int:
    """Compare every guide, or only the ones named on the command line."""
    guides = original_guides(REPO_ROOT)
    if argv:
        wanted = {(REPO_ROOT / arg).resolve() for arg in argv}
        guides = [g for g in guides if g.resolve() in wanted]
    failed = 0
    for guide in guides:
        name = guide.relative_to(REPO_ROOT).as_posix()
        own = check_switcher(guide, None)
        if own:
            failed += 1
            print(f"DIFFERS  {name}")
            for problem in own:
                print(f"    {problem}")
        for lang in LANGUAGES:
            target = translation_path(guide, lang)
            label = target.relative_to(REPO_ROOT).as_posix()
            if not target.exists():
                print(f"MISSING  {label}")
                failed += 1
                continue
            problems = compare(guide, target, lang)
            if problems:
                failed += 1
                print(f"DIFFERS  {label} (original: {name})")
                for problem in problems:
                    print(f"    {problem}")
            else:
                print(f"ok       {label}")
    print(
        f"Checked {len(guides)} guide(s) x {len(LANGUAGES)} language(s): "
        f"{failed} problem file(s)."
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
