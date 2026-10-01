---
name: choose-and-test-impress-manual-slide-advance
description: "Human-readable choice and test of manual versus timed slide advance in an Impress deck, preventing unintended auto-advance during a short run."
---
# 确认 Impress 放映由讲者手动翻页 / Choose and Test Impress Manual Slide Advance

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有至少三页的非敏感 ODP 副本、计划由讲者控制的放映 / Non-sensitive ODP copy with at least three slides and presenter-controlled run |
| Side effects / 现实副作用 | 页停留到讲者主动前进，不自行跳页 / Slides wait for a presenter action instead of auto-advancing |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你准备口头讲述一份短 Impress 稿，不希望某页在你没讲完时自动跳到下一页时使用本篇。成果是所测的三页都等待讲者主动前进，过渡效果本身不改变这个规则。它判断播放控制，不决定每页讲多长，也不把一次试放当作现场设备验收。

### 准备与输入

保存 ODP 副本，选连续三页和一页曾出现自动跳转的样本。查看 Slide Transition 中的 Advance Slide 以及整体 Slide Show Settings；已有自动定时可能藏在个别页。若实际用途是无人值守循环，不应强改手动，本篇不适用。

### 执行

1. 在样本页将 Advance Slide 设为鼠标点击/手动，清除不需要的 After 时间。
2. 检查整场放映设置没有覆盖手动选择的自动前进规则。
3. 试放连续三页，每页停留一段足以观察的时间，核只有主动点击/按键才换页。
4. 若仍跳页，回个别页计时与动画触发查因；正确时保存重开重复一处核查。

### 完成、常见问题与恢复

样本页不会自行跳，讲者可逐页前进；例外页被明确记录。

- **一页仍自动跳：** 查该页 After 时间。
- **点击只揭示对象：** 区别对象动画与整页前进，再试下一点击。
- **整场不响应：** 检查放映设置与输入焦点。

### 假设与边界

只核短样本的手动翻页，不保证遥控器、投影仪或现场输入设备。你决定是否需要定时放映；本篇不作舞台技术支持。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26209-SlideShowsPhotoAlbums.html)（英文，官方手册）— Slide Show Settings 与 Slide Transition 的 Advance Slide 共同决定手动或定时前进。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill for a short orally presented Impress deck that must not jump ahead before you finish speaking. Finish with three tested slides waiting for a deliberate presenter action. A transition effect does not by itself decide advancement. This tests show control, not ideal speaking duration or live hardware readiness.

### Preparation and inputs

Save an ODP copy and choose three consecutive slides, including one suspected auto-advance. Inspect per-slide Advance Slide in Transition deck and overall Slide Show Settings; old timers may reside on individual slides. If purpose is unattended looping, manual control is not the right outcome.

### Execution

1. Set sampled slides to On mouse click/manual and clear unwanted After times.
2. Check show-level settings do not override manual choice with automatic advance.
3. Run three slides, wait visibly on each, and verify only an intentional click/key advances.
4. For continued skipping, inspect individual timers and animation triggers; otherwise save/reopen and retest one point.

### Success, common problems, and recovery

Sampled slides do not auto-advance and presenter can move one at a time; exceptions are recorded.

- **One still auto-advances:** Check that slide's After timer.
- **Click only reveals object:** Distinguish object animation from slide advance.
- **Show ignores input:** Inspect show settings and input focus.

### Assumptions and limits

This tests a short manual sequence, not remotes, projectors or live input devices. You choose whether timed running is appropriate; this is no stage-tech support.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26209-SlideShowsPhotoAlbums.html) — Slide Show Settings and Slide Transition Advance Slide govern manual versus timed movement.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.
