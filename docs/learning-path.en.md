# Learning path

[Tiếng Việt](learning-path.md) · **English** · [简体中文](learning-path.zh-CN.md)

This page helps you choose a starting point, know what to prepare, and check yourself after each part.
Don't know what a quantum computer is yet? Read [What is a quantum computer?](what-is-quantum-computing.en.md) first (15 minutes).

## Where do you start?

| You are | What to do |
|---|---|
| **Curious, no programming experience yet** | Read [What is a quantum computer?](what-is-quantum-computing.en.md) and the [FAQ](faq.en.md). Then read the open book *Quantum Computing for the Quantum Curious* (little math, see [Resources](resources.en.md)). If you want to look at this repo without coding: read the *Quick recap* section of each lesson in [Part 02](../chapters/02_quantum_computing/README.en.md) and [Part 03](../chapters/03_quantum_protocols/README.en.md); the notebooks already contain their output, so there is nothing to run. When you want to code, learn basic Python and then come back |
| **Know basic Python** | Follow the full learning path below, starting from Part 00. This is the route for most readers |
| **Know Python and linear algebra** (vectors, matrices, complex numbers) | Do Part 00. In Part 01: skim 01_01, read 01_02 (reversible gates X, CX, CCX, the foundation of oracles), skim 01_03 to pick up ket notation and the Kronecker product, and skim 01_04 quickly (probabilistic bits, which 02_01 uses for comparison with qubits). (If the tensor/Kronecker product is unfamiliar, read 01_03 carefully.) Read carefully from Part 02 onward |
| **Have already studied quantum mechanics at school** | Read the *Key code* section of [02_01](../chapters/02_quantum_computing/README.en.md) to get used to how Qiskit writes circuits, then 02_04, 02_05 and Part 04 (if the single-qubit gate syntax is unfamiliar, skim 02_03 as well). Use the repo as a Qiskit handbook |

## What you need first

**The only real requirement: basic Python.** The book teaches the math gradually: vectors and matrices in Part 01, complex numbers and the
Bloch sphere in 02_03. Learning is gentler if you have already met them; see the *Math refresher* section below.

| Skill | Level needed | If you are still weak |
|---|---|---|
| **Python** | Variables, functions, loops, lists; know `import` and be able to read short code | Take a basic Python course first. You do not need to know NumPy; the book explains it when it is used |
| **Binary numbers and logic** | Convert binary to decimal; know AND, OR, XOR | Lesson 01_01 teaches it again from scratch |
| **Probability** | The probability of an event, the total being 1; multiplying the probabilities of two independent events | Reviewing grade-10 material is enough |
| **Linear algebra** | Multiply a matrix by a vector | Lesson 01_03 teaches it; looking at it beforehand makes it easier (see the *Math refresher* section) |
| **Complex numbers** | Know $i^2 = -1$, the modulus $\vert a+bi \vert$ | 02_03 teaches it again; looking at it beforehand makes it easier |
| **Quantum physics** | Not needed | The book is built up from the Stern–Gerlach experiment |

### Math refresher (optional, 1–3 hours)

If you have never met matrices or complex numbers, take a look at these beforehand:

