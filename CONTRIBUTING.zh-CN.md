# 参与贡献

[Tiếng Việt](CONTRIBUTING.md) · [English](CONTRIBUTING.en.md) · **简体中文**

感谢你愿意出一份力。本仓库把 [learnquantum.io](https://learnquantum.io) 这本书中的知识分享给越南语读者，并提供英文和简体中文译本。我们欢迎任何形式的贡献，从修正一个错别字到为新章节编写讲解都可以。

## 贡献方式

| 你想 | 怎么做 |
|---|---|
| 报告书中内容的错误（公式、代码、解释） | 使用 **Báo lỗi trong sách**（报告书中错误）模板提交 issue |
| 报告某个 notebook 无法运行 | 使用 **Notebook không chạy**（notebook 无法运行）模板提交 issue，并附上 Qiskit 版本和 traceback |
| 对讲解（越南语、英文或简体中文版本）提出建议或进行修改 | 使用 **Góp ý hướng dẫn**（讲解改进建议）模板提交 issue，或者直接提交 pull request |
| 询问书中的知识 | 使用 **Câu hỏi khi học**（学习中的问题）模板提交 issue（可以用越南语、英文或中文提问），或者到[上游仓库的 Discussions](https://github.com/learn-quantum/lqc-textbook/discussions) 向作者提问（英文） |

## 最重要的原则：notebook 保持原样

`chapters/` 中**除各 README 以外**（`README.md` 及其两个译本 `README.en.md`、`README.zh-CN.md`）的所有文件，都是[上游仓库](https://github.com/learn-quantum/lqc-textbook)的逐字节副本，包括作者运行后保存的输出，也包括其中的错误。这样读者可以与网页版对照，而从上游更新时也只需直接复制覆盖。

- **不要**修改 `chapters/` 中的 notebook 和图片，也不要重新运行后保存，或清除其输出。
- 发现书中的错误时，请记录下来，而不是在原处直接修改：
  1. 在该部分 README 的相关位置添加 `> Lưu ý: ...` 注释；
  2. 在 [ERRATA.md](ERRATA.zh-CN.md) 中相应的表格（代码错误、内容错误或笔误）里添加一行；
  3. 最好也到[上游仓库的 Issues](https://github.com/learn-quantum/lqc-textbook/issues) 告知作者。
- 修改之后，`python scripts/check_upstream.py` 必须报告 *in sync*。CI 每周也会检查这一点。

## 各部分 README 的模板

每个 `chapters/PP_ten_phan/` 文件夹中都有一个用越南语编写的 `README.md`（原文），格式如下；另有两个译本 `README.en.md` 和 `README.zh-CN.md`（见[翻译](#翻译英文与简体中文)）：

```markdown
# PP · 英文名称（越南语名称）

一小段话：这一部分讲什么，以及它如何与前后部分衔接。

> 来源：[PP_01](https://learnquantum.io/chapters/...) · [PP_02](...)
> — Diego Emilio Serrano, learnquantum.io, MIT License.

## 目录

| 课 | Notebook | 网页 | 要点 |
|---|---|---|---|

## PP_BB · 课名（越南语名称）

**目标** — 一句话。

### 核心知识
### 核心代码
### 运行结果
### 速记要点

## 本部分用到的 API 汇总
## 运行方法
```

文风：

- 用越南语撰写；术语首次出现时，在括号中保留原文，例如“vướng víu (entanglement)”。
- 公式使用 GitHub 的 LaTeX 语法：行内公式用 `$...$`，独立公式用 `$$...$$`。在表格中，用 `\vert` 代替 `|`（例如 `$\vert 0\rangle$`）。向量的长度（范数）在表格外写作 `$\|q\|$`，但在表格内必须写成 `$\Vert q\Vert$`，因为 GitHub 的表格会把 `\|` 读成一个 `|`。
- 从 notebook 摘录的代码保持原样，只允许添加解释性注释。
- **运行结果**取自 notebook 中已保存的输出，而不是你自己运行得到的结果。
- 句子要短，一句只讲一个意思；比较多项内容时优先使用表格。

## 从上游更新

当 `scripts/check_upstream.py`（或 **Upstream** 工作流）报告有变化时：

1. 克隆上游仓库：`git clone --depth 1 https://github.com/learn-quantum/lqc-textbook.git <tmp>`。
2. 把被报告为**新增**或**已修改**的文件从 `<tmp>/chapters/` 复制到 `chapters/` 中的相同路径；删除被报告为**已删除**的文件。
3. 重新运行 `python scripts/check_upstream.py --upstream <tmp>`，直到它报告 *in sync*。
4. 更新相应部分的 README 及其两个译本（新章节则按上面的模板编写 README）、[README.md](README.zh-CN.md) 中的目录，以及 README 中*来源与更新*一节里的 commit 和获取日期。
5. 重新检查 [ERRATA.md](ERRATA.zh-CN.md)：删除作者已经修正的错误。

被报告为 *empty stub* 的章节只有标题、还没有内容，因此暂时不需要复制。

## 编写入门文档（`docs/` 目录）

`docs/` 是本仓库为初学者自行编写的部分，因此它首先必须**正确**，其次才是好读：

- **每一条技术表述都必须可以核实**。引用数据时要注明来源；某件事*尚未被证明*时要明确说出来，而不是写得好像已成定论（例如：肖尔（Shor）算法与经典算法的比较）。
- **不要夸大硬件和应用的现状**。凡是会随时间变化的内容都要注明时间点，例如“截至 2026 年 10 月”。
- **文档中的每段代码都必须能运行**（`scripts/check_doc_snippets.py` 会检查这一点，而且每段代码都必须自带所需的全部 `import`，能够单独运行），文档中写出的输出必须来自真实的运行（采样得到的结果要注明每次运行都会不同）。
- **术语首次出现时要加以解释**，或者链接到[术语表](docs/glossary.zh-CN.md)；新术语要添加到术语表中。
- **不要承诺仓库无法保证的事情**。学习时间只是估计；尚未经过自动化测试的平台必须明确注明。
- 修改在多处使用的数据（notebook 数量、已测试的版本、学习时间）时，要找出并修改所有出现的地方：[README](README.zh-CN.md)、[docs/setup.md](docs/setup.zh-CN.md)、[docs/learning-path.md](docs/learning-path.zh-CN.md)、[docs/faq.md](docs/faq.zh-CN.md)。

## 翻译（英文与简体中文）

本仓库的每个 Markdown 文件（`README.md`、`CONTRIBUTING.md`、`ERRATA.md`、`docs/*.md`、`chapters/*/README.md`）旁边都有两个译本：`<名称>.en.md`（英文）和 `<名称>.zh-CN.md`（简体中文）。**越南语版本是原文**：先在越南语版本中修改内容，然后在同一个 pull request 中更新两个译本。

- 每个文件标题（`#`）之后的第一行是语言切换栏，必须严格符合下面的格式（当前语言加粗，另外两种语言链接到对应的同级文件）：

  ```markdown
  [Tiếng Việt](README.md) · **English** · [简体中文](README.zh-CN.md)
  ```

- 译文可以自然地表达，但必须**保持结构不变**：相同的标题（相同级别、相同顺序）、相同的公式、相同的代码（只能翻译注释）、相同的图片、相同的链接（如果目标文件有同一语言的译本，就指向该译本）、相同的表格行数和列表项数。`python scripts/check_translations.py` 会检查这些内容，CI 也会运行它。
- 含有文字标签的 `text` 图示块（例如 `docs/learning-path.md` 中的学习路线图）可以翻译，前提是它正上方一行是 `<!-- translate-block -->`（三个语言版本都要放这一行）。其他所有代码块必须与原文一致，只有注释可以不同。
- 译文中指向标题的链接（锚点，anchor）必须指向**翻译后**的标题；`python scripts/check_links.py` 会检查这一点。
- 专有名词、函数名、命令、路径、数据和时间点保持不变。术语首次出现时在括号中附上英文原文（中文版），并在整个仓库中统一使用同一种译法。
- 只做翻译，不增删内容。如果发现原文有错误，先修改越南语版本，再更新各个译本。
- issue 和 pull request 可以用越南语、英文或中文撰写。懂哪种语言，就可以帮忙审校该语言的译本。

## 提交 pull request 之前的检查

```bash
pip install -r requirements-dev.txt
pytest --nbmake chapters/                # 运行所有 notebook（不覆盖输出）
python scripts/check_upstream.py         # notebook 仍与上游一致
python scripts/check_links.py            # 所有 .md 文件中的链接、图片和锚点仍然正确（包括大小写）
python scripts/check_doc_snippets.py     # README 和 docs/ 中的每段 Python 代码都能运行
python scripts/check_translations.py     # .en.md 和 .zh-CN.md 译本仍与越南语版本一致
black --check scripts/ && ruff check scripts/
```

只想快速运行某一部分：`pytest --nbmake chapters/04_quantum_algorithms/`。

## 提交（commit）

commit 要小，每个 commit 只做一件事；commit 信息用英文书写，遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```text
docs(02_quantum_computing): explain the Bloch sphere angles
fix(errata): correct the Grover oracle note
chore: sync chapters with upstream 1a2b3c4
```

## 维护者须知

- 有两个工作流按计划每周运行（`notebooks.yml` 和 `upstream.yml`）。对于公开仓库，如果 60 天内没有任何活动，GitHub 会自动停用定时工作流；如果发现 CI 不再运行，请到 *Actions* 标签页重新启用。
- `upstream.yml` 只在上游有变化时发出提示（让工作流失败），不会自动更新任何内容。维护者需按照上面*从上游更新*一节的说明复制新章节。
- Markdown 中的公式：像 $\vert 0\rangle$ 中的竖线用 `\vert` 表示（不要用 `|` 或 `\|`），范数符号（向量长度）用 `\Vert` 表示。这两个命令在表格内外都能正确显示；`\|` 只在表格外显示正确。

## 许可证

参与贡献即表示你同意你的贡献以 [MIT License](LICENSE) 发布，与本仓库其余部分相同。
