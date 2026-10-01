---
name: restart-one-writer-numbered-list-intentionally
description: "Human-readable recovery when a distinct Writer numbered sequence continues an earlier list, restarting only the new sequence and checking both."
---
# 让 Writer 新编号列表从一重新开始 / Restart One Writer Numbered List Intentionally

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–10 分钟 / 5–10 minutes |
| Requirements / 必要物品 | 已有两组不同步骤的非敏感 ODT 副本、清楚的新列表起点 / Non-sensitive ODT copy with two distinct step groups and known new start |
| Side effects / 现实副作用 | 第二组从一开始而第一组编号不变 / Second group starts at one while first stays |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有两组真正的 Writer 编号列表，第二组本应从 1 开始却延续了前一组编号时使用本篇。成果是第二组从 1 连续到末项、第一组原编号不变，原步骤文字不丢。它从已有续号错误恢复，不是把普通文字第一次建成列表。

### 准备与输入

保存 ODT 副本，记下第一组末项数字与第二组首末文字，确认中间确有新标题或正文区分两组。把光标放在第二组的第一项，不能选中第一组。若第二组其实应承接上一组，先别重启。

### 执行

1. 在第二组首项右键或打开列表设置，选择 Restart Numbering。
2. 检查第二组首项为 1、后续递增，并核第一组的首末数字未改。
3. 在第二组中间临时插一项验证自动编号，再撤销测试，不用手打数字修表面。
4. 若第一组也变，撤销并确认光标及列表边界；正确时保存重开两组抽查。

### 完成、常见问题与恢复

两组各有正确连续编号，第二组确从 1 开始，前组与文字保留。

- **前组编号也变：** 撤销，重选第二组首项。
- **第二项又跳号：** 核第二组是否分裂成多个列表。
- **出现手打数字：** 去掉重复前缀，保留自动编号。

### 假设与边界

只处理一个有明确语义边界的新序列；多级法律/技术编号不在本篇。你负责判断两组是否真的独立。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26212-Lists.html)（英文，官方手册）— Writer 可在指定段落使用 Restart Numbering，而不重建前一列表。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when two real Writer numbered lists are separate tasks but the second continues the first one's numbering instead of starting at 1. Finish with the second group running from 1 to its last item, the first group unchanged, and step wording intact. This fixes a continuation error, not first-time list creation.

### Preparation and inputs

Save an ODT copy. Note the first group's last number and second group's first/last wording, with a real heading or body boundary between them. Place cursor in the first item of the second group, not the first group. If the sequence actually continues, do not restart.

### Execution

1. At the second group's first item use the context List command or paragraph list setting for Restart Numbering.
2. Check second starts at 1 and rises, while first group's beginning and end numbers remain.
3. Temporarily insert an item inside second group to see managed numbering, then undo; do not hand-type a cosmetic fix.
4. If first group changes, undo and check cursor and list boundary. Save and reopen to spot-check both.

### Success, common problems, and recovery

Both groups retain correct internal numbering, second begins at 1, and first group and wording remain intact.

- **First group changes:** Undo and select second group's first item.
- **Next item jumps:** Inspect split lists.
- **Typed numeral remains:** Remove duplicate prefix, keep managed number.

### Assumptions and limits

This handles one semantically separate new sequence. Multilevel legal or technical numbering is outside scope. You decide whether groups truly differ.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26212-Lists.html) — Writer can Restart Numbering at a chosen paragraph without rebuilding the earlier list.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.

