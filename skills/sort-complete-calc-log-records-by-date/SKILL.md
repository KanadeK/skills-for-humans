---
name: sort-complete-calc-log-records-by-date
description: "Human-readable Calc sort of complete row records by a verified date column, with header exclusion and row-integrity checks."
---
# 按日期排序 Calc 日志且保持整行对应 / Sort Complete Calc Log Records by Date

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存的日志副本、能解析的日期列、记录编号 / Saved log copy, parsed date column and record codes |
| Side effects / 现实副作用 | 完整记录按时间排列而字段不串行 / Whole records become chronological without split fields |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张日期先后混乱的小日志，想按日期排列完整记录时使用本篇。结果是每行的编号、类别、分钟与备注仍跟自己的日期在一起，并能说明升序或降序。这里改变记录顺序，可能影响你原来的手工顺序，所以必须在副本上核对。

### 准备与输入

先保存工作副本，确认日期列是真日期而非看似日期的文本。记下首末三个编号及其对应字段，确认第一行为标题。选择整张连续记录区，不只高亮一个日期列；空行可能让自动识别截断范围。

### 执行

1. 打开 Data > Sort，核对预览/区域包含所有记录列和数据行。
2. 把第一行设为标题不参与排序，选择日期列为第一准则，确定升序或降序。
3. 执行后检查日期的首末顺序，再按之前记录的编号找回对应类别、分钟与备注。
4. 若字段分家或日期顺序异常，立即撤销；修正区域或日期类型后再做，不保存错位结果。

### 完成、常见问题与恢复

日期按指定方向排列，标题留在顶部，抽查编号对应的各列仍原样；否则恢复副本并记录问题。

- **只有日期变位：** 撤销并选完整行范围。
- **标题混入数据：** 重做并启用标题选项。
- **看似日期排序怪：** 先核日期单元格类型。

### 假设与边界

本篇只排序小型单表普通记录。你要先确认全部列的关联；公式引用、合并单元格、共享协作或多个分离数据区会改变风险。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html)（英文，官方手册）— 排序区域、标题选项和排序准则决定整行是否正确移动。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when a small log has records out of date order. Finish with every code, category, minutes and note still attached to its own date, and a named ascending or descending order. This changes row order and may replace a manual order, so verify on a copy.

### Preparation and inputs

Save a working copy and confirm the date column contains real dates rather than date-looking text. Note the first and last three codes with their fields and confirm row one is a header. Select the complete contiguous record range, not only the date column; blank rows can break automatic range detection.

### Execution

1. Open Data > Sort and verify the range includes every record column and data row.
2. Exclude the header row, select date as the first sort key and choose ascending or descending.
3. After sorting inspect first/last dates, then find noted codes and compare category, minutes and notes.
4. If fields split or date order is wrong, undo immediately and correct range or date type before retrying.

### Success, common problems, and recovery

Dates follow the chosen direction, header stays at top, and checked codes retain their associated fields; otherwise restore the copy and record the issue.

- **Only dates moved:** Undo and select whole row range.
- **Header sorted as data:** Retry with header option.
- **Odd date order:** Check date cell types first.

### Assumptions and limits

This sorts a small ordinary single-table log. You must verify all linked fields; formulas, merged cells, shared editing or disjoint ranges change the risk.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html) — sort range, header setting and criteria govern complete-record movement.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
