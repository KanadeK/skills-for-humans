---
name: update-a-stale-writer-table-of-contents
description: "Human-readable recovery of an existing Writer contents list after headings or pagination change, verifying regenerated entries and page references."
---
# 标题或分页改变后更新 Writer 旧目录 / Update a Stale Writer Table of Contents

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有生成目录的 ODT 副本、已知标题或分页变化 / ODT copy with generated contents and known heading or pagination change |
| Side effects / 现实副作用 | 旧目录反映现有标题与页码 / Existing contents reflects current headings and pages |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已修改一处标题文字、标题层级或正文页数，却发现生成目录仍显示旧条目时使用本篇。成果是**同一份已有目录**刷新到当前标题和页码，新增或删除的条目与正文对应。它修复过期视图，不重新手打目录，也不把错误的正文样式问题藏起来。

### 准备与输入

保存 ODT 副本，记下刚改的标题旧新文字及当前页码，在 Navigator 看新结构是否正确。确认目标对象确为 Writer 生成目录，而不是手工打的段落。若 Navigator 本身已错，先修原文标题样式再更新。

### 执行

1. 在已有目录内右键或用 Tools > Update 的索引/目录更新命令，保持原对象位置。
2. 检查改动标题的文字、层级和页码，再抽查一处未改标题，确认没有整体错位。
3. 若仍是旧值，回 Navigator 核标题是否真被改到正文样式或页面是否重排完成。
4. 确认目录与正文相符后保存重开；不能匹配时记录差异，不把已按更新按钮当成功。

### 完成、常见问题与恢复

已有目录的条目和页码与当前正文抽查一致，位置保留；未匹配的差异被明确列出。

- **点更新仍旧：** 核源标题样式与当前页码。
- **意外少条目：** 核是否把标题改成正文样式。
- **目录被手打覆盖：** 恢复副本中的生成对象再更新。

### 假设与边界

本篇只更新一份已有的生成目录。你负责源标题的正确性；页码可能因字体、打印设置和版本变化再改变，输出前还需复核。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26215-TOCsIndexesBiblios.html)（英文，官方手册）— 生成目录需在标题或页码变化后手动更新。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a heading, its level or pagination has changed but an existing generated table of contents still shows old entries. Finish with **that same contents object** updated to current headings and pages, including additions or removals. This repairs a stale view, not a manually rewritten list or a cover for wrong body styles.

### Preparation and inputs

Save an ODT copy. Note the old/new heading text and current body page, and inspect Navigator for the intended structure. Confirm the target is a Writer-generated contents object, not manually typed paragraphs. If Navigator is wrong, fix source heading styles first.

### Execution

1. Right-click within existing contents or use Tools > Update for indexes/contents, retaining its placement.
2. Check changed entry wording, level and page, then sample one unchanged heading for unexpected shift.
3. If stale remains, check whether source heading style truly changed and pagination has settled.
4. Save and reopen once matching. If mismatch remains, record it rather than treating the update click as success.

### Success, common problems, and recovery

The existing contents entries and sampled pages match the current body without moving the object; any remaining mismatch is named.

- **Still stale:** Inspect source styles and current pages.
- **Entry disappeared:** Check accidental body style.
- **Contents overwritten manually:** Restore generated object from copy, then update.

### Assumptions and limits

This updates one existing generated contents. You own source-heading correctness. Fonts, print settings and version changes may move pages again, so recheck before output.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26215-TOCsIndexesBiblios.html) — a generated contents list must be updated after headings or pagination changes.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.
