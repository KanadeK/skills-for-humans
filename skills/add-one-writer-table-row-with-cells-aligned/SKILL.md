---
name: add-one-writer-table-row-with-cells-aligned
description: "Human-readable insertion of one new row in an existing Writer table, preserving header and neighboring records while placing every value in its column."
---
# 给 Writer 现有表格补一行并核对列位 / Add One Writer Table Row with Cells Aligned

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有带表头的非敏感 Writer 表、要补的一条完整资料 / Existing non-sensitive Writer table with header and one complete new record |
| Side effects / 现实副作用 | 新行进入表内且旧行不移错列 / One new row joins the table without shifting old fields |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张已存在的小表，需要补入一条普通资料，想保持每个字段仍在原来的列时使用本篇。成果是表内新增一整行，表头、旧行和表外正文不变，新值与列名对齐。它不是建表或改变表头跨页行为，而是一次具体记录追加。

### 准备与输入

保存 ODT 副本，核新记录的各字段与现表列名一一对应，记下原行数与末条内容。把光标放到要插入位置附近的现有行单元格；不要把普通回车当作新表行。若表有合并格，先确认新增行会继承什么结构。

### 执行

1. 使用 Table > Insert > Rows Above/Below，明确新行放在目标旧行的哪一侧。
2. 逐格填入新资料，按表头从左到右核字段，不用制表符盲跳越界。
3. 核行数只多一、旧末条和表头原样，表外正文没有被挪入新行。
4. 保存重开抽查新行与两侧旧行；若插错位置就撤销并重选正确行。

### 完成、常见问题与恢复

恰好多一整行，新字段对应列名，旧记录及正文仍完整。

- **新增成了新表：** 撤销并在原表单元格内操作。
- **字段错列：** 对照表头逐格修正。
- **多出空行：** 核是否重复插入，撤销多余行。

### 假设与边界

只追加一条结构简单的表记录。你负责源值与行位；有复杂合并格或公式的表需要额外核查。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26213-Tables.html)（英文，官方手册）— Table > Insert 可在当前行上下新增整行且继承相邻格式。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an existing small Writer table needs one ordinary new record without losing column alignment. Finish with one whole row inside the table, header and old rows unchanged, and each new value under its intended label. This appends a record rather than creating the table or configuring repeating headers.

### Preparation and inputs

Save an ODT copy, map each new fact to an existing header and note original row count and last record. Put cursor in a current row near insertion point; a normal Enter is not a new table row. If merged cells exist, inspect what the new row may inherit first.

### Execution

1. Use Table > Insert > Rows Above/Below, explicitly choosing the side of the target old row.
2. Fill each new cell and check field alignment left to right against headers, avoiding blind tabs past the table edge.
3. Check row count increased by one, old last record and header remain, and outside prose did not move into the row.
4. Save and reopen, inspecting new row and neighbours. Undo wrong placement and choose the right row again.

### Success, common problems, and recovery

Exactly one whole row is added with fields under correct labels, while older records and body text remain intact.

- **A separate table appears:** Undo and work inside existing table cell.
- **Values under wrong headers:** Correct cell by cell against labels.
- **Extra blank row:** Check duplicate insertion and undo excess.

### Assumptions and limits

This appends one structurally simple record. You verify source facts and placement. Tables with merged cells or formulas need further review.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26213-Tables.html) — Table > Insert can add a row above or below and inherit neighbouring format.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.

