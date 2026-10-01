---
name: connect-two-draw-nodes-with-attached-connector
description: "Human-readable Draw connector between two existing process nodes, tested by moving a node to prove endpoints stay attached."
---
# 用 Draw 附着式连接线连上两个节点 / Connect Two Draw Nodes with an Attached Connector

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 同页两个已标注节点、已保存 ODG 副本 / Two labelled same-page nodes and saved ODG copy |
| Side effects / 现实副作用 | 箭头表达方向且两端随节点移动 / Arrow shows direction and endpoints follow nodes |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有两个 Draw 流程节点，想表达 A 完成后到 B，而不是在它们之间画一条会脱开的普通线时使用本篇。成果是一条方向清楚的附着式连接线，短距离移动任一节点后端点仍在对应形状上。它建立关系，不决定关系是否现实成立。

### 准备与输入

保存 ODG 副本，确认 A、B 的语义先后与希望箭头走向。查看两节点边缘可用的 gluepoint，留出线段不穿过标签的路线。若图里已有普通直线，先识别它是不是连接器，不叠加两条线。

### 执行

1. 在 Connectors 工具里选适合的箭头连接器，从 A 边缘 gluepoint 拉到 B 边缘 gluepoint。
2. 核箭头方向和两端位置，线段不穿过文字或反向指回 A。
3. 轻移 B 节点再撤回，观察连接器仍附着并自动改路，不是留在原坐标。
4. 保存重开，仍能选到连接器与两个独立节点；掉端则重连正确 gluepoint。

### 完成、常见问题与恢复

A→B 有一条真连接器，移动测试两端未脱，文字仍可读。

- **线端留原处：** 改用连接器而非普通线。
- **箭头反向：** 调整起终点或方向。
- **线压标签：** 换边缘 gluepoint 或路由。

### 假设与边界

只画两个普通节点的一条方向关系，不证明流程因果。你负责语义；本篇不用于工程或安全控制图。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html)（英文，官方手册）— 连接线端点锁在节点 gluepoint，节点移动时仍附着。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when two Draw process nodes exist and A should lead to B, using a real attached connector rather than a loose line that detaches. Finish with a clear directional connector whose endpoints stay on the corresponding shapes after a small node move. This draws a relationship; it does not prove the process is factually correct.

### Preparation and inputs

Save ODG copy and confirm A-to-B semantics and arrow direction. Inspect available gluepoints at shape edges and plan a route away from labels. If a line already exists, determine whether it is an attached connector before doubling it.

### Execution

1. Choose an arrow connector in Connectors tool and draw from A gluepoint to B gluepoint.
2. Check arrow direction/endpoints and avoid crossing text or pointing back to A.
3. Move B a little and back to test connector follows its node rather than staying at old coordinates.
4. Save/reopen; select connector and both nodes independently, reconnecting a loose endpoint.

### Success, common problems, and recovery

One real A→B connector stays attached after move test and labels remain readable.

- **Endpoint stays:** Use connector instead of plain line.
- **Arrow reversed:** Swap source/target or arrow setting.
- **Line covers label:** Use another edge gluepoint or route.

### Assumptions and limits

This draws one directional relation between ordinary nodes, not causal proof. You own meaning; exclude engineering and safety control diagrams.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html) — connector endpoints lock to node gluepoints and remain attached when nodes move.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.

