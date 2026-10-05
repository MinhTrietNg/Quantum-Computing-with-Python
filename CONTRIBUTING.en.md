# Contributing

[Tiếng Việt](CONTRIBUTING.md) · **English** · [简体中文](CONTRIBUTING.zh-CN.md)

Thank you for wanting to help. This repo shares the knowledge of the book at
[learnquantum.io](https://learnquantum.io) with Vietnamese readers, with English and Simplified Chinese translations. Every contribution is welcome,
from fixing a typo to writing a guide for a new chapter.

## Ways to contribute

| You want to | What to do |
|---|---|
| Report an error in the book's content (formulas, code, explanations) | Open an issue with the **Báo lỗi trong sách** template ("Errors in the book") |
| Report a notebook that does not run | Open an issue with the **Notebook không chạy** template ("Notebook does not run"), including your Qiskit version and the traceback |
| Suggest improvements to, or fix something in, the guide (Vietnamese, English or Simplified Chinese version) | Open an issue with the **Góp ý hướng dẫn** template ("Guide feedback"), or just send a pull request |
| Ask about the knowledge in the book | Open an issue with the **Câu hỏi khi học** template ("Question while studying") (Vietnamese, English or Chinese are all fine), or ask the author in the [original repo's Discussions](https://github.com/learn-quantum/lqc-textbook/discussions) (in English) |

## The most important rule: notebooks stay verbatim

Every file in `chapters/` **except the READMEs** (`README.md` and its two translations `README.en.md`, `README.zh-CN.md`) is a byte-for-byte copy of the
[original repo](https://github.com/learn-quantum/lqc-textbook), including the outputs the author ran and including the errors.
That way readers can compare against the website, and updating from upstream only needs a copy-and-overwrite.

- **Do not** edit, re-run and save, or clear the output of the notebooks and figures in `chapters/`.
- If you find an error in the book, record it; do not fix it in place:
  1. add a `> Note: ...` right where it applies in the README of that part;
  2. add a row to the matching table (Code, Content or Typos) in [ERRATA.md](ERRATA.en.md);
  3. you should also report it to the author in the [original repo's Issues](https://github.com/learn-quantum/lqc-textbook/issues).
- `python scripts/check_upstream.py` must report *in sync* after your change. CI also checks this every week.

## README template for a part

Each folder `chapters/PP_part_name/` has one `README.md` written in Vietnamese (the original), following this template, plus two translations `README.en.md` and `README.zh-CN.md` (see [Translations](#translations-english-and-chinese)):

```markdown
# PP · English name (Vietnamese name)

A short paragraph: what this part teaches and how it connects to the previous/next part.

> Source: [PP_01](https://learnquantum.io/chapters/...) · [PP_02](...)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## Contents

| Lesson | Notebook | Web | Key idea |
|---|---|---|---|

## PP_BB · Lesson name (Vietnamese name)

**Goal** — one sentence.

### Key concepts
### Key code
### Results
### Quick recap

## API summary for this part
## How to run
```

Style:

- Write in Vietnamese; the first time a term appears, keep the original word in parentheses, for example "vướng víu (entanglement)".
- Formulas use GitHub's LaTeX: `$...$` inline, `$$...$$` for a formula on its own line. In tables,
  write `\vert` instead of `|` (for example `$\vert 0\rangle$`). The length (norm) of a vector is written `$\|q\|$` outside tables,
  but inside tables it must be written `$\Vert q\Vert$`, because GitHub's tables read `\|` as a single `|`.
- Code taken from notebooks stays unchanged; you may only add explanatory comments.
- **Results** come from the output saved in the notebook, not from your own run.
- Short sentences, one idea per sentence; prefer tables when comparing several things.

## Updating from upstream

When `scripts/check_upstream.py` (or the **Upstream** workflow) reports changes:

1. Clone the original: `git clone --depth 1 https://github.com/learn-quantum/lqc-textbook.git <tmp>`.
2. Copy the files reported as **new** or **modified** from `<tmp>/chapters/` into `chapters/`, at the same paths;
   delete the files reported as **deleted**.
3. Re-run `python scripts/check_upstream.py --upstream <tmp>` until it reports *in sync*.
4. Update the README of the corresponding part and its two translations (for a new chapter, write the README with the template above), the contents table in
   [README.md](README.en.md), and the commit and fetch date in the *Origin and updates* section of the README.
5. Re-read [ERRATA.md](ERRATA.en.md): remove the errors the author has fixed.

A chapter reported as an *empty stub* has only a title and no content yet, so it does not need to be copied yet.

## Writing the introductory documents (the `docs/` folder)

`docs/` is the part this repo writes itself for newcomers, so it must be **correct** first and engaging second:

- **Every technical statement must be verifiable.** Cite a source when you give numbers, and say so when something is
  *not proven* instead of writing as if it were certain (for example: Shor versus classical algorithms).
- **Do not overstate the hardware and the applications.** Anything that depends on timing must carry a date, for example
  "as of October 2026".
- **Every code snippet in the docs must run** (`scripts/check_doc_snippets.py` checks this, and each snippet
  must carry its own `import`s so it can run on its own), and the output shown in the docs must come from a real run
  (for sampled results, add a note that they will differ each time).
- **Explain a term the first time it appears**, or link to the [glossary](docs/glossary.en.md); add new terms
  to it.
- **Do not promise what the repo does not guarantee.** Study times are estimates; say clearly which platforms are not tested automatically.
- When you change a number that is used in several places (number of notebooks, tested versions, study time), find and fix every place:
  [README](README.en.md), [docs/setup.md](docs/setup.en.md), [docs/learning-path.md](docs/learning-path.en.md),
  [docs/faq.md](docs/faq.en.md).

## Translations (English and Chinese)

Every Markdown file in the repo (`README.md`, `CONTRIBUTING.md`, `ERRATA.md`, `docs/*.md`, `chapters/*/README.md`) has two translations
next to it: `<name>.en.md` (English) and `<name>.zh-CN.md` (简体中文, Simplified Chinese). **The Vietnamese version is the original**:
change the content there first, then update both translations in the same pull request.

- The first line after the title (`#`) of every file is the language switcher, in exactly this form (the current language in bold, the other two are links to the sibling files):

  ```markdown
  [Tiếng Việt](README.md) · **English** · [简体中文](README.zh-CN.md)
  ```

- A translation should read naturally, but it **keeps the structure**: the same headings (same level, same order), the same formulas, the same
  code (only comments may be translated), the same figures, the same links (pointing to the same-language translation of the target file where there is one), the same number of table rows and list items.
  `python scripts/check_translations.py` checks these and CI runs it.
- A `text` block that contains a diagram with word labels (for example the learning-path diagram in `docs/learning-path.md`) may be translated when the line directly above it is `<!-- translate-block -->` (put that line in all three versions). Every other code block must match the original, apart from comments.
- A link to a heading (anchor) in a translation must point to the **translated** heading; `python scripts/check_links.py` checks that.
- Keep proper names, function names, commands, paths, numbers and dates unchanged. The first time a term appears, give the English original
  in parentheses (in the Chinese version), and use one translation consistently across the whole repo.
- Translate only; do not add or drop ideas. If you find a mistake in the original, fix it in the Vietnamese version first, then update the translations.
- Issues and pull requests may be written in Vietnamese, English or 中文. Anyone who reads a language can help review the translations in that language.

## Checks before you send a pull request

```bash
pip install -r requirements-dev.txt
pytest --nbmake chapters/                # run every notebook (without overwriting the output)
python scripts/check_upstream.py         # notebooks still match the original
python scripts/check_links.py            # links, figures and anchors in every .md file are still correct (including upper/lower case)
python scripts/check_doc_snippets.py     # every Python snippet in the README and docs/ runs
python scripts/check_translations.py     # the .en.md and .zh-CN.md files still match the Vietnamese original
black --check scripts/ && ruff check scripts/
```

To run just one part quickly: `pytest --nbmake chapters/04_quantum_algorithms/`.

## Commit

Small commits, one thing per commit, English messages following
[Conventional Commits](https://www.conventionalcommits.org/):

```text
docs(02_quantum_computing): explain the Bloch sphere angles
fix(errata): correct the Grover oracle note
chore: sync chapters with upstream 1a2b3c4
```

## For maintainers

- Two workflows run on a weekly schedule (`notebooks.yml` and `upstream.yml`). GitHub automatically disables scheduled workflows
  in a public repo if the repo has no activity for 60 days; if you see CI stop running, go to the *Actions* tab and turn it back on.
- `upstream.yml` only reports (the workflow fails) when the original has changes; it does not update anything by itself. The maintainer copies the new
  chapters following the *Updating from upstream* section above.
- Formulas in Markdown: use `\vert` (not `|` or `\|`) for the vertical bar, as in $\vert 0\rangle$, and use
  `\Vert` for the norm symbol (vector length). These two commands render correctly both inside and outside tables; `\|` is only correct
  outside tables.

## License

By contributing, you agree that your contribution is released under the [MIT License](LICENSE), like the rest
of the repo.
