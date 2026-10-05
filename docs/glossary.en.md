# Glossary

[Tiếng Việt](glossary.md) · **English** · [简体中文](glossary.zh-CN.md)

This is the English edition of the Vietnamese glossary. Each entry gives the English term, with its Vietnamese equivalent in parentheses in italics so you can cross-reference the Vietnamese guides, then a short definition and where to study it in depth. Where the Vietnamese guides use the English term as is, no Vietnamese equivalent is shown. The notation $|\cdot\rangle$ is read "ket".
Use `Ctrl+F` to search quickly. Entries marked *(read later)* are advanced concepts that you do not need to understand when you are just starting.
Came across a word that is not here? [Open an issue](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose) and we will add it.

Abbreviations for where to study: **P01** = [Part 01](../chapters/01_classical_computing/README.en.md),
**P02** = [Part 02](../chapters/02_quantum_computing/README.en.md),
**P03** = [Part 03](../chapters/03_quantum_protocols/README.en.md),
**P04** = [Part 04](../chapters/04_quantum_algorithms/README.en.md).

## Math you need

| Term | Meaning | Where to study |
|---|---|---|
| Vector | An ordered list of numbers, for example $(1, 0)$. Bits and qubits are both written as vectors | P01 |
| Matrix (*ma trận*) | A table of numbers; multiplying a matrix by a vector turns one vector into another. Every gate is a matrix | P01 |
| Complex number (*số phức*) | A number of the form $a + bi$ with $i^2 = -1$; $a$ is the real part, $b$ is the imaginary part. Qubit amplitudes can be complex numbers | P02 |
| Modulus (magnitude) of a complex number (*môđun (độ lớn) của số phức*) | $\vert a + bi \vert = \sqrt{a^2 + b^2}$; for example $\vert 3 + 4i \vert = 5$ | P02 |
| XOR ($\oplus$) | Add two bits and discard the carry: $0 \oplus 0 = 0$, $0 \oplus 1 = 1$, $1 \oplus 1 = 0$ | P01 |
| Constant function / balanced function (*hàm hằng / hàm cân bằng*) | A function $f$ on bit strings: *constant* if it gives the same value for every input; *balanced* if it gives 0 for exactly half of the inputs and 1 for the other half | P04 |
| Expectation value (*giá trị kỳ vọng*) | The average value you get when a measurement is repeated a very large number of times | P02 |

## Fundamentals

| Term | Meaning | Where to study |
|---|---|---|
| Bit | The unit of classical information, taking the value 0 or 1 | P01 |
| Qubit | The unit of quantum information; its state is $\alpha\vert 0\rangle + \beta\vert 1\rangle$ | P02 |
| Ket $\vert \psi\rangle$ | Dirac notation for a state vector (a column). $\vert 0\rangle$ is the column $(1, 0)$ and $\vert 1\rangle$ is the column $(0, 1)$ (written compactly as $(1, 0)^T$: the letter $T$ means arranged as a column) | P01, P02 |
| Amplitude (*biên độ*) | The complex coefficient in front of each basis state. Its squared modulus is the probability of measuring that state | P02 |
| Superposition (*chồng chập*) | A state that is a combination of several basis states, for example $\tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$ | P02 |
| $\vert +\rangle$, $\vert -\rangle$ states (*trạng thái*) | The two equal superposition states: $\vert +\rangle = \tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$ and $\vert -\rangle = \tfrac{1}{\sqrt2}(\vert 0\rangle - \vert 1\rangle)$; they differ only in the relative sign | P02 |
| Measurement (*đo*) | Extracting a classical bit from a qubit, with probability given by the squared modulus of the amplitude; the qubit is changed into the state that was just measured | P02 |
| Basis (*cơ sở*) | A set of states used as the "coordinate axes" for measuring or writing a state, for example the basis $\{\vert 0\rangle,\vert 1\rangle\}$ or $\{\vert +\rangle,\vert -\rangle\}$ | P02 |
| Phase (*pha*) | The angle of a complex amplitude. Global phase cannot be measured; the *relative* phase between amplitudes determines interference | P02 |
| Interference (*giao thoa*) | Amplitudes add up or cancel each other. Together with entanglement, it is the key to the power of quantum algorithms | P02, P04 |
| Bloch sphere | A sphere representing every pure state of a single qubit; $\vert 0\rangle$ is at the north pole and $\vert 1\rangle$ at the south pole | P02 |
| Tensor / Kronecker product (*tích tensor / Kronecker*) | A way to combine the states and gates of several systems: $\vert 0\rangle \otimes \vert 1\rangle = \vert 01\rangle$ | P01, P02 |
| Statevector | A vector holding all the amplitudes of an $n$-qubit system ($2^n$ complex numbers) | P02 |
| Observable *(read later)* | A measurable quantity, represented by a Hermitian matrix; its eigenvalues are the possible measurement results | P02 |

## Gates and circuits

