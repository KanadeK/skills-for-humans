---
name: export-an-audacity-label-list-with-checked-times
description: "Human-readable Audacity 4 label-track text export with name and timestamp checks against the project, without exporting audio."
---
# 从 Audacity 导出标签文字并核对时点 / Export an Audacity Label List with Checked Times

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有两个以上本人命名标签的 `.aup4`、独立文本路径 / .aup4 with at least two self-named labels and separate text destination |
| Side effects / 现实副作用 | 时间标签成为可校对文字清单，音频未导出 / Labels become checked text list without exporting audio |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已在 Audacity 项目里给几处段落打了名字，想把时间点和名字交给自己下次查找时使用本篇。成果是独立的标签文字文件，至少两个名称与起止时间能和项目对应；音频样本没有因此导出。它不同于导出选区音频，输出是索引而非可播放文件。

### 准备与输入

保存 `.aup4`，先在标签轨检查至少两项的文字、顺序与实际音频对应。选择独立文本路径与清楚文件名；不要把标签里包含的私人姓名无意带出。记录第一个和最后一个标签时间供核对。

### 执行

1. 使用 File > Export other > Export labels 或标签轨同名菜单，确认输出是文本。
2. 保存后打开实际文本文件，核至少两条名称、起止时间和顺序。
3. 回 Audacity 点击相应标签重听，核文本时间不是旧版本遗留。
4. 若文本缺标签或顺序错，先在项目里修标签再重新导出；音频原样保留。

### 完成、常见问题与恢复

标签文字清单与项目时间对应，音频主本未改变或泄露。

- **导出了音频：** 取消并选 Export labels。
- **标签名旧：** 回项目核/改后重导。
- **私人信息混入：** 删除不合格文本并修标签。

### 假设与边界

这里只导出项目标签索引，不证明转写准确或许可共享。你负责文本披露范围。

### 来源

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/menu-bar/export-menu/)（英文，官方手册）— File > Export other 可导出标签文本，项目与音频不变。
- Original synthesis — 将一个音频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an Audacity project already has named regions and you need their names and times as a separate text index for later work. Finish with a label text file whose at least two names and boundaries match project, while no audio is exported by this action. Unlike excerpt export, output is an index, not playable sound.

### Preparation and inputs

Save `.aup4`, inspect at least two labels for wording/order against real audio. Choose a separate text path/name and remove private names that should not leave project. Note first and last label times for verification.

### Execution

1. Use File > Export other > Export labels or label-track equivalent, confirming text output.
2. Open resulting text file and check at least two names, start/end times and order.
3. Return to Audacity labels and replay to confirm text times are current.
4. If list is incomplete or stale, correct project labels and export again, leaving audio untouched.

### Success, common problems, and recovery

Text label list matches project timing and audio master remains unchanged/not exported.

- **Audio exported:** Cancel and choose labels export.
- **Names stale:** Update labels and re-export.
- **Private info included:** Discard bad text and sanitize labels.

### Assumptions and limits

This exports a project label index, not proof of transcription or permission to share. You own text disclosure.

### Sources

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/menu-bar/export-menu/) — File > Export other writes label text while project/audio remain unchanged.
- Original synthesis — one audio-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Audacity controls. You choose the content, perform the steps and verify the result.

