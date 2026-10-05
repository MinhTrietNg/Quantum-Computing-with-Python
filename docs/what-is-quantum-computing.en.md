# What is a quantum computer?

[Tiếng Việt](what-is-quantum-computing.md) · **English** · [简体中文](what-is-quantum-computing.zh-CN.md)

*About a 15-minute read. No quantum physics needed; basic Python is enough if you want to run the code.
How to run: [Google Colab or on your own computer](setup.en.md).*

## An honest answer

A quantum computer is a computer that stores and processes information using the phenomena of quantum mechanics.
It is **not** a faster laptop, and it does **not** "try every answer at once". It is a different kind of tool.
In theory it is good at some very specific kinds of problems (many of them need machines much larger and with far fewer errors than today's machines),
and it does not help with most of what you do on a computer every day.

The rest of this page explains what this means.

## From bits to qubits

An ordinary computer stores information in **bits**: each bit is `0` or `1`.

A quantum computer uses **qubits**. The state of one qubit is described by two numbers called **amplitudes**,
$\alpha$ and $\beta$:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1$$

How to read the notation:

- $|0\rangle$ is read "ket 0". It is just the **name** of the state "the qubit is 0"; $|1\rangle$ is similar.
- $\alpha$ and $\beta$ are the two amplitudes. Unlike probabilities, they can be **negative**, and they can even be *complex numbers*
  (numbers with an imaginary part). At first, just think of them as numbers that may be negative.
- $|\alpha|^2$ is the squared magnitude of $\alpha$; for a real number, it is simply $\alpha^2$.
- The condition on the right says: the two probabilities add up to 100%.

When you **measure**, you always get an ordinary bit: `0` with probability $|\alpha|^2$, `1` with probability $|\beta|^2$.
After the measurement, the qubit "locks in" to that result. A measurement does not show you $\alpha$ and $\beta$.

Two things make a qubit different from an ordinary "probabilistic" bit (like a coin whose face you have not seen yet):

1. Amplitudes can be **negative or complex**, not only positive numbers like probabilities.
2. Amplitudes can **cancel out or add up** with each other. This is called *interference*, and together with entanglement it is the key
   to the power of quantum computers (see below).

## Three ideas to remember

| Idea | In plain words | Learn it in depth in |
|---|---|---|
| **Superposition** | A qubit is in **one definite state**, described by two amplitudes $\alpha, \beta$ as above. Superposition (with respect to $\vert 0\rangle, \vert 1\rangle$) means that **both amplitudes are nonzero**, for example $\alpha = \beta = 1/\sqrt2$; $\vert 0\rangle$ has $\alpha = 1, \beta = 0$, so it is not a superposition. It does **not** mean "both 0 and 1 at once"; that is only a shorthand that is easy to misunderstand | [02_01](../chapters/02_quantum_computing/README.en.md#02_01--qubits-and-quantum-circuits) |
| **Entanglement** | Two qubits tied together so closely that you cannot describe each qubit on its own; when you measure in several different directions, their results are correlated in a way that no "pre-matched pair of coins" can reproduce | [02_02](../chapters/02_quantum_computing/README.en.md#02_02--quantum-entanglement) |
| **Interference** | Amplitudes add up or cancel each other out. Quantum algorithms are designed so that the wrong answers cancel out and the right answer is amplified | [Part 04](../chapters/04_quantum_algorithms/README.en.md) |

## Your first quantum program

We use Qiskit, an open-source Python library, to simulate a quantum computer right on your own machine.
`shots=1000` means the circuit is run and measured 1000 times; the result is a table counting how many times each answer appeared.
Because measurement is random, **your numbers will differ slightly from the numbers in this guide**.

Two words to know first: a **gate** is a transformation applied to a qubit (like `h` and `cx` below), and a **circuit**
is a sequence of gates followed by a measurement. The section [Reading a quantum circuit](#reading-a-quantum-circuit) explains how to read the drawing.

### A one-qubit coin flip

The **Hadamard** gate (H gate) turns $|0\rangle$ into $\tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$, that is, two equal amplitudes,
each with a 50% probability.

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)             # Hadamard gate
qc.measure_all()    # measure

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'1': 497, '0': 503}      # example; every run gives different numbers but always close to 50/50
```

### Interference: flip twice and the result is certain

Add **one more H gate** right after the first one:

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)
qc.h(0)             # second H gate
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'0': 1000}
```

If a qubit were only a "random coin", flipping it once more would still give a random result. But the result is **always `0`**.
Work it out yourself. The H gate transforms the two basis states as follows (note the **minus sign**):

$$H|0\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big), \qquad H|1\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)$$

