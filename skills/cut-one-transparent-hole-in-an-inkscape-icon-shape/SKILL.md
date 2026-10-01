---
name: cut-one-transparent-hole-in-an-inkscape-icon-shape
description: "Human workflow to subtract one top cutter shape from an original icon body and verify a real transparent opening rather than a background-colored patch."
---
# 用 Inkscape Difference 在图标里挖一个真透明孔 / Cut One Transparent Hole in an Inkscape Icon Shape

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 已保存原创主体、作为切刀的一件形状和明确孔位置 / Saved original body, one cutter shape and intended hole position |
| Side effects / 现实副作用 | 主体里形成可透出背景的路径开口 / Main icon body has a true path opening revealing the background |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一枚原创图标需要一个把手孔或中心镂空，画一块和背景同色的补丁在换背景时会露馅。用 Difference 从主体里挖真孔，结果是孔能透出棋盘格或不同背景，边缘形状与计划相符。这个布尔操作会改变主体路径，切刀位置和上下层顺序要先核。

### 准备与输入

保存 SVG 或复制主体与切刀，确定孔大小、离外轮廓的最小可见边。让切刀位于主体上方并只选这两个对象；若切刀碰到外边缘，得到的可能是缺口而不是封闭孔。

### 执行

1. 把切刀形状放在孔的计划位置，暂用对比色核它与主体外边缘的距离。
2. 执行 Path > Difference，核上方切刀被消耗，下方主体出现开口。
3. 换一块临时背景色或用透明检查，确认孔真正透出背后，而不是有一块白色对象。
4. 缩到目标尺寸核孔不会糊掉，保存重开；若切坏外轮廓，撤销并移动切刀。

### 完成、常见问题与恢复

图标主体中有一个真实透明孔，小尺寸仍能辨，主体外轮廓和页边未被误切。

- **整个主体消失：** 核上下顺序，恢复源形状后重做 Difference。
- **孔变缺口：** 缩小或内移切刀，留完整边缘。
- **孔其实是白块：** 检查是否仍有独立白色对象，改为真实路径差集。

### 假设与边界

只处理一处普通原创图标镂空，不用于正式防伪标识、激光切割或制造图。

### 来源

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/boolean-operations.html)（英文，官方手册）— Difference 从下方对象减去上方路径，堆叠顺序影响结果。
- Original synthesis — 将一个原创矢量图形结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an original icon needs a handle hole or central cutout. A patch painted the current background color will fail on another background; Difference should create a real transparent opening. The result must reveal whatever sits behind it, with a planned edge. This Boolean edit changes the body path, so cutter position and stack order matter.

### Preparation and inputs

Save or copy body and cutter. Decide hole size and remaining visible rim. Put cutter above body and select only those two. If the cutter crosses the outside edge, the result may be an open notch rather than a closed hole.

### Execution

1. Place the cutter at the intended hole and use temporary contrast to check its distance from the body edge.
2. Run Path > Difference, confirming the upper cutter is consumed and the body now has an opening.
3. Change a temporary background color or inspect transparency to prove the hole exposes what is behind it rather than a white patch.
4. At target size check the hole remains visible, save and reopen; undo and reposition the cutter if the outer silhouette was damaged.

### Success, common problems, and recovery

The icon body has a genuine transparent opening visible when small, with outer silhouette and page edge intact.

- **Body disappears:** Check stacking and restore source shapes before redoing Difference.
- **Hole becomes notch:** Shrink or move cutter inward to leave a rim.
- **White patch:** Inspect separate white object and create a true path subtraction.

### Assumptions and limits

This cuts one ordinary original icon hole, not an anti-counterfeit mark, laser-cutting file or manufacturing drawing.

### Sources

- [Inkscape Beginners' Guide](https://inkscape-manuals.readthedocs.io/en/latest/boolean-operations.html) — Difference subtracts the upper path from the lower object, so stack order affects the result.
- Original synthesis — one original vector-art outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Inkscape controls. You choose the content, perform the steps and verify the result.

