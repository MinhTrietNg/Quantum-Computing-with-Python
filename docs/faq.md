# Câu hỏi thường gặp

**Tiếng Việt** · [English](faq.en.md) · [简体中文](faq.zh-CN.md)

## Về máy tính lượng tử

### Máy tính lượng tử có thay thế máy tính thường không?

Không. Về lý thuyết, nó giỏi một số bài toán đặc thù (xem [bảng trong trang giới thiệu](what-is-quantum-computing.md#những-gì-đã-biết))
và không giúp gì cho phần lớn việc hằng ngày. Nhiều khả năng chúng sẽ tồn tại song song: máy lượng tử như một
bộ tăng tốc cho vài loại phép tính, giống GPU bây giờ.

### Có đúng là nó "thử mọi đáp án cùng lúc" không?

Đây là hiểu lầm phổ biến nhất. Một qubit ở chồng chập đang ở **một trạng thái xác định**, mô tả bằng các biên độ;
nó không phải "vừa 0 vừa 1". Và **phép đo chỉ cho ra một kết quả**. Nếu chỉ "thử hết" rồi đo, bạn nhận được một
đáp án ngẫu nhiên.

Chìa khoá nằm ở **giao thoa** (cùng với vướng víu): thuật toán được thiết kế sao cho các đường dẫn tới đáp án sai triệt tiêu nhau
còn đáp án đúng được khuếch đại. Việc thiết kế được như vậy rất khó, và chỉ làm được cho một số bài toán.
Ví dụ cụ thể ở [trang giới thiệu](what-is-quantum-computing.md) (hai cổng H liên tiếp).

### Vướng víu khác gì hai đồng xu ghép trùng sẵn?

Nếu chỉ nhìn kết quả `00` hoặc `11` thì không khác: hai đồng xu bỏ trong hai phong bì, ghép trùng từ trước, cũng cho
kết quả như vậy. Khác biệt chỉ lộ ra khi **đo theo nhiều hướng khác nhau**. Khi đó các tương quan của qubit vướng víu mạnh
hơn bất kỳ cách "quy định sẵn kết quả từ trước" nào có thể tạo ra. Đây là nội dung của *bất đẳng thức Bell* (ví dụ trò chơi CHSH).
Khoá *Basics of quantum information* của IBM trong [Tài nguyên](resources.md) có phần này.

### Vướng víu có cho phép gửi tin nhanh hơn ánh sáng không?

Không. Kết quả đo ở mỗi đầu là ngẫu nhiên; chỉ khi hai bên **so sánh kết quả qua kênh thông thường** mới thấy tương quan.
Teleportation cũng vậy: Bob chỉ khôi phục được trạng thái sau khi nhận **hai bit cổ điển** từ Alice
([03_02](../chapters/03_quantum_protocols/README.md)).

### Có thể sao chép một qubit không?

Không với trạng thái chưa biết. Đó là định lý *no-cloning* ([02_04](../chapters/02_quantum_computing/README.md)).
Chính tính chất này làm cho tiền lượng tử khó làm giả ([03_01](../chapters/03_quantum_protocols/README.md)).

### Hiện nay máy lượng tử đã làm được gì?

Các máy hiện nay (đến tháng 10/2026) còn nhiễu và chưa sửa lỗi ở quy mô đủ lớn, nên chưa chạy được thuật toán lớn như Shor. Chúng được dùng cho nghiên cứu, thử nghiệm
thuật toán nhỏ và mô phỏng hệ lượng tử. Tiến độ nhanh và nhiều tuyên bố gây tranh cãi; hãy ưu tiên nguồn gốc
(bài báo, tài liệu kỹ thuật của hãng) hơn tin tức, và dè dặt với con số "gấp triệu lần" không nói rõ bài toán nào.

## Về mật mã

### Máy tính lượng tử phá được mã hoá không?

**Một số loại, và chỉ khi có máy đủ lớn.**

- **Mật mã khoá công khai** (dùng để trao đổi khoá và ký số) như RSA và đường cong elliptic (ECC) dựa trên độ khó của phân tích thừa số hoặc
  *logarithm rời rạc* (một bài toán số học khác mà máy tính thường cũng chưa giải nhanh được). Thuật toán **Shor** giải các bài này trong thời gian đa thức, nên một máy lượng tử lớn có sửa lỗi
  sẽ phá được chúng. Máy như vậy **chưa tồn tại** (đến tháng 10/2026).
- **Mã hoá đối xứng** (như AES) bị ảnh hưởng ít hơn nhiều: thuật toán **Grover** chỉ cho tăng tốc bậc hai, nên trước phép dò khoá
  vét cạn, khoá $k$ bit có độ an toàn lý thuyết khoảng $k/2$ bit (AES-128 còn khoảng 64 bit). NIST vẫn chấp nhận AES-128
  (bản dự thảo NIST IR 8547 dùng nó làm mốc cho mức an toàn thấp nhất); một số nơi, như NSA, yêu cầu AES-256 để có dư địa.
  Trong thực tế Grover khó song song hoá nên ảnh hưởng thật còn nhỏ hơn con số lý thuyết.

### Vậy có cần lo ngay không?

Có một lý do để chuẩn bị sớm: kẻ tấn công có thể **lưu dữ liệu mã hoá hôm nay rồi giải mã khi có máy**
("harvest now, decrypt later"). Với dữ liệu cần giữ bí mật hàng chục năm, rủi ro này có thật. (Rủi ro này chủ yếu
với bí mật lâu dài, nhất là trao đổi khoá; chữ ký số chỉ bị đe doạ từ khi máy đủ mạnh xuất hiện, không bị ảnh hưởng ngược về quá khứ. Tuy vậy chữ ký và chứng chỉ tồn tại lâu, như firmware hay chứng chỉ gốc, vẫn cần chuyển sang thuật toán hậu lượng tử trước thời điểm đó.)

Giải pháp là **mật mã hậu lượng tử** (post-quantum cryptography): thuật toán chạy trên máy tính thường nhưng
được cho là chịu được cả máy lượng tử. Tháng 8/2024, NIST công bố ba chuẩn đầu tiên:
FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) và FIPS 205 (SLH-DSA). Đến tháng 10/2026, NIST còn đang hoàn thiện FN-DSA (FIPS 206) và chuẩn HQC.
Bản dự thảo NIST IR 8547 (11/2024, đến tháng 10/2026 vẫn là dự thảo) đề xuất coi RSA/ECC ở mức an toàn 112 bit (như RSA-2048)
là lỗi thời (deprecated) sau 2030, và cấm mọi RSA/ECC sau 2035. Xem
[trang của NIST](https://csrc.nist.gov/projects/post-quantum-cryptography) để biết hiện trạng.

### Còn "mật mã lượng tử" (QKD) thì sao?

QKD (phân phối khoá lượng tử) là hướng khác: dùng vật lý lượng tử để hai bên chia sẻ khoá bí mật,
không phải thuật toán chống máy lượng tử. QKD cần một kênh cổ điển đã được xác thực, thiết bị chuyên dụng và bị giới hạn
khoảng cách; một số cơ quan an ninh quốc gia công khai ưu tiên mật mã hậu lượng tử hơn QKD cho đa số nhu cầu.
Chương về QKD (03_05) của sách gốc chưa có nội dung.

## Về việc học

### Tôi cần biết gì trước khi bắt đầu?

Python cơ bản là chính. Toán cần thiết (vector, ma trận, số phức) được sách dạy dần.
Xem [Lộ trình học](learning-path.md#cần-chuẩn-bị-gì) kèm bài tự kiểm tra 5 phút.

### Tôi chưa biết lập trình thì có học được không?

Hiểu được ý tưởng thì được: trang [Máy tính lượng tử là gì?](what-is-quantum-computing.md), các mục *Ghi nhớ nhanh*
trong README từng phần, và sách *Quantum Computing for the Quantum Curious* ([Tài nguyên](resources.md)) không đòi hỏi code.
Muốn tự tay chạy và làm bài tập thì cần Python cơ bản; vài tuần học Python là đủ để bắt đầu.

### Học máy tính lượng tử để làm gì? Có việc làm không?

Hiện đây chủ yếu là lĩnh vực nghiên cứu và thử nghiệm; số vị trí việc làm còn ít so với lập trình thông thường và
thường đòi hỏi nền tảng vật lý, toán hoặc khoa học máy tính vững. Hãy học vì quan tâm đến chủ đề, vì nền tảng
(đại số tuyến tính, xác suất, tư duy thuật toán) có ích ở nhiều chỗ khác, hơn là vì kỳ vọng việc làm ngay.

### Tôi có phải đọc nhiều tiếng Anh không?

Hướng dẫn trong repo này viết bằng tiếng Việt (có bản dịch English và 简体中文), nhưng notebook gốc, tài liệu của Qiskit và phần lớn tài nguyên học tiếp bằng
tiếng Anh. Không cần giỏi: các notebook dùng câu đơn giản, và [bảng thuật ngữ](glossary.md) có cả tên tiếng Anh
để bạn dần quen.

### Tôi có cần học vật lý lượng tử trước không?

Không. Phần lượng tử của sách (Phần 02) bắt đầu từ thí nghiệm Stern–Gerlach và xây khái niệm qubit từ đó.
Bạn không cần giải phương trình Schrödinger hay biết vật lý nguyên tử.

### Tôi có cần máy lượng tử thật hoặc tài khoản IBM không?

Không. Mọi notebook chạy trên simulator trong máy bạn. Tài khoản IBM Quantum chỉ cần nếu bạn muốn chạy trên
phần cứng thật (hướng dẫn ở [00_02](../chapters/00_getting_started/README.md)); điều kiện truy cập thay đổi theo
chính sách của IBM nên hãy xem trang chính thức.

### Máy tôi cần cấu hình thế nào?

Một laptop bình thường là đủ: các ví dụ dùng nhiều nhất 14 qubit, nên vector trạng thái chỉ chiếm khoảng 256 KiB
(xem [bảng bộ nhớ](what-is-quantum-computing.md#vì-sao-không-thể-chỉ-mô-phỏng-bằng-máy-tính-thường)). Trên máy phát triển của repo, 19 notebook chạy hết trong khoảng 3–5,5 phút (đo các ngày 2026-10-01 và 2026-10-05, sau khi đã cài thư viện); máy bạn có thể chậm hơn.

### Nên dùng Qiskit, Cirq hay PennyLane?

Khác biệt chủ yếu về hệ sinh thái. **Qiskit** (IBM) là một trong những thư viện phổ biến nhất và là thư viện sách này dùng.
**Cirq** (Google) cũng là thư viện Python cho mạch lượng tử. **PennyLane** (Xanadu) mạnh về quantum machine learning và thuật toán biến phân.
Khái niệm giống nhau, nên học một thư viện xong sẽ chuyển được sang thư viện khác (lưu ý quy ước thứ tự qubit có thể khác nhau giữa các thư viện).

### Vì sao qubit trong Qiskit "đọc từ phải sang trái"?

Đó là quy ước *little-endian*: qubit 0 là bit ít quan trọng nhất, nằm bên phải chuỗi kết quả (`'011'` nghĩa là
$q_2 = 0, q_1 = 1, q_0 = 1$). Xem [Cài đặt](setup.md#vài-quy-ước-dễ-gây-nhầm-khi-đọc-code-qiskit).

### Kết quả tôi chạy khác output trong notebook?

Bình thường với kết quả lấy mẫu (`shots`): mỗi lần chạy cho số hơi khác. Kết quả của `Statevector` thì không đổi.
Nếu kết luận khác hẳn (hoặc có lỗi), xem [gỡ lỗi](setup.md#gỡ-lỗi-thường-gặp).

## Về repo này

### Repo này khác gì sách gốc trên learnquantum.io?

Notebook và hình là **bản sao nguyên văn** của sách gốc (giấy phép MIT). Phần do repo này thêm vào là
hướng dẫn tiếng Việt cho từng phần (kèm bản dịch English và 简体中文), [danh sách lỗi](../ERRATA.md), tài liệu nhập môn trong thư mục `docs/`,
và kiểm thử tự động. Mọi công lao về nội dung sách thuộc về tác giả Diego Emilio Serrano.

### Vì sao Phần 05 và 06 (QFT, Shor, ...) không có?

Trên web của sách, các chương này mới chỉ có tiêu đề và chưa có nội dung, nên chưa được sao chép.
Một workflow tự động kiểm tra bản gốc hằng tuần và báo cho người bảo trì, người này sẽ bổ sung khi tác giả viết xong.

### Tôi tìm thấy lỗi hoặc muốn góp ý?

Xem [CONTRIBUTING](../CONTRIBUTING.md). Mọi góp ý đều được hoan nghênh, từ sửa chính tả đến viết hướng dẫn mới.

### Tôi hỏi về kiến thức trong sách ở đâu?

- **Tại repo này (tiếng Việt, English hoặc 中文):** mở một issue theo mẫu *Câu hỏi khi học* trong [Issues của repo này](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose).
  Hãy ghi rõ bạn đang học bài nào và đã thử gì.
- **Bằng tiếng Anh:** [Discussions của repo gốc](https://github.com/learn-quantum/lqc-textbook/discussions), nơi tác giả
  và cộng đồng trả lời.
