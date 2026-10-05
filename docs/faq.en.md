# Frequently asked questions

[Tiếng Việt](faq.md) · **English** · [简体中文](faq.zh-CN.md)

## About quantum computers

### Will quantum computers replace ordinary computers?

No. In theory, a quantum computer is good at a few specific problems (see the [table on the introduction page](what-is-quantum-computing.en.md#what-is-known))
and does not help with most everyday tasks. Most likely the two will coexist: the quantum machine as an
accelerator for a few kinds of computation, like a GPU today.

### Is it true that it "tries every answer at once"?

This is the most common misunderstanding. A qubit in superposition is in **one definite state**, described by amplitudes;
it is not "both 0 and 1". And **a measurement gives only one result**. If you just "try everything" and then measure, you get one
random answer.

The key is **interference** (together with entanglement): the algorithm is designed so that the paths leading to wrong answers cancel each other out
while the right answer is amplified. Designing an algorithm like this is very hard, and it is possible only for some problems.
A concrete example is on the [introduction page](what-is-quantum-computing.en.md) (two H gates in a row).

### How is entanglement different from two coins that were matched in advance?

If you only look at the results `00` or `11`, there is no difference: two coins sealed in two envelopes, matched in advance, give the same
results. The difference shows up only when you **measure in several different directions**. Then the correlations of entangled qubits are stronger
than anything a "results decided in advance" scheme can produce. This is the content of the *Bell inequality* (for example the CHSH game).
IBM's *Basics of quantum information* course in [Resources](resources.en.md) covers this.

### Does entanglement allow messages to travel faster than light?

No. The measurement result at each end is random; you see the correlation only when the two sides **compare their results over an ordinary channel**.
Teleportation works the same way: Bob can recover the state only after receiving **two classical bits** from Alice
([03_02](../chapters/03_quantum_protocols/README.en.md)).

### Can a qubit be copied?

Not if the state is unknown. That is the *no-cloning* theorem ([02_04](../chapters/02_quantum_computing/README.en.md)).
This very property is what makes quantum money hard to counterfeit ([03_01](../chapters/03_quantum_protocols/README.en.md)).

### What can quantum computers do today?

Today's machines (as of October 2026) are noisy and not yet error-corrected at a large enough scale, so they cannot run large algorithms such as Shor's. They are used for research, for trying out
small algorithms and for simulating quantum systems. Progress is fast and many claims are disputed; prefer primary sources
(papers, the companies' technical documents) over news, and be cautious about "a million times faster" figures that do not say which problem they refer to.

## About cryptography

### Can quantum computers break encryption?

**Some kinds, and only if a large enough machine exists.**

- **Public-key cryptography** (used for key exchange and digital signatures), such as RSA and elliptic-curve cryptography (ECC), relies on the difficulty of factoring or of the
  *discrete logarithm* (another number-theory problem that ordinary computers also cannot yet solve quickly). **Shor's** algorithm solves these problems in polynomial time, so a large error-corrected
  quantum computer would break them. Such a machine **does not exist yet** (as of October 2026).
- **Symmetric encryption** (such as AES) is affected much less: **Grover's** algorithm gives only a quadratic speedup, so against brute-force
  key search, a $k$-bit key has a theoretical security of about $k/2$ bits (AES-128 drops to about 64 bits). NIST still accepts AES-128
  (the draft NIST IR 8547 uses it as the benchmark for the lowest security level); some organizations, such as the NSA, require AES-256 to leave a safety margin.
  In practice Grover's algorithm is hard to parallelize, so the real effect is even smaller than the theoretical figure.

### So do I need to worry right now?

There is one reason to prepare early: an attacker can **store encrypted data today and decrypt it once such a machine exists**
("harvest now, decrypt later"). For data that must stay secret for decades, this risk is real. (This risk mainly concerns
long-term secrets, especially key exchange; digital signatures are threatened only from the moment a powerful enough machine appears, and are not affected retroactively. Even so, long-lived signatures and certificates, such as firmware signatures or root certificates, still need to move to post-quantum algorithms before that time.)

The solution is **post-quantum cryptography**: algorithms that run on ordinary computers but
are believed to withstand quantum computers as well. In August 2024, NIST published the first three standards:
FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA). As of October 2026, NIST is still finalizing FN-DSA (FIPS 206) and the HQC standard.
The draft NIST IR 8547 (November 2024; still a draft as of October 2026) proposes to deprecate RSA/ECC at the 112-bit security level (such as RSA-2048)
after 2030, and to disallow all RSA/ECC after 2035. See
[NIST's page](https://csrc.nist.gov/projects/post-quantum-cryptography) for the current status.

### What about "quantum cryptography" (QKD)?

QKD (quantum key distribution) is a different approach: it uses quantum physics to let two parties share a secret key;
it is not an algorithm that resists quantum computers. QKD needs an authenticated classical channel and specialized equipment, and it is limited in
distance; some national security agencies publicly prefer post-quantum cryptography over QKD for most needs.
The QKD chapter (03_05) of the original textbook is still empty.

## About learning

### What do I need to know before I start?

Mostly basic Python. The math you need (vectors, matrices, complex numbers) is taught gradually in the textbook.
See the [Learning path](learning-path.en.md#what-you-need-first), which includes a 5-minute self-check.

### Can I learn this if I don't know how to program?

You can follow the ideas: the page [What is a quantum computer?](what-is-quantum-computing.en.md), the *Quick recap* sections
in each part's README, and the book *Quantum Computing for the Quantum Curious* ([Resources](resources.en.md)) do not require any code.
To run the code and do the exercises yourself, you need basic Python; a few weeks of learning Python is enough to get started.

### Why learn quantum computing? Are there jobs?

Today this is mainly a field of research and experimentation; there are few job openings compared with ordinary programming, and they
usually require a solid background in physics, math or computer science. Learn it because you are interested in the subject, and because the foundations
(linear algebra, probability, algorithmic thinking) are useful in many other places, rather than because you expect a job right away.

### Do I have to read a lot of English?

The guides in this repo are written in Vietnamese (with English and Simplified Chinese translations), but the original notebooks, the Qiskit documentation and most of the resources for further
learning are in English. You do not need to be fluent: the notebooks use simple sentences, and the [glossary](glossary.en.md) also gives the English names
so you can get used to them gradually.

### Do I need to learn quantum physics first?

No. The quantum part of the textbook (Part 02) starts from the Stern–Gerlach experiment and builds the concept of the qubit from there.
You do not need to solve the Schrödinger equation or know atomic physics.

### Do I need a real quantum computer or an IBM account?

No. Every notebook runs on a simulator on your own machine. An IBM Quantum account is needed only if you want to run on
real hardware (instructions in [00_02](../chapters/00_getting_started/README.en.md)); access conditions change with
IBM's policy, so check the official page.

### What computer specs do I need?

An ordinary laptop is enough: the examples use at most 14 qubits, so the statevector takes only about 256 KiB
(see the [memory table](what-is-quantum-computing.en.md#why-not-simply-simulate-it-on-an-ordinary-computer)). On the repo's development machine, all 19 notebooks run in about 3–5.5 minutes (measured on 2026-10-01 and 2026-10-05, after the libraries were installed); your machine may be slower.

### Should I use Qiskit, Cirq or PennyLane?

The differences are mostly about the ecosystem. **Qiskit** (IBM) is one of the most popular libraries and is the one this textbook uses.
**Cirq** (Google) is also a Python library for quantum circuits. **PennyLane** (Xanadu) is strong in quantum machine learning and variational algorithms.
The concepts are the same, so once you have learned one library you can move to another (note that the qubit-ordering convention can differ between libraries).

### Why do qubits in Qiskit "read from right to left"?

That is the *little-endian* convention: qubit 0 is the least significant bit and sits on the right of the result string (`'011'` means
$q_2 = 0, q_1 = 1, q_0 = 1$). See [Setup](setup.en.md#a-few-conventions-that-cause-confusion-when-reading-qiskit-code).

### Why do my results differ from the output in the notebook?

That is normal for sampled results (`shots`): each run gives slightly different numbers. `Statevector` results do not change.
If the conclusion is completely different (or you get an error), see [troubleshooting](setup.en.md#troubleshooting).

## About this repo

### How does this repo differ from the original textbook on learnquantum.io?

The notebooks and figures are **verbatim copies** of the original textbook (MIT license). What this repo adds is
the Vietnamese guide for each part (with English and Simplified Chinese translations), the [list of errata](../ERRATA.en.md), the introductory material in the `docs/` folder,
and automated tests. All credit for the textbook's content belongs to its author, Diego Emilio Serrano.

### Why are Parts 05 and 06 (QFT, Shor, ...) missing?

On the textbook's website, these chapters have only titles and no content yet, so they have not been copied.
An automated workflow checks the original textbook every week and notifies the maintainer, who will add them once the author has finished writing them.

### I found an error or want to make a suggestion. What should I do?

See [CONTRIBUTING](../CONTRIBUTING.en.md). All feedback is welcome, from fixing typos to writing new guides.

### Where can I ask about the content of the textbook?

- **In this repo (Vietnamese, English or Chinese):** open an issue using the *Câu hỏi khi học* ("Question while studying") template in [this repo's Issues](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose).
  Say clearly which lesson you are studying and what you have tried.
- **In English:** [the original repo's Discussions](https://github.com/learn-quantum/lqc-textbook/discussions), where the author
  and the community answer.
