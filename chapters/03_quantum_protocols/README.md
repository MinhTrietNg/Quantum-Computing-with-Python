# 03 · Quantum protocols (Giao thức lượng tử)

Phần này dùng các khái niệm đã học (superposition, measurement, entanglement, Bell state) để xây dựng ba giao thức lượng tử kinh điển: tiền lượng tử chống làm giả, teleportation (dịch chuyển trạng thái lượng tử) và superdense coding (mã hóa siêu đặc). Mỗi bài vừa giải thích bằng toán, vừa kiểm chứng bằng mạch Qiskit chạy trên simulator.

> Nguồn: [03_01](https://learnquantum.io/chapters/03_quantum_protocols/03_01_quantum_money.html), [03_02](https://learnquantum.io/chapters/03_quantum_protocols/03_02_teleportation.html), [03_03](https://learnquantum.io/chapters/03_quantum_protocols/03_03_superdense_coding.html) — Diego Emilio Serrano, learnquantum.io, MIT License.

## Mục lục

| Bài | Notebook | Web | Ý chính |
|---|---|---|---|
| 03_01 | [03_01_quantum_money.ipynb](03_01_quantum_money.ipynb) | [link](https://learnquantum.io/chapters/03_quantum_protocols/03_01_quantum_money.html) | Nguyên lý bất định giữa cơ sở bit/sign khiến đồng xu lượng tử không thể sao chép |
| 03_02 | [03_02_teleportation.ipynb](03_02_teleportation.ipynb) | [link](https://learnquantum.io/chapters/03_quantum_protocols/03_02_teleportation.html) | 1 cặp Bell + 2 bit cổ điển = gửi được trọn vẹn 1 qubit |
| 03_03 | [03_03_superdense_coding.ipynb](03_03_superdense_coding.ipynb) | [link](https://learnquantum.io/chapters/03_quantum_protocols/03_03_superdense_coding.html) | 1 cặp Bell + gửi 1 qubit = truyền được 2 bit cổ điển |

Trang web còn liệt kê "Bell Inequalities" (03_04) và "Quantum Key Distribution" (03_05), nhưng ở repo gốc hai chương này chỉ có tiêu đề (chưa có nội dung) nên không được sao chép vào đây.

> Các đoạn code trong README này là **trích** từ notebook (giữ comment gốc tiếng Anh) và dùng biến đã định nghĩa ở các cell trước. Muốn chạy được, hãy chạy cả notebook từ trên xuống.

---

## 03_01 · Uncertainty & Quantum Money (Nguyên lý bất định và tiền lượng tử)

**Mục tiêu** — Hiểu nguyên lý bất định (uncertainty principle) qua hai observable không tương thích $X$, $Z$, rồi dùng nó để xây giao thức quantum money của Wiesner (bài báo "Conjugate Coding", 1983).

### Kiến thức chính

**1. Bất định với spin (mục 1.1).** Với nam châm cổ điển, hai máy Stern-Gerlach (SG) nối tiếp (trục $x$ rồi trục $z$) xác định được 1 trong 4 hướng I–IV. Với electron thì không:

- Máy SG theo $x$ làm lệch hạt một cách xác suất: $P_{+x}(\theta) = \frac{1}{2}(1+\sin\theta)$, $P_{-x}(\theta) = \frac{1}{2}(1-\sin\theta)$ (với hướng I, II: $\approx 0.853$ / $0.146$).
- Sau phép đo theo $x$, spin bị chiếu về $\pm x$, nên máy SG theo $z$ luôn cho lên/xuống với xác suất $1/2$: thông tin về hướng $z$ ban đầu bị "xóa".
- Spin theo $x$ và spin theo $z$ là **incompatible** (không tương thích) hay **conjugate** (liên hợp): đo cái này làm tăng độ bất định của cái kia.

**2. Bất định với qubit (mục 1.2, có thể bỏ qua khi chỉ cần hiểu quantum money).** Với qubit trong mặt phẳng $xz$: $|q\rangle = \cos\frac{\theta}{2}|0\rangle + \sin\frac{\theta}{2}|1\rangle$:

$$\langle Z\rangle = \cos\theta,\quad \langle X\rangle = \sin\theta,\quad \Delta O^2 = \langle O^2\rangle - \langle O\rangle^2 \;\Rightarrow\; \Delta Z = |\sin\theta|,\quad \Delta X = |\cos\theta|$$

Khi $\Delta Z$ nhỏ nhất thì $\Delta X$ lớn nhất và ngược lại. Tổng quát hơn, với pha tương đối $e^{i\varphi}$ và hệ thức bất định $\Delta A\,\Delta B \geq \frac{1}{2}|\langle [A,B]\rangle|$, dùng $[Z,X] = 2iY$:

$$\Delta Z\,\Delta X \geq |\langle iY\rangle| \quad\Longleftrightarrow\quad |\sin\theta|\sqrt{1-\sin^2\theta\cos^2\varphi} \geq |\sin\theta\sin\varphi|$$

Notebook vẽ hai vế theo $\theta$ với vài giá trị $\varphi$, sau đó kiểm chứng bằng Estimator.

**3. Quantum money (mục 2).**

1. **Ngân hàng phát hành đồng xu**: mỗi đồng xu có số serial công khai $S$ và một trạng thái $n$ qubit, mỗi qubit chọn ngẫu nhiên trong $\{|0\rangle, |1\rangle, |+\rangle, |-\rangle\}$ (bắt đầu từ $|0\rangle$, lật bit bằng $X$ và/hoặc đổi cơ sở bằng $H$). Ví dụ $n=6$: $U = II \otimes II \otimes HI \otimes IX \otimes HX \otimes HI$ cho $|0\rangle|0\rangle|+\rangle|1\rangle|-\rangle|+\rangle$.
2. **Ngân hàng lưu cơ sở dữ liệu bí mật**: serial $S$ ↔ chuỗi cổng đã dùng. (Giao thức BBBW đề xuất sinh trạng thái từ $S$ bằng bộ sinh khóa giả ngẫu nhiên; notebook bỏ qua.)
3. **Kiểm tra**: ngân hàng áp mạch nghịch đảo $U^\dagger$ rồi đo; đồng xu thật **luôn** cho chuỗi toàn 0.
4. **Kẻ làm giả** không biết $U$:
   - Đo thẳng ở cơ sở bit: các qubit $|\pm\rangle$ cho kết quả ngẫu nhiên.
   - Đo ở cơ sở sign (áp $H$ lên mọi qubit trước): các qubit $|0\rangle, |1\rangle$ cho kết quả ngẫu nhiên.
   - Chỉ đo được một lần, vì phép đo làm sụp trạng thái. Đoán mò **chính xác** cả $n$ qubit có xác suất $(1/4)^n$; với $n=6$: $\approx 0.000244$.
     (Đây là xác suất đoán mù. Kẻ làm giả khôn hơn, đo ngẫu nhiên từng qubit rồi chuẩn bị lại, thì **một** đồng qua được
     bước kiểm tra với xác suất $(3/4)^n$ (≈ 0.18 khi $n=6$). Để làm ra **hai** đồng cùng qua, cách đo-rồi-chuẩn-bị-lại
     chỉ đạt $(5/8)^n$ và kẻ gian giỏi nhất, dùng phép sao chép tối ưu, đạt $(3/4)^n$. Tất cả đều giảm theo hàm mũ
     khi thêm qubit.)
5. **Vì sao an toàn**: $\{|+\rangle, |-\rangle\}$ là cơ sở liên hợp với $\{|0\rangle, |1\rangle\}$ (bất định), và theo **no-cloning theorem** không thể sao chép một trạng thái lượng tử chưa biết. Cùng lắm kẻ gian tạo được bản sao *vướng víu*, nhưng khi ngân hàng kiểm tra một đồng thì đồng kia sụp và trở nên vô dụng. (Đó là cách nói của sách; thực ra bản sao vướng víu không đảm bảo bị loại: kẻ gian giỏi nhất vẫn làm cả hai đồng cùng qua với xác suất $(3/4)^n$, giảm theo hàm mũ. Giao thức cũng giả định kẻ gian không thể dò kết quả kiểm tra của ngân hàng nhiều lần.)

Cuối bài nhắc tới hướng "tiền lượng tử ảo" và quantum lightning (Zhandry18) như cách kết hợp với blockchain.

> Lưu ý: notebook có hai chỗ viết nhầm, và một chỗ dễ gây hiểu lầm (phần cuối): (1) câu "In the above, we only consider qubits in the $xy$-plane" phải là mặt phẳng $xz$; (2) câu "the probability of the criminal successfully guessing the state grows with the number of qubits" thực ra là *giảm* theo $n$, đúng như công thức $(1/4)^n$. Ngoài ra, $(1/4)^n$ trong notebook là xác suất đoán mù **chính xác** cả trạng thái; nó không phải xác suất kẻ làm giả thành công. Chiến lược đo ngẫu nhiên từng qubit rồi chuẩn bị lại thì một đồng qua được bước kiểm tra với xác suất $(3/4)^n$ (khoảng 0.18 khi $n=6$, nên cần nhiều qubit hơn ví dụ để thực sự an toàn).

### Code chính

```python
# Use the Paramater class to define arbitrary angles of θ and φ
θ = Parameter('θ')
φ = Parameter('φ')

# Circuit to prepare state cos(θ/2)|0⟩+exp(iφ)sin(θ/2)|1⟩
qc = QuantumCircuit(1)
qc.ry(θ,0)
qc.p(φ,0)
```

Mạch có tham số (`qiskit.circuit.Parameter`): `ry(θ)` đặt biên độ, `p(φ)` thêm pha tương đối. Giá trị cụ thể được gán lúc chạy Estimator.

```python
obsv_lst = [[SparsePauliOp(["Z"],[1])],
            [SparsePauliOp(["X"],[1])],
            [SparsePauliOp(["Y"],[1])]]

estimator = Estimator(mode=AerSimulator())
job = estimator.run([(qc,obsv_lst,angles,0.01)])
exp_vals = job.result()[0].data.evs

ΔZ_lst = np.sqrt(1-exp_vals[0]**2)  # ΔZ = √(1-⟨Z⟩²)
ΔX_lst = np.sqrt(1-exp_vals[1]**2)  # ΔX = √(1-⟨X⟩²)
Ys_lst = np.abs(exp_vals[2])        # |⟨Y⟩|
```

`qiskit_ibm_runtime.Estimator` (kiểu V2) chạy trên `AerSimulator`. Một PUB `(circuit, observables, parameter_values, precision)`: 3 observable dạng `SparsePauliOp` × 21 giá trị $\theta$ (với $\varphi = 9\pi/10$ cố định), độ chính xác 0.01; `.data.evs` trả mảng giá trị kỳ vọng. Notebook ghi chú: hệ số của $Y$ lẽ ra là $i$, nhưng vì chỉ lấy trị tuyệt đối nên dùng 1.

```python
def gen_coin(n):
    ...
    qc = QuantumCircuit(n)
    for i in range(n-1,-1,-1):
        state = np.random.choice(['0','1','+','-'])
        if state in ['1', '-']: qc.x(i)
        else: qc.id(i)
        if state in ['+','-']: qc.h(i)
        else: qc.id(i)
```

Hàm của "ngân hàng": chọn ngẫu nhiên trạng thái cho từng qubit rồi áp $X$ và/hoặc $H$ (`qc.id` chỉ để giữ chỗ). Hàm còn trả về chuỗi LaTeX của trạng thái để hiển thị bằng `IPython.display.Math` (phần này được lược trong trích đoạn).

```python
qc_inv = qc.inverse()
sv_check = sv_coin.evolve(qc_inv)
result_probs = sv_check.probabilities_dict(decimals=5)
plot_distribution(result_probs)
```

Kiểm tra đồng xu: `QuantumCircuit.inverse()` tạo $U^\dagger$, `Statevector.evolve` áp mạch lên statevector, `probabilities_dict` và `plot_distribution` hiển thị phân bố. Kẻ làm giả được mô phỏng bằng `sv_coin.probabilities_dict()` (đo cơ sở bit) và `sv_coin.evolve(qc_h)` với `qc_h.h(range(n))` (đo cơ sở sign).

### Kết quả

- Lần chạy đã lưu sinh ra đồng xu $n=6$: $|+\rangle \otimes |1\rangle \otimes |0\rangle \otimes |0\rangle \otimes |1\rangle \otimes |0\rangle$.
- Các đồ thị (bất định, so sánh Estimator và lý thuyết, phân bố xác suất) chỉ được lưu dưới dạng ảnh. Theo notebook, điểm Estimator khớp với đường lý thuyết $\Delta Z\Delta X$ và $|\langle iY\rangle|$. Theo code, đồng xu thật sau $U^\dagger$ cho `000000` với xác suất 1.

### Ghi nhớ nhanh

- $X$ và $Z$ là cặp observable liên hợp: $\Delta Z = |\sin\theta|$, $\Delta X = |\cos\theta|$, không thể cùng nhỏ.
- Đồng xu = serial công khai + $n$ qubit ngẫu nhiên trong $\{|0\rangle,|1\rangle,|+\rangle,|-\rangle\}$; chỉ ngân hàng biết cơ sở.
- Kiểm tra = áp $U^\dagger$ rồi đo, đồng xu thật cho toàn 0.
- Hai lớp bảo vệ: phép đo phá hủy trạng thái (bất định) và no-cloning; xác suất đoán mù chính xác $(1/4)^n$ (kẻ gian giỏi hơn vẫn làm được với xác suất $(3/4)^n$, cũng giảm theo hàm mũ).
- Estimator V2: `estimator.run([(qc, observables, params, precision)])` rồi đọc `result()[0].data.evs`.

---

## 03_02 · Quantum Teleportation (Dịch chuyển trạng thái lượng tử)

**Mục tiêu** — Gửi *toàn bộ* trạng thái của một qubit bất kỳ từ Alice sang Bob chỉ bằng **2 bit cổ điển**, với điều kiện hai người đã chia sẻ trước một cặp qubit vướng víu (Bennett và cộng sự, 1993).

### Kiến thức chính

**So sánh với cách cổ điển.** Muốn Bob tạo $|q\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\varphi}\sin\frac{\theta}{2}|1\rangle$, Alice phải gửi hai góc $(\theta,\varphi)$, ví dụ dạng FP16 (16 bit mỗi góc), và vẫn chỉ được giá trị xấp xỉ. Teleportation chỉ cần 2 bit và cho trạng thái chính xác.

**Các bước (theo sơ đồ mạch của notebook):**

0. Alice khởi tạo 3 qubit $|000\rangle_A$.
1. Alice tạo Bell state $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ trên hai qubit rồi gửi một qubit cho Bob:
   $|\psi\rangle_1 = \frac{1}{\sqrt{2}}|0\rangle_A(|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B)$.
2. Khi cần, Alice chuẩn bị trạng thái muốn gửi $|q\rangle = \alpha|0\rangle + \beta|1\rangle$ (bằng cổng xoay với $\alpha = \cos\frac{\theta}{2}$, $\beta = e^{i\varphi}\sin\frac{\theta}{2}$). Viết lại toàn hệ theo 4 Bell state của hai qubit Alice:

$$|\psi\rangle_2 = \tfrac{1}{2}\Big[|\Phi^+\rangle_A(\alpha|0\rangle+\beta|1\rangle)_B + |\Psi^+\rangle_A(\alpha|1\rangle+\beta|0\rangle)_B + |\Phi^-\rangle_A(\alpha|0\rangle-\beta|1\rangle)_B + |\Psi^-\rangle_A(\alpha|1\rangle-\beta|0\rangle)_B\Big]$$

   Qubit của Bob đã nằm ở một trong 4 biến thể của $|q\rangle$, chỉ khác nhau bởi bit-flip, phase-flip hoặc cả hai. (Notebook bàn ngắn về tính "phi định xứ" gây tranh cãi của cách mô tả này và các cách diễn giải khác, rồi làm việc trong formalism chuẩn.)
3. Alice áp $CX$ rồi $H$ để chuyển từ cơ sở Bell sang cơ sở tính toán:

$$|\psi\rangle_3 = \tfrac{1}{2}\Big[|00\rangle(\alpha|0\rangle+\beta|1\rangle) + |01\rangle(\alpha|1\rangle+\beta|0\rangle) + |10\rangle(\alpha|0\rangle-\beta|1\rangle) + |11\rangle(\alpha|1\rangle-\beta|0\rangle)\Big]$$

4. Alice đo hai qubit: mỗi kết quả `00`, `01`, `10`, `11` có xác suất $1/4$ và để lại cho Bob trạng thái tương ứng ở trên.
5. Alice gửi 2 bit $(j,i)$ cho Bob qua kênh cổ điển. Bob sửa lỗi: $|\psi\rangle_5 = Z^j X^i|\psi\rangle_4 = \alpha|0\rangle + \beta|1\rangle = |q\rangle$ (với $X^0 = Z^0 = I$).

**Vì sao không nhanh hơn ánh sáng:** Bob chưa biết phải sửa gì cho tới khi nhận 2 bit cổ điển. **Vì sao cặp Bell đáng giá:** nó được thiết lập *trước*, nên khi $|q\rangle$ sẵn sàng thì chỉ cần gửi 2 bit.

**Nhiều qubit (mục 2.2):** mỗi qubit cần gửi dùng một cặp Bell riêng và một cặp bit riêng. Ví dụ trong notebook gửi $|q\rangle = \frac{1}{\sqrt{3}}(|001\rangle - |010\rangle + |100\rangle)$ bằng 3 cặp Bell (6 qubit của Alice, 3 của Bob).

### Code chính

```python
qra = QuantumRegister(2,name="Alice q")
qrb = QuantumRegister(1,name="Bob q")
cra = ClassicalRegister(2, name="Alice c")
qc = QuantumCircuit(qrb,qra,cra)

qc.h(qra[0])                  # Bell pair giữa qra[0] và Bob
qc.cx(qra[0],qrb[0])
qc.ry(np.pi/2,qra[1])         # |q⟩ = 1/√2|0⟩ - i/√2|1⟩
qc.p(-np.pi/2,qra[1])
qc.cx(qra[1],qra[0])          # Bell -> computational basis
qc.h(qra[1])
qc.measure(qra,cra)
```

(Đã lược các `barrier()` và rút gọn comment.) Dùng `QuantumRegister`/`ClassicalRegister` có tên để tách qubit của Alice và Bob. Qubit 0 là của Bob, `qra[1]` chứa trạng thái cần gửi.

```python
# Bob applies X, Z gates conditioned on Alice's results
with qc.if_test((cra[0], 1)): qc.x(0)
with qc.if_test((cra[1], 1)): qc.z(0)

qc.save_statevector('ψout')
```

Điều khiển cổ điển động bằng `QuantumCircuit.if_test` (API hiện đại, thay cho `c_if` đã deprecated): áp $X$ nếu bit `cra[0]` bằng 1, áp $Z$ nếu `cra[1]` bằng 1. `save_statevector` là lệnh của Qiskit Aer để lưu statevector cuối mạch.

```python
result = simulator.run(qc, shots=1, memory=True).result()
alices_bits = result.get_memory()[0]
ψout = result.data().get('ψout')

ρout = partial_trace(ψout,[1,2])
bobs_state = DensityMatrix(np.round(ρout, 8)).to_statevector()
```

Chạy 1 shot trên `AerSimulator` với `memory=True` để lấy chuỗi bit Alice đo được. `partial_trace` loại bỏ qubit 1, 2 (của Alice), còn lại density matrix của Bob. Vì trạng thái đó thuần (pure) nên `DensityMatrix(...).to_statevector()` chuyển được về statevector; `np.round` để khử sai số số học.

```python
# Alice and Bob share two entangled Bell states
qc.h([qra[i] for i in range(3)])
qc.cx([qra[i] for i in reversed(range(3))],[qrb[i] for i in reversed(range(3))])
...
for i in range(3):
    with qc.if_test((cra[i], 1)): qc.x(i)
    with qc.if_test((cra[i+3], 1)): qc.z(i)
```

Bản nhiều qubit: `h`/`cx` nhận danh sách qubit để tạo 3 cặp Bell cùng lúc; trạng thái 3 qubit được chuẩn bị trên `qra[3..5]` bằng `x`, `cry`, `cx`, `z`; Bob sửa từng qubit bằng cặp bit `(cra[i], cra[i+3])`. Khi mô phỏng, `partial_trace(ψout, [3..8])` giữ lại 3 qubit của Bob.

> Lưu ý: các comment trong cell nhiều qubit không khớp code: "two entangled Bell states" (thực tế tạo 3 cặp) và "Alice prepares state |w⟩ = 1/2|01⟩ - √3/2|10⟩" (thực tế mạch chuẩn bị $\frac{1}{\sqrt{3}}(|001\rangle - |010\rangle + |100\rangle)$, đúng như output). Ngoài ra, ở bài 1 qubit, dòng in `(j,i) = ({alices_bits[1]},{alices_bits[0]})` có vẻ đảo nhãn: chuỗi memory của Qiskit viết bit cao trước, nên `alices_bits[1]` là `cra[0]`, tức bit $i$ điều khiển $X$. Điều này không ảnh hưởng tới trạng thái cuối của Bob.

### Kết quả

- **1 qubit**, 5 lần chạy: Alice đo được lần lượt (theo nhãn in ra) `(0,1)`, `(0,0)`, `(1,1)`, `(0,1)`, `(0,0)`. Lần nào Bob cũng nhận $\frac{\sqrt{2}}{2}|0\rangle - \frac{\sqrt{2}\,i}{2}|1\rangle$, đúng bằng $|q\rangle$ Alice đã chuẩn bị.
- **3 qubit**, 5 lần chạy: Alice đo `011100`, `111100`, `011001`, `001110`, `100001`. Lần nào Bob cũng nhận $\frac{\sqrt{3}}{3}|001\rangle - \frac{\sqrt{3}}{3}|010\rangle + \frac{\sqrt{3}}{3}|100\rangle$.

### Ghi nhớ nhanh

- Tài nguyên: 1 cặp Bell dùng chung + 2 bit cổ điển → gửi được 1 qubit (cặp Bell bị tiêu hao).
- Mạch của Alice: $CX$ (qubit $|q\rangle$ điều khiển) → $H$ trên qubit $|q\rangle$ → đo 2 qubit.
- Bob sửa: $Z^j X^i$; $X$ theo bit của qubit thuộc cặp Bell, $Z$ theo bit của qubit $|q\rangle$.
- Kết quả đo của Alice ngẫu nhiên (mỗi khả năng $1/4$) nhưng trạng thái cuối của Bob luôn là $|q\rangle$.
- Qiskit: `if_test` cho điều khiển cổ điển, `save_statevector` + `partial_trace` để xem trạng thái của Bob.

---

## 03_03 · Superdense Coding (Mã hóa siêu đặc)

**Mục tiêu** — Gửi **2 bit cổ điển** bằng cách truyền **1 qubit**, nhờ một cặp Bell đã chia sẻ trước. Đây là "chiều ngược" của teleportation (Bennett và Wiesner; công bố năm 1992).

### Kiến thức chính

Khác teleportation: không cần kênh cổ điển, nhưng kênh lượng tử phải truyền được thêm một qubit nữa.

0. Alice khởi tạo $|00\rangle_A$.
1. Alice tạo $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B)$ và gửi một qubit cho Bob.
2. Alice mã hóa 2 bit $(j,i)$ lên qubit của mình: áp $X$ nếu $i=1$, rồi $Z$ nếu $j=1$:
   $|\psi\rangle_2 = (Z^j \otimes I)(X^i \otimes I)|\psi\rangle_1$. Kết quả là một trong 4 Bell state:

| $(j,i)$ | Cổng Alice áp | $\lvert\psi\rangle_2$ | Bob đo được |
|---|---|---|---|
| (0,0) | $I$ | $\lvert\Phi^+\rangle = \frac{1}{\sqrt{2}}(\lvert 00\rangle + \lvert 11\rangle)$ | `00` |
| (0,1) | $X$ | $\lvert\Psi^+\rangle = \frac{1}{\sqrt{2}}(\lvert 10\rangle + \lvert 01\rangle)$ | `01` |
| (1,0) | $Z$ | $\lvert\Phi^-\rangle = \frac{1}{\sqrt{2}}(\lvert 00\rangle - \lvert 11\rangle)$ | `10` |
| (1,1) | $ZX$ | $\lvert\Psi^-\rangle$ (notebook ghi $\frac{-1}{\sqrt{2}}(\lvert 10\rangle - \lvert 01\rangle)$) | `11` |

   (Trong ket, qubit của Alice viết trước, qubit của Bob viết sau.)
3. Alice gửi qubit của mình cho Bob. Bob áp $CX$ rồi $H$: $|\psi\rangle_3 = (H\otimes I)\,CX\,|\psi\rangle_2$, đưa 4 Bell state về $|00\rangle, |01\rangle, |10\rangle, |11\rangle$. Bob đo và thu đúng $(j,i)$ với xác suất 100%.

**Vì sao được:** 4 Bell state trực giao với nhau, nên phân biệt được hoàn toàn bằng một phép đo trong cơ sở Bell. Alice chỉ cần tác động cục bộ lên qubit của mình là chọn được 1 trong 4 trạng thái đó.

**Mở rộng:** với $n$ cặp Bell, Alice gửi được $2n$ bit (notebook dùng $n=3$, tức 6 bit).

> Lưu ý: bảng kết quả cuối (sau bước 3) trong notebook vẫn ghi nhãn là $|\psi\rangle_2$, lẽ ra là $|\psi\rangle_3$.

### Code chính

```python
alice_bits = np.random.randint(2,size=2)
qc = QuantumCircuit(qr,cr)

qc.h(qr[1])                          # Bell pair
qc.cx(qr[1],qr[0])
if alice_bits[1] == 1: qc.x(1)       # Alice encodes
if alice_bits[0] == 1: qc.z(1)
qc.cx(qr[1],qr[0])                   # Bob: Bell -> computational
qc.h(qr[1])
qc.measure(qr,cr)
```

(Đã lược `barrier()` và rút gọn comment.) Qubit 1 là của Alice. Cổng mã hóa được thêm bằng `if` của Python lúc *dựng* mạch (không phải điều khiển cổ điển trong mạch như `if_test`), vì Alice biết trước bit của mình.

```python
simulator = AerSimulator()
qc_t = transpile(qc, simulator)
bob_bits = simulator.run(qc_t, shots=1, memory=True).result().get_memory()[0]
```

`transpile` biên dịch mạch cho backend, sau đó chạy 1 shot và đọc chuỗi bit Bob đo được bằng `get_memory()`.

```python
for qbit, bit_pair in enumerate(reversed(alice_bit_pairs)):
    if bit_pair[1] == 1: qc.x(qr_encode[qbit])
    if bit_pair[0] == 1: qc.z(qr_encode[qbit])
...
for qbit in range(n):
    qc.measure(qr_entangle[qbit],cr[2*qbit])
    qc.measure(qr_encode[qbit],cr[2*qbit+1])
```

Bản $n$ cặp: hai thanh ghi `entangle`/`encode`, mỗi cặp bit mã hóa lên một qubit `encode`. Thứ tự `reversed` cùng cách gán classical bit giúp chuỗi Bob đọc ra có cùng thứ tự với chuỗi Alice (Qiskit in bit cao trước).

### Kết quả

- 1 cặp: `Alice enconded bits (1,1)`, `Bob recovered bits (1,1)`.
- 3 cặp: `Alice encoded bits 000100`, `Bob recovered bits 000100`.

Bit được chọn ngẫu nhiên nên mỗi lần chạy lại sẽ khác, nhưng bit của Bob luôn trùng bit của Alice.

### Ghi nhớ nhanh

- Tài nguyên: 1 cặp Bell dùng chung + gửi 1 qubit → truyền được 2 bit.
- Alice mã hóa: $X^i$ rồi $Z^j$ lên qubit của mình, tạo ra 1 trong 4 Bell state.
- Bob giải mã: $CX$ → $H$ → đo, chính là mạch "Bell → cơ sở tính toán" giống bước của Alice trong teleportation.
- Teleportation và superdense coding đối ngẫu: (2 bit → 1 qubit) và (1 qubit → 2 bit), cả hai đều cần entanglement chia sẻ trước.

---

## Tổng hợp API Qiskit dùng trong phần này

| API / hàm | Dùng để | Bài |
|---|---|---|
| `QuantumCircuit`, `.h`, `.x`, `.z`, `.id`, `.cx`, `.ry`, `.p`, `.cry` | Dựng mạch, cổng một và hai qubit | 03_01, 03_02, 03_03 |
| `QuantumRegister`, `ClassicalRegister` | Thanh ghi có tên (Alice/Bob) | 03_02, 03_03 |
| `qiskit.circuit.Parameter` | Mạch có tham số $\theta$, $\varphi$ | 03_01 |
| `SparsePauliOp` | Định nghĩa observable $Z$, $X$, $Y$ | 03_01 |
| `qiskit_ibm_runtime.Estimator(mode=AerSimulator())` | Tính giá trị kỳ vọng (primitive V2, PUB có precision) | 03_01 |
| `Statevector`, `.evolve`, `.probabilities_dict` | Mô phỏng statevector và xác suất đo | 03_01 |
| `QuantumCircuit.inverse()` | Mạch nghịch đảo $U^\dagger$ để kiểm tra đồng xu | 03_01 |
| `plot_distribution` | Vẽ phân bố xác suất | 03_01 |
| `.measure`, `.barrier` | Đo, phân tách các bước trong hình vẽ | 03_02, 03_03 |
| `QuantumCircuit.if_test` | Áp cổng theo giá trị bit cổ điển (dynamic circuit) | 03_02 |
| `.save_statevector` (Aer) | Lưu statevector bên trong mô phỏng | 03_02 |
| `AerSimulator().run(..., shots=1, memory=True)`, `get_memory()` | Chạy một shot và lấy chuỗi bit | 03_02, 03_03 |
| `partial_trace`, `DensityMatrix.to_statevector()` | Tách trạng thái riêng của Bob | 03_02 |
| `transpile` | Biên dịch mạch cho simulator | 03_03 |
| `qc.draw(cregbundle=False, fold=-1, idle_wires=True)` | Vẽ mạch | 03_01, 03_02, 03_03 |

## Cách chạy

- Mở notebook bằng Jupyter hoặc VS Code, chọn kernel `.venv` của repo, chạy lần lượt từ trên xuống dưới.
- Thư viện cần thiết nằm trong [`requirements.txt`](../../requirements.txt) (cài từ gốc repo: `pip install -r requirements.txt`).
- Mọi thứ chạy trên simulator cục bộ (`AerSimulator`, `Statevector`). `qiskit_ibm_runtime.Estimator(mode=AerSimulator())` ở bài 03_01 cần cài gói `qiskit-ibm-runtime` nhưng không cần tài khoản IBM.
- Các bài dùng số ngẫu nhiên (đồng xu, bit của Alice, kết quả đo) nên output mỗi lần chạy sẽ khác bản đã lưu, nhưng kết luận vẫn giữ nguyên.

---

<!-- nav -->
[← 02 · Quantum computing](../02_quantum_computing/README.md) · [Mục lục](../../README.md#mục-lục) · [04 · Quantum algorithms →](../04_quantum_algorithms/README.md)
