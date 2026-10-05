# Quantum Computing with Python

[Tiếng Việt](README.md) · **English** · [简体中文](README.zh-CN.md)

[![Notebooks](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/actions/workflows/notebooks.yml/badge.svg)](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/actions/workflows/notebooks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-6929C4)

**Learn quantum computing from scratch, with Python.**
Free. No quantum physics needed, no quantum computer needed, and it runs on an ordinary laptop.
All you need is **basic Python**; the math is taught gradually.

The goal after about 4–6 weeks of steady study (an estimate, one hour a day): to understand what qubits, superposition,
entanglement and interference are, to write and run quantum circuits with Qiskit on your own, and to explain teleportation
and the Deutsch–Jozsa, Bernstein–Vazirani, Simon and Grover algorithms.

## Try it now

Here is a complete quantum program. It creates two **entangled** qubits and then measures them 1000 times:

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)             # H gate: puts qubit 0 (a quantum bit) into a 50/50 state between 0 and 1
qc.cx(0, 1)         # CX gate: ties qubit 1 to qubit 0 (entanglement)
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
# {'11': 496, '00': 504}
```

`shots=1000` means run the circuit and measure 1000 times; your numbers will differ slightly from the ones above because measurement is random.
The result is only ever `00` or `11`, **never** `01` or `10`: each qubit on its own is random 50/50,
but the two qubits always agree. (A real machine has noise, so a few `01`/`10` results slip through now and then; an ideal simulator has none.)
Why does this happen, and why is this alone *not yet* enough to call it quantum? Entanglement is covered in Part 02; the full
evidence (Bell inequalities) has not been written yet in the original textbook, so see [Resources](docs/resources.en.md).

**Haven't installed Qiskit yet?** Open [Google Colab](https://colab.research.google.com) and choose *New notebook*, run `%pip install -q qiskit qiskit-aer`
in a cell, then paste the code above into a new cell. To install it on your own computer, see the [Getting started](#getting-started) section.

**Next steps:**
[Nothing installed? Run it on Google Colab](docs/setup.en.md#2-google-colab-no-installation) ·
[Read the 15-minute introduction](docs/what-is-quantum-computing.en.md) ·
[See the learning path](docs/learning-path.en.md)

## Who this is for

| You are | Start with |
|---|---|
| **Curious, no programming experience yet** | [What is a quantum computer?](docs/what-is-quantum-computing.en.md), 15 minutes, little math (fractions and square roots); then see the [Learning path](docs/learning-path.en.md) |
| **Know basic Python** | The [Learning path](docs/learning-path.en.md), then start from [Part 00](chapters/00_getting_started/) |
| **Know Python and linear algebra** | The [Learning path](docs/learning-path.en.md) shows how to skim Part 01 and go straight into Part 02 |
| **Have studied quantum mechanics** | Read the *Key code* section of [02_01](chapters/02_quantum_computing/) (the first Qiskit circuit), then 02_04, 02_05 and [Part 04](chapters/04_quantum_algorithms/) (if single-qubit gate syntax is unfamiliar, skim 02_03 as well) |
| Looking up a term | The [Glossary](docs/glossary.en.md) |
| Want to know whether a quantum computer can break encryption | The [FAQ](docs/faq.en.md#about-cryptography) |

## Getting started

Three ways, from easiest to most complete ([detailed guide](docs/setup.en.md)):

1. **Read only:** open the [contents](#contents) below and pick a lesson. GitHub shows each notebook with its saved output.
2. **Run on Google Colab:** nothing to install ([how to](docs/setup.en.md#2-google-colab-no-installation)).
3. **Run on your own computer** (needs Python 3.11 or later; the repo is tested with 3.11 and 3.12):

   ```bash
   git clone https://github.com/MinhTrietNg/Quantum-Computing-with-Python.git
   cd Quantum-Computing-with-Python
   python -m venv .venv
   # Windows (PowerShell): .venv\Scripts\Activate.ps1   |   Windows (cmd): .venv\Scripts\activate.bat
   # macOS/Linux:          source .venv/bin/activate
   pip install -r requirements.txt
   jupyter notebook chapters/
   ```

   Stuck (no Python yet, a PowerShell error, no git, ...)? See the [detailed guide and troubleshooting](docs/setup.en.md).

All 19 notebooks have been tested and run successfully ([exact versions](docs/setup.en.md#tested-versions)),
and CI re-checks them every week.

## Learning path

Read in order **Part 00 → 01 → 02 → 03 → 04**, about 25–40 hours for a careful learner (4–6 weeks at one hour a
day). The [Learning path](docs/learning-path.en.md) has a diagram, the time for each part, self-check exercises with suggested answers,
and shortcuts if you already have some background.

Each part has its own guide (written in Vietnamese, translated into English and Simplified Chinese) with key concepts, key code, results and a **quick recap** for revision.

## Contents

| Part | Lesson | Notebook | Topics |
|---|---|---|---|
| **[00 · Getting started](chapters/00_getting_started/)** | 00_00 | [About the textbook](chapters/00_getting_started/00_00_welcome.ipynb) | How to use the book, how to cite it |
| | 00_01 | [Setting up your environment](chapters/00_getting_started/00_01_setting_env.ipynb) | Installing Qiskit, code to check your environment |
| | 00_02 | [Configuring Qiskit](chapters/00_getting_started/00_02_qiskit_config.ipynb) | IBM Quantum token, `settings.conf` |
| **[01 · Classical computing](chapters/01_classical_computing/)** | 01_01 | [Bits and digital circuits](chapters/01_classical_computing/01_01_bits_and_circuits.ipynb) | Bits, logic gates, adder circuits |
| | 01_02 | [Reversible computing](chapters/01_classical_computing/01_02_reversible_computing.ipynb) | Reversible gates X, CX, CCX |
| | 01_03 | [Linear algebra for reversible circuits](chapters/01_classical_computing/01_03_bits_to_vectors.ipynb) | Bits as vectors, gates as matrices, the tensor product |
| | 01_04 | [Probabilistic computing](chapters/01_classical_computing/01_04_probabilistic_circuits.ipynb) | Probabilistic bits, noisy circuits |
| **[02 · Quantum computing](chapters/02_quantum_computing/)** | 02_01 | [Qubits and quantum circuits](chapters/02_quantum_computing/02_01_bits_to_qubits.ipynb) | The Stern–Gerlach experiment, from bits to qubits |
| | 02_02 | [Quantum entanglement](chapters/02_quantum_computing/02_02_entanglement.ipynb) | Separable and entangled states; creating entanglement with H + CX |
| | 02_03 | [Single-qubit systems](chapters/02_quantum_computing/02_03_single_qb_sys.ipynb) | Complex amplitudes, the Bloch sphere, single-qubit gates, measurement, observables |
| | 02_04 | [Multi-qubit systems](chapters/02_quantum_computing/02_04_multi_qb_sys.ipynb) | Controlled gates, SWAP, no-cloning, universal gate sets, partial measurement |
| | 02_05 | [Quantum building blocks](chapters/02_quantum_computing/02_05_quantum_blocks.ipynb) | Bell/GHZ/W states, the Hadamard transform, phase kickback, oracles |
| **[03 · Quantum protocols](chapters/03_quantum_protocols/)** | 03_01 | [Uncertainty & quantum money](chapters/03_quantum_protocols/03_01_quantum_money.ipynb) | The uncertainty principle; Wiesner's quantum money: the more qubits, the harder to forge |
| | 03_02 | [Quantum teleportation](chapters/03_quantum_protocols/03_02_teleportation.ipynb) | Teleporting a quantum state |
| | 03_03 | [Superdense coding](chapters/03_quantum_protocols/03_03_superdense_coding.ipynb) | Sending 2 classical bits with 1 qubit |
| **[04 · Foundational quantum algorithms](chapters/04_quantum_algorithms/)** | 04_01 | [Deutsch–Jozsa](chapters/04_quantum_algorithms/04_01_deutsch-jozsa.ipynb) | Constant or balanced function, 1 query |
| | 04_02 | [Bernstein–Vazirani](chapters/04_quantum_algorithms/04_02_bernstein-vazirani.ipynb) | Finding a secret string, 1 query |
| | 04_03 | [Simon's algorithm](chapters/04_quantum_algorithms/04_03_simons.ipynb) | Finding an XOR period, exponential speedup (in the oracle model) |
| | 04_04 | [Grover's algorithm](chapters/04_quantum_algorithms/04_04_grover.ipynb) | Unstructured search, square-root speedup |

### Chapters that are still empty upstream

In the original textbook, the chapters below only have titles (empty notebooks), so they are **not included** in this repo yet.
When the author finishes them, the repo will be updated; in the meantime, see [resources for further study](docs/resources.en.md).

| Part | Chapters |
|---|---|
| 03 · Quantum protocols | 03_04 Bell inequalities, 03_05 Quantum key distribution |
| 05 · Important quantum primitives | 05_01 QFT, 05_02 QPE, 05_03 Amplitude amplification |
| 06 · Advanced quantum algorithms | 06_01 Shor, 06_02 HHL, 06_03 Hamiltonian simulation |

## Supporting documents

| | |
|---|---|
| [What is a quantum computer?](docs/what-is-quantum-computing.en.md) | The big picture, interference, entanglement, what it is good and not good at |
| [Learning path](docs/learning-path.en.md) | What you need to know first, estimated time, self-check questions for each part |
| [Setup](docs/setup.en.md) | Reading, Colab or running on your computer; troubleshooting common problems |
| [Glossary](docs/glossary.en.md) | Vietnamese–English terms, with where each is taught |
| [FAQ](docs/faq.en.md) | Common misconceptions, cryptography, choosing a library |
| [Resources](docs/resources.en.md) | Books, courses and material for further study |
| [ERRATA](ERRATA.en.md) | Known errors in the original textbook |

## Origin and updates

The notebooks and figures in [chapters/](chapters/) are **verbatim copies** of the open textbook
**[Learn Quantum Computing using Python](https://learnquantum.io)** (Diego Emilio Serrano), including the outputs the author ran
and a few small errors in the original (recorded in [ERRATA](ERRATA.en.md) and in the `> Note:` entries in each part's README, so you do not need to find them yourself). What this repo adds is the README guide of each part (Vietnamese original plus English and Simplified Chinese translations),
the [docs/](docs/) folder, automated tests and the accompanying tools.

| | |
|---|---|
| Original repo | [learn-quantum/lqc-textbook](https://github.com/learn-quantum/lqc-textbook) |
| Copy taken from | commit [`7abf73c`](https://github.com/learn-quantum/lqc-textbook/commit/7abf73cb1d430e0eba1d052d8b4d8bc976e956f6) (2026-03-20), fetched on 2026-09-30 |

To see what is new in the original: `python scripts/check_upstream.py`. The update procedure is in
[CONTRIBUTING](CONTRIBUTING.en.md#updating-from-upstream).

## Repo layout

```text
.
├── chapters/             # the book: one folder per part (Vietnamese README and 2 translations + notebooks + images/)
├── docs/                 # introductory docs: introduction, learning path, setup, glossary, FAQ, resources
├── scripts/              # check_upstream.py (compare with the original repo), check_links.py, check_doc_snippets.py, check_translations.py
├── .github/              # CI that runs the notebooks, issue and pull request templates
├── ERRATA.md, CONTRIBUTING.md, CITATION.cff, LICENSE   # every .md file has an .en.md and a .zh-CN.md version
├── qiskit_settings.conf  # display settings that match the book
└── requirements.txt, requirements-dev.txt, pyproject.toml
```

## Languages

The guides come in three languages with equivalent content. The notebooks and figures in [chapters/](chapters/) are the English original
of the textbook and are shared by all three.

| Language | Start with |
|---|---|
| Tiếng Việt (Vietnamese, the repo's original) | [README.md](README.md) |
| English | [README.en.md](README.en.md) |
| 简体中文 (Chinese, Simplified) | [README.zh-CN.md](README.zh-CN.md) |

Every `.md` file has two translations next to it, named `<name>.en.md` and `<name>.zh-CN.md`
(see the [translation conventions](CONTRIBUTING.en.md#translations-english-and-chinese)).

## Contributing

All contributions are welcome: fixing translation errors or unclear explanations, adding material for newcomers, reporting errors in the
book, or notebooks that do not run with a newer Qiskit. See [CONTRIBUTING](CONTRIBUTING.en.md). Errors in the book itself should also be reported
at the [original repo's Issues](https://github.com/learn-quantum/lqc-textbook/issues).

## License and citation

The notebooks and illustrations are © 2024 Diego Emilio Serrano, released under the [MIT License](LICENSE).
The guides (the Vietnamese originals and their translations) and supporting documents are shared under the same license.
When you use the content, please cite the original book (GitHub shows a *Cite this repository* button based on [CITATION.cff](CITATION.cff)):

```bibtex
@book{learn-quantum,
    author = {Diego Emilio Serrano},
    year = {2024},
    title = {Learn Quantum Computing using Python},
    publisher = {Github},
    url = {learnquantum.io},
}
```

Many thanks to the author, Diego Emilio Serrano, for writing this book and sharing it for free.
