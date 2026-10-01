---
name: add-one-impress-slide-after-a-chosen-slide
description: "Human-readable insertion of one new Impress slide immediately after a chosen existing slide, with count and neighboring order checks."
---
# 在 Impress 指定页后新增一张内容页 / Add One Impress Slide After a Chosen Slide

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有非敏感 ODP 副本、要插入的准确前后页 / Non-sensitive ODP copy and precise insertion neighbours |
| Side effects / 现实副作用 | 新页出现在预定位置且原序保留 / New slide appears at intended position with old order intact |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有一份顺序明确的 Impress 演示稿，发现某个论点之后需要独立的一张新页时使用本篇。成果是新增页恰好位于预定两页之间，原有页未被覆盖或误删，总张数只多一。它处理插入位置，不决定新页的全部内容或母版设计。

### 准备与输入

保存 ODP 副本，记下前一页和后一页标题、原总张数。选一个足够具体的新页目的，避免只是复制旧页的同义句。若要加在末尾，确认不是误选封面或空白区域；本机默认新页可能继承选中页的母版。

### 执行

1. 在幻灯片窗格选中预定前一页，用 Slide > New Slide 或等价命令。
2. 检查新页被插在其后、预定后一页仍在，选择适合该页的现有布局。
3. 填入最少足以识别本页目的的标题，避免留下无法区分的空白页。
4. 在 Slide Sorter 核前新后三页与总数，保存重开；位置不对就撤销后重选前页。

### 完成、常见问题与恢复

新页只多一张、位置与目的清楚，原相邻页保持顺序。

- **加到最后：** 撤销并选准前一页。
- **新页像封面：** 核继承母版和布局。
- **后一页不见：** 核是否误覆盖或隐藏，恢复副本。

### 假设与边界

只插入一张普通内容页。你负责新页事实与版面，未做真人放映验收；不同版本插入命令可能变。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26208-AddingFormattingSlidesNotesdCommentsHandouts.html)（英文，官方手册）— 新幻灯片插在当前选中页之后。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an ordered Impress deck needs one independent new slide after a particular point. Finish with the new slide exactly between intended neighbours, original slides not overwritten or deleted, and total count up by one. This handles insertion position, not the slide's full content or master design.

### Preparation and inputs

Save an ODP copy, noting before/after slide titles and old count. Give the new slide one specific purpose rather than duplicating a synonym. For end insertion, confirm selection, since a new slide may inherit the selected slide's master.

### Execution

1. Select intended predecessor in Slides pane and use Slide > New Slide or equivalent.
2. Check new slide follows it and intended successor remains; choose a suitable existing layout.
3. Enter a minimal identifying title so the slide is not an untraceable blank.
4. Check predecessor/new/successor and total in Slide Sorter, save and reopen; undo wrong placement.

### Success, common problems, and recovery

Exactly one slide is added at intended position with clear purpose, and old neighbours retain their order.

- **Inserted at end:** Undo and select intended predecessor.
- **New page looks like cover:** Inspect inherited master and layout.
- **Successor missing:** Check overwrite or hide, restore copy.

### Assumptions and limits

This inserts one ordinary content slide. You own facts and layout, with no live show acceptance; insertion controls may vary by version.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26208-AddingFormattingSlidesNotesdCommentsHandouts.html) — New Slide is inserted after the selected slide.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.

