---
name: reroute-one-draw-connector-around-a-node
description: "Human-readable repair of one Draw connector that crosses a node or label, using route handles while preserving both attached endpoints."
---
# 把 Draw 一条穿过节点的连接线绕开 / Reroute One Draw Connector Around a Node

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 一条已附着但穿过文字/节点的连接器、ODG 副本 / One attached connector crossing a label/node and ODG copy |
| Side effects / 现实副作用 | 线路绕开遮挡且两端关系不变 / Route clears obstruction while endpoints stay |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有一条正确连接两节点的 Draw 线，但它从第三个节点或文字中间穿过，读图时容易误判关系时使用本篇。成果是这条线绕开遮挡、两个端点和箭头方向仍指向原对象，没有凭空多一条平行线。它修的是走线，不是改变流程目的地。

### 准备与输入

保存 ODG 副本，写下该线的起点、终点和被遮挡对象，确认它确实是连接器而不是普通线。决定靠上、下或侧边绕行的安全空间。不要先删除原线重画，以免丢掉端点或线旁标签。

### 执行

1. 选中连接器，找到中间的方形路由控制点，先不拖动两端圆形控制点。
2. 小幅拖方形控制点，使线段绕过障碍且不压其它标签。
3. 逐线核起点终点与箭头方向，轻移一端节点确认仍附着。
4. 若端点脱落或新交叉更糟，撤销并试另一条路；正确时保存重开。

### 完成、常见问题与恢复

同一条连接器绕开遮挡，起终点不变，移动测试仍附着。

- **端点脱开：** 撤销，重接正确 gluepoint。
- **又压到别的字：** 换另一侧绕行。
- **出现第二条线：** 删除误加副线，保留原关系。

### 假设与边界

只修一条线的视觉路线，不证明流程关系本身正确。你负责起终点语义，禁止用于工程控制图。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html)（英文，官方手册）— 连接器中间方形控制点可改路由，圆形端点仍应附着。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an otherwise correct Draw connector passes through another node or label and makes the relationship ambiguous. Finish with the line routed around obstruction, both endpoints and arrow direction still on original objects, and no duplicate parallel line. This repairs routing, not destinations.

### Preparation and inputs

Save ODG copy and note connector start/end and obstructed object. Confirm it is an attached connector, not plain line. Choose free route above, below or beside obstruction. Avoid deleting/recreating before checking attached endpoints and labels.

### Execution

1. Select connector and find middle square route handles, leaving round endpoint handles alone.
2. Move route handle modestly around obstruction without crossing other labels.
3. Trace source/target and arrow direction, then briefly move one node to confirm attachment.
4. Undo for detached endpoint or worse crossing, try another route and save/reopen when clear.

### Success, common problems, and recovery

Same connector clears obstruction, retains endpoints and follows a node after test move.

- **Endpoint detaches:** Undo and reconnect correct gluepoint.
- **Crosses other text:** Route around another side.
- **Duplicate line appears:** Remove extra line and keep original relation.

### Assumptions and limits

This repairs one visual route, not the truth of the process link. You own endpoint meaning; engineering control diagrams are excluded.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html) — middle square handles reroute a connector while round endpoints should remain attached.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.
