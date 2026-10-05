# 02 · Quantum computing

[Tiếng Việt](README.md) · **English** · [简体中文](README.zh-CN.md)

Starting from the Stern–Gerlach experiment with electron spin, this part builds up the concept of the **qubit**, then goes
through superposition, entanglement, the Bloch sphere, quantum gates and measurement, and finally the
**building blocks** such as the Bell/GHZ/W states, the Hadamard transform, phase kickback and oracles.
This is the direct foundation for Part 03 (protocols) and Part 04 (algorithms).

> Source: [02_01](https://learnquantum.io/chapters/02_quantum_computing/02_01_bits_to_qubits.html) ·
> [02_02](https://learnquantum.io/chapters/02_quantum_computing/02_02_entanglement.html) ·
> [02_03](https://learnquantum.io/chapters/02_quantum_computing/02_03_single_qb_sys.html) ·
> [02_04](https://learnquantum.io/chapters/02_quantum_computing/02_04_multi_qb_sys.html) ·
> [02_05](https://learnquantum.io/chapters/02_quantum_computing/02_05_quantum_blocks.html)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## Contents

| Lesson | Notebook | Web | Key idea |
|---|---|---|---|
| 02_01 · Qubits and quantum circuits | [02_01_bits_to_qubits.ipynb](02_01_bits_to_qubits.ipynb) | [link](https://learnquantum.io/chapters/02_quantum_computing/02_01_bits_to_qubits.html) | Electron spin → probability amplitude → qubit; X and H gates; the first circuit in Qiskit |
| 02_02 · Quantum entanglement | [02_02_entanglement.ipynb](02_02_entanglement.ipynb) | [link](https://learnquantum.io/chapters/02_quantum_computing/02_02_entanglement.html) | Separable and entangled states; H + CX creates entanglement |
| 02_03 · Single-qubit systems | [02_03_single_qb_sys.ipynb](02_03_single_qb_sys.ipynb) | [link](https://learnquantum.io/chapters/02_quantum_computing/02_03_single_qb_sys.html) | Complex amplitudes, Bloch sphere, phase; Pauli, P/S/T, RX/RY/RZ gates; measurement, observables |
| 02_04 · Multi-qubit systems | [02_04_multi_qb_sys.ipynb](02_04_multi_qb_sys.ipynb) | [link](https://learnquantum.io/chapters/02_quantum_computing/02_04_multi_qb_sys.html) | n-qubit states; controlled gates, SWAP; no-cloning; universal gate sets; partial measurement |
| 02_05 · Quantum building blocks | [02_05_quantum_blocks.ipynb](02_05_quantum_blocks.ipynb) | [link](https://learnquantum.io/chapters/02_quantum_computing/02_05_quantum_blocks.html) | Bell, GHZ, W; Hadamard transform; phase kickback; oracles |

> The code snippets in this README are **excerpts** from the notebooks (the original English comments are kept) and use variables defined in earlier cells. To run them, run the whole notebook from top to bottom.

---

## 02_01 · Qubits and quantum circuits

**Goal:** understand why we need **probability amplitudes** instead of probabilities, and build the first quantum circuit.

### Key concepts

> If the physics below is unfamiliar, don't worry. You only need to carry one idea with you:
> **probability = the square of the amplitude**, and amplitudes can be negative. The experiment is just the way the
> textbook leads you to that idea.

**The Stern–Gerlach experiment.** An electron has spin (an intrinsic property that makes it behave like a very small magnet).
Send it through a magnetic field that is not uniform along the $z$ axis:
- spin $+z$ is always deflected up, spin $-z$ is always deflected down;
- spin $\pm x$ does **not** go straight through as a classical magnet would, but is deflected up or down, 50% each, and **never** stays in the middle.

(The textbook uses electrons because they are easier to picture. The real experiment used electrically neutral silver atoms,
because for a charged electron the Lorentz force would overwhelm the effect of the spin.)

<p align="center"><img src="images/02_01_05_stern-gerlach_up-down_elec.png" width="700" alt="Stern–Gerlach apparatus: a spin-up electron is deflected up, a spin-down electron is deflected down"></p>

*Figure: An electron with spin $+z$ is always deflected up (left), and one with spin $-z$ is always deflected down (right).*

<p align="center"><img src="images/02_01_06_stern-gerlach_right_elec.png" width="360" alt="A spin +x electron passing through a Stern–Gerlach apparatus is deflected up or down, 50% each"></p>

*Figure: An electron with spin $+x$ does not go straight through but is deflected up or down, 50% each.*

**Probability vectors are not enough.** Try describing spin with a probability vector (as in 01_04). When measured along the $z$ axis,
both $+x$ and $-x$ give 50% up and 50% down, so both are $[\tfrac12, \tfrac12]^\top$. But they are two *different* states:
if we rotate the measuring device to the $x$ axis, we can tell them apart (one always gives $+x$, the other always gives $-x$).
The probability vector has lost information.

<p align="center"><img src="images/02_01_08_stern-gerlach_left-right_elec.png" width="700" alt="A Stern–Gerlach apparatus rotated so that the magnetic field points along the x axis: spin +x and spin −x electrons are deflected to opposite sides"></p>

*Figure: Rotating the apparatus so that the field points along the $x$ axis: spin $+x$ (left) and spin $-x$ (right) are deflected to opposite sides.*

Even worse, a spin $+z$ electron passing through an apparatus set along the $x$ axis is also deflected to either side, 50% each.
So spin $+z$ can be seen as a combination, half of each, of $+x$ and $-x$.

<p align="center"><img src="images/02_01_09_stern-gerlach_up_elec.png" width="360" alt="A spin +z electron passing through a Stern–Gerlach apparatus set along the x axis is deflected to either side, 50% each"></p>

*Figure: A spin $+z$ electron passing through an apparatus set along the $x$ axis: it is deflected to either side, 50% each.*

But if we take half of each vector and add them, $\tfrac12[\tfrac12, \tfrac12]^\top + \tfrac12[\tfrac12, \tfrac12]^\top$,
we only get back $[\tfrac12, \tfrac12]^\top$, not $[1, 0]^\top$: the "down" component must **cancel out**, and since probabilities
are never negative they cannot cancel. So we must allow **negative** entries, and make the probability the **square** of the amplitude
(the Born rule):

$$|s\rangle = \begin{bmatrix}s_0\\ s_1\end{bmatrix}, \qquad \mathbb{P}_{+z} = s_0^2, \quad \mathbb{P}_{-z} = s_1^2$$

**The qubit.** Let us rename things: spin up is $|0\rangle$, spin down is $|1\rangle$, and

$$|+\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big), \qquad |-\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)$$

> Note: in the summary at the end of section 1.2, the notebook labels both vectors $|s_{-x}\rangle$; the vector
> $[\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2}]^\top$ should be $|s_{+x}\rangle$. Right before that, the sentence "find what $s_0$ and $s_1$
> for the vector $|s_{-z}\rangle$ should be" should also say $|s_{-x}\rangle$.

The general definition:

$$|q\rangle = \begin{bmatrix}\alpha_0\\ \alpha_1\end{bmatrix}, \quad \alpha_j \in \mathbb{C}, \quad |\alpha_0|^2 + |\alpha_1|^2 = 1$$

(The symbol $\mathbb{C}$ is the set of complex numbers. You don't need to understand it yet; it is covered in 02_03. For now, just treat amplitudes as real numbers that can be negative.)

To compare: a bit has entries in $\{0,1\}$; a p-bit has entries in $[0,1]$ whose **sum** is 1; a qubit has **complex** entries
whose **squared moduli add up** to 1.

> Superposition does **not** mean "both 0 and 1" or "being in two states at the same time". $|+\rangle$ is
> **one perfectly definite state**; it is just that, when we choose the $z$ axis to describe it, it is written as a
> combination of $|0\rangle$ and $|1\rangle$ with equal amplitudes.

**A quantum circuit has 3 steps:**
1. **State preparation**, almost always $|0\rangle$.
2. **Transforming the state** with gates.
3. **Measurement**: projecting the quantum state onto classical bits, in a probabilistic way.

<p align="center"><img src="images/02_01_10_spin_vs_qubit_x.png" width="750" alt="The spin experiment and the matching circuit: prepare |0⟩, X gate, measurement always gives 1"></p>

*Figure: The experiment (top) and the matching circuit (bottom). SG1 together with a screen lets only spin-up electrons continue (preparing $|0\rangle$), the magnetic field B flips the spin (the $X$ gate), and SG2 measures and always gives 1.*

**The first two gates:**

$$X = \begin{bmatrix}0&1\\1&0\end{bmatrix}\ (|0\rangle \leftrightarrow |1\rangle), \qquad
H = \tfrac{1}{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}\ (|0\rangle \leftrightarrow |+\rangle,\ |1\rangle \leftrightarrow |-\rangle)$$

<p align="center"><img src="images/02_01_11_spin_vs_qubit_h.png" width="750" alt="The experiment and circuit with an H gate: |0⟩ becomes |+⟩, and the measurement gives 0 or 1, 50% each"></p>

*Figure: The same experiment, but now the magnetic field B rotates the spin from $+z$ to $+x$ (the $H$ gate takes $|0\rangle$ to $|+\rangle$); SG2 gives 0 or 1, 50% each.*

> Note: the decimal form of $H$ in the notebook writes the bottom-right entry as $-\frac{\sqrt2}{\sqrt2}$; the correct value is
> $-\frac{\sqrt2}{2}$. The cell that sends $|0\rangle$ and $|1\rangle$ through `qc_h` prints the wrong label "over an X gate"; the output is
> that of the $H$ gate and is correct.

### Key code

```python
zero = Statevector.from_label('0')
one = Statevector.from_label('1')
plus = Statevector.from_label('+')
minus = Statevector.from_label('-')
```
Creates states from labels. You can also pass a list of amplitudes, for example `Statevector([np.sqrt(1/2), -np.sqrt(1/2)])`.

> Note: the earlier cell wrote `one = Statevector([1, 0])`, which is wrong, because that is $|0\rangle$. This cell overwrites it with
> `from_label('1')`, so the outputs that follow are still correct.

```python
display(plus.draw('latex', prefix='|+ \\rangle = '))                       # display ket representation of |+⟩
display(minus.draw('latex', prefix='|- \\rangle = ', convention='vector')) # display vector representation of |-⟩
```
`draw('latex')` displays the ket form; `convention='vector'` displays the vector form. Qiskit prints a column vector as a **row**
to save space, but it is still the same state.

```python
qc = QuantumCircuit(1,1)  # Create circuit object with 1 qubit and 1 classical bit
qc.reset(0)               # Add state preparation gate (reset) to qubit 0
qc.x(0)                   # Add X gate to circuit to qubit 0
qc.measure(0,0)           # Add measurement gate between qubit 0 and bit 0
qc.draw()
```
A 3-step circuit: reset → X → measure. In Qiskit every qubit starts in $|0\rangle$ by default, so `reset` is usually redundant.

```python
X = Operator(qc_x)
X.draw('latex', prefix='X =')
```
`Operator(circuit)` gets the unitary matrix of a circuit. `state.evolve(circuit)` sends a state through a circuit.
`Statevector(circuit)` always starts from $|0\dots0\rangle$.

```python
plus_counts = plus.sample_counts(100)
```
Simulates the measurement directly on the `Statevector`; `sample_memory(100)` returns the individual outcomes in order.

```python
simulator = BasicSimulator()           # define simulator object
job = simulator.run(qc_hm, shots=100)  # use run method to execute our circuit some number of shots
result = job.result()                  # extract our results
counts = result.get_counts()           # get the counts from the experiment
```
Runs a circuit that contains measurements on a simulator, just like the workflow on real hardware. `plot_histogram(counts)` plots the result.

### Results

| Check | Output |
|---|---|
| `Operator` of the X circuit | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ |
| $\vert 0\rangle$, $\vert 1\rangle$ through H | $\tfrac{\sqrt2}{2}(\vert 0\rangle \pm \vert 1\rangle)$ |
| X then H circuit from $\vert 0\rangle$ | $\vert -\rangle$; matrix $H\cdot X = \tfrac{\sqrt2}{2}\begin{bmatrix}1&1\\-1&1\end{bmatrix}$ |
| `plus.sample_counts(100)` | `{'0': 51, '1': 49}` |
| `zero.sample_counts(100)` | `{'0': 100}` |
| H + measurement circuit, 100 shots, `BasicSimulator` | `{'0': 41, '1': 59}` |

### Quick recap

- Probability = the square (of the modulus) of the amplitude; amplitudes can be negative, and in general they are complex numbers.
- $|+\rangle$ and $|-\rangle$ give the same probabilities when measured along $z$ but are two different states.
- $X$ swaps $|0\rangle \leftrightarrow |1\rangle$; $H$ swaps $|0\rangle \leftrightarrow |+\rangle$, $|1\rangle \leftrightarrow |-\rangle$.
- `Statevector` = exact calculation; `simulator.run(qc, shots=N)` = measure N times.
- `Operator(qc)` = the matrix of the circuit.

---

## 02_02 · Quantum entanglement

**Goal:** distinguish **separable** states from **entangled** states, and create entanglement with a circuit.

### Key concepts

**Two qubits** are combined with the Kronecker product, with the convention that $q_0$ is on the right: $|q\rangle = |q_1\rangle \otimes |q_0\rangle = |q_1 q_0\rangle$.

$$|+\rangle \otimes |+\rangle = \tfrac12\big(|00\rangle + |01\rangle + |10\rangle + |11\rangle\big)$$

Each outcome has probability $(1/2)^2 = 1/4$, which matches the experiment with two independent electrons.

<p align="center"><img src="images/02_02_03_two_spin_right_options.png" width="740" alt="Two independent electrons with the same spin +x, measured in two separate apparatuses: four up/down combinations, 25% each"></p>

*Figure: Two independent electrons, both with spin $+x$, measured in two separate apparatuses: 4 up/down combinations, 25% each.*

**Separable** = can be written as **a single** product of the individual qubit states. For example,
$\tfrac12(|00\rangle - |01\rangle + |10\rangle - |11\rangle) = |+\rangle \otimes |-\rangle$.

**Entanglement.** A spin-0 particle decays into two particles (such as electrons) with opposite spins. Measured along the $z$ axis:
we always get one up and one down, 50% for each case.

<p align="center"><img src="images/02_02_04_two_spin_entangled.png" width="700" alt="A particle decays into two electrons flying toward two measuring devices; one electron is always deflected up and the other down"></p>

*Figure: A particle (shown in purple) decays into two electrons flying toward two apparatuses set along $z$: always one up and one down, 50% for each case.*

One might guess that the pair is always created with spins already fixed along $z$. If that were so, rotating both apparatuses to the $x$ axis
would make the results on the two sides independent: 4 combinations, 25% each.

<p align="center"><img src="images/02_02_06_two_spin_x_entangled.png" width="700" alt="Hypothesis: the spins are already fixed along z, so after rotating the apparatuses each side gives 50/50, independent of the other side"></p>

*Figure: The hypothesis to be tested: if the spins of the pair are already fixed along $z$, then after rotating the apparatuses each side gives 50/50, independent of the other side. The experiment rejects this hypothesis.*

The experiment shows that this is **not** what happens: if we set both apparatuses along the same axis, whichever axis it is, we still always get one up and one down. If we rely
only on the measurement along $z$ (`01` and `10`, 1/2 each), both of the following states fit:

$$\tfrac{1}{\sqrt2}\big(|01\rangle + |10\rangle\big) \quad\text{or}\quad \tfrac{1}{\sqrt2}\big(|01\rangle - |10\rangle\big)$$

**Neither** of them can be split into a product of two separate states. In a classical system, if you know the complete state of the whole system,
you also know the complete state of each part; here that is not so. Of the two states above, only
$\tfrac{1}{\sqrt2}(|01\rangle - |10\rangle)$ gives opposite results along **every** axis, so it is the one that describes the pair
of particles produced by a spin-0 particle. With $\tfrac{1}{\sqrt2}(|01\rangle + |10\rangle)$, measuring both along the $x$ axis would always give the **same** direction.

> Note: the notebook calls $\tfrac{1}{\sqrt2}(|01\rangle + |10\rangle)$ a "reasonable choice" based only on the statistics along the $z$ axis,
> and then says the minus-sign state "gives the same observations too". That is true only when measuring along $z$; given the observation
> "opposite along any axis" above, only the minus-sign state fits.

> Do not over-interpret this: (1) each side still sees a random 50/50 result, so this correlation can **not** be used to send messages;
> (2) the "always opposite along the same axis" property alone can still be imitated by a classical model (each pair carries a predetermined
> random direction). What no "predetermined" model can do only shows up when the two apparatuses are set at **different angles** from each other, through the Bell
> inequality (not in the textbook; see the [glossary](../../docs/glossary.en.md)).

**Creating entanglement with a circuit** (H then CX):

$$|00\rangle \xrightarrow{H \otimes I} \tfrac{1}{\sqrt2}\big(|00\rangle + |10\rangle\big) \xrightarrow{CX} \tfrac{1}{\sqrt2}\big(|00\rangle + |11\rangle\big)$$

<p align="center"><img src="images/02_02_07_spin_vs_qubit_entangled.png" width="750" alt="The experiment and the circuit that creates entanglement: H then CX creates a Bell state, and the measurement gives 00 or 11"></p>

*Figure: The magnetic field B takes the upper electron to $+x$ (the $H$ gate), an electromagnetic field makes the two electrons interact (the $CX$ gate), producing $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$; the measurement gives `00` or `11`, 50% each.*

### Key code

```python
state_00 = state_0.tensor(state_0)    # compose state |0⟩⊗|0⟩
state_01 = state_0.tensor(state_1)    # compose state |0⟩⊗|1⟩
```
`a.tensor(b)` is $a \otimes b$; `b` is the qubit on the right (qubit 0).

```python
H = Operator.from_label('H')
I = Operator.from_label('I')
HI = H.tensor(I)
q = q.evolve(HI)
```
Doing it step by step with matrices: $H \otimes I$ applies H to $q_1$ and leaves $q_0$ unchanged. Then `q.evolve(CX)`
with `CX = Operator([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])`.

```python
qc_ent = QuantumCircuit(2)    # define quantum circuit
qc_ent.h(1)                   # apply H gate to qubit 1
qc_ent.cx(1,0)                # apply CX with control on q1 and target on q0
```
Doing it with a circuit gives the same result. `qc.measure_all()` adds a measurement on every qubit.

### Results

| Check | Output |
|---|---|
| $\vert +-\rangle$, $\vert -+\rangle$, $\vert --\rangle$ | the $\pm\tfrac12$ signs are exactly as the Kronecker product predicts |
| Separable circuit $\vert +\rangle\vert -\rangle$, 1000 shots | `{'01': 270, '10': 229, '11': 225, '00': 276}`, each outcome about 25% |
| H + CX circuit | $\tfrac{\sqrt2}{2}\vert 00\rangle + \tfrac{\sqrt2}{2}\vert 11\rangle$ |
| H + CX circuit, 1000 shots | `{'11': 508, '00': 492}`, `01` and `10` never appear |

### Quick recap

- $|q_1 q_0\rangle = |q_1\rangle \otimes |q_0\rangle$: qubit 0 is on the **right**.
- Separable = a single Kronecker product; entangled = not separable.
- Starting from $|00\rangle$: H on the control + CX = the standard way to create entanglement.
- Measuring $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$ along $z$: the two results are always the same, but each individual result is still
  random 50/50, so no message can be sent.

---

## 02_03 · Single-qubit systems

**Goal:** get the full definition of a qubit, represent it on the Bloch sphere, learn the single-qubit gates and formalize measurement.

### Key concepts

**An arbitrary angle θ.** A spin tilted by an angle $\theta$ from $+z$ gives $\mathbb{P}_0 = \cos^2\tfrac\theta2$ and $\mathbb{P}_1 = \sin^2\tfrac\theta2$, so

$$|q\rangle = \cos\tfrac\theta2\,|0\rangle + \sin\tfrac\theta2\,|1\rangle$$

<p align="center"><img src="images/02_03_01_stern-gerlach_angle_prob.png" width="360" alt="An electron with spin tilted by angle θ from the z axis: deflected up with probability cos²(θ/2), deflected down with probability sin²(θ/2)"></p>

*Figure: A spin tilted by an angle $\theta$ from $+z$: deflected up with probability $\cos^2(\theta/2)$, deflected down with probability $\sin^2(\theta/2)$.*

> Note: the table in section 1.1 of the notebook gives $|-\rangle$ as $\theta = \frac{3\pi}{2}$ with $\cos\frac\theta2 = \frac{1}{\sqrt2}$,
> $\sin\frac\theta2 = -\frac{1}{\sqrt2}$. For $\theta = \frac{3\pi}{2}$ we actually have $\cos\frac{3\pi}{4} = -\frac{1}{\sqrt2}$ and
> $\sin\frac{3\pi}{4} = \frac{1}{\sqrt2}$, which gives $-|-\rangle$ (the same state, differing only by a global phase, see below). The values
> in the table correspond to $\theta = -\frac{\pi}{2}$.

**Complex numbers are needed.** A spin in the $xy$ plane always gives 50/50 when measured along $z$.

<p align="center"><img src="images/02_03_02_elec_phi_angle.png" width="520" alt="A spin lying in the xy plane at an arbitrary angle φ: measuring along z always gives 50% up, 50% down"></p>

*Figure: A spin lying in the $xy$ plane, at an arbitrary angle $\varphi$ from the $x$ axis: measuring along $z$ always gives 50/50, regardless of $\varphi$.*

For $\pm y$, we need amplitudes that both give probability 1/2 and can be combined back into $|0\rangle$, $|1\rangle$. The only **real** numbers that
do this are $\pm\tfrac{1}{\sqrt2}$, but these are already used for $|\pm\rangle$ (the $x$ axis); so we have to use $\pm i$:

$$|r\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle + i|1\rangle\big), \qquad |l\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle - i|1\rangle\big)$$

<p align="center"><img src="images/02_03_05_spin_in_complex_plane.png" width="250" alt="The complex plane placed on top of the xy plane: 1, i, −1, −i lie on the +x, +y, −x, −y axes"></p>

*Figure: Placing the complex plane on the $xy$ plane: the numbers $1, i, -1, -i$ lie on the axes $+x, +y, -x, -y$; a spin at angle $\varphi$ corresponds to the number $e^{i\varphi}$.*

Stated precisely, the Born rule takes the **squared modulus**: $|c|^2 = c\,c^* = a^2 + b^2$. The general form for the $xy$ plane is
$\tfrac{1}{\sqrt2}(|0\rangle + e^{i\varphi}|1\rangle)$.

> Note: the notebook writes the angle of a complex number $c = a + bi$ as $\varphi = \text{atan2}(a, b)$; by the usual convention
> (`numpy.arctan2(y, x)`) it should be $\text{atan2}(b, a)$, with the imaginary part first. Also in section 1.2, the left-hand side of the "minus combination" is written
> $\frac{1}{\sqrt2}|r\rangle - \frac{i}{\sqrt2}|l\rangle$, but the calculation below it (which gives $i|1\rangle$) uses
> $\frac{1}{\sqrt2}|r\rangle - \frac{1}{\sqrt2}|l\rangle$.

**The Bloch sphere.** Combining the two results above:

$$|q\rangle = \cos\tfrac\theta2\,|0\rangle + e^{i\varphi}\sin\tfrac\theta2\,|1\rangle$$

$\theta \in [0, \pi]$ is the angle from the $+z$ axis; $\varphi \in [0, 2\pi)$ is the angle of the projection onto the $xy$ plane, measured from the
$+x$ axis. Every single-qubit state (ignoring the global phase, see right below) is a point on the unit sphere.

<p align="center"><img src="images/02_03_06_bloch.png" width="300" alt="The Bloch sphere with angle θ measured from the z axis, angle φ measured from the x axis, and the positions of |0⟩, |1⟩, |+⟩, |−⟩, |r⟩, |l⟩"></p>

*Figure: The Bloch sphere. $|0\rangle$ and $|1\rangle$ are at the two poles; $|\pm\rangle$ are on the $x$ axis; $|r\rangle$ and $|l\rangle$ are on the $y$ axis.*

**Global phase and relative phase.** For arbitrary complex $\alpha_0, \alpha_1$:

$$|q\rangle = e^{i\gamma}\Big[\cos\tfrac\theta2\,|0\rangle + e^{i\varphi}\sin\tfrac\theta2\,|1\rangle\Big]$$

- $\gamma$ is the **global phase**: it cannot be measured, because $|e^{i\gamma}|^2 = 1$. For example, $i|1\rangle$ is equivalent to $|1\rangle$.
- $\varphi$ is the **relative phase**: it can be measured, because it determines the position on the Bloch sphere. Measuring along $z$ does not
  reveal it (as with $|+\rangle$ and $|-\rangle$), but if we measure along $x$ or $y$, the result changes.

**Bra, inner product, basis.** The bra is the **conjugate transpose**: $\langle q| = [\alpha_0^*, \alpha_1^*]$. The inner product is
$\langle y|x\rangle = \langle x|y\rangle^*$; the norm is $\|q\| = \sqrt{\langle q|q\rangle}$. Three important orthonormal bases:

| Basis | States | Bloch axis |
|---|---|---|
| Computational (bit) | $\vert 0\rangle, \vert 1\rangle$ | $\pm z$ |
| Hadamard (sign) | $\vert +\rangle, \vert -\rangle$ | $\pm x$ |
| Y (hand) | $\vert r\rangle, \vert l\rangle$ | $\pm y$ |

> Note: in the example that converts $\sqrt{2/3}\,|0\rangle - \sqrt{1/3}\,|1\rangle$ to the sign basis, the notebook writes both coefficients as
> $\frac{2\sqrt3 - \sqrt6}{6}$. The coefficient of $|-\rangle$ should be $\frac{2\sqrt3 + \sqrt6}{6} \approx 0.986$; the numerical value in the
> notebook is correct.

The outer product $|x\rangle\langle y|$ is a matrix; the two projectors $\Pi_0 = |0\rangle\langle 0|$ and $\Pi_1 = |1\rangle\langle 1|$ are used for measurement.

**Gates are unitary matrices**: $UU^\dagger = U^\dagger U = I$. This is why every gate has an inverse gate $U^\dagger$ (quantum computation
is reversible), and why a unitary preserves the norm of a vector.

| Gate | Matrix | Effect on the Bloch sphere |
|---|---|---|
| Pauli $X$ | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ | Rotation by π about the $x$ axis |
| Pauli $Y$ | $\begin{bmatrix}0&-i\\i&0\end{bmatrix}$ | Rotation by π about the $y$ axis |
| Pauli $Z$ | $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ | Rotation by π about the $z$ axis: $Z\vert +\rangle = \vert -\rangle$, $Z\vert 1\rangle = -\vert 1\rangle$ |
| Phase $P(\varphi)$ | $\begin{bmatrix}1&0\\0&e^{i\varphi}\end{bmatrix}$ | Rotation by $\varphi$ about $z$; $Z = P(\pi)$, $S = P(\pi/2)$, $T = P(\pi/4)$ |
| $S^\dagger$, $T^\dagger$ | $e^{-i\varphi}$ in the lower corner | Rotation in the opposite direction |
| $RX(\theta)$ | $\begin{bmatrix}\cos\frac\theta2 & -i\sin\frac\theta2\\ -i\sin\frac\theta2 & \cos\frac\theta2\end{bmatrix}$ | Rotation by θ about $x$ |
| $RY(\theta)$ | $\begin{bmatrix}\cos\frac\theta2 & -\sin\frac\theta2\\ \sin\frac\theta2 & \cos\frac\theta2\end{bmatrix}$ | Rotation by θ about $y$ |
| $RZ(\varphi)$ | $\begin{bmatrix}e^{-i\varphi/2}&0\\0&e^{i\varphi/2}\end{bmatrix}$ | Rotation by φ about $z$; $RZ(\varphi) = e^{-i\varphi/2}P(\varphi)$ |

> Note: the notebook says that $S$ together with $H$ and $CX$ is enough to approximate every gate. In fact $\{H, S, CX\}$ only generates the Clifford group,
> and this group can be simulated efficiently on a classical computer (the Gottesman–Knill theorem). Adding the **$T$** gate (the Clifford+T set)
> is what makes the set universal. Lesson 02_04 of the textbook itself says exactly this. The Solovay–Kitaev theorem that the notebook cites does not say
> which sets are universal either; it says that once you have a universal gate set, approximating a gate to an error $\varepsilon$ needs only a
> number of gates on the order of a power of $\log(1/\varepsilon)$, that is, the approximation is **efficient**.

**Destructive and non-destructive measurement.** If an electron hits a screen, it is absorbed: this is a **destructive**
measurement, and afterwards there is no spin left to talk about.

<p align="center"><img src="images/02_03_07_dest_meas.png" width="375" alt="Destructive measurement: after the Stern–Gerlach apparatus the electron hits a screen and leaves a mark at the top or the bottom, 50% each"></p>

*Figure: Destructive measurement: the electron is absorbed by the screen, leaving a mark only at the top or at the bottom (50% each).*

If we cut two holes in the screen for the electron to fly through, we know which way it went and the electron is still there: this is a
**non-destructive** measurement. After the measurement, the spin is in exactly the state that matches the result. The textbook calls this
the state being **projected** or **reduced**, and avoids the word "collapse" because it is often tied to one particular
interpretation of quantum mechanics.

<p align="center"><img src="images/02_03_08_nondest_meas.png" width="400" alt="Non-destructive measurement: the electron flies through the upper or lower hole and remains in the spin-up or spin-down state"></p>

*Figure: Non-destructive measurement: the electron flies through the upper or lower hole (50% each) and continues to exist in the corresponding spin-up or spin-down state.*

So a measurement produces three things: a classical result $j$, its probability $\mathbb{P}_j$, and the quantum state $|j\rangle$ after the measurement.

<p align="center"><img src="images/02_03_09_meas_cir.png" width="500" alt="A circuit with H then a measurement: the classical register receives 0 or 1, and the qubit after the measurement is |0⟩ or |1⟩, each with probability 1/2"></p>

*Figure: Measuring $|+\rangle$: the classical result (0 or 1) is written to the classical register $c$ (the double line), each result has probability 1/2, and the qubit after the measurement is $|0\rangle$ or $|1\rangle$ accordingly.*

**Projective measurement (PVM).** For a set of projectors $\{\Pi_j\}$:
1. Each $\Pi_j$ corresponds to a classical result $j$.
2. Probability: $\mathbb{P}_j = \langle q|\Pi_j|q\rangle$.
3. State after the measurement: $|q'\rangle = \Pi_j|q\rangle / \sqrt{\mathbb{P}_j}$.

This way of writing it sounds redundant for 1 qubit, but it is essential when we measure only part of a multi-qubit system (Lesson 02_04).

> Note (small typos in the notebook): section 3.1 writes $\langle 1|(\alpha_1|0\rangle + \alpha_1|1\rangle)$, which should be
> $\alpha_0|0\rangle + \alpha_1|1\rangle$; and it writes $\sqrt{\mathbb{P}_i}$ twice, which should be $\sqrt{\mathbb{P}_j}$. Section 2.3 lists
> "RX, RY, RX", which should be $RX, RY, RZ$.

**Post-selection and reset.** Post-selection means measuring and then keeping only the desired result. Reset means measuring and then applying $X$ if the result is 1,
so that the qubit always ends up in $|0\rangle$.

**An observable** is a measurable quantity, written as a Hermitian matrix $\mathcal{O} = \sum_j \lambda_j \Pi_j$, where $\lambda_j$ are the
measured values. Assigning $|0\rangle \to +1$ and $|1\rangle \to -1$ gives exactly the matrix $Z = \Pi_0 - \Pi_1$ (similarly for $X$, $Y$).
The expectation value is

$$\langle \mathcal{O}\rangle_q = \langle q|\mathcal{O}|q\rangle$$

For example, $|q\rangle = \sqrt{1/3}\,|0\rangle + \sqrt{2/3}\,|1\rangle$ gives $\langle X\rangle = 2\sqrt{2/9} \approx 0.943$.

### Key code

```python
θ = np.pi/3                # Spin angle wrt to +z axis
α0 = np.cos(θ/2)           # Probability amplitude associated with |0⟩
α1 = np.sin(θ/2)           # Probability amplitude associated with |1⟩

q = Statevector([α0, α1])  # Construct statevector |q⟩ = α0|0⟩ + α1|1⟩ = [α0 α1]ᵀ

probs = q.probabilities() # Extract expected probs array [P₀, P₁]
```
`probabilities()` gives the exact probabilities; `sample_counts(shots=1000)` gives sampled results.

```python
θ = np.pi/3
φ = 2*np.pi/5

α0 = np.cos(θ/2)
α1 = np.sin(θ/2) * np.exp(1j*φ)

sv = Statevector([α0, α1])
sv.draw('bloch')
```
Draws any qubit on the Bloch sphere; change θ and φ to see the vector move.

```python
qc_p = QuantumCircuit(3)
qc_p.h(range(3)) # prepare |+⟩ state in all three qubits
qc_p.z(2)
qc_p.s(1)
qc_p.t(0)
```
Three phase gates on three qubits, then `Statevector(qc_p).draw('bloch', reverse_bits=True)` to compare. The version that rotates in the opposite direction uses `sdg`, `tdg`.

```python
qc = QuantumCircuit(1,1)
qc.h(0)                           # Initialize in superposition
qc.save_statevector('q_pre')     # Save statevector before reset
qc.measure(0,0)                   # Measure state (should give 50/50 `0` or `1`)
with qc.if_test((0,1)): qc.x(0)   # Apply X gate if classical result is `1`
qc.save_statevector('q_pst')      # Save statevector after reset
```
A manual reset: `if_test((clbit, value))` is an instruction controlled by the measurement result (classical feed-forward).
`save_statevector` is an Aer instruction that saves the state in the middle of a circuit.

```python
O = Operator.from_label('X')
O_expval = q.expectation_value(O)
```
The exact expectation value from `Statevector`.

```python
Obs = SparsePauliOp.from_operator(O)
estimator = Estimator(mode=AerSimulator())
result = estimator.run([(qc_o, Obs)]).result()
O_expval = result[0].data.evs
```
The expectation value estimated by sampling, through the `Estimator` primitive (from `qiskit_ibm_runtime`) running on AerSimulator.
No IBM account is needed.

### Results

| Check | Output |
|---|---|
| θ = π/3: `probabilities()` | `[0.75 0.25]` |
| θ = π/3: `sample_counts(1000)` | `{'0': 763, '1': 237}` |
| Reset: before / after | $\tfrac{\sqrt2}{2}(\vert 0\rangle + \vert 1\rangle)$ / $\vert 0\rangle$ |
| Exact $\langle X\rangle$ (`expectation_value`) | `0.9428` |
| $\langle X\rangle$ with `Estimator` | `0.936` (with sampling error) |

### Quick recap

- A qubit = a point on the Bloch sphere: $\cos\frac\theta2|0\rangle + e^{i\varphi}\sin\frac\theta2|1\rangle$.
- The global phase cannot be measured; the relative phase can.
- Probability = $|\alpha|^2 = \alpha\alpha^*$; the bra is the **conjugate transpose**.
- Gate = unitary = rotation on the Bloch sphere; $S = P(\pi/2)$, $T = P(\pi/4)$, $Z = P(\pi)$.
- Measurement: $\mathbb{P}_j = \langle q|\Pi_j|q\rangle$, and after the measurement the state is $\Pi_j|q\rangle/\sqrt{\mathbb{P}_j}$.
- Expectation value: $\langle q|\mathcal{O}|q\rangle$; exact with `expectation_value`, by sampling with `Estimator`.

---

## 02_04 · Multi-qubit systems

**Goal:** extend everything to $n$ qubits: states, multi-qubit gates, the no-cloning theorem, universal gate sets and partial measurement.

### Key concepts

**An $n$-qubit state** is a combination of $N = 2^n$ basis states:

$$|q\rangle = \sum_{j=0}^{N-1} \alpha_j |j\rangle, \qquad \sum_j |\alpha_j|^2 = 1, \qquad \langle i|j\rangle = \delta_{ij}$$

$|j\rangle$ is shorthand for the corresponding binary number, for example $|5\rangle \sim |101\rangle$.

> Note: the notebook writes that $j$ (and $i$) runs "from 0 to $2^{N-1}$"; it should be from 0 to $N - 1 = 2^n - 1$, as in the index of the sum.

**Single-qubit gates on several qubits:** $U = U_{n-1} \otimes \dots \otimes U_0$; for example, X on $q_0$, H on $q_1$, Z on $q_2$
is $Z \otimes H \otimes X$. Gates of this product form **cannot create entanglement**; we need an **entangling gate**.

**Controlled gates written with projectors:**

$$CU = \Pi_0 \otimes I + \Pi_1 \otimes U$$

| Gate | Formula / notes |
|---|---|
| $CX$ | $\Pi_0 \otimes I + \Pi_1 \otimes X$ |
| $CZ$ | $\Pi_0 \otimes I + \Pi_1 \otimes Z$ = diag(1, 1, 1, −1); **symmetric**: swapping control and target gives the same matrix |
| $CP(\varphi)$ | $\Pi_0 \otimes I + \Pi_1 \otimes P(\varphi)$ |
| $\overline{C}X$ (activated when the control is 0) | $\Pi_1 \otimes I + \Pi_0 \otimes X$ = X, then CX, then X on the control |
| $CCX$ (Toffoli) | $(\Pi_{00} + \Pi_{01} + \Pi_{10}) \otimes I + \Pi_{11} \otimes X$ |
| Control not adjacent to the target | Insert $I$ in between: $CZ_{20} = \Pi_0 \otimes I \otimes I + \Pi_1 \otimes I \otimes Z$ |
| SWAP | Swaps the states of two qubits; equal to 3 CX gates (like the XOR swap trick) |
| CSWAP (Fredkin) | Controlled SWAP |

> Note: the notebook calls SWAP an "entangling gate". It is true that SWAP cannot be written as a tensor product of single-qubit
> gates, but it turns every separable state $|a\rangle|b\rangle$ into $|b\rangle|a\rangle$, which is still separable. So SWAP
> on its own does **not** create entanglement.

**The no-cloning theorem.** CX can copy $|0\rangle$ and $|1\rangle$.

<p align="center"><img src="images/02_04_01_copy_1.png" width="500" alt="The CX gate copies the state |ψ⟩ of qubit 1 to qubit 0, only when |ψ⟩ is |0⟩ or |1⟩"></p>

*Figure: CX copies the state $|\psi\rangle$ of qubit 1 to qubit 0 (initialized to $|0\rangle$), but only when $|\psi\rangle$ is $|0\rangle$ or $|1\rangle$.*

Suppose there were a gate $\Theta$ that copies any state:
$(\alpha_0|0\rangle + \alpha_1|1\rangle)|0\rangle \to (\alpha_0|0\rangle + \alpha_1|1\rangle)^{\otimes 2}$.

<p align="center"><img src="images/02_04_02_copy_2.png" width="500" alt="The hypothetical copying gate Θ copies every state |ψ⟩ of qubit 1 to qubit 0"></p>

*Figure: The hypothetical copying gate $\Theta$, applied to every $|\psi\rangle$. The no-cloning theorem says that such a gate does not exist.*

Because a unitary is linear, the output would have to be
$\alpha_0|00\rangle + \alpha_1|11\rangle$, whereas a true copy is
$\alpha_0^2|00\rangle + \alpha_0\alpha_1|01\rangle + \alpha_1\alpha_0|10\rangle + \alpha_1^2|11\rangle$.
The two expressions are equal only when the state is $|0\rangle$ or $|1\rangle$. **An arbitrary quantum state cannot be copied.**

> Note: the notebook writes the second case as $(\alpha_1 = 0, \alpha_1 = 1)$; it should be $(\alpha_0 = 0, \alpha_1 = 1)$.

A **universal gate set** can approximate any unitary to arbitrary precision.
- Today's hardware: native gate sets with continuous parameters, for example $\{CX, SX, RZ(\theta)\}$; `transpile` translates a circuit into such a set.
- Margolus ($RCCX$) is like CCX, differing only in phase: $|101\rangle \to -|101\rangle$, $|110\rangle \to i|111\rangle$,
  $|111\rangle \to -i|110\rangle$ (the textbook simplifies this to adding the phases $-1, i, -i$ to these three inputs). When these phases do not
  affect the result, it needs far fewer gates.
- Fault-tolerant machines use **Clifford+T**: a circuit made only of Clifford gates $\{H, S, CX\}$ can be simulated efficiently on a
  classical computer (Gottesman–Knill); adding $T$ is what brings it up to full quantum power. In most error-correction architectures, the $T$ gate is the most expensive, so
  we must minimize the **T-depth** (the number of layers of T/T† gates).

> Note: the notebook says that the reason why adding $T$ gives full quantum power is "explained by the Solovay–Kitaev theorem". That is not
> so: the universality of Clifford+T comes from the fact that $H$ and $T$ generate a dense set of single-qubit rotations;
> Solovay–Kitaev only tells us that this approximation is **efficient** (a number of gates on the order of a power of $\log(1/\varepsilon)$).

**Measuring everything:** $\mathbb{P}_j = |\alpha_j|^2$, and after the measurement the state becomes $|j\rangle$.

**Partial measurement.** Split the system into a measured part $A$ and an unmeasured part $B$. For the first $m$ qubits ($q_0, \dots, q_{m-1}$, which sit on the **right**
of the tensor product):

$$\Pi_k^A = I^{\otimes(n-m)} \otimes \Pi_k, \qquad \mathbb{P}_k^A = \langle q|\Pi_k^A|q\rangle, \qquad |q'\rangle = \frac{\Pi_k^A|q\rangle}{\sqrt{\mathbb{P}_k^A}}$$

For example, $|w\rangle = \tfrac{1}{\sqrt3}(|001\rangle + i|010\rangle - |100\rangle)$, measuring only $q_0$: $\mathbb{P}_0 = 2/3$, $\mathbb{P}_1 = 1/3$.
If the result is 0, the remaining state is $\tfrac{i}{\sqrt2}|010\rangle - \tfrac{1}{\sqrt2}|100\rangle$; if it is 1, the state is $|001\rangle$.

### Key code

```python
Π0 = Operator.from_label('0')
Π1 = Operator.from_label('1')
I = Operator.from_label('I')
X = Operator.from_label('X')

CX = Π0.tensor(I) + Π1.tensor(X)
```
Builds CX from projectors; `Operator.from_label('0')` is exactly $|0\rangle\langle 0|$.

```python
qc = QuantumCircuit(2)
qc.cx(1,0,ctrl_state='0')
```
`ctrl_state` changes the activation condition. With several controls: `qc.ccx(1,2,0,ctrl_state='10')`. The string is read in
little-endian style: the character on the **right** corresponds to the **first** control in the list ($q_1$), so `'10'` means $q_2 = 1$,
$q_1 = 0$ (output: only $|100\rangle \leftrightarrow |101\rangle$ are swapped).

```python
qc_t = transpile(qc, basis_gates=['cx', 'sx', 'rz']) # Converts arbitrary circuit to a given basis gate-set
```
Translates CCX (or `rccx`) into the hardware's native gate set.

```python
T_depth = qc.depth(lambda instr: instr.operation.name in ['t', 'tdg'])
```
Counts the T-depth: `depth()` with a filter that counts only the `t` and `tdg` gates.

```python
# Create 3-qubit |w⟩ state:
w = np.sqrt(1/3)*(Statevector.from_int(1,8) + 1j*Statevector.from_int(2,8) - Statevector.from_int(4,8))
probs = w.probabilities([0])
c_result, q_result = w.measure([0])
```
`from_int(k, dim)` creates $|k\rangle$; `probabilities([0])` and `measure([0])` measure only qubit 0 (drop `[0]` to measure everything).

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
A circuit that prepares $|w\rangle$ using `cry` (controlled RY), then adds phases with Z and S. After that, measure and use `save_statevector()`
to see the state after the measurement.

### Results

| Check | Output |
|---|---|
| `Z.tensor(H.tensor(X))` and `Operator(qc)` of the X/H/Z circuit | the same 8×8 matrix |
| `Π0⊗I + Π1⊗X` | the same matrix as `qc.cx(1,0)` |
| H⊗H then CZ | $\tfrac12(\vert 00\rangle + \vert 01\rangle + \vert 10\rangle - \vert 11\rangle)$ |
| 3 CX | exactly the SWAP matrix |
| Clifford+T circuit that builds CCX | exactly the CCX matrix, T-depth = `4` |
| `w.probabilities()` | `[0, 1/3, 1/3, 0, 1/3, 0, 0, 0]` |
| `w.probabilities([0])` | `[2/3, 1/3]` |
| Measuring only $q_0$ gives 0 | $\tfrac{\sqrt2 i}{2}\vert 010\rangle - \tfrac{\sqrt2}{2}\vert 100\rangle$ |

### Quick recap

- $n$ qubits → $2^n$ amplitudes.
- Controlled gate: $\Pi_0 \otimes I + \Pi_1 \otimes U$; to skip over qubits in between, insert $I$.
- CZ is symmetric; SWAP = 3 CX; Fredkin = CSWAP.
- **No-cloning:** an arbitrary state cannot be copied (CX can only copy $|0\rangle$, $|1\rangle$).
- Clifford+T is universal; on fault-tolerant machines T is usually the most expensive, so minimize the T-depth.
- Partial measurement: $\Pi_k^A = I \otimes \dots \otimes \Pi_k$, then renormalize.

---

## 02_05 · Quantum building blocks

**Goal:** learn the sub-circuits that are reused in every protocol and algorithm that follows.

### Key concepts

**The four Bell states** (the Bell basis):

$$|\Phi^\pm\rangle = \tfrac{1}{\sqrt2}\big(|00\rangle \pm |11\rangle\big), \qquad |\Psi^\pm\rangle = \tfrac{1}{\sqrt2}\big(|01\rangle \pm |10\rangle\big)$$

The circuit H($q_1$) + CX($q_1 \to q_0$) turns $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ into
$|\Phi^+\rangle, |\Psi^+\rangle, |\Phi^-\rangle, |\Psi^-\rangle$ respectively. Or keep the input $|00\rangle$ and add a gate after CX: Z → $\Phi^-$, X → $\Psi^+$, X and Z → $\Psi^-$.

**GHZ** generalizes $|\Phi^+\rangle$: $|\Omega_n\rangle = \tfrac{1}{\sqrt2}(|0\rangle^{\otimes n} + |1\rangle^{\otimes n})$. There are three ways to build the circuit:

| Approach | Idea | Pros / cons |
|---|---|---|
| `ghz_cir_a` | H on the highest qubit, CX from it to every other qubit | Needs a connection to every qubit; hardware with only nearest-neighbor connections needs extra SWAPs |
| `ghz_cir_b` | CX gates chained between adjacent pairs | Needs only nearest-neighbor connections, but the CX gates run one after another: depth $n$, and qubits wait a long time, which makes errors likely |
| `ghz_cir_c` | H on the middle qubit, spreading out to both sides in parallel | Still only nearest-neighbor connections, and the depth drops to $\lceil n/2\rceil + 1$ |

> Note: the notebook gives the depth of `ghz_cir_b` as $n+1$ and that of `ghz_cir_c` as $n/2 + 2$. Counting with `qc.depth()` gives $n$ and
> $\lceil n/2\rceil + 1$ (for example, $n = 7$: 7 and 5). The conclusion "reduced by about half" is still correct.

**W** generalizes $|\Psi^+\rangle$: each term has exactly one bit equal to 1 (one-hot):
$|W_n\rangle = \tfrac{1}{\sqrt n}\sum_{j=0}^{n-1}|2^j\rangle$. The circuit uses RY/CRY to distribute the amplitudes, then CX to rearrange them.

**The quantum Hadamard transform** $\text{QHT}_n = H^{\otimes n}$, with matrix elements $h_{i,j} = (-1)^{i\cdot j}/\sqrt N$, where $i \cdot j$ is the
**binary dot product** (AND each pair of bits, then XOR the results together). The most important formula for Part 04:

$$H^{\otimes n}|j\rangle = \frac{1}{\sqrt N}\sum_{i=0}^{N-1}(-1)^{i\cdot j}|i\rangle, \qquad H^{\otimes n}|0\dots0\rangle = \frac{1}{\sqrt N}\sum_i |i\rangle$$

**Eigenvalues and eigenvectors.** $U|u\rangle = \lambda|u\rangle$. For a unitary, $|\lambda| = 1$, so $\lambda = e^{i\varphi}$: applying $U$ to an
eigenvector only adds a **global phase**, which cannot be measured. For example, $X$ has $(1, |+\rangle)$ and $(-1, |-\rangle)$; $S$ has $(1, |0\rangle)$ and $(i, |1\rangle)$.

**Phase kickback.** Put the control in superposition and the target in an eigenvector of $U$; the phase $e^{i\varphi}$ is "kicked back" onto the **control**
and becomes a **relative phase**, which means it can be measured:

$$\tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big)|u\rangle \xrightarrow{CU} \tfrac{1}{\sqrt2}\big(|0\rangle + e^{i\varphi}|1\rangle\big)|u\rangle$$

For example, with CX and target $|-\rangle$: $|+\rangle|-\rangle \to |-\rangle|-\rangle$, and sandwiched between two layers of H we get $|01\rangle \to |11\rangle$,
that is, the **target flips the control**. With several controls, only the state $|k\rangle$ that activates $U$ receives the phase, like
"marking" one state. This is a key step of Grover's algorithm (Part 04).

> Note: the notebook says that phase kickback plays a major role in algorithms with a "proven speedup" such as Shor's and
> Grover's. For Grover's, the quadratic speedup is proven in the query (oracle) model. For Shor's, the exponential speedup is only
> relative to the **best known** classical algorithm; no one has proven that there is no fast classical algorithm for the
> factoring problem.

**Computing Boolean functions with circuits.** Every $f:\{0,1\}^n \to \{0,1\}$ becomes a reversible unitary with the help of an ancilla qubit $y$:

$$U_f: |x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle$$

<p align="center"><img src="images/02_05_01_q_eval.png" width="700" alt="A classical function f(x) compared with the unitary U_f: it leaves the |x⟩ qubits unchanged and writes f(x) into the ancilla qubit, giving |y ⊕ f(x)⟩"></p>

*Figure: Left: the classical function $f(x)$, many bits in and one bit out, not reversible. Right: the unitary $U_f$ leaves the input qubits unchanged and XORs $f(x)$ into the ancilla qubit $y$.*

With $y = 0$ we get $f(x)$; with $y = 1$ we get $\overline{f(x)}$ (for example, a 3-bit AND built with `mcx` gives AND/NAND).

**Kickback by function.** Set $y = |-\rangle$:

$$|x\rangle|-\rangle \xrightarrow{U_f} (-1)^{f(x)}|x\rangle|-\rangle$$

**Two kinds of oracle** (black box):

| Oracle | Effect |
|---|---|
| Bit oracle $U_f$ | $\vert x\rangle\vert y\rangle \to \vert x\rangle\vert y \oplus f(x)\rangle$ |
| Phase oracle $Z_f$ | $\vert x\rangle \to (-1)^{f(x)}\vert x\rangle$; = a bit oracle with $y = \vert -\rangle$ and then discarding the qubit $y$, or built directly with MCZ without an ancilla qubit |

<p align="center"><img src="images/02_05_02_oracles.png" width="700" alt="The bit oracle U_f turns |x⟩|y⟩ into |x⟩|y ⊕ f(x)⟩; the phase oracle Z_f turns |x⟩ into (−1)^f(x)|x⟩"></p>

*Figure: The bit oracle $U_f$ (left) writes $f(x)$ into the qubit $y$; the phase oracle $Z_f$ (right) writes $f(x)$ into the sign $(-1)^{f(x)}$.*

<p align="center"><img src="images/02_05_03_oracle_equiv.png" width="400" alt="A bit oracle with the ancilla qubit in |−⟩ is equivalent to a phase oracle"></p>

*Figure: A bit oracle whose ancilla qubit is in $|-\rangle$ (this qubit is still $|-\rangle$ at the output) is equivalent to a phase oracle.*

### Key code

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
A low-depth GHZ circuit, using only CX gates between adjacent qubits.

> Note: the comment "place most significant qubit in equal superposition" was copied from `ghz_cir_a`; here H is applied to the middle qubit
> `qb_mid`, not to the highest qubit.

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
A circuit for the W state; the author explains it in detail in a [separate article](https://nbviewer.org/github/diemilio/quantum-playground/blob/main/w-states/w-states.ipynb).

```python
QHT = Operator.from_label('H'*n)
W = Statevector(w_cir(n))
y = W.evolve(QHT)
```
The QHT with Qiskit; the notebook also writes its own `qht_func(sv)` from the formula for $\beta_i$ for comparison, and gets the same result.

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
Phase kickback: H–CX–H turns $|01\rangle$ into $|11\rangle$, that is, the target has flipped the control.

```python
# create controlled S gate activated by state |01⟩
CC̄S = SGate().control(2, ctrl_state='01')
```
`Gate().control(k, ctrl_state=...)` creates a gate with $k$ controls from any gate; `qc.append(gate, qubits)` attaches it to a circuit.

> Note: in this cell the notebook assigns `qψ_in = Statevector(qc)` (an extra letter `q`) but then displays `ψ_in` from the earlier cell,
> so the output labeled "input", which shows $|01\rangle$, is **wrong**. The output labeled "output" is correct.

> Note: the text of section 3.3 (and the comment "activated by state |01⟩" above) says that the gate is activated when the controls are
> $|q_2 q_1\rangle = |01\rangle$ and predicts that $|01\rangle|1\rangle$ receives the phase $i$. But `ctrl_state` is read in little-endian style:
> with `qc.append(CC̄S, [2,1,0])`, the right-hand character `'1'` corresponds to the first control ($q_2$). So the gate is activated when
> $q_2 = 1$, $q_1 = 0$, and the output (correct according to the code) shows $|101\rangle$ receiving the phase $i$.
> Also in this section, $k$ runs from 0 to $2^m - 1$, not to $2^m$.

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
Kickback by function with a 3-bit AND: only $|111\rangle$ receives the sign $-$. `QuantumRegister(n, name='x')` gives a name to a group of qubits.

```python
qc.ccz(0,2,1, ctrl_state='01')             # Apply Zf 
```
A phase oracle built directly with CCZ, without an ancilla qubit: it marks $x = 011$.

> Note: the text of section 4.3 says $x = 010$ at one point and the state $|10\rangle$ at another, but the code and the output both mark **$x = 011$**. The code is the correct one.

### Results

| Check | Output |
|---|---|
| H+CX on the 4 basis states | $\vert \Phi^+\rangle, \vert \Psi^+\rangle, \vert \Phi^-\rangle, \vert \Psi^-\rangle$ |
| `ghz_cir_a(5)`, `ghz_cir_b(5)`, `ghz_cir_c(7)` | $\tfrac{\sqrt2}{2}(\vert 0\dots0\rangle + \vert 1\dots1\rangle)$ |
| `w_cir(5)` | $\tfrac{\sqrt5}{5}$ on the 5 one-hot states |
| QHT of $\vert W_3\rangle$ (Qiskit and `qht_func`) | the same result, $\tfrac{\sqrt6}{4}\vert 000\rangle + \dots - \tfrac{\sqrt6}{4}\vert 111\rangle$ |
| $\vert 1\rangle\vert -\rangle$ through CX | $-\vert 1\rangle\vert -\rangle$ (only a global phase) |
| H–CX–H on $\vert 01\rangle$ | $\vert 11\rangle$ |
| $C\bar C S$ with the controls in superposition, target $\vert 1\rangle$ | only $\vert 101\rangle$ gets the coefficient $i/2$ |
| 3-bit AND, $y = 0$ / $y = 1$ | only $\vert 111\rangle$ gives $y = 1$ / $y = 0$ (AND / NAND) |
| 3-bit AND kickback | only $\vert 1110\rangle$ carries the sign $-$ |
| Phase oracle (MCX + $\vert -\rangle$, or CCZ) | only $x = 011$ carries the sign $-$ |

### Quick recap

- Bell = H + CX; GHZ = H + a chain of CX gates; W is harder to build (CRY + CX).
- $H^{\otimes n}|j\rangle = \frac{1}{\sqrt N}\sum_i (-1)^{i\cdot j}|i\rangle$, which you should know by heart for Part 04.
- Phase kickback: control in superposition + target in an eigenvector → the phase is kicked back onto the control.
- Oracle: $U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$; with $y = |-\rangle$ we get $(-1)^{f(x)}|x\rangle$.
- `Gate().control(k, ctrl_state=...)`, `mcx`, `ccz` for building oracles.

---

## Qiskit API summary for this part

| API / function | Used for | Lesson |
|---|---|---|
| `Statevector([...])`, `.from_label('0'/'+'/'-')`, `.from_int(k, dim)` | Creating states | 02_01–02_05 |
| `Statevector(qc)` | The output state of a circuit, starting from $\vert 0\dots0\rangle$ | 02_01–02_05 |
| `sv.draw('latex' / 'bloch', convention='vector', reverse_bits=True)` | Displaying kets, vectors, the Bloch sphere | 02_01–02_05 |
| `sv.evolve(qc or Operator)` | Sending a state through a circuit/matrix | 02_01–02_03, 02_05 |
| `sv.tensor(other)` | Kronecker product of states | 02_02, 02_05 |
| `sv.probabilities([qubits])` | Exact probabilities (whole system or part of it) | 02_03, 02_04 |
| `sv.sample_counts(n)`, `sv.sample_memory(n)` | Simulating measurement | 02_01, 02_03 |
| `sv.measure([qubits])` | Measuring once, returns (outcome, state after measurement) | 02_04 |
| `sv.expectation_value(op)` | Exact expectation value | 02_03 |
| `Operator(qc)`, `Operator.from_label('X'/'0'/'HHH')`, `Operator([[...]])` | Matrix of a circuit/gate | 02_01–02_05 |
| `op.tensor(other)`, `op1 + op2` | Combining matrices | 02_02, 02_04 |
| `QuantumCircuit(n, m)`, `QuantumRegister(n, name=)` | Creating circuits and groups of qubits | 02_01–02_05 |
| `x, h, z, s, sdg, t, tdg, rx, ry, rz, id` | Single-qubit gates | 02_01–02_05 |
| `cx(c, t, ctrl_state=)`, `cz`, `cry`, `ccx`, `rccx`, `ccz`, `mcx`, `swap`, `cswap` | Multi-qubit gates | 02_02–02_05 |
| `SGate().control(k, ctrl_state=)`, `qc.append(gate, qubits)` | Creating and attaching controlled gates | 02_05 |
| `reset`, `measure`, `measure_all`, `barrier` | Preparing, measuring, separating parts of a circuit | 02_01–02_05 |
| `with qc.if_test((clbit, val)):` | Applying a gate depending on a measurement result | 02_03 |
| `qc.save_statevector(label)` | Saving the state in the middle of a circuit (Aer) | 02_03, 02_04 |
| `qc.depth(filter)` | Circuit depth, for example T-depth | 02_04 |
| `transpile(qc, basis_gates=[...])`, `transpile(qc, simulator)` | Translating a circuit into a native gate set | 02_04 |
| `BasicSimulator().run(qc, shots=N)` | A simple simulator built into Qiskit | 02_01, 02_02 |
| `AerSimulator().run(qc, shots=N)`, `.result().get_counts()`, `.get_statevector()`, `.data()` | The Qiskit Aer simulator | 02_03, 02_04 |
| `Estimator(mode=AerSimulator())`, `SparsePauliOp.from_operator` | Estimating expectation values | 02_03 |
| `plot_histogram`, `plot_distribution` | Plotting measurement results | 02_01, 02_04 |

## How to run

Open the notebooks in VS Code or Jupyter, choose the repo's `.venv` kernel, and run from top to bottom. The required libraries are listed
in [requirements.txt](../../requirements.txt).

- Everything runs on local simulators (`Statevector`, `BasicSimulator`, `AerSimulator`).
  `Estimator(mode=AerSimulator())` in 02_03 needs `qiskit-ibm-runtime` installed but **does not need an IBM account**.
- The circuit diagrams and Bloch spheres in the outputs were drawn with the settings in [qiskit_settings.conf](../../qiskit_settings.conf)
  (`circuit_reverse_bits = True`). Without these settings the circuits are drawn with the qubit order upside down, but the computed results are the same.
- Sampled results (counts) change on every run; `Statevector`/`Operator` results do not.
- 02_05 reuses variables across sections (for example, `w_cir` from section 1.3 is reused in section 2), so it must be run in order.

---

<!-- nav -->
[← 01 · Classical computing](../01_classical_computing/README.en.md) · [Contents](../../README.en.md#contents) · [03 · Quantum protocols →](../03_quantum_protocols/README.en.md)
