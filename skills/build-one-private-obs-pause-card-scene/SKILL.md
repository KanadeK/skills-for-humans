---
name: build-one-private-obs-pause-card-scene
description: "Human workflow to create a second local OBS scene with a plain owned pause card and verify switching hides the application window in the recorded output."
---
# 给 OBS 私有演示做一页不露窗口的暂停场景 / Build One Private OBS Pause Card Scene

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 已有获准演示主场景、自写暂停文字和私有场景集合 / Permitted main demo scene, self-written pause text and private Scene Collection |
| Side effects / 现实副作用 | 切到暂停场景后录像只见暂停卡，不再见应用窗口 / Recording shows only the pause card when that scene is active |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你录自己应用的操作，中途需要查资料或暂停处理窗口内容，不能让录制继续暴露窗口时，准备一页单独暂停场景。成果是切过去后画面只显示本人写的“暂停”等普通文字和无敏感背景；切回主场景才再次显示应用。场景切换是画面控制，不保证麦克风自动静音，所以声音也要单独核。

### 准备与输入

确认当前独立场景集合只用于本机录制，主场景里有获准窗口源。写一条不含身份或账号的暂停提示，选纯色背景；不要在暂停卡里再引用主场景或直播聊天源。

### 执行

1. 新建第二场景并命名“暂停”或等价名称，添加纯色与本地文字源。
2. 核暂停场景 Sources 列表没有窗口捕获、摄像头或不需要的声音设备。
3. 在主场景与暂停场景之间切换，观察预览中的应用窗口是否完全消失并再恢复。
4. 录短测重开，核切换前后画面与声音；必要时为暂停段设置独立静音动作。

### 完成、常见问题与恢复

实际录像切到暂停时不露应用内容，返回时窗口恢复，声音状态另经核对。

- **暂停仍露窗口：** 查暂停场景是否复用了主源或嵌套主场景。
- **声音继续录：** 核全局音频与静音，不把纯色画面当静音证据。
- **切回错场景：** 明确场景名称和顺序，再做短测。

### 假设与边界

这里只控制本地录像的可见场景，不实现直播遮挡、敏感数据删除或自动暂停录制。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/obs-studio-overview)（英文，官方手册）— Scenes 可包含不同 Sources 并在录制时切换，当前场景决定可见画面。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a private app demonstration must pause while you check information or change the target window. A separate pause scene should show only neutral self-written text and a non-sensitive background until you return to the main scene. Scene switching controls visuals but does not automatically guarantee microphone silence, so review audio separately.

### Preparation and inputs

Confirm the dedicated collection is for local recording and the main scene has only permitted window capture. Write a neutral pause message without identity or account details and choose a plain background. Do not nest the main scene or a stream chat source inside the pause scene.

### Execution

1. Create a second scene named Pause or equivalent, with plain color and local text sources.
2. Inspect its Sources list for absence of window capture, camera and unintended audio devices.
3. Switch between main and pause scenes to see the app window fully disappear and return only when planned.
4. Record and reopen a short test, checking picture and sound across the switch; use a separate mute action if needed.

### Success, common problems, and recovery

The real test hides application content in the pause section and restores it afterward, with audio state checked separately.

- **Window still visible:** Inspect reused sources or nested main scene.
- **Audio continues:** Check global audio and mute state.
- **Wrong return:** Use unambiguous scene names and retest.

### Assumptions and limits

This controls visible scenes in a local recording, not livestream masking, sensitive-data deletion or automatic pause of recording.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/obs-studio-overview) — Scenes contain distinct sources and can be switched so the active scene determines visible output.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

