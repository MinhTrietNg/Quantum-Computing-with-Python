# Quantum Computing Lab

Nơi mình vừa **học** vừa **thử nghiệm** quantum computing bằng Python.

- `learn/`: các bài học theo từng chủ đề, đi từ cơ bản đến nâng cao.
- `experiments/`: các thí nghiệm có câu hỏi rõ ràng, so sánh mô hình và ghi lại kết quả.

## Cấu trúc

Mọi bài học và thí nghiệm đều dùng chung một khuôn: **một folder `NN_ten_chu_de/`**,
bên trong có `README.md`, code và `figures/` (nếu có hình).

```text
.
├── learn/
│   ├── 01_reversible_computing/
│   │   ├── README.md
│   │   └── reversible_computing.ipynb
│   └── 02_parameter_shift_rule/
│       ├── README.md
│       ├── parameter_shift_demo.py   # file chạy
│       ├── circuit.py, gradients.py, plotting.py, ...
│       └── figures/
│
├── experiments/
│   └── 01_qnn_vs_mlp_fourier_regression/
│       ├── README.md
│       ├── qnn_data_reuploading.ipynb
│       └── mlp_baseline.ipynb
│
├── requirements.txt
└── README.md
```

| | Nội dung |
|---|---|
| [learn/01_reversible_computing](learn/01_reversible_computing) | X gate, CX gate, tính khả nghịch |
| [learn/02_parameter_shift_rule](learn/02_parameter_shift_rule) | Gradient của mạch có tham số bằng parameter-shift, shot noise |
| [experiments/01_qnn_vs_mlp_fourier_regression](experiments/01_qnn_vs_mlp_fourier_regression) | QNN data re-uploading vs MLP trên hàm Fourier |

## Cài đặt

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab                                                  # mở các notebook
python learn/02_parameter_shift_rule/parameter_shift_demo.py # chạy script
```

## Quy ước

**Khuôn folder (dùng cho cả `learn/` và `experiments/`)**

```text
NN_ten_chu_de/
├── README.md          # bắt buộc
├── <ten_chu_de>.ipynb # và/hoặc <ten>.py
└── figures/           # chỉ khi có hình
```

- Tên folder: `NN_snake_case`, số thứ tự 2 chữ số, đánh riêng trong `learn/` và `experiments/`.
- Tên file bên trong: `snake_case`, không cần số thứ tự.
- Code chạy độc lập bên trong folder của nó; hình lưu vào `figures/` cạnh code.

**README của bài học (`learn/`)**: `# NN · Tên`, rồi các mục *Mục tiêu*, *Nội dung*, *Cách chạy*, *Kết quả*.

**README của thí nghiệm (`experiments/`)**: `# NN · Tên`, rồi các mục *Câu hỏi*, *Setup*, *Cách chạy*,
*Kết quả*, *Vấn đề đã biết*.
- Các mô hình được so sánh phải dùng cùng dataset, cùng split và cùng ngân sách huấn luyện.
- Báo cáo mean ± std trên nhiều seed thay vì một lần chạy.

**Chung**
- Clear output trước khi commit để diff gọn.
- Khi code bắt đầu bị copy giữa nhiều notebook (dataset, optimizer, metrics, simulator),
  tách ra một package dùng chung, ví dụ `src/qlab/`.

## Lộ trình học (gợi ý)

- [x] 01 · Reversible computing: X, CX
- [x] 02 · Parameter-shift rule: gradient của mạch có tham số, shot noise
- [ ] 03 · Qubit, Bloch sphere, đo lường
- [ ] 04 · Single-qubit gates: H, S, T, rotations
- [ ] 05 · Multi-qubit, tensor product, entanglement, Bell states
- [ ] 06 · Quantum circuits với Qiskit / PennyLane
- [ ] 07 · Thuật toán: Deutsch–Jozsa, Bernstein–Vazirani, Grover
- [ ] 08 · QFT và phase estimation
- [ ] 09 · Variational algorithms: VQE, QAOA
- [ ] 10 · Quantum machine learning