Apply H a second time to $\tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$, that is, apply it to each part and add the results:

$$\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big) + \tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)
= \tfrac12\big(|0\rangle + |1\rangle\big) + \tfrac12\big(|0\rangle - |1\rangle\big) = |0\rangle$$

The amplitude of $|1\rangle$ receives two contributions, $+\tfrac12$ and $-\tfrac12$, so it **cancels out**. The amplitude of $|0\rangle$ receives
$+\tfrac12$ and $+\tfrac12$, so it **adds up** to 1. Probability cannot explain this, because probabilities are never
negative. Amplitudes can be.

This is the core idea: **a quantum algorithm arranges for the paths leading to wrong answers to cancel each other out.**

### Entanglement: two qubits that always agree

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)         # qubit 0: equal amplitudes for 0 and 1
qc.cx(0, 1)     # CX gate: flip qubit 1 if qubit 0 is 1  -> the two qubits are entangled
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'11': 496, '00': 504}      # example; the exact numbers differ on every run
```

The circuit looks like this (read from left to right): the `H` box is the Hadamard gate; the dot `■` joined to the `X` box is the CX gate (the dot is on the
control qubit, the `X` box is on the target qubit); `M` is a measurement; `░` is a *barrier* (a separator line) that `measure_all()` inserts automatically and that does not change the state.

```text
        ┌───┐      ░ ┌─┐   
   q_0: ┤ H ├──■───░─┤M├───
        └───┘┌─┴─┐ ░ └╥┘┌─┐
   q_1: ─────┤ X ├─░──╫─┤M├
             └───┘ ░  ║ └╥┘
meas: 2/══════════════╩══╩═
                      0  1 
