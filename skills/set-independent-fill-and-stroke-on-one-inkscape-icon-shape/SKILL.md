---
name: set-independent-fill-and-stroke-on-one-inkscape-icon-shape
description: "Human workflow to style one original icon shape with deliberate interior fill and outline width, then inspect clarity at intended small size."
---
# 分别设定 Inkscape 图标一件形状的填色和描边 / Set Independent Fill and Stroke on One Inkscape Icon Shape

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存原创 SVG、一个可选形状和计划的前后对比 / Saved original SVG, one selectable shape and intended contrast |
| Side effects / 现实副作用 | 形状内部和轮廓分别符合用途，小尺寸仍清楚 / Shape fill and outline independently suit the icon and remain clear when small |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你做的原创图标主形目前只有默认蓝底黑边，缩小时轮廓可能太重或内部不够清楚；先单独决定填色与描边。成果是内外颜色、线宽有明确作用且不会误把全对象不透明度调低。填充和描边是两种不同属性，点击调色板一次通常只解决其中一项。

### 准备与输入

保存 SVG，单选目标形状，核它不是整个组或背景。写下内部色、轮廓色和想让轮廓承担的识别作用；如果小尺寸根本不需要边线，就可以明确设无描边，而非留一条看不出的细线。

### 执行

1. 在 Fill and Stroke 的 Fill 页设置单色内部或明确无填色。
2. 在 Stroke paint 与 Stroke style 分别设轮廓颜色、宽度与端点/转角，避免超出页边。
3. 缩到目标尺寸检查边线没有吞掉内部形状，颜色对比能让主体被辨认。
4. 切换选中状态看真实外观，保存重开确认样式仍附在目标对象。

### 完成、常见问题与恢复

该对象的填充与轮廓可分别说明，小图能辨认主形，其他对象样式未误改。

- **整图变透明：** 核是否改了全对象 Opacity，恢复后分别调 Fill/Stroke。
- **边线被裁：** 减宽或留更大页边，再核导出范围。
- **没改到目标：** 核当前选择是单对象而不是组。

### 假设与边界

只处理一件矢量形状的普通屏幕样式，不保证色觉可及性、品牌色或印刷色值。

### 来源

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/fill-and-stroke-dialog.html)（英文，官方手册）— Fill and Stroke 将内部填色、描边颜色和描边样式分成独立控制页。
- Original synthesis — 将一个原创矢量图形结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an original icon body still has default fill and outline and becomes muddy at small size. Decide interior paint and stroke separately, giving each a clear role without accidentally lowering whole-object opacity. Fill and stroke are different properties; one palette click usually changes only part of the appearance.

### Preparation and inputs

Save, select the target shape rather than the full group or background, and state the interior, outline and purpose of the outline. If the icon needs no border at target size, choose no stroke explicitly instead of leaving an invisible hairline.

### Execution

1. Set a solid interior or explicit no fill in the Fill tab.
2. Set outline paint, width, joins and caps in Stroke paint and Stroke style, keeping the stroke inside the page margin.
3. Inspect at target size for an outline that does not swallow the interior and for usable subject contrast.
4. Deselect to inspect the true appearance, then save and reopen to confirm style remains on the intended object.

### Success, common problems, and recovery

The object's fill and outline have distinct purposes, its small-size shape reads clearly and other objects remain unchanged.

- **Whole icon fades:** Inspect whole-object Opacity and restore it before styling fill and stroke.
- **Stroke clipped:** Reduce width or increase margin and recheck export bounds.
- **Wrong target:** Check selection is the one object rather than a group.

### Assumptions and limits

This styles one screen vector shape; it does not certify color accessibility, brand color or print values.

### Sources

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/fill-and-stroke-dialog.html) — Fill and Stroke separates interior paint, stroke paint and stroke style controls.
- Original synthesis — one original vector-art outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Inkscape controls. You choose the content, perform the steps and verify the result.

