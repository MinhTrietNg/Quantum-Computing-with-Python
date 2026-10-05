# Lộ trình học

Trang này giúp bạn chọn điểm xuất phát, biết cần chuẩn bị gì, và tự kiểm tra sau mỗi phần.
Chưa biết máy tính lượng tử là gì? Đọc [Máy tính lượng tử là gì?](what-is-quantum-computing.md) trước (15 phút).

## Bạn bắt đầu từ đâu?

| Bạn là | Nên làm |
|---|---|
| **Tò mò, chưa lập trình** | Đọc [Máy tính lượng tử là gì?](what-is-quantum-computing.md) và [FAQ](faq.md). Rồi đọc sách mở *Quantum Computing for the Quantum Curious* (ít toán, xem [Tài nguyên](resources.md)). Muốn xem repo này mà không code: đọc mục *Ghi nhớ nhanh* của từng bài trong [Phần 02](../chapters/02_quantum_computing/README.md) và [Phần 03](../chapters/03_quantum_protocols/README.md); notebook đã có sẵn output nên không cần chạy gì. Khi muốn code, học Python cơ bản rồi quay lại |
| **Biết Python cơ bản** | Đi theo lộ trình đầy đủ bên dưới, từ Phần 00. Đây là đường dành cho đa số người đọc |
| **Biết Python và đại số tuyến tính** (vector, ma trận, số phức) | Làm Phần 00. Ở Phần 01: lướt 01_01, đọc 01_02 (cổng khả nghịch X, CX, CCX, nền của oracle), lướt 01_03 để nắm ký hiệu ket và tích Kronecker, lướt nhanh 01_04 (bit xác suất, mà 02_01 dùng để so sánh với qubit). (Nếu tích tensor/Kronecker còn lạ, hãy đọc kỹ 01_03.) Đọc kỹ từ Phần 02 |
| **Đã học cơ học lượng tử ở trường** | Đọc phần *Code chính* của [02_01](../chapters/02_quantum_computing/README.md) để làm quen cách Qiskit viết mạch, rồi 02_04, 02_05 và Phần 04 (nếu cú pháp cổng một qubit còn lạ, lướt thêm 02_03). Dùng repo như sổ tay Qiskit |

## Cần chuẩn bị gì

**Điều kiện thật sự cần: Python cơ bản.** Toán thì sách dạy dần: vector và ma trận ở Phần 01, số phức và
Bloch sphere ở 02_03. Học nhẹ nhàng hơn nếu bạn đã gặp chúng trước; xem mục *Ôn toán* bên dưới.

| Kỹ năng | Mức cần | Nếu còn yếu |
|---|---|---|
| **Python** | Biến, hàm, vòng lặp, list; biết `import` và đọc được code ngắn | Học một khoá Python cơ bản trước. Không cần biết NumPy; sách giải thích khi dùng |
| **Số nhị phân và logic** | Đổi nhị phân sang thập phân; biết AND, OR, XOR | Phần 01_01 dạy lại từ đầu |
| **Xác suất** | Xác suất của biến cố, tổng bằng 1; nhân xác suất của hai biến cố độc lập | Ôn lại kiến thức lớp 10 là đủ |
| **Đại số tuyến tính** | Nhân ma trận với vector | Phần 01_03 dạy; xem trước sẽ nhẹ hơn (mục *Ôn toán*) |
| **Số phức** | Biết $i^2 = -1$, môđun $\vert a+bi \vert$ | 02_03 dạy lại; xem trước sẽ nhẹ hơn |
| **Vật lý lượng tử** | Không cần | Sách dựng từ thí nghiệm Stern–Gerlach |

### Ôn toán (tuỳ chọn, 1–3 giờ)

Nếu chưa từng gặp ma trận hoặc số phức, hãy xem trước:

