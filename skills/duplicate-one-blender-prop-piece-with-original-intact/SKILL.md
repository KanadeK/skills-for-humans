---
name: duplicate-one-blender-prop-piece-with-original-intact
description: "Human workflow to duplicate one original mesh object for a repeating prop feature, move the copy intentionally and verify the source object remains."
---
# 复制 Blender 道具的一件重复零件并保留原件 / Duplicate One Blender Prop Piece with Original Intact

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存原创道具、需要两个相似零件的草图 / Saved original prop and sketch requiring two similar pieces |
| Side effects / 现实副作用 | 一对位置清楚的独立对象，原件仍在原位 / Two clearly placed objects with original at its prior position |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你为原创道具做了一只脚、一个旋钮或一块装饰，草图要求第二个相似零件时，复制现有物体并明确放置。结果是两个可分别选择的对象，原件仍在起始位置，副本只承担本次重复用途。复制后刚好重叠会看似只有一个；共享材质也可能让后续改色同时影响两者。

### 准备与输入

保存 .blend，单选原件并记录它的名称与位置；在草图上确定副本应沿哪个轴移多远。检查当前处于 Object Mode，避免只在同一网格里复制面而不是生成独立零件。

### 执行

1. 使用 Duplicate Objects 创建副本，立即沿计划轴移到目标位置，确认后退出移动状态。
2. 在 Outliner 给副本按作用命名，分别点击原件和副本核可独立选择。
3. 从正侧视图检查两件间距、对齐与是否穿插主体，必要时只改副本位置。
4. 保存重开，核原件原坐标不变且副本仍在；若将来要单独改材质，先核共享数据关系。

### 完成、常见问题与恢复

场景中有两件独立可选的相似零件，副本到位、原件未被移走。

- **看似只有一个：** 在 Outliner 数对象并检查副本是否与原件重叠。
- **复制了面不是对象：** 撤销，回 Object Mode 再复制。
- **改色两个一起变：** 检查是否共享材质，必要时创建独立材质数据。

### 假设与边界

这里只重复一件可视化零件，不自动生成阵列、机械对称或可制造装配。

### 来源

- [Blender 5.2 LTS Manual](https://docs.blender.org/manual/en/latest/scene_layout/object/editing/duplicate.html)（英文，官方手册）— Duplicate Objects 复制所选对象并进入移动状态，网格通常独立而材质可能共享。
- Original synthesis — 将一个原创三维模型结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an original prop needs a second foot, knob or repeated piece matching one existing object. Duplicate and place it deliberately. Finish with two separately selectable objects and the source still at its original position. An overlapping copy can look like only one object, and shared material data may affect later independent recoloring.

### Preparation and inputs

Save, select only the source piece and note its name and location. Decide which axis and approximate offset place the copy. Confirm Object Mode so you create a separate object rather than duplicate faces inside one mesh.

### Execution

1. Use Duplicate Objects, move the copy along the planned axis and confirm the move.
2. Name the copy for its role in Outliner and select source and copy separately.
3. Inspect spacing, alignment and intersections from front and side, adjusting only the copy as needed.
4. Save and reopen to confirm the source stayed put and copy persisted; check shared data before changing materials independently.

### Success, common problems, and recovery

Two separately selectable matching pieces exist, the copy is placed and the source did not move.

- **Only one visible:** Count objects in Outliner and inspect overlap.
- **Faces duplicated:** Undo and duplicate in Object Mode.
- **Both recolor:** Inspect shared material and make a separate material if needed.

### Assumptions and limits

This repeats one visual prop piece, not an automatic array, mechanical symmetry or manufacturable assembly.

### Sources

- [Blender 5.2 LTS Manual](https://docs.blender.org/manual/en/latest/scene_layout/object/editing/duplicate.html) — Duplicate Objects copies the selected object and enters move mode; mesh may be separate while materials can remain shared.
- Original synthesis — one original 3D-prop outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Blender controls. You choose the content, perform the steps and verify the result.

