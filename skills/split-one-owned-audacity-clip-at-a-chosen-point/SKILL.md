---
name: split-one-owned-audacity-clip-at-a-chosen-point
description: "Human-readable Audacity 4 split of one owned clip into two independently editable clips without deleting samples or changing timing."
---
# 在 Audacity 一个准确时点分开片段 / Split One Owned Audacity Clip at a Chosen Point

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已保存 `.aup4`、一条目标片段和可听到的分割点 / Saved .aup4, one target clip and audible chosen split point |
| Side effects / 现实副作用 | 一段成两段而内容时长不丢 / One clip becomes two without losing audio or duration |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在自有短录音中找到了一个自然停顿，要把一段分成两个可分别移动/裁剪的片段时使用本篇。成果是在准确时点出现两个片段，前后声音与总时长保持原样；这不是删掉错误句，也不是把两个音轨拆成左右声道。

### 准备与输入

保存 `.aup4`，先从停顿前后试听，选择真正适合断开的时间点，记录分割前片段名和时长。确认只选目标音轨/片段，关闭会影响其它轨道的多选。若分割点位于字中或音符中，应先移到自然边界。

### 执行

1. 把编辑光标放在选定点，使用 Split 工具或 Ctrl+I 等价命令。
2. 核原片段变为左右两段、时间轴长度和波形音频没有消失。
3. 分别点选两段，听边界附近的首尾声音是否完整。
4. 如果分割落在音中产生爆点，撤销并移到更自然的低能量/静音位置；保存重开。

### 完成、常见问题与恢复

两个独立片段顺序不变、时间与声音完整，分界可被重听支持。

- **分割太早：** 撤销并重选停顿。
- **别的轨也分了：** 撤销并缩小选择范围。
- **误删一段：** 撤销删除，只执行 Split。

### 假设与边界

只把一个自有片段分两段，不改变语义或授权范围。你负责挑选听觉边界。

### 来源

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/clips/split/)（英文，官方手册）— Split 在光标处把一个 clip 分成两个独立片段而不删除音频。
- Original synthesis — 将一个音频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an owned short recording has a natural pause and one clip should become two independently movable/trimmable clips. Finish with two clips at the intended point while audio and total duration remain intact. This is not removing a mistaken phrase or splitting stereo channels.

### Preparation and inputs

Save `.aup4`, listen around pause and choose a true boundary, noting old clip name and duration. Select only target track/clip and clear multiselection of other tracks. Move away from the middle of a syllable or note.

### Execution

1. Place edit cursor at chosen point and use Split tool or Ctrl+I equivalent.
2. Confirm left and right clips exist and timeline length/waveform audio has not vanished.
3. Select both separately and listen around boundary for complete sound.
4. Undo and choose a lower-energy pause if split causes a click, then save/reopen.

### Success, common problems, and recovery

Two independent clips retain order, timing and sound, with a listened boundary.

- **Split too early:** Undo and choose pause.
- **Other tracks split:** Undo and narrow selection.
- **Half deleted:** Undo delete and use Split only.

### Assumptions and limits

This divides one owned clip, not meaning or rights. You judge an audible boundary.

### Sources

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/clips/split/) — Split divides one clip at cursor into two independent clips without deleting audio.
- Original synthesis — one audio-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Audacity controls. You choose the content, perform the steps and verify the result.

