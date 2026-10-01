---
name: correct-one-mistyped-calc-cell-without-shifting-records
description: "Human-readable recovery for one known mistaken Calc entry, correcting its cell while keeping neighbouring fields and records aligned."
---
# 在 Calc 修正一个错录单元格并保住整行 / Correct One Mistyped Calc Cell Without Shifting Records

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–10 分钟 / 5–10 minutes |
| Requirements / 必要物品 | 已保存的普通 Calc 日志、可信原值和错误格位置 / Saved ordinary Calc log, trusted source value and wrong cell location |
| Side effects / 现实副作用 | 错值被修正，邻格仍原样 / Wrong value corrected while neighbours remain aligned |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已经确定日志里一个具体单元格录错，而其余行列应保留时使用本篇。成果是该格变成可信原值，并有相邻字段前后核对；不为了一个错字删整行或重排表格。原值不可靠时先标记待查，不编造更正。

### 准备与输入

保存工作副本，记下工作表名、列标题和行号，查看左右邻格与上下行的值。准备可核的原始记录或本人刚做的活动笔记。先确认目标不是公式输出；公式错了应另找引用或公式原因。

### 执行

1. 只选中错误格，核名称框地址和列标题，再用输入栏或单元格编辑原内容。
2. 键入可信原值并确认，不用会移动单元格的删除或插入命令。
3. 马上检查本行编号、日期、类别、分钟、备注及相邻两行仍与更正前对齐。
4. 若改错格就撤销并重定位；正确时保存、重开，再看目标格及邻格。

### 完成、常见问题与恢复

目标格与可信来源一致，周围字段没有位移，保存重开仍如此；来源无法确认则保留待查标记。

- **整行错位：** 立即撤销，查是否误用删除单元格。
- **改到别行：** 根据行号、编号与源记录重定位。
- **原值不确定：** 停止替换，备注待核，不猜。

### 假设与边界

只适用于一处已知字面录入错误。你负责核实原值；公式错误、批量清洗或被他人同时修改的共享工作簿不在本篇。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html)（英文，官方手册）— Calc 支持单元格和输入栏编辑、撤销及区域选择。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill after identifying one specific mistyped cell while other fields must stay. Finish with that cell matching a trusted source and neighbouring data checked before and after. Do not delete or reorder a whole row for one typo. If source is uncertain, mark it for review.

### Preparation and inputs

Save a working copy. Note sheet name, column heading and row number, plus neighbour values. Have a trusted original note or just-recorded event. Confirm target is not a formula result; a wrong formula needs separate reference work.

### Execution

1. Select only wrong cell, check address and header, then edit it in input line or cell.
2. Enter trusted source value without a delete or insert command that shifts cells.
3. Check this row's code, date, category, minutes, note and adjacent rows against pre-edit alignment.
4. Undo and relocate if wrong cell changed; otherwise save, reopen and inspect target and neighbours.

### Success, common problems, and recovery

The target matches a trusted source, surrounding fields have not shifted, and result persists after reopening; otherwise keep a review marker.

- **Row shifted:** Undo and check accidental delete-cell action.
- **Wrong row edited:** Use row number, code and source to relocate.
- **Source uncertain:** Stop replacement and mark for checking.

### Assumptions and limits

This covers one known literal entry error. You verify the source; formula bugs, bulk cleaning and concurrently edited shared workbooks are outside scope.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html) — Calc supports cell and input-line editing, undo and range selection.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
