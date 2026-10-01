---
name: turn-aligned-writer-facts-into-a-small-table
description: "Human-readable creation of a small Writer table from existing permitted facts, with one header row and cell-by-cell integrity checks."
---
# 把 Writer 已有对齐资料放进小表格 / Turn Aligned Writer Facts into a Small Table

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 几条已核对的非敏感资料、ODT 工作副本、明确列名 / Several checked non-sensitive facts, ODT working copy and clear column names |
| Side effects / 现实副作用 | 资料成为带表头的真实单元格 / Facts become real cells under headers |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有几条已经核过的普通资料，现在靠空格凑成两三列，想让列真正对齐并可逐格阅读时使用本篇。成果是一张含标题行的小型 Writer 表，原资料各归正确单元格，没有因转表漏掉词句。它是文档内的展示表，不代替 Calc 的计算表。

### 准备与输入

保存 ODT 副本，先在纸上列出列名、需要几条资料行，确认每行字段数一致。记录首条和末条的原文。若资料含私人身份或业务机密，先不要做公开展示。确定表格前后要保留的正文段落。

### 执行

1. 在指定位置插入所需行列的小表，设置第一行为标题；不要用多个空格继续模拟列。
2. 逐行将原资料放进对应单元格，先核列名，再核首末数据行。
3. 检查表前后的正文未被吸进表里，逐格看是否截字或跨错列。
4. 保存重开，对照原资料抽查所有字段；若行列数不适配，调整表结构而不删原信息。

### 完成、常见问题与恢复

表头准确、每条资料行对齐且与原文一致，前后正文完整。

- **某行字段挤一格：** 按原列名拆回对应格。
- **正文进了表：** 撤销并在正确段落边界重插。
- **内容显示不全：** 调整列宽/行高再核真实文字。

### 假设与边界

只适合少量已知事实的简单展示。你负责源资料正确与展示许可；复杂跨页或计算表应另用更适合的结构。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26213-Tables.html)（英文，官方手册）— Writer 插入表格时先规划行列并可设置标题行。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a few checked ordinary facts are spaced into two or three pseudo-columns in Writer and need real aligned cells. Finish with a small table including a heading row, each source fact in the intended cell, and no lost wording. This is a display table inside a document, not a Calc calculation sheet.

### Preparation and inputs

Save an ODT copy and plan column names and data-row count on paper. Confirm each source row has the same fields; note first and last original wording. Avoid public display for identity or confidential details. Identify body paragraphs to preserve before and after the table.

### Execution

1. Insert a small table with planned rows and columns at the chosen point, using row one as headings.
2. Place source facts cell by cell; verify column names, then first and last data rows.
3. Check surrounding prose did not enter the table, and inspect cells for clipped or miscolumned text.
4. Save and reopen, comparing fields with source. Adjust table structure if needed without discarding facts.

### Success, common problems, and recovery

Headers are accurate, every record aligns with source, and surrounding body text remains complete.

- **Fields jam into one cell:** Distribute by original column meanings.
- **Body enters table:** Undo and insert at proper paragraph boundary.
- **Text clipped:** Adjust size and verify actual text.

### Assumptions and limits

This suits a few known facts for display. You own source correctness and permission. Complex multipage or calculation tables need different work.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26213-Tables.html) — Writer table insertion benefits from planned rows/columns and a heading row.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.

