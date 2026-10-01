---
name: isolate-one-obs-local-demo-scene-collection
description: "Human workflow to create a dedicated OBS scene collection for a private permitted window demonstration, separating its sources from old streaming scenes."
---
# 在 OBS 为私有演示建独立场景集合 / Isolate One OBS Local Demo Scene Collection

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | OBS Studio 32.2、本地演示主题和空白或既有场景 / OBS Studio 32.2, local demo purpose and blank or existing scenes |
| Side effects / 现实副作用 | 一套只含本次可控演示源的场景集合 / Scene collection containing only this controlled demonstration's sources |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你要用 OBS 录一段自己应用的私有演示，原界面却还留有旧直播摄像头、聊天或其他项目源时，先建专用场景集合。成果是切换到本次集合后只看到本次准备的场景和来源，不会把旧项目元素误录进去。集合还可能包含全局音频设置，建好后仍要核音频。

### 准备与输入

先列出本次真正需要的自有窗口、可选本人话音和本地标题。确认当前不在录制或直播中；如旧集合有价值，先保留原名称，不通过删除旧场景来腾地方。记录本次集合名，避免误以为新 Profile 就会清掉源。

### 执行

1. 从 Scene Collection 菜单新建本次专用集合，使用能区分“私有本地演示”的名字。
2. 核场景列表里没有旧直播、浏览器源或未经许可画面；若从副本建成，逐项移除本次不需要的源。
3. 切回旧集合再切回新集合，确认两套源没有混淆，且旧集合仍可找回。
4. 检查新集合里的全局音频条目和状态，记录需另行配置的设备后再开始录制。

### 完成、常见问题与恢复

本次集合和旧集合可分别切换，新集合只含有意的演示场景和可检查音频来源。

- **旧源仍在：** 确认不是在旧集合上改名，检查是否复制了旧集合。
- **旧设置不见：** 切回原集合核名称，不随意重建或删除。
- **音频还在动：** 核全局音频设备，不因画面空白就认为没有声音。

### 假设与边界

本篇只隔离场景和来源，不设置编码、文件路径，也不授权捕获他人画面或上线直播。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/scene-collections)（英文，官方手册）— Scene Collection 保存场景及源，与保存输出设置的 Profile 分开。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this before a private OBS demonstration when old stream cameras, chat or unrelated project sources remain in the current setup. Create a dedicated Scene Collection whose scenes and sources belong to this demo only. Global audio settings may also travel with a collection, so inspect audio after switching rather than assuming it is silent.

### Preparation and inputs

List the owned window, optional self narration and local title needed for this demo. Confirm no recording or streaming is active. Keep the old collection intact rather than deleting its scenes for space. Name this collection clearly; a new Profile alone will not remove visual sources.

### Execution

1. Create a new collection through Scene Collection with a name identifying this private local demo.
2. Inspect scenes for old stream, browser or unpermitted visual sources; if duplicated, remove only sources not needed for this demo.
3. Switch to the old and back to the new collection to verify separation and old setup preservation.
4. Inspect global audio entries in the new collection and note devices requiring separate setup before recording.

### Success, common problems, and recovery

Old and new collections switch independently, with only intended demo scenes and inspectable audio sources in the new one.

- **Old sources remain:** Check whether you renamed or duplicated the old collection and remove unintended sources.
- **Old setup missing:** Return to the original named collection without deleting anything.
- **Audio still active:** Inspect global audio devices; a blank scene can still record sound.

### Assumptions and limits

This isolates scenes and sources, not encoding or file paths, and does not authorize capturing other people or starting a stream.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/scene-collections) — Scene Collections save scenes and sources, separate from output Profiles.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

