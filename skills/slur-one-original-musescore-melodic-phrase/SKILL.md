---
name: slur-one-original-musescore-melodic-phrase
description: "Human workflow to mark one multi-note original phrase with a slur and verify its endpoints and interpretation separately from ties."
---
# 给 MuseScore 一句原创旋律加连奏线 / Slur One Original MuseScore Melodic Phrase

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 至少三音的原创旋律短句、已保存谱稿 / Original phrase of at least three notes and saved score |
| Side effects / 现实副作用 | 一条覆盖目标句而不吞邻句的连奏线 / One slur covering the intended phrase only |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一小句原创旋律需要提示演奏者把几个音连贯地处理，而不是将同音延成长音时，使用连奏线。成果是一条从计划首音到末音的乐句线，不多包后一句。它是演奏意图的标记，合成试听是否明显连奏会随乐器音源不同，最终仍要看谱面含义。

### 准备与输入

保存谱面，先在草案中标清句首句末和呼吸位置。检查句内确有多个音且不只是两个同高音的持续；选第一音时不要把整页或下一句一并选择，以免线跨度异常。

### 执行

1. 在正常模式选句首音，使用连奏线工具或命令创建弧线。
2. 把终点延到本句计划的末音，核弧线涵盖中间音却没有包进下句。
3. 正常比例和放大各看一次，核弧线不与歌词、延音线或其他记号混成不可读的一团。
4. 回听整句并对照原意，保存重开；如果其实要延长同音，删连奏线改用延音线。

### 完成、常见问题与恢复

连奏线准确从句首至句末，谱面能与延音线区别，后续乐句未被误括。

- **线跨太远：** 选线终端调整到本句末音。
- **误用了延音线：** 删错线，按多音乐句重新加 slur。
- **记号重叠：** 先核音乐范围，再轻微调布局，不拖离锚点。

### 假设与边界

只标一条普通原创乐句，不决定演奏法流派、呼吸技术或专业制谱的所有摆放规则。

### 来源

- [MuseScore Studio Handbook](https://handbook.musescore.org/notation/expressive-markings/slurs-and-ties)（英文，官方手册）— 连奏线可跨不同音高和多个音，用于乐句连奏表达，与延音线不同。
- Original synthesis — 将一个原创记谱结果、原稿对照和失败停点组合为可核流程。

## English

Use this when several notes in your original melody belong to one legato phrase, not a single held pitch. Finish with a slur from intended first to last note without swallowing the next phrase. This is notation of performance intent; synthetic playback may express it differently by instrument, so visual meaning matters.

### Preparation and inputs

Save and mark the phrase's first note, last note and breathing point in your own plan. Confirm it contains multiple notes rather than merely one pitch held across a bar. Select the starting note carefully, not the whole page or following phrase.

### Execution

1. Select the first phrase note in normal mode and add a slur with the line tool or command.
2. Extend the endpoint to the planned last note, covering the internal notes but not the next phrase.
3. Inspect at normal and enlarged scale so the arc does not collide confusingly with lyrics, ties or other markings.
4. Listen to the phrase against your intent, save and reopen. If the goal was a held same pitch, remove the slur and use a tie.

### Success, common problems, and recovery

The slur spans the intended phrase, is distinguishable from a tie and leaves the following phrase outside it.

- **Too long:** Adjust the slur endpoint to the actual last note.
- **Tie instead:** Remove the tie and add a slur to the multi-note phrase.
- **Markings collide:** Confirm musical span, then adjust layout slightly without detaching anchors.

### Assumptions and limits

This marks one ordinary original phrase; it does not decide school-specific technique, breath training or every professional engraving placement rule.

### Sources

- [MuseScore Studio Handbook](https://handbook.musescore.org/notation/expressive-markings/slurs-and-ties) — Slurs span phrase notes, possibly of different pitches, and differ in purpose from ties.
- Original synthesis — one original notation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain MuseScore controls. You choose the content, perform the steps and verify the result.

