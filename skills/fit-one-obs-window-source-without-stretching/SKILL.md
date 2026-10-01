---
name: fit-one-obs-window-source-without-stretching
description: "Human workflow to fit a permitted application Window Capture inside one OBS canvas without distorting text or hiding necessary controls."
---
# 把 OBS 单窗口源等比放进演示画布 / Fit One OBS Window Source without Stretching

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已选定的获准窗口源和目标录制画布 / Selected permitted window source and recording canvas |
| Side effects / 现实副作用 | 窗口内容比例正确、关键文字与控件完整可见 / Window content keeps correct proportions with essential text and controls visible |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在 OBS 预览里已经抓到自己的应用窗口，但画面只占一角或被拉成宽脸时，先做等比适配。成果是窗口主要操作区域落在画布内，字形比例自然、没有被裁掉关键按钮。填满所有空白不一定是好事；窗口比例与画布不同可以留下有意留白。

### 准备与输入

保存当前场景集合状态，确认选中的来源是目标窗口而不是背景图或整场景。记录源窗口比例和关键菜单的位置；如果窗口内部有真实隐私，先清理而非靠缩小使它不易读。

### 执行

1. 在来源列表单选窗口源，用 Fit to Screen 或变换边框按比例适配到画布。
2. 检查源四边都在安全区内，关键操作按钮没有被画布边界遮住。
3. 短暂显示有明显几何比例的界面元素，核没有使用 Stretch to Screen 把字体或图像压扁。
4. 录一段短测并重开文件确认实际比例，保存该场景源位置。

### 完成、常见问题与恢复

录制文件里的应用窗口按原比例显示、关键内容完整，留白有意。

- **画面被拉宽：** 重置变换后用等比适配而非 Stretch。
- **按钮被裁：** 减小源或调整位置，不靠导出缩放修。
- **选错来源：** 在列表里核名称与预览红框再调整。

### 假设与边界

这里只做一个来源的画布适配，不改变应用自身分辨率或保证所有播放器字体清晰。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide)（英文，官方手册）— 来源边框、Edit Transform 与 Fit to Screen 用于摆位，Stretch 会改变比例。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when your permitted app window is captured but sits in a corner or looks stretched in OBS. Fit it proportionally so the important UI lies inside the canvas with natural letter shapes and visible controls. Filling every blank pixel is not required when source and canvas aspect ratios differ; intentional margin can be better.

### Preparation and inputs

Preserve the current scene setup and select the exact window source rather than background image or whole scene. Note its aspect ratio and key menu locations. Remove any private content from the window rather than relying on small scaling to make it less readable.

### Execution

1. Select only the window source and use Fit to Screen or its transform handles with aspect ratio preserved.
2. Inspect all edges and ensure essential controls remain inside safe frame bounds.
3. Inspect a familiar proportion in the app to confirm Stretch to Screen did not distort text or graphics.
4. Record and reopen a short test to verify the actual proportion, then retain the scene placement.

### Success, common problems, and recovery

The recorded app window keeps its native proportions and essential content, with deliberate rather than accidental margins.

- **Stretched:** Reset transform and fit proportionally instead of Stretch.
- **Control cropped:** Reduce source size or move it within canvas.
- **Wrong source:** Check source name and preview bounding box first.

### Assumptions and limits

This fits one source, not the app's internal resolution or universal text readability in every player.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide) — Source handles, Edit Transform and Fit to Screen position a source; Stretch changes its proportions.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

