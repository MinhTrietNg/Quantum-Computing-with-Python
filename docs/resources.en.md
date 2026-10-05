# Resources for further learning

[Tiếng Việt](resources.md) · **English** · [简体中文](resources.zh-CN.md)

A curated list containing only free or classic material, with the real prerequisites for each item.
Most of it is in English; good Vietnamese-language material for beginners is still very scarce, and that is why this repo exists.
The links were checked in October 2026.

## Math refresher (if needed)

| Resource | Use it for |
|---|---|
| [3Blue1Brown, *Essence of linear algebra*](https://www.3blue1brown.com/topics/linear-algebra) | Vectors and matrices, in intuitive videos; enough for Part 01 |
| [Khan Academy, Linear algebra](https://www.khanacademy.org/math/linear-algebra) and [Precalculus](https://www.khanacademy.org/math/precalculus) | Vectors, matrices and complex numbers, with interactive exercises |

## Reading to get the big picture

| Resource | Aimed at | Notes |
|---|---|---|
| [*Quantum Computing for the Quantum Curious*](https://link.springer.com/book/10.1007/978-3-030-61601-4) (Hughes et al., Springer Open, 2021, CC BY) | **People with only high-school physics and little math** | An open book with an easy-to-read style that explains superposition, measurement and entanglement with a minimum of math |
| [Quantum Country](https://quantum.country) (Andy Matuschak and Michael Nielsen) | People who are **already comfortable with linear algebra and complex numbers** (the authors require a basic level) | Free. Interactive essays with review cards that help you remember for the long term: *Quantum computing for the very curious*, *How the quantum search algorithm works*, *How quantum teleportation works*, *Quantum mechanics distilled* |

## Systematic study (at the same level as this repo)

| Resource | Aimed at | Notes |
|---|---|---|
| [IBM Quantum Learning: Basics of quantum information](https://quantum.cloud.ibm.com/learning/courses/basics-of-quantum-information) | People comfortable with linear algebra and complex numbers | Free. Video lectures by John Watrous with detailed written versions; it goes as far as teleportation, superdense coding and the CHSH game (the Bell inequality). A sensible next step after Part 03 |
| [IBM Quantum Learning: Fundamentals of quantum algorithms](https://quantum.cloud.ibm.com/learning/courses/fundamentals-of-quantum-algorithms) | People who have finished Part 04 | Free, by the same author. Query algorithms (Deutsch–Jozsa, Simon), phase estimation, Shor's algorithm and Grover's algorithm; phase estimation and Shor are the parts the original textbook is still missing |
| [Qiskit documentation](https://quantum.cloud.ibm.com/docs) | People who write code | The official Qiskit documentation: guides and API |
| *Programming Quantum Computers* (Johnston, Harrigan, Gimeno-Segovia, O'Reilly 2019) | Programmers | A paid book that approaches the subject from the programmer's angle rather than the physicist's |

## In depth

| Resource | Aimed at | Notes |
|---|---|---|
| *Quantum Computation and Quantum Information* (Nielsen and Chuang) | People who want a complete foundation | The classic textbook, paid. Quite heavy on math |
| [John Preskill's notes (Caltech Ph219)](https://preskill.caltech.edu/ph219/) | Graduate or final-year undergraduate students | Free. The content ranges from algorithms and quantum error correction to quantum information theory |

## By topic

| Topic | Resource |
|---|---|
| **Quantum machine learning, variational algorithms** | [PennyLane](https://pennylane.ai/qml): library and tutorials |
| **Post-quantum cryptography** | [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) |
| **The original textbook of this repo** | [learnquantum.io](https://learnquantum.io) and [the author's repo](https://github.com/learn-quantum/lqc-textbook) |

## How to choose

- **Complete beginner:** *Quantum Computing for the Quantum Curious*, alongside this repo. Quantum Country once you have finished the *Math refresher* section.
- **Want coding skills:** work through all of Parts 00–04 here, then read the Qiskit documentation.
- **Want to understand Shor, QFT, QPE:** IBM's *Fundamentals of quantum algorithms* course, then Nielsen and Chuang or Preskill's notes.
- **Want to understand the Bell inequality:** IBM's *Basics of quantum information* course.

> Found a broken link or a resource worth adding (especially Vietnamese-language material)? See [CONTRIBUTING](../CONTRIBUTING.en.md).
