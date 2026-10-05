# 原书中的已知错误

[Tiếng Việt](ERRATA.md) · [English](ERRATA.en.md) · **简体中文**

[chapters/](chapters/) 中的 notebook 与[原书](https://github.com/learn-quantum/lqc-textbook)（commit `7abf73c`）保持**完全一致**，错误也原样保留。下面这些错误是在对照阅读时发现的。每个错误也在相应部分的 README 中就地做了注释（形式为 `> 注意：`），并附有详细解释。

错误分级：

- **代码错误**：代码中的错误，导致输出或结论出现偏差。
- **内容错误**：知识性的表述有误。
- **可能已过时**：写书时是正确的，但对于现在的软件、服务可能已不再适用。
- **笔误**：公式、注释或文字中的错误；不影响代码。

## 代码错误

| 课 | 错误 | 影响 | 修正方法 |
|---|---|---|---|
| [02_01](chapters/02_quantum_computing/README.zh-CN.md) | `one = Statevector([1, 0])`，这是 $\vert 0\rangle$ 而不是 $\vert 1\rangle$ | 没有影响，因为下一个单元格用 `from_label('1')` 覆盖了它 | `Statevector([0, 1])` |
| [02_05](chapters/02_quantum_computing/README.zh-CN.md) | 多量子比特相位反冲（kickback）的单元格赋值给 `qψ_in`（多了一个字母 `q`），却显示上一个单元格的 `ψ_in` | 标为“input”的输出写着 $\vert 01\rangle$，这是错的；标为“output”的输出是正确的 | 把 `qψ_in` 改为 `ψ_in` |
| [04_01](chapters/04_quantum_algorithms/README.zh-CN.md) | `black_box()` 使用 `np.random.randint(1,3)`，所以只会生成电路 1 或 2，也就是**只有常数函数** | 第 1.1 节中两张正确/错误统计图没有反映完整的问题 | `np.random.randint(1,5)` |
| [04_04](chapters/04_quantum_algorithms/README.zh-CN.md) | `Uf_M_marked(n, M)` 用 `np.random.randint(N, size=M)` 选取元素，因此**可能重复**；notebook 中保存的输出就是 `['001', '001']` | 两个相同的 MCX 相互抵消，预言机（oracle）什么也没有标记 | `np.random.choice(N, size=M, replace=False)` |
| [04_04](chapters/04_quantum_algorithms/README.zh-CN.md) | `found after: {x_in} tries` 这一行打印的是**索引** $x$ | 实际尝试次数是 `x_in + 1` | 打印 `x_in + 1` |

## 内容错误

| 课 | 错误 | 正确说法 |
|---|---|---|
| [02_03](chapters/02_quantum_computing/README.zh-CN.md) | 说 $\{H, S, CX\}$ 足以近似任意门 | 这组门只能生成 Clifford 群，而 Clifford 群可以在经典计算机上高效模拟（Gottesman–Knill 定理）；还需要加上 $T$ 门（即 Clifford+T）。原书第 02_04 课的说法是正确的 |
| [03_01](chapters/03_quantum_protocols/README.zh-CN.md) | 公式 $(1/4)^n$ 紧挨着关于“造假者成功”的句子，容易被误解为伪造成功的概率 | 它其实是盲猜**完全猜中**整个状态的概率。如果造假者逐个随机测量量子比特、再重新制备，那么**一枚**硬币通过检验的概率是 $(3/4)^n$（$n=6$ 时约为 0.18）；要让**两枚**硬币同时通过，这种方法只能达到 $(5/8)^n$，而最好的策略也只能达到 $(3/4)^n$（这一最优结果已被证明：Molina–Vidick–Watrous 2012，[arXiv:1202.4010](https://arxiv.org/abs/1202.4010)）。这些概率都呈指数下降 |
| [03_01](chapters/03_quantum_protocols/README.zh-CN.md) | “the probability of the criminal successfully guessing the state grows with the number of qubits” | 这个概率随 $n$ **减小**，正如公式 $(1/4)^n$ 所示 |
| [01_02](chapters/01_classical_computing/README.zh-CN.md) | 说把可逆 **OR** 电路作用两次“在这种情况下能得到正确结果” | 只对一半的输入成立。该电路先在 $a, b$ 上各作用一个 X，再用 CCX 作用到 $c = 1$ 上（最后没有 X），所以作用两次会把 $(a, b, 1)$ 变成 $(a, b, a \oplus b)$：只有当 $a \neq b$ 时，$c$ 才会回到 $1$。例如 $(0,0,1) \to (1,1,0) \to (0,0,0)$。必须把门的顺序倒过来才能撤销，正如后面那个单元格所做的那样 |
| [01_03](chapters/01_classical_computing/README.zh-CN.md) | 说 CX 乘以 $\vert 00\rangle$ 得到“等于 CX 第一**行**的列向量” | 应为第一**列** $(c_{00}, c_{10}, c_{20}, c_{30})$。数值结果仍然正确，因为 CX 矩阵是对称的 |
| [01_04](chapters/01_classical_computing/README.zh-CN.md) | 把“随机矩阵（stochastic matrix）”定义为**不能**写成克罗内克积（Kronecker product）形式的多 p-bit 矩阵；并说随机矩阵一般不可逆 | 随机矩阵是元素非负、且每列之和为 1 的矩阵；本课中的矩阵 $P$、$R$、$X$ 和 $R \otimes X$ 都是随机矩阵。关键在于，噪声矩阵的**逆矩阵**一般不再是随机矩阵（会出现负元素或大于 1 的元素），因此不能描述物理操作 |
| [02_02](chapters/02_quantum_computing/README.zh-CN.md) | 把 $\frac{1}{\sqrt2}\vert 01\rangle + \frac{1}{\sqrt2}\vert 10\rangle$ 选作由自旋为 0 的粒子产生的两个粒子的状态（“a reasonable choice”） | 这只与沿 $z$ 方向的测量相符。自旋 0 守恒给出的是**单态**（singlet）$\frac{1}{\sqrt2}(\vert 01\rangle - \vert 10\rangle)$，沿**任意**轴测量结果都相反；如果取 $+$ 号，沿 $x$ 或 $y$ 测量时两边会得到相同的结果 |
| [02_04](chapters/02_quantum_computing/README.zh-CN.md) | 把 SWAP 称为“another important entangling gate” | SWAP 只是交换两个量子比特（$\text{SWAP}\vert a\rangle\vert b\rangle = \vert b\rangle\vert a\rangle$），把乘积态变成乘积态，因此**不会产生纠缠** |
| [02_04](chapters/02_quantum_computing/README.zh-CN.md) | 说 Solovay–Kitaev 定理是加入 $T$ 门后获得完整计算能力的原因 | Solovay–Kitaev 定理只是说：一个已经足够稠密的门集可以**高效地**近似任意门。Clifford+T 是通用（稠密）门集，这是另一个独立的事实 |
| [02_05](chapters/02_quantum_computing/README.zh-CN.md), [04_03](chapters/04_quantum_algorithms/README.zh-CN.md) | 把肖尔（Shor）算法的加速称为“proven”（已证明） | 格罗弗（Grover）算法已被证明是最优的（在预言机模型中）。肖尔算法只是比**已知最好的**经典算法更快；目前还没有证明不存在快速的经典算法 |
| [04_03](chapters/04_quantum_algorithms/README.zh-CN.md) | “只需 $r = 6$ 次尝试，成功概率就已超过 50%”（$n = 5$ 时） | 精确计算（无放回抽样）：$r = 6$ 时为 $43.4\%$，$r = 7$ 时为 $56.5\%$；书中的图也是如此。按同样的计算方法，$n = 7$ 时得到 $r = 14$（第一个超过 50% 的次数），与书中紧随其后的说法一致 |

## 可能已过时

这些内容在写书时是正确的，但对于现在的软件或服务可能已不再适用。

| 课 | 书中的内容 | 现状 |
|---|---|---|
| [00_02](chapters/00_getting_started/README.zh-CN.md) | 在 `quantum.ibm.com` 创建账号，运行 `QiskitRuntimeService.save_account('your-token-here')` | 当前版本的 `qiskit-ibm-runtime` 把 `token` 描述为 IBM Cloud API key，channel 取 `ibm_cloud` 或 `ibm_quantum_platform`，并带有 `instance` 参数；平台已迁移到 `quantum.cloud.ibm.com`。请按照当前的官方文档操作 |

## 笔误

| 课 | 错误 | 正确写法 |
|---|---|---|
| [00_01](chapters/00_getting_started/README.zh-CN.md) | 创建了 `qc_t = transpile(...)`，却运行 `simulator.run(qc, ...)` | 应运行 `qc_t`；对 AerSimulator 来说没有影响，但在真实硬件上需要使用经过 transpile 的电路 |
| [01_01](chapters/01_classical_computing/README.zh-CN.md) | 注释说 Python 的 `and`、`or` 不等价于 `&` 和 `^` | 就在上方的表格写着 AND 是 `&`、OR 是 `\|`、XOR 是 `^`；所以应为 `&` 和 `\|` |
| [01_02](chapters/01_classical_computing/README.zh-CN.md) | “用两个 CCX 来翻转输入” | 代码和图中用的是两个 **X** 门 |
| [01_02](chapters/01_classical_computing/README.zh-CN.md) | 全加器（full adder）代码中的注释把 `ccx(a,b,0)` 称为 AND1，把 `ccx(b2,c,0)` 称为 AND2 | 图 01_02_09 的叫法正好相反：前一个门（控制位为 $a, b$）是 AND2，后一个门（控制位为 $a \oplus b$ 和 $c_{in}$）是 AND1 |
| [01_03](chapters/01_classical_computing/README.zh-CN.md) | 说 $\vec x \otimes \vec y$ 的维数是两者维数之“和” | 应为**乘积**（$2 \times 2 = 4$；$n$ 个比特对应 $2^n$ 维） |
| [01_04](chapters/01_classical_computing/README.zh-CN.md) | 注释写的是“100 times” | `n_samps = 200` |
| [02_03](chapters/02_quantum_computing/README.zh-CN.md) | 在换到 sign 基的例子中，两个系数都写成了 $\frac{2\sqrt3 - \sqrt6}{6}$ | $\vert -\rangle$ 的系数应为 $\frac{2\sqrt3 + \sqrt6}{6} \approx 0.986$；notebook 中的数值是正确的 |
| [02_05](chapters/02_quantum_computing/README.zh-CN.md) | 第 4.3 节一会儿说 $x = 010$，一会儿说 $\vert 10\rangle$ | 代码和输出标记的是 $x = 011$ |
| [02_05](chapters/02_quantum_computing/README.zh-CN.md) | 注释（以及正文）说 `ctrl_state='01'` 的受控 S 门“由 $\vert 01\rangle$ 触发” | `SGate().control(2, ctrl_state='01')` 作用在 `[2,1,0]` 上时，在 $q_2 = 1$ 且 $q_1 = 0$ 时触发，也就是两个控制量子比特处于 $\vert q_2 q_1\rangle = \vert 10\rangle$（`ctrl_state` 字符串从右往左读：最后一个字符对应第一个控制量子比特）；实际运行会在 $\vert 101\rangle$ 上得到相位 $i$。书中的输出是正确的 |
| [03_01](chapters/03_quantum_protocols/README.zh-CN.md) | “we only consider qubits in the $xy$-plane” | 应为 $xz$ 平面 |
| [03_02](chapters/03_quantum_protocols/README.zh-CN.md) | 注释“two entangled Bell states”和“Alice prepares state $\vert w\rangle = \frac12\vert 01\rangle - \frac{\sqrt3}{2}\vert 10\rangle$” | 电路生成了 3 对贝尔态，并制备了 $\frac{1}{\sqrt3}(\vert 001\rangle - \vert 010\rangle + \vert 100\rangle)$，与输出一致 |
| [03_02](chapters/03_quantum_protocols/README.zh-CN.md) | 单量子比特的例子打印 `(j,i) = ({alices_bits[1]},{alices_bits[0]})` | 标签颠倒了：`alices_bits[1]` 是 `cra[0]`，即比特 $i$（已通过只让 `cra[0] = 1` 运行 Qiskit 验证）；Bob 的最终状态不受影响 |
| [03_02](chapters/03_quantum_protocols/README.zh-CN.md) | 当 $(\theta, \varphi) = (\pi/2, \pi/4)$ 时，把这对 FP16 字符串写成 $(0011101001001000, 0011111001001000)$ | 两个字符串的位置互换了：`float16` 给出 $\pi/4 = 0011101001001000$，$\pi/2 = 0011111001001000$ |
| [03_03](chapters/03_quantum_protocols/README.zh-CN.md) | 第 3 步之后的结果表把标签写成 $\vert \psi\rangle_2$ | $\vert \psi\rangle_3$ |
| [04_04](chapters/04_quantum_algorithms/README.zh-CN.md) | 第 2.2 节把 $\vert m^\perp\rangle$ 写成 $\sum_{x \neq 0}$ | 应为 $\sum_{x \neq m}$，并且需要归一化 |
| [04_04](chapters/04_quantum_algorithms/README.zh-CN.md) | 第 2.2 节在关于 $(V U_f)$ 的句子之后紧接着写“作用 $(U_f V)^2$” | 应为 $(V U_f)^2$，与图以及紧接在下方的公式 $(V U_f)^\kappa$ 一致 |

## 报告新错误

如果发现了其他错误，请使用本仓库的 **Báo lỗi trong sách**（报告书中错误）模板提交 issue，最好也到[上游仓库的 Issues](https://github.com/learn-quantum/lqc-textbook/issues) 告知作者，以便修正原书。
