---
name: apply-real-heading-styles-to-a-writer-outline
description: "Human-readable conversion of visually bold Writer headings into semantic Heading 1 and Heading 2 paragraphs checked in Navigator."
---
# 把 Writer 现有标题改为真正的层级样式 / Apply Real Heading Styles to a Writer Outline

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有至少两级标题的非敏感 ODT 副本、当前 Writer 样式面板 / Non-sensitive ODT copy with two heading levels and Writer Styles panel |
| Side effects / 现实副作用 | 文稿导航器识别原本只是加粗的标题 / Navigator recognizes headings once only visually bold |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一份内容已写好的文稿，标题只是手工加粗放大，想让 Writer 识别真正的一级、二级结构时使用本篇。成果是 Navigator 中按顺序出现两级标题，正文仍是正文。它不重新写标题文字，也不把每个加粗句子都猜成标题。

### 准备与输入

保存 ODT 副本，把预期一级与二级标题列在纸上，标明它们之间正文的起止。打开 Styles 面板与 Navigator，先观察目前缺失或错层的条目。选择标题时只把光标放在该段，不选跨正文的文字；编号如需保留先记下。

### 执行

1. 逐段将最高级标题应用 Heading 1，下属标题应用 Heading 2，不用直接字体大小冒充层级。
2. 打开 Navigator 的标题列表，检查顺序、缩进和遗漏项与事先列出的结构一致。
3. 抽查每个标题后的一段正文仍是正文样式，避免连下一段都被改成 Heading。
4. 若层级错，改该段样式后重看 Navigator；保存重开再核层级。

### 完成、常见问题与恢复

预期标题在 Navigator 中按两级出现，正文未混入，原文字与顺序保留。

- **正文被当标题：** 把该段恢复正文样式。
- **二级被顶成一级：** 核当前段落样式改 Heading 2。
- **导航缺一项：** 核该标题是否只做了直接加粗。

### 假设与边界

本篇只处理已知两级结构，不能自动判断文稿语义。你决定哪些句子是标题；具体样式面板入口随界面布局变化。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26209-WorkingWithStyles.html)（英文，官方手册）— 段落样式可表达标题层级并影响导航与目录。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a finished draft has headings that are only manually bold or enlarged and Writer must recognize a real two-level outline. Finish with Heading 1 and Heading 2 entries in Navigator in the intended order, while body paragraphs remain body text. Do not rewrite title words or infer every bold sentence is a heading.

### Preparation and inputs

Save an ODT copy and list intended first- and second-level headings with surrounding body boundaries. Open Styles and Navigator to observe missing or wrong-level entries. Place cursor inside one heading paragraph without selecting body text. Note any numbering that must remain.

### Execution

1. Apply Heading 1 to top sections and Heading 2 to subordinate heading paragraphs, not direct font size as a substitute.
2. Inspect Navigator headings for order, indentation and omissions against your written outline.
3. Spot-check the following body paragraph after each heading to ensure it remains body style.
4. Correct the paragraph style of a wrong-level heading, then recheck Navigator and reopen once after saving.

### Success, common problems, and recovery

Intended headings appear in Navigator at two levels, body does not, and original wording and order remain.

- **Body appears as heading:** Restore body paragraph style.
- **Subheading becomes top level:** Check paragraph and set Heading 2.
- **Heading missing:** Check for direct bold instead of style.

### Assumptions and limits

This handles a known two-level outline, not automatic semantic judgment. You decide which sentences are headings; Styles-panel entry varies by UI.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26209-WorkingWithStyles.html) — paragraph styles express heading hierarchy and feed navigation and contents.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.

