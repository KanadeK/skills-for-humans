---
name: align-owned-external-audio-to-kdenlive-camera-clap
description: "Human-readable alignment of a permitted external audio track to camera sound using one shared clap, with start and later drift checks."
---
# 用拍手把自有外录声音对齐 Kdenlive 画面 / Align Owned External Audio to a Kdenlive Camera Clap

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 本人画面同期声、本人外录音轨、同一拍手提示和保存项目 / Owned camera sound, owned external audio, shared clap cue and saved project |
| Side effects / 现实副作用 | 两轨拍手重合，后段漂移被单独记录 / Two clap cues align while later drift is reported separately |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你用相机和独立录音设备同时录了本人短视频，两个轨道都有同一次拍手，想把好音频对齐画面时使用本篇。成果是拍手声与手接触画面在同一时点附近，开头一段可听；后段若有时钟漂移必须如实记录。它不是把任何不同环境声自动猜成同一事件。

### 准备与输入

保存项目，保留相机同期声作参考，导入自有外录音到另轨。先分别听到同一次拍手，确认两个录音没有速度/采样率异常。记录拍手附近画面和两轨波形，避免对错另一声拍手。

### 执行

1. 选相机同期声设 Set Audio Reference，再选外录音用 Align Audio to Reference。
2. 在拍手点逐帧看手接触与双轨声音尖峰，轻微偏差按耳朵/画面校。
3. 试听开头和末尾各一段，核没有明显双拍或逐渐漂移。
4. 保存项目；末段错位就记录漂移，不把首点对齐宣称整段精确同步。

### 完成、常见问题与恢复

共同拍手附近声画一致，起止抽查有结果，外录原件仍在。

- **两次拍手混淆：** 回原音频分别确认事件。
- **末段漂移：** 记录并转更完整同步流程。
- **参考选错：** 撤销并用相机声重新设参考。

### 假设与边界

只用一处提示对齐短视频，不保证长片时钟准确或广播级对口型。你负责音源许可和试听。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/right_click_menu.html)（英文，官方手册）— Set Audio Reference / Align Audio to Reference 可用近似相同声音对齐不同轨。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when your own camera and separate recorder captured the same clap during a short video and external audio should align with picture. Finish with clap sound near visual hand contact and a checked opening passage; any later clock drift is recorded honestly. Do not ask software to match unrelated background noises as one event.

### Preparation and inputs

Save project and retain camera sound as reference, importing owned external audio on another track. Listen separately for same clap and check speed/sample-rate anomalies. Note visual contact and waveform spikes to avoid matching another clap.

### Execution

1. Set camera audio as Audio Reference, then Align external audio to Reference.
2. Inspect visual contact and two audio peaks frame by frame, adjusting small offsets by sound/image.
3. Listen near beginning and end for double clap or growing drift.
4. Save project. Record later drift instead of claiming full sync from one cue.

### Success, common problems, and recovery

Shared clap aligns with picture, early/late checks are recorded and external source remains.

- **Wrong clap matched:** Verify same event in both sources.
- **Later drift:** Record and use broader sync process.
- **Wrong reference:** Undo and set camera sound.

### Assumptions and limits

This aligns one cue in a short piece, not long-clock accuracy or broadcast lip sync. You own source rights and listening.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/right_click_menu.html) — Set/Align Audio to Reference aligns tracks with nearly identical shared sound.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