- [3Blue1Brown, *Essence of linear algebra*](https://www.3blue1brown.com/topics/linear-algebra): a visual video series about vectors
  and matrices (watching the first four videos, up to multiplying two matrices, is enough for Part 01).
- [Khan Academy, Linear algebra](https://www.khanacademy.org/math/linear-algebra) (vectors, matrices) and
  [Precalculus](https://www.khanacademy.org/math/precalculus) (the complex-numbers part): free, with interactive exercises.

### Self-check (5 minutes)

Answer quickly without looking anything up.

1. What numbers does the Python snippet `for x in range(4): print(x * x)` print?
2. What is the binary number `101` in decimal? And what is `1 XOR 1`?
3. If you flip two fair coins, what is the probability that both land heads?
4. Compute $\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}$.
5. What is the modulus of the complex number $3+4i$?

**How to read your results:** if you got question 1 wrong, review Python first. If you got question 2 wrong (binary, XOR), that is fine: 01_01 teaches it again from scratch.
If you got question 3 wrong, review grade-10 level probability (the probability that two independent events both happen), because 01_04 and 02_02 use exactly
this calculation.
If you got questions 4–5 wrong, that is **fine**, because the book teaches them again; but if both are unfamiliar, look at the *Math refresher* section above.

<details>
<summary>Answers</summary>

1. `0`, `1`, `4`, `9` (one number per line)
2. 5; and `1 XOR 1 = 0`
3. $1/4$
4. $\begin{pmatrix}0\\1\end{pmatrix}$ (this matrix is the X gate, which turns $|0\rangle$ into $|1\rangle$)
5. 5, because $\sqrt{3^2 + 4^2} = 5$

</details>

## Full learning path

<!-- translate-block -->
```text
00 Setup ─> 01 Classical ─> 02 Quantum ─> 03 Protocols ─> 04 Algorithms ─> Keep learning
            (vectors,       (qubits, Bloch,   (teleportation,  (Deutsch–Jozsa → BV    (QFT, Shor,
             matrices)       entanglement,     superdense)      → Simon → Grover)     VQE, ...)
                             oracle)
```

Part 01 looks "classical", but it is the toolkit of vectors, matrices and tensor products that every later part reuses.
Lesson 02_05 (oracle, phase kickback) is the foundation of all of Part 04.

The times below are **estimates** for a careful learner: reading closely, retyping the code yourself, doing the self-checks.
A reader who skims can go much faster. Adding up the five parts below gives roughly 25–40 hours (not counting the optional *Math refresher* section),
that is, 4–6 weeks at one hour a day.

Each part has a **self-check** and **suggested answers**. Try to answer them yourself before opening the answers.

### Part 00 · Getting started ([README](../chapters/00_getting_started/README.en.md)), about 1 hour

Install the environment and get the verification snippet running. See also [Setup](setup.en.md).

**By the end you can:** run a notebook on your own machine and see `00`/`11` results at roughly 50/50.

### Part 01 · Classical computing ([README](../chapters/01_classical_computing/README.en.md)), about 4–6 hours

Bits, logic gates, reversible gates, bits as vectors and gates as matrices, probabilistic bits.

**Self-check:**
- Why is the AND gate not reversible, while the CX gate is?
- Write the $4 \times 4$ matrix of the CX gate (the control bit is the left bit in ket notation) and check that it turns $|10\rangle$ into $|11\rangle$.
- How many dimensions does the Kronecker product of two 2-dimensional vectors have? And for $n$ bits?

<details>
<summary>Suggested answers</summary>

- AND gives the same output 0 for three different inputs (`00`, `01`, `10`), so you cannot work backward from the output to the input.
  CX maps $(a, b) \to (a, a \oplus b)$, so it can be undone; in fact, applying CX again takes you back to the input.
- With the basis order $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ and the left bit as the control bit, the matrix keeps the first two rows unchanged
  and swaps the last two: $\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$.
  The column for $|10\rangle$ has a 1 in the row of $|11\rangle$, that is, $|10\rangle \to |11\rangle$.
- $2 \times 2 = 4$ dimensions; for $n$ bits it is $2^n$ dimensions.

</details>

### Part 02 · Quantum computing ([README](../chapters/02_quantum_computing/README.en.md)), about 10–15 hours

The heaviest and most important part: qubits, superposition, entanglement, the Bloch sphere, one-qubit and multi-qubit gates,
measurement, and the "building blocks" (Bell, GHZ, W, oracle, phase kickback).
Split it into several sessions, and **read 02_05 carefully** because Part 04 depends entirely on it.

**Self-check:**
- Compute $H \cdot H|0\rangle$ by hand, then verify it with Qiskit. Why is the result $|0\rangle$ with certainty?
- Create a Bell state and explain why only `00` or `11` can be measured.
- Where are $|+\rangle$ and $|-\rangle$ on the Bloch sphere? How do these two states differ if you only measure along the $z$ axis?

<details>
<summary>Suggested answers</summary>

- The full calculation is on the [introduction page](what-is-quantum-computing.en.md#interference-flip-twice-and-the-result-is-certain):
  the amplitude of $|1\rangle$ is $+\tfrac12 - \tfrac12 = 0$ so it cancels out, and that of $|0\rangle$ is $\tfrac12 + \tfrac12 = 1$.
- H on qubit 0 and then CX(0, 1) gives $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$. The amplitudes of $|01\rangle$ and $|10\rangle$ are 0,
  so the probability of measuring them is 0.
- $|+\rangle$ lies on the $+x$ axis and $|-\rangle$ on the $-x$ axis of the Bloch sphere, both on the equator. Measuring along the $z$ axis
  gives 50/50 for both, so you cannot tell them apart. They differ in the relative sign of the amplitudes (the phase), which shows up when you measure along the $x$ axis (that is, apply H and then measure: $|+\rangle \to$ `0`, $|-\rangle \to$ `1`).

</details>

### Part 03 · Quantum protocols ([README](../chapters/03_quantum_protocols/README.en.md)), about 3–5 hours

The first three applications of entanglement and the uncertainty principle: quantum money, teleportation, superdense coding.

**Self-check:**
- Does teleportation send information faster than light? Why?
- How are superdense coding and teleportation alike and different in the resources they use (qubits, classical bits, entangled pairs)?
- Why can't a forger of quantum money copy a coin?

<details>
<summary>Suggested answers</summary>

- No. Bob's qubit only becomes the state that was to be sent after he receives **two classical bits** from Alice, and classical bits
  cannot travel faster than light. Before that, what Bob sees is random.
- Both use **a shared entangled pair** prepared beforehand. Teleportation sends **1 qubit** by transmitting **2 classical bits**;
  superdense coding is the reverse: it sends **2 classical bits** by transmitting **1 qubit**.
- The forger does not know which basis each qubit was prepared in (bit or sign). Measuring in the wrong basis ruins the state,
  and the no-cloning theorem forbids copying an unknown state, so there is no way to make a reliable copy: the probability that a forgery
  passes the check falls exponentially as the number of qubits grows (for example $(3/4)^n$ with the measure-and-re-prepare strategy). Details in 03_01.

</details>

### Part 04 · Quantum algorithms ([README](../chapters/04_quantum_algorithms/README.en.md)), about 8–12 hours

Deutsch–Jozsa, Bernstein–Vazirani and Simon share one template (Hadamard → oracle → Hadamard → measure; Simon repeats this template about $n$ times and then solves a system of linear equations mod 2 on a classical computer);
Grover repeats the pair "oracle + amplitude amplification" about (π/4)·√N times.

**Self-check:**
- What is phase kickback, and how does it let the oracle $U_f$ turn the value $f(x)$ into the sign $(-1)^{f(x)}$?
- About how many oracle calls does Grover need to find 1 item among $N = 2^{20}$ items? (Hint: $\tfrac{\pi}{4}\sqrt N$; compare with the classical case.)
- Why does Deutsch–Jozsa give a "speedup" but have no practical application?

<details>
<summary>Suggested answers</summary>

- When the target qubit is in the state $|-\rangle$, the oracle gives $U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle$: the value $f(x)$ "kicks back"
  as a sign on the input qubits, and that sign is something interference can use. Details in 02_05.
- $\tfrac{\pi}{4}\sqrt{2^{20}} \approx 804$ calls. Classically you need on average about $N/2 \approx 524\,000$ calls.
- The Deutsch–Jozsa problem is artificial, designed to show an advantage. In addition, the advantage exists only against classical algorithms
  that are *guaranteed to be correct*; a randomized classical algorithm solves it with a few queries and a very small probability of error.

</details>

## What comes after Part 04?

The original textbook plans further chapters on **QFT, QPE, Shor, HHL, Hamiltonian simulation**, but the author has not written them yet
(see [the chapters that are still empty](../README.en.md#chapters-that-are-still-empty-upstream)). In the meantime, you can:

| Direction | Suggestion |
|---|---|
| Keep learning up to Shor, QFT, QPE | IBM's course *Fundamentals of quantum algorithms* (covers Deutsch–Jozsa, Simon, QPE, Shor, Grover) and Preskill's notes (graduate level), in [Resources](resources.en.md) |
| Understand entanglement more deeply (Bell inequality, CHSH) | IBM's course *Basics of quantum information* in [Resources](resources.en.md) |
| Learn variational algorithms (VQE, QAOA) and quantum machine learning | PennyLane in [Resources](resources.en.md) |
| Understand the threat to cryptography | The cryptography section in the [FAQ](faq.en.md#about-cryptography) |
| Run on a real quantum computer | The 00_02 guide in [Part 00](../chapters/00_getting_started/README.en.md) |

## Study tips

- **Run each cell and predict the result first.** If you guess wrong, that is exactly where you will learn the most.
- **Change the parameters and run again.** Change `shots`, swap the gate, change the control qubit.
- **Don't get stuck on one formula.** The book gives a concrete example after each concept; understand the example, then go back to the formula.
- **Look up unfamiliar terms** in the [glossary](glossary.en.md).
- **Think the book is wrong?** See [ERRATA](../ERRATA.en.md): a few small errors in the book have already been recorded, so you do not have to find them yourself.
