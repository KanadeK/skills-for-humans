---
name: draw-one-onion-skin-krita-inbetween-frame
description: "Human workflow to add one transparent in-between drawing between two owned keyframes using Krita onion skin, then inspect spacing in preview."
---
# 借 Krita 洋葱皮补一张动作中间帧 / Draw One Onion-Skin Krita In-Between Frame

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 20–35 分钟 / 20–35 minutes |
| Requirements / 必要物品 | 两张已保存原创关键帧、透明动画层和洋葱皮面板 / Two saved original keyframes, transparent animation layer and Onion Skin docker |
| Side effects / 现实副作用 | 一张从前后姿态推得的可播放中间帧 / One playable in-between frame guided by neighboring poses |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有原创动作的两端姿态，却在预览时觉得跳变太突然，可以只加一张中间帧测试过渡。成果是新姿态位于两端之间，位置、方向和主要形状能连起来；洋葱皮只是参考叠影，不应留在最终绘画像素里。若两端本身不合理，补帧不会自动修好动作逻辑。

### 准备与输入

保存当前两帧工程，确认动画层透明且两个端点都存在。选定中间时点，检查时间线没有误选背景或另一动画层；先决定物体中点位置，而不是只平均每根线条。

### 执行

1. 在两个端点之间创建一张空白帧，启用目标动画层的洋葱皮并显示前后相邻帧。
2. 参考前后叠影先画主体位置和运动方向，再补必要轮廓，保持与两端一致的身份特征。
3. 关闭洋葱皮单独查看中间帧，确认它确实有自己的像素而非只看到邻帧叠影。
4. 播放 A—中间—B 的短循环，检查跳变是否改善；过渡仍不通顺就改关键帧或中间位置，保存。

### 完成、常见问题与恢复

新增的中间帧单独可见，预览时物体位置与轮廓沿预期动作过渡，原两端帧未丢。

- **只见鬼影没新画：** 确认新帧和绘画层处于活动状态，再补真实笔画。
- **洋葱皮不显示：** 检查动画层透明度、帧存在与面板开关。
- **动作反而抖：** 比对主体中心与两端，修中点而非加装饰细节。

### 假设与边界

只补一帧普通原创逐帧动画，不担保专业动画节奏、视频输出或特定帧率播放体验。

### 来源

- [Krita 5.3 Manual](https://docs.krita.org/en/reference_manual/dockers/onion_skin.html)（英文，官方手册）— 洋葱皮显示相邻帧供中间绘制参考，透明动画层是可见性前提。
- Original synthesis — 将一个数字绘画结果、原稿对照和失败停点组合为可核流程。

## English

Use this when two original key poses jump too abruptly and one intermediary could clarify motion. Finish with a new drawing between them whose position, direction and main shape bridge A and B. Onion skin is a viewing overlay, not paint that should appear in the final pixels. An in-between cannot rescue endpoints that contradict the intended action.

### Preparation and inputs

Save the two-frame project, confirm the animation layer is transparent and both endpoints exist. Choose an intermediate time cell and check you have not selected the background or another animated layer. Decide the object's mid-position before averaging small contour details.

### Execution

1. Create a blank frame between endpoints and enable onion skin for the animated layer, showing both neighboring poses.
2. Use the ghosted frames to place the main mass and motion direction, then draw only the contours needed to preserve the same object's identity.
3. Turn onion skin off and inspect the middle cell alone, confirming it contains actual new pixels rather than only neighboring ghosts.
4. Preview the A-to-middle-to-B loop. If motion still breaks, revise endpoints or placement instead of piling on more frames; save.

### Success, common problems, and recovery

The new middle frame is independently visible, preview motion follows the intended path and both original endpoints remain intact.

- **Only ghosts visible:** Confirm the new frame and paint layer are active, then draw real pixels.
- **No ghosts:** Inspect transparency, neighboring frames and the docker toggle.
- **Motion jitters:** Compare the subject center across all three poses and correct midpoint placement.

### Assumptions and limits

This adds one ordinary original raster in-between, not professional animation timing, video output or guaranteed playback at a particular frame rate.

### Sources

- [Krita 5.3 Manual](https://docs.krita.org/en/reference_manual/dockers/onion_skin.html) — Onion Skin Docker overlays neighboring frames for in-betweens and requires an appropriate transparent animation layer.
- Original synthesis — one digital-painting outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Krita controls. You choose the content, perform the steps and verify the result.

