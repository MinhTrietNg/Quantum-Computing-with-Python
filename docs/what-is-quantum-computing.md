# Máy tính lượng tử là gì?

**Tiếng Việt** · [English](what-is-quantum-computing.en.md) · [简体中文](what-is-quantum-computing.zh-CN.md)

*Đọc mất khoảng 15 phút. Không cần biết vật lý lượng tử; chỉ cần Python cơ bản nếu muốn chạy thử code.
Cách chạy: [Google Colab hoặc trên máy bạn](setup.md).*

## Một câu trả lời trung thực

Máy tính lượng tử là máy tính lưu và xử lý thông tin bằng các hiện tượng của cơ học lượng tử.
Nó **không** phải là laptop nhanh hơn, và **không** "thử mọi đáp án cùng lúc". Nó là một công cụ khác,
về lý thuyết giỏi một số loại bài toán rất cụ thể (nhiều bài cần máy lớn hơn và ít lỗi hơn hẳn máy hiện nay),
và không giúp gì cho phần lớn việc bạn làm với máy tính hằng ngày.

Phần còn lại của trang này giải thích câu trên nghĩa là gì.

## Từ bit đến qubit

Máy tính thường lưu thông tin bằng **bit**: mỗi bit là `0` hoặc `1`.

Máy tính lượng tử dùng **qubit**. Trạng thái của một qubit được mô tả bằng hai con số gọi là **biên độ**
(amplitude), $\alpha$ và $\beta$:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1$$

Cách đọc ký hiệu:

- $|0\rangle$ đọc là "ket 0". Nó chỉ là **tên** của trạng thái "qubit đang là 0"; $|1\rangle$ tương tự.
- $\alpha$ và $\beta$ là hai biên độ. Khác với xác suất, chúng có thể **âm**, và thậm chí là *số phức*
  (số có phần ảo). Lúc đầu bạn chỉ cần nghĩ chúng là các số, có thể âm.
- $|\alpha|^2$ là bình phương độ lớn của $\alpha$; với số thực, nó chỉ là $\alpha^2$.
- Điều kiện bên phải nói: hai xác suất cộng lại bằng 100%.

Khi **đo**, bạn luôn nhận được một bit bình thường: `0` với xác suất $|\alpha|^2$, `1` với xác suất $|\beta|^2$.
Sau khi đo, qubit "chốt" vào kết quả đó. Phép đo không cho bạn thấy $\alpha$ và $\beta$.

Hai điểm khiến qubit khác một bit "xác suất" bình thường (như đồng xu chưa lật):

1. Biên độ có thể **âm hoặc phức**, không chỉ là số dương như xác suất.
2. Biên độ có thể **triệt tiêu hoặc cộng gộp** với nhau. Đây gọi là *giao thoa*, và cùng với vướng víu là chìa khoá
   cho sức mạnh của máy tính lượng tử (xem bên dưới).

## Ba ý tưởng cần nhớ

| Ý tưởng | Nói đơn giản | Học kỹ ở |
|---|---|---|
| **Chồng chập** (superposition) | Qubit đang ở **một trạng thái xác định**, mô tả bằng hai biên độ $\alpha, \beta$ như trên. Chồng chập (so với $\vert 0\rangle, \vert 1\rangle$) là khi **cả hai biên độ đều khác 0**, ví dụ $\alpha = \beta = 1/\sqrt2$; còn $\vert 0\rangle$ có $\alpha = 1, \beta = 0$ nên không phải chồng chập. Nó **không** phải "vừa 0 vừa 1"; đó chỉ là cách nói gọn dễ gây hiểu lầm | [02_01](../chapters/02_quantum_computing/README.md#02_01--qubits-and-quantum-circuits-qubit-và-mạch-lượng-tử) |
| **Vướng víu** (entanglement) | Hai qubit gắn với nhau đến mức không thể mô tả riêng từng qubit; khi đo theo nhiều hướng khác nhau, kết quả của chúng tương quan theo cách mà không "đồng xu ghép sẵn" nào làm được | [02_02](../chapters/02_quantum_computing/README.md#02_02--quantum-entanglement-vướng-víu-lượng-tử) |
| **Giao thoa** (interference) | Các biên độ cộng gộp hoặc triệt tiêu nhau. Thuật toán lượng tử được thiết kế để các đáp án sai triệt tiêu còn đáp án đúng được khuếch đại | [Phần 04](../chapters/04_quantum_algorithms/README.md) |

## Chương trình lượng tử đầu tiên

Ta dùng Qiskit, một thư viện Python mã nguồn mở, để mô phỏng máy tính lượng tử ngay trên máy bạn.
`shots=1000` nghĩa là chạy mạch và đo 1000 lần; kết quả là bảng đếm xem mỗi đáp án xuất hiện bao nhiêu lần.
Vì đo là ngẫu nhiên, **số của bạn sẽ hơi khác số trong tài liệu**.

Hai từ cần biết trước: **cổng** (gate) là một phép biến đổi áp lên qubit (như `h` và `cx` bên dưới), và **mạch**
(circuit) là chuỗi cổng rồi đến phép đo. Mục [Đọc một mạch lượng tử](#đọc-một-mạch-lượng-tử) giải thích cách đọc hình vẽ.

### Một qubit tung đồng xu

Cổng **Hadamard** (cổng H) biến $|0\rangle$ thành $\tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$, tức hai biên độ bằng nhau,
mỗi bên xác suất 50%.

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)             # cổng Hadamard
qc.measure_all()    # đo

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'1': 497, '0': 503}      # ví dụ; mỗi lần chạy ra số khác nhưng luôn gần 50/50
```

### Giao thoa: tung hai lần thì kết quả chắc chắn

Thêm **một cổng H nữa** ngay sau cổng H đầu:

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)
qc.h(0)             # cổng H lần thứ hai
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'0': 1000}
```

Nếu qubit chỉ là "đồng xu ngẫu nhiên", tung thêm lần nữa vẫn ngẫu nhiên. Nhưng kết quả lại **luôn là `0`**.
Hãy tự tính. Cổng H biến đổi hai trạng thái cơ bản như sau (lưu ý **dấu trừ**):

$$H|0\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big), \qquad H|1\rangle = \tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)$$

