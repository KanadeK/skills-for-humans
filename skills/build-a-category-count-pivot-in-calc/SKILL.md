---
name: build-a-category-count-pivot-in-calc
description: "Human-readable pivot summary of a small ordinary Calc log that counts all categories while preserving the original row table."
---
# 用 Calc 透视表汇总日志各类别次数 / Build a Category Count Pivot in Calc

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 已保存逐行日志、清楚的类别列和非空记录编号 / Saved row log, clear category column and nonempty record codes |
| Side effects / 现实副作用 | 各类别次数成一张可核汇总表 / Every category receives a checkable count summary |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已拥有逐行活动日志，想一次看出**所有类别各有几条记录**时使用本篇。成果是一张与原数据分开的透视汇总，类别名和次数能与源记录抽查一致；原表行数、顺序和值保持不变。它比针对单个类别的 COUNTIF 多了全类别分组，不把汇总表当成原始记录。

### 准备与输入

保存 ODS 副本，确认数据首行标题唯一、类别列有值、编号列能代表每条记录。记录原始行数和几个类别的手数结果。选择完整连续的表区，并为透视结果留一块空白区域或新工作表，避免盖住原数据。

### 执行

1. 启动 Data > Pivot Table 的创建流程，核来源范围覆盖标题与所有现有记录列。
2. 把类别放入行字段，把编号放入数据字段，并将聚合设置为计数而非求和。
3. 指定独立输出位置，生成后逐类检查标签及一两类的手数；总计应与有效记录数相符。
4. 保留原表，追加记录后用透视表刷新命令重核；新行未在来源范围时先修范围。

### 完成、常见问题与恢复

汇总列出所有已有类别和各自次数，抽查及总计合理，原表记录未变。缺编号或空类别先标出，不在透视表里默补。

- **显示分钟总和：** 把数据字段改为计数。
- **漏新行：** 核来源范围并刷新。
- **结果盖原表：** 撤销并换独立输出位置。

### 假设与边界

透视表是某时点的汇总视图，不保证新增行自动进入。你负责判定哪些空白或重复编号算有效记录；不同版本拖放界面可能变化。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26210-PivotTables.html)（英文，官方手册）— 透视表按字段分组汇总来源数据，并可刷新结果。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when a row-based activity log needs counts for **every category at once**. Finish with a separate pivot summary whose labels and counts match a source spot check while original rows, order and values remain intact. Unlike one-category COUNTIF, this groups all categories. The summary is not the source log.

### Preparation and inputs

Save an ODS copy. Confirm one header row, category values and a code column representing each record. Note source row count and hand-count a few categories. Select the complete contiguous table and reserve empty space or a new sheet for pivot output so it cannot overwrite source rows.

### Execution

1. Start Data > Pivot Table creation and check the source range covers header and every current record column.
2. Place Category in row fields and Code in data fields, setting aggregation to Count rather than Sum.
3. Choose separate output, then check labels and one or two category hand counts; grand total should match valid records.
4. Keep the source intact. After appending, refresh and recheck; if new rows lie outside source range, correct range first.

### Success, common problems, and recovery

The summary lists all present categories and counts, spot checks and total are plausible, and original records remain unchanged. Flag blank codes or categories instead of silently filling them.

- **Minutes summed instead:** Set data field aggregation to Count.
- **New rows absent:** Check source range and refresh.
- **Output overwrote source:** Undo and choose separate output.

### Assumptions and limits

A pivot is a point-in-time summary and may not include newly added rows automatically. You decide valid blank or repeated codes; drag-and-drop UI varies by version.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26210-PivotTables.html) — pivot tables group and summarize source fields and can refresh their result.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
