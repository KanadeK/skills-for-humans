---
name: capture-only-one-permitted-app-window-in-obs
description: "Human workflow to add a single permitted application Window Capture to an OBS scene and verify that desktop and private notifications stay outside the recorded area."
---
# 在 OBS 只捕获一扇获准的应用窗口 / Capture Only One Permitted App Window in OBS

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 本人应用的无敏感演示窗口、独立 OBS 场景 / Own non-sensitive demo window and isolated OBS scene |
| Side effects / 现实副作用 | 预览与短测只出现目标窗口，没有桌面或私人通知 / Preview and short test show only target window, without desktop or private notifications |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你要演示自己应用里的一个操作，却不希望录到整个桌面、任务栏或弹出的私人通知时，只捕获那扇获准窗口。结果必须在预览和几秒实际录像里都只见目标应用。窗口标题和内容可能变化，开始正式录制前还要再检查一次；“只加了一个源”本身不证明源类型选对。

### 准备与输入

关闭或移走会弹出隐私内容的应用，给目标窗口准备虚构或公开演示数据。确认场景里没有 Display Capture、浏览器源或旧摄像头；OBS 32.2 新增源对话框与早期截图不同，应按当前可见类型选择。

### 执行

1. 在当前场景中添加 Window Capture 或本平台等价的单窗口捕获源，明确选目标应用窗口。
2. 核预览只显示该窗口，切换桌面或弹一个无敏感测试通知，确认录制范围不扩到全屏。
3. 录几秒无敏感测试片并重开，检查标题栏和边缘是否带入不该出现的信息。
4. 清理目标窗口里的真实资料后重新核源选中的窗口，再进入正式录制。

### 完成、常见问题与恢复

实际测试只包含获准窗口的演示内容，不含桌面、无关窗口或私人通知。

- **录到全屏：** 停止并移除 Display Capture，改选单窗口源。
- **抓错窗口：** 在源属性重选准确标题并再录短测。
- **窗口内仍有隐私：** 停录并清理内容，旧文件按实际权限处理。

### 假设与边界

只录自己或明确获准的无敏感应用窗口，不授权他人屏幕、隐藏拍摄、会议录制或直播。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide)（英文，官方手册）— Sources Guide 区分 Window Capture 与 Display Capture，并示范来源添加和预览。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when demonstrating an operation in your own app without recording the desktop, taskbar or private notifications. Add a source for that permitted window and prove in both preview and a short file that only the target is visible. Window titles and content can change; recheck immediately before the actual recording.

### Preparation and inputs

Close apps likely to show private popups and prepare fictional or public demo data in the target app. Confirm the scene lacks Display Capture, browser sources or old cameras. OBS 32.2's new source dialog differs from older screenshots, so use its visible source type labels.

### Execution

1. Add Window Capture or the platform-equivalent single-window source and select the exact target app window.
2. Check preview shows only that window; change desktop view or use a harmless test notification to ensure capture does not expand to full display.
3. Record a few harmless seconds and reopen the file, inspecting title bar and edges for unintended information.
4. Remove any real sensitive data from the target and recheck the selected window immediately before actual capture.

### Success, common problems, and recovery

The actual test file contains only the permitted app demonstration, with no desktop, unrelated window or private notification.

- **Whole display appears:** Stop and remove Display Capture, then use a single-window source.
- **Wrong window:** Reselect exact window in source properties and retest.
- **Private data inside:** Stop recording and remove the content before retrying.

### Assumptions and limits

This covers your own or explicitly permitted non-sensitive app window, not another person's screen, covert capture, meeting recording or livestream.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide) — Sources Guide distinguishes Window Capture from Display Capture and explains source creation and preview.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

