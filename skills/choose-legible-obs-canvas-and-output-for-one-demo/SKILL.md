---
name: choose-legible-obs-canvas-and-output-for-one-demo
description: "Human workflow to match OBS base canvas, scaled output and frame rate to an owned app demonstration, verified by a short private test."
---
# 为一段 OBS 演示选择可读的画布与输出尺寸 / Choose Legible OBS Canvas and Output for One Demo

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 获准应用窗口、预期观看设备和本机录制 Profile / Permitted app window, viewing device and local recording Profile |
| Side effects / 现实副作用 | 测试文件里文字清楚、比例正确且帧速不明显卡顿 / Test file has readable text, correct proportions and no obvious cadence problem |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你准备录自己应用里的操作，OBS 默认画布可能让小字缩得看不清或输出帧率高到设备掉帧。为这段演示选一个与窗口比例相符的画布和可读输出，结果要由几秒真实录制文件证明。分辨率数字越大不必然越清楚，窗口本身字体大小与缩放也会影响读者。

### 准备与输入

确认源窗口只含获准演示内容，记录其横竖比例和关键菜单字的大小。检查本机 Profile 当前 Base Canvas、Output Scaled 和 FPS；如果改变 Base Canvas，原有来源位置可能要重排，先保存集合配置。

### 执行

1. 在 Video 设置中选画布比例与源窗口大致匹配，输出尺寸足以让关键文字可读。
2. 选设备可承受的帧率，避免只按某个通用最高值决定。
3. 录一段只含自有窗口的短测试，重开文件检查文字、画面是否拉伸和动作流畅度。
4. 若字糊，先调窗口字体或捕获区域，再有依据地调整输出，记录有效组合。

### 完成、常见问题与恢复

实际测试文件在目标设备上能读出关键操作文字，画面比例正确且无明显负荷故障。

- **字太小：** 先增应用字体或只捕获相关区域。
- **画面被拉宽：** 核源与画布比例，使用等比适配。
- **掉帧：** 降低输出负荷并重录短测试。

### 假设与边界

只为一段本地演示找可读设置，不保证所有设备播放、专业编码或直播带宽。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/obs-studio-overview)（英文，官方手册）— Video 设置区分 Base Canvas、Output Scaled 分辨率和帧率，需实测设备负荷。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an owned app demonstration would make small text unreadable or overload OBS at default video settings. Choose base canvas, output size and frame rate suited to the source and viewer, then verify with a short actual file. Bigger resolution numbers do not automatically improve readability when the app's own text is tiny.

### Preparation and inputs

Confirm the window contains only permitted demo material, and note its aspect ratio and important menu text size. Inspect current Base Canvas, Output Scaled and FPS. Changing the base canvas may reposition existing sources, so preserve the collection setup first.

### Execution

1. Set a base canvas roughly matching the source aspect ratio and an output size that can preserve essential text.
2. Choose a frame rate the device can sustain rather than a generic maximum.
3. Record a brief owned-window test and reopen it to inspect text, stretching and motion cadence.
4. If text is soft, improve source text size or crop before changing output again, then record the combination that worked.

### Success, common problems, and recovery

An actual test file shows readable essential UI, correct aspect ratio and no obvious device overload.

- **Tiny text:** Increase app text size or capture only the relevant area.
- **Stretched view:** Check source/canvas ratio and fit proportionally.
- **Dropped frames:** Reduce output load and run another short test.

### Assumptions and limits

This tunes one local demo, not playback on every device, professional encoding or streaming bandwidth.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/obs-studio-overview) — Video settings separate Base Canvas, Output Scaled resolution and FPS and require a real device test.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

