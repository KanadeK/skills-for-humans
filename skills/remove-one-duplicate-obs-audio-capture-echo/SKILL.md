---
name: remove-one-duplicate-obs-audio-capture-echo
description: "Human recovery for one duplicated OBS microphone or app-audio capture path, retaining a single source and confirming the echo disappears in a local test file."
---
# 修复 OBS 同一声音被抓两次造成的重影 / Remove One Duplicate OBS Audio Capture Echo

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 可重现的回声或双音短测、已知声源列表 / Reproducible doubled-audio test and known source list |
| Side effects / 现实副作用 | 新短测中同一声音只出现一次且不丢目标音 / New test has one clean copy of target sound without dropping it |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在 OBS 私有测试片里听到本人声音或应用声像叠了两层，先检查是否同一设备通过全局设置和场景源被录两次。成果是只留计划的一条路径，新文件没有重影，目标声仍存在。回声也可能来自物理扬声器被话筒再次收音；如果不是双路径，先回实际声学链路查。

### 准备与输入

保存当前场景和 Profile 名称，在短测里标出重影的是话筒还是应用声。列出 Audio Mixer、Settings Audio 全局设备和每个场景音源，确认同一信号是否出现两次；不要一口气全静音导致无法区分。

### 执行

1. 让目标声单独发出，观察哪两个音量表同时响应，并暂时静音其中一条做短测。
2. 回放文件确认重影消失且目标声还在，再移除或禁用不需要的重复采集入口。
3. 再录一小段正常演示，核声画同步和其它必要音源没有因修复被误关。
4. 保存配置并记录唯一有效音频路径；若仍回声，检查扬声器与话筒物理串音。

### 完成、常见问题与恢复

新实际录像里同一目标声只听一次，音量表和配置能解释其唯一来源。

- **静音后也听不到：** 恢复该路，改查另一条或输出轨。
- **仍有回声：** 转查扬声器串音或监控回放回灌。
- **误关别的音：** 逐源恢复必要项，再短测。

### 假设与边界

只修一处重复采集回声，不进行复杂多轨混音、硬件维修或声学处理。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/audio-sources)（英文，官方手册）— 同设备在全局音频与场景源重复选择可能造成回声。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a private OBS test plays your voice or app sound as two layers. Inspect whether the same device is captured globally and again as a scene source. Finish with one intended path, no doubled sound in a new file and target audio still present. Echo can also be acoustic feedback from speakers into a microphone, so do not assume duplication without checking.

### Preparation and inputs

Record scene and Profile names and identify whether voice or app audio doubles. List Audio Mixer entries, Settings > Audio global devices and scene audio sources to see whether the same signal appears twice. Avoid muting everything at once, which hides the cause.

### Execution

1. Play only the target sound, identify two responding meters and temporarily mute one for a brief test.
2. Play back the file for a single clean sound, then disable or remove only the duplicate capture path.
3. Record a normal short passage to check sync and ensure other needed sources remain.
4. Keep the setup and note the single valid audio path; if echo remains, inspect speaker-to-microphone acoustic bleed.

### Success, common problems, and recovery

The new actual recording plays the target sound once, and meters plus settings identify its single source.

- **Sound vanishes:** Restore it and inspect the other path or output track.
- **Echo remains:** Inspect acoustic bleed or monitoring feedback.
- **Other audio lost:** Restore needed sources one at a time and retest.

### Assumptions and limits

This fixes one duplicated capture path, not advanced multitrack mixing, hardware repair or room acoustics.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/audio-sources) — Selecting the same audio device globally and in a scene can create echo.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

