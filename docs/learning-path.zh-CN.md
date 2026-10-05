# 学习路线

[Tiếng Việt](learning-path.md) · [English](learning-path.en.md) · **简体中文**

本页帮助你选择起点、了解需要先准备什么，并在学完每个部分后进行自测。还不知道量子计算机是什么？请先阅读[什么是量子计算机？](what-is-quantum-computing.zh-CN.md)（15 分钟）。

## 你该从哪里开始？

| 你是 | 建议 |
|---|---|
| **好奇，但还没学过编程** | 阅读[什么是量子计算机？](what-is-quantum-computing.zh-CN.md)和 [FAQ](faq.zh-CN.md)。然后读开放图书 *Quantum Computing for the Quantum Curious*（数学内容较少，见[资源](resources.zh-CN.md)）。如果想在不写代码的情况下浏览本仓库：阅读[第 02 部分](../chapters/02_quantum_computing/README.zh-CN.md)和[第 03 部分](../chapters/03_quantum_protocols/README.zh-CN.md)中每一课的*速记要点*；notebook 里已经保存了输出，所以无需运行任何东西。等你想写代码时，先学好 Python 基础再回来 |
| **掌握 Python 基础** | 从第 00 部分开始，按照下面的完整路线学习。这是为大多数读者准备的路线 |
| **会 Python 和线性代数**（向量、矩阵、复数） | 完成第 00 部分。第 01 部分：略读 01_01；阅读 01_02（可逆门 X、CX、CCX，它们是预言机的基础）；略读 01_03，掌握 ket 记号和克罗内克积（Kronecker product）；快速浏览 01_04（讲概率比特，02_01 会拿它与量子比特作比较）。（如果你对张量积/克罗内克积还不熟悉，请仔细阅读 01_03。）从第 02 部分开始精读 |
| **在学校学过量子力学** | 阅读 [02_01](../chapters/02_quantum_computing/README.zh-CN.md) 的*核心代码*部分，熟悉 Qiskit 编写电路的方式，然后读 02_04、02_05 和第 04 部分（如果对单量子比特门的语法还不熟悉，再略读 02_03）。把本仓库当作 Qiskit 手册来用 |

## 需要先准备什么

**真正必需的条件：Python 基础**。数学部分书中会逐步讲解：向量和矩阵在第 01 部分，复数和布洛赫球（Bloch sphere）在 02_03。如果你之前接触过这些内容，学起来会更轻松；见下面的*数学复习*一节。

| 技能 | 需要达到的程度 | 如果还比较薄弱 |
|---|---|---|
| **Python** | 变量、函数、循环、list；会用 `import`，能读懂简短的代码 | 先学一门 Python 基础课程。不需要会 NumPy；书中用到时会解释 |
| **二进制与逻辑** | 能把二进制转换为十进制；知道 AND、OR、XOR | 第 01_01 课会从头讲起 |
| **概率** | 事件的概率、所有概率之和为 1；两个独立事件的概率相乘 | 复习 10 年级（高一）的知识就够了 |
| **线性代数** | 矩阵乘以向量 | 第 01_03 课会讲；提前看看会更轻松（见*数学复习*一节） |
| **复数** | 知道 $i^2 = -1$、模 $\vert a+bi \vert$ | 02_03 会重新讲；提前看看会更轻松 |
| **量子物理** | 不需要 | 书中从施特恩–格拉赫实验（Stern–Gerlach experiment）讲起 |

### 数学复习（可选，1–3 小时）

如果你从未接触过矩阵或复数，建议先看看：

