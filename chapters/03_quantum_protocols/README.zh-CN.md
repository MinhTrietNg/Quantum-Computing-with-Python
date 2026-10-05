# 03 · Quantum protocols（量子协议）

[Tiếng Việt](README.md) · [English](README.en.md) · **简体中文**

本部分运用前面学过的概念——叠加（superposition）、测量（measurement）、纠缠（entanglement）和贝尔态（Bell state）——构建三个著名的量子协议：防伪的量子货币（quantum money）、量子隐形传态（quantum teleportation）和超密编码（superdense coding）。每一课既用数学讲解原理，又用在模拟器（simulator）上运行的 Qiskit 量子电路加以验证。

> 来源：[03_01](https://learnquantum.io/chapters/03_quantum_protocols/03_01_quantum_money.html)、[03_02](https://learnquantum.io/chapters/03_quantum_protocols/03_02_teleportation.html)、[03_03](https://learnquantum.io/chapters/03_quantum_protocols/03_03_superdense_coding.html) — Diego Emilio Serrano, learnquantum.io, MIT License.

## 目录

| 课 | Notebook | 网页 | 要点 |
|---|---|---|---|
| 03_01 | [03_01_quantum_money.ipynb](03_01_quantum_money.ipynb) | [链接](https://learnquantum.io/chapters/03_quantum_protocols/03_01_quantum_money.html) | 比特基（bit basis）与符号基（sign basis）之间的不确定性原理使量子硬币无法被完美复制；伪造成功的概率随量子比特（qubit）数呈指数下降 |
| 03_02 | [03_02_teleportation.ipynb](03_02_teleportation.ipynb) | [链接](https://learnquantum.io/chapters/03_quantum_protocols/03_02_teleportation.html) | 1 个贝尔对 + 2 个经典比特 = 完整传送 1 个量子比特的状态 |
| 03_03 | [03_03_superdense_coding.ipynb](03_03_superdense_coding.ipynb) | [链接](https://learnquantum.io/chapters/03_quantum_protocols/03_03_superdense_coding.html) | 1 个贝尔对 + 发送 1 个量子比特 = 传输 2 个经典比特 |

原书网站还列出了“Bell Inequalities”（03_04）和“Quantum Key Distribution”（03_05），但上游仓库中这两章只有标题（尚无内容），因此没有收录到这里。

> 本 README 中的代码是从 notebook 中**摘录**的：保留下来的行与原文一字不差（包括原有的英文注释），省略的地方用 `...` 标出，中文注释是另外添加的。代码会用到前面单元格中定义的变量。如果想运行，请从头到尾运行整个 notebook。

---

## 03_01 · Uncertainty & Quantum Money（不确定性原理与量子货币）

**目标** — 通过两个不相容的可观测量（observable）$X$、$Z$ 理解不确定性原理（uncertainty principle），再用它构建 Wiesner 的量子货币协议（论文“Conjugate Coding”，1983 年）。

### 核心知识

**1. 自旋的不确定性（第 1.1 节）**：对于经典磁铁，两台串联的施特恩–格拉赫（Stern-Gerlach，SG）装置（先沿 $x$ 轴，再沿 $z$ 轴）可以确定磁铁处于 I–IV 四个方向中的哪一个。

<p align="center"><img src="images/03_01_02_barmag_SG.png" width="600" alt="磁铁先通过沿 x 轴的 SG 装置，再通过沿 z 轴的 SG 装置，落在两块屏上 I、II、III、IV 四个位置"></p>

*图：经典磁铁：第一台 SG 装置按 $\pm x$ 分开，后面两台 SG 装置按 $\pm z$ 分开，因此 I–IV 每个方向都落在屏上各自的位置。*

电子则不然。电子的自旋（spin）同样可以朝 I–IV 四个方向倾斜，其中 $\theta$ 是自旋与 $+z$ 轴之间的夹角：

<p align="center"><img src="images/03_01_04_spin_orientation.png" width="760" alt="电子自旋在 xz 平面内朝 I、II、III、IV 四个方向倾斜，角度 theta 从 z 轴量起"></p>

*图：$xz$ 平面内的四个自旋方向 I–IV；角 $\theta$ 从 $+z$ 轴量起（I：$\pi/4$，II：$3\pi/4$，III：$5\pi/4$，IV：$7\pi/4$）。*

<p align="center"><img src="images/03_01_03_spin_SG.png" width="600" alt="电子通过沿 x 的 SG 装置，以概率 P(theta) 偏向 +x 或 -x，再通过沿 z 的 SG 装置，以 1/2 的概率向上或向下偏转"></p>

*图：用电子做同样的实验：第一台 SG 装置按概率 $P_{\pm x}(\theta)$ 给出 $\pm x$，随后沿 $z$ 的 SG 装置给出向上或向下，各占 $1/2$。*

- 沿 $x$ 的 SG 装置以概率方式使粒子偏转：$P_{+x}(\theta) = \frac{1}{2}(1+\sin\theta)$，$P_{-x}(\theta) = \frac{1}{2}(1-\sin\theta)$。对于方向 I、II：$P_{+x} \approx 0.854$，$P_{-x} \approx 0.146$（notebook 写的是 $0.853$，因为它截断了多余的位数而不是四舍五入）；方向 III、IV 则正好相反。
- 沿 $x$ 测量之后，自旋被投影到 $\pm x$，所以沿 $z$ 的 SG 装置总是以 $1/2$ 的概率给出向上 / 向下：关于初始 $z$ 方向的信息被“抹掉”了。
- 沿 $x$ 的自旋和沿 $z$ 的自旋是**不相容**（incompatible）的，也称**共轭**（conjugate）的：测量其中一个会增大另一个的不确定度。

**2. 量子比特的不确定性（第 1.2 节；如果只想理解量子货币，可以跳过）**：对于 $xz$ 平面内的量子比特 $|q\rangle = \cos\frac{\theta}{2}|0\rangle + \sin\frac{\theta}{2}|1\rangle$，有：

$$\langle Z\rangle = \cos\theta,\quad \langle X\rangle = \sin\theta,\quad \Delta O^2 = \langle O^2\rangle - \langle O\rangle^2 \;\Rightarrow\; \Delta Z = |\sin\theta|,\quad \Delta X = |\cos\theta|$$

$\Delta Z$ 最小时 $\Delta X$ 最大，反之亦然。更一般地，加入相对相位 $e^{i\varphi}$，并利用不确定关系 $\Delta A\,\Delta B \geq \frac{1}{2}|\langle [A,B]\rangle|$ 以及 $[Z,X] = 2iY$，可得：

$$\Delta Z\,\Delta X \geq |\langle iY\rangle| \quad\Longleftrightarrow\quad |\sin\theta|\sqrt{1-\sin^2\theta\cos^2\varphi} \geq |\sin\theta\sin\varphi|$$

notebook 针对几个 $\varphi$ 值画出两边随 $\theta$ 变化的曲线，然后用 Estimator 加以验证。

> 注意：（1）“In the above, we only consider qubits in the $xy$-plane”这句话中的平面应为 $xz$ 平面（态 $\cos\frac{\theta}{2}|0\rangle + \sin\frac{\theta}{2}|1\rangle$ 的概率幅都是实数）。（2）两边同除以 $|\sin\theta|$ 之后，notebook 论证 $\sqrt{1-\sin^2\theta\cos^2\varphi} \geq |\sin\varphi|$ 成立的理由是“左边的最大值为 1，不小于右边的最大值（也是 1）”。比较两边的最大值并不能证明不等式在每一点上都成立。正确的论证是：因为 $\sin^2\theta \leq 1$，所以 $1-\sin^2\theta\cos^2\varphi \geq 1-\cos^2\varphi = \sin^2\varphi$。（当 $\sin\theta = 0$ 时不能相除，但这时两边都等于 0。）notebook 的结论仍然是正确的。

**3. 量子货币（第 2 节）**

1. **银行发行硬币**：每枚硬币有一个公开的序列号 $S$ 和一个 $n$ 量子比特的量子态。从物理上说，每个量子比特可以是被隔离在硬币中的一个电子的自旋；notebook 明确指出这种技术目前还不存在，所以这是一个理论上的协议。

   <p align="center"><img src="images/03_01_05_coins.png" width="500" alt="量子硬币，每一枚都带有一个量子态和一个序列号，例如 1D062F3ABA"></p>

   *图：每枚硬币都带有各自的量子态（编号 $1, 2, \dots, k$）和一个公开的序列号 $S_k$，例如 `1D062F3ABA`。*

   每个量子比特从 $\{|0\rangle, |1\rangle, |+\rangle, |-\rangle\}$ 中随机选取：从 $|0\rangle$ 出发，用 $X$ 翻转比特，和 / 或用 $H$ 切换基。

   <p align="center"><img src="images/03_01_07_state_select.png" width="450" alt="选择树：从态 0 出发，选择 I 或 X 来决定是否翻转比特，再选择 I 或 H 来决定是否切换基，得到 0、+、1 或 -"></p>

   *图：每个量子比特 $q_i$ 有两次选择：先决定是否翻转比特（$X$），再决定是否切换基（$H$），结果为 $|0\rangle$、$|+\rangle$、$|1\rangle$ 或 $|-\rangle$。*

   以 $n=6$ 为例：$U = II \otimes II \otimes HI \otimes IX \otimes HX \otimes HI$ 给出 $|0\rangle|0\rangle|+\rangle|1\rangle|-\rangle|+\rangle$。

2. **银行保存一个秘密数据库**：序列号 $S$ ↔ 所用的门序列。（BBBW 协议提出用伪随机密钥生成器从 $S$ 生成量子态；notebook 略过了这一点。）
3. **验证**：银行先施加逆电路 $U^\dagger$ 再测量；真硬币**总是**得到全 0 串。
4. **伪造者**不知道 $U$：
   - 直接在比特基下测量：处于 $|\pm\rangle$ 的量子比特给出随机结果。
   - 在符号基下测量（先对所有量子比特施加 $H$）：处于 $|0\rangle, |1\rangle$ 的量子比特给出随机结果。
   - 只能测量一次，因为测量会使量子态坍缩。靠瞎猜**完全**猜中全部 $n$ 个量子比特的概率是 $(1/4)^n$；$n=6$ 时为 $\approx 0.000244$。

   但 $(1/4)^n$ 还不是伪造成功的概率：一个基猜错的量子比特仍有 $1/2$ 的概率通过验证。伪造者的目标是从 1 枚真硬币得到**两枚**都能通过验证的硬币。各个量子比特相互独立，所以总概率是单个量子比特概率的 $n$ 次方：

   | 策略（从 1 枚真硬币出发） | 每个量子比特 | 两枚都通过 | $n=6$ |
   |---|---|---|---|
   | 保留真硬币，按盲猜制备第二枚 | $1/2$ | $(1/2)^n$ | $\approx 0.016$ |
   | 对每个量子比特在随机选择的基下测量，再按测量结果制备两份 | $5/8$ | $(5/8)^n$ | $\approx 0.060$ |
   | 最优复制操作（[Molina, Vidick, Watrous 2012](https://arxiv.org/abs/1202.4010)） | $3/4$ | $(3/4)^n$ | $\approx 0.178$ |

   （采用“先测量、再制备”的方法时，*每一枚*硬币单独通过的概率是 $(3/4)^n$，但两枚同时通过的概率只有 $(5/8)^n$。）所有策略的成功概率都随量子比特数的增加呈指数下降，但示例中的 $n=6$ 还太小，不足以保证安全。

5. **为什么安全**：$\{|+\rangle, |-\rangle\}$ 是与 $\{|0\rangle, |1\rangle\}$ 共轭的基（不确定性），而且根据**不可克隆定理**（no-cloning theorem），无法完美复制一个未知的量子态。书中还写道：伪造者最多只能造出*纠缠*的副本，但银行一旦验证其中一枚，另一枚就会坍缩而变得无用。实际上另一枚不一定作废：用 $CX$ 制作纠缠副本（真硬币的量子比特作控制位，处于 $|0\rangle$ 的新硬币量子比特作目标位）时，两枚硬币同时通过的概率是 $(5/8)^n$，而最优的伪造者可以达到 $(3/4)^n$（见上表）。该协议还假定伪造者不能多次试探银行的验证结果。

这一课最后提到了“虚拟量子货币”和量子闪电（quantum lightning，Zhandry18）等方向，作为与区块链结合的思路。

> 注意：在第 2 节中，notebook 有一处笔误和两处言过其实的说法：（1）“the probability of the criminal successfully guessing the state grows with the number of qubits”这句话中的概率实际上随 $n$ *减小*，正如公式 $(1/4)^n$ 所示；（2）$(1/4)^n$ 是**完全**猜中整个量子态的概率，而不是伪造成功的概率：盲猜得到的假币仍有 $(1/2)^n$ 的概率通过验证，而最优的伪造者在 $n=6$ 时让两枚硬币同时通过的概率为 $(3/4)^n \approx 0.178$（见第 4 点中的表格）；（3）“the second coin's state will collapse making it unusable”这句话并不完全正确（见第 5 点）。

### 核心代码

```python
# Use the Paramater class to define arbitrary angles of θ and φ
θ = Parameter('θ')
φ = Parameter('φ')

# Circuit to prepare state cos(θ/2)|0⟩+exp(iφ)sin(θ/2)|1⟩
qc = QuantumCircuit(1)
qc.ry(θ,0)
qc.p(φ,0)
```

参数化电路（`qiskit.circuit.Parameter`）：`ry(θ)` 设定概率幅，`p(φ)` 加上相对相位。具体的数值在运行 Estimator 时才代入。

```python
estimator = Estimator(mode=AerSimulator())
...
# Define list of observables:
obsv_lst = [[SparsePauliOp(["Z"],[1])],
            [SparsePauliOp(["X"],[1])],
            [SparsePauliOp(["Y"],[1])]]
...
# Run estimator simulation
job = estimator.run([(qc,obsv_lst,angles,0.01)])
exp_vals = job.result()[0].data.evs

# Extract standard deviations for X,Z and expectation values for Y
ΔZ_lst = np.sqrt(1-exp_vals[0]**2)  # ΔZ = √(1-⟨Z⟩²)
ΔX_lst = np.sqrt(1-exp_vals[1]**2)  # ΔX = √(1-⟨X⟩²)
ΔZΔX_lst = ΔZ_lst * ΔX_lst          # ΔZΔX
Ys_lst = np.abs(exp_vals[2])        # |⟨Y⟩|
```

`qiskit_ibm_runtime.Estimator`（V2 版）在 `AerSimulator` 上运行。一个 PUB `(circuit, observables, parameter_values, precision)`：3 个 `SparsePauliOp` 形式的可观测量 × 21 个 $\theta$ 值（固定 $\varphi = 9\pi/10$），精度为 0.01；`.data.evs` 返回期望值数组。notebook 中注明：$Y$ 的系数本应是 $i$，但因为只取绝对值，所以用了 1。

```python
def gen_coin(n):
    ...
    # n-qubit circuit
    qc = QuantumCircuit(n)

    # Iterate over each qubit
    for i in range(n-1,-1,-1):
        state = np.random.choice(['0','1','+','-'])

        # select if bit should be flipped
        if state in ['1', '-']: qc.x(i)
        else: qc.id(i)

        # select if basis should be change
        if state in ['+','-']: qc.h(i)
        else: qc.id(i)
    ...
```

这是“银行”使用的函数：为每个量子比特随机选择一个态，然后施加 $X$ 和 / 或 $H$（`qc.id` 只起占位作用）。函数还会返回该量子态的 LaTeX 字符串，用 `IPython.display.Math` 显示（这部分在摘录中省略了）。循环从量子比特 $n-1$ 倒数到 0，所以这个字符串把最高位的量子比特写在最左边，正好符合 Qiskit 的小端序（little-endian）。

```python
# Generate inverse of circuit
qc_inv = qc.inverse()
...
# Apply inverse circuit to coin statevector
sv_check = sv_coin.evolve(qc_inv)

# Display probability of measuring all-zeros string
result_probs = sv_check.probabilities_dict(decimals=5)
plot_distribution(result_probs)
```

验证硬币：`QuantumCircuit.inverse()` 生成 $U^\dagger$，`Statevector.evolve` 把电路作用到态矢量（statevector）上，`probabilities_dict` 和 `plot_distribution` 显示概率分布。伪造者用 `sv_coin.probabilities_dict()`（在比特基下测量）以及 `sv_coin.evolve(qc_h)`（其中 `qc_h.h(range(n))`，在符号基下测量）来模拟。

### 运行结果

- 不确定性曲线图（4 个 $\varphi$ 值）：$\Delta Z\Delta X$ 曲线始终位于 $|\langle iY\rangle|$ 曲线之上或与之相接。Estimator 曲线图（$\varphi = 9\pi/10 \approx 2.8274$）：每个量的 21 个点都紧贴理论曲线。
- notebook 中保存的那次运行生成了 $n=6$ 的硬币：$|+\rangle \otimes |1\rangle \otimes |0\rangle \otimes |0\rangle \otimes |1\rangle \otimes |0\rangle$（从 $q_5$ 到 $q_0$；电路中只有 $q_5$ 上的 $H$，以及 $q_4$ 和 $q_1$ 上的 $X$）。
- 用 $U^\dagger$ 验证：分布中只有 `000000`，概率为 1.0。
- 伪造者在比特基下测量：得到 `010010` 和 `110010` 两种结果，各占 0.5。在符号基下测量：得到 32 种结果，各占 $\approx 0.031$（$1/32$），最左边的比特总是 0。这次运行中 6 个量子比特只有 1 个属于符号基（notebook 所说的“roughly half”是平均情况），所以第一个分布很窄，第二个分布很宽。

### 速记要点

- $X$ 和 $Z$ 是一对共轭的可观测量：$\Delta Z = |\sin\theta|$，$\Delta X = |\cos\theta|$，两者不可能同时很小。
- 硬币 = 公开的序列号 + 从 $\{|0\rangle,|1\rangle,|+\rangle,|-\rangle\}$ 中随机选取的 $n$ 个量子比特；只有银行知道所用的基（必须保存一份秘密清单）。这是一个理论协议，目前还没有实现它的技术。
- 验证 = 施加 $U^\dagger$ 后测量，真硬币得到全 0。
- 两层保护：测量会破坏量子态（不确定性），以及不可克隆定理。完全猜中的概率：$(1/4)^n$；得到两枚都能通过验证的硬币的概率：从 $(1/2)^n$（盲猜）到 $(3/4)^n$（最优），都呈指数下降。
- Estimator V2：`estimator.run([(qc, observables, params, precision)])`，然后读取 `result()[0].data.evs`。

---

## 03_02 · Quantum Teleportation（量子隐形传态）

**目标** — 在双方事先共享一对纠缠量子比特的前提下，只用 **2 个经典比特**就把任意一个量子比特的*完整*状态从 Alice 发送给 Bob（Bennett 等人，1993 年）。

### 核心知识

**与经典方法比较**：要让 Bob 制备出 $|q\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\varphi}\sin\frac{\theta}{2}|1\rangle$，Alice 必须发送两个角度 $(\theta,\varphi)$，例如采用 FP16 格式（每个角度 16 比特），而且得到的仍然只是近似值。

<p align="center"><img src="images/03_02_01_classical_transmit.png" width="760" alt="Alice 把舍入后的两个角度以比特串形式通过经典信道发送；Bob 用它们设置 Ry 门和 P 门，制备出近似的量子态"></p>

*图：经典方法：Alice 把舍入后的两个角度 $(\tilde\theta, \tilde\varphi)$ 以比特串形式通过经典信道发送；Bob 用它们设置 $R_y$ 门和 $P$ 门，制备出近似态 $|\tilde q\rangle$。*

量子隐形传态只需发送 2 个经典比特（外加一对事先共享的纠缠量子比特），Bob 就能得到与 Alice 手中完全相同的量子态，而不是近似值。代价是：Bob 得到的只是一个处于 $|q\rangle$ 态的*量子比特*，他无法从中读出两个角度 $(\theta,\varphi)$：测量一个量子比特只能得到 1 个比特。

> 注意：在 notebook 的 FP16 示例中，两个比特串的顺序弄反了。`0011101001001000` 是 $\pi/4 \approx 0.785$，`0011111001001000` 是 $\pi/2 \approx 1.570$，所以对于 $(\theta,\varphi) = (\pi/2, \pi/4)$，应当发送 `(0011111001001000, 0011101001001000)`。notebook 中的近似值对 $(1.570, 0.785)$ 则是正确的。

要进行隐形传态，Alice 和 Bob 需要事先共享一对纠缠量子比特：Alice 制备一个贝尔对，然后通过量子信道把其中一个量子比特发给 Bob。此后就只需要经典信道了。

<p align="center"><img src="images/03_02_02_quantum_transmit.png" width="675" alt="Alice 和 Bob 之间有一条量子信道（用来发送一个纠缠量子比特）和一条经典信道"></p>

*图：Alice 与 Bob 之间的两条信道：量子信道（事先发送纠缠对中的一个量子比特）和经典信道（用来发送 2 个测量结果比特）。*

**步骤（按照 notebook 中的电路图）**：

<p align="center"><img src="images/03_02_03_teleportation_circuit.png" width="760" alt="隐形传态电路图：Alice 制备贝尔对并把一个量子比特发给 Bob，用 Ry 和 P 制备 q，施加 CX 和 H，测量两个量子比特；Bob 根据经典信道收到的两个比特施加 X 和 Z；图中标出 psi 1 到 psi 5 各个时刻"></p>

*图：隐形传态电路，时间向右推进，竖直方向表示空间距离。中间量子比特（Alice 手中的那一半贝尔对）的测量结果控制 $X$，最上面量子比特（$|q\rangle$）的测量结果控制 $Z$；虚线标出 $|\psi\rangle_1$ 到 $|\psi\rangle_5$。*

0. Alice 初始化 3 个量子比特 $|000\rangle_A$。
1. Alice 在两个量子比特上制备贝尔态 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$，然后把其中一个发给 Bob：
   $|\psi\rangle_1 = \frac{1}{\sqrt{2}}|0\rangle_A(|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B)$。
2. 需要发送时，Alice 制备要发送的态 $|q\rangle = \alpha|0\rangle + \beta|1\rangle$（用旋转门制备，$\alpha = \cos\frac{\theta}{2}$，$\beta = e^{i\varphi}\sin\frac{\theta}{2}$）。把整个系统按 Alice 两个量子比特的 4 个贝尔态重新写出：

$$|\psi\rangle_2 = \tfrac{1}{2}\Big[|\Phi^+\rangle_A(\alpha|0\rangle+\beta|1\rangle)_B + |\Psi^+\rangle_A(\alpha|1\rangle+\beta|0\rangle)_B + |\Phi^-\rangle_A(\alpha|0\rangle-\beta|1\rangle)_B + |\Psi^-\rangle_A(\alpha|1\rangle-\beta|0\rangle)_B\Big]$$

   如果 Alice 在贝尔基下测量自己的两个量子比特，Bob 的量子比特就会处于 $|q\rangle$ 的 4 种变体之一，它们之间只差一个比特翻转、相位翻转或两者兼有。这只是把同一个态换一组基来写：在 Bob 收到 2 个比特之前，Bob 那个量子比特单独的状态——约化密度矩阵（reduced density matrix）——始终是 $I/2$，与 $|q\rangle$ 无关。（notebook 简短讨论了这种描述方式所隐含的、有争议的“非定域性”以及其他诠释，然后在标准形式体系下继续推导。）
3. Alice 先施加 $CX$ 再施加 $H$，从贝尔基换到计算基：

$$|\psi\rangle_3 = \tfrac{1}{2}\Big[|00\rangle(\alpha|0\rangle+\beta|1\rangle) + |01\rangle(\alpha|1\rangle+\beta|0\rangle) + |10\rangle(\alpha|0\rangle-\beta|1\rangle) + |11\rangle(\alpha|1\rangle-\beta|0\rangle)\Big]$$

4. Alice 测量两个量子比特：`00`、`01`、`10`、`11` 每种结果（第一位 $j$ 来自量子比特 $|q\rangle$，第二位 $i$ 来自贝尔对的一半）出现的概率都是 $1/4$，并给 Bob 留下上式中对应的态。
5. Alice 通过经典信道把 2 个比特 $(j,i)$ 发给 Bob。Bob 进行纠正：$|\psi\rangle_5 = Z^j X^i|\psi\rangle_4 = \alpha|0\rangle + \beta|1\rangle = |q\rangle$（其中 $X^0 = Z^0 = I$）。

**为什么不会超光速**：在收到 2 个经典比特之前，Bob 不知道该做什么纠正。在此之前，即使 Alice 已经完成测量，就 Bob 所知，他的量子比特仍处于 $I/2$ 态（4 种可能的均匀混合，每种 $1/4$），所以 Bob 还没有得到任何信息；而这 2 个比特要经由经典信道传送，不可能比光更快。该协议传送的只是*量子态*，并不传送物质或能量；Alice 原来的量子比特被测量后便失去了 $|q\rangle$ 态，这与不可克隆定理相符。**为什么贝尔对很有价值**：它是*事先*建立好的，所以等 $|q\rangle$ 准备好时，只需要再发送 2 个比特。

**多个量子比特（第 2.2 节）**：每个要发送的量子比特都各自使用一个贝尔对和一对经典比特。notebook 中的例子用 3 个贝尔对（Alice 有 6 个量子比特，Bob 有 3 个）发送 $|q\rangle = \frac{1}{\sqrt{3}}(|001\rangle - |010\rangle + |100\rangle)$。

### 核心代码

```python
qra = QuantumRegister(2,name="Alice q")
qrb = QuantumRegister(1,name="Bob q")
cra = ClassicalRegister(2, name="Alice c")

qc = QuantumCircuit(qrb,qra,cra)   # qubit 0 = Bob, qubit 1 = qra[0], qubit 2 = qra[1]

# Alice and Bob share entangled Bell state
qc.h(qra[0])
qc.cx(qra[0],qrb[0])
qc.barrier()

# Alice prepares state |q⟩ = 1/√2|0⟩ - i/√2|1⟩
qc.ry(np.pi/2,qra[1])
qc.p(-np.pi/2,qra[1])
qc.barrier()

# Alice changes from Bell to Computational basis
qc.cx(qra[1],qra[0])
qc.h(qra[1])
qc.barrier()

# Alice measures her qubits
qc.measure(qra,cra)                # cra[0] <- qra[0] (贝尔对的一半), cra[1] <- qra[1] (|q⟩)
```

用带名字的 `QuantumRegister` / `ClassicalRegister` 区分 Alice 和 Bob 的量子比特。由于先传入的是 `qrb`，量子比特 0 属于 Bob；`qra[0]` 是 Alice 手中的那一半贝尔对，`qra[1]` 存放要发送的态。

```python
# Bob applies X, Z gates conditioned on Alice's results
with qc.if_test((cra[0], 1)): qc.x(0)
with qc.if_test((cra[1], 1)): qc.z(0)

qc.save_statevector('ψout')
```

用 `QuantumCircuit.if_test` 实现动态的经典控制（这是现代 API，取代了已弃用的 `c_if`）：若比特 `cra[0]`（贝尔对那一半的测量结果，即比特 $i$）为 1，就施加 $X$；若 `cra[1]`（量子比特 $|q\rangle$ 的测量结果，即比特 $j$）为 1，就施加 $Z$。`save_statevector` 是 Qiskit Aer 的指令，用来保存电路末尾的态矢量。

```python
result = simulator.run(qc, shots=1, memory=True).result()
alices_bits = result.get_memory()[0]
ψout = result.data().get('ψout')

ρout = partial_trace(ψout,[1,2])
bobs_state = DensityMatrix(np.round(ρout, 8)).to_statevector()
```

在 `AerSimulator` 上以 `memory=True` 运行 1 个 shot（单次运行与测量），以获取 Alice 测得的比特串。`partial_trace` 求偏迹（partial trace），去掉量子比特 1、2（Alice 的），剩下 Bob 的密度矩阵（density matrix）。由于这个态是纯态（pure），`DensityMatrix(...).to_statevector()` 可以把它转换回态矢量；`np.round` 用来消除数值计算误差。

```python
# Alice and Bob share two entangled Bell states
qc.h([qra[i] for i in range(3)])
qc.cx([qra[i] for i in reversed(range(3))],[qrb[i] for i in reversed(range(3))])
...
for i in range(3):
    with qc.if_test((cra[i], 1)): qc.x(i)
    with qc.if_test((cra[i+3], 1)): qc.z(i)
    if i <2: qc.barrier()
```

多量子比特版本：`h` / `cx` 接受量子比特列表，一次创建 3 个贝尔对；3 量子比特的态在 `qra[3..5]` 上用 `x`、`cry`、`cx`、`z` 制备；Bob 用比特对 `(cra[i], cra[i+3])` 逐个纠正各量子比特。模拟时，`partial_trace(ψout, [3..8])` 保留 Bob 的 3 个量子比特。

> 注意：多量子比特单元格中的注释与代码不符：“two entangled Bell states”（实际创建了 3 对）以及“Alice prepares state |w⟩ = 1/2|01⟩ - √3/2|10⟩”（电路实际制备的是 $\frac{1}{\sqrt{3}}(|001\rangle - |010\rangle + |100\rangle)$，与输出一致）。此外，在单量子比特的例子中，打印语句 `(j,i) = ({alices_bits[1]},{alices_bits[0]})` 的标签弄反了：Qiskit 的 memory 字符串先写高位比特（只令 `cra[0] = 1` 试运行，得到的字符串是 `01`），所以 `alices_bits[0]` 是 `cra[1]`（比特 $j$），`alices_bits[1]` 是 `cra[0]`（比特 $i$，控制 $X$）。这行实际打印的是 $(i,j)$；`alices_bits` 字符串本身已经是正确的 $ji$ 顺序。这一点不影响 Bob 的最终态。

### 运行结果

- **1 个量子比特**，运行 5 次：Alice 依次测得（按打印出的标签）`(0,1)`、`(0,0)`、`(1,1)`、`(0,1)`、`(0,0)`，即真正的 $(j,i)$ 为 $(1,0)$、$(0,0)$、$(1,1)$、$(1,0)$、$(0,0)$（见上面的注意）。每一次 Bob 得到的都是 $\frac{\sqrt{2}}{2}|0\rangle - \frac{\sqrt{2}\,i}{2}|1\rangle$，正好等于 Alice 制备的 $|q\rangle$。
- **3 个量子比特**，运行 5 次：Alice 测得 `011100`、`111100`、`011001`、`001110`、`100001`。每一次 Bob 得到的都是 $\frac{\sqrt{3}}{3}|001\rangle - \frac{\sqrt{3}}{3}|010\rangle + \frac{\sqrt{3}}{3}|100\rangle$。

### 速记要点

- 资源：1 个共享的贝尔对 + 2 个经典比特 → 传送 1 个量子比特的状态（贝尔对被消耗掉，Alice 原来的量子比特失去 $|q\rangle$ 态）。
- Alice 的电路：$CX$（量子比特 $|q\rangle$ 作控制位）→ 对量子比特 $|q\rangle$ 施加 $H$ → 测量 2 个量子比特。
- Bob 的纠正：$Z^j X^i$；$X$ 由贝尔对中那个量子比特的测量比特决定，$Z$ 由量子比特 $|q\rangle$ 的测量比特决定。
- Alice 的测量结果是随机的（每种可能各 $1/4$），但 Bob 的最终态总是 $|q\rangle$。
- Qiskit：`if_test` 用于经典控制，`save_statevector` + `partial_trace` 用来查看 Bob 的态。

---

## 03_03 · Superdense Coding（超密编码）

**目标** — 借助一个事先共享的贝尔对，通过传输 **1 个量子比特**来发送 **2 个经典比特**。这是隐形传态的“反方向”（Bennett 和 Wiesner；1992 年发表）。

### 核心知识

与隐形传态不同：这里不需要经典信道，但量子信道还必须再传送一个量子比特。把用来共享贝尔对的那个量子比特也算上，传送 2 个比特仍然要发送 2 个量子比特；好处在于第一个量子比特可以提前发送，那时还没有要传的消息。如果没有共享的纠缠对，1 个量子比特最多只能携带 1 个经典比特（Holevo 定理；notebook 中没有提到）。

<p align="center"><img src="images/03_03_01_superdense_transmit.png" width="675" alt="Alice 通过量子信道向 Bob 发送两个量子比特：q0 是纠缠量子比特，q1 是编码量子比特；没有经典信道"></p>

*图：只有量子信道：$q_0$ 是纠缠量子比特，$q_1$ 是携带 2 个已编码比特的量子比特；没有经典信道。*

<p align="center"><img src="images/03_03_02_superdense_circuit.png" width="760" alt="超密编码电路：Alice 用 H 和 CX 制备贝尔对，然后把一个量子比特发给 Bob；Alice 根据比特 i 施加 X、根据比特 j 施加 Z，再发送自己的量子比特；Bob 施加 CX、H 并测量两个量子比特；图中标出 psi 1 到 psi 3 各个时刻"></p>

*图：超密编码电路：Alice 根据比特 $i$ 施加 $X$、根据比特 $j$ 施加 $Z$ 到自己的量子比特上，然后通过量子信道把它发出；Bob 施加 $CX$（以刚收到的量子比特作控制位）和 $H$，然后测量；虚线标出 $|\psi\rangle_1$ 到 $|\psi\rangle_3$。*

0. Alice 初始化 $|00\rangle_A$。
1. Alice 制备 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B)$，并把一个量子比特发给 Bob。
2. Alice 把 2 个比特 $(j,i)$ 编码到自己的量子比特上：若 $i=1$ 则施加 $X$，然后若 $j=1$ 再施加 $Z$：
   $|\psi\rangle_2 = (Z^j \otimes I)(X^i \otimes I)|\psi\rangle_1$。结果是 4 个贝尔态之一：

| $(j,i)$ | Alice 施加的门 | $\vert\psi\rangle_2$ | Bob 的测量结果（第 3 步之后） |
|---|---|---|---|
| (0,0) | $I$ | $\vert\Phi^+\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle + \vert 11\rangle)$ | `00` |
| (0,1) | $X$ | $\vert\Psi^+\rangle = \frac{1}{\sqrt{2}}(\vert 10\rangle + \vert 01\rangle)$ | `01` |
| (1,0) | $Z$ | $\vert\Phi^-\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle - \vert 11\rangle)$ | `10` |
| (1,1) | $ZX$ | $\vert\Psi^-\rangle$（notebook 中写作 $\frac{-1}{\sqrt{2}}(\vert 10\rangle - \vert 01\rangle)$） | `11` |

   （在右矢（ket）中，Alice 的量子比特写在前面，Bob 的量子比特写在后面。Bob 测得的比特串也是这个顺序，与代码中 Qiskit 的 `memory` 字符串一致，因为 `cr[1]` 取自 Alice 的量子比特。）
3. Alice 把自己的量子比特发给 Bob。Bob 施加 $CX$（以从 Alice 那里收到的量子比特作控制位、Bob 自己的量子比特作目标位），再对从 Alice 那里收到的量子比特施加 $H$：$|\psi\rangle_3 = (H\otimes I)\,CX\,|\psi\rangle_2$，把 4 个贝尔态分别变回 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$。Bob 测量后以 100% 的概率得到正确的 $(j,i)$。

**为什么可行**：4 个贝尔态两两正交，因此在贝尔基下做一次测量就能把它们完全区分开。Alice 只需对自己的量子比特做局域操作，就能从这 4 个态中任选一个。

**扩展**：有 $n$ 个贝尔对时，Alice 可以发送 $2n$ 个比特（notebook 用的是 $n=3$，即 6 个比特）。

> 注意：notebook 中最后的结果表（第 3 步之后）仍然标为 $|\psi\rangle_2$，应为 $|\psi\rangle_3$。

### 核心代码

```python
# Alice selects qubits to encode (picked at random for demo purposes)
alice_bits = np.random.randint(2,size=2)

qr = QuantumRegister(2,name="q")
cr = ClassicalRegister(2, name="Bob c")

qc = QuantumCircuit(qr,cr)

# Alice and Bob share entangled Bell state
qc.h(qr[1])
qc.cx(qr[1],qr[0])
qc.barrier()

# Alice encodes classical bits on her qubit
if alice_bits[1] == 1: qc.x(1)       # alice_bits[1] 是比特 i
if alice_bits[0] == 1: qc.z(1)       # alice_bits[0] 是比特 j
qc.barrier()

# Bob changes from Bell to Computational basis
qc.cx(qr[1],qr[0])
qc.h(qr[1])
qc.barrier()

# Bob measures all qubits
qc.measure(qr,cr)
```

量子比特 1（`qr[1]`）属于 Alice，量子比特 0 属于 Bob。编码门是在*构建*电路时用 Python 的 `if` 添加的（而不是像 `if_test` 那样在电路内部做经典控制），因为 Alice 事先就知道自己的比特。

```python
# run simulation
simulator = AerSimulator()
qc_t = transpile(qc, simulator)

bob_bits = simulator.run(qc_t, shots=1, memory=True).result().get_memory()[0]
```

`transpile` 针对后端（backend）编译电路，然后运行 1 个 shot，并用 `get_memory()` 读出 Bob 测得的比特串。

```python
for qbit, bit_pair in enumerate(reversed(alice_bit_pairs)):
    if bit_pair[1] == 1: qc.x(qr_encode[qbit])
    if bit_pair[0] == 1: qc.z(qr_encode[qbit])
...
for qbit in range(n):
    qc.measure(qr_entangle[qbit],cr[2*qbit])
    qc.measure(qr_encode[qbit],cr[2*qbit+1])
```

$n$ 对版本：两个寄存器 `entangle` / `encode`，每一对比特编码到一个 `encode` 量子比特上。`reversed` 的遍历顺序加上经典比特的分配方式，使 Bob 读出的比特串与 Alice 的比特串顺序相同（Qiskit 先打印高位比特）。

### 运行结果

- 1 对：`Alice enconded bits (1,1)`、`Bob recovered bits (1,1)`（保存的电路中同时有 $X$ 和 $Z$）。这两行按 `(alice_bits[1], alice_bits[0])` 和 `(bob_bits[1], bob_bits[0])` 的顺序打印，即 $(i,j)$，与上文的 $(j,i)$ 约定相反；不过双方按相同的顺序打印，所以仍然可以比较，而且对 `(1,1)` 来说并无区别。
- 3 对：`Alice encoded bits 000100`、`Bob recovered bits 000100`（保存的电路中只有一个 $X$ 门，作用在 `encode[1]` 上）。

比特是随机选取的，所以每次重新运行的结果都会不同，但 Bob 的比特总是与 Alice 的比特一致。

### 速记要点

- 资源：1 个共享的贝尔对 + 发送 1 个量子比特 → 传输 2 个比特。
- Alice 编码：对自己的量子比特先施加 $X^i$ 再施加 $Z^j$，得到 4 个贝尔态之一。
- Bob 解码：$CX$ → $H$ → 测量，这正是“贝尔基 → 计算基”的电路，与隐形传态中 Alice 的那一步相同。
- 隐形传态与超密编码互为对偶：隐形传态发送 2 个经典比特来传送 1 个量子比特的状态；超密编码发送 1 个量子比特来传送 2 个经典比特。两者都需要事先共享的纠缠对。

---

## 本部分用到的 Qiskit API 汇总

| API / 函数 | 用途 | 课 |
|---|---|---|
| `QuantumCircuit`、`.h`、`.x`、`.z`、`.id`、`.cx`、`.ry`、`.p`、`.cry` | 构建电路，单量子比特门和双量子比特门 | 03_01、03_02、03_03 |
| `QuantumRegister`、`ClassicalRegister` | 带名字的寄存器（Alice / Bob） | 03_02、03_03 |
| `qiskit.circuit.Parameter` | 带参数 $\theta$、$\varphi$ 的电路 | 03_01 |
| `SparsePauliOp` | 定义可观测量 $Z$、$X$、$Y$ | 03_01 |
| `qiskit_ibm_runtime.Estimator(mode=AerSimulator())` | 计算期望值（V2 原语，PUB 带 precision） | 03_01 |
| `Statevector`、`.evolve`、`.probabilities_dict` | 模拟态矢量和测量概率 | 03_01 |
| `QuantumCircuit.inverse()` | 逆电路 $U^\dagger$，用于验证硬币 | 03_01 |
| `plot_distribution` | 绘制概率分布 | 03_01 |
| `.measure`、`.barrier` | 测量；在电路图中分隔各个步骤 | 03_02、03_03 |
| `QuantumCircuit.if_test` | 根据经典比特的值施加门（动态电路，dynamic circuit） | 03_02 |
| `.save_statevector`（Aer） | 在模拟过程中保存态矢量 | 03_02 |
| `AerSimulator().run(..., shots=1, memory=True)`、`get_memory()` | 运行一个 shot 并获取比特串 | 03_02、03_03 |
| `partial_trace`、`DensityMatrix.to_statevector()` | 分离出 Bob 自己的态 | 03_02 |
| `transpile` | 针对模拟器编译电路 | 03_03 |
| `qc.draw(cregbundle=False, fold=-1, idle_wires=True)` | 绘制电路 | 03_01、03_02、03_03 |

## 运行方法

- 用 Jupyter 或 VS Code 打开 notebook，选择本仓库的 `.venv` 内核，从上到下依次运行。
- 所需的库列在 [`requirements.txt`](../../requirements.txt) 中（在仓库根目录安装：`pip install -r requirements.txt`）。
- 所有内容都在本地模拟器（`AerSimulator`、`Statevector`）上运行。第 03_01 课中的 `qiskit_ibm_runtime.Estimator(mode=AerSimulator())` 需要安装 `qiskit-ibm-runtime` 包，但不需要 IBM 账号。
- 这些课用到了随机数（硬币、Alice 的比特、测量结果），所以每次运行的输出都会与保存的版本不同，但结论保持不变。

---

<!-- nav -->
[← 02 · Quantum computing](../02_quantum_computing/README.zh-CN.md) · [目录](../../README.zh-CN.md#目录) · [04 · Quantum algorithms →](../04_quantum_algorithms/README.zh-CN.md)
