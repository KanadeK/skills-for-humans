---
name: repair-one-krita-flat-fill-leak-at-a-line-gap
description: "Human recovery for one Krita Fill Tool spill caused by a line-art gap, using a local contour or fill-boundary fix and verifying no outside paint remains."
---
# 修好一处 Krita 平色沿线稿缺口外漏 / Repair One Krita Flat-Fill Leak at a Line Gap

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 能撤销的漏色、可见线稿和独立平色层 / Reversible fill spill, visible ink and separate flat layer |
| Side effects / 现实副作用 | 目标区域保留平色而轮廓外恢复原样 / Intended flat remains while outside area returns unchanged |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你给一块封闭形状上色时，颜色顺着小缺口跑到外面；此时的结果不是再给整张图盖一层颜色，而是找到这一个泄漏点、修好并重新核填色边缘。修复要保住已画好的线稿、其他平色和画面留白。若漏点太大或边界含糊，应回原画决定轮廓，而不是让高阈值替你猜。

### 准备与输入

立即撤销漏色或保留可对照副本，选中正确的平色层与线稿参考层。放大沿着色块边缘找实际漏口，不要只在漏出最大的一角擦一擦；那里可能只是扩散终点而非原因。

### 执行

1. 观察缺口是否应由线稿闭合；若应闭合，在原线稿层补一小段有意边线，再核线条形状。
2. 若只是抗锯齿的小缝，尝试 Fill Tool 的适度 Close Gap 或边界设置，先在可撤销状态重填一次。
3. 放大巡查缺口、相邻细线和画布外侧，确认没有新的外溢或吞掉本应透明的细节。
4. 回正常观看尺寸开关平色层，确认只目标形状变色，保存原稿；若仍不能确定轮廓，停在未填状态。

### 完成、常见问题与恢复

颜色只留在目标形状内，缺口或设置的改动可解释，周围线条和留白未被误染。

- **仍向外漏：** 撤销，继续沿边定位另一个开口。
- **填不满边缘：** 微调扩展而非大范围提高阈值。
- **线被补得太粗：** 撤销并用原线宽重画一小段。

### 假设与边界

只恢复一处普通插画的漏色，不会自动理解复杂开放轮廓、剪影语义或多色图层。若线条本来有意敞开，先由画者重定上色范围。

### 来源

- [Krita 5.3 Manual](https://docs.krita.org/en/reference_manual/tools/fill.html)（英文，官方手册）— 填充工具的 Close Gap 和边界选项可影响相邻填充在小缺口处的传播。
- Original synthesis — 将一个数字绘画结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a flat fill escapes a supposedly closed contour through one small gap. Finish by identifying the leak, repairing the local boundary or fill setting and restoring the outside area. Preserve existing ink, other flats and intentional empty space. If the gap is large or the contour ambiguous, decide the shape rather than asking an aggressive threshold to guess it.

### Preparation and inputs

Undo the spill or keep a comparison copy, then select the correct flat and ink reference layers. Zoom along the boundary to find the actual opening; the largest spill area may be only where propagation ended, not where it escaped.

### Execution

1. Decide whether the ink contour should truly close. If yes, add a small deliberate ink segment and inspect its form.
2. For a tiny antialiased gap, try a modest Close Gap or boundary setting and refill once in a reversible state.
3. Inspect the former gap, nearby thin lines and the outside at high zoom for new spills or lost transparent details.
4. Toggle the flat layer at normal size to confirm only the target shape changed, then save; if the contour remains uncertain, stop with the region unfilled.

### Success, common problems, and recovery

Color stays inside the intended shape, the boundary change is explainable, and surrounding ink and empty space remain intact.

- **Still spills:** Undo and inspect the entire perimeter for another opening.
- **Halo remains:** Adjust edge growth narrowly rather than raising threshold globally.
- **Thick patch:** Undo and redraw the local segment at the original ink width.

### Assumptions and limits

This repairs one ordinary fill leak, not semantic interpretation of complex open contours or multi-color layers. If the line was intentionally open, you must redefine the intended color region first.

### Sources

- [Krita 5.3 Manual](https://docs.krita.org/en/reference_manual/tools/fill.html) — Fill Tool Close Gap and boundary options control propagation through small gaps.
- Original synthesis — one digital-painting outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Krita controls. You choose the content, perform the steps and verify the result.

