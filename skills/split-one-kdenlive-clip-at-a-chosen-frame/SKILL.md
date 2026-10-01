---
name: split-one-kdenlive-clip-at-a-chosen-frame
description: "Human-readable Kdenlive Razor/Cut at one known frame so a shot becomes two independent adjacent pieces without lost frames."
---
# 在 Kdenlive 指定帧把一段素材切成两段 / Split One Kdenlive Clip at a Chosen Frame

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已保存工程、时间线一段镜头、可辨的剪切帧 / Saved project, one timeline clip and identifiable cut frame |
| Side effects / 现实副作用 | 镜头变两段而帧序连续 / One clip becomes two adjacent pieces with frame order intact |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你要在一段自有 Kdenlive 镜头的一个准确动作转换帧把它分为两段，便于以后单独调前后部分时使用本篇。成果是两段相邻、内容没有被删、总时长不变，音频如果联动也在同帧保持同步。它不是把中间坏片直接移除。

### 准备与输入

保存工程，逐帧定位动作转换点，记下时间码及左右各一帧画面。选中正确片段/轨道，核视频和音频是否为一组；若还有其它轨道相同时间码，不要无差别切它们。

### 执行

1. 把播放头放在选定帧，用 Cut Clip 或 Razor 在目标片段上切一次。
2. 核出现左右两段，画面总时长、首末帧和顺序不变。
3. 试听/看切口前后，检查关联音频也保持同步、没有黑帧。
4. 误切别轨或多次切就撤销回一段重新做，保存重开。

### 完成、常见问题与恢复

两段可分别选中、帧序不断、时间不变、关联声画同步。

- **误切别轨：** 撤销并锁/选正确轨。
- **出现一帧黑：** 核边界是否留隙。
- **音频没切：** 核分组与关联方式。

### 假设与边界

只按一帧切开一段素材，不删除或重排故事。你负责帧位判断。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/editing.html)（英文，官方手册）— Razor 或 Cut Clip 能在播放头指定帧切开选中片段。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one owned Kdenlive shot needs a split at a precise action-change frame for separate later treatment. Finish with two adjacent pieces, no frames removed, same total duration and linked audio cut in sync if present. This is not removing a bad middle passage.

### Preparation and inputs

Save project, locate action-change frame and note timecode plus neighbouring frames. Select correct clip/track and inspect video/audio grouping. Do not indiscriminately cut unrelated tracks at same time.

### Execution

1. Place playhead on chosen frame and use Cut Clip or Razor once on target.
2. Confirm two adjacent pieces and unchanged overall duration, first/last frame and order.
3. Preview around cut and check linked audio sync and no black frame.
4. Undo wrong-track or multiple cuts to original clip and retry, then save/reopen.

### Success, common problems, and recovery

Two pieces select independently, frame order stays continuous, duration unchanged and linked A/V synced.

- **Wrong track cut:** Undo and target right track.
- **Black frame:** Inspect gap at cut.
- **Audio unsplit:** Check grouping/link state.

### Assumptions and limits

This splits one clip at one frame; it does not delete or reorder story. You choose frame.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/editing.html) — Razor or Cut Clip splits selected clip at playhead frame.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

