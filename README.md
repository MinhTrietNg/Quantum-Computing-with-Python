# Quantum Computing Lab

Nơi mình vừa **học** vừa **thử nghiệm** quantum computing bằng Python.

- `learn/`: notebook học theo từng chủ đề, đi từ cơ bản đến nâng cao.
- `experiments/`: các thí nghiệm có câu hỏi rõ ràng, so sánh mô hình và ghi lại kết quả.

## Cấu trúc

```text
.
├── learn/                              # Học lý thuyết + code từng khái niệm
│   └── 01_reversible_computing.ipynb   # X gate, CX gate, tính khả nghịch
│
├── experiments/                        # Mỗi thí nghiệm là một folder riêng
│   └── qnn-vs-mlp-fourier-regression/
│       ├── README.md                   # Câu hỏi, cách chạy, kết quả
│       ├── qnn_data_reuploading.ipynb  # QNN data re-uploading (NumPy state vector)
│       └── mlp_baseline.ipynb          # Baseline classical MLP
│
├── requirements.txt
└── README.md
```

## Cài đặt

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Quy ước

**`learn/`**
- Tên file: `NN_chu_de.ipynb` (ví dụ `02_qubits_and_bloch_sphere.ipynb`) để giữ thứ tự học.
- Mỗi notebook tập trung vào một khái niệm và có thể chạy độc lập từ trên xuống dưới.

**`experiments/`**
- Mỗi thí nghiệm là một folder `ten-thi-nghiem/`, có `README.md` ghi:
  câu hỏi, setup (dataset, seed, số tham số, ngân sách huấn luyện), cách chạy, kết quả và kết luận.
- Các mô hình được so sánh phải dùng cùng dataset, cùng split và cùng ngân sách huấn luyện.
- Báo cáo mean ± std trên nhiều seed thay vì một lần chạy.

**Chung**
- Clear output trước khi commit để diff gọn.
- Khi code bắt đầu bị copy giữa nhiều notebook (dataset, optimizer, metrics, simulator),
  tách ra một package dùng chung, ví dụ `src/qlab/`.

## Lộ trình học (gợi ý)

- [x] 01 · Reversible computing: X, CX
- [ ] 02 · Qubit, Bloch sphere, đo lường
- [ ] 03 · Single-qubit gates: H, S, T, rotations
- [ ] 04 · Multi-qubit, tensor product, entanglement, Bell states
- [ ] 05 · Quantum circuits với Qiskit / PennyLane
- [ ] 06 · Thuật toán: Deutsch–Jozsa, Bernstein–Vazirani, Grover
- [ ] 07 · QFT và phase estimation
- [ ] 08 · Variational algorithms: VQE, QAOA
- [ ] 09 · Quantum machine learning
