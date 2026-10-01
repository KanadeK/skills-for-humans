---
name: resize-a-gimp-copy-for-screen-display
description: "Human-readable GIMP pixel-dimension reduction on a copy for screen use, preserving aspect ratio and checking detail after export."
---
# 为屏幕展示缩小一份 GIMP 图片副本 / Resize a GIMP Copy for Screen Display

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存 XCF 与原图、明确屏幕用途和目标最大像素边 / Saved XCF and original, screen purpose and target maximum pixel side |
| Side effects / 现实副作用 | 输出像素更适合屏幕且主体仍清楚 / Output pixels fit screen use while subject remains clear |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张像素很大的自有照片，想做一份屏幕查看或私下发送的较小副本时使用本篇。成果是像素宽高按选定上限降低、纵横比例未变、关键细节在实际显示尺寸仍可辨。这里改变像素数，不等于仅改打印分辨率，也不能凭上采样造出丢失细节。

### 准备与输入

保存 XCF 主本和原图，先从接收屏幕或文件用途选目标长边，不套通用像素数。记录原像素宽高及一个必须看清的细节。另建工作副本或从主本另存版本，缩小是有损像素操作，不在唯一主本上直接做。

### 执行

1. 在工作副本用 Image > Scale Image 输入目标宽或高，保持链状比例锁定。
2. 选择本机提供的合适插值，确认另一边自动按比例变化，避免把图压扁。
3. 缩放后以实际像素或目标显示尺寸查看细节与边缘，再导出独立预览。
4. 重开预览核宽高像素与可读性；不合格就从大尺寸主本重新缩放。

### 完成、常见问题与恢复

屏幕副本的像素尺寸与用途相符，比例和关键信息仍可读，主本未被缩小。

- **图被拉宽：** 撤销并重新锁定宽高比例。
- **细节糊：** 从原主本以更大目标重做。
- **只改了 DPI：** 检查实际像素宽高是否变化。

### 假设与边界

此篇只为屏幕用途下采样，不保证所有接收设备色彩一致，也不涉及公开传播许可。你决定目标像素。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-image-scale.html)（英文，官方手册）— Scale Image 改变像素数，锁定比例可避免拉伸。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill for a large owned photo when a smaller copy is needed for screen viewing or private transfer. Finish with pixel width/height under a chosen bound, aspect ratio intact and important detail legible at actual display size. This changes pixel count, unlike print-resolution metadata; upscaling cannot invent lost detail.

### Preparation and inputs

Keep XCF master and original, choose a target long side from actual receiving screen/purpose, not a universal number. Note starting pixel dimensions and one essential detail. Make a working version before reducing pixels; downscaling discards information.

### Execution

1. On working copy use Image > Scale Image, enter target width or height and keep aspect link intact.
2. Choose suitable available interpolation and confirm the other dimension updates proportionally.
3. Inspect essential detail and edges at actual pixels or target display size, then export a separate preview.
4. Reopen preview and verify pixel dimensions and legibility; retry from larger master if poor.

### Success, common problems, and recovery

Screen copy matches target pixels, proportions and key information remain readable, and master stays large.

- **Image stretched:** Undo and relink dimensions.
- **Detail soft:** Redo from master at larger target.
- **Only DPI changed:** Check pixel width/height changed.

### Assumptions and limits

This downsamples for screen use only; it cannot guarantee color across devices or public-sharing permission. You set pixel target.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-image-scale.html) — Scale Image changes pixel count and linked dimensions prevent distortion.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.

