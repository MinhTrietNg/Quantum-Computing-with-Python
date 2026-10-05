# Bảng thuật ngữ

Thuật ngữ tiếng Việt (tiếng Anh), định nghĩa ngắn, và nơi học kỹ. Ký hiệu $|\cdot\rangle$ đọc là "ket".
Dùng `Ctrl+F` để tìm nhanh. Mục có dấu *(đọc sau)* là khái niệm nâng cao, chưa cần hiểu khi mới bắt đầu.
Gặp từ chưa có ở đây? Hãy [mở issue](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose) để chúng tôi bổ sung.

Viết tắt nơi học: **P01** = [Phần 01](../chapters/01_classical_computing/README.md),
**P02** = [Phần 02](../chapters/02_quantum_computing/README.md),
**P03** = [Phần 03](../chapters/03_quantum_protocols/README.md),
**P04** = [Phần 04](../chapters/04_quantum_algorithms/README.md).

## Toán cần dùng

| Thuật ngữ | Ý nghĩa | Học ở |
|---|---|---|
| Vector | Danh sách số có thứ tự, ví dụ $(1, 0)$. Bit và qubit đều được viết thành vector | P01 |
| Ma trận | Bảng số; nhân ma trận với vector biến một vector thành vector khác. Mỗi cổng là một ma trận | P01 |
| Số phức | Số dạng $a + bi$ với $i^2 = -1$; $a$ là phần thực, $b$ là phần ảo. Biên độ qubit có thể là số phức | P02 |
| Môđun (độ lớn) của số phức | $\vert a + bi \vert = \sqrt{a^2 + b^2}$; ví dụ $\vert 3 + 4i \vert = 5$ | P02 |
| XOR ($\oplus$) | Cộng hai bit rồi bỏ nhớ: $0 \oplus 0 = 0$, $0 \oplus 1 = 1$, $1 \oplus 1 = 0$ | P01 |
| Hàm hằng / hàm cân bằng | Hàm $f$ trên các chuỗi bit: *hằng* nếu cho cùng một giá trị với mọi đầu vào; *cân bằng* nếu cho 0 với đúng một nửa số đầu vào và 1 với nửa còn lại | P04 |
| Giá trị kỳ vọng | Giá trị trung bình khi lặp lại phép đo rất nhiều lần | P02 |

## Nền tảng

| Thuật ngữ | Ý nghĩa | Học ở |
|---|---|---|
| Bit | Đơn vị thông tin cổ điển, nhận giá trị 0 hoặc 1 | P01 |
| Qubit | Đơn vị thông tin lượng tử; trạng thái là $\alpha\vert 0\rangle + \beta\vert 1\rangle$ | P02 |
| Ket $\vert \psi\rangle$ | Ký hiệu Dirac cho vector trạng thái (cột). $\vert 0\rangle$ là cột $(1, 0)$ và $\vert 1\rangle$ là cột $(0, 1)$ (viết gọn $(1, 0)^T$: chữ $T$ nghĩa là xếp thành cột) | P01, P02 |
| Biên độ (amplitude) | Hệ số phức đứng trước mỗi trạng thái cơ sở. Bình phương môđun của nó là xác suất đo được trạng thái đó | P02 |
| Chồng chập (superposition) | Trạng thái là tổ hợp của nhiều trạng thái cơ sở, ví dụ $\tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$ | P02 |
| Trạng thái $\vert +\rangle$, $\vert -\rangle$ | Hai trạng thái chồng chập đều: $\vert +\rangle = \tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$ và $\vert -\rangle = \tfrac{1}{\sqrt2}(\vert 0\rangle - \vert 1\rangle)$; chỉ khác nhau ở dấu tương đối | P02 |
| Đo (measurement) | Lấy ra một bit cổ điển từ qubit, theo xác suất bằng bình phương môđun của biên độ; qubit bị đổi thành trạng thái vừa đo | P02 |
| Cơ sở (basis) | Tập trạng thái dùng làm "hệ trục" để đo hoặc viết trạng thái, ví dụ cơ sở $\{\vert 0\rangle,\vert 1\rangle\}$ hay $\{\vert +\rangle,\vert -\rangle\}$ | P02 |
| Pha (phase) | Góc của biên độ phức. Pha toàn cục không đo được; pha *tương đối* giữa các biên độ thì quyết định giao thoa | P02 |
| Giao thoa (interference) | Các biên độ cộng hoặc triệt tiêu nhau. Cùng với vướng víu, là chìa khoá sức mạnh của thuật toán lượng tử | P02, P04 |
| Bloch sphere | Hình cầu biểu diễn mọi trạng thái thuần của một qubit; $\vert 0\rangle$ ở cực bắc, $\vert 1\rangle$ ở cực nam | P02 |
| Tích tensor / Kronecker | Cách ghép trạng thái và cổng của nhiều hệ: $\vert 0\rangle \otimes \vert 1\rangle = \vert 01\rangle$ | P01, P02 |
| Statevector | Vector chứa toàn bộ biên độ của hệ $n$ qubit ($2^n$ số phức) | P02 |
| Observable *(đọc sau)* | Đại lượng đo được, biểu diễn bằng ma trận Hermitian; các giá trị riêng của nó là những kết quả đo có thể có | P02 |

