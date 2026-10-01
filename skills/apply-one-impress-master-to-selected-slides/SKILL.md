---
name: apply-one-impress-master-to-selected-slides
description: "Human-readable application of one existing Impress master to selected slides, checking shared appearance and untouched excluded slides."
---
# 只给选中页应用同一 Impress 母版 / Apply One Impress Master to Selected Slides

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有多页非敏感 ODP 副本、一个现成可用母版和明确选中页 / Non-sensitive ODP copy, existing usable master and explicit target slides |
| Side effects / 现实副作用 | 目标页共享样式，未选页保留原貌 / Target slides share styling while excluded slides retain appearance |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一组内容页外观不一致，想只给它们应用现有 Impress 母版时使用本篇。成果是明确选中的页共享背景与占位样式，未选的标题页或特殊页保留原貌；所有页的内容文字仍完整。它不创建新母版，也不凭颜色不同就宣称信息层级更好。

### 准备与输入

保存 ODP 副本，记录目标页编号与一张明确不应改变的对照页。确认要用的母版已在演示稿中，且文字对比和图像位置不伤害内容。多选幻灯片时再核一次选中数量，避免母版菜单中的 Apply to All Slides。

### 执行

1. 在幻灯片窗格只选目标页，打开侧栏 Master Slides。
2. 对目标母版明确选择 Apply to Selected Slides，不点 Apply to All Slides。
3. 逐张核目标页的共同样式和原文字、图片，对照未选页仍原样。
4. 放映预览看对比与截字；不合适就撤销，保存重开后再抽查。

### 完成、常见问题与恢复

选中页共享预定母版，未选页没有被改，信息内容与对象仍完整。

- **所有页都变：** 撤销，改用 Selected 命令。
- **文字难读：** 撤销并选更合适母版或改内容。
- **对象被遮：** 检查母版背景对象和局部对象层级。

### 假设与边界

只应用一套已有母版，不评估品牌规范。你负责确认选中范围与实际可读性；不同模板可能有不兼容占位框。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26202-SlideMastersSlideTemplates.html)（英文，官方手册）— 母版侧栏可选 Apply to Selected Slides 而非全部页面。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a defined group of content slides looks inconsistent and should share an existing Impress master. Finish with only selected slides inheriting its background and master text styling, while excluded cover or special slides keep their design and all wording remains. This does not create a new master or prove information hierarchy from color alone.

### Preparation and inputs

Save an ODP copy, note target slide numbers and one excluded control. Confirm the master exists and its contrast and text-area positions fit content. After multiselecting, verify selection count before using the master menu; avoid Apply to All Slides.

### Execution

1. Select only target slides in slide pane and open Sidebar Master Slides.
2. Choose Apply to Selected Slides for the intended master, not Apply to All Slides.
3. Inspect each target's shared styling and original text/images, plus an excluded slide's unchanged appearance.
4. Preview contrast and clipping; undo if unsuitable, then save and reopen for spot checks.

### Success, common problems, and recovery

Selected slides share intended master, excluded slide remains untouched, and content objects survive.

- **Every slide changed:** Undo and use Selected action.
- **Text unreadable:** Undo and choose a fitting master or revise content.
- **Objects obscured:** Inspect master background and local object order.

### Assumptions and limits

This applies one existing master, not brand design review. You verify selection and readability; templates may have incompatible placeholders.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26202-SlideMastersSlideTemplates.html) — master deck offers Apply to Selected Slides rather than all pages.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.
