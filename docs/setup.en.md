# Setup and running the notebooks

[Tiếng Việt](setup.md) · **English** · [简体中文](setup.zh-CN.md)

There are three ways to use this repo, from the easiest to the most complete. You do not need an IBM Quantum account or a real quantum computer;
every notebook runs on a simulator right on your own computer.

| Way | You need | Best when |
|---|---|---|
| **1. Read only on GitHub** | A browser | You want a quick look, or you only need to grasp the ideas. The output is already in the notebooks |
| **2. Google Colab** | A Google account | You want to run code without installing anything |
| **3. Run on your computer** | Python 3.11 or later | Serious study; you get all the figures as in the book |

## 1. Read only on GitHub

Open the [Contents](../README.en.md#contents) and pick a lesson. GitHub displays the notebook together with the output and figures that the author
already ran. This is the fastest way to see what the book looks like.

## 2. Google Colab (no installation)

Colab runs notebooks on Google's servers, in your browser.

### Quickly try the sample code (blank notebook)

Open [colab.research.google.com](https://colab.research.google.com) and choose *New notebook*. In the first cell, paste
`%pip install -q qiskit qiskit-aer` and click the ▶ button to run it. Then paste the sample code (from the [README](../README.en.md#try-it-now)
or the [introduction page](what-is-quantum-computing.en.md)) into a new cell and run it.

### Running the book's notebooks

Every time you open one of the book's notebooks, you do three steps:

1. **Open the notebook in Colab.** Open the notebook on GitHub, then in the address bar change `github.com` to
   `colab.research.google.com/github`. For example:

   ```text
   https://colab.research.google.com/github/MinhTrietNg/Quantum-Computing-with-Python/blob/main/chapters/01_classical_computing/01_01_bits_and_circuits.ipynb
   ```

   (If you use a fork, replace `MinhTrietNg` with your own account name.) Try it right away with
   [00_01 on Colab](https://colab.research.google.com/github/MinhTrietNg/Quantum-Computing-with-Python/blob/main/chapters/00_getting_started/00_01_setting_env.ipynb).

2. **Install the libraries.** Click **+ Code** to add a new code cell (it appears right below the selected cell; the position does not matter, as long as you run it
   **before** the other cells), paste the code below and click the ▶ button (or press `Shift+Enter`) to run it:

   ```python
   %pip install -q "qiskit[visualization]>=2.5,<3" qiskit-aer qiskit-ibm-runtime pylatexenc
   !mkdir -p ~/.qiskit
   !curl -sL https://raw.githubusercontent.com/MinhTrietNg/Quantum-Computing-with-Python/main/qiskit_settings.conf -o ~/.qiskit/settings.conf
   ```

   The last two lines make the figures look like the book (see the [configuration section](#configure-qiskit-so-the-figures-match-the-book)).
   If Colab says it needs a restart, choose *Runtime → Restart session* and continue from this cell.

3. **Run the remaining cells** from top to bottom.

**Limitations of Colab:**
- The illustrations in the text of the notebooks (paths like `images/...`) usually **do not show** in Colab.
  Keep the notebook page on GitHub open next to it to see the figures.
- The repo's CI only tests on Ubuntu with Python 3.11 and 3.12. Colab is **not tested automatically**,
  so if you run into an error, please [tell us](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose).

## 3. Run on your computer

### Step 1: Python

> **Terminal** is the window where you type commands. Windows: click Start, type `PowerShell`, press Enter. macOS: open the *Terminal* app.
> The command `cd folder-name` moves into a folder.

You need **Python 3.11 or later**. The repo is tested with 3.11 and 3.12. If you do not have Python yet, install version **3.12** (on
python.org, open *Downloads* and choose *Python 3.12.x*, instead of the "latest version" button). If you already have a newer version, just try it;
if you get errors when installing the libraries, switch to 3.12. After installing, **close and reopen the terminal**.

Check whether you already have Python:

```bash
python --version        # on macOS/Linux it may be: python3 --version
```

On Windows, if the command above does not work, try `py --version`. If typing `python` makes Windows open the Microsoft Store, install Python
from [python.org](https://www.python.org/downloads/) and **tick the "Add python.exe to PATH" box** on the first screen of the installer.

### Step 2: Get the source code

If you have `git`:

```bash
git clone https://github.com/MinhTrietNg/Quantum-Computing-with-Python.git
cd Quantum-Computing-with-Python
```

No git yet? On the repo page, click the green **Code → Download ZIP** button, unzip it, then open a terminal in the folder you just unzipped.

### Step 3: Virtual environment and libraries

A virtual environment (`.venv`) keeps this repo's libraries separate from the rest of your computer.

```bash
python -m venv .venv                  # Windows with several Python versions: py -3.12 -m venv .venv
```

Activate the virtual environment (do this every time you open a new terminal):

| Operating system | Command |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| macOS, Linux | `source .venv/bin/activate` |

When it works, `(.venv)` appears at the start of the command line. (PowerShell says *running scripts is disabled*? See
[Troubleshooting](#troubleshooting).) Then install the libraries:

```bash
pip install -r requirements.txt
```

### Step 4: Open a notebook

**Option A: Jupyter.** Run:

```bash
jupyter notebook chapters/
```

A browser opens with a list of folders. Click `00_getting_started`, then `00_01_setting_env.ipynb`.
A notebook is made of **cells**: text cells and code cells. Click a code cell, then press **`Shift+Enter`** to run it and
move on to the next cell.

**Option B: VS Code.** Install the *Python* and *Jupyter* extensions, open the repo folder, open the `.ipynb` file, click
*Select Kernel* and choose `.venv`.

Each notebook is independent of the others, but within one notebook, **a later cell uses the variables of the earlier cells**,
so run them from top to bottom.

### Check your environment

In Jupyter, choose *File → New → Notebook* (pick the Python 3 kernel), paste the following into a cell and press `Shift+Enter`.
(Or save it as a file `kiem_tra.py` and run `python kiem_tra.py`.)

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

If you see a result like `{'11': 492, '00': 508}` (the numbers and their order differ every time, but there are only `00` and `11`, each
about half), your environment is fine.

### Configure Qiskit so the figures match the book

Copy [qiskit_settings.conf](../qiskit_settings.conf) to `settings.conf` in your `.qiskit` folder
(create the folder if it does not exist). **If you already have a `settings.conf` file, back it up or merge it by hand** so you do not overwrite your old settings:

| Operating system | Destination |
|---|---|
| Windows | `C:\Users\<name>\.qiskit\settings.conf` |
| macOS, Linux | `~/.qiskit/settings.conf` |

Or use commands, run in the repo's root folder (neither command overwrites an existing file):

```bash
# macOS, Linux
mkdir -p ~/.qiskit && cp -n qiskit_settings.conf ~/.qiskit/settings.conf
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force $HOME\.qiskit | Out-Null
if (-not (Test-Path $HOME\.qiskit\settings.conf)) { Copy-Item qiskit_settings.conf $HOME\.qiskit\settings.conf }
```

Another way that does not touch `~/.qiskit`: set the environment variable `QISKIT_SETTINGS` to point to the repo's `qiskit_settings.conf` file
(the repo's CI does exactly this).

This file sets the circuit drawing style (IBM colors, hiding unused wires, higher-index qubits on top). Without it, circuit drawings
look slightly different from the figures in the book (for example the qubit order is upside down), **but the computed results are the same**.
The meaning of each option is explained in [00_02](../chapters/00_getting_started/README.en.md#00_02--configuring-qiskit).

## A few conventions that cause confusion when reading Qiskit code

You do not need to remember all of this right away; when you run into multi-qubit measurement results, come back here.

- **Qubit order (little-endian):** in a result string such as `'011'`, the **rightmost** character is qubit 0.
  Many other texts write it the other way round.
- `circuit_reverse_bits = True` in `settings.conf` only changes how the circuit is **drawn**, not the results.
- `Statevector(qc)` computes the exact state, with no statistical noise (use it for circuits without measurements).
  `AerSimulator().run(qc, shots=N)` simulates measuring $N$ times, so **each run gives slightly different numbers**
  that also differ from the output saved in the notebook. The conclusions do not change.
- A circuit with measurements needs classical bits to store the results: `QuantumCircuit(n_qubits, n_bits)`.
  (`measure_all()` adds them automatically.)

## Troubleshooting

| Symptom | Common cause | What to do |
|---|---|---|
| `ModuleNotFoundError: No module named 'qiskit'` (or `qiskit_aer`) | Jupyter is using a different kernel from the environment you installed into | Activate `.venv` and run `jupyter` again; in VS Code, select the `.venv` kernel again |
| `ImportError` mentioning `pylatexenc` | A circuit-drawing library is missing | `pip install pylatexenc` (it is already in `requirements.txt`) |
| `ImportError: cannot import name 'execute'` or `'Aer'` | Old-style Qiskit code (before 1.0) | The book uses Qiskit 2.x with `AerSimulator`; install the versions specified in `requirements.txt` |
| PowerShell says *running scripts is disabled* when you activate `.venv` | The Windows execution policy | Use `activate.bat` in cmd, or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `UnicodeEncodeError` on `print(qc.draw("text"))` on Windows | When the output is redirected (`> file`, a pipe, some IDEs), Python uses the Windows ANSI code page (such as cp1252), which cannot encode the box characters ┌─┐ | Set the environment variable `PYTHONUTF8=1` before running the script (notebooks do not have this problem) |
| The circuit drawing differs from the figure in the book | There is no `settings.conf` yet | See the [Configure](#configure-qiskit-so-the-figures-match-the-book) section; the results are still correct |
| The measured numbers differ from the saved output | Random sampling | Normal; compare the *conclusions*, not each number |
| Error on `pip install` with a new Python | There are no prebuilt packages yet for a Python version that is too new | Use Python 3.12 |
| A notebook reports an error after you upgrade Qiskit | The API changed between versions | Run `pip list`, compare with the tested versions below, then [report the error](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose) with the traceback |

## Tested versions

All 19 notebooks run (checked on 2026-10-01) with: Python 3.11, Qiskit 2.5.2, Qiskit Aer 0.17.2,
Qiskit IBM Runtime 0.50.0. CI re-runs weekly with the latest versions to give early warning when a new Qiskit release breaks
a notebook.
