---
name: export-and-check-one-kdenlive-srt-subtitle-file
description: "Human workflow to export an existing Kdenlive subtitle track as SRT and inspect cue order, timestamps, text and privacy before sharing the file."
---
# 从 Kdenlive 导出并核对一份 SRT 字幕文件 / Export and Check One Kdenlive SRT Subtitle File

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 有已校时字幕轨的获准工程、文本查看器和本地输出目录 / Permitted project with timed subtitle track, text viewer and local output folder |
| Side effects / 现实副作用 | 一份可打开、时间顺序正确且内容经核对的本地 SRT / One locally saved, readable SRT with reviewed cue order and wording |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你已有校过的字幕轨，需要给协作者一份独立文字字幕文件时，执行这个导出流程。目标是一份实际存在的 SRT，时间码依序递增、文字不缺段、没有私人信息。这个文件与视频画面是两个产物；导出成功也不代表字幕已经烧录或嵌入视频。

### 准备与输入

先保存工程，在字幕轨从头到尾试听和检查，确认要导出的是当前正确轨道及语言。选择只有项目参与者可访问的本地目录，准备能读取纯文本的查看器；如果同工程存在多个字幕文件，先明确本次要交的那一份。

### 执行

1. 在 Kdenlive 的字幕导出入口选择现有字幕轨，明确选择 SRT 格式和目标文件名，避免把同名旧文件误认成新结果。
2. 完成导出后在文件管理器确认新文件存在且时间有更新，用纯文本查看器打开，检查第一条、最后一条和中间几条。
3. 核对序号、起止时间码递增、每条结束晚于开始、原文无乱码；发现缺漏回到工程字幕轨修改后再导出。
4. 把 SRT 与原始短片的相同片段对齐试听，记录它对应哪个视频版本；交付前再检查人名、地址等不应外传的信息。

### 完成、常见问题与恢复

目标目录里有能直接读取的 SRT；抽查与整段回看均显示时码、原话和视频版本对应，无意外私人内容。

- **文字乱码：** 确认导出与查看器的字符编码；回工程核原文再导出。
- **时码不对：** 核对所选轨道及视频版本，改工程里的字幕时点，勿只改交付副本。
- **文件是旧版：** 用明确版本文件名重导并核修改时间与首尾内容。

### 假设与边界

只核对一份既有字幕轨的 SRT 导出；不提供转写、翻译、字幕嵌入或平台上传。实际可用格式和编码会随版本变化；如导出入口或结果与手册不同，以安装版本的可见输出核实。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/subtitles.html)（英文，官方手册）— 官方字幕工具支持把现有轨道导出为 ASS 或 SRT 文件。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a timed subtitle track already exists and a collaborator needs a separate text subtitle file. Produce an actual SRT whose cues increase in time, whose words have no missing passage and whose content contains no unintended private information. The file and a rendered video are separate deliverables; exporting text does not burn or embed it into the image.

### Preparation and inputs

Save the project and review the subtitle track against the recording from beginning to end. Confirm the intended language and active subtitle file, especially if the project contains several. Choose a local folder accessible only to project participants and a plain-text viewer to inspect the result.

### Execution

1. Use Kdenlive's subtitle export action for the existing track, select SRT and a clear destination name so an older same-named file cannot be mistaken for the result.
2. Confirm the new file exists and has a current modification time, then open it in a text viewer and inspect first, last and several middle cues.
3. Check sequential cue numbers, increasing start/end times, each end after its start and clean readable wording. Correct omissions in the project track, then export again.
4. Play matching passages with the source video and record which video version this SRT fits. Check for names, addresses or other content that should not leave the project before sharing.

### Success, common problems, and recovery

The destination holds a readable SRT; spot checks and full playback link cue timing and words to the intended video version without unintended private content.

- **Mojibake:** Check export and viewer encoding; verify original text in the project and export again.
- **Wrong times:** Check selected subtitle file and video version; fix timing in the project, not only in a delivery copy.
- **Stale file:** Export under a clear versioned name and confirm modification time plus first and last cues.

### Assumptions and limits

This checks one existing subtitle track's SRT export, not transcription, translation, subtitle embedding or upload. Available formats and encoding can vary by installed version; verify the visible output when its interface differs from the manual.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/subtitles.html) — The official subtitle tool exports the existing track as ASS or SRT.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.
