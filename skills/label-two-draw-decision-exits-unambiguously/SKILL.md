---
name: label-two-draw-decision-exits-unambiguously
description: "Human-readable labeling of two existing Draw decision connectors with yes/no or equivalent meanings, checking placement and branch correspondence."
---
# 给 Draw 判断节点的两条出口写清含义 / Label Two Draw Decision Exits Unambiguously

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有一个判断与两条连接线的 ODG 副本、两种已确定条件含义 / ODG copy with decision and two connectors, two settled condition meanings |
| Side effects / 现实副作用 | 每条出口的含义可直接顺线读懂 / Each exit can be understood by following its line |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有 Draw 判断菱形和两条结果线，却发现读者不知道哪条代表“是”、哪条代表“否”时使用本篇。成果是两条线各有简短、位置明确的标签，沿线可对应正确终点，标签不会误压到节点或另一条线。它修正分叉语义，不再新增判断或结果节点。

### 准备与输入

保存 ODG 副本，先逐条核真实条件与目的节点，记下哪条应是“是”、哪条应是“否”或其它清楚词。若两条都不能用这两个词准确表达，回到条件定义，不靠标签掩盖流程错误。选可读的标签位置靠近线起端或中段。

### 执行

1. 先选第一条连接器，加入简短标签，确认文字随该线而非浮到另一条上。
2. 给第二条连接器写互斥标签，逐线追到终点复述结果。
3. 在普通查看尺寸核标签不重叠、不反向、不遮菱形问题或节点文字。
4. 小幅移动节点再核标签与线路关系，保存重开；错线时撤销更正。

### 完成、常见问题与恢复

两出口各自可辨，标签与实际终点一致，移动后仍不会混淆。

- **是/否放反：** 依据实际条件与终点调换。
- **标签压线交点：** 移到相应线段旁。
- **标签独立飘走：** 核是否附着连接器并重放。

### 假设与边界

只说明两条已有普通分支，不替代流程规则核对。你对条件与终点语义负责。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html)（英文，官方手册）— 连接器和流程图可加入文字以说明路径。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a Draw decision diamond and two result connectors exist but a reader cannot tell which means yes versus no. Finish with a short clear label on each route that maps to the right destination and does not overlap nodes or the other line. This fixes branch meaning without adding decision or outcome nodes.

### Preparation and inputs

Save ODG copy and trace each actual condition to its destination. Decide which is yes and no or other clear terms. If those terms do not describe reality, fix the decision definition rather than masking a logic fault. Pick readable label positions near line start or middle.

### Execution

1. Select first connector and add its short label, checking text belongs to that line.
2. Label second connector with its distinct meaning and trace both paths aloud to outcomes.
3. At normal size inspect no overlaps, reversed labels or obscured decision/node text.
4. Move a node slightly and recheck labels/lines, then save/reopen; undo wrong association.

### Success, common problems, and recovery

Both exits are distinguishable, labels match destinations and remain clear after a move.

- **Yes/no reversed:** Swap labels after tracing condition.
- **Label at crossing:** Move beside its own segment.
- **Label drifts:** Check connector attachment.

### Assumptions and limits

This clarifies two existing ordinary branches, not rule validation. You own condition and destination meanings.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26208-ConnectionsFlowchartsOrganisationCharts.html) — connectors and flowchart text can explain route meanings.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.

