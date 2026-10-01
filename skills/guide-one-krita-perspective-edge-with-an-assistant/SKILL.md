---
name: guide-one-krita-perspective-edge-with-an-assistant
description: "Human workflow to use a Krita drawing assistant to place one intended perspective edge while checking it against an original sketch."
---
# 用 Krita 绘画辅助尺画一条透视边 / Guide One Krita Perspective Edge with an Assistant

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 有原创构图的已保存画布、独立线稿层和明确消失方向 / Saved original sketch, separate ink layer and intended vanishing direction |
| Side effects / 现实副作用 | 一条方向受控且与构图相符的物体边线 / One guided object edge matching the planned perspective |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在原创场景草图里已有一个桌沿或建筑边缘，手画总与设定消失方向不一致时，用辅助尺只解决这一条线。成果是和草图空间关系一致的边线，辅助结构仍可修改。工具能帮助直线对齐，但不能替你决定构图是否合理；别把一张图的所有线都强制吸到同一个错误方向。

### 准备与输入

保存工程，先在草图层标好边线两端与大致消失方向。另选线稿层，确认本次只要一条边线，避免辅助尺被误用作正式几何测绘。查看当前有无旧辅助尺，先确认它们不会把新笔触吸到别处。

### 执行

1. 用 Assistant Tool 建一条直尺或合适的消失点辅助结构，按草图方向摆放并检查手柄位置。
2. 在 Freehand Brush 的工具选项里打开对辅助尺吸附，先在非关键位置试一条短线确认吸附对象正确。
3. 沿辅助方向画目标边线，端点只到所需物体边界；若越过主体或吸到别的尺，撤销后改辅助结构。
4. 关闭或隐藏辅助显示，在正常比例看边线与其他物体是否协调，保存工程并保留可解释的辅助布局。

### 完成、常见问题与恢复

该边线与原定透视方向一致，长度和端点正确，辅助显示关闭后仍能读出物体结构。

- **吸到错的尺：** 暂时隐藏或调整旧辅助尺，复试短线。
- **线越界：** 撤销后缩短笔势或用端点分段画。
- **空间看着别扭：** 回草图核消失方向，不靠更多吸附掩盖构图问题。

### 假设与边界

只服务一条原创插画边线，不保证完整透视教学、真实测量或工程精度。辅助尺与画笔吸附状态随工程和版本而异，以实际画面核对。

### 来源

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/painting_with_assistants.html)（英文，官方手册）— 绘画辅助尺能提供直尺、消失点及透视网格，并可让自由画笔吸附。
- Original synthesis — 将一个数字绘画结果、原稿对照和失败停点组合为可核流程。

## English

Use this when one edge in an original scene, such as a table or simple building, should follow a known vanishing direction but hand drawing wanders. Finish with that edge aligned to the sketch while keeping the assistant adjustable. Snapping helps execution; it does not decide whether the underlying perspective choice is sound.

### Preparation and inputs

Save, mark both endpoints and intended vanishing direction on the sketch, then choose a separate ink layer. This is one illustrative edge, not measured architectural geometry. Check existing assistants so an old guide does not capture the new stroke.

### Execution

1. Use Assistant Tool to create a ruler or suitable vanishing-point guide and align its handles with the planned sketch direction.
2. Enable assistant snapping in Freehand Brush options and test a short stroke away from the critical edge to verify the intended guide captures it.
3. Draw the intended edge along the guide, stopping at the object's endpoints. If it overshoots or snaps to another guide, undo and adjust the assistant.
4. Hide assistant display and inspect the line at normal scale against nearby objects; save with a comprehensible assistant layout.

### Success, common problems, and recovery

The edge follows the planned perspective, ends at the intended points and reads as part of the object after guides are hidden.

- **Wrong guide:** Hide or adjust older assistants and repeat the short test.
- **Overshoot:** Undo and shorten the gesture or draw between planned endpoints.
- **Awkward scene:** Revisit the sketch direction instead of adding more snapped lines.

### Assumptions and limits

This handles one illustrative edge, not a full perspective lesson, true measurement or engineering accuracy. Assistant and snap state vary, so inspect the actual stroke.

### Sources

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/painting_with_assistants.html) — Painting assistants include rulers, vanishing points and perspective grids with brush snapping.
- Original synthesis — one digital-painting outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Krita controls. You choose the content, perform the steps and verify the result.

