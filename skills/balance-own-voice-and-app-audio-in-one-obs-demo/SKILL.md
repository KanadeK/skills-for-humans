---
name: balance-own-voice-and-app-audio-in-one-obs-demo
description: "Human workflow to balance self narration against permitted application sound in OBS and verify both are audible without clipping in a recorded test."
---
# 把 OBS 私有演示的本人解说与应用声调到可听 / Balance Own Voice and App Audio in One OBS Demo

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 本人话筒、获准应用声和已保存私有场景 / Own microphone, permitted app sound and saved private scene |
| Side effects / 现实副作用 | 短测里解说清楚、应用声可辨且无明显削波 / Test has intelligible narration, audible app sound and no obvious clipping |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你录自己应用操作时，语音解说被音效盖住，或把应用声降没了而失去示范意义，就需要做一次相对电平调整。成果要由真实短测回放证明：话能听清、应用声也可辨，没有刺耳破音。单看 OBS 表上的绿黄红区不足以证明观众耳朵听到的平衡。

### 准备与输入

准备一段无敏感解说词和应用里最响的获准测试音，确认只有各一条采集路径。先看话筒设备自身增益，不用 OBS 推子去修复已经在输入端削波的信号；选耳机回放以免扬声器串到话筒。

### 执行

1. 让本人讲话并播放应用声，观察两条 Mixer 表的相对电平与峰值。
2. 先调设备或源端过高信号，再用 OBS 推子使语音优先、应用声仍有意义。
3. 录包含安静讲话、正常操作和最响应用声的短测，重开用耳机听。
4. 若破音或听不清，只调整相应来源并再测；保存成功组合。

### 完成、常见问题与恢复

实际文件里本人解说、应用声都能按作用听见，最高片段无明显削波。

- **话筒仍破音：** 降低输入端增益而非仅拉低录制推子。
- **应用声没了：** 核应用音频源和静音状态，再逐步抬电平。
- **回放有回声：** 检查重复抓音和监听回灌。

### 假设与边界

只平衡两条已授权声音，不提供响度标准认证、多轨混音或真实观众体验验收。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/audio-mixer-guide)（英文，官方手册）— Audio Mixer 的推子与电平表用于控制各来源相对音量并观察接近削波的峰值。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when app sound buries your narration or the app is muted so the demonstration loses meaning. Adjust relative levels and prove in an actual short playback that speech is intelligible, app audio remains audible and peaks do not distort. Meter colors alone are not the listener's experience.

### Preparation and inputs

Prepare harmless narration and the loudest permitted app sound likely in the demo. Confirm one capture path each. Inspect microphone input gain first; a fader cannot undo clipping already at the device. Use headphones for playback to avoid speaker bleed.

### Execution

1. Speak and play app audio while inspecting relative mixer levels and peaks for both sources.
2. Correct overly hot device or source input, then use OBS faders for speech priority without losing app sound.
3. Record a short test containing quiet speech, normal action and the loudest app sound, then listen on headphones.
4. If clipping or masking remains, adjust the responsible source and retest, then keep the successful mix.

### Success, common problems, and recovery

The real file gives intelligible narration and meaningful app sound with no obvious clipped peak in the loudest passage.

- **Voice distorts:** Reduce input gain rather than only the recording fader.
- **App absent:** Check app source and mute state before raising level.
- **Echo:** Inspect duplicate capture and monitoring feedback.

### Assumptions and limits

This balances two authorized sources, not loudness-standard certification, multitrack mixing or actual audience acceptance.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/audio-mixer-guide) — Audio Mixer faders and meters control relative levels and reveal peaks near clipping.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

