"""Run the Python code blocks that appear in the introductory docs.

The docs promise that every snippet runs and prints what the text says.
This script keeps that promise honest: it extracts each ```python block from
README.md and docs/*.md, runs it in a fresh interpreter, and fails if any
block raises. Blocks that use notebook magics (``%pip``, ``!cmd``) are skipped
because they only make sense inside Colab or Jupyter.

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
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"^```python[ \t]*\n(.*?)^```", re.DOTALL | re.MULTILINE)
MAGIC = re.compile(r"^\s*(%|!)", re.MULTILINE)
TIMEOUT_SECONDS = 120


def doc_files(root: Path) -> list[Path]:
    """Return README.md and every Markdown file under docs/."""
    return [root / "README.md", *sorted((root / "docs").glob("*.md"))]


def extract_snippets(markdown: str) -> list[str]:
    """Return the body of every ```python fenced block in ``markdown``."""
    return FENCE.findall(markdown)


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