## Cổng và mạch

| Thuật ngữ | Ý nghĩa | Học ở |
|---|---|---|
| Cổng (gate) | Phép biến đổi áp lên qubit; cổng lượng tử là ma trận *unitary* | P02 |
| Unitary *(đọc sau)* | Ma trận $U$ thoả $U^\dagger U = I$ ($U^\dagger$ là ma trận chuyển vị rồi lấy liên hợp phức); bảo toàn tổng xác suất và luôn khả nghịch | P02 |
| Khả nghịch (reversible) | Có thể suy ngược đầu vào từ đầu ra. Mọi cổng lượng tử đều khả nghịch | P01 |
| Cổng X | "NOT" lượng tử: đổi $\vert 0\rangle \leftrightarrow \vert 1\rangle$ | P01, P02 |
| Cổng Hadamard (H) | Biến $\vert 0\rangle$ thành $\tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$; cổng tạo chồng chập quen thuộc nhất | P02 |
| Cổng Pauli (X, Y, Z) | Ba cổng cơ bản một qubit, tương đương phép xoay nửa vòng ($\pi$) quanh ba trục $x, y, z$ của Bloch sphere (sai khác một pha toàn cục không đo được) | P02 |
| Cổng pha (P, S, T) | Chỉ đổi pha của $\vert 1\rangle$; S là $\tfrac{\pi}{2}$, T là $\tfrac{\pi}{4}$ | P02 |
| CX (CNOT) | Cổng điều khiển hai qubit: đảo qubit đích nếu qubit điều khiển là 1. Cổng chính để tạo vướng víu | P01, P02 |
| CCX (Toffoli) | Đảo qubit đích nếu **cả hai** qubit điều khiển là 1 | P01 |
| SWAP | Hoán đổi trạng thái của hai qubit. Biến trạng thái tích thành trạng thái tích nên tự nó không tạo vướng víu | P02 |
| Barrier (vạch ngăn) | Dấu trên sơ đồ mạch (vẽ là `░`) để tách các nhóm cổng cho dễ đọc, không đổi trạng thái; `measure_all()` tự chèn một vạch trước phép đo | P02, [Giới thiệu](what-is-quantum-computing.md) |
| Mạch lượng tử (quantum circuit) | Chuỗi cổng và phép đo áp lên các qubit, vẽ từ trái sang phải | P02 |
| Cổng Clifford *(đọc sau)* | Nhóm cổng sinh bởi H, S, CX. Mạch chỉ gồm các cổng này mô phỏng hiệu quả được trên máy tính thường (định lý Gottesman–Knill) | P02 |
| Bộ cổng phổ quát (universal gate set) | Tập cổng đủ để xấp xỉ mọi phép biến đổi lượng tử, ví dụ Clifford + T | P02 |

## Hiện tượng lượng tử

