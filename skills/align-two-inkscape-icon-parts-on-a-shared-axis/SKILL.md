---
name: align-two-inkscape-icon-parts-on-a-shared-axis
description: "Human workflow to align two independent vector icon parts by center or edge using a chosen reference without altering their shape."
---
# 把 Inkscape 图标两件零件对到同一轴 / Align Two Inkscape Icon Parts on a Shared Axis

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存原创 SVG 和两件应共轴的独立对象 / Saved original SVG and two independent parts meant to share an axis |
| Side effects / 现实副作用 | 两件对象共中心或基线，形状尺寸不变 / Two parts share the planned center or baseline with dimensions unchanged |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一枚原创图标里，主体和小把手应该共中心，但手动拖动总有细微偏差时，用对齐命令完成一个明确关系。成果是两个对象共享预定轴线，大小和外形没有被改变。关键在 Relative to 的参照对象；如果选成整个页面，可能两个部件一起移动到意外位置。

### 准备与输入

保存 SVG，确定要对齐的是水平中心、垂直中心还是某条边，并指定哪个主体应保持不动。确认两件对象都仍独立且没有意外包含隐藏背景或参考线，否则对齐范围会被放大。

### 执行

1. 单选两件对象，打开 Align and Distribute，设置 Relative to 为预定的固定对象或页面。
2. 执行目标方向的一次对齐，观察两对象是否沿正确轴移动。
3. 缩到图标实际大小检查视觉中心，必要时因不对称轮廓做小幅有意光学调整并记录。
4. 核对象的宽高、形状控制柄未变，保存重开再看对齐关系。

### 完成、常见问题与恢复

两件零件沿计划基线或中心对齐，主体形状仍可独立编辑，位置关系稳定。

- **两件都跑走：** 撤销并改 Relative to 参照。
- **按错轴：** 撤销后只执行目标水平或垂直按钮。
- **看着仍偏：** 区分几何中心与视觉重心，做有记录的小调整。

### 假设与边界

这里只对齐两件图标对象，不建立复杂响应式布局或正式品牌网格规范。

### 来源

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/align-and-distribute.html)（英文，官方手册）— Align and Distribute 可按所选对象或页面基准对齐，并需明确 Relative to。
- Original synthesis — 将一个原创矢量图形结果、原稿对照和失败停点组合为可核流程。

## English

Use this when two parts of an original icon should share a centerline or baseline but manual dragging leaves a visible offset. Finish with that exact relation while preserving both shapes and sizes. The Relative to reference matters: aligning to the whole page can move both parts somewhere unintended.

### Preparation and inputs

Save and choose horizontal center, vertical center or one edge, naming which main object should stay fixed. Ensure exactly two independent visible objects are selected, without a hidden background or guide enlarging the bounds.

### Execution

1. Select the two parts, open Align and Distribute and set Relative to to the planned fixed object or page.
2. Apply one alignment action for the intended axis and inspect which object moved.
3. At target icon size inspect visual balance; if asymmetric shapes demand a small optical correction, make it deliberately and note it.
4. Confirm width, height and shape handles did not change, then save and reopen to inspect the relation.

### Success, common problems, and recovery

The parts share the planned axis or baseline, remain independently editable and retain their shape.

- **Both moved away:** Undo and choose the correct Relative to reference.
- **Wrong axis:** Undo and apply only the intended horizontal or vertical action.
- **Still looks off:** Distinguish geometric center from optical balance and adjust knowingly.

### Assumptions and limits

This aligns two icon objects, not a responsive layout or formal brand grid system.

### Sources

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/align-and-distribute.html) — Align and Distribute aligns relative to a chosen object or page reference.
- Original synthesis — one original vector-art outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Inkscape controls. You choose the content, perform the steps and verify the result.

