---
name: choose-a-kdenlive-project-profile-before-cutting
description: "Human-readable Kdenlive profile choice from owned source and intended output, checking frame size/rate before edits or keyframes."
---
# 按目标输出给 Kdenlive 项目选画面规格 / Choose a Kdenlive Project Profile Before Cutting

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已知素材宽高与帧率、明确最终观看场景、新项目 / Known source dimensions/fps, intended viewing context and new project |
| Side effects / 现实副作用 | 工程尺寸帧率有依据且先于时间线特效确定 / Project size/rate are grounded before timeline effects |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你准备把自有短视频做成一个 Kdenlive 项目，需先决定最终画面的宽高与帧率时使用本篇。成果是项目 Profile 与主要素材和预期观看场景相符，设置在剪辑/关键帧前明确；不把“4K”“60fps”当万能更好。改变 Profile 可能重排画面，应先在空项目阶段定。

### 准备与输入

从素材卡看主要视频的宽高、方向与 fps，写出目标观看位置（普通横屏/竖屏私下观看等）。若不同素材帧率混用，选对主线最合理的配置并记录取舍。先不创建自定义 Profile，现有适配预设足够时直接选。

### 执行

1. 在新项目的 Project Settings 查看候选 Profile 的宽高、比例、fps。
2. 选择与主要素材/目标输出接近的一项，核方向正确且不会无谓上采样。
3. 添加一小段素材预览，检查画面没有意外黑边、拉伸或变速。
4. 记录 Profile 名和理由，保存项目；不合适时在正式剪辑前改。

### 完成、常见问题与恢复

工程 Profile 宽高/fps 与目标有解释，主要素材预览不被拉坏。

- **画面被拉长：** 核横纵比例与 Profile。
- **大量黑边：** 确认是否方向或比例不合。
- **后期才改：** 先存副本评估影响，不直接改主项目。

### 假设与边界

只决定个人短片项目口径，不认证播出平台或专业色彩/帧率要求。你负责输出用途。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/project_and_asset_management/project_settings/general_settings.html)（英文，官方手册）— Project profile 决定分辨率与帧率，后期再改可能影响效果。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill before editing owned short footage in Kdenlive when final frame size and rate must be chosen. Finish with a project Profile grounded in main source and viewing purpose before cuts/keyframes, not an automatic preference for 4K or 60 fps. Changing profile later can affect framing/effects, so decide early.

### Preparation and inputs

Use source note for main clip dimensions, orientation and fps, and state viewing context such as private landscape or portrait screen. If mixed rates, choose a main-timeline compromise and record tradeoff. Prefer a suitable built-in profile over unnecessary custom settings.

### Execution

1. In new Project Settings inspect candidate Profiles for dimensions, aspect and fps.
2. Choose a profile near main source and output, with right orientation and no needless upscale.
3. Preview a short imported source and check for bars, stretching or speed anomalies.
4. Record profile and reason, save project and revise before substantial editing if wrong.

### Success, common problems, and recovery

Project dimensions/rate fit a stated purpose and main clip preview is not distorted.

- **Image stretched:** Check aspect and profile.
- **Large black bars:** Check orientation/ratio.
- **Late profile change:** Test on copy first.

### Assumptions and limits

This sets a personal short-film project profile, not platform or broadcast certification. You own target use.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/project_and_asset_management/project_settings/general_settings.html) — project profile sets size/fps and later changes can disturb effects.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

