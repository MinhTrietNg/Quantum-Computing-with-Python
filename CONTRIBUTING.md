# Đóng góp

Cảm ơn bạn muốn góp sức. Repo này chia sẻ kiến thức từ sách
[learnquantum.io](https://learnquantum.io) cho người đọc tiếng Việt. Mọi đóng góp đều được hoan nghênh,
từ sửa một lỗi chính tả đến viết hướng dẫn cho chương mới.

## Những cách đóng góp

| Bạn muốn | Làm gì |
|---|---|
| Báo lỗi trong nội dung sách (công thức, code, giải thích) | Mở issue **Báo lỗi trong sách** |
| Báo notebook không chạy được | Mở issue **Notebook không chạy**, kèm phiên bản Qiskit và traceback |
| Góp ý hoặc sửa hướng dẫn tiếng Việt | Mở issue **Góp ý hướng dẫn**, hoặc gửi pull request luôn |
| Hỏi về kiến thức trong sách | Dùng [Discussions của repo gốc](https://github.com/learn-quantum/lqc-textbook/discussions) |

## Nguyên tắc quan trọng nhất: notebook giữ nguyên văn

Mọi file trong `chapters/` **trừ `README.md`** là bản sao từng byte của
[repo gốc](https://github.com/learn-quantum/lqc-textbook), kể cả output tác giả đã chạy và kể cả lỗi.
Nhờ vậy người đọc có thể đối chiếu với web, và cập nhật từ bản gốc chỉ cần copy đè.

- **Không** sửa, chạy lại rồi lưu, hay clear output các notebook và hình trong `chapters/`.
- Tìm thấy lỗi trong sách thì ghi lại, không sửa tại chỗ:
  1. thêm ghi chú `> Lưu ý: ...` ngay chỗ liên quan trong README của phần đó;
  2. thêm một dòng vào bảng phù hợp (Code, Nội dung hoặc Đánh máy) trong [ERRATA.md](ERRATA.md);
  3. nên báo cho tác giả tại [Issues của repo gốc](https://github.com/learn-quantum/lqc-textbook/issues).
- `python scripts/check_upstream.py` phải báo *in sync* sau khi bạn sửa. CI cũng kiểm tra điều này hằng tuần.

## Khuôn README của một phần

Mỗi folder `chapters/PP_ten_phan/` có đúng một `README.md` viết bằng tiếng Việt, theo khuôn sau:

```markdown
# PP · Tên tiếng Anh (Tên tiếng Việt)

Một đoạn ngắn: phần này dạy gì và nối với phần trước/sau ra sao.

> Nguồn: [PP_01](https://learnquantum.io/chapters/...) · [PP_02](...)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## Mục lục

| Bài | Notebook | Web | Ý chính |
|---|---|---|---|

## PP_BB · Tên bài (Tên tiếng Việt)

**Mục tiêu** — một câu.

### Kiến thức chính
### Code chính
### Kết quả
### Ghi nhớ nhanh

## Tổng hợp API dùng trong phần này
## Cách chạy
```

Văn phong:

- Viết tiếng Việt; lần đầu gặp thuật ngữ thì giữ từ gốc trong ngoặc, ví dụ "vướng víu (entanglement)".
- Công thức dùng LaTeX của GitHub: `$...$` trong dòng, `$$...$$` cho công thức riêng. Trong bảng,
  viết `\vert` thay cho `|` (ví dụ `$\vert 0\rangle$`); chỉ dùng `\|` cho độ dài (chuẩn) của vector, ví dụ `$\|q\|$`.
- Code trích từ notebook giữ nguyên, chỉ được thêm comment giải thích.
- **Kết quả** lấy từ output đã lưu trong notebook, không phải từ lần chạy của bạn.
- Câu ngắn, mỗi ý một câu; ưu tiên bảng khi so sánh nhiều thứ.

## Cập nhật từ bản gốc

Khi `scripts/check_upstream.py` (hoặc workflow **Upstream**) báo có thay đổi:

1. Clone bản gốc: `git clone --depth 1 https://github.com/learn-quantum/lqc-textbook.git <tmp>`.
2. Copy các file được báo **mới** hoặc **đã sửa** từ `<tmp>/chapters/` vào `chapters/`, cùng đường dẫn;
   xoá các file được báo **đã xoá**.
3. Chạy lại `python scripts/check_upstream.py --upstream <tmp>` cho đến khi báo *in sync*.
4. Cập nhật README của phần tương ứng (với chương mới thì viết README theo khuôn ở trên), mục lục trong
   [README.md](README.md), và commit cùng ngày lấy về trong mục *Cập nhật từ bản gốc* của README.
5. Đọc lại [ERRATA.md](ERRATA.md): xoá những lỗi tác giả đã sửa.

Chương được báo *empty stub* là chương mới có tiêu đề, chưa có nội dung, nên chưa cần copy.

## Viết tài liệu nhập môn (thư mục `docs/`)

`docs/` là phần repo này tự viết cho người mới, nên nó phải **đúng** trước rồi mới đến hay:

- **Mỗi phát biểu kỹ thuật phải kiểm chứng được.** Trích nguồn khi nêu số liệu, và nói rõ khi một điều
  *chưa được chứng minh* thay vì viết như đã chắc chắn (ví dụ: Shor so với thuật toán cổ điển).
- **Không nói quá về phần cứng và ứng dụng.** Điều gì phụ thuộc thời điểm thì ghi mốc thời gian, ví dụ
  "đúng với hiểu biết đến tháng 10/2026".
- **Mọi đoạn code trong tài liệu phải chạy được** (`scripts/check_doc_snippets.py` kiểm tra điều này, và mỗi đoạn
  phải tự đủ `import` để chạy riêng), và output ghi trong tài liệu phải lấy từ lần chạy thật
  (kết quả lấy mẫu thì ghi chú là sẽ khác mỗi lần).
- **Giải thích thuật ngữ ở lần đầu xuất hiện**, hoặc dẫn tới [bảng thuật ngữ](docs/glossary.md); thêm thuật ngữ
  mới vào bảng đó.
- **Đừng hứa điều repo không đảm bảo.** Thời gian học là ước tính; nền tảng chưa kiểm thử tự động phải ghi rõ.
- Khi sửa số liệu dùng ở nhiều nơi (số notebook, phiên bản đã kiểm thử, thời gian học), tìm và sửa mọi chỗ:
  [README](README.md), [docs/setup.md](docs/setup.md), [docs/learning-path.md](docs/learning-path.md),
  [docs/faq.md](docs/faq.md).

## Kiểm tra trước khi gửi pull request

```bash
pip install -r requirements-dev.txt
pytest --nbmake chapters/                # chạy mọi notebook (không ghi đè output)
python scripts/check_upstream.py         # notebook vẫn khớp với bản gốc
python scripts/check_links.py            # link và anchor trong mọi file .md còn đúng
python scripts/check_doc_snippets.py     # mọi đoạn code Python trong README và docs/ chạy được
black --check scripts/ && ruff check scripts/
```

Muốn chạy nhanh một phần: `pytest --nbmake chapters/04_quantum_algorithms/`.

## Commit

Commit nhỏ, mỗi commit một việc, message tiếng Anh theo
[Conventional Commits](https://www.conventionalcommits.org/):

```text
docs(02_quantum_computing): explain the Bloch sphere angles
fix(errata): correct the Grover oracle note
chore: sync chapters with upstream 1a2b3c4
```

## Dành cho người bảo trì

- Hai workflow chạy theo lịch hằng tuần (`notebooks.yml` và `upstream.yml`). GitHub tự tắt workflow theo lịch
  trong repo công khai nếu repo không có hoạt động trong 60 ngày; nếu thấy CI ngừng chạy, vào tab *Actions* bật lại.
- `upstream.yml` chỉ báo (workflow thất bại) khi bản gốc có thay đổi; nó không tự cập nhật gì. Người bảo trì copy chương
  mới theo mục *Cập nhật từ bản gốc* ở trên.
- Công thức trong Markdown: dùng `\vert` (không dùng `\|`) cho dấu gạch đứng như $\vert 0\rangle$, và dùng `\|` chỉ
  khi muốn ký hiệu chuẩn (độ dài vector). Cách này hiển thị đúng cả trong bảng lẫn ngoài bảng.

## Giấy phép

Khi đóng góp, bạn đồng ý rằng phần đóng góp được phát hành theo [MIT License](LICENSE), giống phần
còn lại của repo.