| Term | Meaning | Where to study |
|---|---|---|
| Gate (*cổng*) | A transformation applied to qubits; a quantum gate is a *unitary* matrix | P02 |
| Unitary *(read later)* | A matrix $U$ satisfying $U^\dagger U = I$ ($U^\dagger$ is the conjugate transpose: transpose the matrix, then take the complex conjugate); it preserves total probability and is always invertible | P02 |
| Reversible (*khả nghịch*) | You can work out the input from the output. Every quantum gate is reversible | P01 |
| X gate (*cổng X*) | The quantum "NOT": swaps $\vert 0\rangle \leftrightarrow \vert 1\rangle$ | P01, P02 |
| Hadamard gate (H) (*cổng Hadamard*) | Turns $\vert 0\rangle$ into $\tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$; the most familiar gate for creating superposition | P02 |
| Pauli gates (X, Y, Z) (*cổng Pauli*) | The three basic single-qubit gates, equivalent to half-turn ($\pi$) rotations about the three axes $x, y, z$ of the Bloch sphere (up to a global phase, which cannot be measured) | P02 |
| Phase gates (P, S, T) (*cổng pha*) | Change only the phase of $\vert 1\rangle$; S is $\tfrac{\pi}{2}$, T is $\tfrac{\pi}{4}$ | P02 |
| CX (CNOT) | A two-qubit controlled gate: flips the target qubit if the control qubit is 1. The main gate for creating entanglement | P01, P02 |
| CCX (Toffoli) | Flips the target qubit if **both** control qubits are 1 | P01 |
| SWAP | Swaps the states of two qubits. It turns a product state into a product state, so by itself it does not create entanglement | P02 |
| Barrier (*vạch ngăn*) | A mark in the circuit diagram (drawn as `░`) that separates groups of gates for readability, without changing the state; `measure_all()` automatically inserts one barrier before the measurement | P02, [Introduction](what-is-quantum-computing.en.md) |
| Quantum circuit (*mạch lượng tử*) | A sequence of gates and measurements applied to qubits, drawn from left to right | P02 |
| Clifford gates (*cổng Clifford*) *(read later)* | The group of gates generated by H, S, CX. Circuits made only of these gates can be simulated efficiently on an ordinary computer (the Gottesman–Knill theorem) | P02 |
| Universal gate set (*bộ cổng phổ quát*) | A set of gates sufficient to approximate any quantum transformation, for example Clifford + T | P02 |

## Quantum phenomena

| Term | Meaning | Where to study |
|---|---|---|
| Entanglement (*vướng víu*) | A multi-qubit state that cannot be written as a product of the states of the individual qubits; for a pure state, it always gives correlations that violate some Bell inequality (stronger than any classical model) | P02 |
| Bell states (*trạng thái Bell*) | Four two-qubit entangled states, for example $\tfrac{1}{\sqrt2}(\vert 00\rangle + \vert 11\rangle)$ | P02 |
| GHZ, W | Two families of entangled states of three or more qubits, which differ in how they are entangled | P02 |
| Bell inequality / CHSH (*bất đẳng thức Bell / CHSH*) | A limit that the correlations of every classical model (with results "decided in advance") must obey. Entangled qubits violate it, so entanglement is not the same as two coins matched in advance. *Not yet in this textbook* | — |
| Uncertainty principle (*nguyên lý bất định*) | Two quantities such as X and Z (*non-commuting*: measuring them in a different order gives different results) cannot both have definite values at the same time | P03 |
| No-cloning | An unknown quantum state cannot be copied | P02 |
| Decoherence (*mất kết hợp*) | A kind of noise: the qubit loses its quantum properties through interaction with its environment | [Introduction](what-is-quantum-computing.en.md) |
| Noise (*nhiễu*) | Any random deviation caused by imperfect hardware: decoherence, gate errors, readout errors | P01 (probabilistic bits), [Introduction](what-is-quantum-computing.en.md) |

## Tools

| Term | Meaning |
|---|---|
| Notebook (`.ipynb`) | A document made of text cells and runnable code cells, opened with Jupyter, VS Code or Colab |
| Cell (*ô*) | One block in a notebook; run a code cell with `Shift+Enter` |
| Kernel | The Python program behind the notebook that runs the cells; you need to choose the right kernel (the one from `.venv`) |
| Virtual environment (`venv`) (*môi trường ảo*) | The `.venv` folder holding Python and libraries just for this repo, separate from the rest of your machine |
| Terminal | A window for typing commands (PowerShell on Windows, Terminal on macOS) |

## Other Vietnamese renderings

The same concept can be translated differently in different documents. The Vietnamese variants below are kept as they are; use this table when you search Vietnamese-language material.

