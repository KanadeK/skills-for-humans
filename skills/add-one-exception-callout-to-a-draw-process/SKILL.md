---
name: add-one-exception-callout-to-a-draw-process
description: "Human-readable callout note for one exceptional ordinary process condition, anchored near the correct node without becoming another flow step."
---
# 给 Draw 流程一处例外加说明气泡 / Add One Exception Callout to a Draw Process

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有普通流程节点、一个真实例外说明、ODG 副本 / Existing ordinary process node, one real exception note and ODG copy |
| Side effects / 现实副作用 | 例外可见且不误读成新的主流程节点 / Exception is visible without becoming a main step |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张普通 Draw 流程图，某个节点只在少数情形需要一条短提醒，不应因此再添一条主路径时使用本篇。成果是一个指向正确节点的例外说明气泡，主流程箭头仍清楚。气泡内容应说明触发条件与处理边界，不用“其它情况同理”遮掩未知。

### 准备与输入

保存 ODG 副本，写下这条例外何时出现、需要做什么或停止什么，确认不会与原主步骤矛盾。选节点附近的留白，不在箭头交汇处塞长段文字。若例外实际会改变目的节点，可能应该画新分支而非气泡。

### 执行

1. 从 Callouts 工具选简单气泡，放在目标节点附近但不盖住节点或线。
2. 把指向尾部对准目标节点边缘，写一两句触发条件和边界。
3. 从图的入口顺主线阅读，核气泡不会被误当下一步或第三条出口。
4. 保存重开，若内容过长或指错对象，缩短并重新定位。

### 完成、常见问题与恢复

例外说明靠近正确节点、触发条件可读，主流程不受遮挡。

- **气泡像主节点：** 改形状/位置，明确仅为注释。
- **尾巴指错：** 重定位到目标边。
- **文字太长：** 保留触发与停点，详情另写。

### 假设与边界

只给普通流程加一处解释，不替代正式操作规程。你负责例外逻辑；涉及安全/法律时退出范围。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26202-DrawingBasicShapes.html)（英文，官方手册）— Callouts 形状可在图中放注释与指向对象。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one ordinary Draw process node needs a short note for an exceptional condition but no additional main path. Finish with a callout pointing to the right node while main flow arrows remain clear. The note states trigger and limit rather than hiding uncertainty behind 'and so on'.

### Preparation and inputs

Save ODG copy. State when exception happens and the action or stop, checking it does not contradict main step. Choose whitespace near node, not a crowded arrow junction. If it changes destination, draw a proper branch instead of a callout.

### Execution

1. Choose a simple Callout and place near target node without covering it or connectors.
2. Point its tail at target node edge and write one or two short trigger/limit sentences.
3. Read main path from start and check note cannot be mistaken for next step or third exit.
4. Save/reopen; shorten or reposition if overlong or aimed at wrong node.

### Success, common problems, and recovery

Exception note is beside correct node, trigger readable and main flow unobscured.

- **Looks like process node:** Change style/position to signal note.
- **Tail points wrong:** Move it to correct edge.
- **Too much text:** Keep trigger and stop, move detail elsewhere.

### Assumptions and limits

This adds one ordinary-flow explanation, not a formal procedure. You own exception logic; safety/legal cases are outside scope.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26202-DrawingBasicShapes.html) — Callouts shapes can annotate and point to a drawing object.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.

