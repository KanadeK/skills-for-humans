---
name: set-audacity-spoken-word-loudness-for-one-target
description: "Human-readable Audacity 4 loudness normalization of owned spoken audio to one stated destination target, with peak and intelligibility checks."
---
# 按一个目标调整 Audacity 自录讲话响度 / Set Audacity Spoken-Word Loudness for One Target

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已完成剪辑的本人普通讲话 `.aup4`、接收方给出的响度目标 / Finished self-spoken ordinary .aup4 and recipient loudness target |
| Side effects / 现实副作用 | 整体响度更接近目标而词句仍易听 / Overall loudness approaches target while speech remains intelligible |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已剪完本人非敏感讲话，有接收方明确给出的响度目标，想让整段听起来接近该口径时使用本篇。成果是对指定范围做一次响度归一化后，输出仍无破音、轻声词可辨。它与峰值 Normalize 不同；没有接收目标时不编造一个所谓全球标准。

### 准备与输入

保存 `.aup4`，核源声已经删掉不必要尖峰且语义完整。记录接收方单位与目标（例如本机对话框实际支持的 LUFS/RMS 口径），不要混淆峰值 dBFS。确认只选最终讲话轨，不含静音原备份或背景音。

### 执行

1. 打开 Loudness Normalisation，按接收方口径输入目标而不是凭感觉套数值。
2. 只对选定最终讲话范围应用一次，检查处理后最响处是否有削波提示。
3. 试听轻声、正常、较响三处，判断是否更一致且文字不被压缩得生硬。
4. 导出预览重开，若偏差明显回项目修源动态或目标，不重复多次归一化。

### 完成、常见问题与恢复

响度目标与单位明确，实际输出可听且无新增破音；无法核目标时停止声称达标。

- **仍有尖峰破音：** 回源处理峰值，不盲加响度。
- **声音被压扁：** 减少处理或核原动态。
- **单位搞混：** 重查接收规范与对话框。

### 假设与边界

只面向一段本人讲话与一个已给定口径，不保证广播平台验收或听力安全。你负责最终监听。

### 来源

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/effects/volume-and-compression/loudness-normalisation/)（英文，官方手册）— Loudness Normalisation 按感知响度目标处理，与峰值 Normalize 不同。
- Original synthesis — 将一个音频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill after editing your own non-sensitive spoken piece when a destination gives a specific loudness target. Finish with one normalization pass on the intended range and an output without distortion where quiet words remain intelligible. This differs from peak Normalize; without destination guidance do not invent a universal target.

### Preparation and inputs

Save `.aup4`, check source meaning and stray peaks first. Record destination's unit/target using what this dialog actually supports (such as LUFS/RMS), not peak dBFS. Select final speech only, excluding muted backup or backing audio.

### Execution

1. Open Loudness Normalisation and enter destination-specified measure/target rather than a guessed number.
2. Apply once to selected final speech and inspect loudest parts for clipping indication.
3. Listen to soft, normal and loud words for intelligibility and unnatural flattening.
4. Reopen preview export; for poor result revisit source dynamics/target instead of repeated normalization.

### Success, common problems, and recovery

Target and unit are explicit, actual output intelligible without new distortion; no compliance claim when target cannot be checked.

- **Peaks clip:** Address source peaks first.
- **Speech flattened:** Back off and inspect original dynamics.
- **Units confused:** Recheck destination spec and dialog.

### Assumptions and limits

This treats one self-spoken piece against a supplied target, not platform acceptance or hearing safety. You listen to final output.

### Sources

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/effects/volume-and-compression/loudness-normalisation/) — Loudness Normalisation targets perceived level rather than peak alone.
- Original synthesis — one audio-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Audacity controls. You choose the content, perform the steps and verify the result.
