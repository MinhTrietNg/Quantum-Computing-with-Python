# 术语表

[Tiếng Việt](glossary.md) · [English](glossary.en.md) · **简体中文**

本页是越南语术语表的中文版。每个条目给出中文术语（括号里依次是英文原文和斜体的越南语说法；越南语与英文相同时只写英文）、简短定义，以及可以深入学习的位置。附上越南语说法，是为了方便你对照阅读越南语指南。符号 $|\cdot\rangle$ 读作“ket”。用 `Ctrl+F` 可以快速查找。带有 *（稍后再读）* 标记的条目是进阶概念，刚入门时不必弄懂。遇到这里没有收录的词？请[提交 issue](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose)，我们会补充。

学习位置的缩写：**P01** = [第 01 部分](../chapters/01_classical_computing/README.zh-CN.md)，**P02** = [第 02 部分](../chapters/02_quantum_computing/README.zh-CN.md)，**P03** = [第 03 部分](../chapters/03_quantum_protocols/README.zh-CN.md)，**P04** = [第 04 部分](../chapters/04_quantum_algorithms/README.zh-CN.md)。

## 需要用到的数学

| 术语 | 含义 | 学习位置 |
|---|---|---|
| 向量（vector） | 一组有顺序的数，例如 $(1, 0)$。比特和量子比特都写成向量 | P01 |
| 矩阵（matrix，*ma trận*） | 由数排成的表格；矩阵乘以向量，会把一个向量变成另一个向量。每个门都是一个矩阵 | P01 |
| 复数（complex number，*số phức*） | 形如 $a + bi$ 的数，其中 $i^2 = -1$；$a$ 是实部，$b$ 是虚部。量子比特的概率幅可以是复数 | P02 |
| 复数的模（modulus，*môđun (độ lớn) của số phức*） | 即复数的大小：$\vert a + bi \vert = \sqrt{a^2 + b^2}$；例如 $\vert 3 + 4i \vert = 5$ | P02 |
| 异或 $\oplus$（XOR） | 把两个比特相加并舍去进位：$0 \oplus 0 = 0$，$0 \oplus 1 = 1$，$1 \oplus 1 = 0$ | P01 |
| 常数函数 / 平衡函数（constant / balanced function，*hàm hằng / hàm cân bằng*） | 定义在比特串上的函数 $f$：如果对所有输入都给出同一个值，就是*常数*函数；如果恰好对一半输入给出 0、对另一半给出 1，就是*平衡*函数 | P04 |
| 期望值（expectation value，*giá trị kỳ vọng*） | 把测量重复非常多次时得到的平均值 | P02 |

## 基础

| 术语 | 含义 | 学习位置 |
|---|---|---|
| 比特（bit） | 经典信息的单位，取值为 0 或 1 | P01 |
| 量子比特（qubit） | 量子信息的单位；其状态为 $\alpha\vert 0\rangle + \beta\vert 1\rangle$ | P02 |
| 右矢 $\vert \psi\rangle$（ket） | 狄拉克（Dirac）符号中表示（列）态矢量的记号。$\vert 0\rangle$ 是列向量 $(1, 0)$，$\vert 1\rangle$ 是列向量 $(0, 1)$（简写为 $(1, 0)^T$：字母 $T$ 表示排成一列） | P01, P02 |
| 概率幅（amplitude，*biên độ*） | 每个基态前面的复数系数。它的模的平方就是测得该状态的概率 | P02 |
| 叠加（superposition，*chồng chập*） | 由多个基态组合而成的状态，例如 $\tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$ | P02 |
| $\vert +\rangle$ 态、$\vert -\rangle$ 态（plus / minus state，*trạng thái +, −*） | 两个等权叠加态：$\vert +\rangle = \tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$，$\vert -\rangle = \tfrac{1}{\sqrt2}(\vert 0\rangle - \vert 1\rangle)$；两者只在相对符号上不同 | P02 |
| 测量（measurement，*đo*） | 从量子比特中取出一个经典比特，得到各结果的概率由概率幅的模的平方给出；测量后量子比特变成刚测得的那个状态 | P02 |
| 基（basis，*cơ sở*） | 用作“坐标轴”、用来测量或表示状态的一组状态，例如基 $\{\vert 0\rangle,\vert 1\rangle\}$ 或 $\{\vert +\rangle,\vert -\rangle\}$ | P02 |
| 相位（phase，*pha*） | 复数概率幅的角度。全局相位无法测量；而各概率幅之间的*相对*相位决定了干涉 | P02 |
| 干涉（interference，*giao thoa*） | 概率幅之间相互加强或相互抵消。它与纠缠一起，是量子算法威力的关键 | P02, P04 |
| 布洛赫球（Bloch sphere） | 表示单个量子比特所有纯态的球面；$\vert 0\rangle$ 位于北极，$\vert 1\rangle$ 位于南极 | P02 |
| 张量积 / 克罗内克积（tensor product / Kronecker product，*tích tensor / Kronecker*） | 把多个系统的状态和门组合起来的方法：$\vert 0\rangle \otimes \vert 1\rangle = \vert 01\rangle$ | P01, P02 |
| 态矢量（statevector） | 包含 $n$ 量子比特系统全部概率幅的向量（共 $2^n$ 个复数） | P02 |
| 可观测量（observable） *（稍后再读）* | 可以测量的物理量，用厄米（Hermitian）矩阵表示；它的本征值就是可能得到的测量结果 | P02 |

