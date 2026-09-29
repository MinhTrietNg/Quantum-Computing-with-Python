# QNN vs MLP: Fourier regression

## Câu hỏi

Với cùng dataset, cùng split và số tham số gần bằng nhau, QNN data re-uploading có học hàm
Fourier nhiều tần số tốt hơn một MLP classical nhỏ không?

$$y(x)=\sin(2x)+0.5\sin(6x)+0.25\cos(10x), \quad x \in [-\pi, \pi]$$

## Setup

| | `qnn_data_reuploading.ipynb` | `mlp_baseline.ipynb` |
|---|---|---|
| Mô hình | 3 qubit, 4 re-uploading layers, CNOT ring, linear readout | MLP 1 → 5 → 4 → 1, tanh |
| Tham số | 40 | 39 |
| Gradient | Parameter-shift | Backprop |
| Dataset | 400 điểm, `SEED = 42`, split 70/15/15 (`SEED + 1`) | giống QNN |

Hai notebook in ra checksum của split (`55766 12353 11681`) để kiểm tra chúng dùng cùng dữ liệu.

## Cách chạy

Mở và chạy từng notebook từ trên xuống dưới. MLP chạy mất khoảng 1 giây, QNN khoảng 45 giây.

## Kết quả hiện tại

| | MLP | QNN (như notebook hiện tại) |
|---|---|---|
| Số bước tối ưu | 2,250 (250 epoch × 9 batch × 32 mẫu) | 20 (20 bước × 8 mẫu) |
| Test MSE | 0.184 | 0.552 |
| Test R² | 0.74 | 0.21 |

## Vấn đề đã biết (TODO)

- **Ngân sách huấn luyện không ngang nhau.** Với cùng protocol như MLP (2,250 bước, batch 32,
  lr 0.01, 3 seed), QNN đạt test MSE 0.002 ± 0.001 (R² 0.997), còn MLP đạt 0.32 ± 0.22.
  Kết quả trong bảng trên vì vậy phản ánh số bước huấn luyện, không phản ánh mô hình.
  Cần vectorize simulator theo batch để QNN huấn luyện đủ bước trong thời gian hợp lý.
- **Một seed là không đủ.** Test MSE của MLP dao động 0.165–0.636 giữa các seed.
- **Inductive bias.** Tần số encoding {1, 2, 3} được chọn để khớp các tần số 2, 6, 10 của target.
  Nên thêm baseline classical dùng feature sin/cos để tách tác dụng của inductive bias khỏi tính lượng tử.
- **Chưa có tuning thật.** Learning rate khác nhau (MLP 0.01, QNN 0.03) và chưa có code tìm hyperparameter.
