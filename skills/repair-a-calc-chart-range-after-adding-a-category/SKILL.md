---
name: repair-a-calc-chart-range-after-adding-a-category
description: "Human-readable recovery when an existing Calc chart omits an appended category, updating its source range and verifying the new bar."
---
# 新增类别后修正 Calc 图表的数据范围 / Repair a Calc Chart Range After Adding a Category

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 现有类别次数图、刚增加的已核类别汇总行、保存副本 / Existing category-count chart, newly checked summary row and saved copy |
| Side effects / 现实副作用 | 图表包含新类别且旧柱仍对应原值 / Chart includes new category without losing old bars |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在类别汇总表末尾新增一行，原有图表却没有出现新类别时使用本篇。成果是图表数据范围包含新行，新柱与新计数相符，旧柱和原数据仍正常。它从一个已发生的漏图故障恢复，不是第一次建图，也不通过复制一张全新图掩盖旧图范围问题。

### 准备与输入

保存工作副本，记下新类别及其次数、图表当前已有类别数与最后一行来源地址。先核新汇总行本身正确且是数字，不要因为图不更新就改原日志。确认编辑的是正确图对象，图旁若有另一张表不要误纳入。

### 执行

1. 双击目标图进入编辑模式，打开 Format > Data Ranges 或当前版本相同命令。
2. 查看范围末行、首行标签、行列方向与系列；只把新类别汇总行纳入，避免把总计或空行也带入。
3. 确认后比较新柱数值与新行，也抽查旧最大和最小柱未变化。
4. 退出编辑模式，保存重开；若新柱仍不见，回源类型与系列设置，不声称已修复。

### 完成、常见问题与恢复

旧图现在包含新类别且数值对应，旧类别仍在，源表没有被改；否则记录尚未修好的范围或类型原因。

- **把总计也画上：** 缩回范围，只选真实类别行。
- **新柱标签错：** 核首行标签和类别列。
- **图仍不变：** 检查新计数是不是文本以及数据系列。

### 假设与边界

本篇只修现有图的一个新增类别遗漏。你必须核对来源行；公式汇总未刷新、引用外部文件或复杂图表系列需单独处理。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26206-CreatingChartsAndGraphs.html)（英文，官方手册）— 可在图表编辑模式的 Data Ranges 中修正来源区域。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill after adding a checked category row to a summary when the existing chart omits it. Finish with the source range including that row, a bar matching its count, and old bars/source data intact. This recovers an actual omission rather than making a new chart to hide a range fault.

### Preparation and inputs

Save a working copy. Note new category/count, existing chart category count and source's last row. Confirm the new summary itself is correct and numeric; do not alter raw log just because chart is stale. Identify the right chart and nearby unrelated tables.

### Execution

1. Double-click target chart to enter edit mode and open Format > Data Ranges or equivalent.
2. Inspect last source row, header labels, series direction and series; add only new category row, not total or blanks.
3. After confirming, compare new bar with new row and spot-check old largest and smallest bars.
4. Exit edit mode, save and reopen. If new bar remains absent, inspect source type and series settings without claiming repair.

### Success, common problems, and recovery

The existing chart includes the new category with matching value, old categories remain and source table is unchanged; otherwise record the unresolved range or type cause.

- **Grand total plotted:** Narrow range to actual categories.
- **New label wrong:** Check header and category column.
- **Chart unchanged:** Check if new count is text and inspect series.

### Assumptions and limits

This repairs one appended-category omission in an existing chart. You check source rows. Unrefreshed formula summaries, linked external files or complex series need separate work.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26206-CreatingChartsAndGraphs.html) — chart edit mode Data Ranges can correct the source cell area.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
