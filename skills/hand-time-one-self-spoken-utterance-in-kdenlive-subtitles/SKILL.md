---
name: hand-time-one-self-spoken-utterance-in-kdenlive-subtitles
description: "Human procedure to transcribe and time one clear self-spoken line on Kdenlive's subtitle track, checking accuracy and readability without claiming automated recognition."
---
# 给 Kdenlive 中一句本人说的话手动配准字幕 / Hand-Time One Self-Spoken Utterance in Kdenlive Subtitles

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 含一段清晰本人话音的获准工程、耳机和待核文字 / Permitted project with one clear self-spoken line, headphones and draft wording |
| Side effects / 现实副作用 | 一条与话音相符且不遮关键信息的定时字幕 / One timed subtitle matches speech without covering key visual information |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你只需为自有短片中一句本人亲口说的话补上可读文字时，用这个流程完成一条字幕。成果是起止时间贴合听到的话音、用词与原话一致且画面里能读清的一条字幕。先听再写，不能凭印象把语气改成另一层意思，也不要把自动转写当成核实。

### 准备与输入

打开已保存且获准的工程，戴耳机反复听该句话，先记准确原文、语气词及需要保留的停顿。记下大致起止帧；若多人同时说话、音频含私人信息或难以听清，先停下处理授权或清晰度，勿猜测别人说的话。

### 执行

1. 在时间线找到这句话，把播放头移到第一处可听语音，打开字幕轨或字幕窗口并新增一条字幕。
2. 逐字输入核过的原话，用短句和自然断行保持可读；不要改写事实或补充画面外没有说出的内容。
3. 把字幕开始和结束贴近说话实际区间，逐帧播放开头与结尾，避免比声音先出现太久或人还没说完就消失。
4. 在项目监视器正常播放一次，核声音、文字与画面位置；保存工程并重开这段，确认字幕仍在正确时点。

### 完成、常见问题与恢复

同一句话在播放时与一条可读字幕同步出现，文字与本人原话相符，邻近镜头没有被误加字幕。

- **听不清词：** 暂停并回听源音；仍听不清就删去或标明不确定，别自行编词。
- **字幕太早或太晚：** 对照首尾可听音重新拖动字幕边缘，再以正常速度复听。
- **字挡住主体：** 调可用位置或缩短断行，同时检查小屏幕预览。

### 假设与边界

本篇只处理一条本人话音；口音、翻译、多人辨识和无障碍字幕规范都需另行核。保存字幕轨不等于渲染视频或导出 SRT；公开发布前还要做完整检查。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/subtitles.html)（英文，官方手册）— 字幕工具支持在专用字幕轨和字幕窗口中创建、编辑和校时。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an owned short video needs one accurate caption for a line you spoke yourself. The outcome is one subtitle whose start and end follow the audible utterance, whose words match it, and whose placement remains readable in the frame. Listen before typing; a convenient paraphrase or an unreviewed transcription is not evidence of what was said.

### Preparation and inputs

Open a saved permitted project and listen with headphones several times. Draft the exact words, including meaningful fillers or pauses, and identify approximate first and last audible frames. Stop for overlapping speakers, private content, or words you cannot hear clearly; do not guess another person's speech.

### Execution

1. Locate the utterance in the timeline, put the playhead at its first audible sound, open the subtitle track or Subtitle Window and add one entry.
2. Enter the checked words verbatim, using a short readable line break if needed. Do not rewrite facts or insert claims that were never spoken.
3. Set start and end near the actual speech interval. Play frame by frame at both edges so the caption neither arrives too early nor vanishes before speech ends.
4. Play once at normal speed in the project monitor to check sound, wording and screen position; save and reopen the passage to confirm the timing remains correct.

### Success, common problems, and recovery

The single caption appears with the same spoken line, matches your words, reads clearly and does not spill into adjacent footage.

- **Unclear word:** Pause and replay source audio; remove or flag uncertainty rather than inventing words.
- **Timing drifts:** Move subtitle edges against first and last audible sounds, then replay normally.
- **Text hides subject:** Adjust available placement or line breaks and check a small preview.

### Assumptions and limits

This covers one line spoken by you. Dialect interpretation, translation, speaker identification and formal accessibility standards need separate review. A saved subtitle track is not a rendered video or SRT export; inspect the whole work before publication.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/subtitles.html) — The subtitle tool creates and edits timed captions on a dedicated subtitle track or in the Subtitle Window.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

