# 00 · Getting started (Chuẩn bị môi trường)

**Tiếng Việt** · [English](README.en.md) · [简体中文](README.zh-CN.md)

Cài môi trường Python để chạy các notebook của sách, cấu hình Qiskit cho giống hình trong sách,
và (tuỳ chọn) liên kết tài khoản IBM Quantum để chạy trên máy lượng tử thật.

> Nguồn: [About](https://learnquantum.io/chapters/00_getting_started/00_00_welcome.html) ·
> [Setting your environment](https://learnquantum.io/chapters/00_getting_started/00_01_setting_env.html) ·
> [Configuring Qiskit](https://learnquantum.io/chapters/00_getting_started/00_02_qiskit_config.html)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## Mục lục

| Bài | Notebook | Web | Ý chính |
|---|---|---|---|
| 00_00 · About | [00_00_welcome.ipynb](00_00_welcome.ipynb) | [link](https://learnquantum.io/chapters/00_getting_started/00_00_welcome.html) | Cách dùng sách, nơi hỏi đáp, cách trích dẫn |
| 00_01 · Setting your environment | [00_01_setting_env.ipynb](00_01_setting_env.ipynb) | [link](https://learnquantum.io/chapters/00_getting_started/00_01_setting_env.html) | Cài Python, Jupyter, Qiskit, Aer, IBM Runtime; chạy code kiểm tra |
| 00_02 · Configuring Qiskit | [00_02_qiskit_config.ipynb](00_02_qiskit_config.ipynb) | [link](https://learnquantum.io/chapters/00_getting_started/00_02_qiskit_config.html) | Lưu token IBM Quantum; tệp `settings.conf` cho cách hiển thị |

## 00_00 · About the textbook (Giới thiệu sách)

Có hai cách dùng sách: đọc trên web rồi chép code vào môi trường của mình, hoặc tải notebook
từ repo [learn-quantum/lqc-textbook](https://github.com/learn-quantum/lqc-textbook).
Repo này đi theo cách thứ hai: notebook nằm trong `chapters/`.

- Hỏi đáp: mục [Discussions](https://github.com/learn-quantum/lqc-textbook/discussions) của repo gốc.
- Báo lỗi chính tả, bug: mục [Issues](https://github.com/learn-quantum/lqc-textbook/issues).
- Trích dẫn: Serrano, D.E. (2024). *Learn Quantum Computing using Python*. https://learnquantum.io.

## 00_01 · Setting up your environment (Cài đặt môi trường)

**Mục tiêu:** có một môi trường Python riêng, cài đủ thư viện để chạy mọi notebook.

### Các gói cần cài và vai trò

| Gói | Vai trò |
|---|---|
| `notebook` (Jupyter) | Mở và chạy các chương, vốn được viết dưới dạng notebook |
| `qiskit[visualization]` | Thư viện chính: tạo, mô phỏng, chạy mạch lượng tử; kéo theo NumPy, SymPy, Matplotlib |
| `qiskit-aer` | Simulator hiệu năng cao, có mô phỏng nhiễu (noisy simulator) |
| `qiskit-ibm-runtime` | Kết nối tới QPU (quantum processing unit) thật của IBM; cũng cung cấp `Estimator` dùng được với simulator |

### Cài đặt

Sách dùng `conda`. Repo này dùng `venv`, kết quả tương đương:

```bash
# conda (theo sách)
conda create --name learn-quantum python=3
conda activate learn-quantum
pip install "qiskit[visualization]" qiskit-aer qiskit-ibm-runtime notebook

# hoặc venv (theo repo này), chạy ở thư mục gốc repo
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1   |   Windows (cmd): .venv\Scripts\activate.bat
# macOS/Linux:          source .venv/bin/activate
pip install -r requirements.txt
```

Kích hoạt xong thì tên môi trường hiện ở đầu dòng lệnh: `(learn-quantum)` với conda, `(.venv)` với venv.
Hãy kiểm tra điều này trước khi chạy `pip install`.

<p align="center"><img src="images/00_01_02_terminal_window_learn.png" width="350" alt="Cửa sổ terminal: dòng đầu có tiền tố (base), sau lệnh conda activate learn-quantum thì tiền tố đổi thành (learn-quantum)"></p>

*Hình: trước khi kích hoạt, dòng lệnh bắt đầu bằng `(base)`; sau `conda activate learn-quantum` thì đổi thành `(learn-quantum)`.*

> Lưu ý: trên macOS (zsh) phải đặt `qiskit[visualization]` trong dấu nháy, vì zsh hiểu `[...]`
> là mẫu tên file. Trên Windows và bash thì không cần.

### Code kiểm tra môi trường

Đoạn code này dùng `display(...)`, nên phải chạy trong **một ô của notebook** (Jupyter hoặc VS Code), không chạy
bằng `python tên_file.py`.

```python
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_distribution
from qiskit_aer import AerSimulator

simulator = AerSimulator()

qc = QuantumCircuit(2,2)
qc.rx(np.pi/2,1)
qc.cx(1,0)
print("Statevector:")
display(Statevector(qc).draw('latex'))

qc.measure([1,0],[1,0])

print("Circuit:")
display(qc.draw('mpl'))

qc_t = transpile(qc, simulator)
counts = simulator.run(qc, shots=2**10).result().get_counts()

print("Probability Distribution:")
plot_distribution(counts)
```

Đoạn này dùng nhiều thành phần sẽ gặp suốt sách. **Bạn chưa cần hiểu chúng ngay**: lúc này chỉ cần chạy được,
mỗi khái niệm sẽ được giải thích kỹ ở Phần 01–02. Bảng dưới để tra khi tò mò.

| Dòng | Ý nghĩa |
|---|---|
| `QuantumCircuit(2,2)` | Mạch 2 qubit, 2 bit cổ điển để lưu kết quả đo |
| `qc.rx(np.pi/2,1)` | Xoay qubit 1 quanh trục X một góc π/2, tạo chồng chập (superposition) |
| `qc.cx(1,0)` | CNOT: qubit 1 điều khiển (control), qubit 0 là đích (target), tạo vướng víu (entanglement) |
| `Statevector(qc).draw('latex')` | Tính statevector chính xác, hiển thị dạng ket |
| `qc.measure([1,0],[1,0])` | Đo qubit 1 → bit 1, qubit 0 → bit 0 |
| `transpile(qc, simulator)` | Dịch mạch sang tập cổng mà backend hỗ trợ |
| `simulator.run(qc, shots=2**10)` | Chạy 1024 lần, `get_counts()` trả về số lần mỗi kết quả |
| `plot_distribution(counts)` | Vẽ phân bố xác suất |

**Kết quả mong đợi:** trạng thái có dạng $\tfrac{1}{\sqrt{2}}(|00\rangle - i|11\rangle)$ (chữ $i$ là đơn vị ảo,
sẽ học ở 02_03; hệ số $-i$ chỉ là một pha, không làm đổi xác suất của phép đo này), nên chỉ đo được `00` và `11`,
mỗi kết quả khoảng 50%. Output lưu trong notebook cho `00` ≈ 0.493 và `11` ≈ 0.507; lần chạy của bạn sẽ hơi khác.
Đoạn code chạy không lỗi là môi trường đã sẵn sàng. Riêng `qiskit-ibm-runtime` thì đoạn này chưa kiểm tra
(notebook cũng nói vậy); gói đó dùng ở 00_02 và khi gọi `Estimator`.

> Lưu ý: code tạo `qc_t = transpile(...)` nhưng lại chạy `simulator.run(qc, ...)` chứ không phải
> `qc_t`. Với AerSimulator vẫn chạy được, vì Aer tự hỗ trợ các cổng này; trên phần cứng thật cần
> chạy mạch đã transpile.

## 00_02 · Configuring Qiskit (Cấu hình Qiskit)

Cả hai bước đều **tuỳ chọn**.

### 1. Liên kết tài khoản IBM Quantum (chỉ cần khi chạy trên máy thật)

1. Tạo tài khoản ở https://quantum.ibm.com/, đăng nhập và copy API token ở góc trên bên phải trang chủ.

   <p align="center"><img src="images/00_02_01_api_token.png" width="700" alt="Trang chủ IBM Quantum Platform với ô API Token và nút copy ở góc trên bên phải"></p>

   *Hình: ô API Token trên trang chủ IBM Quantum Platform (giao diện cũ, lúc viết sách); nút copy nằm cạnh ô token.*

2. Chạy một lần:

   ```python
   from qiskit_ibm_runtime import QiskitRuntimeService
   QiskitRuntimeService.save_account('your-token-here')
   ```

Token được lưu ở `C:\Users\<tên>\.qiskit\qiskit-ibm.json` (Windows) hoặc `~/.qiskit/qiskit-ibm.json`
(macOS/Linux). **Không bao giờ commit token lên GitHub.**

> Lưu ý (có thể đã lỗi thời): hướng dẫn này theo bản gốc, vốn trỏ tới `quantum.ibm.com` và gọi `save_account` chỉ với token.
> Thư viện `qiskit-ibm-runtime` hiện hành (0.50.0) mô tả `token` là *IBM Cloud API key*, nhận kênh `ibm_cloud` hoặc
> `ibm_quantum_platform`, và có thêm tham số `instance`. Nền tảng IBM Quantum cũng đã chuyển sang
> `quantum.cloud.ibm.com`. Nếu bạn muốn chạy trên máy thật, hãy làm theo tài liệu hiện hành tại
> [quantum.cloud.ibm.com/docs](https://quantum.cloud.ibm.com/docs) thay vì các bước ở trên. Các notebook trong repo này đều chạy trên
> simulator nên không cần token.

### 2. Tệp cấu hình `settings.conf` (để hình giống hệt sách)

Tạo tệp `C:\Users\<tên>\.qiskit\settings.conf` (Windows) hoặc `~/.qiskit/settings.conf`
(macOS/Linux). Repo gốc dùng nội dung dưới đây (tệp `settings.conf` ở thư mục gốc của repo gốc); bản sao có sẵn ở
[qiskit_settings.conf](../../qiskit_settings.conf). Danh sách in trong notebook 00_02 hơi khác: dùng `iqp-dark`
và không có dòng `circuit_idle_wires`.

```ini
[default]
circuit_drawer = mpl
circuit_mpl_style = iqp
circuit_reverse_bits = True
circuit_idle_wires = False
state_drawer = latex
```

| Tuỳ chọn | Tác dụng |
|---|---|
| `circuit_drawer = mpl` | Vẽ mạch bằng matplotlib (hình màu) thay vì ký tự text |
| `circuit_mpl_style = iqp` | Bảng màu IBM Quantum; notebook gợi ý `iqp-dark` cho nền tối |
| `circuit_reverse_bits = True` | Đảo thứ tự qubit khi vẽ: qubit có chỉ số lớn nhất nằm trên cùng |
| `circuit_idle_wires = False` | Ẩn các dây qubit không có cổng nào |
| `state_drawer = latex` | Hiển thị statevector dạng ket bằng LaTeX thay vì mảng NumPy |

> **Quan trọng — thứ tự qubit.** Qiskit dùng quy ước little-endian: qubit 0 là bit **bên phải nhất**
> trong chuỗi kết quả, ví dụ `'01'` nghĩa là $q_1 = 0,\ q_0 = 1$. Nhiều tài liệu khác làm ngược lại.
> `circuit_reverse_bits = True` chỉ đổi **cách vẽ** mạch, không đổi kết quả tính. Nếu không đặt tệp
> này, mạch bạn vẽ ra sẽ bị lộn ngược so với hình trong sách, nhưng số liệu vẫn đúng.

## Ghi nhớ nhanh

- Chỉ cần 4 gói: `qiskit[visualization]`, `qiskit-aer`, `qiskit-ibm-runtime`, `notebook`.
- Chạy được đoạn code kiểm tra (ra `00`/`11` khoảng 50/50) là môi trường đã ổn (đoạn này chưa thử `qiskit-ibm-runtime`).
- Token IBM chỉ cần cho phần cứng thật; không bao giờ đưa token vào code commit.
- Muốn hình giống sách: copy [qiskit_settings.conf](../../qiskit_settings.conf) vào `~/.qiskit/settings.conf`.
- Chuỗi kết quả của Qiskit đọc từ phải sang trái: ký tự cuối là qubit 0.

> Các đoạn code trong README này được **trích nguyên văn** từ notebook. Chúng không cần biến của cell khác, nhưng
> đoạn kiểm tra môi trường phải chạy trong notebook vì dùng `display(...)`.

---

<!-- nav -->
[← Lộ trình học](../../docs/learning-path.md) · [Mục lục](../../README.md#mục-lục) · [01 · Classical computing →](../01_classical_computing/README.md)
