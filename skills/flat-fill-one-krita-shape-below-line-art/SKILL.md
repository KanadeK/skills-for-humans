---
name: flat-fill-one-krita-shape-below-line-art
description: "Human procedure to fill one intended closed region on a separate color layer using Krita's Fill Tool, checking reference layers and edges."
---
# 在线稿下给一处 Krita 封闭形状铺平色 / Flat-Fill One Krita Shape below Line Art

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 有一处近封闭线稿、独立空白上色层和选定基色 / Nearly closed line-art shape, blank color layer and chosen base color |
| Side effects / 现实副作用 | 一块位于线稿下方、边缘正确的平色区域 / One flat color region below ink with checked edges |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一处已经描好的封闭物体，希望在不涂坏线稿的情况下加第一层平色时，单独做这一块填充。成果是颜色在轮廓内、线仍在上方可见，填色和线稿可分别改动。别凭一次点击后远看差不多就结束；放大看细边和开口最容易找到漏色。

### 准备与输入

先保存，在线稿下方建一层独立平色层。确认当前前景色与要画的基色一致，了解 Fill Tool 当前参考的是本层还是所有可见层；空白颜色层若只参考自身，可能会把整个画布填满。

### 执行

1. 选择填充工具，在工具选项中设相邻区域并选择能看到边界线的合适参考来源。
2. 先在封闭区域内部填一次，立即检查是否只落在平色层以及是否越过线条。
3. 放大查看轮廓周边有无白边或外溢，再用适度边缘调整或修线后重新填，不用大笔刷盖住错误。
4. 缩回实际观看尺寸，开关平色层确认与线稿分离，保存原稿。

### 完成、常见问题与恢复

目标形状被均匀铺色，轮廓清楚，外部区域未变且色层可单独关闭。

- **整张都被填：** 撤销并核参考来源与线条开口。
- **边缘有白晕：** 微调扩展或参考线，再填并近看。
- **盖住线稿：** 把平色层放回线稿下方，核混合顺序。

### 假设与边界

只铺一块普通平色，不覆盖复杂线稿自动上色、印刷套色或照片修复。填充参数要以本张线稿的实际边缘核对。

### 来源

- [Krita 5.3 Manual](https://docs.krita.org/en/reference_manual/tools/fill.html)（英文，官方手册）— 填充工具能按相邻区域、参考层和边界等选项决定填色范围。
- Original synthesis — 将一个数字绘画结果、原稿对照和失败停点组合为可核流程。

## English

Use this when one inked shape needs a base flat without painting over the ink. Finish with color bounded by the intended contour, with ink visible above and color separately editable. A one-click fill that looks acceptable from far away may still have halos or spills at close edges.

### Preparation and inputs

Save and create a dedicated flat-color layer beneath ink. Confirm foreground color and whether Fill Tool reads the current layer or all visible layers. A blank color layer used as its only reference may fill far beyond the inked region.

### Execution

1. Select Fill Tool, use a contiguous-region mode and choose a reference source that includes the boundary ink.
2. Fill once inside the intended shape and immediately verify the result appears on the flat layer only and stays within the contour.
3. Zoom in for white halos or overflow; adjust the fill edge modestly or fix the line and refill instead of hiding defects with broad brush strokes.
4. Zoom back to intended size, toggle the flat layer to prove separation from ink and save the master.

### Success, common problems, and recovery

The intended shape has an even flat, ink remains clear, outside areas stay unchanged and the color layer can be toggled alone.

- **Whole canvas filled:** Undo and inspect reference source plus contour gaps.
- **White halo:** Adjust edge growth or reference ink, refill and inspect closely.
- **Ink hidden:** Move flat layer beneath ink and check compositing order.

### Assumptions and limits

This fills one ordinary region, not automatic coloring of a complex page, print separation or photo repair. Tool values must be checked against this drawing's actual edges.

### Sources

- [Krita 5.3 Manual](https://docs.krita.org/en/reference_manual/tools/fill.html) — Fill Tool offers contiguous regions, reference-layer and boundary settings to control its extent.
- Original synthesis — one digital-painting outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Krita controls. You choose the content, perform the steps and verify the result.

