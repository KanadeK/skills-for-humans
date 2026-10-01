---
name: count-one-calc-log-category-with-countif
description: "Human-readable one-category COUNTIF in Calc with criterion, range and near-match checks against visible source rows."
---
# 用 COUNTIF 统计 Calc 日志一个类别 / Count One Calc Log Category with COUNTIF

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已保存日志、普通类别列、一个明确要计数的类别 / Saved log, ordinary category column and one exact category to count |
| Side effects / 现实副作用 | 该类别的记录次数有可复核数字 / One category has a reproducible row count |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你想知道小日志中一个明确类别出现了几次，而不是所有活动总行数时使用本篇。成果是列出类别词、所查列范围和 COUNTIF 结果，再与少量可见行手数对照。近似拼写、大小写或前后空格是否应算同类是人的决定，不由公式自动裁决。

### 准备与输入

保存副本，确认类别列从哪一行到哪一行，并从原记录选一个完整、无歧义的类别词。先目视数几条匹配与一个近似但不应匹配的词。把结果放在表外；本机公式参数分隔符和匹配选项按当前 Calc 帮助。

### 执行

1. 在汇总格输入针对类别列的 COUNTIF，例如范围为 C2:C11 且词为 Reading 时用 `=COUNTIF(C2:C11;"Reading")`。
2. 检查公式中不含标题、不漏最后一行，条件词与原数据逐字一致。
3. 对一小段记录手数目标词和近似词，比较公式结果；异常则查空格、大小写及 Calc 匹配选项。
4. 记录类别、范围和结果；增加新行后主动复核范围是否需扩展。

### 完成、常见问题与恢复

结果代表指定类别在明确范围内的出现次数，手工抽查支持它；拼写不同的行保持待核而非默并。

- **计数为零：** 检查引号、实际列与词中空格。
- **近似词也算入：** 核匹配设置并手工比对。
- **新行没算：** 扩展范围并复核旧结果。

### 假设与边界

本篇只计算一个类别，不清洗类别词，也不把计数当质量分数。你决定类别等价关系；Calc 的通配符或正则设置可能改变文本匹配。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26209-FormulasAndFunctions.html)（英文，官方手册）— COUNTIF 按指定条件统计一个范围，匹配设置会影响文本结果。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when you need the number of rows in one named category rather than the whole log count. Finish with the category word, checked source range and COUNTIF result, then manually compare a small visible sample. Similar spellings, case and surrounding spaces are human classification decisions, not automatically settled by a formula.

### Preparation and inputs

Save a copy, identify first and last category rows, and choose one full unambiguous word from source records. Count a few matching rows and one near-match that should differ. Put the result outside the range; use your Calc version's argument separator and matching settings.

### Execution

1. Enter COUNTIF on the category range, such as `=COUNTIF(C2:C11;"Reading")` only if that is the actual range and word.
2. Check the formula excludes header, includes last row and uses the exact source category word.
3. Manually count target and near-match words in a small segment. If results differ, inspect spaces, case and Calc matching options.
4. Record category, range and result; after appending rows, recheck whether the range must expand.

### Success, common problems, and recovery

The result represents occurrences of one category in a declared range and a manual sample supports it; differently spelled rows remain for review.

- **Count is zero:** Check quotes, source column and spaces.
- **Near-match included:** Review matching settings and source words.
- **New row absent:** Extend range and recheck.

### Assumptions and limits

This counts one category, not cleans vocabulary or scores quality. You decide equivalence; Calc wildcard or regular-expression settings may change text matching.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26209-FormulasAndFunctions.html) — COUNTIF counts a range by criterion and text matching settings can affect result.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
