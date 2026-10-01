---
name: duplicate-an-audacity-track-for-before-after-listening
description: "Human-readable duplicate-track setup in Audacity 4 for one owned recording, with original muted/unmuted comparison and no accidental double playback."
---
# 复制 Audacity 音轨留一份前后对照 / Duplicate an Audacity Track for Before-After Listening

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已保存 `.aup4`、一条自有音轨和即将尝试的一项编辑 / Saved .aup4, owned audio track and one planned edit |
| Side effects / 现实副作用 | 原轨与工作轨可切换对照，不会同时叠加误判 / Original and work tracks can be compared without accidental summing |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你要在 Audacity 做一次可能改变声音的编辑，又想随时听原轨时使用本篇。成果是原轨和复制的工作轨分开命名、可以单独播放比较，避免两轨同时响让声音假变大。它只建立对照结构，不宣称编辑已经改善音质。

### 准备与输入

保存 `.aup4`，确认目标音轨没有隐含私密内容，记下原轨名称与时长。选择整条正确轨道，不只选片段或标签轨。拟好“原始”“工作”的名字；复制轨道会增加项目体积，不代替原文件备份。

### 执行

1. 在目标轨道菜单选择 Duplicate，核多出一条同长度轨道。
2. 把两轨分别命名，工作时只选择工作轨作为效果目标。
3. 用 Mute 或 Solo 轮流试听同一短段，确认每次只听一轨且复制前两者声音相同。
4. 保存重开，若两轨同时响使音量变大，先改静音状态再评价编辑。

### 完成、常见问题与恢复

原轨未改、工作轨独立，单轨对照方法已核，未把双轨叠声当改善。

- **只有片段被复制：** 核是否用了轨道 Duplicate。
- **声音突然变大：** 两轨可能同放，核 Mute/Solo。
- **编辑误落原轨：** 撤销并选工作轨。

### 假设与边界

轨道对照不证明人耳偏好或技术质量。你负责只在获准音频上编辑与保存。

### 来源

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/menu-bar/tracks/)（英文，官方手册）— Tracks 菜单可复制轨道；复制后可用 Mute/Solo 对照。
- Original synthesis — 将一个音频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill before one sound-changing Audacity edit when the original must remain auditionable. Finish with named original and duplicated work tracks that can be played separately, avoiding simultaneous playback that falsely sounds louder. This sets up comparison without claiming the edit improved audio.

### Preparation and inputs

Save `.aup4`, confirm target track is permitted and note original name/duration. Select the correct complete audio track, not a label track or one clip by accident. Plan names like Original and Work; duplicating increases project size and is not external backup.

### Execution

1. Use Duplicate in target track menu and confirm one same-length audio track appears.
2. Name both tracks and select only work track for later effects.
3. Mute/Solo alternately on same short passage, confirming one track at a time and identical starting sound.
4. Save/reopen. If both play and sound louder, correct mute state before judging changes.

### Success, common problems, and recovery

Original is unchanged, work track independent, single-track comparison checked, and double playback is not mistaken for improvement.

- **Only clip copied:** Use track Duplicate.
- **Suddenly louder:** Check both tracks aren't playing.
- **Original edited:** Undo and target Work.

### Assumptions and limits

Track comparison does not prove listening preference or technical quality. You edit/save only permitted audio.

### Sources

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/menu-bar/tracks/) — Tracks menu duplicates a track and Mute/Solo enable comparison.
- Original synthesis — one audio-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Audacity controls. You choose the content, perform the steps and verify the result.

