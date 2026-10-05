# 01 · Classical computing

[Tiếng Việt](README.md) · **English** · [简体中文](README.zh-CN.md)

A review of bits, Boolean logic and digital circuits, which are then gradually "upgraded" in the direction quantum computers need:
**reversible** gates, bits as **vectors** and gates as **matrices**, and finally **probabilistic**
bits (p-bits). The math tools that Part 02 uses constantly (kets, the Kronecker product, the matrix of a circuit) are all built here.

> Source: [01_01](https://learnquantum.io/chapters/01_classical_computing/01_01_bits_and_circuits.html) ·
> [01_02](https://learnquantum.io/chapters/01_classical_computing/01_02_reversible_computing.html) ·
> [01_03](https://learnquantum.io/chapters/01_classical_computing/01_03_bits_to_vectors.html) ·
> [01_04](https://learnquantum.io/chapters/01_classical_computing/01_04_probabilistic_circuits.html)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## Contents

| Lesson | Notebook | Web | Key idea |
|---|---|---|---|
| 01_01 · Bits and digital circuits | [01_01_bits_and_circuits.ipynb](01_01_bits_and_circuits.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_01_bits_and_circuits.html) | Binary numbers in Python, AND/OR/NOT/XOR, adder circuits, CMOS transistors |
| 01_02 · Reversible computing | [01_02_reversible_computing.ipynb](01_02_reversible_computing.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_02_reversible_computing.html) | X, CX, CCX (Toffoli); reversible AND/OR/COPY/full adder |
| 01_03 · Linear algebra for reversible circuits | [01_03_bits_to_vectors.ipynb](01_03_bits_to_vectors.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_03_bits_to_vectors.html) | Bits as vectors $\vert 0\rangle,\vert 1\rangle$; gates as matrices; Kronecker product |
| 01_04 · Probabilistic computing | [01_04_probabilistic_circuits.ipynb](01_04_probabilistic_circuits.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_04_probabilistic_circuits.html) | p-bits, probability vectors, stochastic matrices |

This part uses only **plain Python, NumPy, SymPy and Matplotlib**, with no Qiskit yet.

> The code snippets in this README are **excerpts** from the notebooks (the original English comments are kept) and use variables defined in earlier cells. To run them, run the whole notebook from top to bottom.

---

## 01_01 · Bits and digital circuits

**Goal:** be able to work with binary numbers in Python and understand how logic circuits are built from basic gates.

### Key concepts

**Binary numbers.** $n$ bits $b = b_{n-1}\dots b_1 b_0$ can represent $2^n$ values. $b_0$ (the rightmost) is
the least significant bit (LSB), and $b_{n-1}$ is the most significant bit (MSB). Converting to decimal:

$$x = \sum_{i=0}^{n-1} 2^i\, b_i \qquad\text{for example } 1101 = 8 + 4 + 0 + 1 = 13$$

In the other direction, bit $i$ is $b_i = \lfloor x / 2^i \rfloor \bmod 2$. You need at least
$n \ge \lfloor \log_2 x + 1 \rfloor$ bits to represent $x > 0$ (for example, 13 needs 4 bits).

**Boolean logic.** There are three basic operations: NOT ($\bar a$), OR ($a \lor b$), AND ($a \land b$); every logical statement can
be built from these three. An operation used very heavily throughout the book is **XOR** (exclusive OR):

| $a$ | $b$ | $a \oplus b$ |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

$$a \oplus b = (a \land \bar b) \lor (\bar a \land b) = (a + b) \bmod 2$$

For numbers with several bits, these operations act **bit by bit** (bitwise).

**Digital circuits.** A logic gate is the graphical symbol for a Boolean operation.

<p align="center"><img src="images/01_01_01_basic_logic_gates.png" width="750" alt="Symbols of the three basic logic gates NOT, OR, AND"></p>

*Figure: symbols of the NOT, OR and AND gates (from left to right).*

NAND/NOR/XNOR are AND/OR/XOR with a NOT added at the output, drawn compactly with a small circle:

<p align="center"><img src="images/01_01_03_negated_logic_gates.png" width="760" alt="Symbols of the NAND, NOR, XNOR gates with a small circle at the output"></p>

*Figure: NAND, NOR, XNOR; the small circle at the output stands for a NOT gate.*

For example, the **full adder** adds $a$, $b$ and the carry-in $c_{in}$:

$$s = a \oplus b \oplus c_{in}, \qquad c_{out} = \big((a \oplus b) \land c_{in}\big) \lor (a \land b)$$

<p align="center"><img src="images/01_01_04_adder.png" width="420" alt="Full adder circuit made of two XOR gates, two AND gates and one OR gate"></p>

*Figure: full adder: two XORs give $s$; two ANDs and one OR give $c_{out}$. Each filled dot is a place where a wire splits in two (fan-out).*

**COPY / FAN-OUT** means splitting one wire into two. In a classical circuit this is trivial, but
**a quantum circuit has no equivalent COPY operation**, which we will meet again in Part 02 (no-cloning).

**Transistors.** At the physical level, 0 and 1 are just two voltage levels, $-v$ and $+v$. CMOS technology uses pairs of complementary
NMOS/PMOS transistors as switches: the voltage that turns one type ON turns the other OFF. A NOT gate needs 2 transistors:

<p align="center"><img src="images/01_01_06_not_wi_transistors.png" width="660" alt="NOT gate built from one PMOS transistor connected up to +v and one NMOS connected down to -v, redrawn as two switches"></p>

*Figure: a NOT gate (left) = one PMOS connected up to $+v$ and one NMOS connected down to $-v$ (middle) = two switches (right).*

When $v_{in} = +v$ (1), the NMOS conducts and the PMOS is off, so the output is connected to $-v$ (0); when $v_{in} = -v$ it is the other way round.
A NAND needs 4 transistors:

<p align="center"><img src="images/01_01_09_nand_wi_transistors.png" width="500" alt="NAND gate built from two parallel PMOS transistors connected up to +v and two series NMOS transistors connected down to -v"></p>

*Figure: a NAND from 4 transistors: two PMOS in parallel connected up to $+v$, two NMOS in series connected down to $-v$.*

AND = NAND in series with NOT, which makes 6 transistors.

### Key code

```python
x = 0b1101
print(x)
```
The `0b` prefix writes a binary number, but Python stores it as an `int` (printing `13`), so ordinary arithmetic works.

```python
b = bin(11) + bin(9)  # in decimal: 11 + 9 = 20
print(f'The result in b: {b} is not the correct representation for the number 20: {bin(20)}')
```
`bin()` returns a **string** (`str`), so `+` is string concatenation, not addition. To do arithmetic you must convert back
with `int(b, 2)`.

```python
n = 4  # number of bits to use
for i in range(2**3):
    b = bin(i)[2:].zfill(n)
    print(f'{i}: {b}')
```
`[2:]` drops the `0b` prefix; `zfill(n)` pads zeros on the left up to $n$ bits. A more compact equivalent:
`np.binary_repr(13, 5)` returns `'01101'`.

```python
a = 0b11010
b = 0b10110

c_and = np.binary_repr(a & b, 5)  # Bitwise AND: 11010 & 10110 = 10010
c_or = np.binary_repr(a | b, 5)   # Bitwise OR:  11010 | 10110 = 11110
c_xor = np.binary_repr(a ^ b, 5)  # Bitwise XOR: 11010 ^ 10110 = 01100
```
Python's bitwise operators: `&` (AND), `|` (OR), `^` (XOR).

> Note: Python's `and`/`or` are **logical** operators, not equivalent to `&`/`|` when applied to numbers with several bits.
> The notebook mistakenly says "`&` and `^`"; the correct counterpart of `or` is `|`.

### Results

| Code | Output |
|---|---|
| `0b1011 + 0b1001` | `20` |
| `bin(13)` | `0b1101` (type `str`) |
| `bin(11) + bin(9)` | `0b10110b1001`, wrong, whereas `bin(20)` is `0b10100` |
| `int('1101', 2)` | `13` |
| `np.binary_repr(13, 5)` | `01101` |
| AND / OR / XOR of `11010`, `10110` | `10010` / `11110` / `01100` |

### Quick recap

- $n$ bits represent $2^n$ values; the rightmost bit is $b_0$.
- `bin()` gives a string, `int(s, 2)` converts back to a number, `np.binary_repr(x, n)` gives a string of exactly $n$ bits.
- XOR = addition modulo 2, used very heavily throughout the book.
- Bitwise operators in Python: `&`, `|`, `^`; don't confuse them with `and`, `or`.
- Classical circuits can copy wires freely; quantum circuits cannot.

---

## 01_02 · Reversible computing

**Goal:** understand why AND/OR lose information, and how to build a reversible version of every gate using X, CX, CCX.

### Key concepts

**Why reversibility is needed.** If the output of an AND is 0, you cannot tell whether the input was 00, 01 or 10: information is lost.
Landauer (1961) showed that losing information is tied to energy dissipation; this gave rise to the model of reversible computation
(Bennett 1973, Toffoli 1980, Fredkin 1981). Quantum mechanics is reversible in principle, so the model of
quantum computation must be reversible too.

A gate is **reversible** when each input gives **exactly one** distinct output, so the input can always be recovered from the output.

From this lesson on, the NOT gate is drawn and called the **X** gate, following the notation of quantum circuits:

<p align="center"><img src="images/01_02_01_not_gates.png" width="660" alt="Three equivalent symbols of the NOT gate: classical, Feynman's, and the X box of a quantum circuit"></p>

*Figure: three ways to draw the same NOT gate: the classical symbol, Feynman's symbol (an X on the wire), and the X box used in quantum circuits.*

| Gate | Rule | Notes |
|---|---|---|
| **X** (NOT) | $a' = \bar a$ | Its own inverse: X·X = I |
| **CX** (controlled-X, CNOT) | $a' = a,\ b' = a \oplus b$ | Reversible XOR; with $b = 0$ it becomes **COPY** ($b' = a$) |
| **CCX** (Toffoli) | $a' = a,\ b' = b,\ c' = c \oplus (a \land b)$ | With $c = 0$ it gives **AND**; with $c = 1$ it gives **NAND** |

In the figures, the filled dot sits on the control wire and the X box sits on the target wire:

<p align="center"><img src="images/01_02_02_cx_gate.png" width="180" alt="CX gate: a filled dot on wire a connected down to an X box on wire b"></p>

*Figure: the CX gate: the upper wire $a$ is the control wire, the lower wire $b$ is the target wire.*

<p align="center"><img src="images/01_02_04_ccx_gate.png" width="180" alt="CCX gate: two filled dots on wires a and b connected down to an X box on wire c"></p>

*Figure: the CCX (Toffoli) gate: two control wires $a$, $b$ and the target wire $c$.*

**Reversible OR** uses De Morgan's law $a \lor b = \overline{\bar a \land \bar b}$: put an X on both inputs,
then use a CCX with $c = 1$ (that is, a NAND).

<p align="center"><img src="images/01_02_07_reversible_or.png" width="220" alt="Reversible OR circuit: X gates on wire a and wire b, then a CCX onto a third wire initialized to 1"></p>

*Figure: reversible OR: X on $a$ and $b$, then a CCX onto a third wire initialized to 1; $c' = a \lor b$.*

> Note: the notebook says "use two CCX to invert the inputs", but the code and the figure both use two **X** gates.

**Reversing a circuit** (uncompute) = applying **each gate in the opposite order**. For X, CX, CCX, applying them a second time
is enough, because each gate is its own inverse; but for a composite circuit you must reverse the order. For quantum circuits
there is an extra requirement involving complex numbers, which we will learn later.

<p align="center"><img src="images/01_02_08_reverse_ors.png" width="360" alt="Reversible OR circuit followed by its gates in the opposite order, with the outputs returning to a, b, 1"></p>

*Figure: the OR circuit (left half) followed by its gates in the opposite order (right half): the CCX first, then the two X gates; the outputs return to $a$, $b$, $1$.*

> Note: the notebook says that applying the whole OR circuit twice "happens to give the right answer" in this case. That is not correct:
> with $a = b$, applying it twice turns $c$ from 1 into 0, for example $(0,0,1) \to (1,1,0) \to (0,0,0)$. Only applying the gates in the
> opposite order (as in the figure above and the notebook's code) returns $(a, b, 1)$ for every input.

**The reversible full adder** is obtained by a one-to-one replacement of the classical version, and it needs extra **auxiliary wires** (also called ancillas)
initialized to fixed values. This is a very common feature of reversible and quantum circuits.

<p align="center"><img src="images/01_02_09_reversible_adder.png" width="760" alt="Classical full adder on the left and reversible version on the right, made of AND, XOR and OR blocks built from X, CX, CCX on six wires"></p>

*Figure: classical full adder (left) and reversible version (right): two CCX (AND) write into two auxiliary wires initialized to 0, two CX (XOR) bring $s$ out on the $c_{in}$ wire, and the OR block writes $c_{out}$ into an auxiliary wire initialized to 1.*

### Key code

```python
# define x gate as a function:
def x(a_in):
    a_out = a_in ^ 1   # Remember ^ performs the XOR operation. a^1 = a̅
    return a_out
```
The X gate is exactly XOR with 1.

```python
# define cx gate as a function:
def cx(a_in, b_in):
    
    # a' is always equal to a.
    a_out = a_in
    
    # if control is one (i.e., a == 1): negate target (b' = b̅), 
    # else: leave b alone (b' = b).
    if a_in == 1:                
        b_out = x(b_in)
    else:
        b_out = b_in

    return (a_out, b_out)
```
CX: the control wire stays unchanged, and the target wire is flipped when the control wire equals 1. The function `ccx(a_in, b_in, c_in)` is written similarly,
flipping $c$ only when `a_in == 1 and b_in == 1`.

```python
for a, b, c in inputs:
    a1, b1, d1 = ccx(a, b, 0)      # AND1
    a2, b2 = cx(a1, b1)            # XOR1
    a3, c3, e3 = ccx(b2, c, 0)     # AND2
    b4, s = cx(b2, c3)             # XOR2
    
    d5 = x(d1)                     # OR ...
    e5 = x(e3)                     # 
    d6, e6, cout = ccx(d5, e5, 1)  #
```
The full adder consists only of X, CX, CCX. Three auxiliary wires (two initialized to 0 for the ANDs, one initialized to 1 for the OR) are added
to compute $c_{out}$.

> Note: the comments in the code and the labels in the figure name the two ANDs the opposite way round: the code calls `ccx(a, b, 0)` AND1,
> while the figure calls the $a \land b$ block AND2 (and the $(a \oplus b) \land c_{in}$ block AND1). The circuit is the same.

### Results

- The CX truth table matches $b' = a \oplus b$ exactly; applying CX twice returns exactly $(a, b)$.
- CCX with $c = 0$ gives $c' = a \land b$; applying it twice returns $c = 0$.
- The reversible OR gives $c' = a \lor b$ (`0, 1, 1, 1`), while $a' = \bar a$, $b' = \bar b$ because the two X gates are still there;
  applying the gates in the opposite order returns $(a, b, 1)$.
- The reversible full adder gives exactly the $s$, $c_{out}$ table from lesson 01_01:

| a | b | cin | s | cout |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

(4 of the 8 rows shown)

### Quick recap

- Reversible = each input gives its own distinct output, so you can always recover the input.
- CX = reversible XOR; CX with the target wire at 0 = COPY.
- CCX with the target wire at 0 = AND, at 1 = NAND.
- OR = X on the two inputs + NAND.
- Reversing a circuit: apply the gates in the **opposite order**.
- Reversible circuits often need auxiliary wires (ancillas).

---

## 01_03 · Linear algebra for reversible circuits

**Goal:** represent bits with vectors, and gates and whole circuits with matrices, so that "running a circuit" is just matrix multiplication.
This is the most important lesson of Part 01.

### Key concepts

**Bits are vectors, written in Dirac (bra-ket) notation:**

$$|0\rangle = \begin{bmatrix}1\\0\end{bmatrix}, \qquad |1\rangle = \begin{bmatrix}0\\1\end{bmatrix}$$

<p align="center"><img src="images/01_03_01_light_switches.png" width="400" alt="The vector [1, 0] corresponds to bit 0: switch flipped up, light off; the vector [0, 1] corresponds to bit 1: switch flipped down, light on"></p>

*Figure: a memory aid: the 1 on top (switch flipped up, light off) is bit 0; the 1 at the bottom (switch flipped down, light on) is bit 1.*

A valid bit vector has entries in $\{0,1\}$ and length $\|b\| = 1$, which rules out $[0,0]^\top$ (length 0) and
$[1,1]^\top$ (length $\sqrt 2$).

The **bra** $\langle b|$ is a row vector (for now just the transpose of the ket). The **bra-ket** product $\langle a|b\rangle$ is the
inner product (dot product): $\langle b|b\rangle = 1$ and $\langle 0|1\rangle = 0$, so $|0\rangle$ and $|1\rangle$ are orthogonal.

**Gates are matrices:**

$$\text{X} = \begin{bmatrix}0&1\\1&0\end{bmatrix}, \qquad \text{X}|0\rangle = |1\rangle, \qquad \text{X}^{-1} = \text{X}$$

Reversing a gate really means multiplying by the **inverse matrix**. X "happens to" be its own inverse, so applying it a second time is enough.

**Several bits: the Kronecker product** $\otimes$.

$$|10\rangle = |1\rangle \otimes |0\rangle = \begin{bmatrix}0\\1\end{bmatrix} \otimes \begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}0\\0\\1\\0\end{bmatrix}$$

The rule to remember: the vector of a binary number $b$ has **a single 1 at the position equal to the decimal value of $b$**
(counting from 0, from the top), and 0 everywhere else. $n$ bits give a vector with $2^n$ dimensions. These vectors are orthogonal to each other and
form a **basis**; quantum states will later be linear combinations of them.

> Note: the notebook says the number of dimensions of $\vec x \otimes \vec y$ is the "sum" of the numbers of dimensions; it is actually the **product**
> ($2 \times 2 = 4$, and $n$ bits give $2^n$).

**The matrix of a multi-bit gate** is found by writing down the input → output mapping. For CX, the top bit $b_1$ is the
control bit and the bottom bit $b_0$ is the target bit: $00 \to 00$, $01 \to 01$, $10 \to 11$, $11 \to 10$.

<p align="center"><img src="images/01_03_07_cx_gate.png" width="180" alt="CX gate with control bit b1 on top and target bit b0 at the bottom"></p>

*Figure: CX with control bit $b_1$ (top) and target bit $b_0$ (bottom).*

$$\text{CX} = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}$$

Column $j$ (counting from 0) of the matrix is exactly the output vector when the input is $|j\rangle$, because multiplying the matrix by $|j\rangle$
picks out exactly that column.

> Note: the notebook says that multiplying CX by $|00\rangle$ gives the first **row** $(c_{00}, c_{01}, c_{02}, c_{03})$.
> It is actually the first **column** $(c_{00}, c_{10}, c_{20}, c_{30})$. The final CX matrix is still correct because it is symmetric.

CCX is the $8\times 8$ identity matrix with its last two rows swapped.

**The matrix of a whole circuit:**
- Gates in **the same layer** (in parallel): take the Kronecker product, for example an X on the bottom bit with the top bit left empty gives $I \otimes \text{X}$.

<p align="center"><img src="images/01_03_02_id_and_x.png" width="180" alt="Two-bit circuit: the top bit b1 has no gate, the bottom bit b0 goes through an X gate"></p>

*Figure: the top bit $b_1$ is left empty, the bottom bit $b_0$ goes through an X gate; the matrix is $I \otimes \text{X}$.*

- **Sequential** layers: multiply the matrices **from right to left**, because the layer applied first must multiply the vector first:

$$|b\rangle_{out} = Q_2\, Q_1\, |b\rangle_{in}$$

<p align="center"><img src="images/01_03_03_or_1.png" width="220" alt="Three-bit circuit split into two layers: layer 1 has X gates on b2 and b1, layer 2 has a CCX gate whose target is b0"></p>

*Figure: a 3-bit circuit split into two layers: layer 1 is $Q_1 = \text{X} \otimes \text{X} \otimes I$, layer 2 is $Q_2 = \text{CCX}$.*

- How you split the circuit into layers does not affect the result.

<p align="center"><img src="images/01_03_04_or_2.png" width="280" alt="The same three-bit circuit split into three layers: X on b2, then X on b1, then CCX"></p>

*Figure: the same circuit split into three layers: $Q = \text{CCX}\,(I \otimes \text{X} \otimes I)\,(\text{X} \otimes I \otimes I)$, giving the same matrix.*

**Special case:** a CX connecting two bits that are not adjacent, with an idle bit in between, cannot be written in the form
$I \otimes \text{CX}$ or $\text{CX} \otimes I$.

<p align="center"><img src="images/01_03_06_cx_with_idle.png" width="180" alt="Three-bit circuit: CX from the top bit b2 to the bottom bit b0, the middle bit b1 has no gate"></p>

*Figure: CX with control bit $b_2$ (top) and target bit $b_0$ (bottom); the middle bit $b_1$ is left empty.*

The way to handle it is to split the CX into a **sum** of Kronecker products using two projectors $\Pi_0 = |0\rangle\langle 0|$ and
$\Pi_1 = |1\rangle\langle 1|$:

$$\text{CX} = \Pi_0 \otimes I + \Pi_1 \otimes \text{X} \quad\Rightarrow\quad Q = \Pi_0 \otimes I \otimes I + \Pi_1 \otimes I \otimes \text{X}$$

**Three properties of the matrix of a reversible circuit:** it is square ($2^n \times 2^n$), invertible, and preserves vector length.
In this part every entry is still 0 or 1; lesson 01_04 will break that. In fact each such matrix is a
**permutation matrix**: each row and each column has exactly one 1, so it only rearranges the entries of the vector.

### Key code

```python
# Define |0⟩
ket_0 = np.array([[1],
                  [0]])
print(ket_0)
```
A ket is a NumPy array in **column** form (shape `(2, 1)`). `sp.Matrix(ket_0)` displays it nicely in LaTeX.

```python
# Multiply |0⟩ by X to get |1⟩:
ket_1 = X @ ket_0
sp.Matrix(ket_1)
```
Matrix multiplication uses `@` (or `np.matmul`).

> Note: in NumPy, `*` is **element-wise** multiplication (the Hadamard product, unrelated to the Hadamard gate in Part 02),
> not matrix multiplication. To multiply matrices, always use `@`.

```python
def bin_to_vec(b):
    # define |0⟩ and |1⟩ within the function:
    ket_0 = np.array([[1],[0]])
    ket_1 = np.array([[0],[1]])
    
    b_inv = b[::-1] # Reverse order of b. Like matrix mult,
                    # Kronecker prod is performed from right to left.
    
    # iterate over bits
    for i, bit in enumerate(b_inv):
        if bit == '0':
            b_i = ket_0
        else:
            b_i = ket_1

        # for first bit, we don't perform the product
        if i == 0:
            ket_b = b_i
        else:
            ket_b = np.kron(b_i,ket_b)
            
    return ket_b
```
Converts a binary string into a vector with `np.kron`, combining from the rightmost bit towards the left.

```python
# Compute circuit matrix
Q_1 = np.kron(X, np.kron(X, I))
Q_2 = CCX

Q = Q_2 @ Q_1
```
A two-layer circuit: layer 1 is $\text{X} \otimes \text{X} \otimes I$, layer 2 is CCX. The matrix of the whole circuit is $Q_2 Q_1$.

```python
# Compute Q for our circuit
Q = np.kron(Π0,np.kron(I,I)) + np.kron(Π1,np.kron(I,X))
```
CX between the top bit and the bottom bit, skipping the middle bit.

### Results

| Check | Output |
|---|---|
| Length of $\vert 0\rangle$, $\vert 1\rangle$ | `1.0`, `1.0` |
| Length of $[0,0]^\top$, $[1,1]^\top$ | `0.0`, `1.414…` (not valid) |
| `np.vdot`: $\langle 0\vert 0\rangle$, $\langle 0\vert 1\rangle$, $\langle 1\vert 0\rangle$, $\langle 1\vert 1\rangle$ | `1, 0, 0, 1` |
| `np.linalg.inv(X)` | equal to X (entries are printed as floats, `1.0`) |
| `bin_to_vec('10110')` | a 32-dimensional vector, with the 1 at position 22 |
| $Q_2 Q_1$ and $Q_3 Q_2 Q_1$ (two ways of splitting into layers) | the same matrix |
| $Q\,\vert 100\rangle$ with the CX jumping over the middle bit | $\vert 101\rangle$ (the 1 at position 5) |

### Quick recap

- $|0\rangle = [1, 0]^\top$, $|1\rangle = [0, 1]^\top$; $|b\rangle$ has its 1 at the position equal to the value of $b$.
- Parallel → `np.kron`; sequential → `@`, written **from right to left**.
- `@` is matrix multiplication, `*` is only element-wise multiplication.
- Reversing a gate = multiplying by the inverse matrix.
- A controlled gate that skips over bits: $\Pi_0 \otimes I \otimes \dots + \Pi_1 \otimes \dots \otimes \text{X}$.
- The matrix of a reversible circuit: square, invertible, length-preserving (it is a **permutation matrix**).

---

## 01_04 · Probabilistic computing

**Goal:** bring randomness into classical circuits with p-bits, and see clearly how they differ from the qubits you will learn about in Part 02.

### Key concepts

**A p-bit** (probability bit) is a probability vector:

$$\vec p = \begin{bmatrix}\varrho_0\\ \varrho_1\end{bmatrix}, \qquad \varrho_j \in [0,1], \qquad \varrho_0 + \varrho_1 = 1$$

$\varrho_j$ is the probability of **measuring** the value $j$. If you measure many times, the frequency $n_j / n$ approaches $\varrho_j$.
For example: a noisy NOT gate, with input 0, gives the output $[1/4, 3/4]^\top$.

<p align="center"><img src="images/01_04_03_noisy_not.png" width="560" alt="Noisy NOT gate: the input is not low enough to count as 0, and noise makes the output occasionally flip to 0; 3/4 of the time the output is 1, 1/4 of the time it is 0"></p>

*Figure: a noisy NOT gate: the input voltage is not low enough, and noise makes the output flip to 0 now and then; the output is 1 for 3/4 of the time and 0 for 1/4.*

**Difference from a qubit:** the **sum** of a p-bit's entries equals 1, so its Euclidean length varies
(for example $\|[1/4, 3/4]^\top\| \approx 0.79$). For a qubit, the **sum of the squared moduli** of the entries equals 1, so its length is always 1
(Part 02 will explain why the entries of a qubit can be complex numbers).

<p align="center"><img src="images/01_04_01_prob_vec_length.png" width="200" alt="Probability vector p in the rho0, rho1 plane, with the arrow tip lying on the dashed line segment joining (1,0) and (0,1)"></p>

*Figure: the tip of the probability vector $\vec p$ always lies on the dashed line segment $\varrho_0 + \varrho_1 = 1$, so its length varies.*

<p align="center"><img src="images/01_04_02_prob_amps_vec_length.png" width="200" alt="Qubit vector q in the q0, q1 plane, with the arrow tip lying on a dashed circular arc of radius 1"></p>

*Figure: with $q_0, q_1 \in [0,1]$, the tip of the qubit vector $\vert q\rangle$ lies on the dashed circular arc of radius 1, so its length is always 1.*

**A noisy (non-deterministic) probabilistic gate cannot be reversed physically**, even though its matrix may have an inverse mathematically.
The noisy NOT gate above has the matrix

$$P = \begin{bmatrix}\tfrac14 & 1\\ \tfrac34 & 0\end{bmatrix}, \qquad P^{-1} = \begin{bmatrix}0 & \tfrac43\\ 1 & -\tfrac13\end{bmatrix}$$

$P^{-1}$ has a negative entry (and an entry $\tfrac43 > 1$), so it is not a probability matrix: noise **cannot be "undone"**
by another probabilistic gate. By contrast, the matrix of a quantum circuit is always invertible.

**Deterministic gates still work on p-bits.** X swaps the order of the probabilities: $\text{X}[\varrho_0, \varrho_1]^\top = [\varrho_1, \varrho_0]^\top$.

<p align="center"><img src="images/01_04_04_pbit_thru_x_gate.png" width="440" alt="A sequence of random 0 and 1 values passing through an X gate and coming out as the inverted sequence"></p>

*Figure: a sequence of random values passing through an X gate comes out as the inverted sequence, so the probabilities of 0 and 1 swap places.*

**Several p-bits.** The vector of **statistically independent** p-bits is still a Kronecker product; the matrix of gates acting
separately on each p-bit is also a Kronecker product:

$$\begin{bmatrix}\tfrac23\\ \tfrac13\end{bmatrix} \otimes \begin{bmatrix}\tfrac14\\ \tfrac34\end{bmatrix}
= \begin{bmatrix}\tfrac16\\ \tfrac12\\ \tfrac1{12}\\ \tfrac14\end{bmatrix}
\quad\text{(probabilities of } 00, 01, 10, 11\text{)}$$

When the result on one p-bit depends on the state of another p-bit, the matrix **cannot be separated** into a Kronecker product.
For example: leave $\vec p_0$ unchanged if $\vec p_1 = 0$, but if $\vec p_1 = 1$ then randomize $\vec p_0$:

$$P = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&\tfrac12&\tfrac12\\0&0&\tfrac12&\tfrac12\end{bmatrix}$$

> Note: the notebook calls this particular kind of non-separable matrix a **stochastic matrix**.
> In fact a stochastic matrix is any matrix with non-negative entries and with each column summing to 1 (with the book's column-vector
> convention), that is, a matrix that turns a probability vector into a probability vector. The noisy NOT matrix above, X, and even $R \otimes \text{X}$
> in the Key code section are all stochastic matrices. Whether a matrix can be separated into a Kronecker product is a different property.

**A reversible deterministic circuit is a permutation matrix:** it only swaps the probabilities around, so multiplying by $Q^{-1}$ puts them
back in their original positions. For example the circuit $Q = (\text{X} \otimes I)\,\text{CX}$ in the notebook:

<p align="center"><img src="images/01_04_05_pbit_thru_circuit.png" width="220" alt="Two-p-bit circuit: a CX with p1 as the control and p0 as the target, followed by an X gate on p1"></p>

*Figure: CX ($\vec p_1$ is the control, $\vec p_0$ is the target) then X on $\vec p_1$; the matrix is $Q = (\text{X} \otimes I)\,\text{CX}$.*

### Key code

```python
n_samps = 200                   # number of samples
vals = [0, 1]                   # Possible outcomes: 0 or 1
probs = (vec_p).reshape(-1)     # Flatten to 1D array with probabilities for 0 and 1

# sample 0 or 1 a 100 times using probabilities from p̅
samples = np.random.choice(vals, size=n_samps, p=probs)
print(samples)
```
Simulates measuring a p-bit with `np.random.choice`, with the probabilities taken from the vector.

> Note: the code sets no seed, so the samples and frequencies of each run will differ from the saved output. The comment says
> "100 times" but `n_samps = 200`.

```python
X = np.array([[0,1],
              [1,0]])
R = np.array([[1/2,1/2],
              [1/2,1/2]])

P = np.kron(R, X)
```
Two independent p-bits: X (deterministic) on $\vec p_0$, R (always gives 0/1 with probability 1/2) on $\vec p_1$.

```python
# define general input probability vector
ϱ0, ϱ1, ϱ2, ϱ3 = sp.symbols('ϱ0, ϱ1, ϱ2, ϱ3')
p_in = sp.Matrix([ϱ0, ϱ1, ϱ2, ϱ3])
```
Uses SymPy symbolic variables to see how the circuit $Q = (\text{X} \otimes I)\,\text{CX}$ permutes the probabilities.
Afterwards `Q.inv() @ p_int` puts them back where they were.

### Results

| Check | Output |
|---|---|
| 200 samples from $[1/4, 3/4]$ | frequency of 0 is `0.27`, frequency of 1 is `0.73` |
| $P = R \otimes \text{X}$ applied to $\vert 00\rangle$ | $[0, 0.5, 0, 0.5]$: $\vec p_0$ is always 1, $\vec p_1$ is 0 or 1 with probability 1/2 each |
| $P$ applied to $\vec p_1 \otimes \vec p_0$ with $\vec p_0 = [2/3, 1/3]$, $\vec p_1 = [1/10, 9/10]$ | $[0.1667, 0.3333, 0.1667, 0.3333]$ |
| The non-separable $4 \times 4$ matrix above, applied to $\vert 10\rangle$ | $[0, 0, 0.5, 0.5]$ |
| $Q\,[\varrho_0, \varrho_1, \varrho_2, \varrho_3]^\top$ | $[\varrho_3, \varrho_2, \varrho_0, \varrho_1]^\top$; multiplying by $Q^{-1}$ next gives back the original order |

### Quick recap

- p-bit: entries in $[0,1]$, their **sum** equals 1. Qubit: the **sum of the squared moduli** equals 1.
- Noise cannot be reversed: $P^{-1}$ has negative entries.
- Independent p-bits → Kronecker product; a gate that makes one p-bit depend on another → a non-separable matrix.
- Every matrix that turns a probability vector into a probability vector is a stochastic matrix, whether or not it can be separated.
- A reversible deterministic circuit = a permutation matrix, which holds for p-bits too.

---

## API summary for this part

| API / function | Used for | Lesson |
|---|---|---|
| `0b1101`, `bin(x)`, `int(s, 2)` | Writing binary numbers, converting between numbers and binary strings | 01_01 |
| `str.zfill(n)`, `np.binary_repr(x, n)` | A binary string of exactly $n$ bits | 01_01 |
| `&`, `\|`, `^` | Bitwise AND, OR, XOR | 01_01, 01_02 |
| `np.array([[1],[0]])` | Column vector (ket) | 01_03, 01_04 |
| `@`, `np.matmul` | Matrix multiplication | 01_03, 01_04 |
| `np.kron` | Kronecker product (combining bits, combining gates in parallel) | 01_03, 01_04 |
| `np.vdot` | Inner product | 01_03 |
| `np.linalg.inv` | Inverse matrix | 01_03 |
| `np.eye(n)` | Identity matrix | 01_03 |
| `np.where(v == 1)` | Find the position of the 1 in a vector | 01_03 |
| `np.random.choice(vals, size, p)` | Sample according to given probabilities | 01_04 |
| `sp.Matrix`, `.evalf(n)`, `.inv()` | Display/compute matrices with SymPy | 01_03, 01_04 |
| `sp.symbols` | Symbolic variables | 01_04 |
| `plt.hist` | Plot a histogram of measurement outcomes | 01_04 |

## How to run

Open the notebooks in VS Code or Jupyter, choose the repo's `.venv` kernel, and run from top to bottom. The libraries you need are listed
in [requirements.txt](../../requirements.txt); this part only uses NumPy, SymPy, Matplotlib.

- The notebooks are independent of each other, but within each notebook, later cells use variables from earlier cells
  (for example `X`, `I`, `bin_to_vec` in 01_03), so they must be run in order.
- 01_04 samples randomly without a seed, so the sampled numbers will differ from the saved output. Matrix multiplications always give the same result.

---

<!-- nav -->
[← 00 · Getting started](../00_getting_started/README.en.md) · [Contents](../../README.en.md#contents) · [02 · Quantum computing →](../02_quantum_computing/README.en.md)
