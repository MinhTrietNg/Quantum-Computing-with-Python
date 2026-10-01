# Cài đặt và chạy notebook

Có ba cách dùng repo này, từ dễ nhất đến đầy đủ nhất. Bạn không cần tài khoản IBM Quantum hay máy lượng tử thật;
mọi notebook chạy trên simulator ngay trên máy bạn.

| Cách | Cần | Phù hợp khi |
|---|---|---|
| **1. Chỉ đọc trên GitHub** | Trình duyệt | Muốn xem thử, hoặc chỉ cần hiểu ý tưởng. Output đã có sẵn trong notebook |
| **2. Google Colab** | Tài khoản Google | Muốn chạy code mà không cài gì |
| **3. Chạy trên máy** | Python 3.11 trở lên | Học nghiêm túc; có đủ hình vẽ như sách |

## 1. Chỉ đọc trên GitHub

Mở [Mục lục](../README.md#mục-lục), chọn một bài. GitHub hiển thị notebook cùng output và hình mà tác giả
đã chạy sẵn. Đây là cách nhanh nhất để xem sách trông thế nào.

## 2. Google Colab (không cần cài)

Colab chạy notebook trên máy chủ của Google, trong trình duyệt.

### Thử nhanh đoạn code mẫu (notebook trống)

Mở [colab.research.google.com](https://colab.research.google.com) và chọn *New notebook*. Trong ô đầu tiên dán
`%pip install -q qiskit qiskit-aer` rồi bấm nút ▶ để chạy. Sau đó dán đoạn code mẫu (ở [README](../README.md#thử-ngay)
hoặc [trang giới thiệu](what-is-quantum-computing.md)) vào một ô mới và chạy.

### Chạy notebook của sách

Mỗi lần mở một notebook của sách, bạn làm ba bước:

1. **Mở notebook trên Colab.** Mở notebook trên GitHub, rồi trong thanh địa chỉ đổi `github.com` thành
   `colab.research.google.com/github`. Ví dụ:

   ```text
   https://colab.research.google.com/github/MinhTrietNg/Quantum-Computing-with-Python/blob/main/chapters/01_classical_computing/01_01_bits_and_circuits.ipynb
   ```

   (Nếu bạn dùng bản fork, thay `MinhTrietNg` bằng tên tài khoản của bạn.) Thử ngay với
   [00_01 trên Colab](https://colab.research.google.com/github/MinhTrietNg/Quantum-Computing-with-Python/blob/main/chapters/00_getting_started/00_01_setting_env.ipynb).

2. **Cài thư viện.** Bấm **+ Code** để thêm một ô code mới (nó nằm ngay dưới ô đang chọn; vị trí không quan trọng, miễn là bạn chạy nó
   **trước** các ô khác), dán đoạn dưới đây và bấm nút ▶ (hoặc `Shift+Enter`) để chạy:

   ```python
   %pip install -q "qiskit[visualization]>=2.5,<3" qiskit-aer qiskit-ibm-runtime pylatexenc
   !mkdir -p ~/.qiskit
   !curl -sL https://raw.githubusercontent.com/MinhTrietNg/Quantum-Computing-with-Python/main/qiskit_settings.conf -o ~/.qiskit/settings.conf
   ```

   Hai dòng cuối làm hình vẽ giống sách (xem [mục cấu hình](#cấu-hình-qiskit-để-hình-giống-sách)).
   Nếu Colab báo cần khởi động lại, chọn *Runtime → Restart session* rồi chạy tiếp từ ô này.

3. **Chạy các ô còn lại** từ trên xuống.

**Hạn chế của Colab:**
- Hình minh hoạ trong phần chữ của notebook (đường dẫn dạng `images/...`) thường **không hiện** trên Colab.
  Hãy mở song song trang notebook trên GitHub để xem hình.
- CI của repo chỉ kiểm thử trên Ubuntu với Python 3.11 và 3.12. Colab **chưa được kiểm thử tự động**,
  nên nếu gặp lỗi, hãy [báo cho chúng tôi](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose).

## 3. Chạy trên máy

### Bước 1: Python

> **Terminal** là cửa sổ để gõ lệnh. Windows: bấm Start, gõ `PowerShell`, Enter. macOS: mở ứng dụng *Terminal*.
> Lệnh `cd tên-thư-mục` chuyển vào một thư mục.

Cần **Python 3.11 trở lên**. Repo được kiểm thử với 3.11 và 3.12. Nếu chưa có Python, hãy cài bản **3.12** (trên
python.org, mở mục *Downloads*, chọn *Python 3.12.x*, thay vì nút "bản mới nhất"). Nếu đã có bản mới hơn, cứ thử;
gặp lỗi khi cài thư viện thì chuyển sang 3.12. Cài xong, **đóng và mở lại terminal**.

Kiểm tra bạn đã có Python chưa:

```bash
python --version        # macOS/Linux có thể là: python3 --version
```

Trên Windows, nếu lệnh trên không chạy, thử `py --version`. Nếu gõ `python` mà Windows mở Microsoft Store, hãy cài Python
từ [python.org](https://www.python.org/downloads/) và **tích ô "Add python.exe to PATH"** ở bước đầu của trình cài đặt.

### Bước 2: Lấy mã nguồn

Nếu có `git`:

```bash
git clone https://github.com/MinhTrietNg/Quantum-Computing-with-Python.git
cd Quantum-Computing-with-Python
```

Chưa có git? Trên trang repo, bấm nút xanh **Code → Download ZIP**, giải nén, rồi mở terminal trong thư mục vừa giải nén.

### Bước 3: Môi trường ảo và thư viện

Môi trường ảo (`.venv`) giữ các thư viện của repo này tách khỏi phần còn lại của máy.

```bash
python -m venv .venv                  # Windows với nhiều phiên bản Python: py -3.12 -m venv .venv
```

Kích hoạt môi trường ảo (làm mỗi lần mở terminal mới):

| Hệ điều hành | Lệnh |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| macOS, Linux | `source .venv/bin/activate` |

Khi thành công, đầu dòng lệnh hiện `(.venv)`. (PowerShell báo lỗi *running scripts is disabled*? Xem
[Gỡ lỗi](#gỡ-lỗi-thường-gặp).) Rồi cài thư viện:

```bash
pip install -r requirements.txt
```

### Bước 4: Mở notebook

**Cách A: Jupyter.** Chạy:

```bash
jupyter notebook chapters/
```

Trình duyệt mở ra với danh sách thư mục. Bấm vào `00_getting_started`, rồi `00_01_setting_env.ipynb`.
Một notebook gồm nhiều **ô** (cell): ô chữ và ô code. Bấm vào một ô code rồi nhấn **`Shift+Enter`** để chạy nó và
chuyển sang ô kế tiếp.

**Cách B: VS Code.** Cài các extension *Python* và *Jupyter*, mở thư mục repo, mở file `.ipynb`, bấm
*Select Kernel* rồi chọn `.venv`.

Mỗi notebook độc lập với các notebook khác, nhưng trong một notebook, **ô sau dùng biến của ô trước**,
nên hãy chạy từ trên xuống.

### Kiểm tra môi trường

Trong Jupyter, chọn *File → New → Notebook* (chọn kernel Python 3), dán đoạn sau vào một ô và nhấn `Shift+Enter`.
(Hoặc lưu thành file `kiem_tra.py` rồi chạy `python kiem_tra.py`.)

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(AerSimulator().run(qc, shots=1000).result().get_counts())
```

Thấy kết quả dạng `{'11': 492, '00': 508}` (con số và thứ tự mỗi lần một khác, nhưng chỉ có `00` và `11`, mỗi cái
khoảng một nửa) là môi trường đã ổn.

### Cấu hình Qiskit để hình giống sách

Copy [qiskit_settings.conf](../qiskit_settings.conf) thành `settings.conf` trong thư mục `.qiskit` của bạn
(tạo thư mục nếu chưa có). **Nếu bạn đã có file `settings.conf`, hãy sao lưu hoặc gộp tay** để khỏi ghi đè cấu hình cũ:

| Hệ điều hành | Đích |
|---|---|
| Windows | `C:\Users\<tên>\.qiskit\settings.conf` |
| macOS, Linux | `~/.qiskit/settings.conf` |

Hoặc dùng lệnh, chạy ở thư mục gốc repo (cả hai lệnh đều không ghi đè file đã có):

```bash
# macOS, Linux
mkdir -p ~/.qiskit && cp -n qiskit_settings.conf ~/.qiskit/settings.conf
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force $HOME\.qiskit | Out-Null
if (-not (Test-Path $HOME\.qiskit\settings.conf)) { Copy-Item qiskit_settings.conf $HOME\.qiskit\settings.conf }
```

Cách khác không đụng tới `~/.qiskit`: đặt biến môi trường `QISKIT_SETTINGS` trỏ tới file `qiskit_settings.conf` của repo
(CI của repo làm đúng như vậy).

Tệp này đặt kiểu vẽ mạch (màu IBM, ẩn dây không dùng, qubit chỉ số lớn nằm trên). Không có nó, mạch vẽ ra
sẽ hơi khác hình trong sách (ví dụ thứ tự qubit bị lộn ngược), **nhưng kết quả tính toán vẫn như nhau**.
Ý nghĩa từng tuỳ chọn có ở [00_02](../chapters/00_getting_started/README.md#00_02--configuring-qiskit-cấu-hình-qiskit).

## Vài quy ước dễ gây nhầm khi đọc code Qiskit

Chưa cần nhớ hết ngay; khi gặp kết quả đo nhiều qubit, hãy quay lại đây.

- **Thứ tự qubit (little-endian):** trong chuỗi kết quả như `'011'`, ký tự **bên phải nhất** là qubit 0.
  Nhiều tài liệu khác viết ngược lại.
- `circuit_reverse_bits = True` trong `settings.conf` chỉ đổi cách **vẽ** mạch, không đổi kết quả.
- `Statevector(qc)` tính trạng thái chính xác, không có nhiễu thống kê (dùng cho mạch chưa có phép đo).
  `AerSimulator().run(qc, shots=N)` mô phỏng đo $N$ lần, nên **mỗi lần chạy cho số hơi khác nhau**
  và khác output lưu trong notebook. Kết luận thì không đổi.
- Mạch có phép đo cần bit cổ điển để lưu kết quả: `QuantumCircuit(n_qubits, n_bits)`.
  (`measure_all()` tự thêm chúng.)

## Gỡ lỗi thường gặp

| Triệu chứng | Nguyên nhân thường gặp | Cách xử lý |
|---|---|---|
| `ModuleNotFoundError: No module named 'qiskit'` (hoặc `qiskit_aer`) | Jupyter đang dùng kernel khác với môi trường đã cài | Kích hoạt `.venv` rồi chạy lại `jupyter`; trong VS Code, chọn lại kernel `.venv` |
| `ImportError` nhắc tới `pylatexenc` | Thiếu thư viện vẽ mạch | `pip install pylatexenc` (đã có trong `requirements.txt`) |
| `ImportError: cannot import name 'execute'` hoặc `'Aer'` | Code kiểu Qiskit cũ (trước 1.0) | Sách dùng Qiskit 2.x với `AerSimulator`; cài đúng phiên bản trong `requirements.txt` |
| PowerShell báo *running scripts is disabled* khi kích hoạt `.venv` | Chính sách thực thi của Windows | Dùng `activate.bat` trong cmd, hoặc chạy `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `UnicodeEncodeError` khi `print(qc.draw("text"))` trên Windows | Khi output bị chuyển hướng (`> file`, pipe, một số IDE), Python dùng bảng mã ANSI của Windows (như cp1252), không mã hoá được ký tự khung ┌─┐ | Đặt biến môi trường `PYTHONUTF8=1` trước khi chạy script (trong notebook không bị lỗi này) |
| Mạch vẽ ra khác hình trong sách | Chưa có `settings.conf` | Xem mục [Cấu hình](#cấu-hình-qiskit-để-hình-giống-sách); kết quả vẫn đúng |
| Số liệu đo khác output đã lưu | Lấy mẫu ngẫu nhiên | Bình thường; so sánh *kết luận* chứ không so từng con số |
| Lỗi khi `pip install` trên Python mới | Chưa có bản dựng sẵn cho phiên bản Python quá mới | Dùng Python 3.12 |
| Một notebook báo lỗi sau khi nâng cấp Qiskit | API đổi giữa các phiên bản | Chạy `pip list`, đối chiếu với phiên bản đã kiểm thử bên dưới, rồi [báo lỗi](https://github.com/MinhTrietNg/Quantum-Computing-with-Python/issues/new/choose) kèm traceback |

## Phiên bản đã kiểm thử

Cả 19 notebook chạy được (kiểm tra ngày 2026-10-01) với: Python 3.11, Qiskit 2.5.2, Qiskit Aer 0.17.2,
Qiskit IBM Runtime 0.50.0. CI chạy lại hằng tuần với phiên bản mới nhất để báo sớm khi một bản Qiskit mới làm hỏng
notebook.
