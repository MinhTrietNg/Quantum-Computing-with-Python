# 安装与运行 notebook

[Tiếng Việt](setup.md) · [English](setup.en.md) · **简体中文**

使用本仓库有三种方式，从最简单到最完整。你不需要 IBM Quantum 账号，也不需要真正的量子计算机；所有 notebook 都在你自己电脑上的模拟器（simulator）中运行。

| 方式 | 需要 | 适用场景 |
|---|---|---|
| **1. 只在 GitHub 上阅读** | 浏览器 | 想先看看，或者只需要理解思路。notebook 中已经带有输出 |
| **2. Google Colab** | Google 账号 | 想运行代码，但不想安装任何东西 |
| **3. 在本地运行** | Python 3.11 或更高版本 | 认真学习；能看到与书中相同的全部图形 |

## 1. 只在 GitHub 上阅读

打开[目录](../README.zh-CN.md#目录)，选择一课。GitHub 会显示 notebook，以及作者事先运行好的输出和图形。这是了解这本书大致样子的最快方式。

## 2. Google Colab（无需安装）

Colab 在 Google 的服务器上运行 notebook，你只需要使用浏览器。

### 快速试运行示例代码（空白 notebook）

打开 [colab.research.google.com](https://colab.research.google.com)，选择 *New notebook*。在第一个单元格（cell）中粘贴 `%pip install -q qiskit qiskit-aer`，然后点击 ▶ 按钮运行。之后把示例代码（见 [README](../README.zh-CN.md#立即体验) 或[入门介绍页](what-is-quantum-computing.zh-CN.md)）粘贴到一个新单元格中并运行。

### 运行书中的 notebook

每次打开书中的一个 notebook，都要完成以下三步：

1. **在 Colab 中打开 notebook**。先在 GitHub 上打开该 notebook，然后把浏览器地址栏中的 `github.com` 改成 `colab.research.google.com/github`。例如：

   ```text
   https://colab.research.google.com/github/MinhTrietNg/Quantum-Computing-with-Python/blob/main/chapters/01_classical_computing/01_01_bits_and_circuits.ipynb
   ```

   （如果你使用的是 fork，请把 `MinhTrietNg` 换成你自己的账号名。）现在就可以试试[在 Colab 上打开 00_01](https://colab.research.google.com/github/MinhTrietNg/Quantum-Computing-with-Python/blob/main/chapters/00_getting_started/00_01_setting_env.ipynb)。

2. **安装库**。点击 **+ Code** 添加一个新的代码单元格（它会出现在当前选中单元格的正下方；位置并不重要，只要你在其他单元格**之前**运行它即可），粘贴下面的代码，然后点击 ▶ 按钮（或按 `Shift+Enter`）运行：

   ```python
   %pip install -q "qiskit[visualization]>=2.5,<3" qiskit-aer qiskit-ibm-runtime pylatexenc
   !mkdir -p ~/.qiskit
   !curl -sL https://raw.githubusercontent.com/MinhTrietNg/Quantum-Computing-with-Python/main/qiskit_settings.conf -o ~/.qiskit/settings.conf
   ```

   最后两行让绘图效果与书中一致（见[配置一节](#配置-qiskit使电路图与书中一致)）。如果 Colab 提示需要重启，请选择 *Runtime → Restart session*，然后从这个单元格继续往下运行。

3. 从上到下**运行其余的单元格**。

**Colab 的局限**：
- notebook 文字部分中的插图（路径形如 `images/...`）在 Colab 上通常**无法显示**。请同时在 GitHub 上打开该 notebook 页面来查看图片。
- 本仓库的 CI 只在 Ubuntu 上用 Python 3.11 和 3.12 进行测试。Colab **尚未经过自动化测试**，所以如果遇到错误，请[告诉我们](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose)。

## 3. 在本地运行

### 第 1 步：Python

> **终端**（terminal）是用来输入命令的窗口。Windows：点击“开始”（Start），输入 `PowerShell`，按 Enter。macOS：打开 *Terminal*（终端）应用。命令 `cd 文件夹名` 用于进入某个文件夹。

需要 **Python 3.11 或更高版本**。本仓库已用 3.11 和 3.12 测试。如果还没有 Python，请安装 **3.12** 版本（在 python.org 上打开 *Downloads*，选择 *Python 3.12.x*，而不是点击“最新版本”按钮）。如果你已经装了更新的版本，可以先试试；安装库时出错的话，再换成 3.12。安装完成后，**关闭并重新打开终端**。

检查一下是否已经安装了 Python：

```bash
python --version        # macOS/Linux 上可能是：python3 --version
```

在 Windows 上，如果上面的命令不起作用，试试 `py --version`。如果输入 `python` 后 Windows 打开了 Microsoft Store，请从 [python.org](https://www.python.org/downloads/) 安装 Python，并在安装程序的第一步**勾选“Add python.exe to PATH”**。

### 第 2 步：获取源代码

如果你有 `git`：

```bash
git clone https://github.com/MinhTrietNg/Quantum-Computing-with-Python.git
cd Quantum-Computing-with-Python
```

没有 git？在仓库页面点击绿色的 **Code → Download ZIP** 按钮，解压后，在解压出来的文件夹中打开终端。

### 第 3 步：虚拟环境与库

虚拟环境（virtual environment，即 `.venv`）让本仓库用到的库与电脑上的其他部分相互隔离。

```bash
python -m venv .venv                  # Windows 上装有多个 Python 版本时：py -3.12 -m venv .venv
```

激活虚拟环境（每次打开新的终端都要做）：

| 操作系统 | 命令 |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| macOS、Linux | `source .venv/bin/activate` |

激活成功后，命令行开头会显示 `(.venv)`。（PowerShell 报错 *running scripts is disabled*？请看[常见问题排查](#常见问题排查)。）然后安装库：

```bash
pip install -r requirements.txt
```

### 第 4 步：打开 notebook

**方式 A：Jupyter**。运行：

```bash
jupyter notebook chapters/
```

浏览器会打开并显示文件夹列表。点击 `00_getting_started`，再点击 `00_01_setting_env.ipynb`。一个 notebook 由许多**单元格**（cell）组成：文字单元格和代码单元格。点击一个代码单元格，然后按 **`Shift+Enter`** 运行它，并跳到下一个单元格。

**方式 B：VS Code**。安装 *Python* 和 *Jupyter* 扩展，打开仓库文件夹，打开 `.ipynb` 文件，点击 *Select Kernel*，然后选择 `.venv`。

各个 notebook 彼此独立，但在同一个 notebook 中，**后面的单元格会用到前面单元格的变量**，所以请从上到下依次运行。

### 检查环境

在 Jupyter 中选择 *File → New → Notebook*（内核选择 Python 3），把下面的代码粘贴到一个单元格中，然后按 `Shift+Enter`。（也可以保存为 `kiem_tra.py` 文件，再运行 `python kiem_tra.py`。）

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

如果看到类似 `{'11': 492, '00': 508}` 的结果（每次的数字和顺序都会不同，但只会出现 `00` 和 `11`，各占大约一半），就说明环境已经准备好了。

### 配置 Qiskit，使电路图与书中一致

把 [qiskit_settings.conf](../qiskit_settings.conf) 复制为你的 `.qiskit` 文件夹中的 `settings.conf`（如果该文件夹不存在，就先创建它）。**如果你已经有 `settings.conf` 文件，请先备份或手动合并**，以免覆盖原有的配置：

| 操作系统 | 目标位置 |
|---|---|
| Windows | `C:\Users\<用户名>\.qiskit\settings.conf` |
| macOS、Linux | `~/.qiskit/settings.conf` |

也可以使用命令，在仓库根目录下运行（两组命令都不会覆盖已有的文件）：

```bash
# macOS, Linux
mkdir -p ~/.qiskit && cp -n qiskit_settings.conf ~/.qiskit/settings.conf
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force $HOME\.qiskit | Out-Null
if (-not (Test-Path $HOME\.qiskit\settings.conf)) { Copy-Item qiskit_settings.conf $HOME\.qiskit\settings.conf }
```

另一种不改动 `~/.qiskit` 的方法：设置环境变量 `QISKIT_SETTINGS`，让它指向仓库中的 `qiskit_settings.conf` 文件（本仓库的 CI 正是这样做的）。

这个文件设定了电路的绘制样式：IBM 配色、隐藏未使用的线路、编号较大的量子比特（qubit）画在上方。没有它，画出的电路会与书中的图略有不同（例如量子比特的顺序上下颠倒），**但计算结果完全相同**。各个选项的含义见 [00_02](../chapters/00_getting_started/README.zh-CN.md#00_02--configuring-qiskit配置-qiskit)。

## 阅读 Qiskit 代码时容易混淆的几个约定

不必马上全部记住；等遇到多量子比特的测量结果时，再回来看这里。

- **量子比特的顺序**采用小端序（little-endian）：在 `'011'` 这样的结果字符串中，**最右边**的字符是量子比特 0。很多其他资料的写法正好相反。
- `settings.conf` 中的 `circuit_reverse_bits = True` 只改变电路的**绘制**方式，不改变结果。
- `Statevector(qc)` 精确地计算量子态，没有统计噪声（用于尚未加入测量的电路）。`AerSimulator().run(qc, shots=N)` 模拟测量 $N$ 次，因此**每次运行得到的数字都会略有不同**，也会与 notebook 中保存的输出不同。但结论不变。
- 含测量的电路需要经典比特来保存结果：`QuantumCircuit(n_qubits, n_bits)`。（`measure_all()` 会自动添加经典比特。）

## 常见问题排查

| 症状 | 常见原因 | 解决方法 |
|---|---|---|
| `ModuleNotFoundError: No module named 'qiskit'`（或 `qiskit_aer`） | Jupyter 使用的内核与安装了库的环境不是同一个 | 激活 `.venv` 后重新运行 `jupyter`；在 VS Code 中重新选择 `.venv` 内核 |
| 提到 `pylatexenc` 的 `ImportError` | 缺少绘制电路所需的库 | `pip install pylatexenc`（已包含在 `requirements.txt` 中） |
| `ImportError: cannot import name 'execute'` 或 `'Aer'` | 旧式 Qiskit 代码（1.0 之前） | 本书使用 Qiskit 2.x 和 `AerSimulator`；请安装 `requirements.txt` 中指定的版本 |
| 激活 `.venv` 时 PowerShell 报错 *running scripts is disabled* | Windows 的执行策略 | 在 cmd 中使用 `activate.bat`，或者运行 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| 在 Windows 上执行 `print(qc.draw("text"))` 时出现 `UnicodeEncodeError` | 输出被重定向时（`> file`、管道、某些 IDE），Python 会使用 Windows 的 ANSI 代码页（如 cp1252），无法编码 ┌─┐ 这类边框字符 | 运行脚本前设置环境变量 `PYTHONUTF8=1`（在 notebook 中不会出现这个错误） |
| 画出的电路与书中的图不同 | 还没有 `settings.conf` | 见[配置](#配置-qiskit使电路图与书中一致)一节；结果仍然正确 |
| 测量得到的数据与保存的输出不同 | 随机采样 | 这很正常；要比较的是*结论*，而不是逐个数字 |
| 在很新的 Python 上 `pip install` 出错 | 对于太新的 Python 版本，还没有预先构建好的安装包 | 使用 Python 3.12 |
| 升级 Qiskit 后某个 notebook 报错 | 不同版本之间的 API 有变化 | 运行 `pip list`，与下方已测试的版本对照，然后附上 traceback [报告问题](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose) |

## 已测试的版本

全部 19 个 notebook 都能在以下环境中运行（2026-10-01 检查）：Python 3.11、Qiskit 2.5.2、Qiskit Aer 0.17.2、Qiskit IBM Runtime 0.50.0。CI 每周用最新版本重新运行一次，以便在新版 Qiskit 导致 notebook 出错时尽早发现。
