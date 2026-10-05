# 01 · Classical computing (Tính toán cổ điển)

**Tiếng Việt** · [English](README.en.md) · [简体中文](README.zh-CN.md)

Ôn lại bit, logic Boolean và mạch số, rồi "nâng cấp" dần chúng theo đúng hướng mà máy tính lượng tử cần:
cổng **khả nghịch** (reversible), bit là **vector** và cổng là **ma trận**, và cuối cùng là bit **xác suất**
(p-bit). Các công cụ toán mà phần 02 dùng liên tục (ket, tích Kronecker, ma trận của mạch) đều được xây ở đây.

> Nguồn: [01_01](https://learnquantum.io/chapters/01_classical_computing/01_01_bits_and_circuits.html) ·
> [01_02](https://learnquantum.io/chapters/01_classical_computing/01_02_reversible_computing.html) ·
> [01_03](https://learnquantum.io/chapters/01_classical_computing/01_03_bits_to_vectors.html) ·
> [01_04](https://learnquantum.io/chapters/01_classical_computing/01_04_probabilistic_circuits.html)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## Mục lục

| Bài | Notebook | Web | Ý chính |
|---|---|---|---|
| 01_01 · Bits and digital circuits | [01_01_bits_and_circuits.ipynb](01_01_bits_and_circuits.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_01_bits_and_circuits.html) | Số nhị phân trong Python, AND/OR/NOT/XOR, mạch cộng, transistor CMOS |
| 01_02 · Reversible computing | [01_02_reversible_computing.ipynb](01_02_reversible_computing.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_02_reversible_computing.html) | X, CX, CCX (Toffoli); AND/OR/COPY/full adder khả nghịch |
| 01_03 · Linear algebra for reversible circuits | [01_03_bits_to_vectors.ipynb](01_03_bits_to_vectors.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_03_bits_to_vectors.html) | Bit là vector $\vert 0\rangle,\vert 1\rangle$; cổng là ma trận; tích Kronecker |
| 01_04 · Probabilistic computing | [01_04_probabilistic_circuits.ipynb](01_04_probabilistic_circuits.ipynb) | [link](https://learnquantum.io/chapters/01_classical_computing/01_04_probabilistic_circuits.html) | p-bit, vector xác suất, ma trận ngẫu nhiên (stochastic) |

Phần này chỉ dùng **Python thuần, NumPy, SymPy và Matplotlib**, chưa dùng Qiskit.

> Các đoạn code trong README này là **trích** từ notebook (giữ comment gốc tiếng Anh) và dùng biến đã định nghĩa ở các cell trước. Muốn chạy được, hãy chạy cả notebook từ trên xuống.

---

## 01_01 · Bits and digital circuits (Bit và mạch số)

**Mục tiêu:** làm việc được với số nhị phân trong Python và hiểu mạch logic được xây từ các cổng cơ bản như thế nào.

### Kiến thức chính

**Số nhị phân.** Với $n$ bit $b = b_{n-1}\dots b_1 b_0$ biểu diễn được $2^n$ giá trị. $b_0$ (bên phải nhất) là
bit ít quan trọng nhất (LSB), $b_{n-1}$ là bit quan trọng nhất (MSB). Đổi sang thập phân:

$$x = \sum_{i=0}^{n-1} 2^i\, b_i \qquad\text{ví dụ } 1101 = 8 + 4 + 0 + 1 = 13$$

Chiều ngược lại, bit thứ $i$ là $b_i = \lfloor x / 2^i \rfloor \bmod 2$. Cần ít nhất
$n \ge \lfloor \log_2 x + 1 \rfloor$ bit để biểu diễn $x > 0$ (ví dụ 13 cần 4 bit).

**Logic Boolean.** Ba phép cơ bản: NOT ($\bar a$), OR ($a \lor b$), AND ($a \land b$); mọi mệnh đề logic đều
ghép được từ ba phép này. Phép được dùng rất nhiều trong cả sách là **XOR** (exclusive OR):

| $a$ | $b$ | $a \oplus b$ |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

$$a \oplus b = (a \land \bar b) \lor (\bar a \land b) = (a + b) \bmod 2$$

Với số nhiều bit, các phép này tác động **từng bit một** (bitwise).

**Mạch số.** Cổng logic là ký hiệu vẽ của phép Boolean.

<p align="center"><img src="images/01_01_01_basic_logic_gates.png" width="750" alt="Ký hiệu ba cổng logic cơ bản NOT, OR, AND"></p>

*Hình: ký hiệu cổng NOT, OR, AND (từ trái sang phải).*

NAND/NOR/XNOR là AND/OR/XOR có thêm NOT ở đầu ra, vẽ gọn bằng một vòng tròn nhỏ:

<p align="center"><img src="images/01_01_03_negated_logic_gates.png" width="760" alt="Ký hiệu cổng NAND, NOR, XNOR với vòng tròn nhỏ ở đầu ra"></p>

*Hình: NAND, NOR, XNOR; vòng tròn nhỏ ở đầu ra thay cho một cổng NOT.*

Ví dụ **full adder** cộng $a$, $b$ và số nhớ $c_{in}$:

$$s = a \oplus b \oplus c_{in}, \qquad c_{out} = \big((a \oplus b) \land c_{in}\big) \lor (a \land b)$$

<p align="center"><img src="images/01_01_04_adder.png" width="420" alt="Mạch full adder gồm hai cổng XOR, hai cổng AND và một cổng OR"></p>

*Hình: full adder: hai XOR cho $s$; hai AND và một OR cho $c_{out}$. Mỗi chấm tròn là chỗ một dây tách làm hai (fan-out).*

**COPY / FAN-OUT** là tách một dây thành hai. Trong mạch cổ điển việc này tầm thường, nhưng
**mạch lượng tử không có phép COPY tương đương**, điều sẽ gặp lại ở phần 02 (no-cloning).

**Transistor.** Ở tầng vật lý, 0 và 1 chỉ là hai mức điện áp $-v$ và $+v$. Công nghệ CMOS dùng cặp transistor
NMOS/PMOS bổ sung cho nhau như công tắc: điện áp làm loại này dẫn (ON) thì làm loại kia ngắt (OFF). Cổng NOT cần 2 transistor:

<p align="center"><img src="images/01_01_06_not_wi_transistors.png" width="660" alt="Cổng NOT bằng một transistor PMOS nối lên +v và một NMOS nối xuống -v, vẽ lại thành hai công tắc"></p>

*Hình: cổng NOT (trái) = một PMOS nối lên $+v$ và một NMOS nối xuống $-v$ (giữa) = hai công tắc (phải).*

Khi $v_{in} = +v$ (1), NMOS dẫn và PMOS ngắt, nên đầu ra nối với $-v$ (0); khi $v_{in} = -v$ thì ngược lại.
NAND cần 4 transistor:

<p align="center"><img src="images/01_01_09_nand_wi_transistors.png" width="500" alt="Cổng NAND bằng hai PMOS song song nối lên +v và hai NMOS nối tiếp xuống -v"></p>

*Hình: NAND bằng 4 transistor: hai PMOS song song nối lên $+v$, hai NMOS nối tiếp xuống $-v$.*

AND = NAND nối tiếp với NOT, tức 6 transistor.

### Code chính

```python
x = 0b1101
print(x)
```
Tiền tố `0b` viết số nhị phân, nhưng Python lưu nó là `int` (in ra `13`), nên cộng trừ bình thường được.

```python
b = bin(11) + bin(9)  # in decimal: 11 + 9 = 20
print(f'The result in b: {b} is not the correct representation for the number 20: {bin(20)}')
```
`bin()` trả về **chuỗi** (`str`), nên `+` là nối chuỗi chứ không phải phép cộng. Muốn tính toán phải đổi lại
bằng `int(b, 2)`.

```python
n = 4  # number of bits to use
for i in range(2**3):
    b = bin(i)[2:].zfill(n)
    print(f'{i}: {b}')
```
`[2:]` bỏ tiền tố `0b`; `zfill(n)` thêm số 0 vào bên trái cho đủ $n$ bit. Cách tương đương gọn hơn:
`np.binary_repr(13, 5)` trả về `'01101'`.

```python
a = 0b11010
b = 0b10110

c_and = np.binary_repr(a & b, 5)  # Bitwise AND: 11010 & 10110 = 10010
c_or = np.binary_repr(a | b, 5)   # Bitwise OR:  11010 | 10110 = 11110
c_xor = np.binary_repr(a ^ b, 5)  # Bitwise XOR: 11010 ^ 10110 = 01100
```
Toán tử bitwise của Python: `&` (AND), `|` (OR), `^` (XOR).

> Lưu ý: `and`/`or` của Python là toán tử **logic**, không tương đương `&`/`|` khi áp lên số nhiều bit.
> Notebook viết nhầm thành "`&` và `^`"; cặp đúng của `or` là `|`.

### Kết quả

| Code | Output |
|---|---|
| `0b1011 + 0b1001` | `20` |
| `bin(13)` | `0b1101` (kiểu `str`) |
| `bin(11) + bin(9)` | `0b10110b1001`, sai, trong khi `bin(20)` là `0b10100` |
| `int('1101', 2)` | `13` |
| `np.binary_repr(13, 5)` | `01101` |
| AND / OR / XOR của `11010`, `10110` | `10010` / `11110` / `01100` |

### Ghi nhớ nhanh

- $n$ bit biểu diễn $2^n$ giá trị; bit bên phải nhất là $b_0$.
- `bin()` ra chuỗi, `int(s, 2)` về lại số, `np.binary_repr(x, n)` ra chuỗi đủ $n$ bit.
- XOR = cộng modulo 2, được dùng rất nhiều trong cả sách.
- Bitwise trong Python: `&`, `|`, `^`, đừng nhầm với `and`, `or`.
- Mạch cổ điển copy dây thoải mái; mạch lượng tử thì không.

---

## 01_02 · Reversible computing (Tính toán khả nghịch)

**Mục tiêu:** hiểu vì sao AND/OR làm mất thông tin, và cách xây phiên bản khả nghịch của mọi cổng bằng X, CX, CCX.

### Kiến thức chính

**Vì sao cần khả nghịch.** Nhìn đầu ra của AND là 0 thì không biết đầu vào là 00, 01 hay 10: thông tin bị mất.
Landauer (1961) chỉ ra rằng mất thông tin gắn với tiêu tán năng lượng; từ đó ra đời mô hình tính toán khả nghịch
(Bennett 1973, Toffoli 1980, Fredkin 1981). Cơ học lượng tử về nguyên tắc là khả nghịch, nên mô hình tính toán
lượng tử cũng phải khả nghịch.

Một cổng là **khả nghịch** khi mỗi đầu vào cho **đúng một** đầu ra riêng, nên luôn suy ngược được đầu vào.

Từ bài này, cổng NOT được vẽ và gọi là cổng **X**, theo ký hiệu của mạch lượng tử:

<p align="center"><img src="images/01_02_01_not_gates.png" width="660" alt="Ba ký hiệu tương đương của cổng NOT: cổ điển, của Feynman, và ô X của mạch lượng tử"></p>

*Hình: ba cách vẽ cùng một cổng NOT: ký hiệu cổ điển, ký hiệu của Feynman (chữ X trên dây), và ô X dùng trong mạch lượng tử.*

| Cổng | Quy tắc | Ghi chú |
|---|---|---|
| **X** (NOT) | $a' = \bar a$ | Tự là nghịch đảo của nó: X·X = I |
| **CX** (controlled-X, CNOT) | $a' = a,\ b' = a \oplus b$ | XOR khả nghịch; với $b = 0$ thì thành **COPY** ($b' = a$) |
| **CCX** (Toffoli) | $a' = a,\ b' = b,\ c' = c \oplus (a \land b)$ | Với $c = 0$ ra **AND**; với $c = 1$ ra **NAND** |

Trong hình, chấm tròn đặc nằm trên dây điều khiển (control), ô X nằm trên dây đích (target):

<p align="center"><img src="images/01_02_02_cx_gate.png" width="180" alt="Cổng CX: chấm tròn trên dây a nối xuống ô X trên dây b"></p>

*Hình: cổng CX: dây trên $a$ là dây điều khiển, dây dưới $b$ là dây đích.*

<p align="center"><img src="images/01_02_04_ccx_gate.png" width="180" alt="Cổng CCX: hai chấm tròn trên dây a và b nối xuống ô X trên dây c"></p>

*Hình: cổng CCX (Toffoli): hai dây điều khiển $a$, $b$ và dây đích $c$.*

**OR khả nghịch** dùng định luật De Morgan $a \lor b = \overline{\bar a \land \bar b}$: đặt X lên cả hai đầu vào,
rồi dùng CCX với $c = 1$ (tức NAND).

<p align="center"><img src="images/01_02_07_reversible_or.png" width="220" alt="Mạch OR khả nghịch: cổng X trên dây a và dây b, rồi CCX lên dây thứ ba khởi tạo bằng 1"></p>

*Hình: OR khả nghịch: X trên $a$ và $b$, rồi CCX lên dây thứ ba khởi tạo bằng 1; $c' = a \lor b$.*

> Lưu ý: notebook viết "dùng hai CCX để đảo đầu vào", nhưng code và hình đều dùng hai cổng **X**.

**Đảo ngược một mạch** (uncompute) = áp **từng cổng theo thứ tự ngược lại**. Với X, CX, CCX thì áp lại lần hai
là đủ, vì mỗi cổng tự là nghịch đảo của nó; nhưng với mạch ghép thì phải đảo thứ tự. Sang mạch lượng tử
còn thêm yêu cầu với số phức, sẽ học sau.

<p align="center"><img src="images/01_02_08_reverse_ors.png" width="360" alt="Mạch OR khả nghịch nối với các cổng của nó theo thứ tự ngược lại, đầu ra trở về a, b, 1"></p>

*Hình: mạch OR (nửa trái) rồi các cổng của nó theo thứ tự ngược lại (nửa phải): CCX trước, hai X sau; đầu ra trở về $a$, $b$, $1$.*

> Lưu ý: notebook viết rằng áp cả mạch OR hai lần "tình cờ vẫn cho đúng" trong trường hợp này. Không đúng:
> với $a = b$, áp hai lần làm $c$ từ 1 thành 0, ví dụ $(0,0,1) \to (1,1,0) \to (0,0,0)$. Chỉ áp các cổng theo
> thứ tự ngược lại (như hình trên và code của notebook) mới trả về $(a, b, 1)$ với mọi đầu vào.

**Full adder khả nghịch** được thay thế một-một từ bản cổ điển, cần thêm các **dây phụ** (auxiliary/ancilla)
khởi tạo bằng giá trị cố định. Đây là đặc điểm rất phổ biến của mạch khả nghịch và mạch lượng tử.

<p align="center"><img src="images/01_02_09_reversible_adder.png" width="760" alt="Full adder cổ điển bên trái và bản khả nghịch bên phải, gồm các khối AND, XOR, OR làm bằng X, CX, CCX trên sáu dây"></p>

*Hình: full adder cổ điển (trái) và bản khả nghịch (phải): hai CCX (AND) ghi vào hai dây phụ khởi tạo 0, hai CX (XOR) đưa $s$ ra dây $c_{in}$, khối OR ghi $c_{out}$ vào dây phụ khởi tạo 1.*

### Code chính

```python
# define x gate as a function:
def x(a_in):
    a_out = a_in ^ 1   # Remember ^ performs the XOR operation. a^1 = a̅
    return a_out
```
X gate chính là XOR với 1.

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
CX: dây điều khiển giữ nguyên, dây đích bị lật khi dây điều khiển bằng 1. Hàm `ccx(a_in, b_in, c_in)` viết tương tự,
chỉ lật $c$ khi `a_in == 1 and b_in == 1`.

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
Full adder chỉ gồm X, CX, CCX. Ba dây phụ (hai dây khởi tạo 0 cho AND, một dây khởi tạo 1 cho OR) được thêm
để tính $c_{out}$.

> Lưu ý: comment trong code và nhãn trong hình đặt tên hai AND ngược nhau: code gọi `ccx(a, b, 0)` là AND1,
> còn hình gọi khối $a \land b$ là AND2 (và khối $(a \oplus b) \land c_{in}$ là AND1). Mạch thì giống nhau.

### Kết quả

- Bảng CX đúng $b' = a \oplus b$; áp CX hai lần trả lại đúng $(a, b)$.
- CCX với $c = 0$ cho $c' = a \land b$; áp hai lần trả lại $c = 0$.
- OR khả nghịch cho $c' = a \lor b$ (`0, 1, 1, 1`), còn $a' = \bar a$, $b' = \bar b$ vì hai cổng X vẫn ở đó;
  áp các cổng theo thứ tự ngược lại trả về $(a, b, 1)$.
- Full adder khả nghịch cho đúng bảng $s$, $c_{out}$ của bài 01_01:

| a | b | cin | s | cout |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

(trích 4 trong 8 dòng)

### Ghi nhớ nhanh

- Khả nghịch = mỗi đầu vào ra một đầu ra riêng, luôn suy ngược được.
- CX = XOR khả nghịch; CX với dây đích bằng 0 = COPY.
- CCX với dây đích bằng 0 = AND, bằng 1 = NAND.
- OR = X trên hai đầu vào + NAND.
- Đảo mạch: áp các cổng theo **thứ tự ngược lại**.
- Mạch khả nghịch thường cần dây phụ (ancilla).

---

## 01_03 · Linear algebra for reversible circuits (Đại số tuyến tính cho mạch khả nghịch)

**Mục tiêu:** biểu diễn bit bằng vector, cổng và cả mạch bằng ma trận, để "chạy mạch" chỉ là nhân ma trận.
Đây là bài quan trọng nhất của phần 01.

### Kiến thức chính

**Bit là vector, viết bằng ký hiệu Dirac (bra-ket):**

$$|0\rangle = \begin{bmatrix}1\\0\end{bmatrix}, \qquad |1\rangle = \begin{bmatrix}0\\1\end{bmatrix}$$

<p align="center"><img src="images/01_03_01_light_switches.png" width="400" alt="Vector [1, 0] ứng với bit 0: công tắc gạt lên, đèn tắt; vector [0, 1] ứng với bit 1: công tắc gạt xuống, đèn sáng"></p>

*Hình: mẹo nhớ: số 1 ở trên (công tắc gạt lên, đèn tắt) là bit 0; số 1 ở dưới (công tắc gạt xuống, đèn sáng) là bit 1.*

Vector bit hợp lệ có các phần tử thuộc $\{0,1\}$ và độ dài $\|b\| = 1$, nên loại được $[0,0]^\top$ (độ dài 0) và
$[1,1]^\top$ (độ dài $\sqrt 2$).

**Bra** $\langle b|$ là vector hàng (tạm thời chỉ là chuyển vị của ket). Tích **bra-ket** $\langle a|b\rangle$ là
tích vô hướng: $\langle b|b\rangle = 1$ và $\langle 0|1\rangle = 0$, tức $|0\rangle$ và $|1\rangle$ trực giao.

**Cổng là ma trận:**

$$\text{X} = \begin{bmatrix}0&1\\1&0\end{bmatrix}, \qquad \text{X}|0\rangle = |1\rangle, \qquad \text{X}^{-1} = \text{X}$$

Đảo một cổng đúng nghĩa là nhân với **ma trận nghịch đảo**. X "tình cờ" tự là nghịch đảo của nó, nên áp lại lần hai là đủ.

**Nhiều bit: tích Kronecker** $\otimes$.

$$|10\rangle = |1\rangle \otimes |0\rangle = \begin{bmatrix}0\\1\end{bmatrix} \otimes \begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}0\\0\\1\\0\end{bmatrix}$$

Quy tắc cần nhớ: vector của số nhị phân $b$ có **một số 1 duy nhất ở vị trí bằng giá trị thập phân của $b$**
(đếm từ 0, từ trên xuống), còn lại là 0. $n$ bit cho vector $2^n$ chiều. Các vector này trực giao với nhau và
tạo thành một **cơ sở** (basis); trạng thái lượng tử sau này là tổ hợp tuyến tính của chúng.

> Lưu ý: notebook viết số chiều của $\vec x \otimes \vec y$ là "tổng" số chiều; đúng ra là **tích**
> ($2 \times 2 = 4$, và $n$ bit cho $2^n$).

**Ma trận của cổng nhiều bit** tìm được bằng cách ghi ánh xạ đầu vào → đầu ra. Với CX, bit trên $b_1$ là bit
điều khiển, bit dưới $b_0$ là bit đích: $00 \to 00$, $01 \to 01$, $10 \to 11$, $11 \to 10$.

<p align="center"><img src="images/01_03_07_cx_gate.png" width="180" alt="Cổng CX với bit điều khiển b1 ở trên và bit đích b0 ở dưới"></p>

*Hình: CX với bit điều khiển $b_1$ (trên) và bit đích $b_0$ (dưới).*

$$\text{CX} = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}$$

Cột thứ $j$ (đếm từ 0) của ma trận chính là vector đầu ra khi đầu vào là $|j\rangle$, vì nhân ma trận với $|j\rangle$
chỉ lấy ra đúng cột đó.

> Lưu ý: notebook viết rằng nhân CX với $|00\rangle$ cho ra **hàng** đầu tiên $(c_{00}, c_{01}, c_{02}, c_{03})$.
> Đúng ra là **cột** đầu tiên $(c_{00}, c_{10}, c_{20}, c_{30})$. Ma trận CX cuối cùng vẫn đúng vì nó đối xứng.

CCX là ma trận đơn vị $8\times 8$ với hai hàng cuối đổi chỗ cho nhau.

**Ma trận của cả mạch:**
- Các cổng **cùng một lớp** (song song): lấy tích Kronecker, ví dụ X ở bit dưới và bit trên để trống là $I \otimes \text{X}$.

<p align="center"><img src="images/01_03_02_id_and_x.png" width="180" alt="Mạch hai bit: bit trên b1 không có cổng, bit dưới b0 đi qua cổng X"></p>

*Hình: bit trên $b_1$ để trống, bit dưới $b_0$ qua cổng X; ma trận là $I \otimes \text{X}$.*

- Các lớp **nối tiếp**: nhân ma trận **từ phải sang trái**, vì lớp áp trước phải nhân vào vector trước:

$$|b\rangle_{out} = Q_2\, Q_1\, |b\rangle_{in}$$

<p align="center"><img src="images/01_03_03_or_1.png" width="220" alt="Mạch ba bit chia hai lớp: lớp 1 có cổng X trên b2 và b1, lớp 2 có cổng CCX với đích là b0"></p>

*Hình: mạch 3 bit chia hai lớp: lớp 1 là $Q_1 = \text{X} \otimes \text{X} \otimes I$, lớp 2 là $Q_2 = \text{CCX}$.*

- Cách chia lớp không ảnh hưởng kết quả.

<p align="center"><img src="images/01_03_04_or_2.png" width="280" alt="Cùng mạch ba bit chia thành ba lớp: X trên b2, rồi X trên b1, rồi CCX"></p>

*Hình: cùng mạch đó chia ba lớp: $Q = \text{CCX}\,(I \otimes \text{X} \otimes I)\,(\text{X} \otimes I \otimes I)$, ra cùng ma trận.*

**Trường hợp đặc biệt:** CX nối hai bit không kề nhau, có một bit trống (idle bit) nằm giữa, thì không viết được dạng
$I \otimes \text{CX}$ hay $\text{CX} \otimes I$.

<p align="center"><img src="images/01_03_06_cx_with_idle.png" width="180" alt="Mạch ba bit: CX từ bit trên b2 tới bit dưới b0, bit giữa b1 không có cổng"></p>

*Hình: CX với bit điều khiển $b_2$ (trên) và bit đích $b_0$ (dưới); bit giữa $b_1$ để trống.*

Cách làm là tách CX thành **tổng** các tích Kronecker bằng hai phép chiếu $\Pi_0 = |0\rangle\langle 0|$ và
$\Pi_1 = |1\rangle\langle 1|$:

$$\text{CX} = \Pi_0 \otimes I + \Pi_1 \otimes \text{X} \quad\Rightarrow\quad Q = \Pi_0 \otimes I \otimes I + \Pi_1 \otimes I \otimes \text{X}$$

**Ba tính chất của ma trận mạch khả nghịch:** vuông ($2^n \times 2^n$), khả nghịch, và giữ nguyên độ dài vector.
Ở phần này mọi phần tử còn là 0 hoặc 1; bài 01_04 sẽ phá vỡ điều đó. Thực ra mỗi ma trận như vậy là một
**ma trận hoán vị** (permutation matrix): mỗi hàng và mỗi cột có đúng một số 1, nên nó chỉ đổi chỗ các phần tử của vector.

### Code chính

```python
# Define |0⟩
ket_0 = np.array([[1],
                  [0]])
print(ket_0)
```
Ket là mảng NumPy dạng **cột** (shape `(2, 1)`). `sp.Matrix(ket_0)` hiển thị đẹp bằng LaTeX.

```python
# Multiply |0⟩ by X to get |1⟩:
ket_1 = X @ ket_0
sp.Matrix(ket_1)
```
Nhân ma trận dùng `@` (hoặc `np.matmul`).

> Lưu ý: trong NumPy, `*` là nhân **từng phần tử** (tích Hadamard, không liên quan tới cổng Hadamard ở phần 02),
> không phải nhân ma trận. Muốn nhân ma trận thì luôn dùng `@`.

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
Đổi chuỗi nhị phân thành vector bằng `np.kron`, ghép từ bit phải nhất sang trái.

```python
# Compute circuit matrix
Q_1 = np.kron(X, np.kron(X, I))
Q_2 = CCX

Q = Q_2 @ Q_1
```
Mạch hai lớp: lớp 1 là $\text{X} \otimes \text{X} \otimes I$, lớp 2 là CCX. Ma trận của cả mạch là $Q_2 Q_1$.

```python
# Compute Q for our circuit
Q = np.kron(Π0,np.kron(I,I)) + np.kron(Π1,np.kron(I,X))
```
CX giữa bit trên cùng và bit dưới cùng, bỏ qua bit giữa.

### Kết quả

| Kiểm tra | Output |
|---|---|
| Độ dài $\vert 0\rangle$, $\vert 1\rangle$ | `1.0`, `1.0` |
| Độ dài $[0,0]^\top$, $[1,1]^\top$ | `0.0`, `1.414…` (không hợp lệ) |
| `np.vdot`: $\langle 0\vert 0\rangle$, $\langle 0\vert 1\rangle$, $\langle 1\vert 0\rangle$, $\langle 1\vert 1\rangle$ | `1, 0, 0, 1` |
| `np.linalg.inv(X)` | bằng X (phần tử in dạng số thực `1.0`) |
| `bin_to_vec('10110')` | vector 32 chiều, số 1 ở vị trí 22 |
| $Q_2 Q_1$ và $Q_3 Q_2 Q_1$ (hai cách chia lớp) | cùng một ma trận |
| $Q\,\vert 100\rangle$ với CX nhảy qua bit giữa | $\vert 101\rangle$ (số 1 ở vị trí 5) |

### Ghi nhớ nhanh

- $|0\rangle = [1, 0]^\top$, $|1\rangle = [0, 1]^\top$; $|b\rangle$ có số 1 ở vị trí bằng giá trị của $b$.
- Song song → `np.kron`; nối tiếp → `@`, viết **từ phải sang trái**.
- `@` là nhân ma trận, `*` chỉ là nhân từng phần tử.
- Đảo cổng = nhân ma trận nghịch đảo.
- Cổng điều khiển cách bit: $\Pi_0 \otimes I \otimes \dots + \Pi_1 \otimes \dots \otimes \text{X}$.
- Ma trận mạch khả nghịch: vuông, khả nghịch, giữ độ dài (là **ma trận hoán vị**).

---

## 01_04 · Probabilistic computing (Tính toán xác suất)

**Mục tiêu:** đưa ngẫu nhiên vào mạch cổ điển bằng p-bit, và thấy rõ điểm khác với qubit sẽ học ở phần 02.

### Kiến thức chính

**p-bit** (probability bit) là vector xác suất:

$$\vec p = \begin{bmatrix}\varrho_0\\ \varrho_1\end{bmatrix}, \qquad \varrho_j \in [0,1], \qquad \varrho_0 + \varrho_1 = 1$$

$\varrho_j$ là xác suất **đo** được giá trị $j$. Đo nhiều lần thì tần suất $n_j / n$ tiến về $\varrho_j$.
Ví dụ: một cổng NOT bị nhiễu, đầu vào 0 cho đầu ra $[1/4, 3/4]^\top$.

<p align="center"><img src="images/01_04_03_noisy_not.png" width="560" alt="Cổng NOT nhiễu: đầu vào chưa đủ thấp để là 0, nhiễu làm đầu ra đôi khi lật về 0; 3/4 thời gian đầu ra là 1, 1/4 là 0"></p>

*Hình: cổng NOT nhiễu: điện áp vào chưa đủ thấp, nhiễu làm đầu ra thỉnh thoảng lật về 0; đầu ra là 1 trong 3/4 thời gian, là 0 trong 1/4.*

**Khác biệt với qubit:** p-bit có **tổng** các phần tử bằng 1, nên độ dài Euclid của nó thay đổi
(ví dụ $\|[1/4, 3/4]^\top\| \approx 0.79$). Qubit có **tổng bình phương môđun** các phần tử bằng 1, nên độ dài luôn bằng 1
(phần 02 sẽ giải thích vì sao phần tử của qubit có thể là số phức).

<p align="center"><img src="images/01_04_01_prob_vec_length.png" width="200" alt="Vector xác suất p trong mặt phẳng rho0, rho1, đầu mũi tên nằm trên đoạn thẳng nét đứt nối (1,0) và (0,1)"></p>

*Hình: đầu vector xác suất $\vec p$ luôn nằm trên đoạn thẳng nét đứt $\varrho_0 + \varrho_1 = 1$, nên độ dài của nó thay đổi.*

<p align="center"><img src="images/01_04_02_prob_amps_vec_length.png" width="200" alt="Vector qubit q trong mặt phẳng q0, q1, đầu mũi tên nằm trên cung tròn nét đứt bán kính 1"></p>

*Hình: với $q_0, q_1 \in [0,1]$, đầu vector qubit $\vert q\rangle$ nằm trên cung tròn nét đứt bán kính 1, nên độ dài luôn bằng 1.*

**Cổng xác suất có nhiễu (không tất định) không đảo ngược được về mặt vật lý**, dù ma trận của nó có thể có nghịch đảo về mặt toán học.
Cổng NOT nhiễu ở trên có ma trận

$$P = \begin{bmatrix}\tfrac14 & 1\\ \tfrac34 & 0\end{bmatrix}, \qquad P^{-1} = \begin{bmatrix}0 & \tfrac43\\ 1 & -\tfrac13\end{bmatrix}$$

$P^{-1}$ có phần tử âm (và phần tử $\tfrac43 > 1$) nên không phải ma trận xác suất: nhiễu **không thể bị "huỷ"**
bằng một cổng xác suất khác. Ngược lại, ma trận của mạch lượng tử luôn khả nghịch.

**Cổng tất định vẫn đúng với p-bit.** X đảo thứ tự xác suất: $\text{X}[\varrho_0, \varrho_1]^\top = [\varrho_1, \varrho_0]^\top$.

<p align="center"><img src="images/01_04_04_pbit_thru_x_gate.png" width="440" alt="Một chuỗi giá trị 0 và 1 ngẫu nhiên đi qua cổng X thành chuỗi đảo ngược"></p>

*Hình: một chuỗi giá trị ngẫu nhiên qua cổng X thành chuỗi đảo ngược, nên xác suất của 0 và của 1 đổi chỗ cho nhau.*

**Nhiều p-bit.** Vector của các p-bit **độc lập thống kê** vẫn là tích Kronecker; ma trận của các cổng tác động
riêng lên từng p-bit cũng là tích Kronecker:

$$\begin{bmatrix}\tfrac23\\ \tfrac13\end{bmatrix} \otimes \begin{bmatrix}\tfrac14\\ \tfrac34\end{bmatrix}
= \begin{bmatrix}\tfrac16\\ \tfrac12\\ \tfrac1{12}\\ \tfrac14\end{bmatrix}
\quad\text{(xác suất của } 00, 01, 10, 11\text{)}$$

Khi kết quả trên một p-bit phụ thuộc trạng thái của p-bit khác thì ma trận **không tách được** thành tích Kronecker.
Ví dụ: giữ nguyên $\vec p_0$ nếu $\vec p_1 = 0$, còn nếu $\vec p_1 = 1$ thì làm ngẫu nhiên $\vec p_0$:

$$P = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&\tfrac12&\tfrac12\\0&0&\tfrac12&\tfrac12\end{bmatrix}$$

> Lưu ý: notebook gọi riêng loại ma trận không tách được này là **ma trận ngẫu nhiên** (stochastic matrix).
> Thật ra ma trận ngẫu nhiên là mọi ma trận có phần tử không âm và tổng mỗi cột bằng 1 (với cách viết vector cột
> của sách), tức là biến vector xác suất thành vector xác suất. Ma trận NOT nhiễu ở trên, X, và cả $R \otimes \text{X}$
> ở phần Code chính đều là ma trận ngẫu nhiên. Tách được thành tích Kronecker hay không là một tính chất khác.

**Mạch tất định khả nghịch là ma trận hoán vị:** nó chỉ đổi chỗ các xác suất, nên nhân với $Q^{-1}$ sẽ đưa chúng
về đúng vị trí ban đầu. Ví dụ mạch $Q = (\text{X} \otimes I)\,\text{CX}$ trong notebook:

<p align="center"><img src="images/01_04_05_pbit_thru_circuit.png" width="220" alt="Mạch hai p-bit: CX với p1 điều khiển và p0 là đích, sau đó cổng X trên p1"></p>

*Hình: CX ($\vec p_1$ điều khiển, $\vec p_0$ là đích) rồi X trên $\vec p_1$; ma trận là $Q = (\text{X} \otimes I)\,\text{CX}$.*

### Code chính

```python
n_samps = 200                   # number of samples
vals = [0, 1]                   # Possible outcomes: 0 or 1
probs = (vec_p).reshape(-1)     # Flatten to 1D array with probabilities for 0 and 1

# sample 0 or 1 a 100 times using probabilities from p̅
samples = np.random.choice(vals, size=n_samps, p=probs)
print(samples)
```
Mô phỏng phép đo p-bit bằng `np.random.choice` với xác suất lấy từ vector.

> Lưu ý: code không đặt seed, nên mỗi lần chạy mẫu và tần suất sẽ khác output lưu sẵn. Comment ghi
> "100 times" nhưng `n_samps = 200`.

```python
X = np.array([[0,1],
              [1,0]])
R = np.array([[1/2,1/2],
              [1/2,1/2]])

P = np.kron(R, X)
```
Hai p-bit độc lập: X (tất định) trên $\vec p_0$, R (luôn cho 0/1 với xác suất 1/2) trên $\vec p_1$.

```python
# define general input probability vector
ϱ0, ϱ1, ϱ2, ϱ3 = sp.symbols('ϱ0, ϱ1, ϱ2, ϱ3')
p_in = sp.Matrix([ϱ0, ϱ1, ϱ2, ϱ3])
```
Dùng biến ký hiệu của SymPy để thấy mạch $Q = (\text{X} \otimes I)\,\text{CX}$ hoán vị các xác suất ra sao.
Sau đó `Q.inv() @ p_int` đưa chúng về chỗ cũ.

### Kết quả

| Kiểm tra | Output |
|---|---|
| 200 mẫu từ $[1/4, 3/4]$ | tần suất 0 là `0.27`, tần suất 1 là `0.73` |
| $P = R \otimes \text{X}$ áp lên $\vert 00\rangle$ | $[0, 0.5, 0, 0.5]$: $\vec p_0$ luôn là 1, $\vec p_1$ là 0/1 mỗi bên 1/2 |
| $P$ áp lên $\vec p_1 \otimes \vec p_0$ với $\vec p_0 = [2/3, 1/3]$, $\vec p_1 = [1/10, 9/10]$ | $[0.1667, 0.3333, 0.1667, 0.3333]$ |
| Ma trận $4 \times 4$ không tách được ở trên, áp lên $\vert 10\rangle$ | $[0, 0, 0.5, 0.5]$ |
| $Q\,[\varrho_0, \varrho_1, \varrho_2, \varrho_3]^\top$ | $[\varrho_3, \varrho_2, \varrho_0, \varrho_1]^\top$; nhân tiếp $Q^{-1}$ ra lại thứ tự ban đầu |

### Ghi nhớ nhanh

- p-bit: phần tử thuộc $[0,1]$, **tổng** bằng 1. Qubit: **tổng bình phương môđun** bằng 1.
- Nhiễu không đảo ngược được: $P^{-1}$ có phần tử âm.
- p-bit độc lập → tích Kronecker; cổng làm p-bit này phụ thuộc p-bit kia → ma trận không tách được.
- Mọi ma trận biến vector xác suất thành vector xác suất đều là ma trận ngẫu nhiên (stochastic), dù tách được hay không.
- Mạch tất định khả nghịch = ma trận hoán vị, đúng cả với p-bit.

---

## Tổng hợp API dùng trong phần này

| API / hàm | Dùng để | Bài |
|---|---|---|
| `0b1101`, `bin(x)`, `int(s, 2)` | Viết số nhị phân, đổi số ↔ chuỗi nhị phân | 01_01 |
| `str.zfill(n)`, `np.binary_repr(x, n)` | Chuỗi nhị phân đủ $n$ bit | 01_01 |
| `&`, `\|`, `^` | AND, OR, XOR từng bit | 01_01, 01_02 |
| `np.array([[1],[0]])` | Vector cột (ket) | 01_03, 01_04 |
| `@`, `np.matmul` | Nhân ma trận | 01_03, 01_04 |
| `np.kron` | Tích Kronecker (ghép bit, ghép cổng song song) | 01_03, 01_04 |
| `np.vdot` | Tích vô hướng | 01_03 |
| `np.linalg.inv` | Ma trận nghịch đảo | 01_03 |
| `np.eye(n)` | Ma trận đơn vị | 01_03 |
| `np.where(v == 1)` | Tìm vị trí số 1 trong vector | 01_03 |
| `np.random.choice(vals, size, p)` | Lấy mẫu theo xác suất | 01_04 |
| `sp.Matrix`, `.evalf(n)`, `.inv()` | Hiển thị/tính ma trận bằng SymPy | 01_03, 01_04 |
| `sp.symbols` | Biến ký hiệu | 01_04 |
| `plt.hist` | Vẽ histogram kết quả đo | 01_04 |

## Cách chạy

Mở notebook trong VS Code hoặc Jupyter, chọn kernel `.venv` của repo, chạy từ trên xuống. Thư viện cần có
trong [requirements.txt](../../requirements.txt); phần này chỉ dùng NumPy, SymPy, Matplotlib.

- Các notebook độc lập với nhau, nhưng trong mỗi notebook, cell sau dùng biến của cell trước
  (ví dụ `X`, `I`, `bin_to_vec` ở 01_03), nên phải chạy theo thứ tự.
- 01_04 lấy mẫu ngẫu nhiên không có seed, nên số liệu lấy mẫu sẽ khác output lưu sẵn. Các phép nhân ma trận thì luôn cho cùng kết quả.

---

<!-- nav -->
[← 00 · Getting started](../00_getting_started/README.md) · [Mục lục](../../README.md#mục-lục) · [02 · Quantum computing →](../02_quantum_computing/README.md)
