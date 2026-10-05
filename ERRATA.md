# Lỗi đã biết trong bản gốc

Notebook trong [chapters/](chapters/) được giữ **nguyên văn** so với
[bản gốc](https://github.com/learn-quantum/lqc-textbook) (commit `7abf73c`), kể cả lỗi. Các lỗi dưới đây
được phát hiện khi đọc đối chiếu. Mỗi lỗi cũng được ghi chú tại chỗ (dạng `> Lưu ý:`) trong README của
phần tương ứng, kèm giải thích chi tiết.

Mức độ:

- **Code**: lỗi trong code, làm output hoặc kết luận bị sai lệch.
- **Nội dung**: phát biểu sai về kiến thức.
- **Có thể đã lỗi thời**: đúng lúc viết sách nhưng có thể không còn đúng với phần mềm, dịch vụ hiện nay.
- **Đánh máy**: lỗi trong công thức, comment hoặc chữ; không ảnh hưởng tới code.

## Code

| Bài | Lỗi | Ảnh hưởng | Cách sửa |
|---|---|---|---|
| [02_01](chapters/02_quantum_computing/README.md) | `one = Statevector([1, 0])`, đó là $\vert 0\rangle$ chứ không phải $\vert 1\rangle$ | Không, vì cell sau ghi đè bằng `from_label('1')` | `Statevector([0, 1])` |
| [02_05](chapters/02_quantum_computing/README.md) | Cell kickback nhiều qubit gán `qψ_in` (thừa chữ `q`) nhưng hiển thị `ψ_in` của cell trước | Output "input" ghi $\vert 01\rangle$ là sai; output "output" đúng | Đổi `qψ_in` thành `ψ_in` |
| [04_01](chapters/04_quantum_algorithms/README.md) | `black_box()` dùng `np.random.randint(1,3)` nên chỉ sinh mạch 1 hoặc 2, tức **chỉ hàm hằng** | Hai biểu đồ đúng/sai của mục 1.1 không phản ánh bài toán đầy đủ | `np.random.randint(1,5)` |
| [04_04](chapters/04_quantum_algorithms/README.md) | `Uf_M_marked(n, M)` chọn phần tử bằng `np.random.randint(N, size=M)` nên **có thể trùng**; output lưu sẵn ra `['001', '001']` | Hai MCX giống nhau triệt tiêu, oracle không đánh dấu gì | `np.random.choice(N, size=M, replace=False)` |
| [04_04](chapters/04_quantum_algorithms/README.md) | Dòng `found after: {x_in} tries` in ra **chỉ số** $x$ | Số lần thử thật là `x_in + 1` | In `x_in + 1` |

## Nội dung

| Bài | Lỗi | Đúng ra là |
|---|---|---|
| [02_03](chapters/02_quantum_computing/README.md) | Nói $\{H, S, CX\}$ đủ để xấp xỉ mọi cổng | Bộ này chỉ sinh nhóm Clifford (mô phỏng hiệu quả được trên máy cổ điển, định lý Gottesman–Knill); cần thêm $T$ (Clifford+T). Bài 02_04 của sách nói đúng |
| [03_01](chapters/03_quantum_protocols/README.md) | Công thức $(1/4)^n$ đứng cạnh câu về "kẻ làm giả thành công" dễ bị hiểu là xác suất làm giả thành công | Đó là xác suất đoán mù **chính xác** cả trạng thái. Kẻ đo ngẫu nhiên từng qubit rồi chuẩn bị lại thì **một** đồng qua kiểm tra với xác suất $(3/4)^n$ (khoảng 0.18 khi $n=6$); để **cả hai** đồng cùng qua thì cách này chỉ đạt $(5/8)^n$, và giỏi nhất cũng chỉ $(3/4)^n$ (kết quả tối ưu đã được chứng minh: Molina–Vidick–Watrous 2012, [arXiv:1202.4010](https://arxiv.org/abs/1202.4010)). Đều giảm theo hàm mũ |
| [03_01](chapters/03_quantum_protocols/README.md) | "the probability of the criminal successfully guessing the state grows with the number of qubits" | Xác suất **giảm** theo $n$, đúng như công thức $(1/4)^n$ |
| [01_02](chapters/01_classical_computing/README.md) | Nói áp mạch **OR** khả nghịch hai lần "cho kết quả đúng trong trường hợp này" | Chỉ đúng với một nửa đầu vào. Mạch là X, X lên $a, b$ rồi CCX vào $c = 1$ (không có X cuối), nên áp hai lần biến $(a, b, 1)$ thành $(a, b, a \oplus b)$: $c$ chỉ về $1$ khi $a \neq b$. Ví dụ $(0,0,1) \to (1,1,0) \to (0,0,0)$. Phải đảo thứ tự các cổng mới hoàn tác được, đúng như cell sau đó làm |
| [01_03](chapters/01_classical_computing/README.md) | Nhân CX với $\vert 00\rangle$ cho "cột vector bằng **hàng** đầu của CX" | Là **cột** đầu $(c_{00}, c_{10}, c_{20}, c_{30})$. Kết quả số vẫn đúng vì ma trận CX đối xứng |
| [01_04](chapters/01_classical_computing/README.md) | Định nghĩa "ma trận stochastic" là ma trận nhiều p-bit **không** viết được dưới dạng tích Kronecker; và nói ma trận stochastic nói chung không khả nghịch | Ma trận stochastic là ma trận có phần tử không âm và tổng mỗi cột bằng 1; các ma trận $P$, $R$, $X$ và $R \otimes X$ trong bài đều là stochastic. Điểm cốt lõi là **nghịch đảo** của ma trận nhiễu nói chung không còn là ma trận stochastic (có phần tử âm hoặc lớn hơn 1), nên không mô tả được phép toán vật lý |
| [02_02](chapters/02_quantum_computing/README.md) | Chọn $\frac{1}{\sqrt2}\vert 01\rangle + \frac{1}{\sqrt2}\vert 10\rangle$ làm trạng thái của hai hạt sinh ra từ hạt spin 0 ("a reasonable choice") | Chỉ khớp với phép đo theo $z$. Bảo toàn spin 0 cho **trạng thái đơn** (singlet) $\frac{1}{\sqrt2}(\vert 01\rangle - \vert 10\rangle)$, đối nghịch trên **mọi** trục; với dấu $+$, đo theo $x$ hoặc $y$ cho cùng kết quả ở cả hai phía |
| [02_04](chapters/02_quantum_computing/README.md) | Gọi SWAP là "another important entangling gate" | SWAP chỉ hoán đổi hai qubit ($\text{SWAP}\vert a\rangle\vert b\rangle = \vert b\rangle\vert a\rangle$), biến trạng thái tích thành trạng thái tích nên **không tạo vướng víu** |
| [02_04](chapters/02_quantum_computing/README.md) | Nói định lý Solovay–Kitaev là lý do thêm cổng $T$ cho sức mạnh tính toán đầy đủ | Solovay–Kitaev chỉ nói rằng một bộ cổng đã đủ trù mật thì xấp xỉ được mọi cổng **một cách hiệu quả**. Việc Clifford+T là bộ cổng phổ quát (trù mật) là một sự kiện riêng |
| [02_05](chapters/02_quantum_computing/README.md), [04_03](chapters/04_quantum_algorithms/README.md) | Gọi tăng tốc của Shor là "proven" | Grover được chứng minh tối ưu (trong mô hình oracle). Shor chỉ nhanh hơn thuật toán cổ điển **tốt nhất đã biết**; chưa có chứng minh rằng không có thuật toán cổ điển nhanh |
| [04_03](chapters/04_quantum_algorithms/README.md) | "Chỉ sau $r = 6$ lần thử, xác suất thành công đã vượt 50%" (với $n = 5$) | Tính chính xác (lấy mẫu không lặp): $r = 6$ cho $43.4\%$, $r = 7$ cho $56.5\%$; đồ thị trong sách cũng vậy. Cách tính này cũng cho $r = 14$ khi $n = 7$ (số lần thử đầu tiên vượt 50%), đúng như sách nói ngay sau đó |

## Có thể đã lỗi thời

Những chỗ đúng vào thời điểm viết sách nhưng có thể không còn đúng với phần mềm hoặc dịch vụ hiện nay.

| Bài | Nội dung trong sách | Hiện nay |
|---|---|---|
| [00_02](chapters/00_getting_started/README.md) | Tạo tài khoản ở `quantum.ibm.com`, chạy `QiskitRuntimeService.save_account('your-token-here')` | `qiskit-ibm-runtime` hiện hành mô tả `token` là IBM Cloud API key, kênh là `ibm_cloud` hoặc `ibm_quantum_platform`, kèm tham số `instance`; nền tảng đã chuyển sang `quantum.cloud.ibm.com`. Làm theo tài liệu hiện hành |

## Đánh máy

| Bài | Lỗi | Đúng ra là |
|---|---|---|
| [00_01](chapters/00_getting_started/README.md) | Tạo `qc_t = transpile(...)` nhưng chạy `simulator.run(qc, ...)` | Chạy `qc_t`; với AerSimulator không sao, trên phần cứng thật thì cần mạch đã transpile |
| [01_01](chapters/01_classical_computing/README.md) | Ghi chú nói `and`, `or` của Python không tương đương `&` và `^` | Bảng ngay trên đó ghi AND là `&`, OR là `\|`, XOR là `^`; nên là `&` và `\|` |
| [01_02](chapters/01_classical_computing/README.md) | "dùng hai CCX để đảo đầu vào" | Code và hình dùng hai cổng **X** |
| [01_02](chapters/01_classical_computing/README.md) | Comment trong code bộ cộng đầy đủ gọi `ccx(a,b,0)` là AND1 và `ccx(b2,c,0)` là AND2 | Hình 01_02_09 gọi ngược lại: cổng đầu (điều khiển $a, b$) là AND2, cổng sau (điều khiển $a \oplus b$ và $c_{in}$) là AND1 |
| [01_03](chapters/01_classical_computing/README.md) | Số chiều của $\vec x \otimes \vec y$ là "tổng" số chiều | Là **tích** ($2 \times 2 = 4$; $n$ bit cho $2^n$ chiều) |
| [01_04](chapters/01_classical_computing/README.md) | Comment ghi "100 times" | `n_samps = 200` |
| [02_03](chapters/02_quantum_computing/README.md) | Ví dụ đổi sang cơ sở sign ghi cả hai hệ số là $\frac{2\sqrt3 - \sqrt6}{6}$ | Hệ số của $\vert -\rangle$ là $\frac{2\sqrt3 + \sqrt6}{6} \approx 0.986$; giá trị số trong notebook đúng |
| [02_05](chapters/02_quantum_computing/README.md) | Mục 4.3 lúc nói $x = 010$, lúc nói $\vert 10\rangle$ | Code và output đánh dấu $x = 011$ |
| [02_05](chapters/02_quantum_computing/README.md) | Comment (và câu chữ) nói cổng S điều khiển `ctrl_state='01'` "kích hoạt bởi $\vert 01\rangle$" | `SGate().control(2, ctrl_state='01')` gắn vào `[2,1,0]` kích hoạt khi $q_2 = 1$ và $q_1 = 0$, tức hai qubit điều khiển ở $\vert q_2 q_1\rangle = \vert 10\rangle$ (chuỗi `ctrl_state` đọc từ phải sang trái: ký tự cuối ứng với qubit điều khiển đầu tiên); chạy thật cho pha $i$ ở $\vert 101\rangle$. Output trong sách đúng |
| [03_01](chapters/03_quantum_protocols/README.md) | "we only consider qubits in the $xy$-plane" | Mặt phẳng $xz$ |
| [03_02](chapters/03_quantum_protocols/README.md) | Comment "two entangled Bell states" và "Alice prepares state $\vert w\rangle = \frac12\vert 01\rangle - \frac{\sqrt3}{2}\vert 10\rangle$" | Mạch tạo 3 cặp Bell và chuẩn bị $\frac{1}{\sqrt3}(\vert 001\rangle - \vert 010\rangle + \vert 100\rangle)$, đúng như output |
| [03_02](chapters/03_quantum_protocols/README.md) | Bài 1 qubit in `(j,i) = ({alices_bits[1]},{alices_bits[0]})` | Đảo nhãn: `alices_bits[1]` là `cra[0]`, tức bit $i$ (đã kiểm tra bằng cách chạy Qiskit với chỉ `cra[0] = 1`); trạng thái cuối của Bob không bị ảnh hưởng |
| [03_02](chapters/03_quantum_protocols/README.md) | Với $(\theta, \varphi) = (\pi/2, \pi/4)$, viết cặp chuỗi FP16 là $(0011101001001000, 0011111001001000)$ | Hai chuỗi bị đổi chỗ: `float16` cho $\pi/4 = 0011101001001000$ và $\pi/2 = 0011111001001000$ |
| [03_03](chapters/03_quantum_protocols/README.md) | Bảng kết quả sau bước 3 ghi nhãn $\vert \psi\rangle_2$ | $\vert \psi\rangle_3$ |
| [04_04](chapters/04_quantum_algorithms/README.md) | Mục 2.2 viết $\vert m^\perp\rangle$ là $\sum_{x \neq 0}$ | $\sum_{x \neq m}$, và cần chuẩn hoá |
| [04_04](chapters/04_quantum_algorithms/README.md) | Mục 2.2 viết "áp dụng $(U_f V)^2$" ngay sau câu về $(V U_f)$ | $(V U_f)^2$, đúng như hình và công thức $(V U_f)^\kappa$ ngay dưới |

## Báo lỗi mới

Nếu tìm thấy lỗi khác, hãy mở issue theo mẫu **Báo lỗi trong sách** của repo này, và nên báo thêm cho
tác giả tại [Issues của repo gốc](https://github.com/learn-quantum/lqc-textbook/issues) để bản gốc được sửa.