| Thuật ngữ | Ý nghĩa | Học ở |
|---|---|---|
| Vướng víu (entanglement) | Trạng thái nhiều qubit không thể viết thành tích trạng thái từng qubit; với trạng thái thuần, luôn cho tương quan vi phạm một bất đẳng thức Bell nào đó (mạnh hơn mọi mô hình cổ điển) | P02 |
| Trạng thái Bell | Bốn trạng thái vướng víu hai qubit, ví dụ $\tfrac{1}{\sqrt2}(\vert 00\rangle + \vert 11\rangle)$ | P02 |
| GHZ, W | Hai họ trạng thái vướng víu ba qubit trở lên, khác nhau về cách vướng | P02 |
| Bất đẳng thức Bell / CHSH | Giới hạn mà tương quan của mọi mô hình cổ điển (kết quả "quy định sẵn từ trước") phải tuân theo. Qubit vướng víu vi phạm nó, nên vướng víu không giống hai đồng xu ghép sẵn. *Chưa có trong sách này* | — |
| Nguyên lý bất định (uncertainty) | Hai đại lượng như X và Z (*không giao hoán*: đổi thứ tự đo thì kết quả khác) không thể cùng có giá trị xác định | P03 |
| No-cloning | Không thể sao chép một trạng thái lượng tử chưa biết | P02 |
| Decoherence (mất kết hợp) | Một dạng nhiễu: qubit mất tính chất lượng tử do tương tác với môi trường | [Giới thiệu](what-is-quantum-computing.md) |
| Nhiễu (noise) | Mọi sai lệch ngẫu nhiên do phần cứng không hoàn hảo: mất kết hợp, lỗi cổng, lỗi đọc kết quả | P01 (bit xác suất), [Giới thiệu](what-is-quantum-computing.md) |

## Dụng cụ

| Thuật ngữ | Ý nghĩa |
|---|---|
| Notebook (`.ipynb`) | Tài liệu gồm các ô chữ và ô code chạy được, mở bằng Jupyter, VS Code hoặc Colab |
| Ô (cell) | Một khối trong notebook; chạy ô code bằng `Shift+Enter` |
| Kernel | Chương trình Python đứng sau notebook để chạy các ô; cần chọn đúng kernel (của `.venv`) |
| Môi trường ảo (`venv`) | Thư mục `.venv` chứa Python và thư viện riêng cho repo, tách khỏi phần còn lại của máy |
| Terminal | Cửa sổ để gõ lệnh (PowerShell trên Windows, Terminal trên macOS) |

## Các cách gọi khác

Cùng một khái niệm có thể được dịch khác nhau giữa các tài liệu. Dùng bảng này khi tìm kiếm.

| Trong repo này | Còn gặp |
|---|---|
| Vướng víu (entanglement) | rối lượng tử, vướng mắc lượng tử |
| Chồng chập (superposition) | chồng chất, chồng chập lượng tử |
| Qubit | bit lượng tử |
| Mặt cầu Bloch (Bloch sphere; repo thường giữ nguyên tên tiếng Anh) | quả cầu Bloch |
| Môđun | mô-đun |
| Tích tensor | tích Kronecker (tên sách gốc dùng, nên Phần 01 và 02 cũng dùng; nhất là khi nói về ma trận) |
| Biên độ | biên độ xác suất |

## Giao thức và thuật toán

| Thuật ngữ | Ý nghĩa | Học ở |
|---|---|---|
| Teleportation (dịch chuyển trạng thái lượng tử) | Gửi trạng thái chưa biết của một qubit bằng một cặp vướng víu cộng **hai bit cổ điển**. Không gửi nhanh hơn ánh sáng | P03 |
| Superdense coding (mã hóa siêu đặc) | Gửi **hai bit cổ điển** bằng cách gửi **một qubit**, nhờ cặp vướng víu dùng chung từ trước | P03 |
| Oracle ($U_f$) | "Hộp đen" lượng tử tính hàm $f$: $U_f\vert x\rangle\vert y\rangle = \vert x\rangle\vert y \oplus f(x)\rangle$ | P02, P04 |
| Phase kickback | Với qubit đích ở $\vert -\rangle$, oracle biến giá trị $f(x)$ thành dấu $(-1)^{f(x)}$ trên qubit điều khiển | P02 |
| Độ phức tạp truy vấn (query complexity) | Số lần gọi oracle mà thuật toán cần; thước đo so sánh ở Phần 04 | P04 |
| Deutsch–Jozsa, Bernstein–Vazirani, Simon | Ba thuật toán truy vấn kinh điển trên bài toán nhân tạo. Lợi thế của hai thuật toán đầu nhỏ hoặc chỉ so với thuật toán cổ điển tất định; Simon là lợi thế hàm mũ (trong mô hình oracle) | P04 |
| Grover | Tìm kiếm không cấu trúc với $\sim\sqrt N$ lần truy vấn thay vì $\sim N$ | P04 |
| Shor | Phân tích số nguyên ra thừa số trong thời gian đa thức. *Chưa có trong sách này* | — |
| QFT, QPE | Biến đổi Fourier lượng tử và ước lượng pha, hai khối dựng của Shor. *Chưa có trong sách này* | — |

