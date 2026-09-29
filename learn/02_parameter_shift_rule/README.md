# 02 · Parameter-shift rule

## Mục tiêu

Thấy trực quan cách parameter-shift rule tính gradient của một mạch lượng tử có tham số:
chạy **cùng một mạch** tại θ + π/2 và θ − π/2, rồi kết hợp hai kết quả thành ∂L/∂θ.

## Nội dung

Mạch 1 qubit: `|0> ── RY(θ) ── đo Z`, với L(θ) = ⟨Z⟩ = cos θ.

$$\frac{\partial L}{\partial \theta} = \frac{1}{2}\Big[L(\theta + \tfrac{\pi}{2}) - L(\theta - \tfrac{\pi}{2})\Big]$$

1. **Quantum circuit:** định nghĩa mạch bằng PennyLane và vẽ mạch.
2. **Parameter-shift gradient:** tính thủ công L_plus, L_minus và gradient, so với −sin θ.
3. **Cùng một mạch, chạy hai lần:** vẽ Circuit A (θ + π/2) và Circuit B (θ − π/2).
4. **Shot-based:** ước lượng gradient với 100 / 1,000 / 10,000 shots, lặp 500 lần, so std với lý thuyết.
5. **Ý chính:** gradient được dùng để cập nhật θ_new = θ − η · gradient.

## Cách chạy

```bash
python parameter_shift_demo.py               # θ0 = π/3
python parameter_shift_demo.py --theta 0.5   # góc khác
python parameter_shift_demo.py --no-show     # chỉ lưu hình, không mở cửa sổ
```

Hình được lưu vào `figures/`.

## Kết quả

Tại θ0 = π/3, gradient parameter-shift là −0.866025, trùng với −sin θ0 (sai số 0).

![L(θ), hai điểm shift và tangent tại θ0](figures/parameter_shift_tangent.png)

Đường nét đứt nối hai điểm shift có độ dốc −0.551, **không phải** gradient:
nó chia hiệu cho π, còn parameter-shift chia cho 2.

| shots | mean | std | std lý thuyết |
|---|---|---|---|
| 100 | −0.8665 | 0.0349 | 0.0354 |
| 1,000 | −0.8664 | 0.0105 | 0.0112 |
| 10,000 | −0.8662 | 0.0034 | 0.0035 |

![Phân bố gradient theo số shot](figures/shot_gradient_distributions.png)

Tăng số shot lên 10 lần thì variance giảm khoảng 10 lần: Var[g] = [(1 − L₊²) + (1 − L₋²)] / (4N).
