---
name: moderate-photo-saturation-on-a-gimp-copy
description: "Human-readable single saturation adjustment on an owned GIMP photo copy with subject-color and channel-clipping checks."
---
# 在 GIMP 副本上克制调整照片饱和度 / Moderate Photo Saturation on a GIMP Copy

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 有颜色强度问题的自有 RGB 照片、XCF 原层与工作层 / Owned RGB photo needing color-intensity adjustment, XCF base and work layers |
| Side effects / 现实副作用 | 颜色强弱更适合用途且不出现大片刺眼断层 / Color intensity better fits use without obvious artifacts |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张自有照片颜色显得太灰或太刺眼，想只改颜色强度而不顺手改明度、色相时使用本篇。成果是主体彩色仍可辨、细节和自然物表面没有明显色块或不可信荧光感。它与冷暖偏色修正不同：饱和度只改变彩度观感，不自动校正白平衡。

### 准备与输入

保存 XCF 副本并选工作层，指出一处主体颜色与一处容易过饱和的区域，例如花瓣或天空。核图像为 RGB，若是灰度模式，饱和度命令可能不可用。决定是减弱还是略增强，不用最大滑块位置当质量指标。

### 执行

1. 打开 Colors > Saturation，只改 Scale 一项，小幅观察预览。
2. 在实际尺寸检查主体颜色、渐变和边缘，找是否出现色块、噪点或细节丢失。
3. 切换工作层与原层，判断改善是否符合用途而不是只更艳。
4. 若颜色不可信就退回或撤销，满意时保存独立工作版本与导出预览。

### 完成、常见问题与恢复

颜色强度与用途相符，主体和细节保留，前后对照解释了改变。

- **颜色成荧光：** 减弱增幅或还原。
- **天空出现条带：** 撤回过强调整并核源图压缩。
- **命令不可用：** 核是否灰度图。

### 假设与边界

只调整普通自有图片的整体饱和度，不证明真实颜色或用于商品、证据图。你负责审美与许可。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-filter-saturation.html)（英文，官方手册）— Colors > Saturation 的 Scale 调整体颜色强度。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an owned photo looks too muted or aggressively colorful and you want to change color intensity without simultaneously shifting brightness or hue. Finish with subject colors still distinguishable and no obvious flat patches or implausible neon surfaces. Saturation differs from warm/cool cast correction and cannot set white balance.

### Preparation and inputs

Save XCF copy and select work layer. Identify one subject color and one region prone to over-saturation, such as petals or sky. Confirm RGB; grayscale may disable this command. Decide whether to reduce or gently raise saturation rather than treating slider extremes as quality.

### Execution

1. Open Colors > Saturation and alter only Scale modestly while previewing.
2. Inspect subject colors, gradients and edges at actual size for flat patches, noise or detail loss.
3. Toggle work and base layers to judge fitness for purpose rather than vividness alone.
4. Back off for implausible color; otherwise save an independent work version and preview export.

### Success, common problems, and recovery

Color intensity fits purpose, subject/detail remain, and before/after explains the change.

- **Neon colors:** Reduce increase or restore.
- **Sky bands:** Back off and inspect source compression.
- **Command disabled:** Check grayscale mode.

### Assumptions and limits

This changes global saturation of an ordinary owned image, not proof of true color or suitability for product/evidence photos. You own aesthetics and permission.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-filter-saturation.html) — Colors > Saturation Scale changes overall saturation.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.

