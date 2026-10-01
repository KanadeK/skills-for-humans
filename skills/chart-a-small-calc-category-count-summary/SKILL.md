---
name: chart-a-small-calc-category-count-summary
description: "Human-readable chart creation from a two-column category/count summary in Calc, with explicit range, axes and source checks."
---
# 把 Calc 类别次数汇总画成有标签的图 / Chart a Small Calc Category Count Summary

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已核的两列类别与次数汇总、现有 Calc 工作副本 / Checked two-column category/count summary and Calc working copy |
| Side effects / 现实副作用 | 一张类别和数量都标清的可核图 / A chart labels both categories and counts |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有一张**类别和次数**的两列小汇总，想让读者直观看到不同类别的数量时使用本篇。成果是一张有标题、类别轴与次数轴的简洁柱状图，柱高与表中数字一致；它不从原始散乱日志直接猜汇总。图表只是呈现，不能替代检查来源表。

### 准备与输入

保存工作副本，确认第一行分别为类别与次数，下面至少两类，次数是真数值且单位相同。排除总计行、空白和备注列；先记下最大最小类别及数字。选图前决定是否真的需要图；太少的数也可以保留表格。

### 执行

1. 只选两列标题和实际类别行，启动 Insert > Chart 及向导。
2. 选普通二维柱状图，核数据系列按列组织、首行为标签、类别轴对应类别词。
3. 加说明性标题和次数轴名，检查柱高对应源表最大、最小及一项中间值。
4. 把图放在不遮原表的位置，保存重开；若图显示总计或错标签，回数据范围修正。

### 完成、常见问题与恢复

图标题、类别与次数轴清楚，源表实际类别各有一柱且数字相符，原两列未改。

- **总计成了最大柱：** 从图数据范围移除总计行。
- **类别变成系列名：** 检查首行标签和行列方向。
- **图盖住数据：** 移动图对象，不拖动源单元格。

### 假设与边界

只适用于少量类别计数的普通比较。你选择是否使用图表；色彩与三维效果不改善错误数据，且本篇不作统计推断。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26206-CreatingChartsAndGraphs.html)（英文，官方手册）— 图表向导可选图型、数据范围、行列方向和标签。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill with a checked **category/count** two-column summary when you want readers to compare category sizes. Finish with a simple column chart with title, category labels and count axis whose bars agree with the table. Do not ask the chart to infer a summary from messy raw rows. A chart presents data; it does not validate the source.

### Preparation and inputs

Save a working copy. Confirm category and count headers, at least two categories, numeric same-unit counts, and no grand total, blanks or notes in the range. Note largest and smallest values before charting. Decide whether a chart helps; a tiny table may already suffice.

### Execution

1. Select only the two headers and actual category rows, then start Insert > Chart and its wizard.
2. Choose an ordinary 2D column chart; check series in columns, first row as label, and category axis names.
3. Add a descriptive title and count-axis name; compare bar heights with largest, smallest and one middle source value.
4. Place chart away from source cells, save and reopen. If it includes grand total or wrong labels, fix data range.

### Success, common problems, and recovery

Chart title and axes are clear, each source category has one matching bar, and original two columns remain unchanged.

- **Grand total becomes largest bar:** Remove total row from chart range.
- **Categories become series names:** Check header label and series direction.
- **Chart hides data:** Move chart object, not source cells.

### Assumptions and limits

This suits a few ordinary category counts. You choose whether a chart is useful. Color or 3D effects cannot repair wrong data, and no statistical inference is made.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26206-CreatingChartsAndGraphs.html) — Chart Wizard controls type, data range, series direction and labels.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
