---
name: mirror-view-check-one-krita-illustration-balance
description: "Human review of one original painting in Krita's mirrored view to spot composition imbalance and decide on a concrete edit without flipping image data."
---
# 镜像查看一张 Krita 插画的构图平衡 / Mirror-View Check One Krita Illustration's Balance

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存的原创插画和可见的主要主体 / Saved original illustration with visible main subject |
| Side effects / 现实副作用 | 一条基于镜像观察的具体修正决定或保留理由 / One concrete revision decision or reason to keep the composition |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你盯着原创插画太久，觉得构图顺眼却说不出主体是否偏斜时，用镜像视图做一次短复核。结果是发现一处具体不平衡并决定是否改，或明确记录暂不改的理由。这里翻的是观察视角，不应无意把真正的图像数据左右反转后导出。

### 准备与输入

先保存 .kra，在正常视图记主体中心、留白和视觉重量。若画里有文字或方向性符号，标明它们最终朝向，以免把镜像检查时的反字误当正式作品。选择能看到整张画的缩放比例。

### 执行

1. 使用 Mirror View 切换画布观察方向，确认图层和文件内容本身没有被变换。
2. 比较镜像下主体左右重量、视线方向和边缘留白，指出最多一两处具体问题。
3. 切回正常视图，再判断问题是否仍真实；若要调整，记录要移动的元素或要改的线，不在镜像状态下凭冲动大改。
4. 若本次只做复核，留下“保留/调整”的一句结论并保存；若已改动，再镜像与正常各看一次。

### 完成、常见问题与恢复

完成一次镜像与正常双视角比较，得出有具体对象的修正或保留决定，实际图像朝向未被误改。

- **导出是反的：** 核是否用了 Image 镜像命令，撤销数据变换后重导。
- **只觉着不舒服：** 回到主次、留白或方向三个可描述维度。
- **文字看反：** 切回正常视图核最终字向。

### 假设与边界

这是一项主观构图检查，不是对称评分、解剖诊断或自动审美结论。镜像视图只帮你重新观察，是否修改由画者决定。

### 来源

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/getting_started/navigation.html)（英文，官方手册）— 画布导航的 Mirror View 用于水平镜像观察，并不必改变图像本身。
- Original synthesis — 将一个数字绘画结果、原稿对照和失败停点组合为可核流程。

## English

Use this after looking at your original illustration long enough that its balance is hard to judge. Mirror the view briefly and identify one concrete imbalance to revise, or record why the composition should stay. This is a viewing check; it should not silently flip the actual image pixels for export.

### Preparation and inputs

Save the .kra and note subject center, negative space and visual weight in normal view. If the art has text or directional symbols, note their intended final orientation so reversed letters during review are not mistaken for an export defect. Fit the whole picture on screen.

### Execution

1. Toggle Mirror View and confirm layers and the actual file content have not been transformed.
2. Compare left-right visual weight, gaze direction and margin spacing in the mirrored view, identifying at most one or two concrete issues.
3. Return to normal view and decide whether the concern remains. If it does, name the element or line to change before making broad edits.
4. Record a one-sentence keep-or-revise decision and save. If you made a revision, inspect once in both normal and mirrored views.

### Success, common problems, and recovery

A normal/mirrored comparison produces a concrete keep-or-revise decision while actual image orientation stays unchanged.

- **Export reversed:** Check for an Image mirror operation and undo pixel transformation before exporting again.
- **Vague discomfort:** Name a specific hierarchy, spacing or directional issue.
- **Reversed text:** Return to normal view before judging final lettering.

### Assumptions and limits

This is a subjective composition check, not a symmetry score, anatomy diagnosis or automatic aesthetic judgment. Mirroring offers a fresh view; you make the edit decision.

### Sources

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/getting_started/navigation.html) — Canvas navigation's Mirror View supports horizontally mirrored review without changing image content.
- Original synthesis — one digital-painting outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Krita controls. You choose the content, perform the steps and verify the result.

