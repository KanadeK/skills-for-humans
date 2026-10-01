---
name: union-two-inkscape-shapes-into-one-icon-silhouette
description: "Human workflow to use Boolean Union on two overlapping original icon shapes and inspect the single resulting outer contour."
---
# 把 Inkscape 两件重叠形状并成一个外轮廓 / Union Two Inkscape Shapes into One Icon Silhouette

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 两个构成同一主体的原创重叠形状、已保存 SVG / Two overlapping original shapes making one body and saved SVG |
| Side effects / 现实副作用 | 一条连续主体外轮廓，不保留内部重叠边 / One continuous main silhouette without an internal overlap boundary |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一枚原创图标主体由两个重叠形状拼成，中间意外露出接缝或独立修改已不需要时，用 Union 真正合成外轮廓。成果是一个连续主体路径，不再有内部重叠边。Union 与 Group 不同：组仍保留两个对象；因此要在确定外形后做，并留可回退原稿。

### 准备与输入

保存 SVG 或复制两个源形状，先确认它们确实应成为同一填色主体，而不是一个需要独立改色的装饰。缩小查看当前接缝和目标外形，核选区只有这两件，没有背景页或旁边小标记。

### 执行

1. 让两件源形状按计划交叠，检查交叠区没有意外空隙。
2. 同时选择两件，执行 Path > Union，核结果成为单一外形路径。
3. 放大看原接缝是否消失，节点工具看轮廓没有多余尖角或破洞。
4. 缩回目标尺寸确认仍像原计划主体，保存重开；若装饰被吞，回备份重选对象。

### 完成、常见问题与恢复

两个源形状成为一条连贯的原创图标主体外轮廓，内部接缝消失。

- **并入了装饰：** 撤销，重新只选主体两件。
- **轮廓出现尖角：** 回节点检查交叠处的几何，必要时重摆再并。
- **需要两色：** 回源形状，改用 Group 而非 Union。

### 假设与边界

只并两件原创几何，不复制现有标志，也不保证复杂自交路径在所有查看器相同。

### 来源

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/boolean-operations.html)（英文，官方手册）— Union 将所选路径的共同外形合成，结果不再是两件可独立改的对象。
- Original synthesis — 将一个原创矢量图形结果、原稿对照和失败停点组合为可核流程。

## English

Use this when two overlapping shapes form one original icon body and an internal seam should disappear. Boolean Union should yield a continuous outer path with no separate internal overlap edge. It differs from Group, which keeps two editable members, so perform it only after the silhouette is decided and keep a rollback copy.

### Preparation and inputs

Save or duplicate both source shapes. Confirm they truly belong to one filled body rather than a separately colored detail. Inspect the current seam and desired outer silhouette at small size, selecting only those two objects without background or neighboring marks.

### Execution

1. Position the two source shapes with the intended overlap and no accidental gap.
2. Select both and run Path > Union, confirming one resulting outer path.
3. Zoom in to check seam removal and inspect resulting nodes for kinks or holes.
4. Check the silhouette at target size, save and reopen; if a detail was swallowed, restore source shapes and select correctly.

### Success, common problems, and recovery

The two source shapes become one continuous original icon silhouette and the overlap seam is gone.

- **Detail merged:** Undo and select only the two body shapes.
- **Kink appears:** Inspect overlap geometry and reposition before union.
- **Need two colors:** Restore source objects and use Group instead.

### Assumptions and limits

This unions two original shapes, not an existing logo, and does not guarantee complex self-intersecting paths render identically everywhere.

### Sources

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/boolean-operations.html) — Union keeps the combined outer outline and no longer leaves two independently editable shapes.
- Original synthesis — one original vector-art outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Inkscape controls. You choose the content, perform the steps and verify the result.

