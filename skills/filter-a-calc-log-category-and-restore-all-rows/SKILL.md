---
name: filter-a-calc-log-category-and-restore-all-rows
description: "Human-readable temporary Calc AutoFilter of one category with visible subset checks and an explicit reset to show every record again."
---
# 筛出 Calc 日志一个类别后恢复全表 / Filter One Calc Log Category and Restore All Rows

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 有标题和多个类别的普通 Calc 日志、已保存副本 / Ordinary Calc log with headers and multiple categories, saved copy |
| Side effects / 现实副作用 | 一个类别暂时可见，随后全部记录重新出现 / One category is temporarily visible, then all records return |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你只想临时看日志中的一个类别，又要在结束时恢复所有记录时使用本篇。成果是筛选时可见行都属于目标类别，复位后原有各类别重新出现、记录总数不减少。筛选是视图条件，不是删除；别把隐藏行误报为丢失数据。

### 准备与输入

保存副本，记下未筛选时的记录总数与至少两个不同类别的编号。确认第一行为标题，没有无关表格紧挨着目标范围。选择目标表的连续区域，避免筛选按钮装到别的标题行。

### 执行

1. 对目标表开启 Data > AutoFilter，并找到类别列的下拉入口。
2. 只选目标类别，观察可见行的类别和编号，并注意行号可能跳跃表示隐藏。
3. 记录一次可见行数或列表，避免把它当原表总量。
4. 在类别下拉恢复全部或用重置筛选，逐项核原记录总数与另一类别的编号重新出现。

### 完成、常见问题与恢复

目标类别的临时子集正确，复位后原本全部记录可见，数据内容未变。

- **看不到其他行：** 先检查筛选是否仍启用，别立刻新增或删行。
- **目标类别没全出现：** 核拼写差异与空值，不自动合并词义。
- **筛错表：** 撤销或重置，重新圈定范围。

### 假设与边界

只对小型非敏感日志做单条件临时筛选。你负责在结束时恢复全表；筛选后的可见数不应当作未筛选统计。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html)（英文，官方手册）— 自动筛选隐藏不匹配行并可重置显示。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when you want to view one category temporarily and then restore the whole log. Finish with only the target category visible under the filter, and all original categories and record count visible after reset. Filtering changes visibility, not deletion; do not report hidden rows as lost.

### Preparation and inputs

Save a copy and note total unfiltered record count and codes from two different categories. Confirm row one is the header and no unrelated table adjoins the target. Select its contiguous range so filter controls attach to the intended headers.

### Execution

1. Enable Data > AutoFilter for the target table and locate the category dropdown.
2. Select only the target category, inspect visible categories and codes, and notice skipped row numbers as hidden rows.
3. Record the temporary visible count or list without calling it the full-table total.
4. Show all or reset the filter, then confirm the original total and another category's code return.

### Success, common problems, and recovery

The temporary subset matches the target category and all original records are visible after reset, with data unchanged.

- **Other rows missing:** Check active filter before inserting or deleting rows.
- **Target appears incomplete:** Check spelling and blanks without silently merging categories.
- **Wrong table filtered:** Reset and select the intended range.

### Assumptions and limits

This is a one-condition temporary filter on a small non-sensitive log. You restore full visibility; a filtered visible count is not the unfiltered total.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html) — AutoFilter hides nonmatching rows and can be reset to full visibility.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
