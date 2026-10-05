# 延伸学习资源

[Tiếng Việt](resources.md) · [English](resources.en.md) · **简体中文**

这是一份精选清单，只收录免费或经典的资料，并注明真实的入门要求。大多数资料是英文的；面向初学者的高质量越南语资料仍然很少，这也正是本仓库存在的原因。本页链接已于 2026 年 10 月核查。

## 数学基础复习（如有需要）

| 资料 | 用途 |
|---|---|
| [3Blue1Brown, *Essence of linear algebra*](https://www.3blue1brown.com/topics/linear-algebra) | 用直观的视频讲解向量和矩阵；足以应对第 01 部分 |
| [Khan Academy, Linear algebra](https://www.khanacademy.org/math/linear-algebra) 和 [Precalculus](https://www.khanacademy.org/math/precalculus) | 向量、矩阵和复数，附有交互式练习 |

## 了解全貌

| 资料 | 适合人群 | 备注 |
|---|---|---|
| [*Quantum Computing for the Quantum Curious*](https://link.springer.com/book/10.1007/978-3-030-61601-4)（Hughes 等，Springer Open，2021，CC BY） | **只有高中物理基础、数学不多的人** | 开放获取的书，文字通俗易读，用最少的数学解释叠加（superposition）、测量（measurement）和纠缠（entanglement） |
| [Quantum Country](https://quantum.country)（Andy Matuschak 和 Michael Nielsen） | **已经熟悉线性代数和复数**的人（作者要求具备基础水平） | 免费。一系列交互式文章，配有帮助长期记忆的复习卡片：*Quantum computing for the very curious*、*How the quantum search algorithm works*、*How quantum teleportation works*、*Quantum mechanics distilled* |

## 系统学习（与本仓库同一水平）

| 资料 | 适合人群 | 备注 |
|---|---|---|
| [IBM Quantum Learning: Basics of quantum information](https://quantum.cloud.ibm.com/learning/courses/basics-of-quantum-information) | 熟悉线性代数和复数的人 | 免费。John Watrous 主讲的视频课程，附有详细的文字稿；内容一直讲到量子隐形传态（teleportation）、超密编码（superdense coding）和 CHSH 游戏（贝尔不等式）。适合在学完第 03 部分之后学习 |
| [IBM Quantum Learning: Fundamentals of quantum algorithms](https://quantum.cloud.ibm.com/learning/courses/fundamentals-of-quantum-algorithms) | 已经学完第 04 部分的人 | 免费，同一作者。内容包括查询算法（Deutsch–Jozsa、Simon）、相位估计、肖尔（Shor）算法和格罗弗（Grover）算法；其中相位估计和肖尔算法正是原书尚缺的部分 |
| [Qiskit documentation](https://quantum.cloud.ibm.com/docs) | 写代码的人 | Qiskit 的官方文档：指南和 API |
| *Programming Quantum Computers*（Johnston、Harrigan、Gimeno-Segovia，O'Reilly 2019） | 程序员 | 付费书籍，更多是从程序员而不是物理学的角度切入 |

## 深入学习

| 资料 | 适合人群 | 备注 |
|---|---|---|
| *Quantum Computation and Quantum Information*（Nielsen 和 Chuang） | 想打下完整基础的人 | 经典教材，付费。数学相当多 |
| [John Preskill 的讲义（Caltech Ph219）](https://preskill.caltech.edu/ph219/) | 研究生或大学高年级学生 | 免费。内容从算法、量子纠错一直到量子信息论 |

## 按主题

| 主题 | 资料 |
|---|---|
| **量子机器学习、变分算法** | [PennyLane](https://pennylane.ai/qml)：库和教程 |
| **后量子密码学** | [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) |
| **本仓库所依据的原书** | [learnquantum.io](https://learnquantum.io) 和[作者的仓库](https://github.com/learn-quantum/lqc-textbook) |

## 如何选择

- **完全零基础**：读 *Quantum Computing for the Quantum Curious*，同时跟着本仓库学习。看完*数学基础复习*部分后，再读 Quantum Country。
- **想掌握写代码的技能**：先学完这里的第 00–04 部分，再读 Qiskit documentation。
- **想理解 Shor、QFT、QPE**：学习 IBM 的 *Fundamentals of quantum algorithms* 课程，然后读 Nielsen 和 Chuang 的书或 Preskill 的讲义。
- **想理解贝尔不等式**：学习 IBM 的 *Basics of quantum information* 课程。

> 发现链接失效，或者有值得添加的资料（尤其是越南语资料）？请看 [CONTRIBUTING](../CONTRIBUTING.zh-CN.md)。