## 门与电路

| 术语 | 含义 | 学习位置 |
|---|---|---|
| 门（gate，*cổng*） | 作用在量子比特上的变换；量子门是*酉*矩阵 | P02 |
| 酉矩阵（unitary） *（稍后再读）* | 满足 $U^\dagger U = I$ 的矩阵 $U$（$U^\dagger$ 是先转置、再取复共轭得到的矩阵）；它保持总概率不变，并且总是可逆的 | P02 |
| 可逆（reversible，*khả nghịch*） | 可以从输出反推出输入。所有量子门都是可逆的 | P01 |
| X 门（X gate，*cổng X*） | 量子版的“非”（NOT）：互换 $\vert 0\rangle \leftrightarrow \vert 1\rangle$ | P01, P02 |
| 哈达玛门 H（Hadamard gate，*cổng Hadamard*） | 把 $\vert 0\rangle$ 变为 $\tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$；最常用来制造叠加的门 | P02 |
| 泡利门 X、Y、Z（Pauli gates，*cổng Pauli*） | 三个基本的单量子比特门，分别相当于绕布洛赫球的 $x, y, z$ 轴旋转半圈，即 $\pi$（相差一个无法测量的全局相位） | P02 |
| 相位门 P、S、T（phase gates，*cổng pha*） | 只改变 $\vert 1\rangle$ 的相位；S 对应 $\tfrac{\pi}{2}$，T 对应 $\tfrac{\pi}{4}$ | P02 |
| 受控非门（CX / CNOT） | 双量子比特受控门：控制量子比特为 1 时，翻转目标量子比特。它是制造纠缠的主要门 | P01, P02 |
| 托佛利门（CCX / Toffoli） | 当**两个**控制量子比特都为 1 时，翻转目标量子比特 | P01 |
| SWAP 门（SWAP） | 交换两个量子比特的状态。它把积态变成积态，因此本身不会产生纠缠 | P02 |
| 屏障线（barrier，*vạch ngăn*） | 电路图上的标记（画作 `░`），用来把门分组以便阅读，不改变状态；`measure_all()` 会在测量之前自动插入一条 | P02, [介绍页](what-is-quantum-computing.zh-CN.md) |
| 量子电路（quantum circuit，*mạch lượng tử*） | 作用在量子比特上的一系列门和测量，从左往右画 | P02 |
| Clifford 门（Clifford gates，*cổng Clifford*） *（稍后再读）* | 由 H、S、CX 生成的一组门。只由这些门组成的电路可以在普通计算机上高效模拟（Gottesman–Knill 定理） | P02 |
| 通用门集（universal gate set，*bộ cổng phổ quát*） | 足以近似任意量子变换的一组门，例如 Clifford + T | P02 |

## 量子现象

