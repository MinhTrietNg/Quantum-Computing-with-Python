# 什么是量子计算机？

[Tiếng Việt](what-is-quantum-computing.md) · [English](what-is-quantum-computing.en.md) · **简体中文**

*阅读约需 15 分钟。不需要懂量子物理；如果想动手运行代码，只需具备 Python 基础。运行方法：[Google Colab 或你自己的电脑](setup.zh-CN.md)。*

## 一个诚实的回答

量子计算机是利用量子力学现象来存储和处理信息的计算机。它**不是**更快的笔记本电脑，也**不会**“同时尝试所有答案”。它是另一种工具：理论上擅长某些非常具体的问题（其中许多问题需要比现有机器规模大得多、错误少得多的机器），而对你每天用电脑做的大部分事情毫无帮助。

本页其余部分将解释上面这段话的含义。

## 从比特到量子比特

普通计算机用**比特**（bit）存储信息：每个比特要么是 `0`，要么是 `1`。

量子计算机使用**量子比特**（qubit）。一个量子比特的状态由两个称为**概率幅**（amplitude）的数 $\alpha$ 和 $\beta$ 来描述：

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1$$

符号的读法：

- $|0\rangle$ 读作“ket 0”。它只是“量子比特处于 0”这一状态的**名字**；$|1\rangle$ 同理。
- $\alpha$ 和 $\beta$ 是两个概率幅。与概率不同，它们可以是**负数**，甚至可以是*复数*（带有虚部的数）。刚开始时，你只需把它们看作可以为负的数。
- $|\alpha|^2$ 是 $\alpha$ 的模（大小）的平方；对于实数，它就是 $\alpha^2$。
- 右边的条件是说：两个概率加起来等于 100%。

进行**测量**（measurement）时，你总是得到一个普通的比特：以概率 $|\alpha|^2$ 得到 `0`，以概率 $|\beta|^2$ 得到 `1`。测量之后，量子比特就“锁定”在这个结果上。测量不会让你看到 $\alpha$ 和 $\beta$。

有两点让量子比特不同于普通的“概率”比特（比如一枚还没翻开的硬币）：

1. 概率幅可以是**负数或复数**，而不只是像概率那样的正数。
2. 概率幅之间可以**相互抵消或相互增强**。这叫作*干涉*（interference）；它与纠缠（entanglement）一起，是量子计算机强大能力的关键（见下文）。

## 需要记住的三个概念

| 概念 | 简单来说 | 详细学习 |
|---|---|---|
| **叠加**（superposition） | 量子比特处于**一个确定的状态**，由上面所说的两个概率幅 $\alpha, \beta$ 描述。叠加（相对于 $\vert 0\rangle, \vert 1\rangle$ 而言）是指**两个概率幅都不为 0**，例如 $\alpha = \beta = 1/\sqrt2$；而 $\vert 0\rangle$ 的 $\alpha = 1, \beta = 0$，所以不是叠加。它**不是**“既是 0 又是 1”；那只是一种容易引起误解的简略说法 | [02_01](../chapters/02_quantum_computing/README.zh-CN.md#02_01--qubits-and-quantum-circuits量子比特与量子电路) |
| **纠缠**（entanglement） | 两个量子比特紧密关联，以至于无法单独描述其中任何一个；沿多个不同方向测量时，它们结果之间的相关性是任何“事先配好的硬币”都无法实现的 | [02_02](../chapters/02_quantum_computing/README.zh-CN.md#02_02--quantum-entanglement量子纠缠) |
| **干涉**（interference） | 概率幅相互增强或相互抵消。量子算法的设计目标，是让错误答案相互抵消，而让正确答案得到放大 | [第 04 部分](../chapters/04_quantum_algorithms/README.zh-CN.md) |

## 第一个量子程序

我们使用开源 Python 库 Qiskit，直接在你的电脑上模拟量子计算机。`shots=1000` 表示把电路运行并测量 1000 次；结果是一张计数表，统计每个答案各出现了多少次。由于测量是随机的，**你得到的数字会与文档中的略有不同**。

先要了解两个词：**量子门**（gate）是作用在量子比特上的一种变换（例如下面的 `h` 和 `cx`），**量子电路**（circuit）则是一串量子门再加上测量。[读懂量子电路](#读懂量子电路)一节会解释如何看懂电路图。

### 用一个量子比特抛硬币

**哈达玛门**（Hadamard gate，即 H 门）把 $|0\rangle$ 变成 $\tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$，也就是两个概率幅相等，各对应 50% 的概率。

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)             # 哈达玛门
qc.measure_all()    # 测量

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'1': 497, '0': 503}      # 示例；每次运行得到的数字都不同，但总是接近 50/50
```

### 干涉：连抛两次，结果就确定了

在第一个 H 门之后紧接着**再加一个 H 门**：

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)
qc.h(0)             # 第二个 H 门
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'0': 1000}
```

如果量子比特只是一枚“随机硬币”，再抛一次，结果仍然是随机的。但实际结果却**总是 `0`**。自己算一算吧。H 门对两个基态的作用如下（注意**减号**）：

$$H|0\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big), \qquad H|1\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)$$

