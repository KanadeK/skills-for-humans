---
name: number-impress-content-slides-without-numbering-the-cover
description: "Human-readable Impress slide-number field setup for content slides with a deliberately unnumbered first slide and show-preview checks."
---
# 给 Impress 内容页显示编号但封面不显示 / Number Impress Content Slides Without Numbering the Cover

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有封面和内容页的非敏感 ODP 副本、明确是否显示编号 / Non-sensitive ODP copy with cover/content slides and numbering decision |
| Side effects / 现实副作用 | 内容页有动态编号，封面不显示 / Content slides show dynamic numbers while cover does not |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一份多页 Impress 演示稿，希望内容页能被准确指称，而标题封面不显示数字时使用本篇。成果是内容页的编号随页位变化，封面没有编号，插页后编号仍可核；不在每页手打数字。若演示稿有隐藏页或自定义放映，编号和实际放映次序需另外核对。

### 准备与输入

保存 ODP 副本，记下封面及两张内容页的标题、总张数。检查母版是否有 Slide number 占位区，否则对话框勾选可能不显示。决定编号的位置是否遮住重要文字；如已有手打数字，记录并准备移除。

### 执行

1. 用 Insert > Header and Footer 的 Slide 选项启用 Slide number，并选择首张不显示。
2. 按目标范围 Apply to All，检查封面、第二页和末页的显示与实际页位。
3. 临时插入一页或看已有插页，确认数字由字段更新，不是手写残留，随后撤销测试。
4. 保存重开并在放映预览检查位置与可读；异常时核母版占位和手打数字。

### 完成、常见问题与恢复

封面无编号，内容页数字与页位相符，新增页能使后续编号变化，文字未被遮。

- **全都不显示：** 检查母版 Slide number 占位。
- **封面也显示：** 核首张不显示的设置。
- **数字重叠：** 删除手打旧值或调整占位。

### 假设与边界

这只是页码字段，不保证自定义放映的播放序号相同。你负责讲述引用口径；不同模板母版可能设置不同。

### 来源

- [LibreOffice Impress Help](https://help.libreoffice.org/latest/en-US/text/simpress/01/03152000.html)（英文，官方帮助）— Header and Footer 可启用 Slide number 并选择 Do not show on first slide。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a multipage Impress deck needs referenceable content slides but no number on its title cover. Finish with changing slide-number fields on content slides, no number on cover and plausible values after insertion. Do not type a digit on every page. Hidden slides or custom shows need a separate check against show order.

### Preparation and inputs

Save an ODP copy and note cover, two content titles and total count. Check master for a Slide number field area; dialog settings may not display without one. Ensure placement does not cover content. Record old typed numbers before removing them.

### Execution

1. Open Insert > Header and Footer Slide tab, enable Slide number and choose not to show on first slide.
2. Apply to intended slides and inspect cover, second and last slide numbers against their positions.
3. Temporarily insert a slide or use a known insertion to confirm field values update, then undo test.
4. Save, reopen and preview position/readability; inspect master number area and typed digits for issues.

### Success, common problems, and recovery

Cover is unnumbered, content values match positions, insertion updates later numbers and no text is obscured.

- **None visible:** Check master Slide number field area.
- **Cover numbered:** Check first-slide exclusion.
- **Numbers overlap:** Remove typed old values or adjust number area.

### Assumptions and limits

These are slide-number fields, not guaranteed custom-show sequence numbers. You own verbal reference convention; masters may differ.

### Sources

- [LibreOffice Impress Help](https://help.libreoffice.org/latest/en-US/text/simpress/01/03152000.html) — Header and Footer can enable Slide number with Do not show on first slide.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.
