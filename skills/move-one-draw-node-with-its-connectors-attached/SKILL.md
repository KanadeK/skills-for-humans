---
name: move-one-draw-node-with-its-connectors-attached
description: "Human-readable reposition of one connected Draw node after a layout change, checking every incoming/outgoing endpoint and label."
---
# 移动 Draw 一个节点并核两端连接未脱 / Move One Draw Node with Its Connectors Attached

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有至少两条连线的普通节点、ODG 副本和目标空位 / Ordinary node with at least two connectors, ODG copy and target space |
| Side effects / 现实副作用 | 节点换位后关系仍指向同一对象 / Node moves while relationships still reach it |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你调整 Draw 流程图布局，要把一个已经有入线和出线的节点挪到更易读的位置时使用本篇。成果是节点移位后各条线仍接到原本正确的节点和 gluepoint，箭头方向与文字未被挤乱。它是改版后的关系复核，不是添加新流程步骤。

### 准备与输入

保存 ODG 副本，先列出该节点的入线、出线及各自目的，拍下或记下旧位置。选目标空位时避开其它节点和图例。确认多选状态已清除，免得连邻居一起移动。

### 执行

1. 只选目标节点，把它短距离移向预定位置，观察连线是否自动改路。
2. 逐条从起点追到终点，核端点仍在目标形状边缘而非停在原坐标。
3. 检查箭头方向、线旁文字和邻节点是否被穿过；必要时微调路线而不改语义。
4. 保存重开，再移动一次小幅测试后撤销，确认附着持久。

### 完成、常见问题与恢复

节点换位，所有原有关系仍连到正确对象，图的阅读顺序更清楚。

- **一条线留原处：** 可能是普通线，换附着连接器。
- **邻节点也动：** 撤销并清多选。
- **箭头穿字：** 调整 connector 路由或空位。

### 假设与边界

只移动一个普通流程节点，不改变流程条件。你负责逐线确认实际关系；复杂共享线网可能需更全面复核。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html)（英文，官方手册）— 附着连接器会随对象移动调整，端点需逐条核。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when moving a Draw node that already has incoming and outgoing connectors to improve layout. Finish with every line still attached to the intended node/gluepoint, arrow directions and labels intact after repositioning. This is relationship verification after layout change, not a new process step.

### Preparation and inputs

Save an ODG copy, list each incoming/outgoing connection and its source/destination, and note old position. Choose free space away from other nodes and legend. Clear multiselection so neighbours do not move too.

### Execution

1. Select only target node and move it a short distance, watching attached connectors reroute.
2. Trace each line end to end, verifying endpoints stay on shape edges rather than old coordinates.
3. Check arrow direction, labels and crossings; adjust routing without changing meaning.
4. Save/reopen, perform one small move test and undo to confirm lasting attachment.

### Success, common problems, and recovery

Node changes position, all original relations still attach correctly, and reading order improves.

- **One line stays:** It may be plain line; use connector.
- **Neighbour moves:** Undo and clear multiselection.
- **Arrow crosses text:** Reroute or choose safer space.

### Assumptions and limits

This moves one ordinary node without changing process rules. You verify each relationship; complex networks need broader review.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html) — attached connectors adjust when objects move and endpoints need review.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.
