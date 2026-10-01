---
name: lighten-one-gimp-region-through-a-layer-mask
description: "Human-readable reversible local lightening on an owned image with a duplicate layer, feathered selection mask and before/after boundary check."
---
# 用 GIMP 图层蒙版只提亮一块区域 / Lighten One GIMP Region Through a Layer Mask

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 15–30 分钟 / 15–30 minutes |
| Requirements / 必要物品 | 有局部暗区的自有普通图、XCF 原层、可核软边选区 / Owned ordinary image with local dark area, XCF base and checked feathered selection |
| Side effects / 现实副作用 | 目标区较亮且蒙版边缘不过分显眼 / Target area lightens without a conspicuous mask seam |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张普通自有图只有一小块主体偏暗，不想把整个画面提亮时使用本篇。成果是该区域在上层变亮、周围景物基本保留原亮度，蒙版边界不形成硬圈，原图层可随时切回。它把已核的选区用于可回退局部调整，不虚构原本全黑区域的细节。

### 准备与输入

保存 XCF，复制原图层作工作层，确认目标暗区仍有可见纹理。准备一个软边选区，记录外围两处亮度参考。不要在原底层直接涂亮，也不要把隐私遮挡当成蒙版用途。

### 执行

1. 在复制层上做一次适度全层提亮，先只看目标区域达到可读而不过曝。
2. 保持软边选区，使用 Layer > Mask > Add Layer Masks 并选 Selection 初始化，让调整只在选区内显示。
3. 取消选区并切换上层可见性，检查边界、外部参考及目标纹理。
4. 边界露痕或外部也变时撤销蒙版/重做选区；满意时保存 XCF 与独立预览。

### 完成、常见问题与恢复

目标暗区更可读，外部亮度大致不变，软边自然且原层保留。

- **亮圈明显：** 减小提亮或调整软边。
- **整图都亮：** 核蒙版是否选 Selection 且选区未丢。
- **目标全黑：** 停止声称恢复细节。

### 假设与边界

只对一块有像素信息的普通照片做视觉调整，不代表真实照明或证据修复。你负责蒙版位置与范围。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-layer-mask-add.html)（英文，官方手册）— Add Layer Masks 的 Selection 选项让选中区可见、其余区透明。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when only one small subject area in an owned ordinary image is too dark and a global lift would damage the rest. Finish with the target brighter on an upper layer, surrounding scene near its original brightness, a soft mask edge and recoverable base. It uses a checked selection for reversible local adjustment, not invention of detail in clipped black pixels.

### Preparation and inputs

Save XCF, duplicate base into a work layer and confirm dark target retains visible texture. Prepare a feathered selection and note two outside brightness references. Do not paint directly on base or treat this as privacy masking.

### Execution

1. On duplicate, make a mild whole-layer lightening aimed at target detail without blowing it out.
2. Keep feathered selection and use Layer > Mask > Add Layer Masks initialized from Selection so edit appears only there.
3. Clear selection and toggle upper layer, checking seam, outside references and target texture.
4. Undo/redraw mask for a visible seam or outside change; otherwise save XCF and separate preview.

### Success, common problems, and recovery

Target reads brighter, surrounding brightness stays similar, edge is gentle and base remains.

- **Bright halo:** Reduce lift or refine feather.
- **Whole image bright:** Check Selection mask and active selection.
- **Target clipped black:** Stop claiming recovered detail.

### Assumptions and limits

This visually adjusts one region with actual pixel information; it does not reconstruct real lighting or evidence. You own mask position and range.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-layer-mask-add.html) — Add Layer Masks Selection initializes selected area visible and outside area transparent.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.
