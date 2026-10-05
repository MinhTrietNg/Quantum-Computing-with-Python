# 02 · Quantum computing（量子计算）

[Tiếng Việt](README.md) · [English](README.en.md) · **简体中文**

本部分从电子自旋（spin）的施特恩–格拉赫实验（Stern–Gerlach experiment）出发，建立**量子比特**（qubit）的概念，接着讲解叠加（superposition）、纠缠（entanglement）、布洛赫球（Bloch sphere）、量子门（quantum gate）和测量（measurement），最后介绍各种**构建模块**（building blocks），例如贝尔态 / GHZ 态 / W 态、哈达玛变换（Hadamard transform）、相位反冲（phase kickback）和预言机（oracle）。这些内容是第 03 部分（协议）和第 04 部分（算法）的直接基础。

> 来源：[02_01](https://learnquantum.io/chapters/02_quantum_computing/02_01_bits_to_qubits.html) ·
> [02_02](https://learnquantum.io/chapters/02_quantum_computing/02_02_entanglement.html) ·
> [02_03](https://learnquantum.io/chapters/02_quantum_computing/02_03_single_qb_sys.html) ·
> [02_04](https://learnquantum.io/chapters/02_quantum_computing/02_04_multi_qb_sys.html) ·
> [02_05](https://learnquantum.io/chapters/02_quantum_computing/02_05_quantum_blocks.html)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## 目录

| 课 | Notebook | 网页 | 要点 |
|---|---|---|---|
| 02_01 · Qubits and quantum circuits | [02_01_bits_to_qubits.ipynb](02_01_bits_to_qubits.ipynb) | [链接](https://learnquantum.io/chapters/02_quantum_computing/02_01_bits_to_qubits.html) | 电子自旋 → 概率幅 → 量子比特；X 门、H 门；在 Qiskit 中搭建第一个电路 |
| 02_02 · Quantum entanglement | [02_02_entanglement.ipynb](02_02_entanglement.ipynb) | [链接](https://learnquantum.io/chapters/02_quantum_computing/02_02_entanglement.html) | 可分离态与纠缠态；用 H + CX 制造纠缠 |
| 02_03 · Single-qubit systems | [02_03_single_qb_sys.ipynb](02_03_single_qb_sys.ipynb) | [链接](https://learnquantum.io/chapters/02_quantum_computing/02_03_single_qb_sys.html) | 复数概率幅、布洛赫球、相位；泡利门、P/S/T、RX/RY/RZ；测量、可观测量 |
| 02_04 · Multi-qubit systems | [02_04_multi_qb_sys.ipynb](02_04_multi_qb_sys.ipynb) | [链接](https://learnquantum.io/chapters/02_quantum_computing/02_04_multi_qb_sys.html) | n 量子比特态；受控门、SWAP；不可克隆；通用门集；部分测量 |
| 02_05 · Quantum building blocks | [02_05_quantum_blocks.ipynb](02_05_quantum_blocks.ipynb) | [链接](https://learnquantum.io/chapters/02_quantum_computing/02_05_quantum_blocks.html) | 贝尔态、GHZ 态、W 态；哈达玛变换；相位反冲；预言机 |

> 本 README 中的代码均**摘录**自 notebook（保留原有的英文注释），并且会用到前面单元格中定义的变量。要想运行，请把整个 notebook 从头到尾执行一遍。

---

## 02_01 · Qubits and quantum circuits（量子比特与量子电路）

**目标**：理解为什么需要用**概率幅**（probability amplitude）代替概率，并搭建第一个量子电路。

### 核心知识

> 如果对下面的物理还不熟悉，别担心。你只需记住一点：**概率 = 概率幅的平方**，而概率幅可以是负数。实验只是书中把你引向这一点的方式。

**施特恩–格拉赫实验**：电子具有自旋（一种内禀属性，使电子表现得像一块非常小的磁铁）。让电子穿过沿 $z$ 轴方向的非均匀磁场：
- 自旋 $+z$ 的电子总是向上偏，自旋 $-z$ 的电子总是向下偏；
- 自旋 $\pm x$ 的电子**不会**像经典磁铁那样直线穿过，而是向上或向下偏，各占 50%，并且**从不**落在中间。

（书中用电子是为了便于想象。真实的实验用的是电中性的银原子，因为电子带电，洛伦兹力会盖过自旋的效应。）

<p align="center"><img src="images/02_01_05_stern-gerlach_up-down_elec.png" width="700" alt="施特恩–格拉赫装置：自旋向上的电子向上偏，自旋向下的电子向下偏"></p>

*图：自旋 $+z$ 的电子总是向上偏（左），自旋 $-z$ 的电子总是向下偏（右）。*

<p align="center"><img src="images/02_01_06_stern-gerlach_right_elec.png" width="360" alt="自旋 +x 的电子穿过施特恩–格拉赫装置，向上或向下偏，各占 50%"></p>

*图：自旋 $+x$ 的电子不会直线穿过，而是向上或向下偏，各占 50%。*

**概率向量不够用**：试着用概率向量来描述自旋（就像 01_04 中那样）。沿 $z$ 轴测量时，$+x$ 和 $-x$ 都给出 50% 向上、50% 向下，所以两者都是 $[\tfrac12, \tfrac12]^\top$。但它们是两个*不同*的状态：把测量装置转到 $x$ 轴就能区分它们（一个总是给出 $+x$，另一个总是给出 $-x$）。概率向量丢失了信息。

<p align="center"><img src="images/02_01_08_stern-gerlach_left-right_elec.png" width="700" alt="把施特恩–格拉赫装置旋转到磁场沿 x 轴：自旋 +x 和自旋 −x 的电子偏向相反的两侧"></p>

*图：把测量装置旋转到磁场沿 $x$ 轴：自旋 $+x$（左）和自旋 $-x$（右）的电子偏向相反的两侧。*

更糟的是，自旋 $+z$ 的电子穿过沿 $x$ 轴放置的测量装置时，同样会偏向两侧，各占 50%。因此自旋 $+z$ 可以看作 $+x$ 与 $-x$ 各占一半的组合。

<p align="center"><img src="images/02_01_09_stern-gerlach_up_elec.png" width="360" alt="自旋 +z 的电子穿过沿 x 轴放置的施特恩–格拉赫装置，偏向两侧，各占 50%"></p>

*图：自旋 $+z$ 的电子穿过沿 $x$ 轴放置的测量装置：偏向两侧，各占 50%。*

但把两个向量各取一半再相加，$\tfrac12[\tfrac12, \tfrac12]^\top + \tfrac12[\tfrac12, \tfrac12]^\top$，得到的仍然只是 $[\tfrac12, \tfrac12]^\top$，而不是 $[1, 0]^\top$：“向下”分量本应**相互抵消**，可概率永远不会是负数，所以无法抵消。因此必须允许分量取**负值**，并让概率等于概率幅的**平方**（玻恩定则，Born rule）：

$$|s\rangle = \begin{bmatrix}s_0\\ s_1\end{bmatrix}, \qquad \mathbb{P}_{+z} = s_0^2, \quad \mathbb{P}_{-z} = s_1^2$$

**量子比特**：换个名字，自旋向上记为 $|0\rangle$，自旋向下记为 $|1\rangle$，并且

$$|+\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big), \qquad |-\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)$$

> 注意：在 1.2 节末尾的小结中，notebook 把两个向量都标成了 $|s_{-x}\rangle$；向量 $[\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2}]^\top$ 应为 $|s_{+x}\rangle$。紧挨在它前面的那句“find what $s_0$ and $s_1$ for the vector $|s_{-z}\rangle$ should be”中的向量也应为 $|s_{-x}\rangle$。

一般定义：

$$|q\rangle = \begin{bmatrix}\alpha_0\\ \alpha_1\end{bmatrix}, \quad \alpha_j \in \mathbb{C}, \quad |\alpha_0|^2 + |\alpha_1|^2 = 1$$

（符号 $\mathbb{C}$ 表示复数集，现在不必马上弄懂，02_03 会讲到。目前只需把概率幅看作实数，可以为负。）

对比一下：比特的分量属于 $\{0,1\}$；概率比特（p-bit）的分量属于 $[0,1]$，且**总和**为 1；量子比特的分量是**复数**，且**模的平方和**为 1。

> 叠加**并不**意味着“既是 0 又是 1”或“同时处于两个状态”。$|+\rangle$ 是**一个完全确定的状态**；只是当我们选用 $z$ 轴来描述它时，它被写成 $|0\rangle$ 与 $|1\rangle$ 的组合，且两者的概率幅相等。

**量子电路包括 3 个步骤**：
1. **制备状态**（state preparation），几乎总是制备成 $|0\rangle$。
2. **变换状态**：通过各种门实现。
3. **测量**（measurement）：把量子态投影为经典比特，结果具有概率性。

<p align="center"><img src="images/02_01_10_spin_vs_qubit_x.png" width="750" alt="自旋实验与对应的电路：制备 |0⟩，经过 X 门，测量结果总是 1"></p>

*图：实验（上）与对应的电路（下）。SG1 加上挡板，只让自旋向上的电子继续前进（制备 $|0\rangle$），磁场 B 翻转自旋（$X$ 门），SG2 进行测量，结果总是 1。*

**最初的两个门**：

$$X = \begin{bmatrix}0&1\\1&0\end{bmatrix}\ (|0\rangle \leftrightarrow |1\rangle), \qquad
H = \tfrac{1}{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}\ (|0\rangle \leftrightarrow |+\rangle,\ |1\rangle \leftrightarrow |-\rangle)$$

<p align="center"><img src="images/02_01_11_spin_vs_qubit_h.png" width="750" alt="实验与带 H 门的电路：|0⟩ 变为 |+⟩，测量得到 0 或 1，各占 50%"></p>

*图：同一个实验，但磁场 B 把自旋从 $+z$ 转到 $+x$（$H$ 门把 $|0\rangle$ 变为 $|+\rangle$）；SG2 给出 0 或 1，各占 50%。*

> 注意：notebook 中 $H$ 的小数形式把右下角元素写成了 $-\frac{\sqrt2}{\sqrt2}$，正确的是 $-\frac{\sqrt2}{2}$。让 $|0\rangle$、$|1\rangle$ 通过 `qc_h` 的那个单元格把标签误印成了“over an X gate”；输出其实是 $H$ 门的，而且是正确的。

### 核心代码

```python
zero = Statevector.from_label('0')
one = Statevector.from_label('1')
plus = Statevector.from_label('+')
minus = Statevector.from_label('-')
```
用标签创建状态。也可以传入概率幅列表，例如 `Statevector([np.sqrt(1/2), -np.sqrt(1/2)])`。

> 注意：前面一个单元格写的是 `one = Statevector([1, 0])`，这是错的，因为那是 $|0\rangle$。这个单元格用 `from_label('1')` 重新赋值，所以后面的输出仍然正确。

```python
display(plus.draw('latex', prefix='|+ \\rangle = '))                       # display ket representation of |+⟩
display(minus.draw('latex', prefix='|- \\rangle = ', convention='vector')) # display vector representation of |-⟩
```
`draw('latex')` 以右矢（ket）形式显示；`convention='vector'` 以向量形式显示。为了紧凑，Qiskit 把列向量显示成**行**，但它仍是同一个状态。

```python
qc = QuantumCircuit(1,1)  # Create circuit object with 1 qubit and 1 classical bit
qc.reset(0)               # Add state preparation gate (reset) to qubit 0
qc.x(0)                   # Add X gate to circuit to qubit 0
qc.measure(0,0)           # Add measurement gate between qubit 0 and bit 0
qc.draw()
```
三步电路：reset → X → 测量。在 Qiskit 中，所有量子比特默认从 $|0\rangle$ 开始，所以 `reset` 通常是多余的。

```python
X = Operator(qc_x)
X.draw('latex', prefix='X =')
```
`Operator(circuit)` 取出电路的酉矩阵（unitary）。`state.evolve(circuit)` 让状态通过电路。`Statevector(circuit)` 总是从 $|0\dots0\rangle$ 开始。

```python
plus_counts = plus.sample_counts(100)
```
直接在 `Statevector` 上模拟测量；`sample_memory(100)` 按顺序返回每一次的结果。

```python
simulator = BasicSimulator()           # define simulator object
job = simulator.run(qc_hm, shots=100)  # use run method to execute our circuit some number of shots
result = job.result()                  # extract our results
counts = result.get_counts()           # get the counts from the experiment
```
在模拟器（simulator）上运行带测量的电路，流程与在真实硬件上相同。`plot_histogram(counts)` 绘制结果。

### 运行结果

| 检查项 | 输出 |
|---|---|
| X 电路的 `Operator` | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ |
| $\vert 0\rangle$、$\vert 1\rangle$ 经过 H | $\tfrac{\sqrt2}{2}(\vert 0\rangle \pm \vert 1\rangle)$ |
| 从 $\vert 0\rangle$ 出发、先 X 后 H 的电路 | $\vert -\rangle$；矩阵 $H\cdot X = \tfrac{\sqrt2}{2}\begin{bmatrix}1&1\\-1&1\end{bmatrix}$ |
| `plus.sample_counts(100)` | `{'0': 51, '1': 49}` |
| `zero.sample_counts(100)` | `{'0': 100}` |
| H + 测量电路，100 个 shot（单次运行与测量），`BasicSimulator` | `{'0': 41, '1': 59}` |

### 速记要点

- 概率 = 概率幅（的模）的平方；概率幅可以为负，一般情况下是复数。
- $|+\rangle$、$|-\rangle$ 沿 $z$ 测量时概率相同，但它们是两个不同的状态。
- $X$ 互换 $|0\rangle \leftrightarrow |1\rangle$；$H$ 互换 $|0\rangle \leftrightarrow |+\rangle$、$|1\rangle \leftrightarrow |-\rangle$。
- `Statevector` = 精确计算；`simulator.run(qc, shots=N)` = 测量 N 次。
- `Operator(qc)` = 电路的矩阵。

---

## 02_02 · Quantum entanglement（量子纠缠）

**目标**：区分**可分离**（separable）态与**纠缠**（entangled）态，并用电路制造纠缠。

### 核心知识

**两个量子比特**通过克罗内克积（Kronecker product）组合在一起，约定 $q_0$ 写在右边：$|q\rangle = |q_1\rangle \otimes |q_0\rangle = |q_1 q_0\rangle$。

$$|+\rangle \otimes |+\rangle = \tfrac12\big(|00\rangle + |01\rangle + |10\rangle + |11\rangle\big)$$

每个结果的概率都是 $(1/2)^2 = 1/4$，与两个独立电子的实验相符。

<p align="center"><img src="images/02_02_03_two_spin_right_options.png" width="740" alt="两个相互独立、自旋都是 +x 的电子分别在两台装置中测量：上 / 下共四种组合，每种 25%"></p>

*图：两个相互独立的电子，自旋都是 $+x$，分别在两台装置中测量：上 / 下共 4 种组合，每种 25%。*

**可分离** = 能写成各个量子比特状态的**一个**乘积。例如 $\tfrac12(|00\rangle - |01\rangle + |10\rangle - |11\rangle) = |+\rangle \otimes |-\rangle$。

**纠缠**：一个自旋为 0 的粒子衰变成两个自旋相反的粒子（例如电子）。沿 $z$ 轴测量：总是一个向上、一个向下，两种情况各占 50%。

<p align="center"><img src="images/02_02_04_two_spin_entangled.png" width="700" alt="一个粒子衰变成两个电子，分别飞向两台测量装置；总是一个电子向上偏，另一个向下偏"></p>

*图：一个粒子（紫色）衰变成两个电子，分别飞向两台沿 $z$ 方向的测量装置：总是一个向上、一个向下，两种情况各占 50%。*

你也许会猜：这对粒子产生时，自旋总是已经沿 $z$ 方向定好了。如果是这样，把两台测量装置都转到 $x$ 轴，两边的结果就应该相互独立：4 种组合，每种 25%。

<p align="center"><img src="images/02_02_06_two_spin_x_entangled.png" width="700" alt="假设：自旋早已沿 z 方向定好，因此旋转测量装置后每一边都是 50/50，且与另一边无关"></p>

*图：待检验的假设：如果这对粒子的自旋早已沿 $z$ 方向定好，那么旋转测量装置后，每一边都是 50/50，且与另一边无关。实验否定了这个假设。*

实验表明**并非如此**：把两台测量装置沿同一个任意的轴放置，结果仍然总是一个向上、一个向下。如果只看沿 $z$ 的测量（`01` 和 `10`，各 1/2），那么下面两个状态都符合：

$$\tfrac{1}{\sqrt2}\big(|01\rangle + |10\rangle\big) \quad\text{或}\quad \tfrac{1}{\sqrt2}\big(|01\rangle - |10\rangle\big)$$

两者都**无法**分解成两个单独状态的乘积。对经典系统来说，完全知道整个系统的状态，也就完全知道了每个部分的状态；这里却不是这样。上面两个状态中，只有 $\tfrac{1}{\sqrt2}(|01\rangle - |10\rangle)$ 沿**任何**轴测量都给出相反的结果，所以它才是由自旋为 0 的粒子产生的那对粒子的状态。而对于 $\tfrac{1}{\sqrt2}(|01\rangle + |10\rangle)$，两边都沿 $x$ 轴测量时，结果反而总是**相同**的方向。

> 注意：notebook 仅根据沿 $z$ 轴的统计，就称 $\tfrac{1}{\sqrt2}(|01\rangle + |10\rangle)$ 为“合理的选择”，接着又说负号的那个状态“也给出同样的观测结果”。这只在沿 $z$ 测量时成立；对于上面“沿任何轴都相反”的观测，只有负号的状态才符合。

> 不要过度引申：（1）每一边看到的仍是 50/50 的随机结果，所以这种关联**不能**用来传递信息；（2）单是“同一轴上总是相反”这一点，仍然可以用一个经典模型来模仿（每对粒子事先就带有一个随机方向）。任何“预先设定”的模型都做不到的那部分，只有在两台测量装置的轴**彼此错开**时，才会通过贝尔不等式（Bell inequality）显现出来（书中尚未涉及；参见[术语表](../../docs/glossary.zh-CN.md)）。

**用电路制造纠缠**（先 H 后 CX）：

$$|00\rangle \xrightarrow{H \otimes I} \tfrac{1}{\sqrt2}\big(|00\rangle + |10\rangle\big) \xrightarrow{CX} \tfrac{1}{\sqrt2}\big(|00\rangle + |11\rangle\big)$$

<p align="center"><img src="images/02_02_07_spin_vs_qubit_entangled.png" width="750" alt="制造纠缠的实验与电路：先 H 后 CX 得到贝尔态，测量得到 00 或 11"></p>

*图：磁场 B 把上方的电子转到 $+x$（$H$ 门），电磁场让两个电子发生相互作用（$CX$ 门），得到 $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$；测量得到 `00` 或 `11`，各占 50%。*

### 核心代码

```python
state_00 = state_0.tensor(state_0)    # compose state |0⟩⊗|0⟩
state_01 = state_0.tensor(state_1)    # compose state |0⟩⊗|1⟩
```
`a.tensor(b)` 即 $a \otimes b$；`b` 是右边的量子比特（量子比特 0）。

```python
H = Operator.from_label('H')
I = Operator.from_label('I')
HI = H.tensor(I)
q = q.evolve(HI)
```
用矩阵一步一步地做：$H \otimes I$ 对 $q_1$ 作用 H，同时保持 $q_0$ 不变。然后执行 `q.evolve(CX)`，其中 `CX = Operator([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])`。

```python
qc_ent = QuantumCircuit(2)    # define quantum circuit
qc_ent.h(1)                   # apply H gate to qubit 1
qc_ent.cx(1,0)                # apply CX with control on q1 and target on q0
```
用电路的做法得到相同的结果。`qc.measure_all()` 给所有量子比特加上测量。

### 运行结果

| 检查项 | 输出 |
|---|---|
| $\vert +-\rangle$、$\vert -+\rangle$、$\vert --\rangle$ | 各项符号 $\pm\tfrac12$ 与克罗内克积的结果完全一致 |
| 可分离电路 $\vert +\rangle\vert -\rangle$，1000 个 shot | `{'01': 270, '10': 229, '11': 225, '00': 276}`，每个结果约占 25% |
| H + CX 电路 | $\tfrac{\sqrt2}{2}\vert 00\rangle + \tfrac{\sqrt2}{2}\vert 11\rangle$ |
| H + CX 电路，1000 个 shot | `{'11': 508, '00': 492}`，从不出现 `01`、`10` |

### 速记要点

- $|q_1 q_0\rangle = |q_1\rangle \otimes |q_0\rangle$：量子比特 0 在**右边**。
- 可分离 = 一个克罗内克积；纠缠 = 不可分离。
- 从 $|00\rangle$ 出发：在控制位（control）上作用 H，再加 CX = 制造纠缠的标准做法。
- 沿 $z$ 测量 $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$：两个结果总是相同，但每个结果单独来看仍是 50/50 随机的，所以无法传递信息。

---

## 02_03 · Single-qubit systems（单量子比特系统）

**目标**：给出量子比特的完整定义，在布洛赫球上表示它，掌握单量子比特门，并把测量形式化。

### 核心知识

**任意角 θ**：与 $+z$ 成 $\theta$ 角的自旋给出 $\mathbb{P}_0 = \cos^2\tfrac\theta2$ 和 $\mathbb{P}_1 = \sin^2\tfrac\theta2$，因此

$$|q\rangle = \cos\tfrac\theta2\,|0\rangle + \sin\tfrac\theta2\,|1\rangle$$

<p align="center"><img src="images/02_03_01_stern-gerlach_angle_prob.png" width="360" alt="自旋与 z 轴成 θ 角的电子：以概率 cos²(θ/2) 向上偏，以概率 sin²(θ/2) 向下偏"></p>

*图：自旋与 $+z$ 成 $\theta$ 角：以概率 $\cos^2(\theta/2)$ 向上偏，以概率 $\sin^2(\theta/2)$ 向下偏。*

> 注意：notebook 1.1 节的表格写着 $|-\rangle$ 对应 $\theta = \frac{3\pi}{2}$，且 $\cos\frac\theta2 = \frac{1}{\sqrt2}$、$\sin\frac\theta2 = -\frac{1}{\sqrt2}$。实际上，当 $\theta = \frac{3\pi}{2}$ 时，$\cos\frac{3\pi}{4} = -\frac{1}{\sqrt2}$，$\sin\frac{3\pi}{4} = \frac{1}{\sqrt2}$，得到的是 $-|-\rangle$（同一个状态，只差一个全局相位，见下文）。表中的数值对应的是 $\theta = -\frac{\pi}{2}$。

**需要复数**：位于 $xy$ 平面内的自旋，沿 $z$ 测量时总是给出 50/50。

<p align="center"><img src="images/02_03_02_elec_phi_angle.png" width="520" alt="位于 xy 平面内、处于任意角 φ 的自旋：沿 z 测量总是 50% 向上、50% 向下"></p>

*图：自旋位于 $xy$ 平面内，与 $x$ 轴成任意角 $\varphi$：沿 $z$ 测量总是 50/50，与 $\varphi$ 无关。*

对于 $\pm y$，需要这样的概率幅：既给出概率 1/2，又能重新组合出 $|0\rangle$、$|1\rangle$。能做到这一点的**实数**只有 $\pm\tfrac{1}{\sqrt2}$，但它们已经用在 $|\pm\rangle$（$x$ 轴）上了；所以必须用 $\pm i$：

$$|r\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle + i|1\rangle\big), \qquad |l\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle - i|1\rangle\big)$$

<p align="center"><img src="images/02_03_05_spin_in_complex_plane.png" width="250" alt="让复平面与 xy 平面重合：1、i、−1、−i 分别位于 +x、+y、−x、−y 轴上"></p>

*图：让复平面与 $xy$ 平面重合：数 $1, i, -1, -i$ 分别位于 $+x, +y, -x, -y$ 轴上；角 $\varphi$ 处的自旋对应复数 $e^{i\varphi}$。*

准确地说，玻恩定则取的是**模的平方**：$|c|^2 = c\,c^* = a^2 + b^2$。$xy$ 平面上的一般形式是 $\tfrac{1}{\sqrt2}(|0\rangle + e^{i\varphi}|1\rangle)$。

> 注意：notebook 把复数 $c = a + bi$ 的辐角写成 $\varphi = \text{atan2}(a, b)$；按通用约定（`numpy.arctan2(y, x)`）应为 $\text{atan2}(b, a)$，虚部在前。同样在 1.2 节，“相减组合”的左边写的是 $\frac{1}{\sqrt2}|r\rangle - \frac{i}{\sqrt2}|l\rangle$，但下面的计算（得到 $i|1\rangle$）用的是 $\frac{1}{\sqrt2}|r\rangle - \frac{1}{\sqrt2}|l\rangle$。

**布洛赫球**：把上面两个结果合起来：

$$|q\rangle = \cos\tfrac\theta2\,|0\rangle + e^{i\varphi}\sin\tfrac\theta2\,|1\rangle$$

$\theta \in [0, \pi]$ 是与 $+z$ 轴的夹角；$\varphi \in [0, 2\pi)$ 是在 $xy$ 平面上的投影的角度，从 $+x$ 轴量起。单个量子比特的每一个状态（忽略全局相位，见紧接着的下文）都是单位球面上的一个点。

<p align="center"><img src="images/02_03_06_bloch.png" width="300" alt="布洛赫球：θ 角从 z 轴量起，φ 角从 x 轴量起，并标出 |0⟩、|1⟩、|+⟩、|−⟩、|r⟩、|l⟩ 的位置"></p>

*图：布洛赫球。$|0\rangle$、$|1\rangle$ 位于两极；$|\pm\rangle$ 在 $x$ 轴上；$|r\rangle$、$|l\rangle$ 在 $y$ 轴上。*

**全局相位与相对相位**：对任意复数 $\alpha_0, \alpha_1$：

$$|q\rangle = e^{i\gamma}\Big[\cos\tfrac\theta2\,|0\rangle + e^{i\varphi}\sin\tfrac\theta2\,|1\rangle\Big]$$

- $\gamma$ 是**全局相位**（global phase）：无法测量，因为 $|e^{i\gamma}|^2 = 1$。例如 $i|1\rangle$ 与 $|1\rangle$ 等价。
- $\varphi$ 是**相对相位**（relative phase）：可以测量，因为它决定了状态在布洛赫球上的位置。沿 $z$ 测量时看不出它（如 $|+\rangle$ 和 $|-\rangle$），但沿 $x$ 或 $y$ 测量时结果就会改变。

**左矢、内积与基**：左矢（bra）是**共轭转置**：$\langle q| = [\alpha_0^*, \alpha_1^*]$。内积满足 $\langle y|x\rangle = \langle x|y\rangle^*$；范数 $\|q\| = \sqrt{\langle q|q\rangle}$。三组重要的正交归一基：

| 基 | 状态 | 布洛赫球上的轴 |
|---|---|---|
| 计算基（computational / bit） | $\vert 0\rangle, \vert 1\rangle$ | $\pm z$ |
| 哈达玛基（Hadamard / sign） | $\vert +\rangle, \vert -\rangle$ | $\pm x$ |
| Y 基（Y / hand） | $\vert r\rangle, \vert l\rangle$ | $\pm y$ |

> 注意：在把 $\sqrt{2/3}\,|0\rangle - \sqrt{1/3}\,|1\rangle$ 换到符号基（sign basis）的例子中，notebook 把两个系数都写成了 $\frac{2\sqrt3 - \sqrt6}{6}$。$|-\rangle$ 的系数应为 $\frac{2\sqrt3 + \sqrt6}{6} \approx 0.986$；notebook 中的数值结果是正确的。

外积 $|x\rangle\langle y|$ 是一个矩阵；两个投影算符（projector）$\Pi_0 = |0\rangle\langle 0|$ 和 $\Pi_1 = |1\rangle\langle 1|$ 用于测量。

**门是酉矩阵**：$UU^\dagger = U^\dagger U = I$。因此每个门都有逆门 $U^\dagger$（量子计算是可逆的），而且酉矩阵保持向量的范数不变。

| 类别 | 矩阵 | 在布洛赫球上的作用 |
|---|---|---|
| 泡利 $X$ | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ | 绕 $x$ 轴旋转 π |
| 泡利 $Y$ | $\begin{bmatrix}0&-i\\i&0\end{bmatrix}$ | 绕 $y$ 轴旋转 π |
| 泡利 $Z$ | $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ | 绕 $z$ 轴旋转 π：$Z\vert +\rangle = \vert -\rangle$，$Z\vert 1\rangle = -\vert 1\rangle$ |
| 相位门 $P(\varphi)$ | $\begin{bmatrix}1&0\\0&e^{i\varphi}\end{bmatrix}$ | 绕 $z$ 旋转 $\varphi$；$Z = P(\pi)$，$S = P(\pi/2)$，$T = P(\pi/4)$ |
| $S^\dagger$、$T^\dagger$ | 右下角元素为 $e^{-i\varphi}$ | 反方向旋转 |
| $RX(\theta)$ | $\begin{bmatrix}\cos\frac\theta2 & -i\sin\frac\theta2\\ -i\sin\frac\theta2 & \cos\frac\theta2\end{bmatrix}$ | 绕 $x$ 旋转 θ |
| $RY(\theta)$ | $\begin{bmatrix}\cos\frac\theta2 & -\sin\frac\theta2\\ \sin\frac\theta2 & \cos\frac\theta2\end{bmatrix}$ | 绕 $y$ 旋转 θ |
| $RZ(\varphi)$ | $\begin{bmatrix}e^{-i\varphi/2}&0\\0&e^{i\varphi/2}\end{bmatrix}$ | 绕 $z$ 旋转 φ；$RZ(\varphi) = e^{-i\varphi/2}P(\varphi)$ |

> 注意：notebook 写道，$S$ 加上 $H$ 和 $CX$ 就足以近似任何门。实际上 $\{H, S, CX\}$ 只能生成 Clifford 群，而这个群在经典计算机上可以被高效模拟（Gottesman–Knill 定理）。必须再加上 **$T$** 门（Clifford+T 门集）才是通用的。书中第 02_04 课本身也正是这么说的。notebook 引用的 Solovay–Kitaev 定理也没有说哪个门集是通用的；它说的是：一旦有了通用门集，要把一个门近似到误差 $\varepsilon$，所需的门数只是 $\log(1/\varepsilon)$ 的幂次量级，也就是说可以**高效地**近似。

**破坏性测量与非破坏性测量**：如果电子撞到屏上，它就会被吸收：这是**破坏性**测量（destructive measurement），测量之后就没有自旋可谈了。

<p align="center"><img src="images/02_03_07_dest_meas.png" width="375" alt="破坏性测量：电子穿过施特恩–格拉赫装置后撞到屏上，在上方或下方留下痕迹，各占 50%"></p>

*图：破坏性测量：电子被屏吸收，只在上方或下方留下痕迹（各占 50%）。*

如果在屏上开两个孔让电子飞过去，我们就能知道它走了哪条路，而电子依然存在：这是**非破坏性**测量（non-destructive）。测量之后，自旋恰好处于与结果对应的状态。书中把这称为状态被**投影**（projection）或**约化**（reduction），并避免使用“坍缩”（collapse）一词，因为这个词常常与量子力学的某一种特定诠释联系在一起。

<p align="center"><img src="images/02_03_08_nondest_meas.png" width="400" alt="非破坏性测量：电子穿过上孔或下孔，并继续处于自旋向上或向下的状态"></p>

*图：非破坏性测量：电子穿过上孔或下孔（各占 50%），并继续以相应的自旋向上或向下的状态存在。*

因此，一次测量会给出三样东西：经典结果 $j$、它的概率 $\mathbb{P}_j$，以及测量后的量子态 $|j\rangle$。

<p align="center"><img src="images/02_03_09_meas_cir.png" width="500" alt="先 H 后测量的电路：经典寄存器得到 0 或 1，测量后的量子比特为 |0⟩ 或 |1⟩，每种可能各占 1/2"></p>

*图：测量 $|+\rangle$：经典结果（0 或 1）写入经典寄存器 $c$（双线），每个结果的概率为 1/2，测量后的量子比特相应地为 $|0\rangle$ 或 $|1\rangle$。*

**投影测量（projective measurement，PVM）**：对一组投影算符 $\{\Pi_j\}$：
1. 每个 $\Pi_j$ 对应经典结果 $j$。
2. 概率：$\mathbb{P}_j = \langle q|\Pi_j|q\rangle$。
3. 测量后的状态：$|q'\rangle = \Pi_j|q\rangle / \sqrt{\mathbb{P}_j}$。

对 1 个量子比特来说，这种写法显得多余，但在只测量多量子比特系统的一部分时（第 02_04 课）就非常必要了。

> 注意（notebook 中的小笔误）：3.1 节写的是 $\langle 1|(\alpha_1|0\rangle + \alpha_1|1\rangle)$，应为 $\alpha_0|0\rangle + \alpha_1|1\rangle$；还有两处写成 $\sqrt{\mathbb{P}_i}$，应为 $\sqrt{\mathbb{P}_j}$。2.3 节列出的是“RX, RY, RX”，应为 $RX, RY, RZ$。

**后选择与重置**：后选择（post-selection）是测量之后只保留想要的结果。重置（reset）是测量之后，若结果为 1 就作用 $X$，因此总是得到 $|0\rangle$。

**可观测量**（observable）是可以测量的物理量，用厄米（Hermitian）矩阵 $\mathcal{O} = \sum_j \lambda_j \Pi_j$ 表示，其中 $\lambda_j$ 是测量值。令 $|0\rangle \to +1$、$|1\rangle \to -1$，得到的正好是矩阵 $Z = \Pi_0 - \Pi_1$（$X$、$Y$ 同理）。期望值为

$$\langle \mathcal{O}\rangle_q = \langle q|\mathcal{O}|q\rangle$$

例如 $|q\rangle = \sqrt{1/3}\,|0\rangle + \sqrt{2/3}\,|1\rangle$ 给出 $\langle X\rangle = 2\sqrt{2/9} \approx 0.943$。

### 核心代码

```python
θ = np.pi/3                # Spin angle wrt to +z axis
α0 = np.cos(θ/2)           # Probability amplitude associated with |0⟩
α1 = np.sin(θ/2)           # Probability amplitude associated with |1⟩

q = Statevector([α0, α1])  # Construct statevector |q⟩ = α0|0⟩ + α1|1⟩ = [α0 α1]ᵀ

probs = q.probabilities() # Extract expected probs array [P₀, P₁]
```
`probabilities()` 给出精确的概率；`sample_counts(shots=1000)` 给出采样结果。

```python
θ = np.pi/3
φ = 2*np.pi/5

α0 = np.cos(θ/2)
α1 = np.sin(θ/2) * np.exp(1j*φ)

sv = Statevector([α0, α1])
sv.draw('bloch')
```
在布洛赫球上画出任意一个量子比特；改变 θ、φ，就能看到向量随之移动。

```python
qc_p = QuantumCircuit(3)
qc_p.h(range(3)) # prepare |+⟩ state in all three qubits
qc_p.z(2)
qc_p.s(1)
qc_p.t(0)
```
在三个量子比特上分别作用三个相位门，再用 `Statevector(qc_p).draw('bloch', reverse_bits=True)` 进行比较。反方向旋转的版本用 `sdg`、`tdg`。

```python
qc = QuantumCircuit(1,1)
qc.h(0)                           # Initialize in superposition
qc.save_statevector('q_pre')     # Save statevector before reset
qc.measure(0,0)                   # Measure state (should give 50/50 `0` or `1`)
with qc.if_test((0,1)): qc.x(0)   # Apply X gate if classical result is `1`
qc.save_statevector('q_pst')      # Save statevector after reset
```
手动重置：`if_test((clbit, value))` 是根据测量结果进行控制的指令（经典前馈，classical feed-forward）。`save_statevector` 是 Aer 的指令，用于在电路中途保存状态。

```python
O = Operator.from_label('X')
O_expval = q.expectation_value(O)
```
由 `Statevector` 得到精确的期望值。

```python
Obs = SparsePauliOp.from_operator(O)
estimator = Estimator(mode=AerSimulator())
result = estimator.run([(qc_o, Obs)]).result()
O_expval = result[0].data.evs
```
通过 `Estimator` 原语（primitive，来自 `qiskit_ibm_runtime`）在 AerSimulator 上运行，用采样来估计期望值。不需要 IBM 账号。

### 运行结果

| 检查项 | 输出 |
|---|---|
| θ = π/3：`probabilities()` | `[0.75 0.25]` |
| θ = π/3：`sample_counts(1000)` | `{'0': 763, '1': 237}` |
| 重置：之前 / 之后 | $\tfrac{\sqrt2}{2}(\vert 0\rangle + \vert 1\rangle)$ / $\vert 0\rangle$ |
| 精确的 $\langle X\rangle$（`expectation_value`） | `0.9428` |
| 用 `Estimator` 得到的 $\langle X\rangle$ | `0.936`（有采样误差） |

### 速记要点

- 量子比特 = 布洛赫球上的一个点：$\cos\frac\theta2|0\rangle + e^{i\varphi}\sin\frac\theta2|1\rangle$。
- 全局相位无法测量；相对相位则可以测量。
- 概率 = $|\alpha|^2 = \alpha\alpha^*$；左矢是**共轭转置**。
- 门 = 酉矩阵 = 布洛赫球上的旋转；$S = P(\pi/2)$，$T = P(\pi/4)$，$Z = P(\pi)$。
- 测量：$\mathbb{P}_j = \langle q|\Pi_j|q\rangle$，测量后为 $\Pi_j|q\rangle/\sqrt{\mathbb{P}_j}$。
- 期望值：$\langle q|\mathcal{O}|q\rangle$；精确值用 `expectation_value`，采样估计用 `Estimator`。

---

## 02_04 · Multi-qubit systems（多量子比特系统）

**目标**：把所有内容推广到 $n$ 个量子比特：状态、多量子比特门、不可克隆定理（no-cloning theorem）、通用门集和部分测量。

### 核心知识

**$n$ 量子比特态**是 $N = 2^n$ 个基态的组合：

$$|q\rangle = \sum_{j=0}^{N-1} \alpha_j |j\rangle, \qquad \sum_j |\alpha_j|^2 = 1, \qquad \langle i|j\rangle = \delta_{ij}$$

$|j\rangle$ 是对应二进制数的简写，例如 $|5\rangle \sim |101\rangle$。

> 注意：notebook 写的是 $j$（以及 $i$）“从 0 到 $2^{N-1}$”；正确的是从 0 到 $N - 1 = 2^n - 1$，与求和的下标一致。

**多个量子比特上的单量子比特门**：$U = U_{n-1} \otimes \dots \otimes U_0$，例如在 $q_0$ 上作用 X、在 $q_1$ 上作用 H、在 $q_2$ 上作用 Z，就是 $Z \otimes H \otimes X$。这类乘积形式的门**无法产生纠缠**；需要**纠缠门**（entangling gate）。

**用投影算符表示受控门**：

$$CU = \Pi_0 \otimes I + \Pi_1 \otimes U$$

| 门 | 公式 / 说明 |
|---|---|
| $CX$ | $\Pi_0 \otimes I + \Pi_1 \otimes X$ |
| $CZ$ | $\Pi_0 \otimes I + \Pi_1 \otimes Z$ = diag(1, 1, 1, −1)；**对称**：交换控制位和目标位，矩阵不变 |
| $CP(\varphi)$ | $\Pi_0 \otimes I + \Pi_1 \otimes P(\varphi)$ |
| $\overline{C}X$（控制位为 0 时激活） | $\Pi_1 \otimes I + \Pi_0 \otimes X$ = 在控制位上先 X，再 CX，再 X |
| $CCX$（托佛利门，Toffoli） | $(\Pi_{00} + \Pi_{01} + \Pi_{10}) \otimes I + \Pi_{11} \otimes X$ |
| 控制位与目标位不相邻 | 在中间插入 $I$：$CZ_{20} = \Pi_0 \otimes I \otimes I + \Pi_1 \otimes I \otimes Z$ |
| SWAP | 交换两个量子比特的状态；等于 3 个 CX 门（类似 XOR 交换技巧） |
| CSWAP（Fredkin 门） | 受控 SWAP |

> 注意：notebook 把 SWAP 称为一种“entangling gate”（纠缠门）。SWAP 确实不能写成单量子比特门的张量积，但它把任何可分离态 $|a\rangle|b\rangle$ 变成 $|b\rangle|a\rangle$，结果仍然可分离。因此单靠 SWAP **不能**产生纠缠。

**不可克隆定理**：CX 能复制 $|0\rangle$ 和 $|1\rangle$。

<p align="center"><img src="images/02_04_01_copy_1.png" width="500" alt="CX 门把量子比特 1 的状态 |ψ⟩ 复制到量子比特 0，但仅当 |ψ⟩ 是 |0⟩ 或 |1⟩ 时成立"></p>

*图：CX 把量子比特 1 的状态 $|\psi\rangle$ 复制到量子比特 0（初始为 $|0\rangle$），但仅当 $|\psi\rangle$ 是 $|0\rangle$ 或 $|1\rangle$ 时才行。*

假设存在一个能复制任意状态的门 $\Theta$：$(\alpha_0|0\rangle + \alpha_1|1\rangle)|0\rangle \to (\alpha_0|0\rangle + \alpha_1|1\rangle)^{\otimes 2}$。

<p align="center"><img src="images/02_04_02_copy_2.png" width="500" alt="假想的复制门 Θ 把量子比特 1 的任意状态 |ψ⟩ 复制到量子比特 0"></p>

*图：假想的复制门 $\Theta$，对任意 $|\psi\rangle$ 都适用。不可克隆定理指出，这样的门并不存在。*

由于酉变换是线性的，输出必然是 $\alpha_0|00\rangle + \alpha_1|11\rangle$，而真正的副本应为 $\alpha_0^2|00\rangle + \alpha_0\alpha_1|01\rangle + \alpha_1\alpha_0|10\rangle + \alpha_1^2|11\rangle$。只有当状态是 $|0\rangle$ 或 $|1\rangle$ 时，这两个表达式才相等。**无法复制一个任意的量子态。**

> 注意：notebook 把第二种情况写成了 $(\alpha_1 = 0, \alpha_1 = 1)$；应为 $(\alpha_0 = 0, \alpha_1 = 1)$。

**通用门集**（universal gate set）能以任意精度近似任何酉变换。
- 现有硬件：使用带连续参数的原生门集，例如 $\{CX, SX, RZ(\theta)\}$；`transpile` 把电路转换到这个门集上。
- Margolus 门（$RCCX$）与 CCX 相同，只是相位不同：$|101\rangle \to -|101\rangle$，$|110\rangle \to i|111\rangle$，$|111\rangle \to -i|110\rangle$（书中简化地说成给这三个输入加上相位 $-1, i, -i$）。当这些相位不影响结果时，它所需的门要少得多。
- 容错（fault-tolerant）量子计算机使用 **Clifford+T**：只由 Clifford 门 $\{H, S, CX\}$ 组成的电路可以在经典计算机上高效模拟（Gottesman–Knill）；加上 $T$ 才具备完整的量子能力。在大多数纠错架构中，$T$ 门的代价最高，因此必须尽量减小 **T 深度**（T-depth，即 T/T† 门的层数）。

> 注意：notebook 写道，加上 $T$ 就具备完整量子能力的原因“由 Solovay–Kitaev 定理解释”。并非如此：Clifford+T 的通用性来自 $H$ 和 $T$ 能生成单量子比特旋转的一个稠密集；Solovay–Kitaev 定理只说明这种近似是**高效的**（门数为 $\log(1/\varepsilon)$ 的幂次量级）。

**全部测量**：$\mathbb{P}_j = |\alpha_j|^2$，测量后变为 $|j\rangle$。

**部分测量**：把系统分成被测量的部分 $A$ 和不测量的部分 $B$。对于前 $m$ 个量子比特（$q_0, \dots, q_{m-1}$，位于张量积的**右侧**）：

$$\Pi_k^A = I^{\otimes(n-m)} \otimes \Pi_k, \qquad \mathbb{P}_k^A = \langle q|\Pi_k^A|q\rangle, \qquad |q'\rangle = \frac{\Pi_k^A|q\rangle}{\sqrt{\mathbb{P}_k^A}}$$

例如 $|w\rangle = \tfrac{1}{\sqrt3}(|001\rangle + i|010\rangle - |100\rangle)$，只测量 $q_0$：$\mathbb{P}_0 = 2/3$，$\mathbb{P}_1 = 1/3$。若结果为 0，剩下的状态是 $\tfrac{i}{\sqrt2}|010\rangle - \tfrac{1}{\sqrt2}|100\rangle$；若结果为 1，则是 $|001\rangle$。

### 核心代码

```python
Π0 = Operator.from_label('0')
Π1 = Operator.from_label('1')
I = Operator.from_label('I')
X = Operator.from_label('X')

CX = Π0.tensor(I) + Π1.tensor(X)
```
用投影算符搭建 CX；`Operator.from_label('0')` 就是 $|0\rangle\langle 0|$。

```python
qc = QuantumCircuit(2)
qc.cx(1,0,ctrl_state='0')
```
`ctrl_state` 改变激活条件。有多个控制位时：`qc.ccx(1,2,0,ctrl_state='10')`。该字符串按小端序（little-endian）读取：**最右边**的字符对应列表中的**第一个**控制位（$q_1$），所以 `'10'` 表示 $q_2 = 1$、$q_1 = 0$（输出：只有 $|100\rangle \leftrightarrow |101\rangle$ 互换）。

```python
qc_t = transpile(qc, basis_gates=['cx', 'sx', 'rz']) # Converts arbitrary circuit to a given basis gate-set
```
把 CCX（或 `rccx`）转换为硬件的原生门集。

```python
T_depth = qc.depth(lambda instr: instr.operation.name in ['t', 'tdg'])
```
统计 T 深度：给 `depth()` 加一个过滤条件，只计入 `t`、`tdg` 门。

```python
# Create 3-qubit |w⟩ state:
w = np.sqrt(1/3)*(Statevector.from_int(1,8) + 1j*Statevector.from_int(2,8) - Statevector.from_int(4,8))
probs = w.probabilities([0])
c_result, q_result = w.measure([0])
```
`from_int(k, dim)` 创建 $|k\rangle$；`probabilities([0])` 和 `measure([0])` 只测量量子比特 0（去掉 `[0]` 则测量全部）。

```python
qc = QuantumCircuit(3)

# prepare |w⟩
qc.x(2)
qc.cry(2*np.arccos(np.sqrt(1/3)),2,1)
qc.cx(1,2)
qc.cry(2*np.arccos(np.sqrt(1/2)),1,0)
qc.cx(0,1)
qc.barrier()
qc.z(2)
qc.s(1)
qc.id(0)
```
用 `cry`（受控 RY）制备 $|w\rangle$ 的电路，再用 Z、S 加上相位。之后进行测量，并用 `save_statevector()` 查看测量后的状态。

### 运行结果

| 检查项 | 输出 |
|---|---|
| `Z.tensor(H.tensor(X))` 与 X/H/Z 电路的 `Operator(qc)` | 同一个 8×8 矩阵 |
| `Π0⊗I + Π1⊗X` | 与 `qc.cx(1,0)` 的矩阵一致 |
| H⊗H 之后接 CZ | $\tfrac12(\vert 00\rangle + \vert 01\rangle + \vert 10\rangle - \vert 11\rangle)$ |
| 3 个 CX | 正好得到 SWAP 矩阵 |
| 用 Clifford+T 搭建 CCX 的电路 | 正是 CCX 矩阵，T 深度 = `4` |
| `w.probabilities()` | `[0, 1/3, 1/3, 0, 1/3, 0, 0, 0]` |
| `w.probabilities([0])` | `[2/3, 1/3]` |
| 只测量 $q_0$，结果为 0 | $\tfrac{\sqrt2 i}{2}\vert 010\rangle - \tfrac{\sqrt2}{2}\vert 100\rangle$ |

### 速记要点

- $n$ 个量子比特 → $2^n$ 个概率幅。
- 受控门：$\Pi_0 \otimes I + \Pi_1 \otimes U$；中间隔着其他量子比特时就插入 $I$。
- CZ 是对称的；SWAP = 3 个 CX；Fredkin = CSWAP。
- **不可克隆**：无法复制任意状态（CX 只能复制 $|0\rangle$、$|1\rangle$）。
- Clifford+T 是通用的；在容错计算机上 T 通常代价最高，所以要尽量减小 T 深度。
- 部分测量：$\Pi_k^A = I \otimes \dots \otimes \Pi_k$，然后重新归一化。

---

## 02_05 · Quantum building blocks（量子构建模块）

**目标**：掌握在后面所有协议和算法中反复用到的子电路。

### 核心知识

**四个贝尔态**（贝尔基，Bell basis）：

$$|\Phi^\pm\rangle = \tfrac{1}{\sqrt2}\big(|00\rangle \pm |11\rangle\big), \qquad |\Psi^\pm\rangle = \tfrac{1}{\sqrt2}\big(|01\rangle \pm |10\rangle\big)$$

电路 H($q_1$) + CX($q_1 \to q_0$) 把 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ 依次变为 $|\Phi^+\rangle, |\Psi^+\rangle, |\Phi^-\rangle, |\Psi^-\rangle$。也可以保持输入为 $|00\rangle$，在 CX 之后再加门：Z → $\Phi^-$，X → $\Psi^+$，X 和 Z → $\Psi^-$。

**GHZ 态**是 $|\Phi^+\rangle$ 的推广：$|\Omega_n\rangle = \tfrac{1}{\sqrt2}(|0\rangle^{\otimes n} + |1\rangle^{\otimes n})$。搭建电路有三种方法：

| 方法 | 思路 | 优缺点 |
|---|---|---|
| `ghz_cir_a` | 对最高位的量子比特作用 H，再从它向其他每个量子比特作用 CX | 需要与所有量子比特相连；如果硬件只连接相邻的量子比特，就得额外加 SWAP |
| `ghz_cir_b` | 在相邻的量子比特对之间依次作用 CX | 只需相邻连接，但各个 CX 只能串行执行：深度为 $n$，量子比特等待时间长，容易出错 |
| `ghz_cir_c` | H 作用在中间的量子比特上，再向两侧并行扩展 | 仍然只需相邻连接，深度降到 $\lceil n/2\rceil + 1$ |

> 注意：notebook 写的是 `ghz_cir_b` 的深度为 $n+1$，`ghz_cir_c` 的深度为 $n/2 + 2$。用 `qc.depth()` 数出来分别是 $n$ 和 $\lceil n/2\rceil + 1$（例如 $n = 7$ 时为 7 和 5）。“大约减半”的结论仍然成立。

**W 态**是 $|\Psi^+\rangle$ 的推广：每个分量都恰好只有一个比特为 1（one-hot，独热）：$|W_n\rangle = \tfrac{1}{\sqrt n}\sum_{j=0}^{n-1}|2^j\rangle$。电路先用 RY/CRY 分配概率幅，再用 CX 重新排列。

**量子哈达玛变换** $\text{QHT}_n = H^{\otimes n}$，矩阵元为 $h_{i,j} = (-1)^{i\cdot j}/\sqrt N$，其中 $i \cdot j$ 是**二进制点积**（逐位 AND，再把结果 XOR 起来）。对第 04 部分来说最重要的公式是：

$$H^{\otimes n}|j\rangle = \frac{1}{\sqrt N}\sum_{i=0}^{N-1}(-1)^{i\cdot j}|i\rangle, \qquad H^{\otimes n}|0\dots0\rangle = \frac{1}{\sqrt N}\sum_i |i\rangle$$

**特征值与特征向量**：$U|u\rangle = \lambda|u\rangle$。对酉矩阵而言 $|\lambda| = 1$，所以 $\lambda = e^{i\varphi}$：把 $U$ 作用在特征向量上只会添加一个**全局相位**，无法测量。例如 $X$ 有 $(1, |+\rangle)$ 和 $(-1, |-\rangle)$；$S$ 有 $(1, |0\rangle)$ 和 $(i, |1\rangle)$。

**相位反冲**：让控制位处于叠加态，目标位处于 $U$ 的特征向量；相位 $e^{i\varphi}$ 被“反冲”到**控制位**上，成为**相对相位**，也就是说可以被测量：

$$\tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big)|u\rangle \xrightarrow{CU} \tfrac{1}{\sqrt2}\big(|0\rangle + e^{i\varphi}|1\rangle\big)|u\rangle$$

例如对于 CX 且目标位为 $|-\rangle$：$|+\rangle|-\rangle \to |-\rangle|-\rangle$；若再在前后各夹一层 H，则 $|01\rangle \to |11\rangle$，即**目标位翻转了控制位**。有多个控制位时，只有激活 $U$ 的那个状态 $|k\rangle$ 才会获得相位，就像“标记”了一个状态。这是格罗弗（Grover）算法（第 04 部分）的关键步骤之一。

> 注意：notebook 写道，相位反冲在肖尔（Shor）算法和格罗弗算法等“已被证明具有加速”的算法中起着重要作用。对格罗弗算法来说，平方级加速是在查询模型（预言机模型）中得到证明的。对肖尔算法来说，指数级加速只是相对于**目前已知最好的**经典算法而言；还没有人证明整数分解问题不存在快速的经典算法。

**用电路计算布尔函数**：借助一个辅助量子比特 $y$，任何 $f:\{0,1\}^n \to \{0,1\}$ 都可以变成可逆的酉变换：

$$U_f: |x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle$$

<p align="center"><img src="images/02_05_01_q_eval.png" width="700" alt="经典函数 f(x) 与酉变换 U_f 的对比：U_f 保持量子比特 |x⟩ 不变，并把 f(x) 写入辅助量子比特，使其变为 |y ⊕ f(x)⟩"></p>

*图：左：经典函数 $f(x)$，多个比特输入、一个比特输出，不可逆。右：酉变换 $U_f$ 保持输入量子比特不变，并把 $f(x)$ 以 XOR 的方式加到辅助量子比特 $y$ 上。*

当 $y = 0$ 时得到 $f(x)$；当 $y = 1$ 时得到 $\overline{f(x)}$（例如用 `mcx` 实现 3 比特 AND，可分别得到 AND/NAND）。

**基于函数的相位反冲**：令 $y = |-\rangle$：

$$|x\rangle|-\rangle \xrightarrow{U_f} (-1)^{f(x)}|x\rangle|-\rangle$$

**两类预言机**（即黑盒，black box）：

| 预言机 | 作用 |
|---|---|
| 比特预言机（bit oracle）$U_f$ | $\vert x\rangle\vert y\rangle \to \vert x\rangle\vert y \oplus f(x)\rangle$ |
| 相位预言机（phase oracle）$Z_f$ | $\vert x\rangle \to (-1)^{f(x)}\vert x\rangle$；= 令 $y = \vert -\rangle$ 的比特预言机再丢弃量子比特 $y$，或者直接用 MCZ 搭建，无需辅助量子比特 |

<p align="center"><img src="images/02_05_02_oracles.png" width="700" alt="比特预言机 U_f 把 |x⟩|y⟩ 变为 |x⟩|y ⊕ f(x)⟩；相位预言机 Z_f 把 |x⟩ 变为 (−1)^f(x)|x⟩"></p>

*图：比特预言机 $U_f$（左）把 $f(x)$ 写入量子比特 $y$；相位预言机 $Z_f$（右）把 $f(x)$ 写进符号 $(-1)^{f(x)}$。*

<p align="center"><img src="images/02_05_03_oracle_equiv.png" width="400" alt="辅助量子比特处于 |−⟩ 的比特预言机等价于相位预言机"></p>

*图：辅助量子比特处于 $|-\rangle$ 的比特预言机（该量子比特输出时仍为 $|-\rangle$）等价于一个相位预言机。*

### 核心代码

```python
def ghz_cir_c(n):
    # create quantum circuit with n qubits
    qb_mid = n//2
    qc_ghz = QuantumCircuit(n)
    
    # place most significant qubit in equal superposition
    qc_ghz.h(qb_mid)
    
    # apply cx gates between successive pairs of qubits
    for i in reversed(range(qb_mid)):
        qc_ghz.cx(i+1,i)
    
    for i in range(qb_mid,n-1):
        qc_ghz.cx(i,i+1)
    
    return qc_ghz
```
低深度的 GHZ 电路，只在相邻的量子比特之间使用 CX。

> 注意：注释“place most significant qubit in equal superposition”是从 `ghz_cir_a` 照搬过来的；这里 H 作用在中间的量子比特 `qb_mid` 上，而不是最高位的量子比特。

```python
def w_cir(n):
    
    prob_amp = np.sqrt(1/n)          # probability amplitude
    rot_ang = 2*np.arccos(prob_amp)  # initial rotation angle
    
    # create quantum circuit with n qubits
    qc_w = QuantumCircuit(n) 
    
    # probability redistribution
    qc_w.ry(rot_ang,n-1)
    for i in range(n-1,1,-1):
        comp_amp = np.sqrt(i/n)
        rot_ang = 2*np.arccos(prob_amp/(comp_amp))
        qc_w.cry(rot_ang,i,i-1)
    
    # state reshuffling
    for i in range(1, n):
        qc_w.cx(i,i-1)
    
    qc_w.x(n-1)
    
    return qc_w
```
W 态电路；作者在[另一篇文章](https://nbviewer.org/github/diemilio/quantum-playground/blob/main/w-states/w-states.ipynb)中有详细讲解。

```python
QHT = Operator.from_label('H'*n)
W = Statevector(w_cir(n))
y = W.evolve(QHT)
```
用 Qiskit 实现 QHT；notebook 还按照 $\beta_i$ 的公式自己写了 `qht_func(sv)` 进行对照，得到的结果相同。

```python
qc = QuantumCircuit(2)
qc.x(0)
qc.barrier()
ψ_in = Statevector(qc)
qc.h([0,1])
qc.cx(1,0)
qc.h([0,1])
ψ_out = Statevector(qc)
```
相位反冲：H–CX–H 把 $|01\rangle$ 变为 $|11\rangle$，即目标位翻转了控制位。

```python
# create controlled S gate activated by state |01⟩
CC̄S = SGate().control(2, ctrl_state='01')
```
`Gate().control(k, ctrl_state=...)` 由任意一个门创建带 $k$ 个控制位的门；用 `qc.append(gate, qubits)` 把它加入电路。

> 注意：在这个单元格中，notebook 赋值的是 `qψ_in = Statevector(qc)`（多了一个 `q`），显示的却是前一个单元格的 `ψ_in`，所以标为“input”的输出 $|01\rangle$ 是**错误的**。标为“output”的输出是正确的。

> 注意：3.3 节的正文（以及上面的注释“activated by state |01⟩”）说，该门在控制位 $|q_2 q_1\rangle = |01\rangle$ 时激活，并预测 $|01\rangle|1\rangle$ 会获得相位 $i$。但 `ctrl_state` 是按小端序读取的：对于 `qc.append(CC̄S, [2,1,0])`，最右边的字符 `'1'` 对应第一个控制位（$q_2$）。因此该门在 $q_2 = 1$、$q_1 = 0$ 时激活，而输出（与代码一致）显示获得相位 $i$ 的是 $|101\rangle$。同样在这一节中，$k$ 的取值是从 0 到 $2^m - 1$，而不是到 $2^m$。

```python
qc_f = QuantumCircuit(qr_y, qr_x)

# Prepare |x⟩ in equal superposition
qc_f.h(qr_x)
qc_f.barrier()

# Initialize |y⟩ in state |-⟩
qc_f.x(qr_y)
qc_f.h(qr_y)
qc_f.barrier()

# Apply 3-qubit AND gate
qc_f.mcx(qr_x, qr_y)
qc_f.barrier()

# Take |y⟩ back to state |0⟩
qc_f.h(qr_y)
qc_f.x(qr_y)
```
用 3 比特 AND 演示基于函数的相位反冲：只有 $|111\rangle$ 获得负号 $-$。`QuantumRegister(n, name='x')` 为一组量子比特命名。

```python
qc.ccz(0,2,1, ctrl_state='01')             # Apply Zf 
```
直接用 CCZ 搭建相位预言机，无需辅助量子比特：标记 $x = 011$。

> 注意：4.3 节的正文有时说 $x = 010$，有时说状态 $|10\rangle$，但代码和输出标记的都是 **$x = 011$**。代码是正确的。

### 运行结果

| 检查项 | 输出 |
|---|---|
| 4 个基态经过 H+CX | $\vert \Phi^+\rangle, \vert \Psi^+\rangle, \vert \Phi^-\rangle, \vert \Psi^-\rangle$ |
| `ghz_cir_a(5)`、`ghz_cir_b(5)`、`ghz_cir_c(7)` | $\tfrac{\sqrt2}{2}(\vert 0\dots0\rangle + \vert 1\dots1\rangle)$ |
| `w_cir(5)` | 5 个 one-hot 态上的系数均为 $\tfrac{\sqrt5}{5}$ |
| $\vert W_3\rangle$ 的 QHT（Qiskit 与 `qht_func`） | 结果相同，$\tfrac{\sqrt6}{4}\vert 000\rangle + \dots - \tfrac{\sqrt6}{4}\vert 111\rangle$ |
| $\vert 1\rangle\vert -\rangle$ 经过 CX | $-\vert 1\rangle\vert -\rangle$（只是全局相位） |
| $\vert 01\rangle$ 经过 H–CX–H | $\vert 11\rangle$ |
| 控制位处于叠加态、目标位为 $\vert 1\rangle$ 时的 $C\bar C S$ | 只有 $\vert 101\rangle$ 获得系数 $i/2$ |
| 3 比特 AND，$y = 0$ / $y = 1$ | 只有 $\vert 111\rangle$ 给出 $y = 1$ / $y = 0$（AND / NAND） |
| 3 比特 AND 的相位反冲 | 只有 $\vert 1110\rangle$ 带负号 $-$ |
| 相位预言机（MCX + $\vert -\rangle$，或 CCZ） | 只有 $x = 011$ 带负号 $-$ |

### 速记要点

- 贝尔态 = H + CX；GHZ 态 = H + 一串 CX；W 态较难搭建（CRY + CX）。
- $H^{\otimes n}|j\rangle = \frac{1}{\sqrt N}\sum_i (-1)^{i\cdot j}|i\rangle$，为了第 04 部分必须牢记。
- 相位反冲：控制位处于叠加态 + 目标位是特征向量 → 相位反冲到控制位上。
- 预言机：$U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$；当 $y = |-\rangle$ 时得到 $(-1)^{f(x)}|x\rangle$。
- 用 `Gate().control(k, ctrl_state=...)`、`mcx`、`ccz` 搭建预言机。

---

## 本部分用到的 Qiskit API 汇总

| API / 函数 | 用途 | 课 |
|---|---|---|
| `Statevector([...])`、`.from_label('0'/'+'/'-')`、`.from_int(k, dim)` | 创建状态 | 02_01–02_05 |
| `Statevector(qc)` | 电路的输出状态，从 $\vert 0\dots0\rangle$ 开始 | 02_01–02_05 |
| `sv.draw('latex' / 'bloch', convention='vector', reverse_bits=True)` | 显示右矢、向量、布洛赫球 | 02_01–02_05 |
| `sv.evolve(qc 或 Operator)` | 让状态通过电路 / 矩阵 | 02_01–02_03、02_05 |
| `sv.tensor(other)` | 状态的克罗内克积 | 02_02、02_05 |
| `sv.probabilities([qubits])` | 精确概率（全部或部分量子比特） | 02_03、02_04 |
| `sv.sample_counts(n)`、`sv.sample_memory(n)` | 模拟测量 | 02_01、02_03 |
| `sv.measure([qubits])` | 测量一次，返回（结果，测量后的状态） | 02_04 |
| `sv.expectation_value(op)` | 精确期望值 | 02_03 |
| `Operator(qc)`、`Operator.from_label('X'/'0'/'HHH')`、`Operator([[...]])` | 电路 / 门的矩阵 | 02_01–02_05 |
| `op.tensor(other)`、`op1 + op2` | 组合矩阵 | 02_02、02_04 |
| `QuantumCircuit(n, m)`、`QuantumRegister(n, name=)` | 创建电路、量子比特组 | 02_01–02_05 |
| `x, h, z, s, sdg, t, tdg, rx, ry, rz, id` | 单量子比特门 | 02_01–02_05 |
| `cx(c, t, ctrl_state=)`、`cz`、`cry`、`ccx`、`rccx`、`ccz`、`mcx`、`swap`、`cswap` | 多量子比特门 | 02_02–02_05 |
| `SGate().control(k, ctrl_state=)`、`qc.append(gate, qubits)` | 创建受控门并加入电路 | 02_05 |
| `reset`、`measure`、`measure_all`、`barrier` | 制备、测量、分隔电路 | 02_01–02_05 |
| `with qc.if_test((clbit, val)):` | 根据测量结果作用门 | 02_03 |
| `qc.save_statevector(label)` | 在电路中途保存状态（Aer） | 02_03、02_04 |
| `qc.depth(filter)` | 电路深度，例如 T 深度 | 02_04 |
| `transpile(qc, basis_gates=[...])`、`transpile(qc, simulator)` | 把电路转换为原生门集 | 02_04 |
| `BasicSimulator().run(qc, shots=N)` | Qiskit 自带的简单模拟器 | 02_01、02_02 |
| `AerSimulator().run(qc, shots=N)`、`.result().get_counts()`、`.get_statevector()`、`.data()` | Qiskit Aer 模拟器 | 02_03、02_04 |
| `Estimator(mode=AerSimulator())`、`SparsePauliOp.from_operator` | 估计期望值 | 02_03 |
| `plot_histogram`、`plot_distribution` | 绘制测量结果 | 02_01、02_04 |

## 运行方法

在 VS Code 或 Jupyter 中打开 notebook，选择本仓库的 `.venv` 内核，从上到下依次运行。所需的库都列在 [requirements.txt](../../requirements.txt) 中。

- 所有内容都在本地模拟器上运行（`Statevector`、`BasicSimulator`、`AerSimulator`）。02_03 中的 `Estimator(mode=AerSimulator())` 需要安装 `qiskit-ibm-runtime`，但**不需要 IBM 账号**。
- 输出中的电路图和布洛赫球图是用配置文件 [qiskit_settings.conf](../../qiskit_settings.conf)（`circuit_reverse_bits = True`）绘制的。没有这个配置，画出的电路中量子比特的顺序会上下颠倒，但计算结果不变。
- 采样结果（计数，counts）每次运行都会变化；`Statevector`/`Operator` 的结果则不会。
- 02_05 的各节之间共用变量（例如 1.3 节中的 `w_cir` 在第 2 节中被再次使用），所以必须按顺序运行。

---

<!-- nav -->
[← 01 · Classical computing](../01_classical_computing/README.zh-CN.md) · [目录](../../README.zh-CN.md#目录) · [03 · Quantum protocols →](../03_quantum_protocols/README.zh-CN.md)
