---
name: group-related-impress-objects-for-one-move
description: "Human-readable grouping of related Impress shapes for one joint move, followed by an ungroup check that preserves component identity."
---
# 把 Impress 相关对象成组移动再拆开 / Group Related Impress Objects for One Move

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 同页两个以上应一起移动的对象、ODP 工作副本 / Two or more related same-slide objects and ODP working copy |
| Side effects / 现实副作用 | 相关对象一起移动，之后仍可分开编辑 / Related objects move together and remain independently editable after ungroup |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一组图形和说明标签要整体挪位，单独拖动总让相对位置乱掉时使用本篇。成果是它们作为组一起移动到安全位置，随后测试拆组仍能选到每个原对象。分组只方便共同操作，不表示图形与说明内容已被合并成不可逆新图。

### 准备与输入

保存 ODP 副本，列出要纳入组的对象与不应纳入的背景/标题，记下相对位置。检查目的地有足够空间，不遮正文。选择组而非 Combine，因为 Combine 可能改变对象属性。

### 执行

1. 多选有关对象，核选择框没有包含不相关标题或背景。
2. 执行 Group，在组外缘拖动一小段，检查组件同步、内部相对位置不变。
3. 到目标位置后检查不压住其它内容，再试 Ungroup 选回每个组件；如仍需成组可重新 Group。
4. 保存重开，核组/拆组的最终状态与图片、标签完整性。

### 完成、常见问题与恢复

相关对象整体移动且可拆回各组件，未选对象没有移动或被覆盖。

- **标题也跟着动：** 撤销并缩小选择范围。
- **拆不开：** 检查是否误用了 Combine。
- **目的地遮字：** 撤销移动，找安全空位。

### 假设与边界

只做一组可逆对象操作，不处理复杂嵌套图、连接线约束或图像编辑。你负责对象归属与视觉效果。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26205-ManagingGraphicObjects.html)（英文，官方手册）— Group 将多对象视为一个可移动组，Ungroup 可恢复各对象。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when related graphic and label objects must move together but individual dragging breaks their relative arrangement. Finish with a group moved into a safe location and a checked ungroup that restores each original object. Grouping is a reversible joint operation, not an irreversible flattening of content.

### Preparation and inputs

Save an ODP copy, list intended graphic/label objects and excluded background/title, and note relative positions. Check destination space and body visibility. Choose Group rather than Combine, since combining can change properties.

### Execution

1. Select related objects and check the selection excludes unrelated title or background.
2. Use Group and drag the outer group a short distance; components should move together with relative positions intact.
3. At target position check no overlap, then test Ungroup and select components separately; regroup if desired.
4. Save/reopen and verify final group state and integrity of graphic and label.

### Success, common problems, and recovery

Related objects move together and can return to separate components, while excluded objects stay and remain visible.

- **Title moves too:** Undo and narrow selection.
- **Cannot ungroup:** Check whether Combine was used.
- **Destination covers text:** Undo move and choose free space.

### Assumptions and limits

This handles one reversible group, not nested diagrams, connector constraints or image editing. You decide object membership and visual fit.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26205-ManagingGraphicObjects.html) — Group treats objects as one movable unit and Ungroup restores separate objects.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.