把第二个 H 门作用在 $\tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$ 上，也就是分别作用在每一项上，再把结果相加：

$$\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big) + \tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)
= \tfrac12\big(|0\rangle + |1\rangle\big) + \tfrac12\big(|0\rangle - |1\rangle\big) = |0\rangle$$

$|1\rangle$ 的概率幅得到 $+\tfrac12$ 和 $-\tfrac12$ 两份贡献，因此**相互抵消**。$|0\rangle$ 的概率幅得到 $+\tfrac12$ 和 $+\tfrac12$，因此**相加**为 1。用概率无法解释这一点，因为概率永远不会是负数，而概率幅可以。

这就是核心思想：**量子算法会精心安排，让通向错误答案的各条路径相互抵消**。

### 纠缠：两个量子比特总是一致

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)         # 量子比特 0：0 和 1 的概率幅相等
qc.cx(0, 1)     # CX 门：若量子比特 0 为 1，则翻转量子比特 1  -> 两个量子比特纠缠在一起
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'11': 496, '00': 504}      # 示例；每次运行的具体数字都不一样
```

电路如下（从左往右读）：方框 `H` 是哈达玛门；圆点 `■` 与方框 `X` 相连，表示受控非门，即 CX 门（圆点在控制量子比特上，方框 `X` 在目标量子比特上）；`M` 是测量；`░` 是 `measure_all()` 自动插入的 *barrier*（屏障线），它不会改变状态。

```text
        ┌───┐      ░ ┌─┐   
   q_0: ┤ H ├──■───░─┤M├───
        └───┘┌─┴─┐ ░ └╥┘┌─┐
   q_1: ─────┤ X ├─░──╫─┤M├
             └───┘ ░  ║ └╥┘
meas: 2/══════════════╩══╩═
                      0  1 
