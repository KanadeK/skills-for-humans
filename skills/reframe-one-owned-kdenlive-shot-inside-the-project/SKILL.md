---
name: reframe-one-owned-kdenlive-shot-inside-the-project
description: "Human-readable clip-level Kdenlive Transform adjustment to center a permitted subject within project frame while preserving proportions and source media."
---
# 在 Kdenlive 画布内重构图一段自有镜头 / Reframe One Owned Kdenlive Shot Inside the Project

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 主体偏边的一段自有镜头、保存工程、已定项目画布 / Owned shot with off-center subject, saved project and set frame profile |
| Side effects / 现实副作用 | 主体在输出框内更清楚，原素材未裁改 / Subject fits output frame better with source untouched |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一段自有镜头在项目画幅里主体过于靠边或出现多余边框，想只调整这一镜头在画布里的位置与大小时使用本篇。成果是主体在开始、中间、结束都留在可见区，画面不被拉变形，源媒体原件未改。它不是对拍摄事实作造假裁切，不能用来隐藏关键证据。

### 准备与输入

保存工程，先看镜头首中尾主体运动范围，确定需要保留的环境线索。核项目画幅比例与素材比例，过度放大可能掉像素；记录原效果设置便于回退。只选时间线上这一次出现的片段，避免对项目箱源素材全局生效。

### 执行

1. 给目标时间线片段加 Transform，调整位置与大小，保持比例且不启用非均匀 Distort。
2. 在首中尾三处核主体是否始终在框内、边缘和字幕安全区不被挤。
3. 对照原镜头看必要背景没有被裁掉，像素细节未被过度放大。
4. 不合适就撤回变换，保存重开并预览实际项目画幅。

### 完成、常见问题与恢复

这段镜头在项目画布内更合适，主体不跑出框，比例和必要上下文保留。

- **主体后半段出框：** 检查整段运动，必要时用有限关键帧。
- **画面被拉宽：** 关闭 Distort 并恢复比例。
- **图像变糊：** 减小放大或换更高像素源。

### 假设与边界

只修一段普通镜头构图，不做证据遮蔽或承诺画质提升。你负责场景真实性。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/video_effects/transform_distort_perspective/transform.html)（英文，官方手册）— Transform 可在项目画布内调 X/Y/宽高，关闭 Distort 可免非均匀拉伸。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an owned shot sits too far to an edge or has unnecessary border in the chosen project frame and needs clip-level position/size adjustment. Finish with subject inside frame at start/middle/end, no non-uniform stretch and source unchanged. Do not use reframing to hide key evidentiary context.

### Preparation and inputs

Save project and inspect subject movement at beginning/middle/end plus context to retain. Compare project/source aspect; excessive zoom loses detail. Note original effect state. Select this timeline instance only, not a bin-wide source effect.

### Execution

1. Apply Transform to target timeline clip, adjust position/size with proportions intact and no non-uniform Distort.
2. Check subject at first/middle/last frames plus edges and subtitle space.
3. Compare original for lost context and over-enlarged detail.
4. Undo poor transform; save/reopen and preview actual project frame.

### Success, common problems, and recovery

Shot fits project frame, subject stays visible and aspect/context remain.

- **Subject exits later:** Inspect motion; use limited keyframe if needed.
- **Image stretched:** Disable Distort and relink ratio.
- **Image soft:** Reduce zoom or use better source.

### Assumptions and limits

This reframes an ordinary shot, not evidence concealment or quality gain. You preserve scene truth.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/video_effects/transform_distort_perspective/transform.html) — Transform adjusts X/Y/size within canvas and avoiding Distort prevents uneven stretch.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

