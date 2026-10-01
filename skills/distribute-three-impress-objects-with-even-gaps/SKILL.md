---
name: distribute-three-impress-objects-with-even-gaps
description: "Human-readable Impress distribution of at least three objects by horizontal or vertical spacing, preserving order and edge boundaries."
---
# 让 Impress 三个对象之间留出均匀间隔 / Distribute Three Impress Objects with Even Gaps

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 同页至少三个相关对象、可用空白和 ODP 副本 / At least three related same-slide objects, spare space and ODP copy |
| Side effects / 现实副作用 | 对象间距更均匀且仍各自可读 / Gaps become even while objects remain readable |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一页三个以上已经排好顺序的对象，但中间空隙一大一小，想让间隔更均匀时使用本篇。成果是对象按原顺序占据原范围，间距接近一致，文本与图片无重叠。这不同于对齐共同边：对齐可以成立而间距仍混乱。

### 准备与输入

保存 ODP 副本，确定要按水平还是垂直方向分布，标明最左/最右或最上/最下两个边界对象。先确认所有对象宽高与可用空间，若空间本身放不下，分布命令不能创造空间，应先删减或缩小内容。

### 执行

1. 只选目标的三项以上对象，检查外侧边界和中间顺序。
2. 使用 Distribute Selection 中的水平或垂直 Spacing 项，而非误选 Align Objects。
3. 比较相邻空隙、外侧位置、文字可读性和对象是否仍在画布内。
4. 若顺序或文字受损立即撤销，重新确认对象尺寸；正确时保存重开预览。

### 完成、常见问题与恢复

至少三对象沿指定方向的空隙近似均匀，原顺序保留、无覆盖。

- **命令不可用：** 核是否确实选了至少三项。
- **对象重叠：** 空间不足，撤销后先缩减。
- **水平变垂直：** 撤销并选正确方向。

### 假设与边界

只调整一组三个以上对象的间距，不替代信息取舍。你负责是否真的需要等距；不同尺寸的对象视觉上可能仍需微调。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26205-ManagingGraphicObjects.html)（英文，官方手册）— Distribute Selection 需至少三对象并可选水平或垂直间距。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when at least three ordered slide objects have visibly uneven gaps. Finish with their original order and outer span retained, more even spacing and no overlap. This differs from sharing an alignment edge: objects can align correctly while their gaps remain poor.

### Preparation and inputs

Save an ODP copy, choose horizontal or vertical distribution, and identify outer boundary objects. Check object sizes and available space. If they cannot physically fit, distribution cannot create room; reduce content or objects first.

### Execution

1. Select only the three or more intended objects, checking outer boundaries and internal order.
2. Use horizontal or vertical Spacing in Distribute Selection, not Align Objects.
3. Compare adjacent gaps, outer positions, readability and on-canvas placement.
4. Undo for changed order or damaged text and recheck sizes; otherwise save/reopen and preview.

### Success, common problems, and recovery

At least three objects have roughly even gaps on chosen axis with original order and no collision.

- **Command inactive:** Check at least three selected.
- **Objects overlap:** Insufficient space; undo and reduce first.
- **Wrong axis:** Undo and choose correct direction.

### Assumptions and limits

This adjusts spacing for one group of three or more objects, not content selection. You decide whether equal gaps help; varying object sizes may still need visual refinement.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26205-ManagingGraphicObjects.html) — Distribute Selection needs at least three objects and offers horizontal or vertical spacing.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.

