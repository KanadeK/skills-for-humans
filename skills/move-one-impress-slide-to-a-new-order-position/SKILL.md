---
name: move-one-impress-slide-to-a-new-order-position
description: "Human-readable reordering of one Impress slide in Slide Sorter with preserved slide count, content and neighboring sequence checks."
---
# 在 Impress 浏览视图移动一张页的顺序 / Move One Impress Slide to a New Order Position

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有至少三页的非敏感 ODP 副本、目标页与新邻居 / Non-sensitive ODP copy with at least three slides, target and new neighbours |
| Side effects / 现实副作用 | 一张页换位，页数和内容不变 / One slide moves while count and content stay |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你发现一张 Impress 页的论证顺序不合适，想把它移动到更合理的位置时使用本篇。成果是目标页换位后前后邻居符合预期，整稿张数及对象内容不变。它不是复制一页，也不靠改页标题伪装顺序已变；要判断新顺序是否有利于理解，仍须实际走读。

### 准备与输入

保存 ODP 副本，列出目标页标题、原邻居和新邻居，记下总张数。打开 Slide Sorter，确认没有多选，避免拖动一整组。若演示稿有自动跳转或自定义放映，先记录它们，位置移动可能影响路径。

### 执行

1. 在 Slide Sorter 找到目标缩略图，核标题与内容避免拖错。
2. 拖到预定新邻居之间，观察插入线后松开，不按复制修饰键。
3. 对照目标的前后页、总张数和旧位置，确认没有留下副本或误删。
4. 从新位置前一页放映两三张确认衔接；不合理就撤销，保存重开再核排序。

### 完成、常见问题与恢复

目标页只存在一次，处于指定位置，张数与内容未变；衔接经短走读。

- **变成两张：** 撤销复制，重新用移动。
- **拖错页：** 按标题和内容从副本重定位。
- **自定义放映跳转坏：** 核自定义列表与链接目标。

### 假设与边界

只移动一张普通页。你负责语义顺序；交互式跳转和自定义放映需额外测试，不由静态缩略图保证。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26209-SlideShowsPhotoAlbums.html)（英文，官方手册）— Slide Sorter 可查看并调整放映页序。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one Impress slide belongs at a different point in the argument. Finish with its predecessor and successor matching the intended order while slide count and objects remain unchanged. This is movement, not duplication or retitling. You still need to walk through whether the new sequence makes sense.

### Preparation and inputs

Save an ODP copy and note target title, old and intended neighbours and total count. Open Slide Sorter and confirm only one slide selected. Record custom shows or jumps if present, since moving a slide may affect navigation.

### Execution

1. Locate target thumbnail in Slide Sorter and verify title/content before moving.
2. Drag between intended new neighbours and release at insertion line without a copy modifier.
3. Check target's new neighbours, total count and old position for a duplicate or missing slide.
4. Preview a few slides starting before new position; undo if flow is worse, then save and reopen.

### Success, common problems, and recovery

Target exists once at intended position, count and content stay, and a short sequence walkthrough supports the move.

- **Two copies appear:** Undo copy and move without modifier.
- **Wrong slide moved:** Locate by title/content and restore.
- **Custom show breaks:** Check its list and links.

### Assumptions and limits

This moves one ordinary slide. You judge narrative order; interactive jumps and custom shows need extra testing beyond thumbnails.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26209-SlideShowsPhotoAlbums.html) — Slide Sorter shows and permits rearranging the show sequence.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.

