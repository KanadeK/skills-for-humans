---
name: set-draw-snap-guides-for-diagram-margins
description: "Human-readable two-guide setup for a standalone Draw diagram's content margins, checking object placement and nonprinting guide behavior."
---
# 给 Draw 图设两条页边吸附参考线 / Set Draw Snap Guides for Diagram Margins

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有 ODG 页、要保留的左右或上下边界空白 / ODG page with intended left-right or top-bottom content margin |
| Side effects / 现实副作用 | 对象边界有可重复参考且参考线不打印 / Objects have repeatable margins while guides do not print |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一张 Draw 图节点靠页边忽远忽近，想给内容区留一致的两侧空白时使用本篇。成果是两条位于预定边界的参考线，最外侧对象能贴合它们，输出时线本身不显示。它与密集网格不同，只为内容外缘提供位置锚点。

### 准备与输入

保存 ODG 副本，选要设左右还是上下两侧，核页尺寸和所需标题/图例空间。明确参考线与真实边框不同，若要在成品画边框应另画对象。先记录最外侧节点当前位置，避免设线后把它们推到页外。

### 执行

1. 使用 Insert > Snap Guide 建第一条垂直或水平线，在同一单位下建第二条。
2. 开启显示与吸附参考线，移动一个最外侧节点到线旁，核位置被帮助而非遮挡标签。
3. 预览或打印预览核参考线不在输出页面，真实对象仍在安全内容区。
4. 保存重开，若两侧间距不合适，编辑参考线坐标而不硬拖所有节点。

### 完成、常见问题与恢复

两条边界参考线可用、对象与内容区一致，输出不含编辑辅助线。

- **线出现在输出：** 那可能是真实线对象，撤销重建参考线。
- **吸附无效：** 核显示与吸附是两个开关。
- **内容区太窄：** 调整坐标或减少信息。

### 假设与边界

只设两个普通图的排版边界，不保证任何打印机纸边距或测量精度。你负责页面用途。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26203-WorkingWithObjects.html)（英文，官方手册）— Insert > Snap Guide 可建水平或垂直参考线，参考线不进入打印输出。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when Draw nodes approach the page edge inconsistently and the content region needs repeatable outer margins. Finish with two guides at chosen boundaries, outer objects aligned to them and no guide line in output. Unlike a dense grid, these mark only content edges.

### Preparation and inputs

Save ODG copy, choose left/right or top/bottom pair and consider page size plus title/legend space. Guides differ from real borders; draw an object only if a visible border is needed. Note current outer nodes to avoid pushing them off-page.

### Execution

1. Use Insert > Snap Guide for first vertical/horizontal line and create the second in the same units.
2. Show/snap to guides and move one outer node near a line, checking alignment without obscuring labels.
3. Use preview to confirm guide lines do not appear in output while objects remain in content area.
4. Save/reopen and edit guide coordinates if margins are poor rather than dragging every node blindly.

### Success, common problems, and recovery

Two guides define usable bounds, objects fit content region and output omits editing aids.

- **Line prints:** It may be a drawn object; recreate guide.
- **No snap:** Check display and snap toggles.
- **Region too narrow:** Move guides or reduce content.

### Assumptions and limits

This sets two layout bounds for an ordinary diagram, not printer-margin or measurement guarantee. You choose page purpose.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26203-WorkingWithObjects.html) — Insert > Snap Guide adds horizontal or vertical snap lines that do not print.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.

