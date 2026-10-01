---
name: reduce-low-rumble-in-owned-audacity-speech
description: "Human-readable restrained high-pass filtering of self-recorded speech in Audacity 4, checking rumble reduction against voice-body loss."
---
# 用 Audacity 高通滤镜减轻本人讲话低频隆隆声 / Reduce Low Rumble in Owned Audacity Speech

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 有持续低频隆隆声的自录非敏感讲话 `.aup4`、原轨对照 / Self-recorded non-sensitive speech .aup4 with steady low rumble and original comparison |
| Side effects / 现实副作用 | 隆隆声减轻，语音厚度与字词仍自然 / Rumble lessens while voice body and words remain natural |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在本人普通讲话录音里听见空调或桌面振动造成的持续低频隆隆声，想减轻而不把声音削成薄尖时使用本篇。成果是低频干扰下降、辅音和人声主体仍自然，原轨可对照。它只处理稳定低频问题，不承诺去掉所有环境噪声或修坏掉的麦克风。

### 准备与输入

保存 `.aup4`，复制工作轨，找一处只有隆隆声的停顿和一处低沉元音。确认问题确实主要在低频，不把正常低音当噪声。先听原轨并记录目标；若录音设备持续故障，后续录制还需修源头。

### 执行

1. 只选工作轨，打开 Effect > EQ and filters > High-pass Filter，预览从保守截止设置起。
2. 比较停顿的低频与低沉元音，不让噪声下降以牺牲整个人声厚度。
3. 小幅调截止或坡度一次，再与原轨交替试听，核词句可辨。
4. 满意时保存重开并导出短预览；声音发薄就撤销或减弱。

### 完成、常见问题与恢复

隆隆声减轻、人声仍饱满可懂，所选设置与取舍有记录。

- **声音发薄：** 降低截止或撤销。
- **隆隆仍在：** 可能非恒定低频或源设备问题。
- **整轨没变化：** 核工作轨与效果目标。

### 假设与边界

只减轻本人录音的一类低频干扰，不作听力医学判断或专业母带保证。你负责实听。

### 来源

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/effects/eq-and-filters/high-pass-filter/)（英文，官方手册）— High-pass Filter 衰减截止频率以下内容，过高截止会削薄声音。
- Original synthesis — 将一个音频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when your own ordinary speech contains steady air-conditioning or desk-vibration rumble that should be reduced without making the voice thin. Finish with less low-frequency disturbance, natural speech body/consonants and an original comparison. This addresses stable low rumble, not all noise or broken microphone hardware.

### Preparation and inputs

Save `.aup4`, duplicate work track, choose one rumble-only pause and one deep vowel. Confirm disturbance is low-frequency rather than normal vocal bass. Listen to base and note aim; persistent capture hardware trouble needs source correction later.

### Execution

1. Select work track and open Effect > EQ and filters > High-pass Filter, previewing a conservative cutoff.
2. Compare low-frequency pause and deep vowel, rejecting settings that hollow voice.
3. Nudge cutoff or roll-off once and alternate with original, checking intelligibility.
4. Save/reopen and export short preview if acceptable; undo/reduce for thin sound.

### Success, common problems, and recovery

Rumble is lower, speech remains full and intelligible, and setting/tradeoff are recorded.

- **Voice thins:** Lower cutoff or undo.
- **Rumble remains:** May be other noise or source hardware.
- **No change:** Check selected work track.

### Assumptions and limits

This reduces one low-frequency issue in your recording, not hearing medicine or mastering assurance. You listen.

### Sources

- [LibreOffice Audacity 4 Manual](https://www.audacityteam.org/manual/effects/eq-and-filters/high-pass-filter/) — High-pass attenuates below cutoff and too high a cutoff can thin speech.
- Original synthesis — one audio-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Audacity controls. You choose the content, perform the steps and verify the result.
