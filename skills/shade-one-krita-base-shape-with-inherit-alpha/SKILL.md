---
name: shade-one-krita-base-shape-with-inherit-alpha
description: "Human workflow to put one shadow on a separate layer clipped to an original base shape within a Krita group, verifying no spill beyond silhouette."
---
# 用 Krita 继承 Alpha 在一块底色里加阴影 / Shade One Krita Base Shape with Inherit Alpha

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 一块独立透明底色、其上新阴影层和已保存 .kra / Separate transparent base shape, new shadow layer and saved .kra |
| Side effects / 现实副作用 | 一片只出现在底色轮廓内且可关掉的阴影 / One toggleable shadow confined to the base silhouette |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有一块独立透明的平色，想为它增加一片可改动的阴影而不越出形状时，可用组内继承 Alpha。完成后阴影只在那块底色的剪影里出现，关掉阴影层即可回到原平色。关键是组里下方真正负责界限的是物体底色，若把整张不透明背景放进去，约束可能变成全画布。

### 准备与输入

保存 .kra，确认底色层外是透明而不是白色像素，准备只容纳这一物体的图层组。另建阴影层并选更暗但仍能看清主体的颜色；先决定受光方向，不在同一形状里随机加深所有边。

### 执行

1. 把底色放在组的下方、阴影层放在同组上方，打开阴影层的 Inherit Alpha。
2. 先用明显颜色在边界上短试一笔，核组外背景未出现笔触；撤销试笔后再画实际阴影。
3. 沿既定受光方向画一小片阴影，避免整个形状被暗色盖掉；正常比例看体积是否更清楚。
4. 关闭阴影层验证底色未变，再开启并保存工程；若外溢先核组内底层而不是继续擦阴影。

### 完成、常见问题与恢复

阴影只影响目标物体的透明底色范围，原平色与阴影可分别编辑和隐藏。

- **画到整张纸：** 检查组里是否有不透明背景，移出后再试。
- **阴影看不见：** 核阴影层位置、继承 Alpha 和底色层实际透明范围。
- **颜色太脏：** 降低阴影层不透明度或重新选明度。

### 假设与边界

只为一块原创底色加简单阴影，不等于照片蒙版、真实物理光照或全画面自动调色。继承 Alpha 的实际效果需在当前图层组合里试验。

### 来源

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/layers_and_masks.html)（英文，官方手册）— 继承 Alpha 以同组下方图层的像素透明范围限制上层显示，背景层位置会影响结果。
- Original synthesis — 将一个数字绘画结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a transparent base-color shape needs one adjustable shadow confined to its silhouette. The shadow should disappear when its own layer is hidden, leaving the flat intact. The lower layer in the group must actually represent the object boundary; a full opaque background can make the inherited area span the entire canvas.

### Preparation and inputs

Save the .kra and verify transparent pixels outside the base, not white paint. Prepare a group for this object and a separate shadow layer above its base. Choose a darker readable color and decide the light direction before adding an arbitrary dark rim.

### Execution

1. Place the base at the bottom of its group and shadow above it, then enable Inherit Alpha on the shadow layer.
2. Make one conspicuous trial across the edge to confirm nothing appears outside the object; undo it before drawing the real shadow.
3. Paint a small shadow consistent with the light direction, avoiding a full opaque cover; inspect whether the form reads better at normal scale.
4. Hide shadow to verify the base is untouched, restore it and save; if paint spills, inspect the group's lower layers before erasing.

### Success, common problems, and recovery

Shadow appears only within the intended base silhouette, while flat and shadow remain separately editable and toggleable.

- **Full-canvas paint:** Inspect the group for an opaque background and move it out before retrying.
- **Invisible shadow:** Check layer order, Inherit Alpha and the base's real alpha.
- **Muddy color:** Reduce shadow opacity or reconsider its value.

### Assumptions and limits

This adds one simple shadow to an original flat, not photo masking, physically accurate lighting or automatic global grading. Verify inheritance against the current group.

### Sources

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/layers_and_masks.html) — Inherit Alpha clips an upper layer to lower layers within its group, with background placement affecting the result.
- Original synthesis — one digital-painting outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Krita controls. You choose the content, perform the steps and verify the result.

