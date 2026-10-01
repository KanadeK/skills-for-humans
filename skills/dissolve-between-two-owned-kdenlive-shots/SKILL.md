---
name: dissolve-between-two-owned-kdenlive-shots
description: "Human-readable short visual dissolve between two permitted Kdenlive shots with overlap, midpoint and final subject visibility checks."
---
# 在 Kdenlive 两段自有镜头间做一次短溶解 / Dissolve Between Two Owned Kdenlive Shots

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 相邻两段自有或获准镜头、保存工程、明确过渡目的 / Adjacent permitted shots, saved project and reason for a visual blend |
| Side effects / 现实副作用 | 两镜头有克制过渡且内容不被长时间叠影 / Two shots blend briefly without prolonged ghosting |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有两段自有短片镜头，直接硬切让时间或地点变化显得过急，想用一处短溶解帮助衔接时使用本篇。成果是上一镜头逐渐离开、下一镜头逐渐出现，过渡中点可理解主体，片段本身首尾动作不丢。不是每个剪辑点都需要溶解，硬切仍可能更清楚。

### 准备与输入

保存工程，先看片一尾与片二头，确认两者内容允许短重叠且没有互相遮蔽的重要字。准备两条视频轨或当前版本支持的混合方式，选短过渡，不下载额外花哨模板。若音频也需衔接，单独核声音，不把画面溶解当音频淡变。

### 执行

1. 让两镜头在目标边界有少量重叠，使用默认无花纹 Dissolve 组合。
2. 从前数秒播放到后数秒，核开始、中点、结束画面主体与时长。
3. 看过渡是否产生过长双影或把下一镜头首个动作盖掉，必要时缩短或退回硬切。
4. 核声音与后续时间线未无意移动，保存重开预览。

### 完成、常见问题与恢复

一处短溶解自然、主体可辨、声画和邻片未被误改；不合适可明确保留硬切。

- **双影很久：** 缩短重叠。
- **首动作被盖：** 移动边界或用硬切。
- **只有声音渐变：** 核作用对象是视频合成。

### 假设与边界

只处理一处普通视觉衔接，不证明叙事质量或真人观看接受度。你决定是否用过渡。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/compositing/transitions/composite_transitions.html)（英文，官方手册）— 重叠片段可形成默认无图案溶解，过渡时长按重叠帧数。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a hard cut between two owned shots rushes a time/place change and one short dissolve could clarify it. Finish with outgoing shot fading as incoming arrives, midpoint still interpretable and each shot's important action intact. Not every boundary needs a dissolve; a hard cut may read better.

### Preparation and inputs

Save project and inspect end of shot A and start of B for overlap without hiding key words/objects. Use two video tracks or supported mix, choose short transition and no downloaded templates. Audio continuity needs separate listening; a visual dissolve is not an audio fade.

### Execution

1. Overlap shots briefly at intended boundary and use plain default Dissolve composition.
2. Play across boundary, checking start, midpoint, end subjects and duration.
3. Check for long ghosting or hidden incoming action; shorten or revert to cut if better.
4. Check audio/later timeline unchanged, save/reopen and preview.

### Success, common problems, and recovery

One short dissolve reads clearly with no accidental A/V change; a deliberate hard cut remains valid fallback.

- **Long ghost:** Shorten overlap.
- **Incoming action hidden:** Move cut or use hard cut.
- **Only audio fades:** Check video composition target.

### Assumptions and limits

This treats one ordinary visual boundary, not story quality or viewer acceptance. You decide whether dissolve helps.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/compositing/transitions/composite_transitions.html) — overlapping clips can use default dissolve with duration set by overlap frames.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