## Độ phức tạp và mật mã

Dùng trong [Giới thiệu](what-is-quantum-computing.md) và [FAQ](faq.md); sách gốc chưa dạy các khái niệm này.

| Thuật ngữ | Ý nghĩa |
|---|---|
| Thời gian đa thức / siêu đa thức | Số bước tính tăng như một lũy thừa cố định của kích thước đầu vào (đa thức, thường coi là "nhanh"), hay tăng nhanh hơn mọi lũy thừa như vậy (siêu đa thức, ví dụ hàm mũ) |
| NP-đầy-đủ | Lớp bài toán "khó nhất" trong NP: nếu giải được một bài NP-đầy-đủ trong thời gian đa thức thì giải được mọi bài trong NP. Chưa ai biết có thuật toán nhanh hay không (bài toán P với NP) |
| Mật mã khoá công khai (RSA, ECC) | Mật mã dùng để trao đổi khoá và ký số, dựa trên độ khó của phân tích thừa số (RSA) hoặc *logarithm rời rạc* (ECC, Diffie–Hellman) |
| Logarithm rời rạc | Bài toán tìm $x$ từ $g^x \bmod p$ (hoặc phép tương tự trên đường cong elliptic); máy tính thường chưa có cách giải nhanh, thuật toán Shor giải được trong thời gian đa thức |
| Mật mã hậu lượng tử (post-quantum) | Thuật toán mật mã chạy trên máy tính thường nhưng được thiết kế để chống cả máy lượng tử, ví dụ ML-KEM (FIPS 203) và ML-DSA (FIPS 204) |
| QKD (phân phối khoá lượng tử) | Dùng vật lý lượng tử để hai bên chia sẻ khoá bí mật; khác với mật mã hậu lượng tử, nó cần thiết bị chuyên dụng |
| "Harvest now, decrypt later" | Kẻ tấn công thu thập dữ liệu mã hoá hôm nay để giải mã sau này, khi có máy lượng tử đủ mạnh |

## Phần cứng và chạy thực tế

| Thuật ngữ | Ý nghĩa | Học ở |
|---|---|---|
| NISQ | Noisy Intermediate-Scale Quantum: máy hiện nay, nhiều qubit nhưng nhiễu và chưa sửa lỗi ở quy mô đủ lớn | — |
| Qubit vật lý / qubit logic | Qubit vật lý là phần tử phần cứng thật, có nhiễu; qubit logic là một qubit "ảo" ít lỗi hơn, được mã hoá trên nhiều qubit vật lý nhờ sửa lỗi | — |
| Sửa lỗi lượng tử (error correction) | Dùng nhiều qubit vật lý để tạo ra một qubit logic ít lỗi | — |
| QPU | Quantum Processing Unit: chip lượng tử thật | Phần 00 |
| Simulator | Chương trình mô phỏng máy lượng tử trên máy tính thường (như `AerSimulator`) | Phần 00 |
| Shot | Một lần chạy mạch kèm phép đo; chạy $N$ shot cho phân bố kết quả | P02 |
| Counts | Bảng đếm kết quả đo qua các shot, ví dụ `{'00': 504, '11': 496}` | P02 |
| Little-endian | Quy ước của Qiskit: qubit 0 nằm ở **bên phải** trong chuỗi bit kết quả | [Cài đặt](setup.md) |
