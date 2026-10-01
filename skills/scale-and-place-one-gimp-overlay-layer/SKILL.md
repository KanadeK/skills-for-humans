---
name: scale-and-place-one-gimp-overlay-layer
description: "Human-readable size-and-position correction for one imported GIMP overlay layer while keeping the base image and source proportions intact."
---
# 在 GIMP 合成图中缩放定位一层前景 / Scale and Place One GIMP Overlay Layer

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有两层的自有合成 XCF、明确上层应占的画面区域 / Existing owned two-layer composite XCF and intended overlay area |
| Side effects / 现实副作用 | 上层大小位置符合构图而底层未被误改 / Overlay fits composition while base stays untouched |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已把第二张获准图作为 GIMP 上层导入，但它太大或偏离该在的位置时使用本篇。成果是上层按比例缩放并放到计划区域，底图像素与位置不变，合成画面边缘没有意外空缺。它是对已有合成的前景定位，不再重复导入两张图。

### 准备与输入

保存 XCF，选中上层并记下其原宽高及底图尺寸。规划前景应占画面的大致比例和不该被遮的底图信息。Move 工具若处于“Pick a layer”可能选错层，先设仅移动选中层；不靠无比例拉伸硬塞进框。

### 执行

1. 对选中上层使用 Layer > Scale Layer，保持宽高比例链连着，设合理新尺寸。
2. 用 Move 工具的选中层模式把上层移到目标位置，核底层没有跟着走。
3. 在实际尺寸查上层边缘、底图遮挡和透视/比例是否可信，不暗示是同一张现场照片。
4. 保存重开，若位置或比例错误，撤销上层变换而不改底图。

### 完成、常见问题与恢复

上层位置与比例符合构图，底层不变、两个来源仍分层可追溯。

- **底图被移动：** 撤销并改 Move 选中层模式。
- **前景拉变形：** 恢复比例链从源层重缩。
- **边缘露空：** 重新定位或重新定尺寸，不删除底层。

### 假设与边界

只作一个上层的几何定位，不证明两图光照/透视真能相合。你负责合成标识与来源许可。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-layer-scale.html)（英文，官方手册）— Scale Layer 只改一层且比例链防失真。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill after importing a permitted second image as an upper GIMP layer when it is too large or misplaced. Finish with proportionate overlay size in the planned area, base pixels/position intact and no unintended canvas gaps. This positions an existing composite foreground; it does not re-import sources.

### Preparation and inputs

Save XCF, select upper layer and note its starting size and base canvas. Plan overlay's share of frame and base information not to cover. Move tool may pick a different layer unless set to move selected layer. Avoid independent width/height stretching just to make it fit.

### Execution

1. Use Layer > Scale Layer on selected upper layer with width/height link intact and a suitable size.
2. Use Move selected layers mode to place upper layer, checking base does not move.
3. At actual size inspect overlay edges, blocked base details and plausible scale, without implying one real exposure.
4. Save/reopen and undo upper transform for wrong placement or scale without changing base.

### Success, common problems, and recovery

Overlay position/scale fit composition, base is unchanged and sources remain separate.

- **Base moves:** Undo and choose selected-layer move mode.
- **Overlay distorted:** Relink dimensions and rescale from source.
- **Empty gap:** Reposition or resize overlay, keep base.

### Assumptions and limits

This positions one upper layer geometrically, not proof lighting/perspective match. You own composite disclosure and source rights.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-layer-scale.html) — Scale Layer changes one layer and linked dimensions prevent distortion.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.