| 术语 | 含义 | 学习位置 |
|---|---|---|
| 纠缠（entanglement，*vướng víu*） | 无法写成各个量子比特状态之积的多量子比特状态；对于纯态，它总会产生违反某个贝尔不等式的关联（比任何经典模型都强） | P02 |
| 贝尔态（Bell state，*trạng thái Bell*） | 四个双量子比特纠缠态，例如 $\tfrac{1}{\sqrt2}(\vert 00\rangle + \vert 11\rangle)$ | P02 |
| GHZ 态、W 态（GHZ, W） | 两类由三个或更多量子比特构成的纠缠态，二者的纠缠方式不同 | P02 |
| 贝尔不等式 / CHSH（Bell inequality / CHSH，*bất đẳng thức Bell / CHSH*） | 任何经典模型（结果“事先规定好”）的关联都必须遵守的界限。纠缠的量子比特会违反它，所以纠缠不同于两枚事先配好的硬币。*本书尚未涉及* | — |
| 不确定性原理（uncertainty principle，*nguyên lý bất định*） | 像 X 和 Z 这样的两个量（*不对易*：交换测量顺序，结果就会不同）不可能同时具有确定的值 | P03 |
| 不可克隆定理（no-cloning） | 无法复制一个未知的量子态 | P02 |
| 退相干（decoherence，*mất kết hợp*） | 噪声的一种：量子比特因与环境相互作用而失去量子特性 | [介绍页](what-is-quantum-computing.zh-CN.md) |
| 噪声（noise，*nhiễu*） | 硬件不完美导致的各种随机偏差：退相干、门错误、读出错误 | P01（概率比特），[介绍页](what-is-quantum-computing.zh-CN.md) |

## 工具

| 术语 | 含义 |
|---|---|
| notebook（`.ipynb`） | 由文字单元格和可运行的代码单元格组成的文档，可以用 Jupyter、VS Code 或 Colab 打开 |
| 单元格（cell，*ô*） | notebook 中的一个块；按 `Shift+Enter` 运行代码单元格 |
| 内核（kernel） | 在 notebook 背后负责运行各个单元格的 Python 程序；需要选对内核（`.venv` 里的那个） |
| 虚拟环境（virtual environment，`venv`，*môi trường ảo*） | `.venv` 文件夹，存放本仓库专用的 Python 和库，与电脑上的其他部分隔离开 |
| 终端（terminal） | 输入命令的窗口（Windows 上是 PowerShell，macOS 上是 Terminal） |

## 越南语中的其他叫法

同一个概念在不同的越南语资料里可能有不同的译法。查找越南语资料时，可以参考这张表。

| 本仓库（越南语指南）的用法 | 其他常见说法 |
|---|---|
| Vướng víu（纠缠，entanglement） | rối lượng tử, vướng mắc lượng tử |
| Chồng chập（叠加，superposition） | chồng chất, chồng chập lượng tử |
| Qubit（量子比特） | bit lượng tử |
| Mặt cầu Bloch（布洛赫球，Bloch sphere；越南语指南通常直接保留英文名） | quả cầu Bloch |
| Môđun（模） | mô-đun |
| Tích tensor（张量积） | tích Kronecker（克罗内克积；原书使用这个名称，所以第 01 和第 02 部分也沿用它，尤其是在讲矩阵时） |
| Biên độ（概率幅） | biên độ xác suất |

## 协议与算法

| 术语 | 含义 | 学习位置 |
|---|---|---|
| 量子隐形传态（teleportation，*dịch chuyển trạng thái lượng tử*） | 借助一对纠缠量子比特再加上**两个经典比特**，传送一个量子比特的未知状态。它不能比光更快地传送 | P03 |
| 超密编码（superdense coding，*mã hóa siêu đặc*） | 借助事先共享的一对纠缠量子比特，只发送**一个量子比特**就能传递**两个经典比特** | P03 |
| 预言机 $U_f$（oracle） | 计算函数 $f$ 的量子“黑盒”：$U_f\vert x\rangle\vert y\rangle = \vert x\rangle\vert y \oplus f(x)\rangle$ | P02, P04 |
| 相位反冲（phase kickback） | 当目标量子比特处于 $\vert -\rangle$ 时，预言机会把函数值 $f(x)$ 变成控制量子比特上的符号 $(-1)^{f(x)}$ | P02 |
| 查询复杂度（query complexity，*độ phức tạp truy vấn*） | 算法需要调用预言机的次数；第 04 部分用它作为比较的标准 | P04 |
| Deutsch–Jozsa 算法、Bernstein–Vazirani 算法、西蒙算法（Deutsch–Jozsa, Bernstein–Vazirani, Simon） | 三个在人为构造的问题上运行的著名查询算法。前两个算法的优势很小，或者只是相对于确定性的经典算法而言；西蒙算法则具有指数级优势（在预言机模型中） | P04 |
| 格罗弗算法（Grover） | 无结构搜索，只需 $\sim\sqrt N$ 次查询，而不是 $\sim N$ 次 | P04 |
| 肖尔算法（Shor） | 在多项式时间内把整数分解为质因数。*本书尚未涉及* | — |
| QFT、QPE | 量子傅里叶变换（quantum Fourier transform）和相位估计（phase estimation），是肖尔算法的两个构建模块。*本书尚未涉及* | — |

