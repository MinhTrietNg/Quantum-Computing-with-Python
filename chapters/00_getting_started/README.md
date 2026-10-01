# 00 · Getting started (Chuẩn bị môi trường)

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
Folder `learnquantum/` này là cách thứ hai.

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
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r learnquantum/requirements.txt
```

> Lưu ý: trên macOS (zsh) phải đặt `qiskit[visualization]` trong dấu nháy, vì zsh hiểu `[...]`
> là mẫu tên file. Trên Windows và bash thì không cần.

### Code kiểm tra môi trường

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

Đoạn này dùng đủ các thành phần sẽ gặp suốt sách:

| Dòng | Ý nghĩa |
|---|---|
| `QuantumCircuit(2,2)` | Mạch 2 qubit, 2 bit cổ điển để lưu kết quả đo |
| `qc.rx(np.pi/2,1)` | Xoay qubit 1 quanh trục X một góc π/2, tạo chồng chập (superposition) |
| `qc.cx(1,0)` | CNOT: qubit 1 điều khiển, qubit 0 là target, tạo vướng víu (entanglement) |
| `Statevector(qc).draw('latex')` | Tính statevector chính xác, hiển thị dạng ket |
| `qc.measure([1,0],[1,0])` | Đo qubit 1 → bit 1, qubit 0 → bit 0 |
| `transpile(qc, simulator)` | Dịch mạch sang tập cổng mà backend hỗ trợ |
| `simulator.run(qc, shots=2**10)` | Chạy 1024 lần, `get_counts()` trả về số lần mỗi kết quả |
| `plot_distribution(counts)` | Vẽ phân bố xác suất |

**Kết quả mong đợi:** trạng thái có dạng $\tfrac{1}{\sqrt{2}}(|00\rangle - i|11\rangle)$, nên chỉ đo được `00`
và `11`, mỗi kết quả khoảng 50%. Đoạn code chạy không lỗi là môi trường đã sẵn sàng.

> Lưu ý: code tạo `qc_t = transpile(...)` nhưng lại chạy `simulator.run(qc, ...)` chứ không phải
> `qc_t`. Với AerSimulator vẫn chạy được, vì Aer tự hỗ trợ các cổng này; trên phần cứng thật cần
> chạy mạch đã transpile.

## 00_02 · Configuring Qiskit (Cấu hình Qiskit)

Cả hai bước đều **tuỳ chọn**.

### 1. Liên kết tài khoản IBM Quantum (chỉ cần khi chạy trên máy thật)

1. Tạo tài khoản ở https://quantum.ibm.com/ và copy API token.
2. Chạy một lần:

   ```python
   from qiskit_ibm_runtime import QiskitRuntimeService
   QiskitRuntimeService.save_account('your-token-here')
   ```

Token được lưu ở `C:\Users\<tên>\.qiskit\qiskit-ibm.json` (Windows) hoặc `~/.qiskit/qiskit-ibm.json`
(macOS/Linux). **Không bao giờ commit token lên GitHub.** Các notebook trong folder này đều chạy trên
simulator nên không cần token.

### 2. Tệp cấu hình `settings.conf` (để hình giống hệt sách)

Tạo tệp `C:\Users\<tên>\.qiskit\settings.conf` (Windows) hoặc `~/.qiskit/settings.conf`
(macOS/Linux). Repo gốc dùng nội dung dưới đây; bản sao có sẵn ở
[../qiskit_settings.conf](../qiskit_settings.conf):

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
- Chạy được đoạn code kiểm tra (ra `00`/`11` khoảng 50/50) là môi trường đã ổn.
- Token IBM chỉ cần cho phần cứng thật; không bao giờ đưa token vào code commit.
- Muốn hình giống sách: copy [../qiskit_settings.conf](../qiskit_settings.conf) vào `~/.qiskit/settings.conf`.
- Chuỗi kết quả của Qiskit đọc từ phải sang trái: ký tự cuối là qubit 0.
