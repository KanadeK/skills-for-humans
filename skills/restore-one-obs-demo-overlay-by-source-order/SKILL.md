---
name: restore-one-obs-demo-overlay-by-source-order
description: "Human recovery for one title or owned image hidden under an application capture in OBS by changing source stack order without changing source geometry."
---
# 用 OBS 来源顺序找回被盖住的演示叠层 / Restore One OBS Demo Overlay by Source Order

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有私有演示场景、被盖的标题或自有图片 / Private demo scene with hidden title or owned image |
| Side effects / 现实副作用 | 叠层在目标前后关系可见，主窗口仍完整 / Overlay visible at intended depth with main window intact |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你明明加了原创标题或自有小图，OBS 预览却看不到，原因可能是被单窗口源盖在下面。只改变来源列表前后次序，结果应是叠层在计划位置出现，窗口大小、裁切和隐私边界都保持。把标题拖到别处虽然也可能显露，却改变布局而没有解决层叠根因。

### 准备与输入

确认目标源在 Sources 列表中存在且眼睛图标可见；记下它在预览里本应占的位置。若源其实显示为错误文件或已被裁空，先处理相应原因，别把所有“看不见”都归到层叠。

### 执行

1. 在来源列表单选被盖的叠层，逐级上移到窗口捕获源上方。
2. 观察预览中叠层是否在原位置出现，核没有盖住应用按钮、状态或提示。
3. 开关叠层可见性，对照主窗口前后视觉，确认只改显示次序。
4. 录短测并重开文件，确认录像里的顺序和预览一致，保留场景设置。

### 完成、常见问题与恢复

叠层重新出现在预定位置，主窗口和其它来源的变换未被误改。

- **上移仍不见：** 检查源可见性、文件路径和裁切。
- **标题盖住关键内容：** 保持层级但调整位置或缩短标题。
- **主窗口消失：** 核是否把不透明大图抬到顶层，退回一步。

### 假设与边界

只修一处普通来源层叠问题，不处理插件渲染、音轨路由或真实隐私遮蔽。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide)（英文，官方手册）— Sources 列表上方来源会显示在下方来源前面，可调整顺序与可见性。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an original title or owned image exists in an OBS scene but disappears behind the app capture. Change source stack order so the overlay appears at its planned place while window size, crop and privacy boundary stay intact. Dragging the title elsewhere could reveal it without fixing the depth relationship.

### Preparation and inputs

Confirm the target source exists in Sources and its eye icon is enabled. Note its intended preview position. If the source points to a missing file or is cropped away, repair that cause rather than assuming every invisible item is a stack issue.

### Execution

1. Select the hidden overlay and move it one step at a time above the window capture source.
2. Check it appears in its original position without covering application controls or messages.
3. Toggle overlay visibility to verify the underlying app remains unchanged and only depth order moved.
4. Record and reopen a short test to confirm recorded order matches preview, then retain the scene setup.

### Success, common problems, and recovery

The overlay reappears in its planned place with window and other source transforms unchanged.

- **Still hidden:** Inspect eye state, file path and crop.
- **Covers controls:** Keep correct depth but reposition or shorten the title.
- **App disappears:** Check for an opaque full-frame image moved above it and step back.

### Assumptions and limits

This repairs one ordinary visual stack issue, not plugin rendering, audio routing or true privacy redaction.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/sources-guide) — Sources higher in the list appear above lower sources; order and visibility can be changed.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

