---
name: name-two-draw-objects-for-navigator-retrieval
description: "Human-readable naming of two important Draw diagram objects so Navigator can distinguish and return to each without changing visible labels."
---
# 给 Draw 两个关键对象起可找回的名字 / Name Two Draw Objects for Navigator Retrieval

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 含同形节点的普通 ODG 副本、两处关键对象 / Ordinary ODG copy with similar shapes and two key objects |
| Side effects / 现实副作用 | Navigator 中两个对象可按用途区分 / Two objects become distinguishable in Navigator |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一张 Draw 图有多个外观相似的流程框，要回头定位某两处关键节点时总要逐个点时使用本篇。成果是这两个对象在 Navigator 中有不同、说明用途的名称，点击可回到正确位置；图上可见的动作标签不被改写。命名对象是编辑索引，不另造流程步骤。

### 准备与输入

保存 ODG 副本，先在图上识别两处对象的页面、可见文字和流程角色。拟短且唯一的内部名，例如“判断_资料齐全”与“动作_补材料”，不用私人姓名或秘密代号。确认选中对象而非其文本编辑光标。

### 执行

1. 选第一对象，通过对象属性/名称命令设置内部名，核可见标签未变。
2. 为第二对象设不同名称，避免系统默认 Rectangle 1/2 这种无意义序号。
3. 在 Navigator 查找两个名称并逐个跳转，核落到正确页和形状。
4. 保存重开再测一次，若名称冲突或指错形状，重新命名对应对象。

### 完成、常见问题与恢复

两个关键对象可按内部名称准确找回，可见图中文字与线不变。

- **改了可见标签：** 撤销，改对象 Name 属性。
- **导航跳错：** 核是否选中错误形状。
- **名字相似难分：** 加入角色和动作词。

### 假设与边界

对象名只是本地图形编辑线索，不保证导出 SVG/PDF 保留或成为可及性文字。你负责名称不含敏感信息。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26201-IntroducingDraw.html)（英文，官方手册）— Draw 的 Navigator 可按有意义对象名定位页面和图形。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when many similar-looking Draw nodes make two important objects hard to find later. Finish with distinct purpose-based names in Navigator that locate the correct shapes, while visible action labels stay unchanged. Object names are an editing index, not additional process steps.

### Preparation and inputs

Save ODG copy and identify each object's page, visible label and role. Draft short unique internal names such as 'decision_materials_ready' and 'action_request_missing' without private names or secrets. Select shape itself rather than placing text cursor inside it.

### Execution

1. Select first shape and set its internal Name via object properties/name control; keep visible label.
2. Give second shape a distinct name rather than generic Rectangle 1/2.
3. Find both names in Navigator and jump to each, checking correct page/shape.
4. Save/reopen and test again; correct conflict or misnamed object.

### Success, common problems, and recovery

Both key objects are retrievable by distinct internal names, while visible labels and connectors remain.

- **Visible text changed:** Undo and edit object Name.
- **Navigator jumps wrong:** Check selected shape.
- **Names ambiguous:** Add role and action words.

### Assumptions and limits

Object names are local editing aids, not guaranteed SVG/PDF metadata or alternative text. You keep names non-sensitive.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26201-IntroducingDraw.html) — Draw Navigator locates pages and objects more easily with meaningful names.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.