Áp H lần thứ hai lên $\tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$, tức áp lên từng phần rồi cộng lại:

$$\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\big(|0\rangle + |1\rangle\big) + \tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)
= \tfrac12\big(|0\rangle + |1\rangle\big) + \tfrac12\big(|0\rangle - |1\rangle\big) = |0\rangle$$

Biên độ của $|1\rangle$ nhận hai đóng góp $+\tfrac12$ và $-\tfrac12$, nên **triệt tiêu**. Biên độ của $|0\rangle$ nhận
$+\tfrac12$ và $+\tfrac12$, nên **cộng gộp** thành 1. Xác suất không giải thích được điều này, vì xác suất không bao
giờ âm. Biên độ thì có thể.

Đây là ý tưởng cốt lõi: **thuật toán lượng tử sắp xếp để các đường dẫn tới đáp án sai triệt tiêu nhau.**

### Vướng víu: hai qubit luôn đồng ý với nhau

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)         # qubit 0: biên độ bằng nhau cho 0 và 1
qc.cx(0, 1)     # cổng CX: đảo qubit 1 nếu qubit 0 là 1  -> hai qubit vướng víu
qc.measure_all()

print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

```text
{'11': 496, '00': 504}      # ví dụ; số cụ thể mỗi lần một khác
```

Mạch trông như sau (đọc từ trái sang phải): ô `H` là cổng Hadamard; chấm `■` nối với ô `X` là cổng CX (chấm ở qubit
điều khiển, ô `X` ở qubit đích); `M` là phép đo; `░` là *barrier* (vạch ngăn) mà `measure_all()` tự chèn vào, không làm thay đổi trạng thái.

```text
        ┌───┐      ░ ┌─┐   
   q_0: ┤ H ├──■───░─┤M├───
        └───┘┌─┴─┐ ░ └╥┘┌─┐
   q_1: ─────┤ X ├─░──╫─┤M├
             └───┘ ░  ║ └╥┘
meas: 2/══════════════╩══╩═
                      0  1 
```

Kết quả chỉ có `00` hoặc `11`, **không bao giờ** `01` hay `10` (trên máy thật, nhiễu đôi khi làm lọt ra vài kết
quả `01`/`10`; simulator lý tưởng thì không). Từng qubit riêng lẻ là ngẫu nhiên 50/50, nhưng hai qubit luôn trùng nhau.

