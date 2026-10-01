---
name: review-duplicate-calc-log-codes-without-deleting
description: "Human-readable review of suspected duplicate record codes with Calc Data Duplicates Select action, preserving every row for a later decision."
---
# 在 Calc 找出重复编号但先不删记录 / Review Duplicate Calc Log Codes Without Deleting

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 带唯一性预期编号的普通日志副本、原始记录 / Ordinary log copy with expected unique codes and original records |
| Side effects / 现实副作用 | 重复编号成为待核行清单，记录仍完整 / Repeated codes become a review list while rows remain |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你怀疑普通日志的事件编号有重复，但还不知道它们是误录还是两次真实活动时使用本篇。结果是一份需要人工对照原始记录的重复编号候选清单，行数和内容保持不变。绝不把“编号重复”直接等同于“多余记录”，也不在此篇执行 Remove。

### 准备与输入

保存工作副本并记录原总行数。确认编号列应唯一且前导零已按文本保留。选连续完整表区，包含标题和所有相关记录列；如果有空编号，先区分缺值和真正重复编号。准备原始活动笔记供后续核实。

### 执行

1. 在完整表区打开 Data > Duplicates，设按行比较并标记首行为标题。
2. 只把编号列选作比较依据，动作明确选择 Select 而非 Remove。
3. 执行后记下被选行的编号、日期和行号，逐对回原始记录判断是重号还是合法两次。
4. 不在本篇删行；核总行数与原来相同，保存待核清单或撤销临时选择。

### 完成、常见问题与恢复

有具体重复编号候选与待核原因，表内记录数未减少；若操作误选 Remove，立即撤销并恢复副本。

- **没有选出预期重号：** 检查前导零、空格和比较列。
- **选出不同活动：** 保留两行，另议编号修正。
- **误删行：** 撤销并与原总行数核对。

### 假设与边界

只找候选，不裁决是否删除。你需凭原始记录判断；如果本机版本没有 Select 动作，停在手工或其它只读核查方法，不改用删除。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html)（英文，官方手册）— Data > Duplicates 可按指定列比较并选择而非删除重复记录。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when event codes may repeat but you do not yet know whether they are mistakes or two real events. Finish with suspect codes and row locations for source review while preserving every row. A repeated code is not automatically a disposable record, and this Skill never uses Remove.

### Preparation and inputs

Save a working copy and note total row count. Confirm codes should be unique and leading zeros are preserved as text. Select the complete contiguous table with header and all record columns. Separate blank codes from actual repeated codes, and have original notes for later review.

### Execution

1. Open Data > Duplicates for the full table, compare by rows and mark the first row as a header.
2. Choose only the code column as comparison key and explicitly choose Select, not Remove.
3. Record selected rows' codes, dates and row numbers; compare pairs with original notes to judge duplicate code versus two real events.
4. Delete no rows here; confirm total row count stayed the same and save a review list or clear the temporary selection.

### Success, common problems, and recovery

You have specific suspect codes and review reasons, with no reduction in record count. If Remove was accidentally chosen, undo immediately and restore the copy.

- **Expected pair not selected:** Check leading zeros, spaces and comparison key.
- **Different real events selected:** Keep both rows and review code correction.
- **Rows removed:** Undo and compare original row count.

### Assumptions and limits

This finds candidates but does not decide deletion. You need source records. If your version lacks a Select action, stop and use a read-only alternative rather than Remove.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html) — Data > Duplicates can compare selected columns and Select rather than Remove duplicate records.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
