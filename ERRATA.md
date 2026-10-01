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
| [03_01](chapters/03_quantum_protocols/README.md) | Công thức $(1/4)^n$ đứng cạnh câu về "kẻ làm giả thành công" dễ bị hiểu là xác suất làm giả thành công | Đó là xác suất đoán mù **chính xác** cả trạng thái. Kẻ đo ngẫu nhiên từng qubit rồi chuẩn bị lại thì một đồng qua kiểm tra với xác suất $(3/4)^n$ (khoảng 0.18 khi $n=6$); để cả hai đồng cùng qua thì giỏi nhất cũng chỉ $(3/4)^n$. Đều giảm theo hàm mũ |
| [03_01](chapters/03_quantum_protocols/README.md) | "the probability of the criminal successfully guessing the state grows with the number of qubits" | Xác suất **giảm** theo $n$, đúng như công thức $(1/4)^n$ |

## Có thể đã lỗi thời

Những chỗ đúng vào thời điểm viết sách nhưng có thể không còn đúng với phần mềm hoặc dịch vụ hiện nay.

| Bài | Nội dung trong sách | Hiện nay |
|---|---|---|
| [00_02](chapters/00_getting_started/README.md) | Tạo tài khoản ở `quantum.ibm.com`, chạy `QiskitRuntimeService.save_account('your-token-here')` | `qiskit-ibm-runtime` hiện hành mô tả `token` là IBM Cloud API key, kênh là `ibm_cloud` hoặc `ibm_quantum_platform`, kèm tham số `instance`; nền tảng đã chuyển sang `quantum.cloud.ibm.com`. Làm theo tài liệu hiện hành |

## Đánh máy

| Bài | Lỗi | Đúng ra là |
|---|---|---|
| [00_01](chapters/00_getting_started/README.md) | Tạo `qc_t = transpile(...)` nhưng chạy `simulator.run(qc, ...)` | Chạy `qc_t`; với AerSimulator không sao, trên phần cứng thật thì cần mạch đã transpile |
| [01_02](chapters/01_classical_computing/README.md) | "dùng hai CCX để đảo đầu vào" | Code và hình dùng hai cổng **X** |
| [01_03](chapters/01_classical_computing/README.md) | Số chiều của $\vec x \otimes \vec y$ là "tổng" số chiều | Là **tích** ($2 \times 2 = 4$; $n$ bit cho $2^n$ chiều) |
| [01_04](chapters/01_classical_computing/README.md) | Comment ghi "100 times" | `n_samps = 200` |
| [02_03](chapters/02_quantum_computing/README.md) | Ví dụ đổi sang cơ sở sign ghi cả hai hệ số là $\frac{2\sqrt3 - \sqrt6}{6}$ | Hệ số của $\vert -\rangle$ là $\frac{2\sqrt3 + \sqrt6}{6} \approx 0.986$; giá trị số trong notebook đúng |
| [02_05](chapters/02_quantum_computing/README.md) | Mục 4.3 lúc nói $x = 010$, lúc nói $\vert 10\rangle$ | Code và output đánh dấu $x = 011$ |
| [03_01](chapters/03_quantum_protocols/README.md) | "we only consider qubits in the $xy$-plane" | Mặt phẳng $xz$ |
| [03_02](chapters/03_quantum_protocols/README.md) | Comment "two entangled Bell states" và "Alice prepares state $\vert w\rangle = \frac12\vert 01\rangle - \frac{\sqrt3}{2}\vert 10\rangle$" | Mạch tạo 3 cặp Bell và chuẩn bị $\frac{1}{\sqrt3}(\vert 001\rangle - \vert 010\rangle + \vert 100\rangle)$, đúng như output |
| [03_02](chapters/03_quantum_protocols/README.md) | Bài 1 qubit in `(j,i) = ({alices_bits[1]},{alices_bits[0]})` | Có vẻ đảo nhãn: `alices_bits[1]` là `cra[0]`, tức bit $i$; trạng thái cuối của Bob không bị ảnh hưởng |
| [03_03](chapters/03_quantum_protocols/README.md) | Bảng kết quả sau bước 3 ghi nhãn $\vert \psi\rangle_2$ | $\vert \psi\rangle_3$ |
| [04_04](chapters/04_quantum_algorithms/README.md) | Mục 2.2 viết $\vert m^\perp\rangle$ là $\sum_{x \neq 0}$ | $\sum_{x \neq m}$, và cần chuẩn hoá |

## Báo lỗi mới

Nếu tìm thấy lỗi khác, hãy mở issue theo mẫu **Báo lỗi trong sách** của repo này, và nên báo thêm cho
tác giả tại [Issues của repo gốc](https://github.com/learn-quantum/lqc-textbook/issues) để bản gốc được sửa.
