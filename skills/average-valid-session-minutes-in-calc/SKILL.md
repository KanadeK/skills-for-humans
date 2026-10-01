---
name: average-valid-session-minutes-in-calc
description: "Human-readable AVERAGE of numeric session minutes in Calc with an included-count check and explicit handling of blanks or text."
---
# 用 Calc 求有效活动时长的平均值 / Average Valid Session Minutes in Calc

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已保存日志、同单位数字分钟列、至少两条有效记录 / Saved log, same-unit numeric minute column and at least two valid records |
| Side effects / 现实副作用 | 有明确分母的平均分钟数 / Average minutes has an explicit included count |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你想知道已记录的普通活动中**有效数字时长**的平均分钟数时使用本篇。成果不仅是一个 AVERAGE 数字，还包括实际参与计算的记录数与排除原因。平均值不是对所有空白行填零；若记录中有“约半小时”文本，先按原始事实处理，不能静默算成 30。

### 准备与输入

保存副本，确定数字分钟列的真实首末行。数清有效数字、空格、文本和异常值，确认所有数字单位都是分钟。为手算挑两三条小样本。汇总格置于来源范围外，明确显示结果是“平均每次有效记录”。

### 执行

1. 在汇总格用实际范围输入 AVERAGE，例如仅当 D2:D11 为真范围时 `=AVERAGE(D2:D11)`。
2. 另数范围中有效数字格的个数，核空白与文本未被算作零分钟参与分母。
3. 对两三条小样本用总和除以有效条数手算，比较本机显示值与预计四舍五入。
4. 标记排除项和范围，保存重开；如果有效数字为零，停止报告平均值。

### 完成、常见问题与恢复

平均值、单位、输入范围与有效分母都写明，小样本复核一致；无有效数值时有明确停止结论。

- **平均异常低：** 核是否真实的零值与空白混淆。
- **平均异常高：** 核漏行、文本数字和离群值来源。
- **只显示错误：** 检查范围内是否有有效数字及公式引用。

### 假设与边界

平均只描述这份日志中有效数字记录，不推断习惯、表现或健康。你决定哪些记录可纳入；格式显示不能修复源数据类型。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26209-FormulasAndFunctions.html)（英文，官方手册）— AVERAGE 忽略文本和空白，计算分母取决于有效数字格。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill for the mean minutes of valid numeric durations in an ordinary log. Finish with an AVERAGE value plus the number of records actually included and reasons for exclusions. An average does not turn blank rows into zero. A text note like 'about half an hour' cannot silently become 30.

### Preparation and inputs

Save a copy and find the true first and last duration rows. Count numeric, blank, text and suspicious cells; confirm all numbers use minutes. Choose two or three values for a manual sample. Put summary outside source and label it mean per valid record.

### Execution

1. Enter AVERAGE on the actual range, for example `=AVERAGE(D2:D11)` only when D2:D11 is real.
2. Count numeric cells included and confirm blank/text cells were not treated as zero-minute observations.
3. Manually divide a small sample sum by its valid count and compare with displayed result and rounding.
4. Label exclusions and range, save and reopen; if no numeric observations remain, do not report a mean.

### Success, common problems, and recovery

Mean, unit, input range and valid denominator are clear, a small manual check agrees, and zero valid values lead to a stop rather than a claimed mean.

- **Mean unexpectedly low:** Distinguish genuine zeros from blanks.
- **Mean unexpectedly high:** Inspect omitted rows, text numbers and source outliers.
- **Formula error:** Check valid numeric cells and reference.

### Assumptions and limits

The mean describes valid numeric records in this log, not habits, performance or health. You decide inclusion; display formatting cannot repair source data types.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26209-FormulasAndFunctions.html) — AVERAGE ignores text and blanks so denominator depends on valid numeric cells.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
