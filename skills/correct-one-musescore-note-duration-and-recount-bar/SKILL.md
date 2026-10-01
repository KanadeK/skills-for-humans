---
name: correct-one-musescore-note-duration-and-recount-bar
description: "Human recovery for one wrong note value in an original score, checking how the change affects following rests, notes and complete bar duration."
---
# 修正 MuseScore 一个音的时值并重数小节 / Correct One MuseScore Note Duration and Recount the Bar

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 本人节奏计划和一个时值有误的已保存小节 / Self-authored rhythm plan and saved bar with one wrong value |
| Side effects / 现实副作用 | 目标音时值正确且整小节拍数重新核实 / Corrected note value with bar total recounted |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一小节原创旋律中，一个音应更长或更短，但当前记谱与纸上节奏不一致。只修这一音并重数整小节，避免软件自动用休止填空或挤走后续音后看起来仍像一小节。结果是目标音和前后节奏共同符合原计划；若原计划本身加总有错，先修计划。

### 准备与输入

保存 .mscz，用拍号逐个列出目标小节现有音符和休止的时值，标出待改音以及改变后多出或减少的拍数。确认不是需要延音线跨小节，而只是本小节内时值输入错误。

### 执行

1. 选中唯一目标音并记录其原拍位，在编辑模式改为计划的时值。
2. 观察同小节剩余休止和音是否变化，按拍数重新数完整小节而非只看目标音的符尾。
3. 播放目标小节及下一小节开头，核后续音没有被意外提前、延后或替换。
4. 与原计划逐项对照后保存；若改动牵连太多，撤销回保存稿并分步重输该小节。

### 完成、常见问题与恢复

目标音时值符合计划，前后事件顺序不变，小节总拍数与拍号一致。

- **出现多余休止：** 核这是否软件填补空拍，再与计划决定保留或重输。
- **后音被覆盖：** 撤销并分段重输，先保证后音位置。
- **小节仍不满：** 从第一拍重数所有音和休止，不靠视觉宽度判断。

### 假设与边界

只修一处普通单声部节奏错误，不讨论复杂连音、复合拍的重分组或跨声部改时值。

### 来源

- [MuseScore Studio Handbook](https://handbook.musescore.org/basics/editing-notes-and-rests)（英文，官方手册）— 编辑音符和休止可更改已有音的时值，可能影响邻近拍位，需复核。
- Original synthesis — 将一个原创记谱结果、原稿对照和失败停点组合为可核流程。

## English

Use this when one note's value in your original bar differs from a written rhythm plan. Correct that value and recount the entire measure, rather than assuming automatic rest filling or shifted neighbors kept the intended rhythm. The result is a bar in which target and surrounding events match the plan. If the plan itself has the wrong total, revise the plan first.

### Preparation and inputs

Save the .mscz and list each note and rest value in the bar against its time signature. Mark the target and how many beats the change adds or removes. Confirm the issue is a value within this measure rather than a sustained pitch needing a tie across the barline.

### Execution

1. Select only the target note, note its original beat and set its planned duration in editing mode.
2. Inspect remaining notes and rests and recount the complete measure, not merely the target's flag or stem.
3. Play the target bar and start of the next, checking no later note moved or was replaced unexpectedly.
4. Compare each event with the written plan and save. If too much changed, undo to the saved state and reenter the bar in smaller steps.

### Success, common problems, and recovery

The target duration matches the plan, surrounding event order remains correct and the bar totals match its meter.

- **Extra rest:** Check whether it fills freed time, then reconcile it with the plan.
- **Following note lost:** Undo and reenter the passage in small steps, preserving later position.
- **Bar incomplete:** Recount every duration from beat one rather than judging horizontal spacing.

### Assumptions and limits

This fixes one simple single-voice rhythm error, not complex tuplets, compound-meter beaming or cross-voice duration editing.

### Sources

- [MuseScore Studio Handbook](https://handbook.musescore.org/basics/editing-notes-and-rests) — Editing notes and rests changes existing durations and requires checking surrounding rhythm.
- Original synthesis — one original notation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain MuseScore controls. You choose the content, perform the steps and verify the result.

