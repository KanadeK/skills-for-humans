---
name: place-one-owned-static-image-in-an-obs-demo-scene
description: "Human workflow to add one owned local image as a static OBS source and verify its size, alpha and appearance without importing remote material."
---
# 在 OBS 私有演示里放一张自有静态图 / Place One Owned Static Image in an OBS Demo Scene

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 本人拥有的本地 PNG/图片、私有场景和明确用途 / Owned local PNG/image, private scene and clear purpose |
| Side effects / 现实副作用 | 一张静态参考图按计划显示且不挡演示主体 / One static reference image displays as planned without hiding the demo |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你想在自己的应用演示角落放一张本人画的简图，提醒观看者操作目标时，可添加一张本地图像源。成果是图在录制文件中清楚且不挡真正操作，素材路径明确、重开 OBS 仍能加载。不要直接用网上抓来的图或他人商标充数；图像源也可能因文件搬走变成空白。

### 准备与输入

确认图片是自有或获准、无个人敏感信息，保存在稳定本地目录。查看是否有透明背景以及原像素尺寸；如果源图太小，不通过无限放大来假装高质量。检查本次场景只需要这一张，不添加轮播。

### 执行

1. 添加 Image Source 并选本地目标文件，给源起可辨名称。
2. 在预览里按比例摆到辅助位置，核透明边缘或实色背景不会遮住应用操作。
3. 切换源可见性确认确是这张图片，并保存场景后重开看路径仍有效。
4. 录短测重开文件，核实际输出里图片与主窗口同时可读。

### 完成、常见问题与恢复

一张自有本地图在实际录像中处于辅助位置，来源和路径可追溯。

- **图不见：** 检查文件路径、源可见性与堆叠位置。
- **图挡界面：** 缩小或移位，不裁掉主操作。
- **边缘有色块：** 核源图片 Alpha 或背景，并换底色测试。

### 假设与边界

只加入一张普通自有静图，不授权第三方素材、远程浏览器源或动态广告。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/image-sources)（英文，官方手册）— Image Source 从本地图片路径加载素材，可含 Alpha 透明度。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a small diagram you made should sit beside your app demonstration as a static reference. Add it as a local Image Source, verify it appears in the recorded file without covering the action and survives reopening OBS. Do not use a grabbed web image or someone else's logo. Moving the source file later can break the scene.

### Preparation and inputs

Confirm the image is owned or permitted and contains no private data, then place it in a stable local folder. Inspect alpha and native pixel dimensions. Avoid extreme enlargement of a tiny source. This task uses one still, not a slideshow.

### Execution

1. Add an Image Source for the local file and name it clearly.
2. Scale proportionally into a supporting position, checking transparent or opaque edges do not cover the app.
3. Toggle the source to prove identity, preserve the scene and reopen to confirm its path remains valid.
4. Record and reopen a short test to check both image and main window remain readable.

### Success, common problems, and recovery

One owned local image appears in the actual recording in a supporting place with traceable source and path.

- **Image missing:** Check file path, source visibility and stack order.
- **Covers app:** Resize or move it without cropping the main action.
- **Colored box:** Inspect source alpha or background against another backdrop.

### Assumptions and limits

This adds one ordinary owned still, not third-party media rights, remote browser sources or dynamic advertising.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/image-sources) — Image Source loads a local file path and may support alpha transparency.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