- [3Blue1Brown, *Essence of linear algebra*](https://www.3blue1brown.com/topics/linear-algebra): loạt video trực quan về vector
  và ma trận (xem bốn video đầu, tới phép nhân hai ma trận, là đủ cho Phần 01).
- [Khan Academy, Linear algebra](https://www.khanacademy.org/math/linear-algebra) (vector, ma trận) và
  [Precalculus](https://www.khanacademy.org/math/precalculus) (phần số phức): có bài tập tương tác, miễn phí.

### Tự kiểm tra (5 phút)

Trả lời nhanh mà không tra cứu.

1. Đoạn Python `for x in range(4): print(x * x)` in ra những số nào?
2. Số nhị phân `101` bằng bao nhiêu trong hệ thập phân? Còn `1 XOR 1`?
3. Tung hai đồng xu công bằng, xác suất cả hai ngửa là bao nhiêu?
4. Tính $\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}$.
5. Môđun của số phức $3+4i$ là bao nhiêu?

**Cách đọc kết quả:** sai câu 1 thì nên ôn Python trước. Sai câu 2 (nhị phân, XOR) thì không sao: 01_01 dạy lại từ đầu.
Sai câu 3 thì nên ôn lại xác suất mức lớp 10 (xác suất để hai biến cố độc lập cùng xảy ra), vì 01_04 và 02_02 dùng đúng
phép tính này.
Sai câu 4–5 thì **không sao**, vì sách dạy lại; nhưng nếu cả hai đều lạ, hãy xem mục *Ôn toán* ở trên.

<details>
<summary>Đáp án</summary>

1. `0`, `1`, `4`, `9` (mỗi số một dòng)
2. 5; và `1 XOR 1 = 0`
3. $1/4$
4. $\begin{pmatrix}0\\1\end{pmatrix}$ (ma trận này là cổng X, đổi $|0\rangle$ thành $|1\rangle$)
5. 5, vì $\sqrt{3^2 + 4^2} = 5$

</details>

## Lộ trình đầy đủ

```text
00 Cài đặt ─> 01 Cổ điển ─> 02 Lượng tử ─> 03 Giao thức ─> 04 Thuật toán ─> Học tiếp
               (vector,       (qubit, Bloch,    (teleportation,   (Deutsch–Jozsa → BV     (QFT, Shor,
                ma trận)       vướng víu, oracle) superdense)       → Simon → Grover)       VQE, ...)
```

Phần 01 trông "cổ điển" nhưng là bộ công cụ vector, ma trận và tích tensor mà mọi phần sau dùng lại.
Bài 02_05 (oracle, phase kickback) là nền của cả Phần 04.

Thời gian dưới đây là **ước tính** cho người học cẩn thận: đọc kỹ, tự gõ lại code, làm phần tự kiểm tra.
Người đọc lướt có thể nhanh hơn nhiều. Cộng năm phần dưới đây được khoảng 25–40 giờ (chưa tính mục *Ôn toán* tuỳ chọn),
tức 4–6 tuần nếu học một giờ mỗi ngày.

Mỗi phần có phần **tự kiểm tra** và **đáp án gợi ý**. Hãy tự trả lời trước khi mở đáp án.

### Phần 00 · Chuẩn bị ([README](../chapters/00_getting_started/README.md)), khoảng 1 giờ

Cài môi trường và chạy được đoạn code kiểm tra. Xem thêm [Cài đặt](setup.md).

**Làm được khi xong:** chạy được một notebook trên máy bạn và thấy kết quả `00`/`11` xấp xỉ 50/50.

### Phần 01 · Tính toán cổ điển ([README](../chapters/01_classical_computing/README.md)), khoảng 4–6 giờ

Bit, cổng logic, cổng khả nghịch, bit là vector và cổng là ma trận, bit xác suất.

**Tự kiểm tra:**
- Vì sao cổng AND không khả nghịch, còn cổng CX thì có?
- Viết ma trận $4 \times 4$ của cổng CX (bit điều khiển là bit bên trái trong ký hiệu ket) và kiểm tra nó biến $|10\rangle$ thành $|11\rangle$.
- Tích Kronecker của hai vector 2 chiều có mấy chiều? Với $n$ bit là bao nhiêu?

<details>
<summary>Đáp án gợi ý</summary>

- AND cho cùng đầu ra 0 với ba đầu vào khác nhau (`00`, `01`, `10`), nên từ đầu ra không suy ngược được đầu vào.
  CX biến $(a, b) \to (a, a \oplus b)$ nên suy ngược được; thật ra áp CX lần nữa là trở về đầu vào.
- Với thứ tự cơ sở $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ và bit trái là bit điều khiển, ma trận giữ nguyên hai hàng đầu
  và hoán đổi hai hàng cuối: $\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$.
  Cột ứng với $|10\rangle$ có số 1 ở hàng của $|11\rangle$, tức $|10\rangle \to |11\rangle$.
- $2 \times 2 = 4$ chiều; với $n$ bit là $2^n$ chiều.

</details>

### Phần 02 · Tính toán lượng tử ([README](../chapters/02_quantum_computing/README.md)), khoảng 10–15 giờ

Phần nặng nhất và quan trọng nhất: qubit, chồng chập, vướng víu, Bloch sphere, các cổng một và nhiều qubit,
phép đo, và các "khối dựng" (Bell, GHZ, W, oracle, phase kickback).
Nên chia thành nhiều buổi, và **đọc kỹ 02_05** vì Phần 04 dựa hoàn toàn vào nó.

**Tự kiểm tra:**
- Tính $H \cdot H|0\rangle$ bằng tay, rồi kiểm chứng bằng Qiskit. Vì sao kết quả là $|0\rangle$ chắc chắn?
- Tạo trạng thái Bell và giải thích vì sao chỉ đo được `00` hoặc `11`.
- $|+\rangle$ và $|-\rangle$ nằm ở đâu trên Bloch sphere? Hai trạng thái này khác nhau ở điểm nào nếu chỉ đo theo trục $z$?

<details>
<summary>Đáp án gợi ý</summary>

- Phép tính đầy đủ có ở [trang giới thiệu](what-is-quantum-computing.md#giao-thoa-tung-hai-lần-thì-kết-quả-chắc-chắn):
  biên độ của $|1\rangle$ là $+\tfrac12 - \tfrac12 = 0$ nên triệt tiêu, của $|0\rangle$ là $\tfrac12 + \tfrac12 = 1$.
- H trên qubit 0 rồi CX(0, 1) cho $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$. Biên độ của $|01\rangle$ và $|10\rangle$ bằng 0,
  nên xác suất đo ra chúng bằng 0.
- $|+\rangle$ nằm trên trục $+x$ và $|-\rangle$ trên trục $-x$ của Bloch sphere, cả hai ở đường xích đạo. Đo theo trục $z$
  cả hai cho 50/50 nên không phân biệt được. Chúng khác nhau ở dấu tương đối của biên độ (pha), lộ ra khi đo theo trục $x$ (tức áp H rồi đo: $|+\rangle \to$ `0`, $|-\rangle \to$ `1`).

</details>

### Phần 03 · Giao thức lượng tử ([README](../chapters/03_quantum_protocols/README.md)), khoảng 3–5 giờ

Ba ứng dụng đầu tiên của vướng víu và nguyên lý bất định: tiền lượng tử, teleportation, superdense coding.

**Tự kiểm tra:**
- Teleportation có gửi thông tin nhanh hơn ánh sáng không? Vì sao?
- Superdense coding và teleportation giống và khác nhau thế nào về tài nguyên dùng (qubit, bit cổ điển, cặp vướng víu)?
- Vì sao kẻ làm giả tiền lượng tử không thể sao chép đồng xu?

<details>
<summary>Đáp án gợi ý</summary>

- Không. Qubit của Bob chỉ trở thành đúng trạng thái cần gửi sau khi anh nhận **hai bit cổ điển** từ Alice, mà bit cổ điển
  thì không thể truyền nhanh hơn ánh sáng. Trước đó, những gì Bob thấy là ngẫu nhiên.
- Cả hai đều dùng **một cặp vướng víu** chia sẻ trước. Teleportation gửi **1 qubit** bằng cách truyền **2 bit cổ điển**;
  superdense coding ngược lại, gửi **2 bit cổ điển** bằng cách truyền **1 qubit**.
- Kẻ làm giả không biết mỗi qubit được chuẩn bị theo cơ sở nào (bit hay sign). Đo sai cơ sở thì làm hỏng trạng thái,
  còn định lý no-cloning cấm sao chép một trạng thái chưa biết, nên không có cách nào làm bản sao đáng tin: xác suất làm giả
  qua được kiểm tra giảm theo hàm mũ khi tăng số qubit (ví dụ $(3/4)^n$ với cách đo rồi chuẩn bị lại). Chi tiết ở 03_01.

</details>

### Phần 04 · Thuật toán lượng tử ([README](../chapters/04_quantum_algorithms/README.md)), khoảng 8–12 giờ

Deutsch–Jozsa, Bernstein–Vazirani và Simon dùng chung một khuôn (Hadamard → oracle → Hadamard → đo; Simon lặp khuôn này khoảng $n$ lần rồi giải hệ phương trình tuyến tính mod 2 trên máy cổ điển);
Grover lặp lại cặp "oracle + khuếch đại biên độ" khoảng (π/4)·√N lần.

**Tự kiểm tra:**
- Phase kickback là gì, và nó giúp oracle $U_f$ biến giá trị $f(x)$ thành dấu $(-1)^{f(x)}$ ra sao?
- Grover tìm 1 phần tử trong $N = 2^{20}$ mục cần khoảng bao nhiêu lần gọi oracle? (Gợi ý: $\tfrac{\pi}{4}\sqrt N$; so sánh với cổ điển.)
- Vì sao Deutsch–Jozsa "tăng tốc" nhưng không có ứng dụng thực tế?

<details>
<summary>Đáp án gợi ý</summary>

- Khi qubit đích ở trạng thái $|-\rangle$, oracle cho $U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle$: giá trị $f(x)$ "đá ngược"
  thành một dấu trên các qubit đầu vào, và dấu đó thì giao thoa dùng được. Chi tiết ở 02_05.
- $\tfrac{\pi}{4}\sqrt{2^{20}} \approx 804$ lần. Cổ điển cần trung bình khoảng $N/2 \approx 524\,000$ lần.
- Bài toán Deutsch–Jozsa là nhân tạo, được thiết kế để thể hiện lợi thế. Ngoài ra lợi thế chỉ có so với thuật toán cổ điển
  *chắc chắn đúng*; một thuật toán cổ điển ngẫu nhiên giải được với vài truy vấn và sai số rất nhỏ.

</details>

## Sau Phần 04 thì sao?

Sách gốc dự định có thêm các chương **QFT, QPE, Shor, HHL, mô phỏng Hamiltonian** nhưng tác giả chưa viết
(xem [chương chưa có nội dung](../README.md#các-chương-chưa-có-nội-dung-trên-web)). Trong lúc chờ, bạn có thể:

| Hướng | Gợi ý |
|---|---|
| Học tiếp tới Shor, QFT, QPE | Khoá *Fundamentals of quantum algorithms* của IBM (có Deutsch–Jozsa, Simon, QPE, Shor, Grover) và ghi chú của Preskill (cấp cao học), trong [Tài nguyên](resources.md) |
| Hiểu vướng víu sâu hơn (bất đẳng thức Bell, CHSH) | Khoá *Basics of quantum information* của IBM trong [Tài nguyên](resources.md) |
| Học thuật toán biến phân (VQE, QAOA) và quantum machine learning | PennyLane trong [Tài nguyên](resources.md) |
| Hiểu mối đe doạ với mật mã | Mục mật mã trong [FAQ](faq.md#về-mật-mã) |
| Chạy trên máy lượng tử thật | Hướng dẫn 00_02 trong [Phần 00](../chapters/00_getting_started/README.md) |

## Mẹo học

- **Chạy từng cell và đoán trước kết quả.** Nếu đoán sai, đó là chỗ đáng học nhất.
- **Đổi tham số rồi chạy lại.** Thay `shots`, đổi cổng, đổi qubit điều khiển.
- **Đừng sa lầy vào một công thức.** Sách đưa ví dụ cụ thể sau mỗi khái niệm; hiểu ví dụ rồi quay lại công thức.
- **Gặp thuật ngữ lạ thì tra** [bảng thuật ngữ](glossary.md).
- **Nghi ngờ sách sai?** Xem [ERRATA](../ERRATA.md): sách có một số lỗi nhỏ đã được ghi lại, bạn không cần tự phát hiện.
