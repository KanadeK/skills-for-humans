---
name: enter-and-check-real-date-cells-in-calc
description: "Human-readable entry of unambiguous event dates in Calc with format and type checks before relying on chronological operations."
---
# 在 Calc 录入并核对真正的日期单元格 / Enter and Check Real Date Cells in Calc

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 现有 Calc、可核对的普通活动日期、已保存工作副本 / Existing Calc, verifiable ordinary event dates and saved working copy |
| Side effects / 现实副作用 | 日期可读且能按时间排序 / Dates are readable and sortable chronologically |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你想在普通活动日志中录入日期，并让它们以后能真正按时间排序时使用本篇。成果是两三个日期单元格解析为日期，显示格式明确，原始日月没有颠倒。只把字体改成日期样式并不能证明文本变成了日期。

### 准备与输入

从自己的普通活动或虚构样本取至少两个相隔月份的日期，写下原始年月日。区域设置可能把 `03/04` 解为不同日月，练习优先用 ISO `YYYY-MM-DD`。先保存工作副本，只处理日期列，不改旁边编号与分钟数。

### 执行

1. 在日期列录入完整 ISO 日期，离开单元格后检查 Calc 是否识别。
2. 用单元格格式选择清楚的日期显示，同时核输入栏与类型，不以显示替代转换。
3. 在小副本排序这几条完整记录，检查顺序是否与原始年月日一致，随后撤销或保留核过的结果。
4. 保存并重开，再查年月日和邻行仍对齐；日期有歧义就从源记录核实并重录。

### 完成、常见问题与恢复

至少两个跨月日期保留正确年月日，按时间而非字母顺序排列，重开仍一致。无法核原始日月时停在未验证状态。

- **日月颠倒：** 返回原始记录，用完整 ISO 日期重录。
- **像日期却排序怪：** 核是否文本，按官方转换指引处理。
- **邻列错位：** 撤销排序，从完整行范围重做。

### 假设与边界

区域语言和 Calc 版本影响解析，你必须与原始日期核对。此篇只作普通日志日期类型检查，不代表日历预约或法律时限确认。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html)（英文，官方手册）— Calc 识别 ISO 日期输入，显示格式和区域设置影响外观。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when dates in an ordinary activity log must later sort chronologically. Finish with two or three cells parsed as dates, a declared display format, and no month/day reversal. Changing appearance to a date style alone does not prove text became date data.

### Preparation and inputs

Take at least two dates in different months from permitted events or synthetic samples and note exact year, month and day. Locales can read `03/04` differently, so prefer ISO `YYYY-MM-DD`. Save a working copy and touch only the date column.

### Execution

1. Enter full ISO dates and leave each cell to see whether Calc recognizes them.
2. Choose a clear Date display in Format Cells while checking input and type.
3. On a small copy sort whole records by date and compare order with source year-month-day; undo or keep only a checked result.
4. Save and reopen, confirming dates and adjacent records. Verify ambiguous entries against source and re-enter.

### Success, common problems, and recovery

At least two dates across months retain correct year-month-day, sort in time rather than lexical order and remain so after reopening. Stop as unverified if source month/day cannot be confirmed.

- **Month/day swapped:** Check source and re-enter full ISO date.
- **Looks like date but sorts oddly:** Check for text data and official conversion steps.
- **Other columns misalign:** Undo sorting and retry on whole records.

### Assumptions and limits

Locale and Calc version affect parsing, so compare with source dates. This checks ordinary log cell types, not calendar bookings or legal deadlines.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html) — Calc accepts ISO date input while display format and locale affect appearance.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