```

结果只会是 `00` 或 `11`，**永远不会**出现 `01` 或 `10`（在真实的量子计算机上，噪声偶尔会让少量 `01`/`10` 结果漏出来；理想的模拟器则不会）。单独看每个量子比特，结果都是 50/50 随机的，但两个量子比特的结果总是相同。

**仅凭这一点还不足以称之为“量子”**。把两枚事先配成相同的硬币分别装进两个信封，也能得到完全一样的结果。真正的区别只有在沿**多个不同方向**测量时才会显现：这时的相关性比任何“事先配好”的方式所能产生的都要强（这正是*贝尔不等式*（Bell inequality）的内容，例如 CHSH 游戏）。在 [02_02](../chapters/02_quantum_computing/README.zh-CN.md#02_02--quantum-entanglement量子纠缠) 中你会看到，这个状态无法写成“两个独立的量子比特”。原书的 Bell inequalities 一章尚无内容；[资源](resources.zh-CN.md)中列出的 IBM 课程涵盖了这部分。

上面的状态称为*贝尔态*（Bell state），它是[量子隐形传态](../chapters/03_quantum_protocols/README.zh-CN.md#03_02--quantum-teleportation量子隐形传态)（teleportation）和超密编码（superdense coding）的基础。

## 读懂量子电路

量子电路按时间顺序**从左往右**读。每条横线代表一个量子比特，每个方框是一个量子门（一种变换），仪表图标表示测量。双线是承载测量结果的经典（classical）比特。

例如，下面是量子隐形传态的电路：Alice 利用一对纠缠的量子比特和**两个经典比特**，把一个量子比特的状态发送给 Bob。

![量子隐形传态电路：Alice 用 H 门和 CX 门制备一对纠缠的量子比特，再通过量子信道把其中一个发给 Bob；Alice 准备好要发送的状态，作用 CX 门和 H 门，测量两个量子比特；两个结果比特经经典信道传给 Bob，供他作用 X 门和 Z 门](../chapters/03_quantum_protocols/images/03_02_03_teleportation_circuit.png)

*图：Diego Emilio Serrano，[learnquantum.io](https://learnquantum.io)，MIT License。*

现在不必全部看懂。学完[第 03 部分](../chapters/03_quantum_protocols/README.zh-CN.md)后，你就能读懂这个电路了。

## 量子计算机擅长什么，不擅长什么

### 目前已知的情况

> 这张表信息量有点大。第一次阅读时跳过也没关系；遇到陌生的术语，可以查[术语表](glossary.zh-CN.md)。

| 问题 | 加速 | 诚实的说明 |
|---|---|---|
| **整数分解**（肖尔算法，Shor's algorithm） | 从*超多项式*（super-polynomial，即增长得比位数的任何多项式函数都快）降到多项式 | 目前没有人知道多项式时间的经典算法，但也没有人证明它不存在。需要带纠错的大型量子计算机，而这样的机器尚不存在（截至 2026 年 10 月）。**注意**：没有人证明过这个问题是 *NP 完全*（NP-complete，即 NP 类中“最难”的那一组问题，例如逻辑表达式可满足性问题 SAT）的，而且它很可能不是；研究界也不认为量子计算机能在多项式时间内解决 NP 完全问题 |
| **无结构搜索**（[格罗弗（Grover）算法](../chapters/04_quantum_algorithms/README.zh-CN.md#04_04--grovers-algorithm格罗弗算法)） | 平方根级：$N \to \sqrt N$ | 已证明它**在黑盒模型中**（只能查询预言机，即 oracle）是最优的；对于有结构的问题，这并不排除存在更快的方法。对于 $N = 2^{20} \approx 10^6$ 个条目、要找的目标只有 1 个的情况：经典方法平均约需 $N/2 \approx 524$ 千次（约 52.4 万次）查询，Grover 约需 800 轮，每轮调用一次预言机。平方级加速是有限的：在实际规模下，预言机和纠错的开销可能会抵消这一优势 |
| **模拟量子系统**（化学、材料） | 前景广阔 | 这是物理学家 Richard Feynman 最初的设想。目前仍是研究方向，正在真实的量子计算机上进行试验 |
| 机器学习、优化 | **尚不明确** | 说法很多，确凿的证据很少。对各种宣传要保持谨慎 |

[第 04 部分](../chapters/04_quantum_algorithms/README.zh-CN.md)中的四个算法（Deutsch–Jozsa、Bernstein–Vazirani、Simon、Grover）是**用于学习的示例**。前三个算法解决的是人为构造的问题，没有实际应用：

- *Deutsch–Jozsa* 只是比**保证必定正确**的经典算法更快；一个允许很小出错概率的随机经典算法也只需要几次查询。
- *Bernstein–Vazirani* 带来的差距很小（从 $n$ 次查询降到 1 次）。
- *Simon* 是第一个即使与随机经典算法相比也具有**指数级**优势的例子，但它仍然局限在预言机模型之中。

它们传授的技巧——预言机、相位反冲（phase kickback）、干涉——会在 Shor 等算法中再次用到。

### 量子计算机做不到的事

- **不能**取代笔记本电脑或手机。对于日常任务（上网、处理文档、玩游戏），它更慢，也更贵。
- **不会**“同时尝试所有答案，再挑出正确的那个”。测量只给出一个结果，所以必须精心设计干涉，让正确答案以很高的概率出现。对于大多数问题，没有人知道该怎么做到这一点。
- **不能**以超光速传递信息。纠缠产生的是相关性，而不是通信信道；量子隐形传态仍然需要发送普通的经典比特（见 [03_02](../chapters/03_quantum_protocols/README.zh-CN.md#03_02--quantum-teleportation量子隐形传态)）。
- **不能**复制未知的量子态（即*不可克隆定理*，no-cloning theorem；见 [02_04](../chapters/02_quantum_computing/README.zh-CN.md#02_04--multi-qubit-systems多量子比特系统)）。

## 为什么难以制造

量子比特很容易被环境（热、振动、电磁干扰）以及控制设备的不精确所破坏。这些偏差统称为*噪声*（noise），包括*退相干*（decoherence）、每个门的误差，以及读取结果时的误差。现有的机器仍处于 **NISQ** 时代（noisy intermediate-scale quantum，含噪声中等规模量子；这一术语由物理学家 John Preskill 于 2017 年底提出，并通过 2018 年的一篇论文广为流传）：量子比特数量不少，但噪声大，还不足以运行像 Shor 这样的大型算法。

解决办法是**量子纠错**（quantum error correction）：用许多物理量子比特构成一个可靠的“逻辑”量子比特。每个逻辑量子比特需要多少个物理量子比特，估计从几十个到几千个不等，取决于所用的纠错码和噪声水平。目前正在探索的技术包括超导电路、离子阱、中性原子、光子，以及许多其他方向。

> 这一领域发展很快。以上关于硬件的所有说法均基于截至 2026 年 10 月的认识；引用具体数据之前，请先查阅最新资料。

## 为什么不能直接用普通计算机来模拟？

完整描述 $n$ 个量子比特的状态需要 $2^n$ 个概率幅。每增加一个量子比特，所需内存就翻一倍：

| 量子比特数 | 概率幅个数 | 内存（每个复数 16 字节） |
|---|---|---|
| 10 | 1 024 | 16 KiB |
| 30 | 约 $10^9$ | 16 GiB |
| 50 | 约 $10^{15}$ | 16 PiB |

三十个量子比特已经可以放进一台性能强劲的电脑（16 GiB 只是这个向量本身所需；实际计算时还要多一些），五十个则远远超出任何单台机器的能力。这就是完全模拟无法扩展的原因，也是你可以**在笔记本电脑上学完本仓库全部内容**的原因：这里的示例最多使用 14 个量子比特（Simon 算法那一课），态矢量（statevector）只需约 256 KiB。

（对于具有特殊结构的电路，存在一些巧妙的模拟技术，所以上表给出的是“暴力穷举”式模拟的开销，而不是绝对的极限。）

## 下一步

| 你想要 | 阅读 |
|---|---|
| 循序渐进、按路线学习 | [学习路线](learning-path.zh-CN.md) |
| 搭建环境，或者不安装直接运行 | [安装与运行](setup.zh-CN.md) |
| 查一个术语 | [术语表](glossary.zh-CN.md) |
| 常见问题解答（也谈到密码学） | [FAQ](faq.zh-CN.md) |
| 继续学习的外部资料 | [资源](resources.zh-CN.md) |
