# Learn Quantum Computing using Python (learnquantum.io)

Bản sao toàn bộ code và notebook của sách mở **[Learn Quantum Computing using Python](https://learnquantum.io)**
(Diego Emilio Serrano), kèm README tiếng Việt cho từng phần để học, tra cứu và ôn lại khi quên.
Sách dạy tính toán lượng tử từ gốc: bắt đầu từ bit và mạch cổ điển, đi đến qubit, vướng víu, các giao thức
và thuật toán lượng tử, tất cả đều có code **Qiskit** chạy được.

| | |
|---|---|
| Tác giả | Diego Emilio Serrano |
| Web | https://learnquantum.io |
| Repo gốc | [learn-quantum/lqc-textbook](https://github.com/learn-quantum/lqc-textbook) |
| Bản sao lấy từ | commit [`7abf73c`](https://github.com/learn-quantum/lqc-textbook/commit/7abf73cb1d430e0eba1d052d8b4d8bc976e956f6) (2026-03-20), lấy về ngày 2026-09-30 |
| Giấy phép | MIT, xem [LICENSE](LICENSE) |
| Thư viện | Qiskit, Qiskit Aer, Qiskit IBM Runtime, NumPy, SymPy, Matplotlib |

Notebook được giữ **nguyên văn** so với bản gốc, kể cả output mà tác giả đã chạy sẵn, nên có thể đọc
thẳng trên GitHub mà không cần chạy. Phần do repo này viết thêm là các file `README.md`,
[requirements.txt](requirements.txt) và [qiskit_settings.conf](qiskit_settings.conf).

## Mục lục

Mỗi phần có README riêng giải thích kiến thức, code chính, kết quả và ghi nhớ nhanh cho từng bài.

| Phần | Bài | Notebook | Nội dung |
|---|---|---|---|
| **[00 · Getting started](00_getting_started/)** | 00_00 | [About](00_getting_started/00_00_welcome.ipynb) | Cách dùng sách, trích dẫn |
| | 00_01 | [Setting your environment](00_getting_started/00_01_setting_env.ipynb) | Cài Qiskit, code kiểm tra môi trường |
| | 00_02 | [Configuring Qiskit](00_getting_started/00_02_qiskit_config.ipynb) | Token IBM Quantum, `settings.conf` |
| **[01 · Classical computing](01_classical_computing/)** | 01_01 | [Bits and circuits](01_classical_computing/01_01_bits_and_circuits.ipynb) | Bit, cổng logic, mạch cộng |
| | 01_02 | [Reversible computing](01_classical_computing/01_02_reversible_computing.ipynb) | Cổng khả nghịch X, CX, CCX |
| | 01_03 | [Bits to vectors](01_classical_computing/01_03_bits_to_vectors.ipynb) | Bit là vector, cổng là ma trận, tích tensor |
| | 01_04 | [Probabilistic circuits](01_classical_computing/01_04_probabilistic_circuits.ipynb) | Bit xác suất, mạch có nhiễu |
| **[02 · Quantum computing](02_quantum_computing/)** | 02_01 | [Bits to qubits](02_quantum_computing/02_01_bits_to_qubits.ipynb) | Thí nghiệm Stern–Gerlach, từ bit đến qubit |
| | 02_02 | [Entanglement](02_quantum_computing/02_02_entanglement.ipynb) | Trạng thái tách được và vướng víu; tạo vướng víu bằng H + CX |
| | 02_03 | [Single-qubit systems](02_quantum_computing/02_03_single_qb_sys.ipynb) | Biên độ phức, Bloch sphere, cổng một qubit, phép đo, observable |
| | 02_04 | [Multi-qubit systems](02_quantum_computing/02_04_multi_qb_sys.ipynb) | Cổng điều khiển, SWAP, no-cloning, bộ cổng phổ quát, đo một phần |
| | 02_05 | [Quantum building blocks](02_quantum_computing/02_05_quantum_blocks.ipynb) | Bell/GHZ/W, biến đổi Hadamard, phase kickback, oracle |
| **[03 · Quantum protocols](03_quantum_protocols/)** | 03_01 | [Quantum money](03_quantum_protocols/03_01_quantum_money.ipynb) | Nguyên lý bất định; tiền lượng tử Wiesner không thể làm giả |
| | 03_02 | [Teleportation](03_quantum_protocols/03_02_teleportation.ipynb) | Dịch chuyển trạng thái lượng tử |
| | 03_03 | [Superdense coding](03_quantum_protocols/03_03_superdense_coding.ipynb) | Gửi 2 bit cổ điển bằng 1 qubit |
| **[04 · Quantum algorithms](04_quantum_algorithms/)** | 04_01 | [Deutsch–Jozsa](04_quantum_algorithms/04_01_deutsch-jozsa.ipynb) | Hàm hằng hay cân bằng, 1 lần truy vấn |
| | 04_02 | [Bernstein–Vazirani](04_quantum_algorithms/04_02_bernstein-vazirani.ipynb) | Tìm chuỗi bí mật, 1 lần truy vấn |
| | 04_03 | [Simon's algorithm](04_quantum_algorithms/04_03_simons.ipynb) | Tìm chu kỳ XOR, tăng tốc hàm mũ |
| | 04_04 | [Grover's algorithm](04_quantum_algorithms/04_04_grover.ipynb) | Tìm kiếm không cấu trúc, tăng tốc căn bậc hai |

### Các chương chưa có nội dung trên web

Tính đến commit trên, những chương sau mới chỉ có tiêu đề (notebook trống) nên **chưa được sao chép**:

| Phần | Chương |
|---|---|
| 03 · Quantum protocols | 03_04 Bell inequalities, 03_05 Quantum key distribution |
| 05 · Important quantum primitives | 05_01 QFT, 05_02 QPE, 05_03 Amplitude amplification |
| 06 · Advanced quantum algorithms | 06_01 Shor, 06_02 HHL, 06_03 Hamiltonian simulation |

Khi tác giả bổ sung, xem mục [Cập nhật từ bản gốc](#cập-nhật-từ-bản-gốc).

## Cài đặt

Chạy ở thư mục gốc của repo:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r learnquantum/requirements.txt
```

**Nên làm thêm để hình vẽ giống sách:** copy [qiskit_settings.conf](qiskit_settings.conf) thành
`C:\Users\<tên>\.qiskit\settings.conf` (Windows) hoặc `~/.qiskit/settings.conf` (macOS/Linux).
Chi tiết từng tuỳ chọn ở [00_getting_started/README.md](00_getting_started/README.md#00_02--configuring-qiskit-cấu-hình-qiskit).

Mọi notebook đều chạy trên **simulator cục bộ** (`AerSimulator`, `Statevector`), không cần tài khoản IBM Quantum.
`qiskit-ibm-runtime` chỉ cần được cài, vì một số bài dùng `Estimator(mode=AerSimulator())`.

## Cách dùng

- **Đọc:** mở README của phần cần học, rồi mở notebook tương ứng trên GitHub; output đã có sẵn.
- **Chạy:** mở notebook trong VS Code hoặc Jupyter (`jupyter notebook`), chọn kernel `.venv`,
  chạy từ trên xuống. Mỗi notebook độc lập, không phụ thuộc notebook khác.
- **Ôn lại:** mỗi bài trong README có mục **Ghi nhớ nhanh** và mỗi phần có bảng **Tổng hợp API**.

### Lộ trình gợi ý

```text
00 Cài đặt ─> 01 Cổ điển ─> 02 Lượng tử ─> 03 Giao thức ─> 04 Thuật toán
               (vector,       (qubit, Bloch,    (teleportation,   (Deutsch–Jozsa → BV
                ma trận)       vướng víu, oracle) superdense)       → Simon → Grover)
```

Phần 01 trông "cổ điển" nhưng rất quan trọng: nó xây toàn bộ công cụ vector, ma trận, tích tensor
dùng lại cho qubit. Bài [02_05 Quantum building blocks](02_quantum_computing/02_05_quantum_blocks.ipynb)
(oracle, phase kickback) là nền cho cả phần 04, nên đọc kỹ trước khi sang thuật toán.

Liên hệ với các bài tự học trong repo này:

| Bài trong repo | Liên quan |
|---|---|
| [learn/01_reversible_computing](../learn/01_reversible_computing) | Trùng chủ đề với 01_02 Reversible computing |
| [learn/02_parameter_shift_rule](../learn/02_parameter_shift_rule) | Mở rộng: gradient của mạch có tham số (PennyLane), dùng kiến thức cổng xoay và giá trị kỳ vọng ở 02_03 |

## Quy ước cần nhớ khi đọc code Qiskit

- **Thứ tự qubit (little-endian):** trong chuỗi kết quả như `'011'`, ký tự **bên phải nhất** là qubit 0.
- `circuit_reverse_bits = True` trong `settings.conf` chỉ đổi cách **vẽ** mạch, không đổi kết quả.
- `Statevector(qc)` tính trạng thái chính xác; `AerSimulator().run(qc, shots=N)` mô phỏng đo N lần.
  Kết quả shot có nhiễu thống kê, nên số liệu khi bạn chạy lại sẽ hơi khác output lưu trong notebook.
- Mạch có phép đo phải có bit cổ điển: `QuantumCircuit(n_qubits, n_bits)`.

## Lỗi đã biết trong bản gốc

Notebook được giữ **nguyên văn**, kể cả lỗi. Các lỗi dưới đây phát hiện khi đọc đối chiếu và được ghi chú chi tiết
(dạng `> Lưu ý:`) trong README của từng phần:

| Bài | Lỗi | Ảnh hưởng |
|---|---|---|
| 02_01 | `one = Statevector([1, 0])` (đúng ra là `[0, 1]`) | Không, vì cell sau ghi đè lại |
| 02_03 | Nói $\{H, S, CX\}$ đủ để xấp xỉ mọi cổng; đúng ra cần thêm $T$ (Clifford+T) | Kiến thức; bài 02_04 nói đúng |
| 02_05 | Cell kickback nhiều qubit hiển thị `ψ_in` của cell trước | Output "input" sai; output "output" đúng |
| 04_01 | `np.random.randint(1,3)` chỉ sinh hàm hằng (cần `randint(1,5)`) | Biểu đồ đúng/sai của thuật toán Deutsch lệch |
| 04_04 | `Uf_M_marked` có thể chọn trùng phần tử (output thật ra `['001', '001']`) | Oracle có thể không đánh dấu gì |

Ngoài ra còn một số lỗi đánh máy trong công thức, cũng đã ghi trong README từng phần.

> Output trong notebook do tác giả chạy. Bản sao này **chưa chạy lại** notebook trong môi trường của repo, nên
> nếu phiên bản Qiskit mới hơn đổi API thì có thể gặp lỗi khi chạy; khi đó hãy đối chiếu với repo gốc.

## Cấu trúc folder

```text
learnquantum/
├── README.md                 # file này: tổng quan, mục lục, cài đặt
├── LICENSE                   # MIT License của bản gốc (bắt buộc giữ)
├── requirements.txt          # thư viện cần cài
├── qiskit_settings.conf      # cấu hình hiển thị giống sách
├── 00_getting_started/       # README.md + 3 notebook + images/
├── 01_classical_computing/   # README.md + 4 notebook + images/
├── 02_quantum_computing/     # README.md + 5 notebook + images/
├── 03_quantum_protocols/     # README.md + 3 notebook + images/
└── 04_quantum_algorithms/    # README.md + 4 notebook + images/
```

Tên notebook giữ nguyên như bản gốc (`PP_BB_ten_bai.ipynb`, PP là phần, BB là bài) để dễ đối chiếu
với web và cập nhật khi bản gốc thay đổi.

## Cập nhật từ bản gốc

```bash
git clone --depth 1 https://github.com/learn-quantum/lqc-textbook.git /tmp/lqc
# so sánh rồi copy các notebook mới/đã sửa từ /tmp/lqc/chapters/<phần>/ vào learnquantum/<phần>/
```

Sau khi cập nhật, sửa commit và ngày trong bảng đầu file này, và bổ sung README của phần tương ứng.

## Giấy phép và trích dẫn

Nội dung notebook và hình minh hoạ © 2024 Diego Emilio Serrano, phát hành theo
[MIT License](LICENSE). Bản sao này giữ nguyên thông báo bản quyền theo yêu cầu của giấy phép.

Trích dẫn theo đề nghị của tác giả:

```bibtex
@book{learn-quantum,
    author = {Diego Emilio Serrano},
    year = {2024},
    title = {Learn Quantum Computing using Python},
    publisher = {Github},
    url = {learnquantum.io},
}
```
