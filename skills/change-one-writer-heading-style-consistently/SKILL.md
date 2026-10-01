---
name: change-one-writer-heading-style-consistently
description: "Human-readable edit of one existing Writer heading paragraph style so matching headings update together without touching body text."
---
# 一次修改 Writer 同级标题的共同样式 / Change One Writer Heading Style Consistently

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有真正 Heading 样式的非敏感 ODT 副本、需调整的一个可读属性 / Non-sensitive ODT copy with real Heading style and one readability property to change |
| Side effects / 现实副作用 | 同级标题同时变化而正文保持原样 / Same-level headings change together while body stays |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你发现同一级标题整体太挤或太小，想通过共同样式改一次而非逐段点改时使用本篇。成果是该级所有标题一致变化，其他级别和正文没有意外变化。优先选一项清楚的可读性属性，如段前间距，不同时重做颜色、字体和层级。

### 准备与输入

保存 ODT 副本，数出该级标题并记下修改前的一处和末尾一处外观。确认它们真的都用了同一段落样式，若有例外先记录。打开 Styles 面板的该样式编辑入口，不在某个单独标题上直接格式化。

### 执行

1. 只改一项属性，例如段前间距或字号，并记下原值以便恢复。
2. 应用后检查第一处与末尾一处同级标题是否同时变化，正文是否未变。
3. 巡视有例外的标题；若某标题没变，先核它是否另用样式或有直接格式覆盖。
4. 不满意就恢复原样式属性；满意时保存重开再核两处样本。

### 完成、常见问题与恢复

同级标题的选定属性一致，其他层级与正文无意外变化，旧值可追溯。

- **只有一处变化：** 查是否误做了直接格式。
- **正文也变化：** 核是否改错成正文样式，恢复原值。
- **少数标题没变：** 查样式不一或局部覆盖。

### 假设与边界

只调整一个现有标题样式的一个属性，不重建整套模板。你负责可读性判断；样式级全局变化会影响采用它的每一段，先在副本操作。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26209-WorkingWithStyles.html)（英文，官方手册）— 修改段落样式会影响采用该样式的各段。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one heading level is consistently cramped or too small and you want one shared style change instead of many direct edits. Finish with all headings using that style changed consistently, while other heading levels and body remain as before. Choose one clear readability property, such as space before, rather than redesigning font, color and hierarchy together.

### Preparation and inputs

Save an ODT copy, count headings at the target level and note appearance of an early and late example. Confirm they actually share one paragraph style; note exceptions first. Open that style's edit command rather than direct-formatting an individual heading.

### Execution

1. Change one property, such as space-before or font size, and note the previous value for recovery.
2. Check an early and late same-level heading both changed and body text did not.
3. Inspect exceptions. If one did not change, check its style or direct-format override before making another global edit.
4. Restore old style property if worse; otherwise save and reopen two sample headings.

### Success, common problems, and recovery

The chosen property is consistent across that heading level, other levels and body are unaffected, and the old value is known.

- **Only one changed:** Check accidental direct formatting.
- **Body changed too:** Check wrong style and restore old value.
- **A few unchanged:** Inspect style mismatch or local override.

### Assumptions and limits

This changes one property of one existing heading style, not an entire template. You judge readability. A style edit affects every paragraph using it, so work on a copy.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26209-WorkingWithStyles.html) — editing a paragraph style affects each paragraph using it.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.
