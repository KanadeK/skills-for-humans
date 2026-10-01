---
name: capture-only-the-owners-microphone-in-obs
description: "Human workflow to select an owned microphone for private OBS narration, check its meter and real test playback, and exclude unintended inputs."
---
# 在 OBS 只选本人话筒作为解说输入 / Capture Only the Owner's Microphone in OBS

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 本人话筒、明确同意的本人解说和私有测试目录 / Own microphone, self-consented narration and private test folder |
| Side effects / 现实副作用 | 短测文件里只有本人清楚可听的解说，没有错误设备 / Test file contains intelligible own narration from the intended device only |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你为自己应用的录屏加口头解说，OBS 可能抓错内建话筒、旧耳机或根本没收到输入。只选择本人正在用的一支话筒，成果是音量表随本人说话而动、实际短文件中语音清楚，没有其他人的声音。看表有动只能说明有信号，录后听才知道内容是否正确。

### 准备与输入

确认房间里没有未同意录入的人，试说一段无敏感示例词。检查 Settings Audio 的全局麦克风与场景 Audio Input Capture 是否重复使用同设备；决定只留一条采集路径，别让两条信号互相叠加。

### 执行

1. 在场景或全局音频设置里明确选择本人话筒设备，并关闭同设备的重复入口。
2. 说几句测试词，观察对应音量表随语音变化，不说话时明显回落。
3. 录一小段重开听，核语音来自正确设备、没有旁人话音或过载失真。
4. 保存场景/配置，正式录制前再核设备没有被系统切换。

### 完成、常见问题与恢复

真实短测文件中本人解说可听、来源单一且没有未经同意声音。

- **表没动：** 检查设备名称、系统权限和静音状态。
- **声音重影：** 查全局与场景是否双重抓同设备。
- **有旁人声音：** 停录并重新准备安静私有环境。

### 假设与边界

只处理本人有意解说，不录会议、他人声音或隐蔽音频，也不保证播客级音质。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/audio-sources)（英文，官方手册）— Audio Input Capture 可指定设备，全局设置中的同设备可能导致重复录制。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when narrating your own app recording and OBS might be listening to the wrong built-in mic, old headset or no input. Choose only the device you are using. Finish with meter movement from your speech and intelligible voice in an actual short file, without other people's voices. A moving meter proves signal, not correct recorded content.

### Preparation and inputs

Ensure no unconsenting person is audible and prepare harmless test speech. Inspect both Settings > Audio global mic and scene Audio Input Capture for the same device. Keep one capture path to avoid duplication.

### Execution

1. Select the owner's microphone in one scene or global audio location and disable duplicate use of that same device.
2. Speak a few test words and inspect the matching meter moving with voice and falling during silence.
3. Record and listen to a short file for correct device, no bystander voice and no overload distortion.
4. Keep the configuration and recheck device selection before the actual recording.

### Success, common problems, and recovery

The actual short recording contains intelligible self narration from one intended device and no unconsented voice.

- **Meter idle:** Inspect device name, system permission and mute.
- **Voice doubles:** Inspect global and scene duplicate capture.
- **Bystander heard:** Stop and prepare a private environment before retrying.

### Assumptions and limits

This covers deliberate self narration, not meetings, other people's voices or covert audio, and does not promise podcast-level sound.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/audio-sources) — Audio Input Capture chooses a device; the same device globally can create duplicate capture.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

