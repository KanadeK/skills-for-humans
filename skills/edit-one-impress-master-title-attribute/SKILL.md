---
name: edit-one-impress-master-title-attribute
description: "Human-readable one-property change to an existing Impress master title style, checked on multiple dependent slides and excluded masters."
---
# 在 Impress 母版中统一调整标题一项属性 / Edit One Impress Master Title Attribute

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 使用同一母版的非敏感 ODP 副本、一个要调整的标题属性 / Non-sensitive ODP copy with shared master and one title property to adjust |
| Side effects / 现实副作用 | 同母版标题同步变化而其他母版不变 / Same-master titles update while other masters stay |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你发现采用同一 Impress 母版的标题整体太小或间距不适，想统一改一个属性时使用本篇。成果是依赖该母版的两张以上页面同步变化，别的母版页和正文不受影响。它不同于只改一张的布局，也不在内容页逐张直接格式化。

### 准备与输入

保存 ODP 副本，列出采用目标母版的两页和一张使用别的母版的对照页。记下标题样式当前一项属性的原值，比如字号或段前间距。先确定它确实由母版控制，若内容页有局部覆盖，需记录例外。

### 执行

1. 进入 View > Master Slide，选准目标母版的标题样式或占位框。
2. 只改一项已记录属性，保存并退出母版视图，不顺手改正文或背景。
3. 比较两张依赖页的标题与对照页，核前两张同步、对照页未变，文字无截断。
4. 有意外就恢复原属性或副本；正确时保存重开再抽查。

### 完成、常见问题与恢复

同一母版的标题属性统一，未用该母版的页与正文仍原样，原值可恢复。

- **只有一页变化：** 检查该页是否直接格式化，或误改了单页。
- **全部母版都变：** 撤销并确认母版选择。
- **标题截断：** 恢复原值或调整允许空间。

### 假设与边界

只改一套母版标题的单项属性。你负责审美和可读性判断；一次样式变化可能波及该母版所有页面，务必在副本中操作。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26202-SlideMastersSlideTemplates.html)（英文，官方手册）— 母版样式改动会传递到采用该母版的页面。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when titles on slides sharing one Impress master are consistently too small or cramped and one property should change globally. Finish with at least two dependent slides updated together while another master's slide and body text remain unaffected. This differs from one-slide layout changes and avoids repeated direct formatting.

### Preparation and inputs

Save an ODP copy and identify two slides using target master plus one control using another. Note old value of one title property such as size or spacing. Confirm it is master-controlled; record any direct-format overrides on individual slides.

### Execution

1. Enter View > Master Slide and select the intended master's title style or title area.
2. Change only the noted property, save and leave master view without editing body or background.
3. Compare two dependent titles with control slide; both intended update, control remains, text does not clip.
4. Restore old property or copy for unintended changes; otherwise save and reopen to spot-check.

### Success, common problems, and recovery

One title property is consistent across target-master slides, excluded master and body stay, and old value is known.

- **Only one updates:** Check direct override or one-slide edit.
- **All masters change:** Undo and inspect master selection.
- **Title clips:** Restore old value or available space.

### Assumptions and limits

This changes one title property on one master. You judge readability. A style change may affect every dependent slide, so work on a copy.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26202-SlideMastersSlideTemplates.html) — master style edits propagate to slides based on that master.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.
