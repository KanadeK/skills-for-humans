---
name: add-and-size-one-blender-mesh-primitive-for-a-prop
description: "Human workflow to add one cube or cylinder mesh primitive to an original prop scene and size it to a sketch while checking dimensions and object identity."
---
# 为 Blender 原创道具添加并定好一个基础网格 / Add and Size One Blender Mesh Primitive for a Prop

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存场景、原创道具草图和一项基础形状 / Saved scene, original prop sketch and one intended base shape |
| Side effects / 现实副作用 | 一件名称明确、尺寸与草图相符的基础网格物体 / One named base mesh object sized to the sketch |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一张简单原创道具草图，需要一块底座或主体体积时，先放一个合适基础体而不是同时堆很多形状。成果是一个已命名、大小和方向接近草图的立方体或圆柱，后续可继续编辑。选基础体只是获得几何起点，不等于做成完整模型，也不保证真实制造尺寸。

### 准备与输入

保存场景，指出草图哪一块将由这个基础体代表，选择立方体还是圆柱以及大致长宽高。核当前 3D 光标位置和场景单位，避免新物体生成在视野之外或与已有物体完全重叠。

### 执行

1. 在 Object Mode 通过 Add Mesh 选所需基础体，只创建一个新物体。
2. 在 Outliner 给它按作用命名，确认当前选择确实是新物体而非相机或旧零件。
3. 按草图调整长宽高，查看正面和侧面轮廓，不只在斜视角凭视觉猜尺寸。
4. 核它与其他对象不发生无意重叠，保存并重开确认基础体仍在正确位置。

### 完成、常见问题与恢复

一个基础体以明确名称和合理比例存在场景，后续可独立选择编辑。

- **新物体看不到：** 在 Outliner 选它并 Frame Selected，核光标位置。
- **尺寸不一致：** 用统一单位核对象尺寸，分别看正侧视图。
- **误选旧物件：** 先撤销并在 Outliner 核新对象名。

### 假设与边界

只创建一个普通可视化道具基础体，不制作复杂拓扑、机械配合或可打印实体。

### 来源

- [Blender 5.2 LTS Manual](https://docs.blender.org/manual/en/latest/modeling/meshes/primitives.html)（英文，官方手册）— Blender 网格基础体如立方体和圆柱可作为建模起点。
- Original synthesis — 将一个原创三维模型结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an original prop sketch calls for a base or main mass. Add one suitable primitive rather than scattering many shapes at once. Finish with a named cube or cylinder whose dimensions and orientation roughly match the sketch and can be edited later. A primitive is a geometric starting point, not a finished model or manufacturing specification.

### Preparation and inputs

Save the scene and identify which part of the sketch this base represents. Choose cube or cylinder with approximate proportions. Inspect 3D cursor and scene units so the new object does not spawn outside view or exactly on top of another piece.

### Execution

1. In Object Mode use Add > Mesh for the chosen primitive, creating one new object.
2. Name it for its role in the Outliner and confirm selection is the new mesh, not camera or an older piece.
3. Adjust dimensions to the sketch and inspect front and side silhouettes rather than estimating from one angled view.
4. Check it does not unintentionally overlap other objects, then save and reopen to confirm its location.

### Success, common problems, and recovery

One named, proportionate base primitive exists in the scene and remains independently selectable for later editing.

- **Invisible object:** Select it in Outliner, frame it and inspect cursor position.
- **Wrong proportions:** Inspect dimensions in one unit system and both front and side views.
- **Old object selected:** Undo and verify the new object in Outliner.

### Assumptions and limits

This creates one simple visual prop base, not complex topology, mechanical fit or a printable solid.

### Sources

- [Blender 5.2 LTS Manual](https://docs.blender.org/manual/en/latest/modeling/meshes/primitives.html) — Blender mesh primitives such as cube and cylinder provide starting geometry.
- Original synthesis — one original 3D-prop outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Blender controls. You choose the content, perform the steps and verify the result.

