---
name: constrain-a-calc-category-column-to-known-choices
description: "Human-readable Calc validity setup for a small category vocabulary, followed by one accepted and one rejected entry check."
---
# 给 Calc 日志类别列设置已知选项 / Constrain a Calc Category Column to Known Choices

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存的普通日志、事先确定的三四个类别词 / Saved ordinary log and three or four agreed category words |
| Side effects / 现实副作用 | 新类别录入受到可测试的规则约束 / New category entries follow a testable rule |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已确定日志只能使用少数几个类别，录入时常因同义词或拼写不同把同类拆散时使用本篇。结果是目标类别格出现可选列表，允许一个已知词并按设定拒绝或提示一个新词；原有记录需另行核对，规则不会自动修好旧值。这里约束新输入，不替你决定分类含义。

### 准备与输入

和使用这张表的人先定三四个互不含糊的普通类别，写在同表旁的安全区域或规则设置里。保存工作副本，只圈定将来要录入类别的数据格，排除第一行标题及其他列。若已有类别词不一致，先保留它们作为待核清单。

### 执行

1. 在选中类别范围打开 Data > Validity，选择列表或单元格范围来源。
2. 填入约定词并设定清楚的错误提示或拒绝方式；确认空白是否允许符合本表规则。
3. 在一格测试一个已知类别，再尝试无关的新词，观察选择、接受或错误反馈。
4. 撤销测试垃圾值，检查标题和其他列未被限制，再保存并重开验证规则仍在。

### 完成、常见问题与恢复

目标列能选到已知词，对未知词有预期反馈，且标题与旁列未被误锁。旧记录的分类质量仍需人工核对。

- **标题也被下拉限制：** 撤销，重选数据行范围。
- **未知词仍直接进入：** 检查错误警示级别与规则适用范围。
- **旧值不一致：** 列待核，不批量默改。

### 假设与边界

只为非敏感、小词表的普通日志设置输入有效性，不能当权限或安全控制。不同版本提示/拒绝方式不同；你必须实际试一个好值与坏值。

### 来源

- [LibreOffice Calc Guide 26.2](https://help.libreoffice.org/latest/en-US/text/scalc/01/12120100.html)（英文，官方手册）— Data > Validity 可按单元格范围或选项列表限制输入。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when a small log has a fixed category vocabulary but new entries use inconsistent synonyms or spellings. Finish with choices available in target cells and an observed accepted known word plus a rejected or warned unknown word. Existing records still need review; a new rule does not repair old values or decide category meaning for you.

### Preparation and inputs

Agree on three or four clear non-sensitive categories with anyone using the sheet and place them in a safe range or list setting. Save a working copy. Select future category data cells, excluding the header and other columns. Keep inconsistent existing words as a review list.

### Execution

1. For the selected category cells open Data > Validity and choose a list or cell-range source.
2. Enter agreed words and set a clear error warning or rejection; decide whether blank is allowed.
3. Test one known category, then an unrelated word, observing choice and acceptance or warning.
4. Remove test values, confirm header and other columns remain unrestricted, then save and reopen to verify the rule.

### Success, common problems, and recovery

Target cells offer known words and respond as planned to an unknown word, while header and neighbour columns remain untouched. Old categories still require human review.

- **Header constrained too:** Undo and select data rows only.
- **Unknown word still enters:** Check error-action level and selected range.
- **Existing values differ:** List them for review rather than silently replacing.

### Assumptions and limits

This is input validity for a small non-sensitive vocabulary, not access or security control. Warning/rejection behavior varies by version; test one good and one bad value.

### Sources

- [LibreOffice Calc Guide 26.2](https://help.libreoffice.org/latest/en-US/text/scalc/01/12120100.html) — Data > Validity can restrict input to a cell range or listed choices.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
