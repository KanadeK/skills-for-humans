---
name: crop-one-irrelevant-obs-window-edge
description: "Human workflow to crop one nonessential border or sidebar from a permitted window source while verifying no instruction or private content is hidden deceptively."
---
# 裁掉 OBS 单窗口源的一处无关边缘 / Crop One Irrelevant OBS Window Edge

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已获准的单窗口源、明确无关的一侧边缘 / Permitted single-window source and one clearly irrelevant edge |
| Side effects / 现实副作用 | 录制区域更聚焦，必要操作信息仍完整 / More focused capture with necessary operation information intact |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在录制自己应用时，窗口一侧留了大量空白工具区，真正操作区域因此太小，可只裁掉这处无关边。成果是内容更聚焦而关键步骤、错误提示和上下文仍完整。裁切不能用来伪造操作结果或掩盖会改变判断的重要信息，录前应明确哪些边界可以丢。

### 准备与输入

保存场景，指出要裁的是哪一侧和大致宽度。按实际操作走一遍，确认这块区域在整个演示期间都不包含必要控件、状态或个人数据；若时有重要提示，改缩放布局而不要裁。

### 执行

1. 选单一窗口源，用 Edit Transform 裁切项或裁切手势从目标边缘逐步收进。
2. 观察红框与预览，核主体仍在画面中，关键菜单文字未被截。
3. 在实际操作流程中触发无敏感示例提示，确认它不会被裁掉而导致录像意义改变。
4. 录短测并重开，核四边与时间中的弹窗；不合适就恢复裁切参数。

### 完成、常见问题与恢复

目标无关边被裁，实际录像更可读，重要控制与状态仍在画面里。

- **提示被切掉：** 撤回裁切，保留该区域或重新安排窗口。
- **比例变怪：** 裁切后按比例重新适配来源。
- **源被裁成黑屏：** 重置源变换并从小范围重试。

### 假设与边界

这里只裁一处非关键视觉边缘，不提供真实性认证、隐私删除或后期剪辑。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide)（英文，官方手册）— 来源可通过变换编辑或 Alt/Option 拖边执行裁切。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when one side of your own application window has irrelevant blank chrome that makes the actual demonstration too small. Crop that edge to focus the view while retaining controls, error messages and context needed to understand the action. Do not use crop to misrepresent what happened or conceal material information.

### Preparation and inputs

Preserve the scene and name which side and approximate width to remove. Walk through the intended operation to ensure that region never contains a needed control, status or private data. If important prompts appear there, use layout changes rather than cropping.

### Execution

1. Select the one window source and crop incrementally from the planned edge via Edit Transform or crop handles.
2. Inspect source bounds and preview for retained subject and uncropped key labels.
3. Trigger a harmless example prompt during the workflow to ensure cropping does not remove information that changes the recording's meaning.
4. Record and reopen a short test for all edges and transient dialogs; restore crop parameters if unsuitable.

### Success, common problems, and recovery

The irrelevant edge is removed and the real test is more readable while necessary controls and status remain visible.

- **Prompt missing:** Undo the crop and retain the region or rearrange the app.
- **Aspect feels wrong:** Refit the cropped source proportionally.
- **Black or empty:** Reset transform and retry a smaller crop.

### Assumptions and limits

This crops one nonessential visual edge, not authenticity certification, privacy deletion or postproduction editing.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide) — Source crop can be made through Edit Transform or Alt/Option dragging handles.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

