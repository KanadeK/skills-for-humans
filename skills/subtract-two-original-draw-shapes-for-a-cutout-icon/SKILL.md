---
name: subtract-two-original-draw-shapes-for-a-cutout-icon
description: "Human-readable subtraction of two original vector primitives in Draw to create one editable cutout silhouette while keeping a source copy."
---
# 在 Draw 用两个原创形状相减做镂空小图标 / Subtract Two Original Draw Shapes for a Cutout Icon

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 两个自画且重叠的简单形状、ODG 副本、明确镂空位置 / Two overlapping self-drawn simple shapes, ODG copy and intended cutout |
| Side effects / 现实副作用 | 形成一枚有真实空洞的原创矢量轮廓 / One original vector silhouette has a genuine opening |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你想给自画的普通说明图做一个简单镂空图标，比如环形标签，但不想靠同色填块假装中间透明时使用本篇。成果是前方形状从后方底形真实扣除，生成一个可选的矢量轮廓，原两个组件另有副本可回退。它不是临摹现成商标或制作行业安全符号。

### 准备与输入

保存 ODG 副本，在不影响主图的空白处复制两个自画形状作试验，明确哪个在前、哪个在后以及目标空洞。检查两者是否确实重叠，扣除后剩余轮廓仍足够宽可见。先不要对唯一原形状直接做相减。

### 执行

1. 将扣除用小形状置前、大底形置后，调整交叠到预定空洞。
2. 同时选两形，使用 Shape > Subtract，观察新形状是否真的透出页面背景。
3. 在深浅背景上核边缘、空洞与整体轮廓，确认不是两层假遮挡。
4. 保存重开，若扣反或轮廓断裂，从保留的原组件副本重做。

### 完成、常见问题与恢复

生成真实镂空的原创矢量对象，原形状仍可回退，轮廓在不同背景可辨。

- **整形消失：** 核前后叠放与选中顺序。
- **空洞是假色块：** 确认相减后只有一个对象且背景透出。
- **边缘太薄：** 从源副本调整重叠重做。

### 假设与边界

只做一个原创小图标轮廓，不证明商标独创性或安全标识合规。你负责使用许可与语义。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26205-CombiningMultipleObjects.html)（英文，官方手册）— Shape > Subtract 将前方对象从后方对象中扣出新形状。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill for a simple original cutout icon in an ordinary explanatory drawing, such as a ring-like marker, when a same-color cover would only fake a hole. Finish with a front shape genuinely subtracted from a rear shape into a selectable vector outline, and source primitives saved elsewhere for rollback. This is not copying a trademark or designing formal safety symbols.

### Preparation and inputs

Save ODG copy and duplicate two original primitives into safe workspace. Decide front subtractor, rear base and desired opening. Check overlap and enough remaining contour width. Do not subtract on sole originals.

### Execution

1. Place small subtractor in front and base behind, positioning overlap at planned opening.
2. Select both and use Shape > Subtract, checking the new hole reveals page background.
3. Inspect opening and contour on light/dark backgrounds to confirm it is not two-layer cover.
4. Save/reopen; for reversed subtraction or broken contour, retry from preserved primitives.

### Success, common problems, and recovery

A genuine open original vector object results, source primitives remain and contour reads on different backgrounds.

- **Whole shape disappears:** Check stacking and selection.
- **Fake color hole:** Verify one object and true opening.
- **Edge too thin:** Redo from source with different overlap.

### Assumptions and limits

This creates one original small icon outline, not trademark originality or safety-sign compliance. You own use rights and meaning.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26205-CombiningMultipleObjects.html) — Shape > Subtract removes front shape from rear to create a new outline.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.