| In this repo | Also found (Vietnamese) |
|---|---|
| Entanglement (*vướng víu*) | rối lượng tử, vướng mắc lượng tử |
| Superposition (*chồng chập*) | chồng chất, chồng chập lượng tử |
| Qubit | bit lượng tử |
| Bloch sphere (*mặt cầu Bloch*; this repo usually keeps the English name) | quả cầu Bloch |
| Modulus (*môđun*) | mô-đun |
| Tensor product (*tích tensor*) | tích Kronecker (the name the original textbook uses, so Parts 01 and 02 use it too, especially when talking about matrices) |
| Amplitude (*biên độ*) | biên độ xác suất |

## Protocols and algorithms

| Term | Meaning | Where to study |
|---|---|---|
| Teleportation (*dịch chuyển trạng thái lượng tử*) | Sending the unknown state of a qubit using an entangled pair plus **two classical bits**. It does not send anything faster than light | P03 |
| Superdense coding (*mã hóa siêu đặc*) | Sending **two classical bits** by sending **one qubit**, thanks to an entangled pair shared in advance | P03 |
| Oracle ($U_f$) | A quantum "black box" that computes a function $f$: $U_f\vert x\rangle\vert y\rangle = \vert x\rangle\vert y \oplus f(x)\rangle$ | P02, P04 |
| Phase kickback | When the target qubit is in $\vert -\rangle$, the oracle turns the value $f(x)$ into the sign $(-1)^{f(x)}$ on the control qubit | P02 |
| Query complexity (*độ phức tạp truy vấn*) | The number of oracle calls an algorithm needs; the yardstick used for comparison in Part 04 | P04 |
| Deutsch–Jozsa, Bernstein–Vazirani, Simon | Three classic query algorithms on artificial problems. The advantage of the first two is small, or only relative to a deterministic classical algorithm; Simon's gives an exponential advantage (in the oracle model) | P04 |
| Grover | Unstructured search with $\sim\sqrt N$ queries instead of $\sim N$ | P04 |
| Shor | Factoring integers into their prime factors in polynomial time. *Not yet in this textbook* | — |
| QFT, QPE | The quantum Fourier transform and phase estimation, two building blocks of Shor's algorithm. *Not yet in this textbook* | — |

## Complexity and cryptography

Used in the [Introduction](what-is-quantum-computing.en.md) and the [FAQ](faq.en.md); the original textbook does not teach these concepts yet.

| Term | Meaning |
|---|---|
| Polynomial / super-polynomial time (*thời gian đa thức / siêu đa thức*) | The number of computation steps grows like a fixed power of the input size (polynomial, usually considered "fast"), or grows faster than any such power (super-polynomial, for example exponential) |
| NP-complete (*NP-đầy-đủ*) | The "hardest" class of problems in NP: if one NP-complete problem can be solved in polynomial time, then every problem in NP can be. Nobody knows whether a fast algorithm exists (the P versus NP problem) |
| Public-key cryptography (RSA, ECC) (*mật mã khoá công khai*) | Cryptography used for key exchange and digital signatures, based on the difficulty of factoring (RSA) or of the *discrete logarithm* (ECC, Diffie–Hellman) |
| Discrete logarithm (*logarithm rời rạc*) | The problem of finding $x$ from $g^x \bmod p$ (or the analogous operation on an elliptic curve); ordinary computers have no known fast way to solve it, while Shor's algorithm solves it in polynomial time |
| Post-quantum cryptography (*mật mã hậu lượng tử*) | Cryptographic algorithms that run on ordinary computers but are designed to resist quantum computers as well, for example ML-KEM (FIPS 203) and ML-DSA (FIPS 204) |
| QKD, quantum key distribution (*phân phối khoá lượng tử*) | Using quantum physics so that two parties can share a secret key; unlike post-quantum cryptography, it needs specialized equipment |
| "Harvest now, decrypt later" | An attacker collects encrypted data today to decrypt it later, once a powerful enough quantum computer exists |

## Hardware and running on real devices

| Term | Meaning | Where to study |
|---|---|---|
| NISQ | Noisy Intermediate-Scale Quantum: today's machines, with many qubits but noisy and not yet error-corrected at a large enough scale | — |
| Physical qubit / logical qubit (*qubit vật lý / qubit logic*) | A physical qubit is an actual hardware element, and it is noisy; a logical qubit is a "virtual" qubit with fewer errors, encoded across many physical qubits by error correction | — |
| Quantum error correction (*sửa lỗi lượng tử*) | Using many physical qubits to create one logical qubit with fewer errors | — |
| QPU | Quantum Processing Unit: a real quantum chip | Part 00 |
| Simulator | A program that simulates a quantum computer on an ordinary computer (such as `AerSimulator`) | Part 00 |
| Shot | One run of a circuit together with its measurement; running $N$ shots gives a distribution of results | P02 |
| Counts | A tally of the measurement results over the shots, for example `{'00': 504, '11': 496}` | P02 |
| Little-endian | Qiskit's convention: qubit 0 is on the **right** of the result bit string | [Setup](setup.en.md) |
