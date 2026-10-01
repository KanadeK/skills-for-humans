---
name: sum-numeric-session-minutes-in-calc
description: "Human-readable SUM of a checked numeric duration range in a neutral Calc log, including a small manual cross-check and excluded-text warning."
---
# 用 Calc 核对一段活动分钟数合计 / Sum Numeric Session Minutes in Calc

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已保存日志、同单位的数字分钟列、至少两条可手算记录 / Saved log, same-unit numeric minutes column and at least two manually checkable rows |
| Side effects / 现实副作用 | 有范围明确且可复算的分钟数合计 / A range-bounded reproducible total of minutes |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一列普通活动的分钟数，想知道**指定几行**的总时长时使用本篇。成果是标明范围与单位的 SUM 结果，并用至少两行手算复核。不要把文本“30 分钟”、空格或筛选后隐藏行自动当作已参与合计；先决定统计口径。

### 准备与输入

保存副本，找出分钟列首末数据行，例如 D2 到 D11；核每格单位都为分钟、数值非文本，记下两三条已知数字作手算对照。把汇总格放在表外或清楚标成汇总，避免它落进自己的求和范围形成循环。

### 执行

1. 在汇总格输入覆盖实际首末行的公式，例如仅当范围确为 D2:D11 时用 `=SUM(D2:D11)`。
2. 核公式栏中的范围没有标题、汇总格或漏掉最后一条记录。
3. 用已知两三行手算一个小副本结果，或临时只对样本区求和，与 Calc 结果比较。
4. 检查空白、文本和筛选状态，标注结果代表的范围与单位，保存重开再核一次。

### 完成、常见问题与恢复

总数与明确的数字范围相符，小样本复核通过，单位写明分钟；文本或缺值会被列为未纳入项。

- **结果偏小：** 找文本型数字或漏掉的末行。
- **结果偏大：** 检查是否把汇总行或无关行纳入。
- **公式报循环：** 把结果格移出输入范围。

### 假设与边界

只对同一单位的普通分钟数求和，不评价健康或效率。你选统计范围；SUM 忽略文本与空白，结果不能替代原始记录质量检查。

### 来源

- [LibreOffice Calc Guide 26.2](https://help.libreoffice.org/latest/en-US/text/scalc/01/func_sum.html)（英文，官方手册）— SUM 累加指定范围内数字，忽略空白和文本。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when you need the total duration of a stated set of ordinary activity rows. Finish with a SUM result labelled by range and minutes, checked manually against at least two rows. Do not assume a text value such as '30 minutes', a blank, or filtered-hidden row participates as expected; decide the counting boundary first.

### Preparation and inputs

Save a copy and identify first and last duration cells, such as D2 through D11. Confirm all units are minutes and values are numeric, then note two or three known numbers for manual checking. Place the result outside the source range or label it clearly to avoid a circular reference.

### Execution

1. Enter a formula covering actual first and last rows; use `=SUM(D2:D11)` only when that is the real range.
2. Check formula range excludes header and result cell and includes the final intended event.
3. Manually add two or three known rows or test a small sample range and compare with Calc.
4. Inspect blanks, text and filter state; label scope and unit, then save and reopen to verify.

### Success, common problems, and recovery

The total matches the stated numeric range, a small manual check passes, and minutes are labelled. Text or missing values are listed as exclusions.

- **Total too low:** Look for text numbers or missing last row.
- **Total too high:** Check for total or unrelated rows in range.
- **Circular reference:** Move result outside input range.

### Assumptions and limits

This sums ordinary same-unit minutes, not health or performance. You choose the range. SUM ignores text and blanks, so result cannot replace source-quality review.

### Sources

- [LibreOffice Calc Guide 26.2](https://help.libreoffice.org/latest/en-US/text/scalc/01/func_sum.html) — SUM adds numbers in a specified range and ignores blanks and text.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
