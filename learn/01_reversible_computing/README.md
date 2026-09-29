# 01 · Reversible computing

## Mục tiêu

Hiểu vì sao cổng lượng tử phải **khả nghịch**, thông qua hai cổng cổ điển khả nghịch là X và CX.

## Nội dung

- **X gate (NOT):** `a' = a ⊕ 1`.
- **CX gate (CNOT):** giữ nguyên control `a`, lật target `b` khi `a = 1`, tức `b' = a ⊕ b`.
  Đây là phép XOR khả nghịch.
- **CX · CX = I:** áp CX hai lần trả lại đúng input, nên CX là nghịch đảo của chính nó.

## Cách chạy

Mở `reversible_computing.ipynb` và chạy từ trên xuống dưới.

## Kết quả

| a | b | CX: a' | CX: b' | CX·CX: a'' | CX·CX: b'' |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 1 |
