---
name: mix-two-permitted-audacity-tracks-for-private-preview
description: "Human-readable non-destructive export preview of two owned Audacity 4 tracks, checking both components and peak headroom while keeping multitrack project."
---
# 把 Audacity 两条获准音轨混成一份私下预览 / Mix Two Permitted Audacity Tracks for Private Preview

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 两条获准且已对齐的短音轨、已保存 `.aup4`、私下试听 / Two permitted aligned short tracks, saved .aup4 and private playback |
| Side effects / 现实副作用 | 一份合成预览中两组件可辨，项目仍分轨 / Combined preview keeps both components audible while project remains multitrack |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有两条本人拥有或获准的短音轨，例如本人讲话和自制轻背景声，想听一份合在一起的私下预览时使用本篇。成果是导出文件能听到两者且讲话不被盖住、没有新削波，`.aup4` 项目仍保留两条可独立调的轨道。不要把合成声当单次原始现场录音。

### 准备与输入

保存 `.aup4`，确认两条素材的许可、时间对齐和一个主要/次要关系。静音不应进入成品的原备份轨，先试听最响叠加处。若两轨内容会误导真实对话或身份，就停止。

### 执行

1. 分别单独听两轨，再同时播放，调整轨道级音量让主声始终可辨。
2. 看最响叠加处电平，没有削波或明显盖声。
3. 使用 Export full project audio 做独立私下预览，重开文件从头中尾试听两组件。
4. 确认 `.aup4` 仍分轨可调；不满意回项目改平衡后重导，勿只改扁平文件。

### 完成、常见问题与恢复

合成预览里两声源层次清楚、无新削波，主项目仍分轨且来源可辨。

- **背景盖讲话：** 降低背景轨音量。
- **导出有原轨叠加：** 核备份轨静音状态。
- **峰值削波：** 减小轨道总输出再重导。

### 假设与边界

只做两条合法素材的私人预览，不发布、不制造假对话，也不保证专业混音或听力安全。

### 来源

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/menu-bar/export-menu/)（英文，官方手册）— 导出会按播放状态把音轨混成副本，项目分轨不被扁平化。
- Original synthesis — 将一个音频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when two short owned or permitted tracks, such as your speech and self-made soft background, need a private combined preview. Finish with both audible, speech not masked, no new clipping, and `.aup4` still holding two adjustable tracks. Do not present the mix as one unedited field recording.

### Preparation and inputs

Save `.aup4`, confirm rights, timing and lead/background roles. Mute any backup track that should not export. Listen where both overlap loudest. Stop if the combination would misrepresent a real conversation or identity.

### Execution

1. Solo each track, then play together and adjust track levels so lead stays clear.
2. Inspect combined loudest passage for clipping or masked speech.
3. Export full project audio as separate private preview and reopen it, checking both components at start/middle/end.
4. Confirm `.aup4` remains multitrack; revise balance there and re-export rather than editing only flat file.

### Success, common problems, and recovery

Both sources remain audible with clear hierarchy and no new clipping, while project tracks and provenance remain.

- **Background masks voice:** Lower backing track.
- **Backup also mixed:** Mute source backup.
- **Mix clips:** Lower summed level and re-export.

### Assumptions and limits

This is a private preview of two permitted sources, not publication, fake dialogue, professional mixing or hearing-safety assurance.

### Sources

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/menu-bar/export-menu/) — export renders playback mix as a copy while project tracks remain separate.
- Original synthesis — one audio-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Audacity controls. You choose the content, perform the steps and verify the result.
