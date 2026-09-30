# 04 · Foundational quantum algorithms (Các thuật toán lượng tử nền tảng)

Bốn thuật toán kinh điển cho thấy máy lượng tử vượt máy cổ điển ở đâu: **Deutsch–Jozsa**, **Bernstein–Vazirani**,
**Simon** và **Grover**. Cả bốn dùng chung một khuôn: đưa đầu vào về chồng chập bằng Hadamard, gọi **oracle** $U_f$
(hộp đen chứa bài toán), rồi dùng **giao thoa** (interference) để kết quả cần tìm nổi lên khi đo. Thước đo so sánh
là **số lần truy vấn oracle** (query complexity).

> Nguồn: [04_01](https://learnquantum.io/chapters/04_quantum_algorithms/04_01_deutsch-jozsa.html) ·
> [04_02](https://learnquantum.io/chapters/04_quantum_algorithms/04_02_bernstein-vazirani.html) ·
> [04_03](https://learnquantum.io/chapters/04_quantum_algorithms/04_03_simons.html) ·
> [04_04](https://learnquantum.io/chapters/04_quantum_algorithms/04_04_grover.html)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

**Cần nắm trước** (bài [02_05](../02_quantum_computing/README.md#02_05--quantum-building-blocks-các-khối-dựng-lượng-tử)):
oracle $U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$, phase kickback
$|x\rangle|-\rangle \to (-1)^{f(x)}|x\rangle|-\rangle$, và biến đổi Hadamard
$H^{\otimes n}|x\rangle = \frac{1}{\sqrt N}\sum_z (-1)^{x\cdot z}|z\rangle$.

## Mục lục

| Bài | Notebook | Web | Bài toán | Số lần gọi oracle (cổ điển → lượng tử) |
|---|---|---|---|---|
| 04_01 · Deutsch–Jozsa | [04_01_deutsch-jozsa.ipynb](04_01_deutsch-jozsa.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_01_deutsch-jozsa.html) | $f$ là hằng hay cân bằng? | $2^{n-1} + 1$ (chắc chắn) → **1** |
| 04_02 · Bernstein–Vazirani | [04_02_bernstein-vazirani.ipynb](04_02_bernstein-vazirani.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_02_bernstein-vazirani.html) | Tìm $s$ với $f(x) = s\cdot x$ | $n$ → **1** |
| 04_03 · Simon | [04_03_simons.ipynb](04_03_simons.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_03_simons.html) | Tìm $s$ với $f(x) = f(x \oplus s)$ | $\sim 2^{n/2}$ → $\sim n$ (tăng tốc **hàm mũ**) |
| 04_04 · Grover | [04_04_grover.ipynb](04_04_grover.ipynb) | [link](https://learnquantum.io/chapters/04_quantum_algorithms/04_04_grover.html) | Tìm $x$ với $f(x) = 1$ (tìm kiếm không cấu trúc) | $\sim N$ → $\sim\sqrt N$ (tăng tốc **bậc hai**) |

---

## 04_01 · Deutsch–Jozsa algorithm (Thuật toán Deutsch–Jozsa)

**Bài toán.** Cho oracle $U_f$ của hàm $f:\{0,1\}^n \to \{0,1\}$ và được **hứa** (promise) rằng $f$ hoặc **hằng**
(luôn 0 hoặc luôn 1), hoặc **cân bằng** (một nửa đầu vào cho 0, nửa còn lại cho 1). Xác định $f$ thuộc loại nào.

### Kiến thức chính

**Trường hợp $n = 1$ (thuật toán Deutsch).** Có 4 hàm: $f = 0$, $f = 1$ (hằng), $f = x$, $f = \bar x$ (cân bằng).
Cổ điển, một lần hỏi chỉ đoán đúng 50%, vì mỗi đầu vào luôn ra trùng với một hàm hằng và một hàm cân bằng; cần 2 lần
mới chắc chắn. Lượng tử: bọc hộp đen bằng H. Với hàm hằng, hai lớp H triệt tiêu nhau; với CX, H–CX–H **đảo chiều**
điều khiển (phase kickback), nên qubit trên bị lật.

Các bước ($q_1$ là $x$, $q_0$ là $y$):

$$|0\rangle|0\rangle \xrightarrow{X \text{ lên } y} |0\rangle|1\rangle \xrightarrow{H\otimes H} |+\rangle|-\rangle
\xrightarrow{U_f} \tfrac{(-1)^{f(0)}}{\sqrt2}\big(|0\rangle + (-1)^{f(0)\oplus f(1)}|1\rangle\big)|-\rangle
\xrightarrow{H\otimes H} \pm|f(0)\oplus f(1)\rangle|1\rangle$$

Đo qubit trên ra 0 thì $f$ hằng, ra 1 thì $f$ cân bằng. Chỉ cần **1 lần gọi**, kết quả tất định.

**Tổng quát $n$ bit.**
- **Cổ điển:** muốn chắc chắn thì trong trường hợp xấu nhất phải thử $2^n/2 + 1$ đầu vào. Nếu chấp nhận đoán theo xác suất,
  sau $r$ lần thử ngẫu nhiên thì $\mathbb{P}_\text{success} = 1 - 1/2^r$, nhưng vẫn chỉ là đoán.
- **Lượng tử:** cùng mạch, thay H bằng $H^{\otimes n}$:

$$|\psi\rangle_3 = \Big(\frac{1}{\sqrt N}\sum_x (-1)^{f(x)}|x\rangle\Big)|-\rangle$$

  - $f$ **hằng:** $(-1)^{f(x)}$ là pha toàn cục; $H^{\otimes n}$ lần hai đưa về $|0\rangle^{\otimes n}$.
  - $f$ **cân bằng:** biên độ của $|0\rangle^{\otimes n}$ là $\frac1N\sum_x(-1)^{f(x)} = 0$ vì số hạng dương và âm triệt tiêu,
    nên **không bao giờ** đo được toàn 0.

**Luật đọc kết quả:** đo được toàn 0 thì $f$ hằng; kết quả khác thì $f$ cân bằng.

**Dựng oracle:**

| Loại hàm | Mạch |
|---|---|
| Hằng $f = 1$ | Một cổng X lên qubit $y$ (hằng $f = 0$: không làm gì) |
| Cân bằng, parity | CX từ mọi qubit $x_i$ sang $y$; DJ luôn cho kết quả $11\dots1$ |
| Cân bằng, chia đôi | MCX cho nửa đầu (hoặc nửa sau) các giá trị $x$ |
| Cân bằng ngẫu nhiên | MCX với `ctrl_state` là $N/2$ giá trị $x$ chọn ngẫu nhiên |

### Code chính

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
Thuật toán Deutsch. `qc.append(sub_circuit, qubits)` gắn hộp đen vào mạch.

> Lưu ý: hàm `black_box()` dùng `np.random.randint(1,3)`, mà `randint` loại trừ cận trên, nên chỉ sinh ra mạch 1 hoặc 2
> (**chỉ hàm hằng**). Muốn đủ 4 mạch như comment ghi thì phải là `np.random.randint(1,5)`. Vì vậy hai biểu đồ
> đúng/sai của mục 1.1 trong output không phản ánh đúng bài toán đầy đủ.

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
Oracle $n$ bit: hàm hằng là mạch rỗng ($f = 0$); hàm cân bằng là $N/2$ cổng MCX, mỗi cổng lật $y$ tại một giá trị $x$.
`qubit 0` là $y$, các qubit $1..n$ là $x$.

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
Mạch Deutsch–Jozsa hoàn chỉnh. Mô phỏng cổ điển dùng `qc.prepare_state(k, qubits)` để nạp đầu vào $|k\rangle$.

### Kết quả

| Kiểm tra | Output |
|---|---|
| Statevector cuối cho $f = 0,\ 1,\ x,\ \bar x$ | $\|01\rangle,\ -\|01\rangle,\ \|11\rangle,\ -\|11\rangle$: qubit trên là 0 với hàm hằng, 1 với hàm cân bằng |
| Oracle hằng $f = 1$ (X lên $y$) | mọi $\|x\rangle\|0\rangle \to \|x\rangle\|1\rangle$ |
| Oracle parity, 3 bit | $f(x)$ = parity của $x$ (ví dụ $011 \to 0$, $111 \to 1$) |
| DJ với parity | luôn ra $111$ |
| DJ với các hàm cân bằng khác | không bao giờ ra $000$ |
| Mô phỏng $n = 4$, 100 lần | cổ điển khoảng 50% số lần cần $2^n/2 + 1 = 9$ lần thử; DJ luôn 1 lần (biểu đồ) |

### Ghi nhớ nhanh

- Mạch: X lên $y$ → H mọi qubit → $U_f$ → H mọi qubit → đo $x$.
- Toàn 0 thì hằng, khác 0 thì cân bằng; 1 lần gọi, tất định.
- Cơ chế: kickback đưa $(-1)^{f(x)}$ vào biên độ; $H^{\otimes n}$ cộng các dấu lại, nên biên độ của $|0\dots0\rangle$ bằng 0 khi cân bằng.
- Cổ điển chắc chắn cần $2^{n-1} + 1$ lần gọi (trường hợp xấu nhất).

---

## 04_02 · Bernstein–Vazirani algorithm (Thuật toán Bernstein–Vazirani)

**Bài toán.** Cho oracle của $f(x) = s \cdot x = s_0x_0 \oplus s_1x_1 \oplus \dots \oplus s_{n-1}x_{n-1}$ (tích vô hướng
nhị phân). Tìm chuỗi bí mật $s$ có $n$ bit.

### Kiến thức chính

**Cổ điển: cần đúng $n$ lần gọi.** Dùng các đầu vào chỉ có một bit 1, $x = 0\dots01,\ 0\dots10,\ \dots$. Mỗi lần như vậy
$f(x) = s_i$, tức "mặt nạ" lấy ra từng bit của $s$.

**Lượng tử: 1 lần gọi**, mạch **giống hệt Deutsch–Jozsa**, chỉ khác oracle:

$$|\psi\rangle_3 = \Big(\frac{1}{\sqrt N}\sum_x (-1)^{s\cdot x}|x\rangle\Big)|-\rangle = \big(H^{\otimes n}|s\rangle\big)|-\rangle$$

Biểu thức trong ngoặc chính là $H^{\otimes n}|s\rangle$. Áp $H^{\otimes n}$ thêm lần nữa (H tự là nghịch đảo của nó) ra
đúng $|s\rangle$, và đo được $s$ với xác suất 100%.

**Dựng oracle:** đặt một CX từ mỗi qubit $x_i$ có $s_i = 1$ sang qubit $y$. Như vậy $y \oplus \bigoplus_{i: s_i=1} x_i = y \oplus s\cdot x$.

### Code chính

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
Oracle cho $s$ ngẫu nhiên. `reversed(s)` vì bit phải nhất của chuỗi là $s_0$ (ứng với qubit 1);
`qc.cx(list_c, list_t)` đặt nhiều CX cùng lúc.

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
Cách cổ điển: $n$ lần chạy với $x = 2^i$, mỗi lần lấy được một bit của $s$.

```python
qc, s = bernstein_vazirani(n)
qc_t = transpile(qc, simulator)
job = simulator.run(qc_t, shots=1, memory=True)  # Run simulation once
s_out = job.result().get_memory()[0]
```
Cách lượng tử: **1 shot** là đọc được $s$. `bernstein_vazirani(n)` có cùng cấu trúc với `deutsch_josza(n)`.

### Kết quả

| Kiểm tra | Output |
|---|---|
| Bảng $f(x)$ với $s = 1101$ | các dòng $x$ có một bit 1 (đánh dấu ←) cho đúng $s_i$ |
| Cổ điển, $n = 3$ | `secret string: 011`, `extracted string: 011` (3 lần gọi) |
| Lượng tử, $n = 4$ | `secret string: 1000`, `extracted string: 1000` (1 lần gọi) |
| Oracle cho $s = 1011$ | $f(x) = s\cdot x$ đúng với cả 16 giá trị $x$ |

### Ghi nhớ nhanh

- Mạch giống hệt DJ; oracle là các CX từ những $x_i$ có $s_i = 1$.
- $\sum_x (-1)^{s\cdot x}|x\rangle = H^{\otimes n}|s\rangle$, nên thêm $H^{\otimes n}$ là ra $|s\rangle$.
- $n$ lần gọi cổ điển → 1 lần gọi lượng tử.

---

## 04_03 · Simon's algorithm (Thuật toán Simon)

**Bài toán.** Cho oracle của $f:\{0,1\}^n \to \{0,1\}^n$, được hứa rằng $f(x) = f(x \oplus s)$ với một chuỗi $s \neq 0$
(tức $f$ là hàm **hai-một**: mỗi giá trị đầu ra đến từ đúng một cặp $\{x, x\oplus s\}$). Tìm $s$.

Đây là thuật toán đầu tiên có tăng tốc **hàm mũ** so với cổ điển, và là tiền thân trực tiếp của thuật toán Shor.

### Kiến thức chính

**Cổ điển.** Thử các $x$ đến khi gặp hai đầu vào $a, b$ có $f(a) = f(b)$, khi đó $s = a \oplus b$. Giống bài toán ngày
sinh (birthday paradox):

$$\mathbb{P}_\text{success} = 1 - \prod_{k=0}^{r-1}\frac{2^n - 2k}{2^n - k}$$

Cần khoảng $2^{n/2}$ lần để thành công quá 50%, tức tăng theo **hàm mũ** của $n$ (trường hợp xấu nhất $2^{n-1} + 1$).

**Mạch lượng tử** (khác DJ/BV: thanh ghi dưới có $n$ qubit, khởi tạo $|0\rangle^{\otimes n}$, **không** dùng kickback):

1. $H^{\otimes n}$ lên thanh ghi $x$: $\frac{1}{\sqrt N}\sum_x |x\rangle|0\rangle$.
2. $U_f$: $\frac{1}{\sqrt N}\sum_x |x\rangle|f(x)\rangle = \frac{1}{\sqrt N}\sum_{x\in S}\big(|x\rangle + |x\oplus s\rangle\big)|f(x)\rangle$.
3. **Đo thanh ghi dưới**, ra một giá trị $f(a)$. Thanh ghi trên chỉ còn $\frac{1}{\sqrt2}\big(|a\rangle + |a\oplus s\rangle\big)$.
4. $H^{\otimes n}$ lên thanh ghi trên:

$$\frac{1}{\sqrt{2N}}\sum_z (-1)^{a\cdot z}\big[1 + (-1)^{s\cdot z}\big]|z\rangle$$

   Các $z$ có $s\cdot z = 1$ triệt tiêu; chỉ còn các $z$ thoả **$s \cdot z = 0$**, bất kể $a$ là gì.
5. Đo thanh ghi trên, được một $z$ thoả $s\cdot z = 0$. Ra $z = 0$ (xác suất $2/N$) thì vô ích, phải chạy lại.

**Hậu xử lý cổ điển.** Mỗi $z$ cho một phương trình tuyến tính modulo 2. Cần $n-1$ phương trình **độc lập tuyến tính**:

$$Z\vec s = \vec 0 \pmod 2 \quad\Rightarrow\quad \vec s = \text{kernel}(Z)$$

Quy trình lai lượng tử–cổ điển:
1. Chạy mạch lấy $z$.
2. Bỏ nếu $z = 0$ hoặc $z$ phụ thuộc tuyến tính vào các $z$ đã có (khử Gauss modulo 2).
3. Lặp đến khi có $n-1$ vector cơ sở.
4. Giải kernel (dạng bậc thang rút gọn RREF, rồi thế ngược) ra $s$.

Số lần chạy trung bình chỉ tăng **tuyến tính** theo $n$.

**Ví dụ trong notebook ($s = 1010$).** Các $z$ có thể là $\{0000, 0001, 0100, 0101, 1010, 1011, 1110, 1111\}$.
- $z = 0001$ cho $s_0 = 0$.
- $z = 1010$ cho $s_3 \oplus s_1 = 0$.
- $z = 1011$ phụ thuộc tuyến tính vào hai $z$ trước, nên bỏ.
- $z = 1110$ cho $s_2 = 0$.

Vì $s \neq 0$ nên $s = 1010$.

**Dựng oracle từ bảng chân trị.**
- Cách ngây thơ: mỗi bit $f(x)_i$ viết dạng tổng các tích (DNF), mỗi tích là một MCX. Mạch rất dài.
- Cách gọn: rút gọn biểu thức bằng `sympy.logic.boolalg.SOPform`, ví dụ $(\bar x_2 x_1 x_0) \lor (x_2 x_1 x_0) = x_1 \land x_0$,
  rồi dựng mạch bằng `BitFlipOracleGate`. Transpiler của Qiskit không tự rút gọn được việc này.

### Code chính

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
Sinh ngẫu nhiên một hàm Simon hợp lệ: mỗi cặp $\{x, x\oplus s\}$ nhận chung một giá trị đầu ra.

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
Thanh ghi $x$ là các qubit $n..2n-1$, thanh ghi $f(x)$ là các qubit $0..n-1$. Chuỗi `memory` in bit cao trước, nên
`z_and_fx[0:n]` là $z$.

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
Khử Gauss modulo 2 trên số nguyên: mỗi vector là một `int`, phép cộng là `^` (XOR), còn `b & -b` tách ra bit 1 thấp nhất
(pivot). Hàm `kernel_from_basis(basis, n)` cho các biến tự do bằng 1 và giải các biến pivot để ra $s$.

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
Vòng lặp lai: chạy mạch, lọc $z$, cập nhật cơ sở đến khi đủ $n-1$ vector, rồi giải kernel.

```python
expr = SOPform(x_symbs, fx_0)
...
qc_bool.append(BitFlipOracleGate(fx_expr, x_vars), x_qubits)
```
Rút gọn biểu thức Boolean bằng SymPy, rồi `BitFlipOracleGate` (trong `qiskit.circuit.library`) dựng oracle từ chuỗi
biểu thức. `qc.decompose()` để xem mạch bên trong.

### Kết quả

| Kiểm tra | Output |
|---|---|
| `fx_simon` với $s = 1101$ | ví dụ $f(0000) = f(1101) = 1011$ |
| Oracle, $n = 3$, $s = 100$ | $f(x) = f(x \oplus 100)$ với mọi $x$ |
| Cổ điển, $n = 7$ | `secret 1101000`, tìm được sau `22` lần thử |
| Lượng tử, $n = 7$ | `secret 0111110`, tìm được sau `6` lần chạy mạch |
| Biểu đồ trong notebook, $n = 7$ | lượng tử vượt 50% ở $r = 7$; cổ điển cần $r = 14$ |
| `SOPform` cho $f(x)_0$ | $x_0 \land x_1$ |

### Ghi nhớ nhanh

- Hứa: $f(x) = f(x\oplus s)$, hàm hai-một; tìm $s$.
- Mạch: H lên $x$ → $U_f$ → đo $f(x)$ → H lên $x$ → đo $x$ được một $z$ với $s\cdot z = 0$.
- Cần $n-1$ giá trị $z$ độc lập tuyến tính, rồi giải kernel modulo 2 (khử Gauss bằng XOR).
- Cổ điển $\sim 2^{n/2}$ lần, lượng tử $\sim n$ lần: tăng tốc **hàm mũ**.
- Là thuật toán lai: phần lượng tử lấy mẫu, phần cổ điển giải hệ phương trình.

---

## 04_04 · Grover's algorithm (Thuật toán Grover)

**Bài toán.** Tìm kiếm không cấu trúc (unstructured search): cho oracle của $f:\{0,1\}^n \to \{0,1\}$, tìm các đầu vào
$x$ có $f(x) = 1$ (**phần tử được đánh dấu**, marked element). $N = 2^n$.

> Ví dụ "tra danh bạ theo số điện thoại" chỉ để minh hoạ. Muốn dựng oracle cho danh bạ thì phải duyệt hết danh bạ trước,
> nên Grover chỉ có ích khi $f$ **dựng được hiệu quả** thành mạch, ví dụ bài toán thoả mãn mạch (circuit satisfiability).

### Kiến thức chính

**Cổ điển.** Thử lần lượt từng phần tử: $\mathbb{P}_\text{success} = r/2^n$, nên cần $2^{n-1}$ lần để đạt 50% và $N$ lần để
chắc chắn. Tức tăng tuyến tính theo $N$.

**Ý tưởng lượng tử: khuếch đại biên độ** (amplitude amplification). Lặp $\kappa$ lần cặp (oracle, diffuser):
1. $H^{\otimes n}$: mọi biên độ bằng $1/\sqrt N$ (trạng thái $|s\rangle$).
2. **Oracle** $U_f$ với $y = |-\rangle$: **đảo dấu** biên độ của phần tử đánh dấu.
3. **Diffuser** $V$: **lật mọi biên độ quanh giá trị trung bình** $\mu$: $\alpha_x \to 2\mu - \alpha_x$.
   Biên độ đánh dấu (đang âm, nằm xa dưới $\mu$) bị bật lên cao; các biên độ khác giảm nhẹ.

Ví dụ $n = 3$, $m = 101$:

| Bước | Biên độ của $m$ | Xác suất đo được $m$ |
|---|---|---|
| Sau H | 0.354 | 12.5% |
| Sau 1 vòng (oracle + diffuser) | $\frac{1}{\sqrt8}\cdot\frac{3\cdot8-4}{8} \approx 0.884$ | ≈ 78% |
| Sau 2 vòng | $\approx 0.972$ | ≈ 94.5% |
| Thêm vòng thứ 3 | giảm | giảm, vì xác suất **dao động tuần hoàn** chứ không tăng mãi |

**Mạch của diffuser.**

$$V = 2|s\rangle\langle s| - I = H^{\otimes n}\big(2|0\rangle\langle 0| - I\big)H^{\otimes n} = H^{\otimes n}X^{\otimes n}\,\text{MCZ}\,X^{\otimes n}H^{\otimes n}$$

$2|0\rangle\langle0| - I$ bằng (sai khác pha toàn cục $-1$) một cổng đảo dấu **chỉ** trạng thái $|0\dots0\rangle$,
tức MCZ kẹp giữa hai lớp X.

**Góc nhìn hình học → số vòng lặp.** Tách $|s\rangle = \cos\frac\theta2|m^\perp\rangle + \sin\frac\theta2|m\rangle$, với
$\sin\frac\theta2 = 1/\sqrt N$. Oracle là phép phản xạ qua $|m^\perp\rangle$; diffuser là phép phản xạ qua $|s\rangle$.
Hai phản xạ ghép lại thành **phép quay một góc $\theta$** về phía $|m\rangle$. Muốn tới $\pi/2$ thì
$\kappa\theta + \theta/2 = \pi/2$:

$$\kappa = \left\lfloor \frac{\pi}{4\arcsin(1/\sqrt N)} - \frac12 \right\rceil \;\approx\; \frac{\pi}{4}\sqrt N$$

Với $M$ phần tử đánh dấu, thay $1/\sqrt N$ bằng $\sqrt{M/N}$.

**Kiểm tra kết quả.** Chạy Grover một lần được $x_\text{out}$, rồi gọi $f(x_\text{out})$ để kiểm tra; sai thì chạy lại.
Tổng cộng tối thiểu $\kappa + 1$ lần gọi oracle. Với $N = 32$: gần 100% sau $\kappa + 1 = 5$ lần gọi, so với 32 lần cho cổ điển.

### Code chính

```python
def Uf_one_marked(n):
    N = 2**n
    m_int = np.random.randint(N)
    m = np.binary_repr(m_int,n)
    
    qc_bb = QuantumCircuit(n+1, name=' $U_f$ (Oracle)')
    qc_bb.mcx(list(range(1,n+1)),0, ctrl_state=m)
    
    return qc_bb, m
```
Oracle đánh dấu một phần tử: một MCX chỉ kích hoạt khi $x = m$.

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
Diffuser $V = H\,X\,\text{MCZ}\,X\,H$. `ZGate().control(n-1)` tạo MCZ trên $n$ qubit.

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
Mạch Grover đầy đủ: qubit 0 ở $|-\rangle$ để kickback, lặp $\kappa$ lần (oracle, diffuser), rồi đo.

```python
κ = round(np.pi/(4*np.arcsin(1/np.sqrt(N)))-1/2)
```
Số vòng lặp tối ưu. Notebook còn có `find_κ(N)` tính lặp theo công thức $2\mu - \alpha$ và ra cùng kết quả.

> Lưu ý: `Uf_M_marked(n, M)` chọn phần tử bằng `np.random.randint(N, size=M)` nên **có thể trùng**. Output lưu sẵn
> thực sự ra `['001', '001']`: hai MCX giống nhau triệt tiêu, và oracle không đánh dấu gì cả. Nên dùng
> `np.random.choice(N, size=M, replace=False)`.

> Lưu ý nhỏ: ở mục 2.2, $|m^\perp\rangle$ viết là $\sum_{x \neq 0}$, đúng ra là $\sum_{x \neq m}$ (và cần chuẩn hoá).
> Ở mục 1, dòng in `found after: {x_in} tries` in ra **chỉ số** $x$, nên số lần thử thật là `x_in + 1`.

### Kết quả

| Kiểm tra | Output |
|---|---|
| `find_κ(32)` và công thức đóng | cùng ra $\kappa = 4$ |
| Tìm cổ điển, $n = 5$ | `marked element: 01101`, tìm thấy ở chỉ số 13 (lần thử thứ 14) trên 32 |
| Grover $n = 3$, $\kappa = 2$, $2^{13}$ shot | `m = 110` là kết quả xuất hiện nhiều nhất (biểu đồ) |
| Grover $M = 2$, $n = 5$ | `['00010', '11100']` là hai kết quả nổi bật (biểu đồ) |

### Ghi nhớ nhanh

- Một vòng Grover = oracle (đảo dấu phần tử đánh dấu) + diffuser (lật quanh trung bình).
- $V = H^{\otimes n}X^{\otimes n}\,\text{MCZ}\,X^{\otimes n}H^{\otimes n} = 2|s\rangle\langle s| - I$.
- Hình học: mỗi vòng quay $\theta = 2\arcsin\sqrt{M/N}$; $\kappa \approx \frac\pi4\sqrt{N/M}$. Lặp **quá** $\kappa$ thì xác suất giảm.
- Cổ điển $\sim N$, Grover $\sim\sqrt N$: tăng tốc **bậc hai**, không phải hàm mũ.
- Chỉ có ích khi oracle dựng được hiệu quả.

---

## So sánh 4 thuật toán

| | Deutsch–Jozsa | Bernstein–Vazirani | Simon | Grover |
|---|---|---|---|---|
| Đầu ra của $f$ | 1 bit | 1 bit | $n$ bit | 1 bit |
| Qubit phụ | 1, ở $\|-\rangle$ | 1, ở $\|-\rangle$ | $n$, ở $\|0\rangle^{\otimes n}$ | 1, ở $\|-\rangle$ |
| Cơ chế chính | Kickback + $H^{\otimes n}$ | Kickback + $H^{\otimes n}$ | Đo thanh ghi dưới + $H^{\otimes n}$ | Kickback + diffuser, lặp $\kappa$ lần |
| Kết quả mỗi lần chạy | Tất định | Tất định | Ngẫu nhiên: một $z$ với $s\cdot z = 0$ | Xác suất cao |
| Hậu xử lý cổ điển | Không | Không | Khử Gauss modulo 2 | Kiểm tra $f(x_\text{out})$ |
| Gọi oracle, cổ điển | $2^{n-1}+1$ (chắc chắn) | $n$ | $\sim 2^{n/2}$ | $\sim N$ |
| Gọi oracle, lượng tử | 1 | 1 | $\sim n$ | $\sim\sqrt N$ |

## Tổng hợp API dùng trong phần này

| API / hàm | Dùng để | Bài |
|---|---|---|
| `QuantumCircuit(n, m, name=)`, `QuantumRegister` | Tạo mạch/hộp đen có tên | 04_01–04_04 |
| `qc.append(sub_circuit_or_gate, qubits)` | Gắn hộp đen, diffuser vào mạch | 04_01–04_04 |
| `qc.mcx(controls, target, ctrl_state=)` | Oracle: lật $y$ tại một giá trị $x$ | 04_01, 04_03, 04_04 |
| `qc.cx(list_controls, list_targets)` | Nhiều CX cùng lúc (oracle BV, parity) | 04_01, 04_02 |
| `qc.prepare_state(k, qubits)` | Nạp đầu vào cổ điển $\|k\rangle$ | 04_01, 04_04 |
| `ZGate().control(k)` | Tạo MCZ cho diffuser | 04_04 |
| `BitFlipOracleGate(expr, vars)` | Dựng oracle từ biểu thức Boolean | 04_03 |
| `sympy.symbols`, `sympy.logic.boolalg.SOPform` | Rút gọn biểu thức Boolean | 04_03 |
| `qc.decompose()` | Xem mạch bên trong một cổng | 04_03, 04_04 |
| `transpile(qc, simulator)`, `AerSimulator().run(qc, shots=, memory=True)` | Chạy mạch | 04_01–04_04 |
| `result.get_memory()`, `result.get_counts()` | Lấy chuỗi bit từng shot / số lần đếm | 04_01–04_04 |
| `Statevector(qc)`, `Statevector.from_label` | Kiểm tra trạng thái chính xác | 04_01–04_03 |
| `plot_histogram`, `plot_distribution` | Vẽ kết quả | 04_01, 04_04 |
| `np.binary_repr`, `np.random.choice(..., replace=False)` | Chuỗi nhị phân, chọn ngẫu nhiên không trùng | 04_01–04_04 |

## Cách chạy

Mở notebook trong VS Code hoặc Jupyter, chọn kernel `.venv` của repo, chạy từ trên xuống. Thư viện cần có
trong [../requirements.txt](../requirements.txt); 04_03 cần thêm `sympy`, đã có sẵn trong file đó.

- Mọi thứ chạy trên `AerSimulator` cục bộ, không cần tài khoản IBM.
- Hộp đen, chuỗi bí mật và phần tử đánh dấu đều sinh **ngẫu nhiên**, nên output mỗi lần chạy khác bản đã lưu;
  kết luận thì không đổi (trừ lỗi của `black_box()` ở 04_01 và `Uf_M_marked` ở 04_04 đã nêu ở trên).
- Một số biểu đồ so sánh cổ điển/lượng tử (xác suất theo số lần thử) chỉ có dạng **ảnh tĩnh** trong notebook,
  không có code sinh ra chúng.
- Các notebook dùng lại hàm giữa các mục (ví dụ `black_box_n`, `diffuser`, `fx_simon`), nên phải chạy theo thứ tự.
