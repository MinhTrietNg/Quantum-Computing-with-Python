# Quantum Computing with Python

[Tiếng Việt](README.md) · [English](README.en.md) · **简体中文**

[![Notebooks](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/actions/workflows/notebooks.yml/badge.svg)](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/actions/workflows/notebooks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-6929C4)

**用 Python 从零开始学习量子计算**。完全免费。不需要懂量子物理，不需要量子计算机，普通笔记本电脑就能运行。只需要掌握 **Python 基础**；数学知识会循序渐进地讲解。

坚持学习约 4–6 周（估计值，按每天一小时计）之后的目标：理解量子比特（qubit）、叠加（superposition）、纠缠（entanglement）和干涉（interference）是什么，能用 Qiskit 自己编写并运行量子电路（quantum circuit），并能解释量子隐形传态（quantum teleportation）以及 Deutsch–Jozsa、Bernstein–Vazirani、西蒙（Simon）和格罗弗（Grover）算法。

## 立即体验

下面就是一个完整的量子程序。它让两个量子比特进入**纠缠**状态，然后对它们测量 1000 次：

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)             # H 门：把 0 号 qubit（量子比特）置于 0 和 1 各占 50/50 的状态
qc.cx(0, 1)         # CX 门：把 1 号量子比特与 0 号量子比特绑定在一起（纠缠）
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
# {'11': 496, '00': 504}
```

`shots=1000` 表示把电路运行并测量 1000 次；由于测量（measurement）是随机的，你得到的数字会和上面略有不同。结果只会是 `00` 或 `11`，**永远不会**是 `01` 或 `10`：单看每个量子比特，结果都是 50/50 随机的，但两个量子比特的结果总是相同。（真实的量子计算机有噪声，所以偶尔会混进几个 `01`/`10`；理想的模拟器则不会。）为什么会这样？为什么仅凭这一点*还不足以*说明它是“量子”的？纠缠在第 02 部分讲解；完整的证据（贝尔不等式，Bell inequality）原书还没有写，请参阅[资源](docs/resources.zh-CN.md)。

**还没安装 Qiskit**？打开 [Google Colab](https://colab.research.google.com)，选择 *New notebook*，在一个单元格（cell）中运行 `%pip install -q qiskit qiskit-aer`，然后把上面的代码粘贴到一个新的单元格中。如果要在自己的电脑上安装，请看[开始使用](#开始使用)一节。

**下一步**：
[什么都没装？用 Google Colab 运行](docs/setup.zh-CN.md#2-google-colab无需安装) ·
[阅读 15 分钟入门介绍](docs/what-is-quantum-computing.zh-CN.md) ·
[查看学习路线](docs/learning-path.zh-CN.md)

## 适合哪些读者

| 你是 | 从这里开始 |
|---|---|
| **好奇，但还没学过编程** | [量子计算机是什么？](docs/what-is-quantum-computing.zh-CN.md)，15 分钟，数学很少（只有分数和平方根）；然后看[学习路线](docs/learning-path.zh-CN.md) |
| **掌握 Python 基础** | [学习路线](docs/learning-path.zh-CN.md)，然后从[第 00 部分](chapters/00_getting_started/)开始 |
| **会 Python，也学过线性代数** | [学习路线](docs/learning-path.zh-CN.md)介绍了如何快速浏览第 01 部分、直接进入第 02 部分 |
| **学过量子力学** | 阅读 [02_01](chapters/02_quantum_computing/) 的*核心代码*部分（第一个 Qiskit 电路），然后看 02_04、02_05 和[第 04 部分](chapters/04_quantum_algorithms/)（如果对单量子比特门的语法还不熟悉，再浏览一下 02_03） |
| 查术语 | [术语表](docs/glossary.zh-CN.md) |
| 想知道量子计算机能不能破解加密 | [FAQ](docs/faq.zh-CN.md#关于密码学) |

## 开始使用

有三种方式，从最简单到最完整（[详细指南](docs/setup.zh-CN.md)）：

1. **只阅读**：打开下方的[目录](#目录)，选一课。GitHub 会直接显示 notebook 以及其中已保存的输出。
2. **在 Google Colab 上运行**：无需安装任何东西（[操作方法](docs/setup.zh-CN.md#2-google-colab无需安装)）。
3. **在自己的电脑上运行**（需要 Python 3.11 或更高版本；本仓库已用 3.11 和 3.12 测试）：

   ```bash
   git clone https://github.com/MinhTrietNg/Quantum-Computing-with-Python.git
   cd Quantum-Computing-with-Python
   python -m venv .venv
   # Windows (PowerShell): .venv\Scripts\Activate.ps1   |   Windows (cmd): .venv\Scripts\activate.bat
   # macOS/Linux:          source .venv/bin/activate
   pip install -r requirements.txt
   jupyter notebook chapters/
   ```

   遇到问题（还没有 Python、PowerShell 报错、不用 git 等）？请看[详细指南与问题排查](docs/setup.zh-CN.md)。

全部 19 个 notebook 都已测试可以运行（[具体版本](docs/setup.zh-CN.md#已测试的版本)），CI 每周还会重新检查一次。

## 学习路线

按**第 00 → 01 → 02 → 03 → 04 部分**的顺序阅读，认真学习大约需要 25–40 小时（每天一小时，约 4–6 周）。[学习路线](docs/learning-path.zh-CN.md)里有路线图、各部分的预计用时、附参考答案的自测题，以及已有基础时可以走的捷径。

每个部分都有单独的讲解（越南语原文，另有英文和简体中文译本），包括核心知识、核心代码、运行结果，以及便于复习的**速记要点**。

## 目录

| 部分 | 课 | Notebook | 内容 |
|---|---|---|---|
| **[00 · Getting started](chapters/00_getting_started/)** | 00_00 | [About the textbook](chapters/00_getting_started/00_00_welcome.ipynb) | 本书的用法、引用方式 |
| | 00_01 | [Setting up your environment](chapters/00_getting_started/00_01_setting_env.ipynb) | 安装 Qiskit、检查环境的代码 |
| | 00_02 | [Configuring Qiskit](chapters/00_getting_started/00_02_qiskit_config.ipynb) | IBM Quantum 令牌（token）、`settings.conf` |
| **[01 · Classical computing](chapters/01_classical_computing/)** | 01_01 | [Bits and digital circuits](chapters/01_classical_computing/01_01_bits_and_circuits.ipynb) | 比特、逻辑门（logic gate）、加法器（adder） |
| | 01_02 | [Reversible computing](chapters/01_classical_computing/01_02_reversible_computing.ipynb) | 可逆（reversible）门 X、CX、CCX |
| | 01_03 | [Linear algebra for reversible circuits](chapters/01_classical_computing/01_03_bits_to_vectors.ipynb) | 比特是向量，门是矩阵，张量积（tensor product） |
| | 01_04 | [Probabilistic computing](chapters/01_classical_computing/01_04_probabilistic_circuits.ipynb) | 概率比特（p-bit）、含噪声的电路 |
| **[02 · Quantum computing](chapters/02_quantum_computing/)** | 02_01 | [Qubits and quantum circuits](chapters/02_quantum_computing/02_01_bits_to_qubits.ipynb) | 施特恩–格拉赫实验（Stern–Gerlach experiment），从比特到量子比特 |
| | 02_02 | [Quantum entanglement](chapters/02_quantum_computing/02_02_entanglement.ipynb) | 可分离态与纠缠态；用 H + CX 产生纠缠 |
| | 02_03 | [Single-qubit systems](chapters/02_quantum_computing/02_03_single_qb_sys.ipynb) | 复概率幅（amplitude）、布洛赫球（Bloch sphere）、单量子比特门、测量、可观测量（observable） |
| | 02_04 | [Multi-qubit systems](chapters/02_quantum_computing/02_04_multi_qb_sys.ipynb) | 受控门、SWAP、不可克隆（no-cloning）、通用门集、部分测量 |
| | 02_05 | [Quantum building blocks](chapters/02_quantum_computing/02_05_quantum_blocks.ipynb) | Bell/GHZ/W 态、哈达玛变换（Hadamard transform）、相位反冲（phase kickback）、预言机（oracle） |
| **[03 · Quantum protocols](chapters/03_quantum_protocols/)** | 03_01 | [Uncertainty & quantum money](chapters/03_quantum_protocols/03_01_quantum_money.ipynb) | 不确定性原理（uncertainty principle）；Wiesner 量子货币：量子比特越多越难伪造 |
| | 03_02 | [Quantum teleportation](chapters/03_quantum_protocols/03_02_teleportation.ipynb) | 量子隐形传态 |
| | 03_03 | [Superdense coding](chapters/03_quantum_protocols/03_03_superdense_coding.ipynb) | 用 1 个量子比特发送 2 个经典比特 |
| **[04 · Foundational quantum algorithms](chapters/04_quantum_algorithms/)** | 04_01 | [Deutsch–Jozsa](chapters/04_quantum_algorithms/04_01_deutsch-jozsa.ipynb) | 常数函数还是平衡函数，1 次查询 |
| | 04_02 | [Bernstein–Vazirani](chapters/04_quantum_algorithms/04_02_bernstein-vazirani.ipynb) | 找出秘密字符串，1 次查询 |
| | 04_03 | [Simon's algorithm](chapters/04_quantum_algorithms/04_03_simons.ipynb) | 寻找 XOR 周期，指数级加速（在预言机模型中） |
| | 04_04 | [Grover's algorithm](chapters/04_quantum_algorithms/04_04_grover.ipynb) | 无结构搜索，平方根级加速 |

### 原书中尚无内容的章节

在原书中，以下章节目前只有标题（notebook 是空的），因此**尚未收录**到本仓库。作者写完后，本仓库会随之更新；在此之前，可以先看看[进阶学习资源](docs/resources.zh-CN.md)。

| 部分 | 章节 |
|---|---|
| 03 · Quantum protocols | 03_04 Bell inequalities, 03_05 Quantum key distribution |
| 05 · Important quantum primitives | 05_01 QFT, 05_02 QPE, 05_03 Amplitude amplification |
| 06 · Advanced quantum algorithms | 06_01 Shor, 06_02 HHL, 06_03 Hamiltonian simulation |

## 配套文档

| | |
|---|---|
| [量子计算机是什么？](docs/what-is-quantum-computing.zh-CN.md) | 整体概览、干涉、纠缠，以及它擅长什么、不擅长什么 |
| [学习路线](docs/learning-path.zh-CN.md) | 需要先掌握什么、预计用时、各部分的自测题 |
| [安装与运行](docs/setup.zh-CN.md) | 只阅读、用 Colab 还是在本地运行；常见问题排查 |
| [术语表](docs/glossary.zh-CN.md) | 越南语–英语术语对照，并注明在哪里学到 |
| [FAQ](docs/faq.zh-CN.md) | 常见误解、密码学、如何选择库 |
| [资源](docs/resources.zh-CN.md) | 书籍、课程、进阶学习资料 |
| [ERRATA](ERRATA.zh-CN.md) | 原书中的已知错误 |

## 来源与更新

[chapters/](chapters/) 中的 notebook 和图片是开放教材 **[Learn Quantum Computing using Python](https://learnquantum.io)**（Diego Emilio Serrano 著）的**原样副本**，包括作者运行后保存的输出，以及原书中的几处小错误（已记录在 [ERRATA](ERRATA.zh-CN.md) 和各部分 README 的 `> 注意` 条目中，你无需自己去发现）。本仓库自己编写的部分是各部分的越南语 README（及其英文和简体中文译本）、[docs/](docs/) 目录、自动化测试以及配套工具。

| | |
|---|---|
| 上游仓库 | [learn-quantum/lqc-textbook](https://github.com/learn-quantum/lqc-textbook) |
| 副本来源 | commit [`7abf73c`](https://github.com/learn-quantum/lqc-textbook/commit/7abf73cb1d430e0eba1d052d8b4d8bc976e956f6)（2026-03-20），于 2026-09-30 获取 |

想知道上游有什么更新，请运行 `python scripts/check_upstream.py`。更新流程见 [CONTRIBUTING](CONTRIBUTING.zh-CN.md#从上游更新)。

## 仓库结构

```text
.
├── chapters/             # 教材：每个部分一个文件夹（越南语 README 及 2 个译本 + notebook + images/）
├── docs/                 # 入门文档：介绍、学习路线、安装、术语、FAQ、资源
├── scripts/              # check_upstream.py（与上游仓库比较）、check_links.py、check_doc_snippets.py、check_translations.py
├── .github/              # 运行 notebook 的 CI，issue 和 pull request 模板
├── ERRATA.md, CONTRIBUTING.md, CITATION.cff, LICENSE   # 每个 .md 文件都有 .en.md 和 .zh-CN.md 译本
├── qiskit_settings.conf  # 让显示效果与书中一致的配置
└── requirements.txt, requirements-dev.txt, pyproject.toml
```

## 语言

本指南提供三种语言，内容相互对应。[chapters/](chapters/) 中的 notebook 和图片是原书的英文原版，三种语言共用。

| 语言 | 从这里开始 |
|---|---|
| Tiếng Việt（越南语，本仓库的原文） | [README.md](README.md) |
| English | [README.en.md](README.en.md) |
| 简体中文（Chinese, Simplified） | [README.zh-CN.md](README.zh-CN.md) |

每个 `.md` 文件旁边都有两个译本，分别命名为 `<名称>.en.md` 和 `<名称>.zh-CN.md`（见[翻译约定](CONTRIBUTING.zh-CN.md#翻译英文与简体中文)）。

## 参与贡献

欢迎任何意见和建议：修正翻译错误、改进不够清楚的解释、为初学者补充资料、报告书中的错误，或者报告在新版 Qiskit 上无法运行的 notebook。详见 [CONTRIBUTING](CONTRIBUTING.zh-CN.md)。原书本身的错误，最好也到[上游仓库的 Issues](https://github.com/learn-quantum/lqc-textbook/issues) 报告。

## 许可证与引用

notebook 和插图 © 2024 Diego Emilio Serrano，以 [MIT License](LICENSE) 发布。讲解（越南语原文及其译本）和配套文档以相同的许可证共享。使用本内容时，请引用原书（GitHub 会根据 [CITATION.cff](CITATION.cff) 显示 *Cite this repository* 按钮）：

```bibtex
@book{learn-quantum,
    author = {Diego Emilio Serrano},
    year = {2024},
    title = {Learn Quantum Computing using Python},
    publisher = {Github},
    url = {learnquantum.io},
}
```

感谢作者 Diego Emilio Serrano 编写并免费分享这本书。
