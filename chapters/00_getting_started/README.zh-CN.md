# 00 · Getting started（准备环境）

[Tiếng Việt](README.md) · [English](README.en.md) · **简体中文**

安装 Python 环境来运行书中的 notebook，配置 Qiskit 让绘出的图与书中一致，并（可选）关联 IBM Quantum 账户，以便在真实的量子计算机上运行。

> 来源：[About](https://learnquantum.io/chapters/00_getting_started/00_00_welcome.html) · [Setting your environment](https://learnquantum.io/chapters/00_getting_started/00_01_setting_env.html) · [Configuring Qiskit](https://learnquantum.io/chapters/00_getting_started/00_02_qiskit_config.html) — Diego Emilio Serrano, learnquantum.io, MIT License.

## 目录

| 课 | Notebook | 网页 | 要点 |
|---|---|---|---|
| 00_00 · About | [00_00_welcome.ipynb](00_00_welcome.ipynb) | [链接](https://learnquantum.io/chapters/00_getting_started/00_00_welcome.html) | 本书的使用方法、在哪里提问、如何引用 |
| 00_01 · Setting your environment | [00_01_setting_env.ipynb](00_01_setting_env.ipynb) | [链接](https://learnquantum.io/chapters/00_getting_started/00_01_setting_env.html) | 安装 Python、Jupyter、Qiskit、Aer、IBM Runtime；运行检查代码 |
| 00_02 · Configuring Qiskit | [00_02_qiskit_config.ipynb](00_02_qiskit_config.ipynb) | [链接](https://learnquantum.io/chapters/00_getting_started/00_02_qiskit_config.html) | 保存 IBM Quantum token；用 `settings.conf` 文件设置显示方式 |

## 00_00 · About the textbook（本书简介）

这本书有两种用法：在网页上阅读，再把代码复制到自己的环境中；或者从 [learn-quantum/lqc-textbook](https://github.com/learn-quantum/lqc-textbook) 仓库下载 notebook。本仓库采用第二种方式：notebook 都放在 `chapters/` 目录下。

- 提问交流：上游仓库的 [Discussions](https://github.com/learn-quantum/lqc-textbook/discussions) 页面。
- 报告错别字、bug：[Issues](https://github.com/learn-quantum/lqc-textbook/issues) 页面。
- 引用格式：Serrano, D.E. (2024). *Learn Quantum Computing using Python*. https://learnquantum.io.

## 00_01 · Setting up your environment（搭建环境）

**目标**：拥有一个独立的 Python 环境，并装好运行所有 notebook 所需的库。

### 需要安装的包及其作用

| 包 | 作用 |
|---|---|
| `notebook`（Jupyter） | 打开并运行各章内容（各章本身就是以 notebook 形式编写的） |
| `qiskit[visualization]` | 核心库：创建、模拟和运行量子电路（quantum circuit）；会连带安装 NumPy、SymPy、Matplotlib |
| `qiskit-aer` | 高性能模拟器（simulator），支持噪声模拟（noisy simulator） |
| `qiskit-ibm-runtime` | 连接 IBM 的真实量子处理器（QPU，quantum processing unit）；还提供可以配合模拟器使用的 `Estimator` |

### 安装

原书使用 `conda`，本仓库使用 `venv`，两者效果相同：

```bash
# conda (原书的做法)
conda create --name learn-quantum python=3
conda activate learn-quantum
pip install "qiskit[visualization]" qiskit-aer qiskit-ibm-runtime notebook

# 或者用 venv (本仓库的做法): 在仓库根目录下运行
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1   |   Windows (cmd): .venv\Scripts\activate.bat
# macOS/Linux:          source .venv/bin/activate
pip install -r requirements.txt
```

激活之后，环境名会显示在命令行开头：conda 显示 `(learn-quantum)`，venv 显示 `(.venv)`。运行 `pip install` 之前请先确认这一点。

<p align="center"><img src="images/00_01_02_terminal_window_learn.png" width="350" alt="终端窗口：第一行的前缀是 (base)，执行 conda activate learn-quantum 后前缀变为 (learn-quantum)"></p>

*图：激活之前，命令行以 `(base)` 开头；执行 `conda activate learn-quantum` 之后变为 `(learn-quantum)`。*

> 注意：在 macOS（zsh）上必须给 `qiskit[visualization]` 加上引号，因为 zsh 会把 `[...]` 当作文件名匹配模式。在 Windows 和 bash 上则不需要。

### 检查环境的代码

这段代码用到了 `display(...)`，所以必须在 **notebook 的单元格**（Jupyter 或 VS Code）中运行，不能用 `python 文件名.py` 来运行。

```python
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_distribution
from qiskit_aer import AerSimulator

simulator = AerSimulator()

qc = QuantumCircuit(2,2)
qc.rx(np.pi/2,1)
qc.cx(1,0)
print("Statevector:")
display(Statevector(qc).draw('latex'))

qc.measure([1,0],[1,0])

print("Circuit:")
display(qc.draw('mpl'))

qc_t = transpile(qc, simulator)
counts = simulator.run(qc, shots=2**10).result().get_counts()

print("Probability Distribution:")
plot_distribution(counts)
```

这段代码用到了许多贯穿全书的组件。**你暂时不必弄懂它们**：现在只要能运行就行，每个概念都会在第 01–02 部分详细讲解。下表供你好奇时查阅。

| 代码行 | 含义 |
|---|---|
| `QuantumCircuit(2,2)` | 含 2 个量子比特（qubit）的电路，另有 2 个经典比特用来保存测量结果 |
| `qc.rx(np.pi/2,1)` | 让量子比特 1 绕 X 轴旋转 π/2，产生叠加（superposition） |
| `qc.cx(1,0)` | 受控非门（CNOT）：量子比特 1 为控制位（control），量子比特 0 为目标位（target），产生纠缠（entanglement） |
| `Statevector(qc).draw('latex')` | 精确计算态矢量（statevector），以 ket 形式显示 |
| `qc.measure([1,0],[1,0])` | 测量：量子比特 1 → 比特 1，量子比特 0 → 比特 0 |
| `transpile(qc, simulator)` | 把电路转换为后端（backend）所支持的门集合 |
| `simulator.run(qc, shots=2**10)` | 运行 1024 次，`get_counts()` 返回每种结果出现的次数 |
| `plot_distribution(counts)` | 绘制概率分布 |

**预期结果**：量子态的形式为 $\tfrac{1}{\sqrt{2}}(|00\rangle - i|11\rangle)$，所以只会测到 `00` 和 `11`，各占约 50%。其中 $i$ 是虚数单位，将在 02_03 中学习；系数 $-i$ 只是一个相位（phase），不会改变这次测量的概率。notebook 中保存的输出为 `00` ≈ 0.493、`11` ≈ 0.507；你自己运行的结果会略有不同。代码运行不报错，就说明环境已经就绪。不过这段代码并没有检查 `qiskit-ibm-runtime`（notebook 中也这样说明）；这个包要到 00_02 以及调用 `Estimator` 时才会用到。

> 注意：代码创建了 `qc_t = transpile(...)`，运行的却是 `simulator.run(qc, ...)`，而不是 `qc_t`。在 AerSimulator 上这样也能运行，因为 Aer 本身就支持这些门；在真实硬件上则需要运行经过 transpile 的电路。

## 00_02 · Configuring Qiskit（配置 Qiskit）

下面两步都是**可选的**。

### 1. 关联 IBM Quantum 账户（仅在真机上运行时需要）

1. 在 https://quantum.ibm.com/ 注册账户，登录后复制主页右上角的 API token。

   <p align="center"><img src="images/00_02_01_api_token.png" width="700" alt="IBM Quantum Platform 主页，右上角有 API Token 框和复制按钮"></p>

   *图：IBM Quantum Platform 主页上的 API Token 框（旧版界面，即原书写作时的样子）；复制按钮就在 token 框旁边。*

2. 运行一次：

   ```python
   from qiskit_ibm_runtime import QiskitRuntimeService
   QiskitRuntimeService.save_account('your-token-here')
   ```

token 会保存在 `C:\Users\<用户名>\.qiskit\qiskit-ibm.json`（Windows）或 `~/.qiskit/qiskit-ibm.json`（macOS/Linux）中。**永远不要把 token 提交（commit）到 GitHub。**

> 注意（可能已过时）：本说明沿用原书的写法，原书指向 `quantum.ibm.com`，并且调用 `save_account` 时只传入 token。目前版本的 `qiskit-ibm-runtime` 库（0.50.0）把 `token` 描述为 *IBM Cloud API key*，可接受 `ibm_cloud` 或 `ibm_quantum_platform` 两种通道（channel），并新增了 `instance` 参数。IBM Quantum 平台也已经迁移到 `quantum.cloud.ibm.com`。如果你想在真机上运行，请按照 [quantum.cloud.ibm.com/docs](https://quantum.cloud.ibm.com/docs) 上的最新文档操作，而不是按上面的步骤。本仓库中的 notebook 都在模拟器上运行，因此不需要 token。

### 2. 配置文件 `settings.conf`（让图与原书完全一致）

创建文件 `C:\Users\<用户名>\.qiskit\settings.conf`（Windows）或 `~/.qiskit/settings.conf`（macOS/Linux）。上游仓库使用的是下面的内容（即上游仓库根目录下的 `settings.conf` 文件）；本仓库在 [qiskit_settings.conf](../../qiskit_settings.conf) 中提供了一份副本。notebook 00_02 中列出的配置略有不同：使用的是 `iqp-dark`，并且没有 `circuit_idle_wires` 这一行。

```ini
[default]
circuit_drawer = mpl
circuit_mpl_style = iqp
circuit_reverse_bits = True
circuit_idle_wires = False
state_drawer = latex
```

| 选项 | 作用 |
|---|---|
| `circuit_drawer = mpl` | 用 matplotlib 绘制电路（彩色图），而不是用文本字符 |
| `circuit_mpl_style = iqp` | IBM Quantum 配色；notebook 建议深色背景使用 `iqp-dark` |
| `circuit_reverse_bits = True` | 绘图时反转量子比特的顺序：编号最大的量子比特位于最上方 |
| `circuit_idle_wires = False` | 隐藏没有任何门的量子比特线 |
| `state_drawer = latex` | 用 LaTeX 以 ket 形式显示态矢量，而不是显示 NumPy 数组 |

> **重要：量子比特的顺序**。Qiskit 采用小端序（little-endian）约定：量子比特 0 是结果字符串中**最右边**的那一位，例如 `'01'` 表示 $q_1 = 0,\ q_0 = 1$。许多其他资料的约定正好相反。`circuit_reverse_bits = True` 只改变电路的**绘制方式**，不改变计算结果。如果不设置这个文件，你画出的电路会与书中的图上下颠倒，但数值仍然正确。

## 速记要点

- 只需要 4 个包：`qiskit[visualization]`、`qiskit-aer`、`qiskit-ibm-runtime`、`notebook`。
- 能运行环境检查代码（得到 `00`/`11` 各约 50%），就说明环境没问题（这段代码没有测试 `qiskit-ibm-runtime`）。
- IBM token 只在使用真实硬件时才需要；永远不要把 token 写进要提交的代码里。
- 想让图与原书一致：把 [qiskit_settings.conf](../../qiskit_settings.conf) 复制到 `~/.qiskit/settings.conf`。
- Qiskit 的结果字符串要从右往左读：最后一个字符是量子比特 0。

> 本 README 中的代码都是从 notebook 中**原样摘录**的。它们不依赖其他单元格中的变量，但环境检查代码因为用到了 `display(...)`，必须在 notebook 中运行。

---

<!-- nav -->
[← 学习路线](../../docs/learning-path.zh-CN.md) · [目录](../../README.zh-CN.md#目录) · [01 · Classical computing →](../01_classical_computing/README.zh-CN.md)
