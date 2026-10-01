---
name: capture-only-permitted-windows-app-audio-in-obs
description: "Human workflow for OBS on supported Windows to capture one permitted demo application's own audio while disabling broad desktop audio and checking the real recording."
---
# 在 Windows OBS 只抓获准演示应用的声音 / Capture Only Permitted Windows App Audio in OBS

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 受支持 Windows、会发声的自有演示应用和私有 OBS 场景 / Supported Windows, owned demo app with sound and private OBS scene |
| Side effects / 现实副作用 | 短测里有目标应用声、无无关系统声 / Test contains target app audio and excludes unrelated system sound |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在 Windows 上录自己应用的音效演示，OBS 默认 Desktop Audio 可能顺便抓到通知、音乐或其他应用。改用只针对这一个获准应用的音频路径，并做实际短测。成果是目标声可听、无关系统声不进入文件。若平台或应用不支持该路径，停在无应用声状态，不装第三方虚拟线缆兜底。

### 准备与输入

确认应用声音和内容获授权、不会含他人语音；准备一段可识别的无敏感测试声。检查当前 Window Capture 是否已有 Capture Audio，或是否另建 Application Audio Capture，不两者同时打开；把全局 Desktop Audio 的宽域抓取边界单独核清。

### 执行

1. 按安装版本可见入口选择窗口内 Capture Audio 或独立 Application Audio Capture，仅指向目标应用。
2. 关闭不需要的全局 Desktop Audio 路径，核音量表只有目标应用声对应条目响应。
3. 播放无敏感应用声并触发一个无关系统测试音，录短片重开听，确认后者没有进入文件。
4. 保存设置并在正式录制前重核当前应用窗口与音频来源没有改变。

### 完成、常见问题与恢复

短测文件有目标应用声而无其他桌面声音，音频入口只有一条计划路径。

- **没有应用声：** 核此应用是否支持和窗口选择，不装额外插件硬接。
- **通知也录进来：** 核 Desktop Audio 是否仍启用，停止后重测。
- **声源重复：** 只留窗口音频或独立应用音频之一。

### 假设与边界

限于受支持 Windows 的获准应用声音；其他平台、受保护媒体、系统声音全捕获和虚拟线缆均不在此篇。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/application-audio-capture-guide)（英文，官方手册）— Windows 可用 Application Audio Capture 或部分 Window Capture 的 Capture Audio 选项，需避免同时抓全桌面。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this on supported Windows when your own demo app has sound but global Desktop Audio could also capture notifications, music or unrelated apps. Choose one per-app audio path and prove with a real short test that only target sound enters the file. If the platform or app cannot support it, stop with no app audio rather than installing a virtual-cable workaround.

### Preparation and inputs

Confirm the app sound is yours and contains no other people's voices, then prepare a harmless recognizable tone. Inspect whether Window Capture already includes audio or a separate Application Audio Capture exists; avoid enabling both, and inspect global Desktop Audio separately.

### Execution

1. Choose either the installed Window Capture audio option or a separate Application Audio Capture, targeting only the demo app.
2. Disable unnecessary global Desktop Audio and inspect the meter responding only to target-app sound.
3. Play harmless app audio and an unrelated system test sound, then record and listen to ensure the latter is absent.
4. Keep settings and recheck the selected app window and audio source before actual recording.

### Success, common problems, and recovery

The short file contains target-app audio but no unrelated desktop sound, with one planned capture path.

- **No app sound:** Inspect support and selected window without installing plugins.
- **Notification recorded:** Check whether Desktop Audio remains active, then stop and retest.
- **Duplicate sound:** Keep either window audio or separate app audio, not both.

### Assumptions and limits

This is limited to supported Windows and permitted app sound. Other platforms, protected media, all-system audio and virtual cables are outside scope.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/application-audio-capture-guide) — Supported Windows can capture per-app audio or use Window Capture audio, while broad Desktop Audio should not duplicate it.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

