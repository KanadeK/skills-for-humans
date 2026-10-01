---
name: extrude-one-blender-prop-face-into-a-raised-feature
description: "Human workflow to extrude one selected face into a shallow connected prop feature and verify depth, side faces and normal orientation."
---
# 从 Blender 道具一张面挤出一个低凸起 / Extrude One Blender Prop Face into a Raised Feature

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 已保存原创建模网格、准确选中的一张目标面 / Saved original mesh and accurately selected target face |
| Side effects / 现实副作用 | 一个与主体连成网格的浅凸起，侧面完整 / One shallow raised feature connected to the mesh with intact side faces |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有简单道具主体，草图上要求在一张面上加浅按钮或连接凸台时，挤出一次而不是叠放一个看似相连的独立物体。成果是顶部新面、四周侧面与主体连续，凸起深度适中。挤出命令取消移动也可能留下重合新面，因此出现奇怪闪烁时应检查是否有零距离挤出。

### 准备与输入

保存 .blend，确认只选中计划面，写下大致挤出方向和深度。先从正侧视图看原面与邻件距离，避免一挤出就穿过另一零件；若当前有镜像修饰器，先了解对侧会同步预览。

### 执行

1. 在 Edit Mode 对目标面运行 Extrude Faces，沿面法线或指定轴移动一个克制距离并确认。
2. 从侧面看新顶面和周围侧面是否出现，核它们连在同一网格而不是只移动旧面。
3. 开 Face Orientation 或合适显示检查新面朝向，发现重叠或零深度就撤销重做。
4. 回 Object Mode 从正常观看大小评估形状，保存并重开。

### 完成、常见问题与恢复

目标面生出一个深度合理的连续凸起，侧面和顶面完整，邻近零件未误改。

- **只见闪烁：** 检查零距离重复面，撤销挤出后重做。
- **方向反了：** 撤销并核法线及目标轴。
- **挤到邻件里：** 减小深度或回草图改结构。

### 假设与边界

只做一处可视化浅凸起，不保证封闭流形、机械强度或可打印公差。

### 来源

- [Blender 5.2 LTS Manual](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/face/extrude_faces.html)（英文，官方手册）— Extrude Faces 从选中面边界创建新侧面并沿轴移动，需确认挤出深度。
- Original synthesis — 将一个原创三维模型结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an original prop body needs a shallow button or raised connector from one face. One extrusion should create a top and connected side faces rather than a separate overlapping object. Keep the depth deliberate. Canceling the movement portion can leave overlapping geometry, so flicker after a failed attempt calls for an actual mesh check.

### Preparation and inputs

Save, confirm the one planned face is selected and note direction and approximate depth. Inspect side and front clearance so the feature does not pass through another piece. If a Mirror modifier is active, expect the opposite side to update in preview.

### Execution

1. In Edit Mode run Extrude Faces on the target, move a modest distance along its normal or chosen axis and confirm.
2. Inspect from the side for a new cap and surrounding faces connected to the same mesh.
3. Inspect orientation and look for overlapping or zero-depth geometry, undoing and retrying if needed.
4. Return to Object Mode, judge the silhouette at normal size and save/reopen.

### Success, common problems, and recovery

The target surface has a connected, shallow feature with cap and sides intact and neighboring pieces unchanged.

- **Flicker:** Inspect for a zero-distance duplicate face and undo before retrying.
- **Wrong direction:** Undo and inspect normal and chosen axis.
- **Intersects neighbor:** Reduce depth or revise the sketch structure.

### Assumptions and limits

This adds one visual raised feature, not a guarantee of manifold topology, mechanical strength or printable tolerance.

### Sources

- [Blender 5.2 LTS Manual](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/face/extrude_faces.html) — Extrude Faces creates side faces around the selection and moves the new face along an axis.
- Original synthesis — one original 3D-prop outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Blender controls. You choose the content, perform the steps and verify the result.

