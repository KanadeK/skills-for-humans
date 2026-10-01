---
name: give-the-first-writer-page-a-distinct-footer
description: "Human-readable first-page footer distinction in a Writer multipage draft using page-style settings while later page footers remain intact."
---
# 让 Writer 首页页脚不同于后续页面 / Give the First Writer Page a Distinct Footer

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有多页非敏感 ODT 副本、首页与后页不同的明确需求 / Non-sensitive multipage ODT copy and clear first-versus-later footer requirement |
| Side effects / 现实副作用 | 封面页脚可空，后续页脚保留 / Cover footer can be blank while later footers remain |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有封面和后续正文，想让首页页脚留空或写不同内容，而正文页脚继续显示页码时使用本篇。成果是首页与第二页页脚明确不同，第三页等后续页保持一致；不能通过在共享页脚里删一个数字来实现，否则会一起删除。这里只处理页脚，正文内容不变。

### 准备与输入

保存 ODT 副本，确认文稿首页和至少两页后续正文采用哪个页样式。记下第二、第三页页脚的原样和页码；若文稿本来用 First Page 与 Default 两种样式，先了解现有切换，避免重复设置。

### 执行

1. 在当前页样式的 Page Style 页脚设置中启用页脚并关闭 Same content on first page，或沿用已存在的首页页样式。
2. 只编辑首页专属页脚为目标内容或空白，不在后续共享页脚删字段。
3. 并排核首页、第二页、第三页，确认第二第三页的页码或文字仍各自正确。
4. 保存重开；若后续页脚意外消失，撤销到副本并检查是否误编辑了共享区。

### 完成、常见问题与恢复

首页页脚按要求不同，第二、第三页仍保留原有后续规则，没有改动正文。

- **后页也空了：** 查是否在共享页脚删了内容。
- **首页仍相同：** 核 Same content on first page 或首页页样式。
- **页码跳号：** 核页面样式的编号重置设置。

### 假设与边界

本篇只处理首页页脚差异，不统一处理奇偶页或整本书的页码方案。你决定封面应显示什么；页面样式变化可能影响同样式的其它页面。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26205-FormattingPagesBasics.html)（英文，官方手册）— 页样式可取消 Same content on first page 以分别设置首页页脚。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a cover's footer must be blank or different but following pages still need their shared footer or page number. Finish with a distinct first footer and consistent second/later footers. Deleting a digit inside a shared footer would affect them all. This handles footer distinction, not prose.

### Preparation and inputs

Save an ODT copy and identify the page style used on cover and at least two following pages. Note existing second/third page footer and numbers. If First Page and Default styles already alternate, inspect that transition before adding another setting.

### Execution

1. In the page style footer settings enable footer and disable Same content on first page, or use an existing First Page style.
2. Edit only the first-page-specific footer to desired content or blank; do not remove fields from later shared footer.
3. Compare first, second and third pages and ensure later page numbers or text remain correct.
4. Save and reopen. If later footer disappears, restore copy and check accidental editing of shared area.

### Success, common problems, and recovery

First-page footer differs as required; second and third pages keep their prior rule, with body text unchanged.

- **Later footers blank too:** Check whether shared footer was edited.
- **First still identical:** Check first-page content toggle or style.
- **Numbers jump:** Check page-style numbering reset.

### Assumptions and limits

This handles first-page footer only, not odd/even pages or a book-wide numbering system. You decide cover content; page-style edits may affect other pages using it.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26205-FormattingPagesBasics.html) — page style can disable Same content on first page for different first-page footer.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.
