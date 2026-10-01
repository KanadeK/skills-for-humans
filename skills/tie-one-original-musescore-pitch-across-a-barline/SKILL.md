---
name: tie-one-original-musescore-pitch-across-a-barline
description: "Human workflow to tie two same-pitch notes across a barline in an original score, checking total duration and avoiding a slur."
---
# 把 MuseScore 同一音高跨小节延成一音 / Tie One Original MuseScore Pitch across a Barline

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 跨小节保持同音的本人节奏计划和已保存谱 / Original plan for one sustained pitch across a barline and saved score |
| Side effects / 现实副作用 | 两音同高以延音线连成一个发音时长 / Same-pitch notes joined as one sustained duration |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一句原创旋律有一个音要从小节末持续到下一小节开头，若重新发音会改变节奏意图，就添加延音线。完成后两端是同音高、总时值等于计划，谱面和试听都指向一次持续发音。外形相似的连奏线表达不同音乐意思，不能因为它更容易选到就代用。

### 准备与输入

保存工程，先在纸上写跨线前后各需多少拍、音名和八度。确认两小节拍数本来完整；若后半音高不同，先改音高或承认这不是延音。退出可能会连续输入新音的模式，定位小节线两边目标。

### 执行

1. 选第一音并确认下一小节目标音同高；若第二音尚不存在，按计划时值创建它。
2. 使用延音线命令连接这两个音，而不是添加跨多个不同音的连奏线。
3. 放大核弧线起止正落在两个同高音上，逐小节重数拍数；播放听是否出现意外再发音。
4. 保存并重开核延音仍存在，若发音仍断，查是否错选音或两个音的升降状态不同。

### 完成、常见问题与恢复

两个同高音被延音线跨小节连接，时值总和正确，没有误用连奏线。

- **弧线连到不同音：** 删错线并核两个音的实际音高。
- **多出第二次起音：** 确认是 tie 而不是 slur，查播放设置。
- **小节超拍：** 改两边音符时值，不靠移动弧线掩盖。

### 假设与边界

本篇只处理相邻小节的一处普通延音，不讨论跨反复、跨声部或特殊乐器的延音解释。

### 来源

- [MuseScore Studio Handbook](https://handbook.musescore.org/basics/entering-notes-and-rests)（英文，官方手册）— 延音线只连接同音高并合并演奏时值，区别于连奏线。
- Original synthesis — 将一个原创记谱结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a note in your own phrase must continue from one bar into the next without a second attack. The result is two same-pitch written values whose total matches the plan and whose tie communicates one sustained sound. A visually similar slur conveys a different musical meaning and should not stand in for the tie.

### Preparation and inputs

Save and write the required durations before and after the barline, plus pitch and octave. Confirm both bars are rhythmically complete. If the second pitch differs, fix it or recognize this is not a tie. Locate exact notes on both sides.

### Execution

1. Select the first note and verify the next-bar target is the same pitch; create the second value if it does not yet exist.
2. Use the tie action for those notes, not a phrase slur across different pitches.
3. Inspect tie endpoints at high zoom, recount both bars and listen for an unintended second attack.
4. Save and reopen to confirm the tie persists; if sound still breaks, check selection and the effective accidental on each note.

### Success, common problems, and recovery

Two same-pitch notes are tied across the barline with correct combined value and no slur substituted.

- **Different pitches:** Remove the wrong line and verify effective pitch of both notes.
- **Second attack:** Confirm tie type rather than slur and inspect playback.
- **Bar overfull:** Correct durations on both sides instead of moving the arc visually.

### Assumptions and limits

This handles one ordinary tie over adjacent bars, not ties across repeats, voices or specialized instrument interpretation.

### Sources

- [MuseScore Studio Handbook](https://handbook.musescore.org/basics/entering-notes-and-rests) — A tie links same-pitch notes into one sustained duration, unlike a slur.
- Original synthesis — one original notation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain MuseScore controls. You choose the content, perform the steps and verify the result.

