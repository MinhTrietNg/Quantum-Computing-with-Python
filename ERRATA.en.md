# Known errors in the original textbook

[Tiếng Việt](ERRATA.md) · **English** · [简体中文](ERRATA.zh-CN.md)

The notebooks in [chapters/](chapters/) are kept **verbatim** from the
[original](https://github.com/learn-quantum/lqc-textbook) (commit `7abf73c`), errors included. The errors below
were found by careful cross-checking while reading. Each error is also noted in place (as a `> Note:`) in the README of the
corresponding part, with a detailed explanation.

Severity:

- **Code**: an error in the code that makes the output or the conclusion wrong.
- **Content**: a wrong statement about the subject matter.
- **Possibly outdated**: correct when the book was written but may no longer be correct for today's software and services.
- **Typos**: an error in a formula, a comment or the text; it does not affect the code.

## Code

| Lesson | Error | Effect | Fix |
|---|---|---|---|
| [02_01](chapters/02_quantum_computing/README.en.md) | `one = Statevector([1, 0])`, which is $\vert 0\rangle$, not $\vert 1\rangle$ | None, because a later cell overwrites it with `from_label('1')` | `Statevector([0, 1])` |
| [02_05](chapters/02_quantum_computing/README.en.md) | The multi-qubit kickback cell assigns `qψ_in` (with an extra `q`) but displays the `ψ_in` of the previous cell | The "input" line of the output reads $\vert 01\rangle$, which is wrong; the "output" line is correct | Change `qψ_in` to `ψ_in` |
| [04_01](chapters/04_quantum_algorithms/README.en.md) | `black_box()` uses `np.random.randint(1,3)`, so it only generates circuit 1 or 2, that is, **constant functions only** | The two right/wrong charts of section 1.1 do not reflect the full problem | `np.random.randint(1,5)` |
| [04_04](chapters/04_quantum_algorithms/README.en.md) | `Uf_M_marked(n, M)` picks the elements with `np.random.randint(N, size=M)`, so they **can repeat**; the saved output is `['001', '001']` | Two identical MCX gates cancel each other, and the oracle marks nothing | `np.random.choice(N, size=M, replace=False)` |
| [04_04](chapters/04_quantum_algorithms/README.en.md) | The line `found after: {x_in} tries` prints the **index** $x$ | The real number of tries is `x_in + 1` | Print `x_in + 1` |

## Content

| Lesson | Error | What it should be |
|---|---|---|
| [02_03](chapters/02_quantum_computing/README.en.md) | Says $\{H, S, CX\}$ is enough to approximate every gate | This set only generates the Clifford group (which a classical computer can simulate efficiently, the Gottesman–Knill theorem); $T$ must be added (Clifford+T). Lesson 02_04 of the book states this correctly |
| [03_01](chapters/03_quantum_protocols/README.en.md) | The formula $(1/4)^n$ placed next to the sentence about "a forger who succeeds" is easily read as the probability that the forgery succeeds | It is the probability of blindly guessing the state **exactly**. A forger who measures each qubit at random and then re-prepares it gets **one** coin through the check with probability $(3/4)^n$ (about 0.18 for $n=6$); for **both** coins to pass together, this method only reaches $(5/8)^n$, and even the best method only reaches $(3/4)^n$ (the optimal result has been proven: Molina–Vidick–Watrous 2012, [arXiv:1202.4010](https://arxiv.org/abs/1202.4010)). All of them decrease exponentially |
| [03_01](chapters/03_quantum_protocols/README.en.md) | "the probability of the criminal successfully guessing the state grows with the number of qubits" | The probability **decreases** with $n$, exactly as the formula $(1/4)^n$ says |
| [01_02](chapters/01_classical_computing/README.en.md) | Says applying the reversible **OR** circuit twice "gives the correct result in this case" | True for only half of the inputs. The circuit is X, X on $a, b$ and then CCX into $c = 1$ (with no final X), so applying it twice turns $(a, b, 1)$ into $(a, b, a \oplus b)$: $c$ returns to $1$ only when $a \neq b$. For example $(0,0,1) \to (1,1,0) \to (0,0,0)$. The order of the gates has to be reversed to undo it, exactly as the next cell does |
| [01_03](chapters/01_classical_computing/README.en.md) | Multiplying CX by $\vert 00\rangle$ is said to give "a column vector equal to the first **row** of CX" | It is the first **column** $(c_{00}, c_{10}, c_{20}, c_{30})$. The numerical result is still correct because the CX matrix is symmetric |
| [01_04](chapters/01_classical_computing/README.en.md) | Defines a "stochastic matrix" as a matrix on several p-bits that **cannot** be written as a Kronecker product; and says that stochastic matrices in general are not invertible | A stochastic matrix is a matrix with non-negative entries whose columns each sum to 1; the matrices $P$, $R$, $X$ and $R \otimes X$ in the lesson are all stochastic. The key point is that the **inverse** of a noise matrix is in general no longer a stochastic matrix (it has negative entries or entries greater than 1), so it cannot describe a physical operation |
| [02_02](chapters/02_quantum_computing/README.en.md) | Chooses $\frac{1}{\sqrt2}\vert 01\rangle + \frac{1}{\sqrt2}\vert 10\rangle$ as the state of the two particles produced from a spin-0 particle ("a reasonable choice") | It only matches measurements along $z$. Conservation of spin 0 gives the **singlet** state $\frac{1}{\sqrt2}(\vert 01\rangle - \vert 10\rangle)$, which is opposite along **every** axis; with the $+$ sign, measuring along $x$ or $y$ gives the same result on both sides |
| [02_04](chapters/02_quantum_computing/README.en.md) | Calls SWAP "another important entangling gate" | SWAP only exchanges the two qubits ($\text{SWAP}\vert a\rangle\vert b\rangle = \vert b\rangle\vert a\rangle$) and turns a product state into a product state, so it **does not create entanglement** |
| [02_04](chapters/02_quantum_computing/README.en.md) | Says the Solovay–Kitaev theorem is the reason for adding the $T$ gate for full computational power | Solovay–Kitaev only says that a gate set that is already dense can approximate every gate **efficiently**. That Clifford+T is a universal (dense) gate set is a separate fact |
| [02_05](chapters/02_quantum_computing/README.en.md), [04_03](chapters/04_quantum_algorithms/README.en.md) | Calls the speedup of Shor "proven" | Grover is proven optimal (in the oracle model). Shor is only faster than the **best known** classical algorithm; there is no proof that no fast classical algorithm exists |
| [04_03](chapters/04_quantum_algorithms/README.en.md) | "After only $r = 6$ tries, the success probability already exceeds 50%" (for $n = 5$) | Computed exactly (sampling without replacement): $r = 6$ gives $43.4\%$ and $r = 7$ gives $56.5\%$; the plot in the book shows the same. The same calculation gives $r = 14$ for $n = 7$ (the first number of tries above 50%), as the book states right afterwards |

## Possibly outdated

Places that were correct when the book was written but may no longer be correct for today's software or services.

| Lesson | In the book | Now |
|---|---|---|
| [00_02](chapters/00_getting_started/README.en.md) | Create an account at `quantum.ibm.com`, run `QiskitRuntimeService.save_account('your-token-here')` | The current `qiskit-ibm-runtime` describes `token` as an IBM Cloud API key and the channel as `ibm_cloud` or `ibm_quantum_platform`, with an `instance` parameter; the platform has moved to `quantum.cloud.ibm.com`. Follow the current documentation |

## Typos

| Lesson | Error | What it should be |
|---|---|---|
| [00_01](chapters/00_getting_started/README.en.md) | Creates `qc_t = transpile(...)` but runs `simulator.run(qc, ...)` | Run `qc_t`; with AerSimulator it does not matter, but on real hardware the transpiled circuit is needed |
| [01_01](chapters/01_classical_computing/README.en.md) | A note says Python's `and`, `or` are not equivalent to `&` and `^` | The table right above it lists AND as `&`, OR as `\|`, XOR as `^`; it should be `&` and `\|` |
| [01_02](chapters/01_classical_computing/README.en.md) | "use two CCX to flip the inputs" | The code and the figure use two **X** gates |
| [01_02](chapters/01_classical_computing/README.en.md) | A comment in the full adder code calls `ccx(a,b,0)` AND1 and `ccx(b2,c,0)` AND2 | Figure 01_02_09 names them the other way round: the first gate (controls $a, b$) is AND2 and the later gate (controls $a \oplus b$ and $c_{in}$) is AND1 |
| [01_03](chapters/01_classical_computing/README.en.md) | The dimension of $\vec x \otimes \vec y$ is the "sum" of the dimensions | It is the **product** ($2 \times 2 = 4$; $n$ bits give $2^n$ dimensions) |
| [01_04](chapters/01_classical_computing/README.en.md) | A comment says "100 times" | `n_samps = 200` |
| [02_03](chapters/02_quantum_computing/README.en.md) | The example of changing to the sign basis writes both coefficients as $\frac{2\sqrt3 - \sqrt6}{6}$ | The coefficient of $\vert -\rangle$ is $\frac{2\sqrt3 + \sqrt6}{6} \approx 0.986$; the numerical value in the notebook is correct |
| [02_05](chapters/02_quantum_computing/README.en.md) | Section 4.3 says $x = 010$ in one place and $\vert 10\rangle$ in another | The code and the output mark $x = 011$ |
| [02_05](chapters/02_quantum_computing/README.en.md) | A comment (and the text) says the controlled S gate with `ctrl_state='01'` is "activated by $\vert 01\rangle$" | `SGate().control(2, ctrl_state='01')` attached to `[2,1,0]` is activated when $q_2 = 1$ and $q_1 = 0$, that is, when the two control qubits are in $\vert q_2 q_1\rangle = \vert 10\rangle$ (the `ctrl_state` string is read from right to left: the last character corresponds to the first control qubit); a real run gives phase $i$ at $\vert 101\rangle$. The output in the book is correct |
| [03_01](chapters/03_quantum_protocols/README.en.md) | "we only consider qubits in the $xy$-plane" | The $xz$-plane |
| [03_02](chapters/03_quantum_protocols/README.en.md) | The comments "two entangled Bell states" and "Alice prepares state $\vert w\rangle = \frac12\vert 01\rangle - \frac{\sqrt3}{2}\vert 10\rangle$" | The circuit creates 3 Bell pairs and prepares $\frac{1}{\sqrt3}(\vert 001\rangle - \vert 010\rangle + \vert 100\rangle)$, exactly as the output shows |
| [03_02](chapters/03_quantum_protocols/README.en.md) | The 1-qubit example prints `(j,i) = ({alices_bits[1]},{alices_bits[0]})` | The labels are swapped: `alices_bits[1]` is `cra[0]`, that is, bit $i$ (checked by running Qiskit with only `cra[0] = 1`); Bob's final state is not affected |
| [03_02](chapters/03_quantum_protocols/README.en.md) | For $(\theta, \varphi) = (\pi/2, \pi/4)$, writes the pair of FP16 strings as $(0011101001001000, 0011111001001000)$ | The two strings are swapped: `float16` gives $\pi/4 = 0011101001001000$ and $\pi/2 = 0011111001001000$ |
| [03_03](chapters/03_quantum_protocols/README.en.md) | The results table after step 3 labels the state $\vert \psi\rangle_2$ | $\vert \psi\rangle_3$ |
| [04_04](chapters/04_quantum_algorithms/README.en.md) | Section 2.2 writes $\vert m^\perp\rangle$ as $\sum_{x \neq 0}$ | $\sum_{x \neq m}$, and it needs to be normalized |
| [04_04](chapters/04_quantum_algorithms/README.en.md) | Section 2.2 writes "apply $(U_f V)^2$" right after the sentence about $(V U_f)$ | $(V U_f)^2$, exactly as in the figure and the formula $(V U_f)^\kappa$ right below |

## Reporting a new error

If you find another error, open an issue with the **Báo lỗi trong sách** template of this repo ("Errors in the book"), and ideally also report it to the
author in the [original repo's Issues](https://github.com/learn-quantum/lqc-textbook/issues) so that the original gets fixed.
