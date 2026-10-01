---
name: create-a-writer-table-of-contents-from-headings
description: "Human-readable creation of a Writer table of contents from existing semantic headings with entry and page checks."
---
# 由 Writer 真标题生成一份目录 / Create a Writer Table of Contents from Headings

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 有真正 Heading 样式的多页 ODT 副本、清楚的目录插入位置 / Multipage ODT copy with real Heading styles and chosen contents location |
| Side effects / 现实副作用 | 出现可核对标题与页码的生成目录 / A generated contents list shows checkable headings and pages |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有真正的 Writer 标题层级，想在多页文稿前部生成目录时使用本篇。成果是目录条目来自那些标题、层级与页码能和正文对上；不手打一个容易过期的目录。它创建初次目录，不处理后来文字变化造成的过期页码。

### 准备与输入

保存 ODT 副本，先在 Navigator 核预期标题及顺序，选一个不会割断正文的目录插入段落。估计目录要收录到第几级，确保文稿里没有空标题或误用 Heading 样式的正文。记录两个远处标题的当前页码供核对。

### 执行

1. 将光标放在预定位置，用 Insert > Table of Contents and Index 的目录命令。
2. 选择 Table of Contents 类型与需要的标题级数，让条目取自大纲标题，不手输清单。
3. 生成后对照 Navigator 检目录顺序与层级，点击或查两个条目的页码是否匹配正文。
4. 若多出正文或漏标题，先修其段落样式再重建或更新目录；保存重开核查。

### 完成、常见问题与恢复

目录位置、条目、级数与抽查页码都符合正文，原文字未改。

- **目录为空：** 先核是否真用了 Heading 样式。
- **正文进目录：** 纠正该段错误的标题样式。
- **页码不对：** 检查目录创建后的分页并更新。

### 假设与边界

目录依赖标题样式和当前分页，不证明内容完整。你决定收录层级；不同版本的插入对话框名称可能变化。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26215-TOCsIndexesBiblios.html)（英文，官方手册）— 目录依据标题大纲级别与段落内容生成。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a multipage Writer draft already has real heading levels and needs a contents list near the front. Finish with entries derived from those headings whose levels and page references match the body, rather than a manually typed list that quickly stales. This creates the first table; later stale entries are a separate recovery task.

### Preparation and inputs

Save an ODT copy and check expected heading order in Navigator. Choose a contents insertion paragraph that does not split body text. Decide how many levels to include and check for empty headings or body paragraphs styled as headings. Note page numbers of two distant headings for verification.

### Execution

1. Place cursor at intended location and use Insert > Table of Contents and Index.
2. Choose Table of Contents type and desired heading levels, sourcing entries from outline headings.
3. Compare resulting entry order and levels with Navigator, then check two page references against body.
4. If body appears or a heading is missing, correct paragraph styles then rebuild or update; save and reopen to inspect.

### Success, common problems, and recovery

Contents location, entries, levels and sampled page numbers match the body, with original prose intact.

- **Contents empty:** Check for real Heading styles.
- **Body in contents:** Correct its mistaken heading style.
- **Page reference wrong:** Inspect pagination after insertion and update.

### Assumptions and limits

A table of contents depends on heading styles and current pagination and does not prove substantive completeness. You choose depth; dialog labels may vary by version.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26215-TOCsIndexesBiblios.html) — table of contents entries come from heading outline levels and paragraph contents.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.
