---
name: hide-and-restore-one-impress-slide-for-a-run
description: "Human-readable temporary exclusion of one optional Impress slide from a show while retaining it in the ODP and restoring it afterward."
---
# 为一次放映隐藏再恢复一张 Impress 页 / Hide and Restore One Impress Slide for a Run

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有可选页的非敏感 ODP 副本、明确本次放映范围 / Non-sensitive ODP copy with optional slide and stated run scope |
| Side effects / 现实副作用 | 一场放映跳过可选页，源文件仍保留并可恢复 / One run skips optional slide while source retains it |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张只在某次讲述中不适合展示的可选页，想暂时跳过但保留在 Impress 文件里时使用本篇。成果是放映从前页直接到后页，选中页在编辑器中仍存在且可恢复；结束后按计划恢复。它不是删除，也不是保密措施，隐藏页仍在 ODP 文件中。

### 准备与输入

保存 ODP 副本，记录可选页标题、前后页与隐藏原因，确认本次观众不应看到它。若页含不可披露信息，不要靠隐藏后发送文件。打开 Slide Sorter，确认只选择一张目标页。

### 执行

1. 对目标页执行 Slide > Hide Slide，核缩略图变灰而张数未减少。
2. 从前一页试放到后一页，确认本次放映不出现隐藏页。
3. 需要恢复时在编辑视图选灰色页，执行 Show Slide，核它重新参与放映。
4. 保存合适状态的 ODP，记录当前是隐藏还是恢复，避免下次误会。

### 完成、常见问题与恢复

目标页在本次放映中被跳过且未被删除，随后可明确恢复；文件披露风险被理解。

- **页被删除：** 从副本恢复，不用隐藏替代删除。
- **放映仍出现：** 核是否选错页或未启用隐藏。
- **下次忘记恢复：** 用记录核最终状态并 Show Slide。

### 假设与边界

隐藏只改变放映路线，不保护 ODP 内容。你负责是否共享文件及演示范围；自定义放映还需另核。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26209-SlideShowsPhotoAlbums.html)（英文，官方手册）— Hide Slide 让页在放映中跳过但仍留在文件中，可用 Show Slide 恢复。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one optional slide should be skipped in a particular run yet remain in the Impress file. Finish with show moving from its predecessor to successor, the slide still present in editor and later restored as planned. This is not deletion or confidentiality: hidden content remains in the ODP file.

### Preparation and inputs

Save an ODP copy and note optional slide title, neighbours and reason to skip it. If content is confidential, do not rely on hiding before sending the file. Open Slide Sorter and select only the target slide.

### Execution

1. Use Slide > Hide Slide; thumbnail should gray while slide count stays.
2. Run briefly from predecessor to successor and confirm hidden slide is skipped.
3. For restoration select gray thumbnail and use Show Slide; confirm it rejoins show.
4. Save ODP in the intended final state and record whether currently hidden or restored.

### Success, common problems, and recovery

Target is skipped for one run without deletion and can be explicitly restored; file-disclosure implications are understood.

- **Slide deleted:** Restore from copy; hide is different.
- **Still appears:** Check selected slide and hide state.
- **Forgot restoration:** Use recorded state and Show Slide.

### Assumptions and limits

Hiding changes show path, not ODP confidentiality. You decide sharing and run scope; custom shows need separate checks.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26209-SlideShowsPhotoAlbums.html) — Hide Slide skips a slide during show while retaining it; Show Slide restores it.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.

