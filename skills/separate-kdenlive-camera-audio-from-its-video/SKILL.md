---
name: separate-kdenlive-camera-audio-from-its-video
description: "Human-readable Kdenlive ungroup of one linked camera A/V clip for independent audio treatment, with sync markers and source preservation."
---
# 把 Kdenlive 一段同期声与画面拆开单独编辑 / Separate Kdenlive Camera Audio from Its Video

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 含本人获准同期声的视频片段、已保存项目、一个明确音频处理目的 / Video clip with permitted camera sound, saved project and one audio-edit purpose |
| Side effects / 现实副作用 | 声画可单独选，原同步点仍可核 / Audio and picture select separately with sync cue retained |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一段自有视频有同期声，想只调声音而不改变画面时使用本篇。成果是声画在时间线上能分别选中、原始起点和可听可见提示仍对齐，原媒体未被分文件改写。拆组后更容易错位，所以不把“能单独点到”就当完成。

### 准备与输入

保存工程，找到一个声画共同事件，如拍手或门关声，记下时间码。确认视频与音频原本成组、没有别的片段被一起选中。规划要改的只是声音电平或淡变，不为了拆组去删除原同期声。

### 执行

1. 只选这一段关联声画，使用 Ungroup Clips 解除组。
2. 分别点视频与音频，核另一部分未跟着移动或消失。
3. 播放共同提示点，核画面动作与声响仍在同一时间附近。
4. 保存重开，若误移音频，撤销或按提示点对齐，必要时重新成组。

### 完成、常见问题与恢复

声画可单独编辑、同步提示仍合拍、原源文件在。

- **选不到音频：** 核是否存在音轨及组状态。
- **声音先于画面：** 撤销移动并按共同提示对齐。
- **其它片段也拆：** 撤销并缩小选择。

### 假设与边界

只拆一段获准同期声以便普通编辑，不保证长素材无漂移或专业对口型。你负责同步核查。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/grouping.html)（英文，官方手册）— Ungroup Clips 可解除自动关联，使视频和音频分别编辑。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an owned camera clip's sound needs treatment without moving picture. Finish with audio and video separately selectable on timeline but original starts and a visible/audible cue still aligned; source media is not rewritten. Ungrouping increases desync risk, so independent selection alone is not success.

### Preparation and inputs

Save project and locate a shared audiovisual cue such as clap or door close, noting timecode. Confirm A/V are grouped and no other clips selected. Plan audio-only treatment such as level/fade; do not delete source sound merely to ungroup.

### Execution

1. Select only this A/V pair and use Ungroup Clips.
2. Select video and audio separately, checking the other remains.
3. Play shared cue and verify picture action and sound still coincide.
4. Save/reopen; undo or realign any moved audio at cue and regroup if appropriate.

### Success, common problems, and recovery

A/V edit independently yet shared cue stays synchronized and original source remains.

- **Audio not selectable:** Check audio track and grouping.
- **Audio leads picture:** Undo and align cue.
- **Other clips ungrouped:** Undo and select only pair.

### Assumptions and limits

This ungroups one permitted camera sound for ordinary work, not long-run drift or professional lip-sync guarantee. You verify synchronization.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/grouping.html) — Ungroup Clips separates associated picture/audio for individual editing.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