**Chỉ riêng điều này chưa đủ để gọi là lượng tử.** Hai đồng xu bỏ trong hai phong bì, được ghép trùng nhau từ trước,
cũng cho kết quả giống hệt. Chỗ khác biệt thật sự chỉ lộ ra khi đo theo **nhiều hướng khác nhau**: khi đó các tương
quan mạnh hơn mọi cách "ghép sẵn" có thể tạo ra (đó là nội dung của *bất đẳng thức Bell*, ví dụ trò chơi CHSH). Bạn sẽ thấy
trạng thái này không thể viết thành "hai qubit độc lập" ở [02_02](../chapters/02_quantum_computing/README.md#02_02--quantum-entanglement-vướng-víu-lượng-tử).
Chương Bell inequalities của sách gốc chưa có nội dung; khoá của IBM trong [Tài nguyên](resources.md) có phần này.

Trạng thái trên gọi là *trạng thái Bell*, và là nền cho
[teleportation](../chapters/03_quantum_protocols/README.md#03_02--quantum-teleportation-dịch-chuyển-trạng-thái-lượng-tử)
và superdense coding.

## Đọc một mạch lượng tử

Mạch lượng tử đọc từ **trái sang phải** theo thời gian. Mỗi đường ngang là một qubit, mỗi ô là một cổng
(phép biến đổi), biểu tượng đồng hồ đo là phép đo. Đường đôi là bit cổ điển mang kết quả đo.

Ví dụ, đây là mạch teleportation: Alice gửi trạng thái của một qubit cho Bob, bằng cách dùng một cặp qubit
vướng víu và **hai bit cổ điển**.

![Mạch teleportation: Alice tạo cặp vướng víu bằng cổng H và CX rồi gửi một qubit cho Bob qua kênh lượng tử; Alice chuẩn bị trạng thái cần gửi, áp CX và H, đo hai qubit; hai bit kết quả đi qua kênh cổ điển để Bob áp cổng X và Z](../chapters/03_quantum_protocols/images/03_02_03_teleportation_circuit.png)

*Hình: Diego Emilio Serrano, [learnquantum.io](https://learnquantum.io), MIT License.*

Không cần hiểu hết ngay. Sau [Phần 03](../chapters/03_quantum_protocols/README.md) bạn sẽ đọc được mạch này.

## Máy tính lượng tử giỏi và không giỏi gì

### Những gì đã biết

> Bảng này hơi nặng. Bỏ qua trong lần đọc đầu cũng không sao; thuật ngữ nào lạ thì tra
> [bảng thuật ngữ](glossary.md).

| Bài toán | Tăng tốc | Ghi chú trung thực |
|---|---|---|
| **Phân tích số nguyên ra thừa số** (thuật toán Shor) | Từ *siêu đa thức* (tăng nhanh hơn mọi hàm đa thức của số chữ số) xuống đa thức | Chưa ai biết thuật toán cổ điển đa thức, nhưng cũng chưa chứng minh là không tồn tại. Cần máy lớn có sửa lỗi, chưa tồn tại (đến tháng 10/2026). **Lưu ý:** chưa ai chứng minh bài toán này là *NP-đầy-đủ* (NP-complete, nhóm bài "khó nhất" trong lớp NP, như bài toán thoả mãn biểu thức logic SAT) và nhiều khả năng nó không phải; giới nghiên cứu cũng không tin máy lượng tử giải được các bài NP-đầy-đủ trong thời gian đa thức |
| **Tìm kiếm không cấu trúc** ([Grover](../chapters/04_quantum_algorithms/README.md#04_04--grovers-algorithm-thuật-toán-grover)) | Căn bậc hai: $N \to \sqrt N$ | Đã chứng minh là tối ưu **trong mô hình hộp đen** (chỉ được hỏi oracle); với bài toán có cấu trúc thì điều đó không loại trừ cách nhanh hơn. Với $N = 2^{20} \approx 10^6$ mục và 1 phần tử cần tìm: cổ điển cần trung bình khoảng $N/2 \approx 524$ nghìn lần truy vấn, Grover cần khoảng 800 vòng, mỗi vòng một lần gọi oracle. Tăng tốc bậc hai là khiêm tốn: chi phí oracle và sửa lỗi có thể xoá lợi thế ở quy mô thực tế |
| **Mô phỏng hệ lượng tử** (hoá học, vật liệu) | Có triển vọng lớn | Ý tưởng gốc của nhà vật lý Richard Feynman. Vẫn là hướng nghiên cứu, đang được thử nghiệm trên máy thật |
| Machine learning, tối ưu hoá | **Chưa rõ** | Có nhiều tuyên bố, ít bằng chứng chắc chắn. Hãy dè dặt với quảng cáo |

Bốn thuật toán trong [Phần 04](../chapters/04_quantum_algorithms/README.md) (Deutsch–Jozsa, Bernstein–Vazirani,
Simon, Grover) là **ví dụ để học**. Ba thuật toán đầu giải những bài toán nhân tạo, không có ứng dụng thực tế:

- *Deutsch–Jozsa* chỉ nhanh hơn thuật toán cổ điển **chắc chắn đúng**; một thuật toán cổ điển ngẫu nhiên với sai số
  nhỏ cũng chỉ cần vài truy vấn.
- *Bernstein–Vazirani* chỉ cho khoảng cách nhỏ ($n$ truy vấn xuống 1).
- *Simon* là ví dụ đầu tiên của lợi thế **hàm mũ** ngay cả khi so với thuật toán cổ điển có ngẫu nhiên, nhưng vẫn
  trong mô hình oracle.

Chúng dạy các kỹ thuật (oracle, phase kickback, giao thoa) mà những thuật toán như Shor dùng lại.

### Những gì máy tính lượng tử không làm

- **Không** thay thế laptop hay điện thoại. Với việc hằng ngày (web, văn bản, game), nó chậm hơn và đắt hơn.
- **Không** "thử mọi đáp án cùng lúc rồi chọn đáp án đúng". Phép đo chỉ cho một kết quả, nên phải thiết kế
  giao thoa để đáp án đúng có xác suất cao. Với đa số bài toán, không ai biết cách làm điều đó.
- **Không** gửi thông tin nhanh hơn ánh sáng. Vướng víu tạo tương quan, không phải kênh truyền tin; teleportation
  vẫn cần gửi bit cổ điển bình thường (xem [03_02](../chapters/03_quantum_protocols/README.md#03_02--quantum-teleportation-dịch-chuyển-trạng-thái-lượng-tử)).
- **Không** sao chép được trạng thái lượng tử chưa biết (định lý *no-cloning*,
  [02_04](../chapters/02_quantum_computing/README.md#02_04--multi-qubit-systems-hệ-nhiều-qubit)).

## Vì sao khó chế tạo

Qubit rất dễ bị phá hỏng bởi môi trường (nhiệt, rung, nhiễu điện từ) và bởi sự thiếu chính xác của thiết bị điều khiển.
Các sai lệch này gọi chung là *nhiễu* (noise): gồm *mất kết hợp* (decoherence), lỗi của từng cổng và lỗi khi đọc kết quả.
Các máy hiện nay vẫn thuộc thời kỳ **NISQ** (noisy intermediate-scale quantum, thuật ngữ do nhà vật lý John Preskill
đưa ra cuối năm 2017, phổ biến qua bài báo năm 2018): có nhiều qubit nhưng nhiễu, chưa đủ tốt để chạy các thuật toán lớn như Shor.

Hướng giải quyết là **sửa lỗi lượng tử**: dùng nhiều qubit vật lý để tạo ra một qubit "logic" đáng tin cậy.
Số qubit vật lý cần cho mỗi qubit logic được ước tính từ hàng chục đến hàng nghìn, tuỳ mã sửa lỗi và độ nhiễu.
Các công nghệ đang được theo đuổi gồm mạch siêu dẫn, bẫy ion, nguyên tử trung hoà, photon, và nhiều hướng khác.

> Lĩnh vực này thay đổi nhanh. Mọi nhận định về phần cứng ở trên đúng với hiểu biết đến tháng 10/2026;
> hãy kiểm tra nguồn mới trước khi trích dẫn số liệu cụ thể.

## Vì sao không thể chỉ "mô phỏng bằng máy tính thường"?

Mô tả đầy đủ trạng thái $n$ qubit cần $2^n$ biên độ. Mỗi khi thêm một qubit, bộ nhớ nhân đôi:

| Số qubit | Số biên độ | Bộ nhớ (số phức 16 byte) |
|---|---|---|
| 10 | 1 024 | 16 KiB |
| 30 | khoảng $10^9$ | 16 GiB |
| 50 | khoảng $10^{15}$ | 16 PiB |

Ba mươi qubit đã vừa với một máy tính mạnh (con số 16 GiB là cho riêng vector; thực tế cần nhiều hơn một chút để tính toán), năm mươi thì vượt xa mọi máy đơn lẻ. Đây là lý do mô phỏng
đầy đủ không mở rộng được, và cũng là lý do bạn có thể **học mọi thứ trong repo này trên laptop**:
các ví dụ dùng nhiều nhất 14 qubit (bài Simon), tức chỉ khoảng 256 KiB cho vector trạng thái.

(Có những kỹ thuật mô phỏng thông minh cho các mạch có cấu trúc đặc biệt, nên bảng trên là chi phí
của cách mô phỏng "vét cạn", không phải giới hạn tuyệt đối.)

## Tiếp theo

| Bạn muốn | Đọc |
|---|---|
| Học từng bước, có lộ trình | [Lộ trình học](learning-path.md) |
| Cài môi trường hoặc chạy không cần cài | [Cài đặt](setup.md) |
| Tra một thuật ngữ | [Bảng thuật ngữ](glossary.md) |
| Giải đáp thắc mắc thường gặp (có cả chuyện mật mã) | [FAQ](faq.md) |
| Tài liệu bên ngoài để học tiếp | [Tài nguyên](resources.md) |