```

The result is only `00` or `11`, **never** `01` or `10` (on a real machine, noise sometimes lets a few `01`/`10` results slip through; the ideal simulator does not).
Each qubit on its own is random 50/50, but the two qubits always match.

**This alone is not enough to call it quantum.** Two coins put in two envelopes, matched up in advance,
also give exactly the same results. The real difference only shows when you measure in **several different directions**: then the correlations
are stronger than any "pre-arranged" scheme can produce (that is the content of the *Bell inequality*, for example the CHSH game). You will see that
this state cannot be written as "two independent qubits" in [02_02](../chapters/02_quantum_computing/README.en.md#02_02--quantum-entanglement).
The Bell inequalities chapter of the original textbook has no content yet; the IBM course in [Resources](resources.en.md) covers this.

The state above is called a *Bell state*, and it is the foundation for
[teleportation](../chapters/03_quantum_protocols/README.en.md#03_02--quantum-teleportation)
and superdense coding.

## Reading a quantum circuit

A quantum circuit is read from **left to right** in time. Each horizontal line is a qubit, each box is a gate
(a transformation), and the meter symbol is a measurement. A double line is a classical bit carrying the measurement result.

For example, this is the teleportation circuit: Alice sends the state of one qubit to Bob, using a pair of
entangled qubits and **two classical bits**.

![Teleportation circuit: Alice creates an entangled pair with an H gate and a CX gate, then sends one qubit to Bob through a quantum channel; Alice prepares the state to be sent, applies CX and H, and measures her two qubits; the two result bits travel through a classical channel so that Bob can apply an X gate and a Z gate](../chapters/03_quantum_protocols/images/03_02_03_teleportation_circuit.png)

*Figure: Diego Emilio Serrano, [learnquantum.io](https://learnquantum.io), MIT License.*

You do not need to understand it all right away. After [Part 03](../chapters/03_quantum_protocols/README.en.md) you will be able to read this circuit.

## What quantum computers are and are not good at

### What is known

> This table is a bit heavy. It is fine to skip it on a first read; look up any unfamiliar term in the
> [glossary](glossary.en.md).

| Problem | Speedup | Honest notes |
|---|---|---|
| **Integer factoring** (Shor's algorithm) | From *super-polynomial* (growing faster than any polynomial function of the number of digits) down to polynomial | Nobody knows a polynomial-time classical algorithm, but nobody has proven that none exists either. It needs a large error-corrected machine, which does not exist yet (as of October 2026). **Note:** nobody has proven that this problem is *NP-complete* (one of the "hardest" problems in the class NP, like the logic-formula satisfiability problem SAT), and it most likely is not; researchers also do not believe that quantum computers can solve NP-complete problems in polynomial time |
| **Unstructured search** ([Grover](../chapters/04_quantum_algorithms/README.en.md#04_04--grovers-algorithm)) | Square root: $N \to \sqrt N$ | Proven optimal **in the black-box model** (you may only query the oracle); for problems with structure, that does not rule out a faster method. With $N = 2^{20} \approx 10^6$ items and 1 item to find: classically you need on average about $N/2 \approx 524$ thousand queries, while Grover needs about 800 iterations, each one calling the oracle once. A quadratic speedup is modest: the cost of the oracle and of error correction can erase the advantage at realistic scales |
| **Simulating quantum systems** (chemistry, materials) | Very promising | The original idea of the physicist Richard Feynman. Still a research direction, being tried out on real machines |
| Machine learning, optimization | **Unclear** | Many claims, little solid evidence. Be wary of marketing claims |

The four algorithms in [Part 04](../chapters/04_quantum_algorithms/README.en.md) (Deutsch–Jozsa, Bernstein–Vazirani,
Simon, Grover) are **examples for learning**. The first three solve artificial problems with no practical application:

- *Deutsch–Jozsa* is only faster than a classical algorithm that is **guaranteed to be correct**; a randomized classical algorithm with a small
  error probability also needs only a few queries.
- *Bernstein–Vazirani* gives only a small gap ($n$ queries down to 1).
- *Simon* is the first example of an **exponential** advantage even when compared with a randomized classical algorithm, but it is still
  in the oracle model.

They teach the techniques (oracle, phase kickback, interference) that algorithms such as Shor's reuse.

### What quantum computers do not do

- They do **not** replace a laptop or a phone. For everyday tasks (web, documents, games), they are slower and more expensive.
- They do **not** "try every answer at once and then pick the right one". A measurement gives only one result, so interference
  has to be designed so that the right answer has a high probability. For most problems, nobody knows how to do that.
- They do **not** send information faster than light. Entanglement creates correlations, not a communication channel; teleportation
  still needs ordinary classical bits to be sent (see [03_02](../chapters/03_quantum_protocols/README.en.md#03_02--quantum-teleportation)).
- They **cannot** copy an unknown quantum state (the *no-cloning* theorem,
  [02_04](../chapters/02_quantum_computing/README.en.md#02_04--multi-qubit-systems)).

## Why they are hard to build

Qubits are very easily disrupted by the environment (heat, vibration, electromagnetic noise) and by the imprecision of the control equipment.
These disturbances are collectively called *noise*: it includes *decoherence*, errors in individual gates, and errors when reading out the result.
Today's machines are still in the **NISQ** era (noisy intermediate-scale quantum, a term introduced by the physicist John Preskill
in late 2017 and popularized by a 2018 paper): they have many qubits but are noisy, and are not yet good enough to run large algorithms such as Shor's.

The way forward is **quantum error correction**: using many physical qubits to build one reliable "logical" qubit.
The number of physical qubits needed per logical qubit is estimated at anywhere from tens to thousands, depending on the error-correcting code and the amount of noise.
Technologies being pursued include superconducting circuits, trapped ions, neutral atoms, photons, and many other approaches.

> This field changes quickly. All the statements about hardware above are correct to the best of our knowledge as of October 2026;
> check recent sources before quoting specific figures.

## Why not simply simulate it on an ordinary computer?

Fully describing the state of $n$ qubits takes $2^n$ amplitudes. Each time you add a qubit, the memory doubles:

| Number of qubits | Number of amplitudes | Memory (16-byte complex numbers) |
|---|---|---|
| 10 | 1,024 | 16 KiB |
| 30 | about $10^9$ | 16 GiB |
| 50 | about $10^{15}$ | 16 PiB |

Thirty qubits already fit on a powerful computer (the 16 GiB figure is for the vector alone; in practice a bit more is needed to do the calculation), while fifty goes far beyond any single machine. This is why full simulation
does not scale, and also why you can **learn everything in this repo on a laptop**:
the examples use at most 14 qubits (the Simon lesson), which is only about 256 KiB for the statevector.

(There are clever simulation techniques for circuits with a special structure, so the table above is the cost
of the "brute-force" way of simulating, not an absolute limit.)

## What next

| You want to | Read |
|---|---|
| Learn step by step, with a plan | [Learning path](learning-path.en.md) |
| Install the environment, or run without installing | [Setup](setup.en.md) |
| Look up a term | [Glossary](glossary.en.md) |
| Find answers to common questions (including cryptography) | [FAQ](faq.en.md) |
| Find outside materials to keep learning | [Resources](resources.en.md) |
