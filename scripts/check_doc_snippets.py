"""Run the Python code blocks that appear in the introductory docs.

The docs promise that every snippet runs and prints what the text says.
This script keeps that promise honest: it extracts each ```python (or ```py)
block from README*.md and docs/*.md, translations such as README.en.md
included, runs it in a fresh interpreter, and fails if any block raises.
Blocks indented inside list items are found too. Blocks that use notebook
magics (``%pip``, ``!cmd``) are skipped because they only make sense inside
Colab or Jupyter.

Output of sampling code differs on every run, so only the exit status is
checked, not the printed counts.

Usage
-----
    python scripts/check_doc_snippets.py

Exits with status 1 when any snippet fails, so it can be used in CI.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
# A fence may be indented (inside a list item); its body is dedented before use.
FENCE = re.compile(
    r"^[ \t]*(?P<fence>`{3,}|~{3,})[ \t]*(?:python3?|py)\b[^\n]*\n"
    r"(?P<body>.*?)^[ \t]*(?P=fence)[ \t]*$",
    re.DOTALL | re.MULTILINE | re.IGNORECASE,
)
MAGIC = re.compile(r"^\s*(%|!)", re.MULTILINE)
TIMEOUT_SECONDS = 120


def doc_files(root: Path) -> list[Path]:
    """Return README*.md at the root and every Markdown file under docs/."""
    return [*sorted(root.glob("README*.md")), *sorted((root / "docs").glob("*.md"))]


def extract_snippets(markdown: str) -> list[str]:
    """Return the dedented body of every Python fenced block in ``markdown``."""
    return [textwrap.dedent(m.group("body")) for m in FENCE.finditer(markdown)]


def run_snippet(code: str) -> subprocess.CompletedProcess[str]:
    """Run ``code`` in a fresh Python process with UTF-8 output."""
    env = {**os.environ, "PYTHONUTF8": "1", "MPLBACKEND": "Agg"}
    return subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        timeout=TIMEOUT_SECONDS,
    )


def main() -> int:
    """Run all snippets and return the process exit code."""
    ran = skipped = failed = 0
    for path in doc_files(REPO_ROOT):
        name = path.relative_to(REPO_ROOT).as_posix()
        for index, code in enumerate(extract_snippets(path.read_text("utf-8")), 1):
            if MAGIC.search(code):
                skipped += 1
                print(f"skip  {name} #{index} (notebook magics)")
                continue
            result = run_snippet(code)
            ran += 1
            if result.returncode:
                failed += 1
                print(f"FAIL  {name} #{index}\n{result.stderr.strip()[-600:]}")
            else:
                print(f"ok    {name} #{index}")
    print(f"Ran {ran} snippet(s), skipped {skipped}, failed {failed}.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