- [3Blue1Brown, *Essence of linear algebra*](https://www.3blue1brown.com/topics/linear-algebra)：一套直观讲解向量和矩阵的视频（看完前四集，也就是讲到两个矩阵相乘为止，就足够应付第 01 部分了）。
- [Khan Academy, Linear algebra](https://www.khanacademy.org/math/linear-algebra)（向量、矩阵）和 [Precalculus](https://www.khanacademy.org/math/precalculus)（复数部分）：有互动练习，免费。

### 自测（5 分钟）

不查资料，快速作答。

1. Python 代码 `for x in range(4): print(x * x)` 会打印出哪些数？
2. 二进制数 `101` 等于十进制的多少？`1 XOR 1` 呢？
3. 抛两枚均匀的硬币，两枚都是正面朝上的概率是多少？
4. 计算 $\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}$。
5. 复数 $3+4i$ 的模是多少？

**如何看结果**：第 1 题答错，建议先复习 Python。第 2 题（二进制、XOR）答错没关系：01_01 会从头讲起。第 3 题答错，建议复习一下 10 年级程度的概率知识（两个独立事件同时发生的概率），因为 01_04 和 02_02 用的正是这种计算。第 4–5 题答错**没关系**，因为书中会重新讲；但如果这两题你都觉得陌生，请看上面的*数学复习*一节。

<details>
<summary>答案</summary>

1. `0`、`1`、`4`、`9`（每个数占一行）
2. 5；而 `1 XOR 1 = 0`
3. $1/4$
4. $\begin{pmatrix}0\\1\end{pmatrix}$（这个矩阵就是 X 门，它把 $|0\rangle$ 变成 $|1\rangle$）
5. 5，因为 $\sqrt{3^2 + 4^2} = 5$

</details>

## 完整路线

<!-- translate-block -->
```text
00 安装与运行
└─> 01 经典计算（向量、矩阵）
    └─> 02 量子计算（量子比特、布洛赫球、纠缠、预言机）
        └─> 03 量子协议（量子隐形传态、超密编码）
            └─> 04 量子算法（Deutsch–Jozsa → BV → Simon → Grover）
                └─> 继续学习（QFT、Shor、VQE 等）
```

第 01 部分看起来很“经典”，但它提供的是向量、矩阵和张量积（tensor product）这套工具，后面所有部分都会反复用到。第 02_05 课讲预言机（oracle）和相位反冲（phase kickback），是整个第 04 部分的基础。

下面给出的时间是针对认真学习者的**估计**：仔细阅读、亲手把代码重敲一遍、完成自测题。快速浏览的读者可能会快得多。下面五个部分加起来约 25–40 小时（不含可选的*数学复习*），也就是说，如果每天学一小时，需要 4–6 周。

每个部分都有**自测题**和**参考答案**。请先自己作答，再展开答案。

### 第 00 部分 · 准备工作（[README](../chapters/00_getting_started/README.zh-CN.md)），约 1 小时

搭建环境，并成功运行检查代码。另见[安装与运行](setup.zh-CN.md)。

**完成后你应该能够**：在你的电脑上运行一个 notebook，并看到 `00`/`11` 大约各占 50/50 的结果。

### 第 01 部分 · 经典计算（[README](../chapters/01_classical_computing/README.zh-CN.md)），约 4–6 小时

比特、逻辑门、可逆门、把比特看作向量和把门看作矩阵、概率比特。

**自测**：
- 为什么 AND 门不可逆，而 CX 门可逆？
- 写出 CX 门的 $4 \times 4$ 矩阵（控制位是 ket 记号中左边的那一位），并验证它把 $|10\rangle$ 变成 $|11\rangle$。
- 两个 2 维向量的克罗内克积是几维？$n$ 个比特时又是多少维？

<details>
<summary>参考答案</summary>

- AND 对三种不同的输入（`00`、`01`、`10`）给出相同的输出 0，所以无法从输出反推出输入。CX 把 $(a, b) \to (a, a \oplus b)$，所以可以反推；事实上，再作用一次 CX 就会回到原来的输入。
- 按基的顺序 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$，并以左边的位作为控制位，矩阵保持前两行不变，交换后两行：$\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$。对应 $|10\rangle$ 的那一列在 $|11\rangle$ 所在的行上为 1，即 $|10\rangle \to |11\rangle$。
- $2 \times 2 = 4$ 维；$n$ 个比特时是 $2^n$ 维。

</details>

### 第 02 部分 · 量子计算（[README](../chapters/02_quantum_computing/README.zh-CN.md)），约 10–15 小时

这是分量最重、也最重要的部分：量子比特、叠加（superposition）、纠缠（entanglement）、布洛赫球、单量子比特门与多量子比特门、测量，以及各种“构建模块”（贝尔态、GHZ 态、W 态、预言机、相位反冲）。建议分成多次学习，并且要**认真阅读 02_05**，因为第 04 部分完全建立在它之上。

**自测**：
- 手算 $H \cdot H|0\rangle$，再用 Qiskit 验证。为什么结果必定是 $|0\rangle$？
- 制备贝尔态，并解释为什么只会测到 `00` 或 `11`。
- $|+\rangle$ 和 $|-\rangle$ 位于布洛赫球的什么位置？如果只沿 $z$ 轴测量，这两个状态有什么区别？

<details>
<summary>参考答案</summary>

- 完整的计算见[入门介绍页](what-is-quantum-computing.zh-CN.md#干涉连抛两次结果就确定了)：$|1\rangle$ 的概率幅是 $+\tfrac12 - \tfrac12 = 0$，因此相互抵消；$|0\rangle$ 的概率幅是 $\tfrac12 + \tfrac12 = 1$。
- 在量子比特 0 上作用 H，再作用 CX(0, 1)，得到 $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$。$|01\rangle$ 和 $|10\rangle$ 的概率幅为 0，所以测到它们的概率为 0。
- $|+\rangle$ 位于布洛赫球的 $+x$ 轴上，$|-\rangle$ 位于 $-x$ 轴上，两者都在赤道上。沿 $z$ 轴测量时，两者都给出 50/50，因此无法区分。它们的区别在于概率幅的相对符号（相位），这一点在沿 $x$ 轴测量时会显现出来（也就是先作用 H 再测量：$|+\rangle \to$ `0`，$|-\rangle \to$ `1`）。

</details>

### 第 03 部分 · 量子协议（[README](../chapters/03_quantum_protocols/README.zh-CN.md)），约 3–5 小时

纠缠和不确定性原理（uncertainty principle）最初的三个应用：量子货币（quantum money）、量子隐形传态（quantum teleportation）、超密编码（superdense coding）。

**自测**：
- 量子隐形传态能以超光速传递信息吗？为什么？
- 在所用资源（量子比特、经典比特、纠缠对）方面，超密编码和量子隐形传态有哪些相同点和不同点？
- 为什么量子货币的伪造者无法复制硬币？

<details>
<summary>参考答案</summary>

- 不能。只有当 Bob 从 Alice 那里收到**两个经典比特**之后，他的量子比特才会变成要传送的那个状态，而经典比特不可能以超光速传输。在此之前，Bob 看到的只是随机结果。
- 两者都使用事先共享的**一对纠缠量子比特**。量子隐形传态通过传输 **2 个经典比特**来发送 **1 个量子比特**；超密编码则相反，通过传输 **1 个量子比特**来发送 **2 个经典比特**。
- 伪造者不知道每个量子比特是按哪组基（bit 基还是 sign 基）制备的。用错误的基测量会破坏状态，而不可克隆定理（no-cloning theorem）又禁止复制未知的状态，所以没有任何办法做出可靠的副本：伪造品通过检验的概率随量子比特数的增加呈指数下降（例如采用“先测量、再重新制备”的方法时为 $(3/4)^n$）。详见 03_01。

</details>

### 第 04 部分 · 量子算法（[README](../chapters/04_quantum_algorithms/README.zh-CN.md)），约 8–12 小时

Deutsch–Jozsa、Bernstein–Vazirani 和 Simon 使用同一个模板（哈达玛门 → 预言机 → 哈达玛门 → 测量；Simon 把这个模板重复约 $n$ 次，再在经典计算机上求解模 2 线性方程组）；Grover 则把“预言机 + 振幅放大（amplitude amplification）”这一组操作重复约 (π/4)·√N 次。

**自测**：
- 什么是相位反冲？它如何帮助预言机 $U_f$ 把函数值 $f(x)$ 变成符号 $(-1)^{f(x)}$？
- Grover 在 $N = 2^{20}$ 个条目中找 1 个元素，大约需要调用多少次预言机？（提示：$\tfrac{\pi}{4}\sqrt N$；与经典方法比较一下。）
- 为什么 Deutsch–Jozsa 有“加速”，却没有实际应用？

<details>
<summary>参考答案</summary>

- 当目标量子比特处于 $|-\rangle$ 态时，预言机给出 $U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle$：函数值 $f(x)$ 被“反冲”成输入量子比特上的一个符号，而干涉可以利用这个符号。详见 02_05。
- $\tfrac{\pi}{4}\sqrt{2^{20}} \approx 804$ 次。经典方法平均约需 $N/2 \approx 524\,000$ 次。
- Deutsch–Jozsa 问题是人为构造的，专门用来展示优势。此外，这种优势只是相对于*保证必定正确*的经典算法而言；随机经典算法只需几次查询就能解决，而且出错概率极小。

</details>

## 学完第 04 部分之后呢？

原书计划增加 **QFT、QPE、Shor、HHL、哈密顿量模拟**等章节，但作者尚未写出（见[尚无内容的章节](../README.zh-CN.md#原书中尚无内容的章节)）。在此期间，你可以：

| 方向 | 建议 |
|---|---|
| 继续学习 Shor、QFT、QPE | IBM 的 *Fundamentals of quantum algorithms* 课程（包含 Deutsch–Jozsa、Simon、QPE、Shor、Grover），以及 Preskill 的讲义（研究生水平），均列在[资源](resources.zh-CN.md)中 |
| 更深入地理解纠缠（贝尔不等式、CHSH） | IBM 的 *Basics of quantum information* 课程，列在[资源](resources.zh-CN.md)中 |
| 学习变分算法（VQE、QAOA）和量子机器学习 | [资源](resources.zh-CN.md)中的 PennyLane |
| 了解量子计算对密码学的威胁 | [FAQ](faq.zh-CN.md#关于密码学) 中关于密码学的部分 |
| 在真实的量子计算机上运行 | [第 00 部分](../chapters/00_getting_started/README.zh-CN.md)中的 00_02 教程 |

## 学习技巧

- **逐个运行单元格，并事先猜测结果**。如果猜错了，那正是最值得学习的地方。
- **改变参数后重新运行**。修改 `shots`、换一个门、换一个控制量子比特。
- **不要在一个公式上钻牛角尖**。书中每个概念之后都会给出具体例子；先理解例子，再回头看公式。
- **遇到陌生术语就查**[术语表](glossary.zh-CN.md)。
- **怀疑书中有错**？请查看 [ERRATA](../ERRATA.zh-CN.md)：书中有一些小错误已经被记录下来，你不需要自己去发现。
