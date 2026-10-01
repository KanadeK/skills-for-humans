---
name: align-impress-objects-on-one-common-axis
description: "Human-readable alignment of two or more selected Impress objects on one edge or center axis while preserving their content and spacing needs."
---
# 把 Impress 多个对象对齐到同一条边 / Align Impress Objects on One Common Axis

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 同页两个以上应对齐的非敏感对象、ODP 工作副本 / Two or more same-slide non-sensitive objects needing alignment and ODP copy |
| Side effects / 现实副作用 | 对象共享一条边或中心线而不遮挡 / Objects share an edge or centerline without overlap |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一页两个以上文字框、图标或图片应沿同一边排列，却因手拖有轻微错位时使用本篇。成果是选中对象共享指定左边、中心或顶边，文字和图像不被覆盖。这里解决一条轴的对齐，不自动处理对象之间的均匀间距；单选一个对象可能会改成相对页面对齐。

### 准备与输入

保存 ODP 副本，圈定确实应对齐的对象，记下原上下顺序和可读间距。先想好是左边、水平中心还是顶部，避免按错方向把对象叠在一起。确保至少选中两个对象，不把整页背景误选进来。

### 执行

1. 逐一选中目标对象，核选择框数量及对象名称或内容。
2. 在 Align Objects 选择一项明确的边或中心对齐，不同时尝试多个轴。
3. 放大检查共同轴、对象顺序和文字是否重叠；如果重叠，撤销并选另一对齐方式。
4. 保存重开并在放映预览看同一轴是否仍稳、整体没有偏出画布。

### 完成、常见问题与恢复

至少两个目标对象共享预定轴，顺序和内容可读，未选对象不动。

- **对象叠在一起：** 撤销，检查选择与轴方向。
- **整组移到页中：** 可能只选了一项，重选两项以上。
- **未选图也动：** 恢复副本并缩小选择。

### 假设与边界

只做一个轴的相对对齐，不规定幻灯片的设计系统或视觉验收。你负责对象归组及投影环境可读性。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26205-ManagingGraphicObjects.html)（英文，官方手册）— Align Objects 提供左中右或上中下的相对对齐。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when two or more boxes, icons or images on one slide should share an edge but hand dragging left them uneven. Finish with selected objects aligned on the chosen left edge, center or top without covering their contents. This solves one axis, not even spacing. A single selected object may align to the page rather than peers.

### Preparation and inputs

Save an ODP copy and identify objects that truly belong on a shared line. Note vertical order and readable gaps. Decide left edge, horizontal center or top before choosing a command. Select at least two objects and exclude the slide background.

### Execution

1. Select intended objects one by one, checking selection boxes and contents.
2. Choose one edge or center option in Align Objects rather than changing several axes at once.
3. Zoom in to check common axis, order and text overlap; undo if alignment causes collision.
4. Save/reopen and inspect show preview for stable line and no off-canvas objects.

### Success, common problems, and recovery

At least two target objects share intended axis, remain ordered/readable and excluded objects do not move.

- **Objects overlap:** Undo and inspect selection/axis.
- **Object moves to page center:** Maybe only one selected; choose at least two.
- **Unselected image moves:** Restore and narrow selection.

### Assumptions and limits

This handles relative alignment on one axis, not a full slide design system or live visual acceptance. You decide which objects belong together.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26205-ManagingGraphicObjects.html) — Align Objects provides relative left/center/right or top/middle/bottom alignment.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.

