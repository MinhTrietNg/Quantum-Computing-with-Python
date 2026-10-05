# 03 · Quantum protocols

[Tiếng Việt](README.md) · **English** · [简体中文](README.zh-CN.md)

This part uses the concepts you have already learned (superposition, measurement, entanglement, Bell states) to build three classic quantum protocols: counterfeit-resistant quantum money, teleportation (transferring a quantum state) and superdense coding. Each lesson explains the idea with math and checks it with a Qiskit circuit run on a simulator.

> Source: [03_01](https://learnquantum.io/chapters/03_quantum_protocols/03_01_quantum_money.html), [03_02](https://learnquantum.io/chapters/03_quantum_protocols/03_02_teleportation.html), [03_03](https://learnquantum.io/chapters/03_quantum_protocols/03_03_superdense_coding.html) — Diego Emilio Serrano, learnquantum.io, MIT License.

## Contents

| Lesson | Notebook | Web | Key idea |
|---|---|---|---|
| 03_01 | [03_01_quantum_money.ipynb](03_01_quantum_money.ipynb) | [link](https://learnquantum.io/chapters/03_quantum_protocols/03_01_quantum_money.html) | The uncertainty principle between the bit and sign bases means a quantum coin cannot be copied perfectly; the probability of forgery falls exponentially with the number of qubits |
| 03_02 | [03_02_teleportation.ipynb](03_02_teleportation.ipynb) | [link](https://learnquantum.io/chapters/03_quantum_protocols/03_02_teleportation.html) | 1 Bell pair + 2 classical bits = the full state of 1 qubit can be transferred |
| 03_03 | [03_03_superdense_coding.ipynb](03_03_superdense_coding.ipynb) | [link](https://learnquantum.io/chapters/03_quantum_protocols/03_03_superdense_coding.html) | 1 Bell pair + sending 1 qubit = 2 classical bits transmitted |

The website also lists "Bell Inequalities" (03_04) and "Quantum Key Distribution" (03_05), but in the upstream repo these two chapters contain only a title (no content yet), so they are not copied here.

> The code snippets in this README are **excerpts** from the notebooks: the lines are kept verbatim (including the original English comments from the notebook), omitted parts are marked `...`, and the other comments are additions (written in Vietnamese in the Vietnamese original). The code uses variables defined in earlier cells. To run it, run the whole notebook from top to bottom.

---

## 03_01 · Uncertainty & Quantum Money

**Goal** — Understand the uncertainty principle through two incompatible observables $X$ and $Z$, then use it to build Wiesner's quantum money protocol (the paper "Conjugate Coding", 1983).

### Key concepts

**1. Uncertainty with spin (section 1.1).** With classical magnets, two Stern–Gerlach (SG) apparatuses in series (the $x$ axis, then the $z$ axis) can determine which of the 4 orientations I–IV the magnet has.

<p align="center"><img src="images/03_01_02_barmag_SG.png" width="600" alt="A magnet passes through an SG apparatus along the x axis, then through an SG apparatus along the z axis, and lands in four positions I, II, III, IV on two screens"></p>

*Figure: A classical magnet: the first SG apparatus splits along $\pm x$, the next two SG apparatuses split along $\pm z$, so each orientation I–IV lands in its own place on the screen.*

Electrons are different. The spin can also be tilted in 4 orientations I–IV, where $\theta$ is the angle between the spin and the $+z$ axis:

<p align="center"><img src="images/03_01_04_spin_orientation.png" width="760" alt="An electron spin tilted in four orientations I, II, III, IV in the xz-plane, with the angle theta measured from the z axis"></p>

*Figure: The four spin orientations I–IV in the $xz$-plane; the angle $\theta$ is measured from the $+z$ axis (I: $\pi/4$, II: $3\pi/4$, III: $5\pi/4$, IV: $7\pi/4$).*

<p align="center"><img src="images/03_01_03_spin_SG.png" width="600" alt="An electron passes through an SG apparatus along x and is deflected to +x or -x with probability P(theta), then through an SG apparatus along z and is deflected up or down with probability 1/2"></p>

*Figure: The same experiment with an electron: the first SG apparatus gives $\pm x$ with probability $P_{\pm x}(\theta)$, then the SG apparatus along $z$ gives up or down, $1/2$ each.*

- The SG apparatus along $x$ deflects the particle probabilistically: $P_{+x}(\theta) = \frac{1}{2}(1+\sin\theta)$, $P_{-x}(\theta) = \frac{1}{2}(1-\sin\theta)$. For orientations I and II: $P_{+x} \approx 0.854$, $P_{-x} \approx 0.146$ (the notebook writes $0.853$ because it truncates digits instead of rounding); for orientations III and IV it is the other way round.
- After the measurement along $x$, the spin is projected onto $\pm x$, so the SG apparatus along $z$ always gives up/down with probability $1/2$: the information about the original $z$ direction is "erased".
- Spin along $x$ and spin along $z$ are **incompatible** or **conjugate**: measuring one increases the uncertainty of the other.

**2. Uncertainty with qubits (section 1.2, can be skipped if you only need to understand quantum money).** For a qubit in the $xz$-plane: $|q\rangle = \cos\frac{\theta}{2}|0\rangle + \sin\frac{\theta}{2}|1\rangle$:

$$\langle Z\rangle = \cos\theta,\quad \langle X\rangle = \sin\theta,\quad \Delta O^2 = \langle O^2\rangle - \langle O\rangle^2 \;\Rightarrow\; \Delta Z = |\sin\theta|,\quad \Delta X = |\cos\theta|$$

When $\Delta Z$ is smallest, $\Delta X$ is largest, and vice versa. More generally, with a relative phase $e^{i\varphi}$ and the uncertainty relation $\Delta A\,\Delta B \geq \frac{1}{2}|\langle [A,B]\rangle|$, using $[Z,X] = 2iY$:

$$\Delta Z\,\Delta X \geq |\langle iY\rangle| \quad\Longleftrightarrow\quad |\sin\theta|\sqrt{1-\sin^2\theta\cos^2\varphi} \geq |\sin\theta\sin\varphi|$$

The notebook plots both sides against $\theta$ for a few values of $\varphi$, then verifies the result with the Estimator.

> Note: (1) the sentence "In the above, we only consider qubits in the $xy$-plane" should say the $xz$-plane (the state $\cos\frac{\theta}{2}|0\rangle + \sin\frac{\theta}{2}|1\rangle$ has real amplitudes). (2) After dividing both sides by $|\sin\theta|$, the notebook argues that $\sqrt{1-\sin^2\theta\cos^2\varphi} \geq |\sin\varphi|$ holds because "the maximum value of the left side is 1, which is not smaller than the maximum value of the right side (also 1)". Comparing two maxima does not prove the inequality at each point. The correct argument: since $\sin^2\theta \leq 1$, we have $1-\sin^2\theta\cos^2\varphi \geq 1-\cos^2\varphi = \sin^2\varphi$. (When $\sin\theta = 0$ you cannot divide, but then both sides equal 0.) The notebook's conclusion is still correct.

**3. Quantum money (section 2).**

1. **The bank issues the coins**: each coin has a public serial number $S$ and an $n$-qubit state. Physically, each qubit could be the spin of an electron isolated in the coin; the notebook states clearly that this technology does not exist yet, so this is a theoretical protocol.

   <p align="center"><img src="images/03_01_05_coins.png" width="500" alt="Quantum coins, each carrying a quantum state and a serial number such as 1D062F3ABA"></p>

   *Figure: Each coin carries its own quantum state (numbered $1, 2, \dots, k$) and a public serial number $S_k$, for example `1D062F3ABA`.*

   Each qubit is chosen at random from $\{|0\rangle, |1\rangle, |+\rangle, |-\rangle\}$: start from $|0\rangle$, flip the bit with $X$ and/or change the basis with $H$.

   <p align="center"><img src="images/03_01_07_state_select.png" width="450" alt="Selection tree: from state 0, choose I or X to flip the bit, then choose I or H to change the basis, giving 0, +, 1 or -"></p>

   *Figure: Two choices for each qubit $q_i$: whether to flip the bit ($X$), then whether to change the basis ($H$), giving $|0\rangle$, $|+\rangle$, $|1\rangle$ or $|-\rangle$.*

   Example with $n=6$: $U = II \otimes II \otimes HI \otimes IX \otimes HX \otimes HI$ gives $|0\rangle|0\rangle|+\rangle|1\rangle|-\rangle|+\rangle$.

2. **The bank keeps a secret database**: serial $S$ ↔ the sequence of gates used. (The BBBW protocol proposes generating the state from $S$ with a pseudorandom key generator; the notebook skips this.)
3. **Verification**: the bank applies the inverse circuit $U^\dagger$ and measures; a genuine coin **always** gives the all-zeros string.
4. **A forger** who does not know $U$:
   - Measuring directly in the bit basis: the $|\pm\rangle$ qubits give random results.
   - Measuring in the sign basis (apply $H$ to every qubit first): the $|0\rangle, |1\rangle$ qubits give random results.
   - The forger can measure only once, because measurement collapses the state. The probability of blindly guessing all $n$ qubits **exactly** is $(1/4)^n$; for $n=6$: $\approx 0.000244$.

   But $(1/4)^n$ is not the probability that the forgery succeeds: a qubit whose basis was guessed wrong still passes the verification with probability $1/2$. The forger's goal is to turn 1 genuine coin into **two** coins that both pass verification. The qubits are independent, so the per-qubit probability is multiplied across the $n$ qubits:

   | Strategy (starting from 1 genuine coin) | Per qubit | Both coins pass | $n=6$ |
   |---|---|---|---|
   | Keep the genuine coin, prepare the second coin by blind guessing | $1/2$ | $(1/2)^n$ | $\approx 0.016$ |
   | Measure each qubit in a randomly chosen basis, prepare two copies from the results | $5/8$ | $(5/8)^n$ | $\approx 0.060$ |
   | Optimal cloning ([Molina, Vidick, Watrous 2012](https://arxiv.org/abs/1202.4010)) | $3/4$ | $(3/4)^n$ | $\approx 0.178$ |

   (With measure-then-prepare, *each* coin on its own passes with probability $(3/4)^n$, but both pass together only with $(5/8)^n$.) For every strategy, the probability decreases exponentially as qubits are added, but $n=6$ in the example is still too small to be secure.

5. **Why it is secure**: $\{|+\rangle, |-\rangle\}$ is a basis conjugate to $\{|0\rangle, |1\rangle\}$ (uncertainty), and by the **no-cloning theorem** an unknown quantum state cannot be copied perfectly. The textbook adds: at best the forger can create an *entangled* copy, but when the bank verifies one coin, the other collapses and becomes useless. In fact the other coin is not necessarily rejected: with an entangled copy made with $CX$ (the qubit of the genuine coin as control, the qubit of the new coin in $|0\rangle$ as target), both coins pass together with probability $(5/8)^n$, and an optimal forger reaches $(3/4)^n$ (table above). The protocol also assumes that the forger cannot probe the bank's verification result many times.

The lesson ends by mentioning "virtual quantum money" and quantum lightning (Zhandry18) as ways to combine it with blockchain.

> Note: in section 2, the notebook has one slip and two overstatements: (1) the sentence "the probability of the criminal successfully guessing the state grows with the number of qubits" actually *decreases* with $n$, as the formula $(1/4)^n$ says; (2) $(1/4)^n$ is the probability of guessing the whole state **exactly**, not the probability that the forgery succeeds: a blindly guessed fake coin still passes the verification with probability $(1/2)^n$, and an optimal forger gets two coins that both pass with probability $(3/4)^n \approx 0.178$ for $n=6$ (table in point 4); (3) the sentence "the second coin's state will collapse making it unusable" is not entirely correct (see point 5).

### Key code

```python
# Use the Paramater class to define arbitrary angles of θ and φ
θ = Parameter('θ')
φ = Parameter('φ')

# Circuit to prepare state cos(θ/2)|0⟩+exp(iφ)sin(θ/2)|1⟩
qc = QuantumCircuit(1)
qc.ry(θ,0)
qc.p(φ,0)
```

A parameterized circuit (`qiskit.circuit.Parameter`): `ry(θ)` sets the amplitudes, `p(φ)` adds the relative phase. Concrete values are assigned when the Estimator runs.

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

`qiskit_ibm_runtime.Estimator` (V2 style) runs on `AerSimulator`. One PUB `(circuit, observables, parameter_values, precision)`: 3 observables of type `SparsePauliOp` × 21 values of $\theta$ (with $\varphi = 9\pi/10$ fixed), precision 0.01; `.data.evs` returns an array of expectation values. The notebook notes that the coefficient of $Y$ should really be $i$, but since only the absolute value is taken, it uses 1.

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

The "bank" function: it chooses a random state for each qubit, then applies $X$ and/or $H$ (`qc.id` is only a placeholder). The function also returns a LaTeX string of the state for display with `IPython.display.Math` (this part is omitted from the excerpt). The loop goes from qubit $n-1$ down to 0, so that string writes the highest qubit on the left, matching Qiskit's little-endian order.

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

Verifying the coin: `QuantumCircuit.inverse()` builds $U^\dagger$, `Statevector.evolve` applies the circuit to a statevector, and `probabilities_dict` and `plot_distribution` display the distribution. The forger is simulated with `sv_coin.probabilities_dict()` (measuring in the bit basis) and `sv_coin.evolve(qc_h)` with `qc_h.h(range(n))` (measuring in the sign basis).

### Results

- Uncertainty plot (4 values of $\varphi$): the $\Delta Z\Delta X$ curve always lies above or touches the $|\langle iY\rangle|$ curve. Estimator plot ($\varphi = 9\pi/10 \approx 2.8274$): the 21 points of each quantity lie close to the theoretical curve.
- The saved run generated an $n=6$ coin: $|+\rangle \otimes |1\rangle \otimes |0\rangle \otimes |0\rangle \otimes |1\rangle \otimes |0\rangle$ (from $q_5$ to $q_0$; the circuit has only $H$ on $q_5$, and $X$ on $q_4$ and $q_1$).
- Verification with $U^\dagger$: the distribution contains only `000000`, with probability 1.0.
- The forger measuring in the bit basis: two outcomes `010010` and `110010`, 0.5 each. Measuring in the sign basis: 32 outcomes, each $\approx 0.031$ ($1/32$), with the leftmost bit always 0. In this run only 1 of the 6 qubits is in the sign basis (the notebook says "roughly half" for the average case), so the first distribution is narrow and the second is wide.

### Quick recap

- $X$ and $Z$ are a conjugate pair of observables: $\Delta Z = |\sin\theta|$, $\Delta X = |\cos\theta|$; they cannot both be small.
- A coin = a public serial number + $n$ random qubits in $\{|0\rangle,|1\rangle,|+\rangle,|-\rangle\}$; only the bank knows the bases (it must keep a secret list). This is a theoretical protocol; the technology to build it does not exist yet.
- Verification = apply $U^\dagger$ and then measure; a genuine coin gives all zeros.
- Two layers of protection: measurement destroys the state (uncertainty), and no-cloning. Guessing exactly right: $(1/4)^n$; getting two coins that both pass the verification: from $(1/2)^n$ (blind guess) to $(3/4)^n$ (optimal), all decreasing exponentially.
- Estimator V2: `estimator.run([(qc, observables, params, precision)])`, then read `result()[0].data.evs`.

---

## 03_02 · Quantum Teleportation

**Goal** — Send the *entire* state of an arbitrary qubit from Alice to Bob using only **2 classical bits**, provided the two of them have already shared an entangled pair of qubits beforehand (Bennett et al., 1993).

### Key concepts

**Comparison with the classical approach.** For Bob to create $|q\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\varphi}\sin\frac{\theta}{2}|1\rangle$, Alice has to send two angles $(\theta,\varphi)$, for example in FP16 format (16 bits per angle), and Bob still gets only an approximate value.

<p align="center"><img src="images/03_02_01_classical_transmit.png" width="760" alt="Alice sends two rounded angles as bit strings over a classical channel; Bob uses them in Ry and P gates to create an approximate state"></p>

*Figure: The classical approach: Alice sends the two rounded angles $(\tilde\theta, \tilde\varphi)$ as bit strings over a classical channel; Bob uses them in the $R_y$ and $P$ gates to create the approximate state $|\tilde q\rangle$.*

Teleportation needs to send only 2 classical bits (plus an entangled pair shared beforehand), and Bob receives exactly the state Alice has, not an approximation. The trade-off is that Bob only has a *qubit* in the state $|q\rangle$; he cannot read out the two angles $(\theta,\varphi)$: measuring one qubit gives only 1 bit.

> Note: in the notebook's FP16 example, the two bit strings are swapped. `0011101001001000` is $\pi/4 \approx 0.785$ and `0011111001001000` is $\pi/2 \approx 1.570$, so for $(\theta,\varphi) = (\pi/2, \pi/4)$ one must send `(0011111001001000, 0011101001001000)`. The pair of approximate values $(1.570, 0.785)$ in the notebook is correct.

To teleport, Alice and Bob must first share an entangled pair: Alice creates a Bell pair and then sends one qubit to Bob over a quantum channel. After that, only a classical channel is needed.

<p align="center"><img src="images/03_02_02_quantum_transmit.png" width="675" alt="Alice and Bob are connected by a quantum channel, used to send one entangled qubit, and by a classical channel"></p>

*Figure: The two channels between Alice and Bob: the quantum channel (used to send one qubit of the entangled pair in advance) and the classical channel (used to send the 2 bits of measurement results).*

**The steps (following the notebook's circuit diagram):**

<p align="center"><img src="images/03_02_03_teleportation_circuit.png" width="760" alt="Teleportation circuit diagram: Alice creates a Bell pair, sends one qubit to Bob, prepares q with Ry and P, applies CX and H, and measures two qubits; Bob applies X and Z according to the two bits received over the classical channel; markers psi 1 to psi 5"></p>

*Figure: The teleportation circuit, with time running to the right and distance running vertically. The measurement result of the middle qubit (Alice's half of the Bell pair) controls $X$, the measurement result of the top qubit ($|q\rangle$) controls $Z$; the dashed lines mark $|\psi\rangle_1$ to $|\psi\rangle_5$.*

0. Alice initializes 3 qubits $|000\rangle_A$.
1. Alice creates the Bell state $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ on two qubits and then sends one qubit to Bob:
   $|\psi\rangle_1 = \frac{1}{\sqrt{2}}|0\rangle_A(|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B)$.
2. When needed, Alice prepares the state she wants to send, $|q\rangle = \alpha|0\rangle + \beta|1\rangle$ (with rotation gates, where $\alpha = \cos\frac{\theta}{2}$, $\beta = e^{i\varphi}\sin\frac{\theta}{2}$). Rewrite the whole system in terms of the 4 Bell states of Alice's two qubits:

$$|\psi\rangle_2 = \tfrac{1}{2}\Big[|\Phi^+\rangle_A(\alpha|0\rangle+\beta|1\rangle)_B + |\Psi^+\rangle_A(\alpha|1\rangle+\beta|0\rangle)_B + |\Phi^-\rangle_A(\alpha|0\rangle-\beta|1\rangle)_B + |\Psi^-\rangle_A(\alpha|1\rangle-\beta|0\rangle)_B\Big]$$

   If Alice measures her two qubits in the Bell basis, Bob's qubit will be in one of 4 variants of $|q\rangle$, differing only by a bit flip, a phase flip, or both. This is just the same state written in a different basis: before Bob receives the 2 bits, the state of Bob's qubit on its own (the reduced density matrix) is always $I/2$, regardless of $|q\rangle$. (The notebook briefly discusses the controversial "nonlocal" character of this description and other interpretations, then works in the standard formalism.)
3. Alice applies $CX$ and then $H$ to change from the Bell basis to the computational basis:

$$|\psi\rangle_3 = \tfrac{1}{2}\Big[|00\rangle(\alpha|0\rangle+\beta|1\rangle) + |01\rangle(\alpha|1\rangle+\beta|0\rangle) + |10\rangle(\alpha|0\rangle-\beta|1\rangle) + |11\rangle(\alpha|1\rangle-\beta|0\rangle)\Big]$$

4. Alice measures the two qubits: each outcome `00`, `01`, `10`, `11` (the first bit $j$ from the qubit $|q\rangle$, the second bit $i$ from the half of the Bell pair) has probability $1/4$ and leaves Bob with the corresponding state above.
5. Alice sends the 2 bits $(j,i)$ to Bob over the classical channel. Bob corrects the state: $|\psi\rangle_5 = Z^j X^i|\psi\rangle_4 = \alpha|0\rangle + \beta|1\rangle = |q\rangle$ (with $X^0 = Z^0 = I$).

**Why it is not faster than light:** Bob does not know what correction to apply until he receives the 2 classical bits. Before that, even if Alice has already measured, as far as Bob knows his qubit is still in the state $I/2$ (an even mixture of the 4 possibilities, each with probability $1/4$), so Bob has no information yet; the 2 bits travel over the classical channel, no faster than light. The protocol transfers only the *state*, not matter or energy; Alice's original qubit is measured and so loses the state $|q\rangle$, consistent with no-cloning. **Why the Bell pair is worth it:** it is set up *beforehand*, so when $|q\rangle$ is ready, only 2 bits need to be sent.

**Multiple qubits (section 2.2):** each qubit to be sent uses its own Bell pair and its own pair of bits. The notebook's example sends $|q\rangle = \frac{1}{\sqrt{3}}(|001\rangle - |010\rangle + |100\rangle)$ using 3 Bell pairs (6 qubits for Alice, 3 for Bob).

### Key code

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
qc.measure(qra,cra)                # cra[0] <- qra[0] (half of the Bell pair), cra[1] <- qra[1] (|q⟩)
```

This uses named `QuantumRegister`/`ClassicalRegister` objects to keep Alice's and Bob's qubits apart. Because `qrb` is passed first, qubit 0 is Bob's; `qra[0]` is Alice's half of the Bell pair, and `qra[1]` holds the state to be sent.

```python
# Bob applies X, Z gates conditioned on Alice's results
with qc.if_test((cra[0], 1)): qc.x(0)
with qc.if_test((cra[1], 1)): qc.z(0)

qc.save_statevector('ψout')
```

Dynamic classical control with `QuantumCircuit.if_test` (the modern API, replacing the deprecated `c_if`): apply $X$ if the bit `cra[0]` (the result of measuring the half of the Bell pair, i.e. bit $i$) equals 1, and apply $Z$ if `cra[1]` (the result of measuring the qubit $|q\rangle$, i.e. bit $j$) equals 1. `save_statevector` is a Qiskit Aer instruction that saves the statevector at the end of the circuit.

```python
result = simulator.run(qc, shots=1, memory=True).result()
alices_bits = result.get_memory()[0]
ψout = result.data().get('ψout')

ρout = partial_trace(ψout,[1,2])
bobs_state = DensityMatrix(np.round(ρout, 8)).to_statevector()
```

This runs 1 shot on `AerSimulator` with `memory=True` to get the bit string Alice measured. `partial_trace` removes qubits 1 and 2 (Alice's), leaving Bob's density matrix. Because that state is pure, `DensityMatrix(...).to_statevector()` can convert it back to a statevector; `np.round` removes numerical error.

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

The multi-qubit version: `h`/`cx` accept lists of qubits to create 3 Bell pairs at once; the 3-qubit state is prepared on `qra[3..5]` with `x`, `cry`, `cx`, `z`; Bob corrects each qubit with the bit pair `(cra[i], cra[i+3])`. In the simulation, `partial_trace(ψout, [3..8])` keeps Bob's 3 qubits.

> Note: the comments in the multi-qubit cell do not match the code: "two entangled Bell states" (it actually creates 3 pairs) and "Alice prepares state |w⟩ = 1/2|01⟩ - √3/2|10⟩" (the circuit actually prepares $\frac{1}{\sqrt{3}}(|001\rangle - |010\rangle + |100\rangle)$, as the output shows). In addition, in the 1-qubit example, the print line `(j,i) = ({alices_bits[1]},{alices_bits[0]})` has its labels swapped: Qiskit's memory string writes the high bit first (a test run with only `cra[0] = 1` gives the string `01`), so `alices_bits[0]` is `cra[1]` (bit $j$) and `alices_bits[1]` is `cra[0]` (bit $i$, which controls $X$). The print line actually prints $(i,j)$; the string `alices_bits` itself already has the correct order $ji$. This does not affect Bob's final state.

### Results

- **1 qubit**, 5 runs: Alice measured (according to the printed labels) `(0,1)`, `(0,0)`, `(1,1)`, `(0,1)`, `(0,0)`, so the true $(j,i)$ are $(1,0)$, $(0,0)$, $(1,1)$, $(1,0)$, $(0,0)$ (see the Note above). Each time, Bob received $\frac{\sqrt{2}}{2}|0\rangle - \frac{\sqrt{2}\,i}{2}|1\rangle$, exactly the $|q\rangle$ that Alice prepared.
- **3 qubits**, 5 runs: Alice measured `011100`, `111100`, `011001`, `001110`, `100001`. Each time, Bob received $\frac{\sqrt{3}}{3}|001\rangle - \frac{\sqrt{3}}{3}|010\rangle + \frac{\sqrt{3}}{3}|100\rangle$.

### Quick recap

- Resources: 1 shared Bell pair + 2 classical bits → the state of 1 qubit can be transferred (the Bell pair is used up, and Alice's original qubit loses the state $|q\rangle$).
- Alice's circuit: $CX$ (qubit $|q\rangle$ as the control) → $H$ on the qubit $|q\rangle$ → measure the 2 qubits.
- Bob corrects with $Z^j X^i$; $X$ according to the bit of the qubit from the Bell pair, $Z$ according to the bit of the $|q\rangle$ qubit.
- Alice's measurement results are random (each $1/4$), but Bob's final state is always $|q\rangle$.
- Qiskit: `if_test` for classical control, `save_statevector` + `partial_trace` to see Bob's state.

---

## 03_03 · Superdense Coding

**Goal** — Send **2 classical bits** by transmitting **1 qubit**, thanks to a Bell pair shared in advance. This is the "reverse direction" of teleportation (Bennett and Wiesner; published in 1992).

### Key concepts

Unlike teleportation, no classical channel is needed, but the quantum channel must carry one more qubit. Counting the qubit used to share the Bell pair, 2 qubits still have to be sent for 2 bits; the advantage is that the first qubit is sent in advance, before there is any message. Without a shared entangled pair, 1 qubit can carry at most 1 classical bit (Holevo's theorem; the notebook does not mention it).

<p align="center"><img src="images/03_03_01_superdense_transmit.png" width="675" alt="Alice sends Bob two qubits over a quantum channel: q0 is the entangled qubit, q1 is the encoding qubit; there is no classical channel"></p>

*Figure: Only a quantum channel: $q_0$ is the entangled qubit, $q_1$ is the qubit that carries the 2 encoded bits; there is no classical channel.*

<p align="center"><img src="images/03_03_02_superdense_circuit.png" width="760" alt="Superdense coding circuit: Alice creates a Bell pair with H and CX and sends one qubit to Bob; Alice applies X according to bit i and Z according to bit j and then sends her qubit; Bob applies CX and H and measures both qubits; markers psi 1 to psi 3"></p>

*Figure: The superdense coding circuit: Alice applies $X$ according to bit $i$ and $Z$ according to bit $j$ to her qubit and then sends it over the quantum channel; Bob applies $CX$ (the qubit he just received as the control), then $H$, and then measures; the dashed lines mark $|\psi\rangle_1$ to $|\psi\rangle_3$.*

0. Alice initializes $|00\rangle_A$.
1. Alice creates $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B)$ and sends one qubit to Bob.
2. Alice encodes the 2 bits $(j,i)$ on her qubit: apply $X$ if $i=1$, then $Z$ if $j=1$:
   $|\psi\rangle_2 = (Z^j \otimes I)(X^i \otimes I)|\psi\rangle_1$. The result is one of the 4 Bell states:

| $(j,i)$ | Gate Alice applies | $\vert\psi\rangle_2$ | Bob measures (after step 3) |
|---|---|---|---|
| (0,0) | $I$ | $\vert\Phi^+\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle + \vert 11\rangle)$ | `00` |
| (0,1) | $X$ | $\vert\Psi^+\rangle = \frac{1}{\sqrt{2}}(\vert 10\rangle + \vert 01\rangle)$ | `01` |
| (1,0) | $Z$ | $\vert\Phi^-\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle - \vert 11\rangle)$ | `10` |
| (1,1) | $ZX$ | $\vert\Psi^-\rangle$ (the notebook writes $\frac{-1}{\sqrt{2}}(\vert 10\rangle - \vert 01\rangle)$) | `11` |

   (In the kets, Alice's qubit is written first and Bob's second. The string Bob measures also follows this order, matching Qiskit's `memory` string in the code, because `cr[1]` takes its value from Alice's qubit.)
3. Alice sends her qubit to Bob. Bob applies $CX$ (the qubit received from Alice as the control, Bob's qubit as the target) and then $H$ on the qubit received from Alice: $|\psi\rangle_3 = (H\otimes I)\,CX\,|\psi\rangle_2$, which maps the 4 Bell states to $|00\rangle, |01\rangle, |10\rangle, |11\rangle$. Bob measures and obtains exactly $(j,i)$ with probability 100%.

**Why it works:** the 4 Bell states are orthogonal to each other, so they can be told apart perfectly by one measurement in the Bell basis. Alice only needs to act locally on her own qubit to choose 1 of those 4 states.

**Extension:** with $n$ Bell pairs, Alice can send $2n$ bits (the notebook uses $n=3$, i.e. 6 bits).

> Note: the final results table (after step 3) in the notebook is still labeled $|\psi\rangle_2$; it should be $|\psi\rangle_3$.

### Key code

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
if alice_bits[1] == 1: qc.x(1)       # alice_bits[1] is bit i
if alice_bits[0] == 1: qc.z(1)       # alice_bits[0] is bit j
qc.barrier()

# Bob changes from Bell to Computational basis
qc.cx(qr[1],qr[0])
qc.h(qr[1])
qc.barrier()

# Bob measures all qubits
qc.measure(qr,cr)
```

Qubit 1 (`qr[1]`) is Alice's and qubit 0 is Bob's. The encoding gates are added with a Python `if` when the circuit is *built* (not classical control inside the circuit like `if_test`), because Alice knows her bits in advance.

```python
# run simulation
simulator = AerSimulator()
qc_t = transpile(qc, simulator)

bob_bits = simulator.run(qc_t, shots=1, memory=True).result().get_memory()[0]
```

`transpile` compiles the circuit for the backend, then 1 shot is run and the bit string Bob measured is read with `get_memory()`.

```python
for qbit, bit_pair in enumerate(reversed(alice_bit_pairs)):
    if bit_pair[1] == 1: qc.x(qr_encode[qbit])
    if bit_pair[0] == 1: qc.z(qr_encode[qbit])
...
for qbit in range(n):
    qc.measure(qr_entangle[qbit],cr[2*qbit])
    qc.measure(qr_encode[qbit],cr[2*qbit+1])
```

The $n$-pair version: two registers `entangle`/`encode`, with each pair of bits encoded on one `encode` qubit. The `reversed` order together with the way the classical bits are assigned makes the string Bob reads have the same order as Alice's string (Qiskit prints the high bit first).

### Results

- 1 pair: `Alice enconded bits (1,1)`, `Bob recovered bits (1,1)` (the saved circuit has both $X$ and $Z$). The two print lines use the order `(alice_bits[1], alice_bits[0])` and `(bob_bits[1], bob_bits[0])`, i.e. $(i,j)$, the reverse of the $(j,i)$ convention above; both sides print in the same order, so they can still be compared, and for `(1,1)` it makes no difference.
- 3 pairs: `Alice encoded bits 000100`, `Bob recovered bits 000100` (the saved circuit has only one $X$ gate, on `encode[1]`).

The bits are chosen at random, so each run differs, but Bob's bits always match Alice's.

### Quick recap

- Resources: 1 shared Bell pair + sending 1 qubit → 2 bits transmitted.
- Alice encodes: $X^i$ and then $Z^j$ on her qubit, producing 1 of the 4 Bell states.
- Bob decodes: $CX$ → $H$ → measure, which is exactly the "Bell → computational basis" circuit, the same as Alice's step in teleportation.
- Teleportation and superdense coding are dual: teleportation sends 2 classical bits to transfer the state of 1 qubit; superdense coding sends 1 qubit to transfer 2 classical bits. Both need an entangled pair shared in advance.

---

## Qiskit API summary for this part

| API / function | Used for | Lesson |
|---|---|---|
| `QuantumCircuit`, `.h`, `.x`, `.z`, `.id`, `.cx`, `.ry`, `.p`, `.cry` | Building circuits, one- and two-qubit gates | 03_01, 03_02, 03_03 |
| `QuantumRegister`, `ClassicalRegister` | Named registers (Alice/Bob) | 03_02, 03_03 |
| `qiskit.circuit.Parameter` | Parameterized circuit with $\theta$, $\varphi$ | 03_01 |
| `SparsePauliOp` | Defining the observables $Z$, $X$, $Y$ | 03_01 |
| `qiskit_ibm_runtime.Estimator(mode=AerSimulator())` | Computing expectation values (V2 primitive, PUBs with precision) | 03_01 |
| `Statevector`, `.evolve`, `.probabilities_dict` | Statevector simulation and measurement probabilities | 03_01 |
| `QuantumCircuit.inverse()` | Inverse circuit $U^\dagger$ for verifying the coin | 03_01 |
| `plot_distribution` | Plotting a probability distribution | 03_01 |
| `.measure`, `.barrier` | Measuring, separating the steps in the drawing | 03_02, 03_03 |
| `QuantumCircuit.if_test` | Applying gates according to the value of a classical bit (dynamic circuit) | 03_02 |
| `.save_statevector` (Aer) | Saving the statevector inside the simulation | 03_02 |
| `AerSimulator().run(..., shots=1, memory=True)`, `get_memory()` | Running one shot and getting the bit string | 03_02, 03_03 |
| `partial_trace`, `DensityMatrix.to_statevector()` | Extracting Bob's state on its own | 03_02 |
| `transpile` | Compiling the circuit for the simulator | 03_03 |
| `qc.draw(cregbundle=False, fold=-1, idle_wires=True)` | Drawing the circuit | 03_01, 03_02, 03_03 |

## How to run

- Open the notebooks with Jupyter or VS Code, choose the repo's `.venv` kernel, and run from top to bottom.
- The required libraries are listed in [`requirements.txt`](../../requirements.txt) (install from the repo root: `pip install -r requirements.txt`).
- Everything runs on a local simulator (`AerSimulator`, `Statevector`). `qiskit_ibm_runtime.Estimator(mode=AerSimulator())` in Lesson 03_01 needs the `qiskit-ibm-runtime` package installed but does not need an IBM account.
- The lessons use random numbers (the coin, Alice's bits, the measurement results), so the output differs from the saved one on every run, but the conclusions stay the same.

---

<!-- nav -->
[← 02 · Quantum computing](../02_quantum_computing/README.en.md) · [Contents](../../README.en.md#contents) · [04 · Quantum algorithms →](../04_quantum_algorithms/README.en.md)
