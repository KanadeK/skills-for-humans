---
name: add-one-original-accompaniment-instrument-to-musescore
description: "Human workflow to add one independent pitched instrument to an original solo score and enter a short self-authored accompaniment without changing the melody."
---
# 给 MuseScore 原创旋律增加一件伴奏乐器 / Add One Original Accompaniment Instrument to MuseScore

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 20–35 分钟 / 20–35 minutes |
| Requirements / 必要物品 | 已保存原创旋律、本人写的一小段简单伴奏节奏 / Saved original melody and self-authored simple accompaniment plan |
| Side effects / 现实副作用 | 主旋律不变、第二件乐器有独立可读声部 / Original melody unchanged with an independent readable accompaniment part |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有一段自己写的独奏旋律，想让另一件乐器按简单节奏伴奏时，在同一谱里增加独立乐器。结果是主旋律仍原样，第二声部有自己的谱表、音域和几小节原创内容，之后可生成独立分谱。不要把“增加同一乐器的第二谱表”当作自动获得第二位演奏者。

### 准备与输入

先保存并在纸上写伴奏乐器、音域、与旋律合拍的简单节奏。确定这真是第二件乐器而非同一键盘乐器的另一只手；若想让两行完全同步，也不是独立伴奏，应另选链接谱表方案。

### 执行

1. 打开 Layout 面板的 Add instrument，选定第二件有音高的乐器并核它出现在原旋律旁。
2. 核乐器名称、谱号和初始空小节，不在主旋律层上输入伴奏。
3. 按本人草案在第二谱表输入一小段伴奏，逐小节核节拍与主旋律对齐且音区可演奏。
4. 开关或单独试听声部，确认旋律原音未被改写；保存重开核两件乐器与内容仍在。

### 完成、常见问题与恢复

谱面有两件明确乐器和对齐的小节，原旋律保留、伴奏独立可选与修改。

- **加成同一乐器谱表：** 撤销并用 Add instrument 重新建立独立乐器。
- **旋律被覆盖：** 回保存稿恢复主声部，把伴奏重输到新谱表。
- **音区异常：** 核新乐器实际谱号和演奏范围，再改伴奏音高。

### 假设与边界

这里只新增一件简单伴奏乐器，不自动编配、不证明真实演奏者能照谱完成，也不处理移调乐器的复杂写实音转换。

### 来源

- [MuseScore Studio Handbook](https://handbook.musescore.org/notation/instruments-staves-and-systems/instruments-and-system-markings)（英文，官方手册）— Layout 面板可加乐器；新乐器与仅给同一乐器增加谱表不同。
- Original synthesis — 将一个原创记谱结果、原稿对照和失败停点组合为可核流程。

## English

Use this when your original solo melody needs a simple independently performed accompaniment. Add a second instrument, leaving the melody intact, and enter a few measures from your own accompaniment plan on its staff. A second staff of the same instrument is not automatically a separate player's part.

### Preparation and inputs

Save and write the accompaniment instrument, practical register and basic rhythm aligned to the melody. Confirm it represents a second player or instrument rather than another hand of one keyboard part; a linked staff is for synchronized notation, not independent accompaniment.

### Execution

1. Use Layout > Add instrument for one pitched instrument and confirm its staff appears beside the original melody.
2. Inspect name, clef and empty measures, and avoid entering accompaniment on the melody staff.
3. Enter a short self-authored accompaniment on the second staff, checking bar alignment and practical range.
4. Listen to parts separately or together to confirm melody notes remain unchanged, then save and reopen both instruments.

### Success, common problems, and recovery

The score has two named instruments with aligned bars; original melody survives and accompaniment is independently editable.

- **Extra staff only:** Undo and use Add instrument for a separate player.
- **Melody overwritten:** Restore melody from saved state and reenter accompaniment on the new staff.
- **Range warning:** Inspect the new instrument's clef and range before adjusting notes.

### Assumptions and limits

This adds one simple accompaniment instrument, not automatic arrangement or proof that a live player can perform it. Complex transposing-instrument notation needs separate care.

### Sources

- [MuseScore Studio Handbook](https://handbook.musescore.org/notation/instruments-staves-and-systems/instruments-and-system-markings) — Layout panel adds an instrument, distinct from adding another staff to the same instrument.
- Original synthesis — one original notation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain MuseScore controls. You choose the content, perform the steps and verify the result.

