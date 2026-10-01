---
name: update-one-custom-draw-style-across-nodes
description: "Human-readable one-property update of a custom Draw style already used by nodes, checking propagation and excluded symbols."
---
# 修改 Draw 一套自定样式并核同类节点同步 / Update One Custom Draw Style Across Nodes

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有自定样式的 ODG 副本、两目标节点和一排除节点 / ODG copy with custom style, two target nodes and one excluded node |
| Side effects / 现实副作用 | 一次样式调整同步同类节点而异类不动 / One style change propagates only to same-role nodes |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已用一套自定 Draw 样式标记同类流程节点，现在发现这类线条整体太细或文字对比不足，想改一次让它们同步时使用本篇。成果是两处以上目标节点一起改变一项属性，异类节点和背景不变。它是已有样式维护，不重新给每个节点逐个上色。

### 准备与输入

保存 ODG 副本，确认两个目标都真用同一个自定样式，记下原属性值和一处排除对象。只选择一个要改的属性，例如线宽；同时改填色、字体和透明度会让原因无法判断。检查是否有局部直接格式覆盖样式。

### 执行

1. 在一处目标对象或 Styles 面板编辑自定样式的一项属性，记下原值。
2. 执行 Update Selected Style 或该版本等价命令，确认不是内置默认样式。
3. 比较另一目标与排除节点：同类同步、异类未变，标签没有被压坏。
4. 有意外就撤回样式属性；正确时保存重开再核两处。

### 完成、常见问题与恢复

一项改动同步目标样式，排除对象不动，原值可恢复。

- **只一节点变：** 查是否直接格式而非样式更新。
- **所有图都变：** 撤销内置样式误改。
- **文字被压：** 恢复原线宽或调整节点空间。

### 假设与边界

只更新本图一套自定样式的一项属性，不做全局主题重构。你负责传播范围与可读性。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26204-ChangingObjectAttributes.html)（英文，官方手册）— Update Style 会传播自定样式变更，内置样式不宜随意更新。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when multiple same-role Draw nodes already share a custom style whose line is too thin or text contrast too low. Finish with one chosen property changing across at least two targets while other node types and background stay. This maintains an existing shared style rather than recoloring each node.

### Preparation and inputs

Save ODG copy. Verify two targets use the same custom style, note old property and an excluded object. Pick one change such as line width; changing fill, font and opacity together obscures cause. Note any local direct-format overrides.

### Execution

1. Edit one property of the custom style through a target or Styles deck, preserving old value.
2. Use Update Selected Style or equivalent, confirming it is custom rather than built-in default.
3. Compare second target with excluded node: same-role propagates, other role stays, labels remain intact.
4. Restore old property for unintended spread; otherwise save/reopen and check both targets.

### Success, common problems, and recovery

One property change reaches target style users, excluded object stays and old value remains recoverable.

- **Only one changes:** Check direct formatting versus style update.
- **Everything changes:** Undo built-in style edit.
- **Text squeezed:** Restore old width or node space.

### Assumptions and limits

This updates one property of one custom style in this drawing, not an entire theme. You verify spread and readability.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26204-ChangingObjectAttributes.html) — Update Style propagates custom-style edits while built-in styles should be handled cautiously.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.
