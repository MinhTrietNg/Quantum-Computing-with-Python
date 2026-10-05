# 04 · Foundational quantum algorithms

[Tiếng Việt](README.md) · **English** · [简体中文](README.zh-CN.md)

Four classic algorithms show how, in the black-box model, a quantum computer needs fewer calls than a classical one:
**Deutsch–Jozsa**, **Bernstein–Vazirani**, **Simon** and **Grover**. All four share one template: bring the input into
superposition with Hadamard gates, call the **oracle** $U_f$ (the black box that holds the problem), then use
**interference** so that the answer stands out when you measure. The yardstick for comparison is the
**number of oracle queries**, that is, the query complexity. These are problems built specifically as illustrations:
fewer oracle calls does not mean that a quantum computer solves real-world problems faster.

> Source: [04_01](https://learnquantum.io/chapters/04_quantum_algorithms/04_01_deutsch-jozsa.html) ·
> [04_02](https://learnquantum.io/chapters/04_quantum_algorithms/04_02_bernstein-vazirani.html) ·
> [04_03](https://learnquantum.io/chapters/04_quantum_algorithms/04_03_simons.html) ·
> [04_04](https://learnquantum.io/chapters/04_quantum_algorithms/04_04_grover.html)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

**Prerequisites** (lesson [02_05](../02_quantum_computing/README.en.md#02_05--quantum-building-blocks)):
the oracle $U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$, phase kickback
$|x\rangle|-\rangle \to (-1)^{f(x)}|x\rangle|-\rangle$, and the Hadamard transform
$H^{\otimes n}|x\rangle = \frac{1}{\sqrt N}\sum_z (-1)^{x\cdot z}|z\rangle$.

## Contents

| Lesson | Notebook | Web | Problem | Oracle calls (classical → quantum) |
|---|---|---|---|---|
| 04_01 · Deutsch–Jozsa | [04_01_deutsch-jozsa.ipynb](04_01_deutsch-jozsa.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_01_deutsch-jozsa.html) | Is $f$ constant or balanced? | $2^{n-1} + 1$ (with certainty) → **1** |
| 04_02 · Bernstein–Vazirani | [04_02_bernstein-vazirani.ipynb](04_02_bernstein-vazirani.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_02_bernstein-vazirani.html) | Find $s$ with $f(x) = s\cdot x$ | $n$ → **1** |
| 04_03 · Simon | [04_03_simons.ipynb](04_03_simons.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_03_simons.html) | Find $s$ with $f(x) = f(x \oplus s)$ | $\sim 2^{n/2}$ → $\sim n$ (**exponential** speedup) |
| 04_04 · Grover | [04_04_grover.ipynb](04_04_grover.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_04_grover.html) | Find $x$ with $f(x) = 1$ (unstructured search) | $\sim N$ → $\sim\sqrt N$ (**quadratic** speedup) |

> The code snippets in this README are **excerpts** from the notebooks (the original English comments are kept) and use variables defined in earlier cells. To run them, run the whole notebook from top to bottom.

---

## 04_01 · Deutsch–Jozsa algorithm

**Problem.** Given the oracle $U_f$ of a function $f:\{0,1\}^n \to \{0,1\}$ and the **promise** that $f$ is either
**constant** (always 0 or always 1) or **balanced** (half of the inputs give 0, the other half give 1). Decide which kind
$f$ is.

### Key concepts

**The case $n = 1$ (Deutsch's algorithm).** There are 4 functions: $f = 0$, $f = 1$ (constant), $f = x$, $f = \bar x$ (balanced).

<p align="center"><img src="images/04_01_02_oracles.png" width="750" alt="Four two-wire circuits on x and y: two plain wires; an X gate on y; a CX controlled by x onto y; a CX that fires when x is 0"></p>

*Figure: the four circuits that can be inside the black box; circuits 1 and 2 are constant functions ($f = 0$, $f = 1$), circuits 3 and 4 are balanced functions ($f = x$, $f = \bar x$).*

Classically, a single query only guesses right 50% of the time, because for any one input the output always agrees with
one constant function and one balanced function; you need 2 queries to be certain. Quantum: wrap the black box in H gates.
For a constant function, the two layers of H cancel each other; for a CX, H–CX–H **reverses** the direction of the control
(phase kickback), so the top qubit gets flipped.

<p align="center"><img src="images/04_01_05_cir1_equiv.png" width="630" alt="Circuit 1 (an empty box) sandwiched between two layers of H is equivalent to two plain wires"></p>

*Figure: circuit 1 (an empty box) sandwiched between two layers of H is still just two plain wires, because $HH = I$.*

<p align="center"><img src="images/04_01_06_cir3_equiv.png" width="630" alt="Circuit 3 (a CX from x down to y) sandwiched between two layers of H is equivalent to a reversed CX, with y as the control and x as the target"></p>

*Figure: circuit 3 (a CX from $x$ down to $y$) sandwiched between two layers of H is equivalent to a reversed CX: $y$ is the control and $x$ is the target.*

<p align="center"><img src="images/04_01_07_deutsch.png" width="500" alt="Deutsch circuit: X on the bottom qubit, H on both qubits, the black box, H on both qubits, measure the top qubit; stages psi 0 to psi 4"></p>

*Figure: the Deutsch circuit with the stages $|\psi\rangle_0$ to $|\psi\rangle_4$; only the top qubit is measured.*

The steps ($q_1$ is $x$, $q_0$ is $y$):

$$|0\rangle|0\rangle \xrightarrow{X \text{ on } y} |0\rangle|1\rangle \xrightarrow{H\otimes H} |+\rangle|-\rangle
\xrightarrow{U_f} \tfrac{(-1)^{f(0)}}{\sqrt2}\big(|0\rangle + (-1)^{f(0)\oplus f(1)}|1\rangle\big)|-\rangle
\xrightarrow{H\otimes H} \pm|f(0)\oplus f(1)\rangle|1\rangle$$

If measuring the top qubit gives 0, then $f$ is constant; if it gives 1, then $f$ is balanced. Only **1 call** is needed,
and the result is deterministic.

**The general case of $n$ bits.**
- **Classical:** to be certain, in the worst case you must try $2^n/2 + 1 = 2^{n-1} + 1$ inputs, because $2^{n-1}$ identical
  outputs still do not rule out a balanced function. If you accept probabilistic guessing (try $r$ random inputs; if all the
  outputs are the same, guess constant), the notebook gives $\mathbb{P}_\text{success} = 1 - 1/2^r$, but it is still only a guess.

<p align="center"><img src="images/04_01_11_classical_probs.png" width="520" alt="Bar chart: probability of guessing the function type correctly versus the number of inputs tried r, with N = 32; about 51% at r = 1, about 99% at r = 6, nearly 100% from r = 7"></p>

*Figure: probabilistic guessing with $N = 32$ (simulation): about 99% at $r = 6$, without needing the 17 tries that certainty requires.*

> Note: the formula $1 - 1/2^r$ implicitly assumes that the black box is constant or balanced with 50/50 probability and
> that the tries are chosen independently (they may coincide). If you choose $r$ **different** inputs, as in the simulation,
> the probability is slightly higher (99.1% instead of 98.4% at $N = 32$, $r = 6$). If the black box is a balanced function,
> the probability of guessing wrong is $1/2^{r-1}$ (independent tries). Either way, the error shrinks exponentially in $r$ and
> does not depend on $n$: with 11 tries the error is below 0.1%. So DJ's advantage of "1 call versus $2^{n-1} + 1$ calls"
> holds only against a **deterministic** classical algorithm (one that is not allowed to be wrong).

- **Quantum:** the same circuit, with H replaced by $H^{\otimes n}$:

<p align="center"><img src="images/04_01_10_deutsch-jozsa.png" width="520" alt="Deutsch–Jozsa circuit: the n qubits x go through QHT, the qubit y goes through X then H, then the oracle U_f, then QHT on x, H on y, and measure the n qubits x; stages psi 0 to psi 4"></p>

*Figure: the Deutsch–Jozsa circuit; QHT is $H^{\otimes n}$ on the register $x$, and only the register $x$ is measured.*

$$|\psi\rangle_3 = \Big(\frac{1}{\sqrt N}\sum_x (-1)^{f(x)}|x\rangle\Big)|-\rangle$$

  - $f$ **constant:** $(-1)^{f(x)}$ is a global phase; a second $H^{\otimes n}$ takes the state back to $|0\rangle^{\otimes n}$.
  - $f$ **balanced:** the amplitude of $|0\rangle^{\otimes n}$ is $\frac1N\sum_x(-1)^{f(x)} = 0$ because the positive and negative terms cancel,
    so you **never** measure all zeros.

**Rule for reading the result:** if you measure all zeros, $f$ is constant; any other result means $f$ is balanced.

**Building the oracle:**

| Type of function | Circuit |
|---|---|
| Constant $f = 1$ | A single X gate on qubit $y$ (constant $f = 0$: do nothing) |
| Balanced, parity | A CX from every qubit $x_i$ to $y$; DJ always gives the result $11\dots1$ |
| Balanced, split in half | An MCX for the first half (or the second half) of the values of $x$ |
| Balanced, random | An MCX with `ctrl_state` set to $N/2$ randomly chosen values of $x$ |

### Key code

```python
def deutsch_quantum():
    bb, bb_num = black_box()  # generate random black-box
    
    qc_dq = QuantumCircuit(2,1)
    qc_dq.x(0)                   # Initialize bottom qubit to |1〉
    qc_dq.barrier()
    qc_dq.h([1,0])               # Hadamard before black box
    qc_dq.append(bb,[0,1])       # append black box to circuit
    qc_dq.h([1,0])               # Hadamard after black box
    qc_dq.measure(1,0)           # measure top qubit
    
    return qc_dq, bb_num
```
Deutsch's algorithm. `qc.append(sub_circuit, qubits)` attaches the black box to the circuit.

> Note: the function `black_box()` uses `np.random.randint(1,3)`, but `randint` excludes the upper bound, so it only
> generates circuit 1 or 2 (**constant functions only**). To get all 4 circuits, as the comment says, it would have to be
> `np.random.randint(1,5)`. Because of this, the two right/wrong bar charts of section 1.1 in the output do not reflect the
> full problem correctly.

```python
def black_box_n(n):
    bb_type = np.random.randint(2) # bb_type = 0 for constant, bb_type = 1 for balanced
    
    qc_bb = QuantumCircuit(n+1, name='Black Box')
    
    if bb_type:
        # Generate random list of x values that evaluate to f(x) = 1
        x_list = np.random.choice(2**n, size=2**n//2, replace=False)
        
        for x in x_list:
            qc_bb.mcx(list(range(1,n+1)),0, ctrl_state=np.binary_repr(x,n))
            
    return qc_bb, bb_type
```
The $n$-bit oracle: a constant function is an empty circuit ($f = 0$); a balanced function is $N/2$ MCX gates, each of which flips $y$ at one value of $x$.
`qubit 0` is $y$, and qubits $1..n$ are $x$.

```python
def deutsch_josza(n):
    bb, bb_type = black_box_n(n)              # generate random black-box of n input qubits
    
    qc_dj = QuantumCircuit(n+1,n)
    qc_dj.x(0)                                # Initialize bottom qubit to |1〉
    qc_dj.barrier()
    qc_dj.h(range(n+1))                       # Hadamard gates on all qubits
    qc_dj.append(bb,range(n+1))               # append black box to circuit
    qc_dj.h(range(n+1))                       # Hadamard gates on all qubits
    qc_dj.measure(range(1,n+1),range(n))      # measure top n qubits
    
    return qc_dj, bb_type
```
The complete Deutsch–Jozsa circuit. The simulation of the classical method uses `qc.prepare_state(k, qubits)` to load the input $|k\rangle$.

### Results

| Check | Output |
|---|---|
| Final statevector for $f = 0,\ 1,\ x,\ \bar x$ | $\vert 01\rangle,\ -\vert 01\rangle,\ \vert 11\rangle,\ -\vert 11\rangle$: the top qubit is 0 for a constant function and 1 for a balanced function |
| Constant oracle $f = 1$ (X on $y$) | every $\vert x\rangle\vert 0\rangle \to \vert x\rangle\vert 1\rangle$ |
| Parity oracle, 3 bits | $f(x)$ = the parity of $x$ (for example $011 \to 0$, $111 \to 1$) |
| DJ with parity | always gives $111$ |
| DJ with the other balanced functions | never gives $000$ |
| Simulation with $n = 4$, 100 runs | classically, about 50% of the runs need $2^n/2 + 1 = 9$ tries; DJ always needs 1 call (chart) |

### Quick recap

- Circuit: X on $y$ → H on every qubit → $U_f$ → H on every qubit → measure $x$.
- All zeros means constant, anything else means balanced; 1 call, deterministic.
- Mechanism: kickback puts $(-1)^{f(x)}$ into the amplitudes; $H^{\otimes n}$ adds the signs together, so the amplitude of $|0\dots0\rangle$ is 0 when the function is balanced.
- Classically, certainty needs $2^{n-1} + 1$ calls (worst case). If you accept a very small error, a few random calls are
  enough, so DJ's advantage is only against deterministic classical algorithms.

---

## 04_02 · Bernstein–Vazirani algorithm

**Problem.** Given the oracle of $f(x) = s \cdot x = s_0x_0 \oplus s_1x_1 \oplus \dots \oplus s_{n-1}x_{n-1}$ (the binary
dot product). Find the secret string $s$ of $n$ bits.

### Key concepts

**Classical: exactly $n$ calls are needed.** Use the inputs that have a single bit 1, $x = 0\dots01,\ 0\dots10,\ \dots$. Each
such call gives $f(x) = s_i$, that is, a "mask" that picks out one bit of $s$ at a time. A deterministic classical algorithm
cannot do with fewer calls: each call returns only 1 bit, while $s$ has $n$ bits.

**Quantum: 1 call**, with a circuit **identical to Deutsch–Jozsa**; only the oracle differs:

<p align="center"><img src="images/04_01_10_deutsch-jozsa.png" width="520" alt="The Deutsch–Jozsa circuit reused for Bernstein–Vazirani: the n qubits x go through QHT, the qubit y goes through X then H, then the oracle U_f, then QHT on x, H on y, and measure the n qubits x"></p>

*Figure: Bernstein–Vazirani uses exactly the Deutsch–Jozsa circuit; the only difference is that $U_f$ computes $f(x) = s\cdot x$, so the measurement gives $s$ directly.*

$$|\psi\rangle_3 = \Big(\frac{1}{\sqrt N}\sum_x (-1)^{s\cdot x}|x\rangle\Big)|-\rangle = \big(H^{\otimes n}|s\rangle\big)|-\rangle$$

The expression in parentheses is exactly $H^{\otimes n}|s\rangle$. Applying $H^{\otimes n}$ once more (H is its own inverse)
gives exactly $|s\rangle$, and $s$ is measured with probability 100%.

**Building the oracle:** put one CX from each qubit $x_i$ with $s_i = 1$ to the qubit $y$. This gives $y \oplus \bigoplus_{i: s_i=1} x_i = y \oplus s\cdot x$.

### Key code

```python
def black_box(n):
    s_int = np.random.randint(2**n)
    s = np.binary_repr(s_int, n)
    controls = [i+1 for i, v in enumerate(reversed(s)) if v == '1']
    
    qc_bb = QuantumCircuit(n+1, name='Black Box')
    if controls:
        qc_bb.cx(controls,[0]*len(controls))
        
    return qc_bb, s
```
An oracle for a random $s$. `reversed(s)` is used because the rightmost bit of the string is $s_0$ (which corresponds to qubit 1);
`qc.cx(list_c, list_t)` places several CX gates at once.

```python
for i in range(n):
    
    x_int = 2**i
    x = np.binary_repr(x_int, n)
    input_ones = [i+1 for i, v in enumerate(reversed(x)) if v == '1']
    
    qc = QuantumCircuit(n+1,1)
    qc.x(input_ones)
    qc.append(bb,range(n+1))
    qc.measure(0,0)
```
The classical method: $n$ runs with $x = 2^i$, each run extracting one bit of $s$.

```python
qc, s = bernstein_vazirani(n)
qc_t = transpile(qc, simulator)
job = simulator.run(qc_t, shots=1, memory=True)  # Run simulation once
s_out = job.result().get_memory()[0]
```
The quantum method: **1 shot** is enough to read $s$. `bernstein_vazirani(n)` has the same structure as `deutsch_josza(n)`.

### Results

| Check | Output |
|---|---|
| Table of $f(x)$ with $s = 1101$ | the rows $x$ with a single bit 1 (marked ←) give exactly $s_i$ |
| Classical, $n = 3$ | `secret string: 011`, `extracted string: 011` (3 calls) |
| Quantum, $n = 4$ | `secret string: 1000`, `extracted string: 1000` (1 call) |
| Oracle for $s = 1011$ | $f(x) = s\cdot x$ holds for all 16 values of $x$ |

### Quick recap

- The circuit is identical to DJ; the oracle is the CX gates from those $x_i$ with $s_i = 1$.
- $\sum_x (-1)^{s\cdot x}|x\rangle = H^{\otimes n}|s\rangle$, so one more $H^{\otimes n}$ gives $|s\rangle$.
- $n$ classical calls → 1 quantum call: only a linear speedup, not an exponential one.

---

## 04_03 · Simon's algorithm

**Problem.** Given the oracle of $f:\{0,1\}^n \to \{0,1\}^n$, with the promise that $f(x) = f(x \oplus s)$ for some string $s \neq 0$
(that is, $f$ is a **two-to-one** function: each output value comes from exactly one pair $\{x, x\oplus s\}$). Find $s$.

<p align="center"><img src="images/04_03_01_simons_bb.png" width="650" alt="Simon's oracle U_f: the n wires x pass through unchanged, the n wires y come out as y_i XOR f(x)_i; when y is 0 the bottom register outputs f(x)"></p>

*Figure: Simon's oracle has $2n$ qubits; with $y = 0\dots0$, the bottom register outputs exactly $|f(x)\rangle$.*

This is the first algorithm with an **exponential** speedup over every classical algorithm, including randomized ones, but
only in the oracle model (counting the number of calls to $U_f$). The problem has no direct application; its idea is the
forerunner of Shor's algorithm.

> Note: the introduction of the notebook calls Shor's algorithm an algorithm with a **proven** advantage for a practical
> application. In fact, nobody has proven that factoring is hard for classical computers: Shor's algorithm is much faster than the
> **best known** classical algorithm, but its advantage over every classical algorithm has not been proven.

### Key concepts

**Classical.** Try values of $x$ until you find two inputs $a, b$ with $f(a) = f(b)$; then $s = a \oplus b$. This is like the
birthday problem (birthday paradox). With $r$ different inputs chosen at random:

$$\mathbb{P}_\text{success} = 1 - \prod_{k=0}^{r-1}\frac{2^n - 2k}{2^n - k}$$

About $2^{n/2}$ tries are needed (more precisely, about $1.18 \cdot 2^{n/2}$) to succeed with probability above 50%, which grows
**exponentially** in $n$. In the worst case, this approach needs $2^{n-1} + 1$ tries. Simon also proved that every classical
algorithm, including randomized ones, needs on the order of $2^{n/2}$ calls.

<p align="center"><img src="images/04_03_02_classical_probs.png" width="520" alt="Bar chart: the classical probability of finding s versus the number of tries r, with n = 5; about 44% at r = 6, about 58% at r = 7, nearly 100% from r = 14"></p>

*Figure: the classical method with $n = 5$ (simulation): the probability of finding $s$ exceeds 50% only from $r = 7$.*

> Note: the notebook says that for $n = 5$ the probability exceeds 50% "after $r = 6$ tries". Both the formula above (43.4%
> at $r = 6$, 56.5% at $r = 7$) and the chart itself show that you need to reach $r = 7$.

**Quantum circuit** (unlike DJ/BV: the bottom register has $n$ qubits, initialized to $|0\rangle^{\otimes n}$, and it does **not** use kickback):

<p align="center"><img src="images/04_03_03_simon.png" width="520" alt="Simon circuit: QHT on the n qubits x, U_f on all 2n qubits, measure the n qubits y right after U_f, then QHT on x and measure x; stages psi 0 to psi 4"></p>

*Figure: Simon's circuit; the bottom register starts at $|0\rangle^{\otimes n}$ and is measured right after $U_f$.*

1. $H^{\otimes n}$ on the register $x$: $\frac{1}{\sqrt N}\sum_x |x\rangle|0\rangle$.
2. $U_f$: $\frac{1}{\sqrt N}\sum_x |x\rangle|f(x)\rangle = \frac{1}{\sqrt N}\sum_{x\in S}\big(|x\rangle + |x\oplus s\rangle\big)|f(x)\rangle$.
3. **Measure the bottom register**, which gives a value $f(a)$. The top register is then left in just $\frac{1}{\sqrt2}\big(|a\rangle + |a\oplus s\rangle\big)$.
4. $H^{\otimes n}$ on the top register:

$$\frac{1}{\sqrt{2N}}\sum_z (-1)^{a\cdot z}\big[1 + (-1)^{s\cdot z}\big]|z\rangle$$

   The $z$ with $s\cdot z = 1$ cancel out; only the $z$ that satisfy **$s \cdot z = 0$** remain, whatever $a$ is.
5. Measure the top register to get a $z$ with $s\cdot z = 0$. If it gives $z = 0$ (probability $2/N$), it is useless and you must run again.

**Classical post-processing.** Each $z$ gives one linear equation modulo 2. You need $n-1$ **linearly independent** equations:

$$Z\vec s = \vec 0 \pmod 2 \quad\Rightarrow\quad \vec s = \text{kernel}(Z)$$

The hybrid quantum–classical procedure:

<p align="center"><img src="images/04_03_04_full_simon.png" width="760" alt="Simon flowchart: if k is not yet n−1, run the circuit to get z; keep z if it is nonzero, not yet in the list and linearly independent, then increase k; when there are enough, solve the system s·z = 0 for s"></p>

*Figure: Simon's flowchart: run the circuit, filter $z$, store the values until there are $n-1$ linearly independent ones, then solve the system $s\cdot z = 0$.*

1. Run the circuit to get $z$.
2. Discard it if $z = 0$ or if $z$ is linearly dependent on the $z$ values already collected (Gaussian elimination modulo 2).
3. Repeat until you have $n-1$ basis vectors.
4. Solve for the kernel (reduced row echelon form, RREF, then back-substitution) to get $s$.

The average number of runs grows only **linearly** in $n$: each run gives a random $z$, uniformly distributed over the $2^{n-1}$
solutions of $s\cdot z = 0$, so on average fewer than $n + 1$ runs are enough to get $n-1$ independent vectors. The Gaussian elimination
takes only polynomial time in $n$. That is, the quantum side needs $O(n)$ oracle calls **plus** classical post-processing,
compared with about $2^{n/2}$ calls classically.

<p align="center"><img src="images/04_03_06_compare_probs.png" width="750" alt="Bar chart comparing the probability of finding s versus the number of calls r, with n = 7: quantum is 0 for r below 6 and exceeds 50% at r = 7; classical exceeds 50% only at r = 14"></p>

*Figure: $n = 7$, classical (pink) and quantum (purple): quantum exceeds 50% at $r = 7$, classical needs $r = 14$.*

**Example in the notebook ($s = 1010$).** The possible values of $z$ are $\{0000, 0001, 0100, 0101, 1010, 1011, 1110, 1111\}$.
- $z = 0001$ gives $s_0 = 0$.
- $z = 1010$ gives $s_3 \oplus s_1 = 0$.
- $z = 1011$ is linearly dependent on the previous two $z$, so it is discarded.
- $z = 1110$ gives $s_3 \oplus s_2 \oplus s_1 = 0$; combined with $s_3 \oplus s_1 = 0$ this gives $s_2 = 0$.

Since $s \neq 0$, we get $s = 1010$.

**Building the oracle from a truth table.**
- The naive way: write each bit $f(x)_i$ as a sum of products (DNF), where each product is one MCX. The circuit is very long.
- The compact way: simplify the expression with `sympy.logic.boolalg.SOPform`, for example $(\bar x_2 x_1 x_0) \lor (x_2 x_1 x_0) = x_1 \land x_0$,
  then build the circuit with `BitFlipOracleGate`. According to the book, Qiskit's transpiler cannot do this simplification on its own.

### Key code

```python
def fx_simon(s_int, n):
    fx_lst = [0]*2**n
    x_used = []
    fx_avail = list(range(2**n))
    
    for x_int in range(2**n):
        if x_int in x_used: continue

        x_pair = s_int ^ x_int
        x_used.extend((x_int, x_pair))
        
        # pick random f(x) value and remove from available list
        fx_int = np.random.choice(fx_avail)
        fx_avail.remove(fx_int)
        
        # assign f(x) value to x and s⊕x
        fx_lst[x_int] = fx_int
        fx_lst[x_pair] = fx_int
        
    return fx_lst
```
Randomly generates a valid Simon function: each pair $\{x, x\oplus s\}$ receives a common output value.

```python
def simons_cir(n):
    bb, s = black_box(n)                     # generate random black-box of n input qubits
    
    qc_s = QuantumCircuit(2*n,2*n)
    qc_s.h(range(n,2*n))                     # Hadamard gates top n qubits
    qc_s.append(bb,range(2*n))               # append black box to circuit
    qc_s.measure(range(n),range(n))          # measure bottom n qubits
    qc_s.barrier()
    qc_s.h(range(n,2*n))                     # Hadamard gates on top n qubits
    qc_s.measure(range(n,2*n),range(n,2*n))  # measure top n qubits
    
    return qc_s, s
```
The register $x$ is the qubits $n..2n-1$, and the register $f(x)$ is the qubits $0..n-1$. The `memory` string prints the high bit first, so
`z_and_fx[0:n]` is $z$.

```python
def generate_basis(basis: list[int], z: int):
    # Returns updated list of binary basis vectors by reducing a new entry `z` through
    # Gaussian elimination (mod 2). For convenience, we treat each "vector" as an integer,
    # where the bits of its binary representation correspond to the elements of the vector.
    
    basis = basis.copy()
    
    # Reduce z using existing pivots
    for b in basis:
        p = (b & -b).bit_length() - 1   # finds index of the lsb that's equal to 1 (pivot)
        if (z >> p) & 1:                # checks if the p^th bit of z is 1
            z ^= b                      # reduce z by XOR with basis vector b
            
    if z == 0: return basis             # If reduced z is zero, it was dependent
    p = (z & -z).bit_length() - 1       # finds index of the lsb that's equal to 1 (pivot)
    
    
    # Eliminate pivot from existing basis vectors (now z contains it)
    for i, b in enumerate(basis):
        if (b >> p) & 1:
            basis[i] ^= z
    
    basis.append(z)
    return basis
```
Gaussian elimination modulo 2 on integers: each vector is an `int`, addition is `^` (XOR), and `b & -b` isolates the lowest bit 1
(the pivot). The function `kernel_from_basis(basis, n)` sets the free variables to 1 and solves for the pivot variables to get $s$.

```python
while k < n - 1:
    
    # transpile and run quantum circuit
    qc_t = transpile(qc_s_cir, simulator)
    job = simulator.run(qc_t, shots=1, memory=True)
    z_and_fx = job.result().get_memory()[0]   # returns results for both top and bottom registers
    z = int(z_and_fx[0:n], 2)                 # extract z only (as integer)
    
    if z != 0:
        basis_vects = generate_basis(basis_vects, z)
        k = len(basis_vects)
        
    tries += 1

s_out = np.binary_repr(kernel_from_basis(basis_vects, n)[0],n)
```
The hybrid loop: run the circuit, filter $z$, and update the basis until there are $n-1$ vectors, then solve for the kernel.

```python
expr = SOPform(x_symbs, fx_0)
...
qc_bool.append(BitFlipOracleGate(fx_expr, x_vars), x_qubits)
```
Simplify the Boolean expression with SymPy, then `BitFlipOracleGate` (in `qiskit.circuit.library`) builds the oracle from the string of
the expression. Use `qc.decompose()` to see the circuit inside.

> Minor note: the closing remark of the notebook writes the general function as $f:\{0,1\}^n \to \{0,1\}^n$ with $m \ge n$; it should be
> $\{0,1\}^n \to \{0,1\}^m$. Section 2.1 promises an "example using 3 qubits" in section 2.3, but that example is $s = 1010$ (4 bits, 8 qubits).
> A few places that refer to "section 1.2.1", "1.2.2", "1.1" actually mean sections 2.1, 2.2 and 1.

### Results

| Check | Output |
|---|---|
| `fx_simon` with $s = 1101$ | for example $f(0000) = f(1101) = 1011$ |
| Oracle, $n = 3$, $s = 100$ | $f(x) = f(x \oplus 100)$ for every $x$ |
| Classical, $n = 7$ | `secret 1101000`, found after `22` tries |
| Quantum, $n = 7$ | `secret 0111110`, found after `6` runs of the circuit |
| Chart in the notebook, $n = 7$ | quantum exceeds 50% at $r = 7$; classical needs $r = 14$ |
| `SOPform` for $f(x)_0$ | $x_0 \land x_1$ |

### Quick recap

- Promise: $f(x) = f(x\oplus s)$, a two-to-one function; find $s$.
- Circuit: H on $x$ → $U_f$ → measure $f(x)$ → H on $x$ → measure $x$ to get a $z$ with $s\cdot z = 0$.
- You need $n-1$ linearly independent values of $z$, then solve for the kernel modulo 2 (Gaussian elimination with XOR).
- Classically $\sim 2^{n/2}$ calls (even for randomized algorithms), quantum $\sim n$ calls plus Gaussian elimination: an
  **exponential** speedup in the oracle model.
- It is a hybrid algorithm: the quantum part samples, the classical part solves the system of equations.

---

## 04_04 · Grover's algorithm

**Problem.** Unstructured search: given the oracle of $f:\{0,1\}^n \to \{0,1\}$, find the inputs $x$ with $f(x) = 1$
(the **marked elements**). $N = 2^n$.

> The example of "searching a phone book for a given phone number" is only an illustration. To build an oracle for the phone book you
> would first have to go through the whole phone book, so Grover is useful only when $f$ can be **built efficiently** as a
> circuit, for example the circuit satisfiability problem. Even then, the advantage is only quadratic over exhaustive search,
> not over every classical algorithm specialized for that problem.

### Key concepts

**Classical.** Try the elements one by one: $\mathbb{P}_\text{success} = r/2^n$, so you need $2^{n-1}$ tries to reach 50% and about $N$ tries
to be certain. That is, the cost grows linearly in $N$.

**The quantum idea: amplitude amplification.**

<p align="center"><img src="images/04_04_03_grover.png" width="450" alt="Grover circuit: QHT on the n input qubits, the ancilla qubit in the minus state, the pair U_f and V repeated kappa times, then measure; run once, the output is m with high probability"></p>

*Figure: the Grover circuit; the pair $U_f$ and $V$ (the diffuser) is repeated $\kappa$ times before measuring.*

Repeat the pair (oracle, diffuser) $\kappa$ times:
1. $H^{\otimes n}$: every amplitude equals $1/\sqrt N$ (the state $|s\rangle$).
2. **Oracle** $U_f$ with $y = |-\rangle$: **flips the sign** of the amplitude of the marked element.
3. **Diffuser** $V$: **reflects every amplitude about the mean** $\mu$: $\alpha_x \to 2\mu - \alpha_x$.
   The marked amplitude (now negative, far below $\mu$) is bounced up high; the other amplitudes decrease.

Example with $n = 3$, $m = 101$:

<p align="center"><img src="images/04_04_07_grover_step03.png" width="600" alt="Amplitude chart of the 8 states after the oracle: seven states at about 0.354, only 101 at about −0.354"></p>

*Figure: after the oracle, only the amplitude of $|101\rangle$ changes sign.*

<p align="center"><img src="images/04_04_09_grover_step04.png" width="600" alt="Amplitude chart after the diffuser, the dashed line is the mean at about 0.265: seven states are left at about 0.177, only 101 jumps up to about 0.884"></p>

*Figure: the diffuser reflects every amplitude about the mean (the dashed line): $|101\rangle$ jumps up to 0.884, the other states drop to 0.177.*

| Step | Amplitude of $m$ | Probability of measuring $m$ |
|---|---|---|
| After H | 0.354 | 12.5% |
| After 1 round (oracle + diffuser) | $\frac{1}{\sqrt8}\cdot\frac{3\cdot8-4}{8} \approx 0.884$ | ≈ 78% |
| After 2 rounds | $\approx 0.972$ | ≈ 94.5% |
| Adding a 3rd round | drops to $\approx 0.574$ | ≈ 33%, because the probability **oscillates periodically** and does not keep increasing |

<p align="center"><img src="images/04_04_12_grover_step06.png" width="600" alt="Amplitude chart after 2 rounds: 101 at about 0.972, the seven other states at about −0.088"></p>

*Figure: after 2 rounds, the amplitude of $|101\rangle$ is 0.972 (probability about 94.5%); the other states are left at $-0.088$.*

**The circuit of the diffuser.**

$$V = 2|s\rangle\langle s| - I = H^{\otimes n}\big(2|0\rangle\langle 0| - I\big)H^{\otimes n} = -\,H^{\otimes n}X^{\otimes n}\,\text{MCZ}\,X^{\otimes n}H^{\otimes n}$$

$2|0\rangle\langle0| - I$ equals $-1$ times a gate that flips the sign of **only** the state $|0\dots0\rangle$, that is, an MCZ sandwiched between two layers of X.
The $-1$ is a global phase and can be ignored: the circuit `diffuser(n)` actually builds $-V$, which gives the same measurement results.

**The geometric view → the number of iterations.** Split $|s\rangle = \cos\frac\theta2|m^\perp\rangle + \sin\frac\theta2|m\rangle$, with
$\sin\frac\theta2 = 1/\sqrt N$. The oracle is a reflection about $|m^\perp\rangle$; the diffuser is a reflection about $|s\rangle$.
The two reflections combined make a **rotation by an angle $\theta$** toward $|m\rangle$.

<p align="center"><img src="images/04_04_15_grover_rotation03.png" width="270" alt="Plane with the two perpendicular axes m-perp and m: s is tilted by the angle theta/2; the oracle reflects s into Z_f s at the negative angle theta/2; the diffuser reflects about s, giving V U_f s, at the angle theta from s"></p>

*Figure: one Grover round: the oracle ($Z_f$, the phase form of $U_f$) reflects $|s\rangle$ across the axis $|m^\perp\rangle$, and the diffuser reflects back across $|s\rangle$; the result is an extra rotation by the angle $\theta$.*

After $\kappa$ rounds, the state makes an angle $(2\kappa + 1)\frac\theta2$ with $|m^\perp\rangle$, so the probability of measuring $m$ is
$\sin^2\big((2\kappa + 1)\tfrac\theta2\big)$. To reach $\pi/2$ we need $\kappa\theta + \theta/2 = \pi/2$:

$$\kappa = \left\lfloor \frac{\pi}{4\arcsin(1/\sqrt N)} - \frac12 \right\rceil \;\approx\; \frac{\pi}{4}\sqrt N$$

If you repeat more rounds than this, the vector passes $|m\rangle$ (overshoot) and the probability falls, as in the 3rd round of the example above.

<p align="center"><img src="images/04_04_16_grover_rotation04.png" width="270" alt="After two rounds, the vector (V U_f)^2 s has rotated by 2 theta relative to s and has passed the m axis"></p>

*Figure: two rounds rotate $|s\rangle$ by a further $2\theta$; with a large $\theta$ as in the figure, the vector has already passed the $|m\rangle$ axis.*

With $M$ marked elements (you must know $M$ in advance), replace $1/\sqrt N$ by $\sqrt{M/N}$, so $\kappa \approx \frac\pi4\sqrt{N/M}$ when $M \ll N$.

No quantum algorithm does better: unstructured search needs at least on the order of $\sqrt N$ oracle calls (Bennett,
Bernstein, Brassard, Vazirani, 1997). So Grover's **quadratic** speedup is optimal, and it is not an exponential speedup.

**Checking the result.** Run Grover once to get $x_\text{out}$, then call $f(x_\text{out})$ to check it; if it is wrong, run it again.
In total, at least $\kappa + 1$ oracle calls. With $N = 32$: nearly 100% after $\kappa + 1 = 5$ calls, whereas the classical method
has to try almost all of the 32 elements to be certain.

<p align="center"><img src="images/04_04_18_compare_probs.png" width="750" alt="Bar chart comparing the probability of finding m versus the number of calls r with N = 32: Grover is 0 for r below 5 and nearly 100% from r = 5; classical grows almost linearly, reaching 100% at r = 31"></p>

*Figure: $N = 32$, classical (pink) and Grover with one check (purple): Grover is nearly 100% from $r = \kappa + 1 = 5$, while classical grows almost linearly.*

### Key code

```python
def Uf_one_marked(n):
    N = 2**n
    m_int = np.random.randint(N)
    m = np.binary_repr(m_int,n)
    
    qc_bb = QuantumCircuit(n+1, name=' $U_f$ (Oracle)')
    qc_bb.mcx(list(range(1,n+1)),0, ctrl_state=m)
    
    return qc_bb, m
```
An oracle that marks one element: a single MCX that fires only when $x = m$.

```python
def diffuser(n):
    
    mcz = ZGate().control(n-1)
    
    qc_v = QuantumCircuit(n, name=' $V$ (Diffuser)')
    qc_v.h(range(n))
    qc_v.x(range(n))
    qc_v.append(mcz,range(n))
    qc_v.x(range(n))
    qc_v.h(range(n))
    
    return qc_v
```
The diffuser $H\,X\,\text{MCZ}\,X\,H$, that is, $V$ up to a global phase of $-1$. `ZGate().control(n-1)` creates an MCZ on $n$ qubits.

```python
def grover_one_marked(n, κ):
    
    bb, m = Uf_one_marked(n)
    
    qc_g = QuantumCircuit(n+1,n)
    qc_g.x(0)
    qc_g.h(0)
    qc_g.barrier()
    qc_g.h(range(1,n+1))
    
    for _ in range(κ):
        qc_g.append(bb,range(n+1))
        qc_g.append(diffuser(n),range(1,n+1))

    qc_g.barrier()
    qc_g.measure(range(1,n+1),range(n))
    
    return qc_g, m
```
The complete Grover circuit: qubit 0 is in $|-\rangle$ for kickback, repeat $\kappa$ times (oracle, diffuser), then measure.

```python
κ = round(np.pi/(4*np.arcsin(1/np.sqrt(N)))-1/2)
```
The optimal number of iterations. The notebook also has `find_κ(N)`, which computes it iteratively with the formula $2\mu - \alpha$ and gets the same result.

> Note: `Uf_M_marked(n, M)` picks the elements with `np.random.randint(N, size=M)`, so they **may coincide**. The saved
> output actually gives `['001', '001']`: two identical MCX gates cancel, and the oracle marks nothing at all. It should use
> `np.random.choice(N, size=M, replace=False)`.

> Minor note: in section 2.2, $|m^\perp\rangle$ is written as $\sum_{x \neq 0}$; it should be $\sum_{x \neq m}$ (and it needs normalization).
> Section 3 also lacks normalization in the same way: it should be $|\xi\rangle = \frac{1}{\sqrt M}\sum_{m \in \Xi}|m\rangle$ and
> $|\xi^\perp\rangle = \frac{1}{\sqrt{N-M}}\sum_{x \notin \Xi}|x\rangle$.
> In section 2.1 step 5, the general formula for $\alpha_x^{(5)}$ has the denominator $N$; it should be $N^2$; the numerical values 0.972 and
> $-0.088$ are still correct. Section 2.2 writes "$(U_f V)^2$", which should be $(V U_f)^2$ as in the figure.
> In section 1, the line that prints `found after: {x_in} tries` prints the **index** $x$, so the real number of tries is `x_in + 1`.

### Results

| Check | Output |
|---|---|
| `find_κ(32)` and the closed formula | both give $\kappa = 4$ |
| Classical search, $n = 5$ | `marked element: 01101`, found at index 13 (the 14th try) out of 32 |
| Grover $n = 3$, $\kappa = 2$, $2^{13}$ shots | `m = 110` is the most frequent result (chart) |
| Grover $M = 2$, $n = 5$ | `['00010', '11100']` are the two standout results (chart) |

### Quick recap

- One Grover round = oracle (flips the sign of the marked element) + diffuser (reflection about the mean).
- $H^{\otimes n}X^{\otimes n}\,\text{MCZ}\,X^{\otimes n}H^{\otimes n} = -(2|s\rangle\langle s| - I)$, that is, it equals $V$ up to a global phase.
- Geometry: each round rotates by $\theta = 2\arcsin\sqrt{M/N}$; the success probability after $\kappa$ rounds is
  $\sin^2\big((2\kappa+1)\tfrac\theta2\big)$; $\kappa \approx \frac\pi4\sqrt{N/M}$. Repeating **more** than $\kappa$ rounds lowers the probability.
- Classically $\sim N$, Grover $\sim\sqrt N$: a **quadratic** speedup, not an exponential one, and no quantum algorithm does better.
- It is useful only when the oracle can be built efficiently.

---

## Comparison of the 4 algorithms

<p align="center"><img src="images/04_04_02_algo_compare.png" width="760" alt="Three circuits side by side: Deutsch–Jozsa, Bernstein–Vazirani and Simon, with the same template QHT, U_f, QHT and then measure, plus notes on how to read the result of each algorithm"></p>

*Figure: the common template of DJ, BV and Simon: DJ and BV run once; Simon runs until it has $n-1$ linearly independent results and then post-processes (the Grover circuit is in section 04_04).*

| | Deutsch–Jozsa | Bernstein–Vazirani | Simon | Grover |
|---|---|---|---|---|
| Output of $f$ | 1 bit | 1 bit | $n$ bits | 1 bit |
| Ancilla qubits | 1, in $\vert -\rangle$ | 1, in $\vert -\rangle$ | $n$, in $\vert 0\rangle^{\otimes n}$ | 1, in $\vert -\rangle$ |
| Key mechanism | Kickback + $H^{\otimes n}$ | Kickback + $H^{\otimes n}$ | Measure the bottom register + $H^{\otimes n}$ | Kickback + diffuser, repeated $\kappa$ times |
| Result of each run | Deterministic | Deterministic | Random: a $z$ with $s\cdot z = 0$ | High probability |
| Classical post-processing | None | None | Gaussian elimination modulo 2 | Check $f(x_\text{out})$ |
| Oracle calls, classical | $2^{n-1}+1$ (with certainty) | $n$ | $\sim 2^{n/2}$ | $\sim N$ |
| Oracle calls, quantum | 1 | 1 | $\sim n$ | $\sim\sqrt N$ |
| Advantage (number of oracle calls) | Exponential, but only against deterministic classical algorithms | Linear | Exponential, even against randomized classical algorithms | Quadratic, and optimal |

## API summary for this part

| API / function | Used for | Lesson |
|---|---|---|
| `QuantumCircuit(n, m, name=)`, `QuantumRegister` | Create a named circuit/black box | 04_01–04_04 |
| `qc.append(sub_circuit_or_gate, qubits)` | Attach the black box or the diffuser to the circuit | 04_01–04_04 |
| `qc.mcx(controls, target, ctrl_state=)` | Oracle: flip $y$ at one value of $x$ | 04_01, 04_03, 04_04 |
| `qc.cx(list_controls, list_targets)` | Several CX gates at once (BV oracle) | 04_02 |
| `qc.prepare_state(k, qubits)` | Load a classical input $\vert k\rangle$ | 04_01, 04_04 |
| `ZGate().control(k)` | Create the MCZ for the diffuser | 04_04 |
| `BitFlipOracleGate(expr, vars)` | Build an oracle from a Boolean expression | 04_03 |
| `sympy.symbols`, `sympy.logic.boolalg.SOPform` | Simplify Boolean expressions | 04_03 |
| `qc.decompose()` | Look at the circuit inside a gate | 04_03, 04_04 |
| `transpile(qc, simulator)`, `AerSimulator().run(qc, shots=, memory=True)` | Run circuits | 04_01–04_04 |
| `result.get_memory()`, `result.get_counts()` | Get the bit string of each shot / the counts | 04_01–04_04 |
| `Statevector(qc)`, `Statevector.from_label` | Check the exact state | 04_01–04_03 |
| `plot_histogram`, `plot_distribution` | Plot the results | 04_01, 04_04 |
| `np.binary_repr`, `np.random.choice(..., replace=False)` | Binary strings, random choice without repeats | 04_01–04_04 |

## How to run

Open the notebooks in VS Code or Jupyter, select the repo's `.venv` kernel, and run from top to bottom. The required libraries
are in [requirements.txt](../../requirements.txt); 04_03 also needs `sympy`, which is already included in that file.

- Everything runs on a local `AerSimulator`; no IBM account is needed.
- The black box, the secret string and the marked element are all generated **randomly**, so the output differs from the saved one on every run;
  the conclusions do not change (except for the bugs in `black_box()` in 04_01 and in `Uf_M_marked` in 04_04 mentioned above).
- Some classical/quantum comparison charts (probability versus the number of tries) exist only as **static images** in the notebooks,
  with no code that generates them.
- The notebooks reuse functions between sections (for example `black_box_n`, `diffuser`, `fx_simon`), so they must be run in order.

---

<!-- nav -->
[← 03 · Quantum protocols](../03_quantum_protocols/README.en.md) · [Contents](../../README.en.md#contents) · [Keep learning after Part 04 →](../../docs/learning-path.en.md#what-comes-after-part-04)
