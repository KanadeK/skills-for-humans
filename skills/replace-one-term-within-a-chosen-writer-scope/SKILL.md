---
name: replace-one-term-within-a-chosen-writer-scope
description: "Human-readable scoped Find and Replace in Writer with individual match review, preserving occurrences outside the selected passage."
---
# 只在 Writer 指定范围内替换一个词 / Replace One Term Within a Chosen Writer Scope

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 非敏感 ODT 副本、明确旧词新词及要处理的章节 / Non-sensitive ODT copy, exact old/new terms and chosen section |
| Side effects / 现实副作用 | 目标范围统一用词，范围外保留原样 / Target scope uses one term while outside text remains |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你决定在 Writer 某一节内把一个普通术语统一成新词，但全文其他位置仍需保留旧词时使用本篇。成果是所选节里的真实匹配逐项核过并替换，范围外的一个已知样本保持原样。不要因“替换全部”方便就把标题、引文或他人姓名一并改掉。

### 准备与输入

保存 ODT 副本，写下准确旧词、新词及要处理的节起止，先在范围外找一处旧词作保留对照。确认是否区分大小写、词界与变形，避免替换了较长词的组成部分。选区要覆盖目标段落但不跨进下一节。

### 执行

1. 先选定目标节，打开 Find and Replace，启用仅当前选区/范围选项。
2. 逐个查命中，确认语境后替换；不明句子先跳过，不直接全局替换。
3. 检查目标节首末处的新词与未替换项，另到范围外核那处旧词仍在。
4. 保存重开；若范围外也变了，撤销或恢复副本并缩小选区。

### 完成、常见问题与恢复

目标节用词按判断更新，范围外对照保留，原句不因机械替换变错。

- **替换到了标题：** 恢复并缩小选区或逐项跳过。
- **长词里误命中：** 启用整词或逐项核。
- **范围外也变：** 恢复副本，核当前选区选项。

### 假设与边界

只处理一个普通术语的一次限定替换，不决定法律、技术或品牌术语是否等价。你负责语义判断；不同 Writer 版本选区选项可能变。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26202-TextBasics.html)（英文，官方手册）— Find and Replace 可在选区内限定搜索并逐项替换。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one section of a Writer draft should use a new ordinary term but other sections must retain the old one. Finish with matches in the chosen section reviewed and replaced, and a known outside occurrence unchanged. Do not use global Replace All merely because it is convenient; headings, quotations and names may need different treatment.

### Preparation and inputs

Save an ODT copy and write exact old/new terms and section boundaries. Find one outside occurrence as a preservation control. Decide case, whole-word and inflection handling to avoid replacing part of a longer word. Select target paragraphs without crossing into next section.

### Execution

1. Select the target section, open Find and Replace, and enable current-selection-only scope.
2. Review each match in context and replace only valid ones; skip uncertain sentences rather than globally replacing.
3. Check new and remaining terms at section edges and the known outside old-term control.
4. Save and reopen; if outside text changed, undo or restore and narrow scope.

### Success, common problems, and recovery

Chosen section's terminology is updated as judged, outside control remains, and sentences are not broken by mechanical replacement.

- **Heading changed unexpectedly:** Restore and narrow scope or skip.
- **Substring changed:** Use whole-word option or manual review.
- **Outside changed:** Restore and check selection-only option.

### Assumptions and limits

This performs one scoped ordinary term change. It does not decide legal, technical or brand equivalence. You judge meaning; selection controls vary by Writer version.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26202-TextBasics.html) — Find and Replace can limit search to a selection and review replacements.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.