## 复杂度与密码学

这些概念用于[介绍页](what-is-quantum-computing.zh-CN.md)和[常见问题](faq.zh-CN.md)；原书尚未讲授。

| 术语 | 含义 |
|---|---|
| 多项式时间 / 超多项式时间（polynomial / super-polynomial time，*thời gian đa thức / siêu đa thức*） | 计算步数随输入规模按某个固定幂次增长（多项式，通常被视为“快”），或者增长得比任何这样的幂次都快（超多项式，例如指数） |
| NP 完全（NP-complete，*NP-đầy-đủ*） | NP 中“最难”的一类问题：只要能在多项式时间内解出一个 NP 完全问题，就能解出 NP 中的所有问题。至今没有人知道是否存在快速算法（P 与 NP 问题） |
| 公钥密码学 RSA、ECC（public-key cryptography，*mật mã khoá công khai*） | 用于密钥交换和数字签名的密码，其安全性依赖于整数分解（RSA）或*离散对数*（ECC、Diffie–Hellman）的困难性 |
| 离散对数（discrete logarithm，*logarithm rời rạc*） | 由 $g^x \bmod p$ 求出 $x$ 的问题（或椭圆曲线上的类似运算）；普通计算机还没有快速的解法，肖尔算法能在多项式时间内解决它 |
| 后量子密码学（post-quantum cryptography，*mật mã hậu lượng tử*） | 运行在普通计算机上、但设计为也能抵御量子计算机的密码算法，例如 ML-KEM（FIPS 203）和 ML-DSA（FIPS 204） |
| 量子密钥分发（QKD，*phân phối khoá lượng tử*） | 利用量子物理让双方共享秘密密钥；与后量子密码学不同，它需要专用设备 |
| “先收集、后解密”（harvest now, decrypt later） | 攻击者今天先收集加密数据，等以后有了足够强大的量子计算机再解密 |

## 硬件与实际运行

| 术语 | 含义 | 学习位置 |
|---|---|---|
| NISQ（含噪声中等规模量子） | Noisy Intermediate-Scale Quantum：指当今的量子计算机，量子比特数量不少，但有噪声，也尚未实现足够规模的纠错 | — |
| 物理量子比特 / 逻辑量子比特（physical / logical qubit，*qubit vật lý / qubit logic*） | 物理量子比特是真实的硬件元件，带有噪声；逻辑量子比特是借助纠错、编码在多个物理量子比特上的“虚拟”量子比特，错误更少 | — |
| 量子纠错（error correction，*sửa lỗi lượng tử*） | 用多个物理量子比特构造出一个错误更少的逻辑量子比特 | — |
| 量子处理器（QPU） | Quantum Processing Unit：真实的量子芯片 | 第 00 部分 |
| 模拟器（simulator） | 在普通计算机上模拟量子计算机的程序（如 `AerSimulator`） | 第 00 部分 |
| shot | 运行一次电路并进行测量；运行 $N$ 个 shot 就能得到结果的分布 | P02 |
| 计数（counts） | 统计各个 shot 测量结果的表，例如 `{'00': 504, '11': 496}` | P02 |
| 小端序（little-endian） | Qiskit 的约定：在结果比特串中，量子比特 0 位于**最右边** | [安装与运行](setup.zh-CN.md) |
