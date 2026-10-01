---
name: turn-writer-step-lines-into-one-numbered-list
description: "Human-readable conversion of existing step paragraphs into a single Writer numbered list while preserving wording and checking sequence."
---
# 把 Writer 步骤行变成一组真正编号列表 / Turn Writer Step Lines into One Numbered List

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有几段同级步骤文字的非敏感 ODT 副本 / Non-sensitive ODT copy with several same-level step paragraphs |
| Side effects / 现实副作用 | 步骤由真正列表管理顺序而非手打数字 / Steps have managed numbering instead of typed digits |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有几行同级操作步骤，每行前面手打 `1.`、`2.`，想让 Writer 真正管理编号时使用本篇。成果是一组连续列表，插入或删一步时编号会跟着变化，原步骤文字不丢。它只转换一组同级步骤，不推断步骤本身是否合理，也不把其它正文纳入列表。

### 准备与输入

保存 ODT 副本，数清目标步骤行及其前后的普通段落，记录当前首末文字。打开格式标记看每步是否真是单独段落；如果一行只是软换行，先决定是否应拆成段落。保留手打数字原样作对照，但转换时需去掉重复前缀。

### 执行

1. 只选目标步骤段落，应用 Writer 编号列表样式或工具，不带入引言和结束段。
2. 核第一到最后一项编号连续，逐项删除旧手打数字而不删实际步骤文字。
3. 在副本中临时插入一项或移动光标测试连续性，验证是自动编号，再撤销测试。
4. 保存重开，检查首末步骤、总项数与相邻正文没有被套上编号。

### 完成、常见问题与恢复

目标步骤构成一组真正连续编号列表，文字保持，临时增项会自动改号。

- **出现两个数字：** 删除旧手打前缀，保留列表编号。
- **正文也编号：** 撤销并缩小选择范围。
- **中途重新从一开始：** 核是否分成两个列表或有重启设置。

### 假设与边界

只处理同级简单编号列表；多层大纲和法律条款编号需要更严谨方案。你决定步骤顺序，本篇不评估内容正确性。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26212-Lists.html)（英文，官方手册）— Writer 列表工具为多个段落管理编号及连续性。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when several peer instruction paragraphs have manually typed `1.`, `2.` and you want Writer to manage the sequence. Finish with one continuous numbered list that adjusts after inserting or removing a step, with original step words intact. This converts one peer group, not its logic, and leaves other body paragraphs outside.

### Preparation and inputs

Save an ODT copy and count target step paragraphs and adjacent body paragraphs, noting first and last words. Show formatting marks to see whether each step is a real paragraph; a soft line break may need separate correction. Keep typed numbers for comparison but remove their duplicate prefixes during conversion.

### Execution

1. Select only target step paragraphs and apply a Writer numbered-list style/control, excluding intro and closing body.
2. Check numbering runs first to last and remove old typed numeral prefixes without deleting step words.
3. On the copy temporarily add a peer item to see numbers adjust, then undo the test.
4. Save and reopen, checking first/last steps, item count and adjacent body style.

### Success, common problems, and recovery

Target steps form one genuinely continuous numbered list with wording intact, and a temporary item adjusts numbering.

- **Two numbers appear:** Remove typed prefix and keep list number.
- **Body numbered too:** Undo and narrow selection.
- **Restarts midway:** Check split lists or restart option.

### Assumptions and limits

This covers one simple peer-level list. Multilevel outlines and legal clause numbering need stricter design. You decide step order; this does not judge instruction correctness.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26212-Lists.html) — Writer list controls manage numbering and continuity across paragraphs.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.

