# Quantum Computing with Python

[![Notebooks](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/actions/workflows/notebooks.yml/badge.svg)](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/actions/workflows/notebooks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-6929C4)

**Học máy tính lượng tử từ con số 0, bằng tiếng Việt và Python.**
Miễn phí. Không cần biết vật lý lượng tử, không cần máy lượng tử, chạy được trên laptop thường.
Chỉ cần **Python cơ bản**; phần toán được dạy dần.

Mục tiêu sau khoảng 4–6 tuần học đều (ước tính, mỗi ngày một giờ): hiểu qubit, chồng chập, vướng víu và giao thoa
là gì, tự viết và chạy được mạch lượng tử bằng Qiskit, và giải thích được teleportation cùng các thuật toán
Deutsch–Jozsa, Bernstein–Vazirani, Simon và Grover.

## Thử ngay

Đây là toàn bộ một chương trình lượng tử. Nó tạo hai qubit **vướng víu**, rồi đo chúng 1000 lần:

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)             # cổng H: đưa qubit 0 (bit lượng tử) vào trạng thái 50/50 giữa 0 và 1
qc.cx(0, 1)         # cổng CX: ràng buộc qubit 1 với qubit 0 (vướng víu)
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
# {'11': 496, '00': 504}
```

`shots=1000` nghĩa là chạy mạch và đo 1000 lần; số của bạn sẽ hơi khác số ở trên vì phép đo là ngẫu nhiên.
Kết quả chỉ có `00` hoặc `11`, **không bao giờ** `01` hay `10`: từng qubit riêng lẻ là ngẫu nhiên 50/50,
nhưng hai qubit luôn trùng nhau. (Máy thật có nhiễu nên thỉnh thoảng lọt ra vài `01`/`10`; simulator lý tưởng thì không.)
Vì sao lại vậy, và vì sao riêng điều này *chưa* đủ để gọi là lượng tử? Phần vướng víu được học ở Phần 02; bằng chứng
đầy đủ (bất đẳng thức Bell) thì sách gốc chưa viết, xem [Tài nguyên](docs/resources.md).

**Chưa cài Qiskit?** Mở [Google Colab](https://colab.research.google.com) rồi chọn *New notebook*, chạy `%pip install -q qiskit qiskit-aer`
trong một ô, rồi dán đoạn code trên vào ô mới. Cài trên máy bạn thì xem mục [Bắt đầu](#bắt-đầu).

**Bước tiếp theo:**
[Chưa cài gì? Chạy bằng Google Colab](docs/setup.md#2-google-colab-không-cần-cài) ·
[Đọc giới thiệu 15 phút](docs/what-is-quantum-computing.md) ·
[Xem lộ trình học](docs/learning-path.md)

## Dành cho ai

| Bạn là | Bắt đầu từ |
|---|---|
| **Tò mò, chưa lập trình** | [Máy tính lượng tử là gì?](docs/what-is-quantum-computing.md), 15 phút, ít toán (phân số và căn bậc hai); rồi xem [Lộ trình học](docs/learning-path.md) |
| **Biết Python cơ bản** | [Lộ trình học](docs/learning-path.md), rồi bắt đầu từ [Phần 00](chapters/00_getting_started/) |
| **Biết Python và đại số tuyến tính** | [Lộ trình học](docs/learning-path.md) chỉ cách lướt Phần 01 và vào thẳng Phần 02 |
| **Đã học cơ học lượng tử** | Đọc phần *Code chính* của [02_01](chapters/02_quantum_computing/) (mạch Qiskit đầu tiên), rồi 02_04, 02_05 và [Phần 04](chapters/04_quantum_algorithms/) (nếu cú pháp cổng một qubit còn lạ, lướt thêm 02_03) |
| Tra thuật ngữ | [Bảng thuật ngữ](docs/glossary.md) |
| Muốn biết máy lượng tử có phá được mã hoá không | [FAQ](docs/faq.md#về-mật-mã) |

## Bắt đầu

Ba cách, từ dễ đến đầy đủ ([hướng dẫn chi tiết](docs/setup.md)):

1. **Chỉ đọc:** mở [mục lục](#mục-lục) bên dưới, chọn một bài. GitHub hiển thị notebook kèm output có sẵn.
2. **Chạy trên Google Colab:** không cần cài gì ([cách làm](docs/setup.md#2-google-colab-không-cần-cài)).
3. **Chạy trên máy** (cần Python 3.11 trở lên; repo được kiểm thử với 3.11 và 3.12):

   ```bash
   git clone https://github.com/MinhTrietNg/Quantum-Computing-with-Python.git
   cd Quantum-Computing-with-Python
   python -m venv .venv
   # Windows (PowerShell): .venv\Scripts\Activate.ps1   |   Windows (cmd): .venv\Scripts\activate.bat
   # macOS/Linux:          source .venv/bin/activate
   pip install -r requirements.txt
   jupyter notebook chapters/
   ```

   Gặp vướng mắc (chưa có Python, lỗi PowerShell, không dùng git, ...)? Xem [hướng dẫn chi tiết và gỡ lỗi](docs/setup.md).

Cả 19 notebook đã được kiểm thử chạy được ([phiên bản cụ thể](docs/setup.md#phiên-bản-đã-kiểm-thử)),
và CI kiểm tra lại hằng tuần.

## Lộ trình

Đọc theo thứ tự **Phần 00 → 01 → 02 → 03 → 04**, khoảng 25–40 giờ cho người học cẩn thận (4–6 tuần với một giờ mỗi
ngày). [Lộ trình học](docs/learning-path.md) có sơ đồ, thời gian từng phần, bài tự kiểm tra kèm đáp án gợi ý,
và cách đi tắt nếu bạn đã có nền tảng.

Mỗi phần có hướng dẫn tiếng Việt riêng gồm kiến thức chính, code chính, kết quả và **ghi nhớ nhanh** để ôn lại.

## Mục lục

| Phần | Bài | Notebook | Nội dung |
|---|---|---|---|
| **[00 · Getting started](chapters/00_getting_started/)** | 00_00 | [About the textbook](chapters/00_getting_started/00_00_welcome.ipynb) | Cách dùng sách, trích dẫn |
| | 00_01 | [Setting up your environment](chapters/00_getting_started/00_01_setting_env.ipynb) | Cài Qiskit, code kiểm tra môi trường |
| | 00_02 | [Configuring Qiskit](chapters/00_getting_started/00_02_qiskit_config.ipynb) | Token IBM Quantum, `settings.conf` |
| **[01 · Classical computing](chapters/01_classical_computing/)** | 01_01 | [Bits and digital circuits](chapters/01_classical_computing/01_01_bits_and_circuits.ipynb) | Bit, cổng logic, mạch cộng |
| | 01_02 | [Reversible computing](chapters/01_classical_computing/01_02_reversible_computing.ipynb) | Cổng khả nghịch X, CX, CCX |
| | 01_03 | [Linear algebra for reversible circuits](chapters/01_classical_computing/01_03_bits_to_vectors.ipynb) | Bit là vector, cổng là ma trận, tích tensor |
| | 01_04 | [Probabilistic computing](chapters/01_classical_computing/01_04_probabilistic_circuits.ipynb) | Bit xác suất, mạch có nhiễu |
| **[02 · Quantum computing](chapters/02_quantum_computing/)** | 02_01 | [Qubits and quantum circuits](chapters/02_quantum_computing/02_01_bits_to_qubits.ipynb) | Thí nghiệm Stern–Gerlach, từ bit đến qubit |
| | 02_02 | [Quantum entanglement](chapters/02_quantum_computing/02_02_entanglement.ipynb) | Trạng thái tách được và vướng víu; tạo vướng víu bằng H + CX |
| | 02_03 | [Single-qubit systems](chapters/02_quantum_computing/02_03_single_qb_sys.ipynb) | Biên độ phức, Bloch sphere, cổng một qubit, phép đo, observable |
| | 02_04 | [Multi-qubit systems](chapters/02_quantum_computing/02_04_multi_qb_sys.ipynb) | Cổng điều khiển, SWAP, no-cloning, bộ cổng phổ quát, đo một phần |
| | 02_05 | [Quantum building blocks](chapters/02_quantum_computing/02_05_quantum_blocks.ipynb) | Bell/GHZ/W, biến đổi Hadamard, phase kickback, oracle |
| **[03 · Quantum protocols](chapters/03_quantum_protocols/)** | 03_01 | [Uncertainty & quantum money](chapters/03_quantum_protocols/03_01_quantum_money.ipynb) | Nguyên lý bất định; tiền lượng tử Wiesner: càng nhiều qubit càng khó làm giả |
| | 03_02 | [Quantum teleportation](chapters/03_quantum_protocols/03_02_teleportation.ipynb) | Dịch chuyển trạng thái lượng tử |
| | 03_03 | [Superdense coding](chapters/03_quantum_protocols/03_03_superdense_coding.ipynb) | Gửi 2 bit cổ điển bằng 1 qubit |
| **[04 · Foundational quantum algorithms](chapters/04_quantum_algorithms/)** | 04_01 | [Deutsch–Jozsa](chapters/04_quantum_algorithms/04_01_deutsch-jozsa.ipynb) | Hàm hằng hay cân bằng, 1 lần truy vấn |
| | 04_02 | [Bernstein–Vazirani](chapters/04_quantum_algorithms/04_02_bernstein-vazirani.ipynb) | Tìm chuỗi bí mật, 1 lần truy vấn |
| | 04_03 | [Simon's algorithm](chapters/04_quantum_algorithms/04_03_simons.ipynb) | Tìm chu kỳ XOR, tăng tốc hàm mũ (trong mô hình oracle) |
| | 04_04 | [Grover's algorithm](chapters/04_quantum_algorithms/04_04_grover.ipynb) | Tìm kiếm không cấu trúc, tăng tốc căn bậc hai |

### Các chương chưa có nội dung trên web

Ở bản gốc, các chương sau mới chỉ có tiêu đề (notebook trống) nên **chưa được đưa vào** repo này.
Khi tác giả viết xong, repo sẽ được cập nhật; trong lúc chờ, xem [tài nguyên học tiếp](docs/resources.md).

| Phần | Chương |
|---|---|
| 03 · Quantum protocols | 03_04 Bell inequalities, 03_05 Quantum key distribution |
| 05 · Important quantum primitives | 05_01 QFT, 05_02 QPE, 05_03 Amplitude amplification |
| 06 · Advanced quantum algorithms | 06_01 Shor, 06_02 HHL, 06_03 Hamiltonian simulation |

## Tài liệu bổ trợ

| | |
|---|---|
| [Máy tính lượng tử là gì?](docs/what-is-quantum-computing.md) | Bức tranh tổng quan, giao thoa, vướng víu, nó giỏi và không giỏi gì |
| [Lộ trình học](docs/learning-path.md) | Cần biết gì trước, thời gian dự kiến, bài tự kiểm tra từng phần |
| [Cài đặt](docs/setup.md) | Đọc, Colab hay chạy trên máy; gỡ lỗi thường gặp |
| [Bảng thuật ngữ](docs/glossary.md) | Thuật ngữ Việt–Anh kèm nơi học |
| [FAQ](docs/faq.md) | Hiểu lầm phổ biến, mật mã, chọn thư viện |
| [Tài nguyên](docs/resources.md) | Sách, khoá học, tài liệu học tiếp |
| [ERRATA](ERRATA.md) | Các lỗi đã biết trong sách gốc |

## Nguồn gốc và cập nhật

Notebook và hình trong [chapters/](chapters/) là **bản sao nguyên văn** của sách mở
**[Learn Quantum Computing using Python](https://learnquantum.io)** (Diego Emilio Serrano), kể cả output tác giả đã chạy
và vài lỗi nhỏ của sách gốc (đã ghi trong [ERRATA](ERRATA.md) và ở các mục `> Lưu ý` trong README từng phần, nên bạn không cần tự phát hiện). Phần do repo này viết là README tiếng Việt của từng phần,
thư mục [docs/](docs/), kiểm thử tự động và các công cụ đi kèm.

| | |
|---|---|
| Repo gốc | [learn-quantum/lqc-textbook](https://github.com/learn-quantum/lqc-textbook) |
| Bản sao lấy từ | commit [`7abf73c`](https://github.com/learn-quantum/lqc-textbook/commit/7abf73cb1d430e0eba1d052d8b4d8bc976e956f6) (2026-03-20), lấy về ngày 2026-09-30 |

Để biết bản gốc có gì mới: `python scripts/check_upstream.py`. Quy trình cập nhật ở
[CONTRIBUTING](CONTRIBUTING.md#cập-nhật-từ-bản-gốc).

## Cấu trúc repo

```text
.
├── chapters/             # sách: mỗi phần một folder (README tiếng Việt + notebook + images/)
├── docs/                 # tài liệu nhập môn: giới thiệu, lộ trình, cài đặt, thuật ngữ, FAQ, tài nguyên
├── scripts/              # check_upstream.py (so sánh với repo gốc), check_links.py, check_doc_snippets.py
├── .github/              # CI chạy notebook, mẫu issue và pull request
├── ERRATA.md, CONTRIBUTING.md, CITATION.cff, LICENSE
├── qiskit_settings.conf  # cấu hình hiển thị giống sách
└── requirements.txt, requirements-dev.txt, pyproject.toml
```

## English summary

A beginner-friendly Vietnamese guide to quantum computing: 19 runnable Qiskit notebooks from the open textbook
[learnquantum.io](https://learnquantum.io) by Diego Emilio Serrano (MIT License), kept verbatim, plus a Vietnamese
walkthrough of every chapter, introductory docs (what quantum computing is, learning path, setup, glossary, FAQ,
resources), an [errata list](ERRATA.md), and CI that re-runs every notebook weekly. The notebooks and figures are
copied unmodified; the Vietnamese material is original to this repo.

## Đóng góp

Mọi góp ý đều được hoan nghênh: sửa lỗi dịch, giải thích chưa rõ, bổ sung tài liệu cho người mới, báo lỗi trong
sách hoặc notebook không chạy với Qiskit mới. Xem [CONTRIBUTING](CONTRIBUTING.md). Lỗi của chính sách nên báo thêm
tại [Issues của repo gốc](https://github.com/learn-quantum/lqc-textbook/issues).

## Giấy phép và trích dẫn

Notebook và hình minh hoạ © 2024 Diego Emilio Serrano, phát hành theo [MIT License](LICENSE).
Phần hướng dẫn tiếng Việt và tài liệu bổ trợ được chia sẻ theo cùng giấy phép.
Khi dùng nội dung, hãy trích dẫn sách gốc (GitHub hiện nút *Cite this repository* từ [CITATION.cff](CITATION.cff)):

```bibtex
@book{learn-quantum,
    author = {Diego Emilio Serrano},
    year = {2024},
    title = {Learn Quantum Computing using Python},
    publisher = {Github},
    url = {learnquantum.io},
}
```

Cảm ơn tác giả Diego Emilio Serrano đã viết và chia sẻ miễn phí cuốn sách này.
