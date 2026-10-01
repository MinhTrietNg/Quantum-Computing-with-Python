"""Compare this repo's notebooks with the upstream learnquantum.io textbook.

The upstream repo (learn-quantum/lqc-textbook) keeps every chapter under
``chapters/<part>/``, the same layout as this repo. The script lists files
that are new, changed or removed upstream, and chapters that are still empty
stubs there. Local ``README.md`` files are this repo's own study guides and
are ignored.

Usage
-----
    python scripts/check_upstream.py                    # clone upstream
    python scripts/check_upstream.py --upstream PATH    # use a local clone

Exits with status 1 when the local copy differs from upstream, so it can be
used in CI.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

UPSTREAM_URL = "https://github.com/learn-quantum/lqc-textbook.git"
REPO_ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = "chapters"

# Upstream files kept outside chapters/, mapped to their local names.
EXTRA_FILES = {"LICENSE": "LICENSE", "settings.conf": "qiskit_settings.conf"}

# Files in chapters/ that exist only in this repo.
LOCAL_ONLY = {"README.md"}

# Upstream stubs hold only a title, about 30 characters of source in total.
STUB_MAX_CHARS = 200

TEXT_SUFFIXES = {".ipynb", ".md", ".conf", ".txt", ""}


@dataclass
class Report:
    """Differences between the local copy and upstream."""

    new: list[str] = field(default_factory=list)
    changed: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    stubs: list[str] = field(default_factory=list)

    @property
    def in_sync(self) -> bool:
        """Return True when nothing needs to be copied or deleted."""
        return not (self.new or self.changed or self.removed)


def clone_upstream(dest: Path) -> Path:
    """Shallow-clone the upstream repo into ``dest`` and return its path."""
    subprocess.run(
        ["git", "clone", "--quiet", "--depth", "1", UPSTREAM_URL, str(dest)],
        check=True,
    )
    return dest


def head_commit(repo: Path) -> str:
    """Return ``<sha> (<date>)`` of the checked-out commit in ``repo``."""
    result = subprocess.run(
        ["git", "-C", str(repo), "log", "-1", "--format=%H (%cs)"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def read_normalized(path: Path) -> bytes:
    """Read a file, ignoring line endings and final newlines in text files."""
    data = path.read_bytes()
    if path.suffix in TEXT_SUFFIXES:
        data = data.replace(b"\r\n", b"\n").rstrip(b"\n")
    return data


def is_stub(notebook: Path) -> bool:
    """Return True if a notebook has (almost) no content yet.

    Parameters
    ----------
    notebook : Path
        Path to an ``.ipynb`` file.

    Returns
    -------
    bool
        True when all cell sources together are shorter than
        ``STUB_MAX_CHARS`` characters.
    """
    cells = json.loads(notebook.read_text(encoding="utf-8"))["cells"]
    chars = sum(len("".join(cell["source"])) for cell in cells)
    return chars < STUB_MAX_CHARS


def list_files(root: Path) -> set[str]:
    """Return POSIX paths of all files under ``root``, relative to it."""
    return {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}


def compare(upstream: Path, local: Path) -> Report:
    """Build a :class:`Report` comparing two repo checkouts.

    Parameters
    ----------
    upstream : Path
        Root of an lqc-textbook checkout.
    local : Path
        Root of this repo.

    Returns
    -------
    Report
        Paths are relative to each repo root and use local names.
    """
    report = Report()
    up_files = list_files(upstream / CHAPTERS)
    local_files = {
        f for f in list_files(local / CHAPTERS) if Path(f).name not in LOCAL_ONLY
    }

    pairs = [(f"{CHAPTERS}/{f}", f"{CHAPTERS}/{f}") for f in sorted(up_files)]
    pairs += sorted(EXTRA_FILES.items())

    for up_rel, local_rel in pairs:
        up_path, local_path = upstream / up_rel, local / local_rel
        if not up_path.exists():
            continue
        if up_path.suffix == ".ipynb" and is_stub(up_path):
            if not local_path.exists():
                report.stubs.append(local_rel)
                continue
        if not local_path.exists():
            report.new.append(local_rel)
        elif read_normalized(up_path) != read_normalized(local_path):
            report.changed.append(local_rel)

    report.removed = [f"{CHAPTERS}/{f}" for f in sorted(local_files - up_files)]
    return report


def print_section(title: str, paths: list[str]) -> None:
    """Print a titled list of paths, or nothing if the list is empty."""
    if not paths:
        return
    print(f"\n{title} ({len(paths)}):")
    for path in paths:
        print(f"  {path}")


def print_report(report: Report, commit: str) -> None:
    """Print a human-readable summary of ``report``."""
    print(f"Upstream: {UPSTREAM_URL}")
    print(f"Commit:   {commit}")
    print_section("New upstream, missing here", report.new)
    print_section("Changed upstream", report.changed)
    print_section("Removed upstream, still here", report.removed)
    print_section("Still empty stubs upstream (not copied)", report.stubs)
    if report.in_sync:
        print("\nLocal copy is in sync with upstream.")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--upstream",
        type=Path,
        help="path to an existing lqc-textbook clone (default: clone a fresh one)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the comparison and return the process exit code."""
    args = parse_args(argv)
    # Git marks pack files read-only, which breaks cleanup on Windows.
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        upstream = args.upstream or clone_upstream(Path(tmp) / "lqc-textbook")
        report = compare(upstream, REPO_ROOT)
        print_report(report, head_commit(upstream))
    return 0 if report.in_sync else 1


if __name__ == "__main__":
    sys.exit(main())
