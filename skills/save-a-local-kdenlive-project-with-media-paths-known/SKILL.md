---
name: save-a-local-kdenlive-project-with-media-paths-known
description: "Human-readable save of a separate local Kdenlive project with source-folder mapping and reopen test, without moving originals."
---
# 保存 Kdenlive 本机工程并记住素材位置 / Save a Local Kdenlive Project with Media Paths Known

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已有导入自有素材的 Kdenlive 项目、独立保存目录 / Kdenlive project with owned imported media and separate save folder |
| Side effects / 现实副作用 | 工程可重开且原素材路径可找到 / Project reopens with original media locatable |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已导入自有素材，准备在 Kdenlive 剪辑前想留下可继续编辑的本机工程时使用本篇。成果是独立 `.kdenlive` 文件可重开，素材预览和路径有效，原视频/音频没有被工程文件替代。项目只是引用与剪辑状态，不等于已输出可播放成片。

### 准备与输入

给工程选明确目录与名称，记下所有原素材所在文件夹，不移动或删除它们。若媒体在外接盘，确认下次仍能接入；否则先复制到稳定工作位置并保留原件。不同工程版本不要同名覆盖。

### 执行

1. 使用 File > Save Project/Save As，把工程保存为独立 `.kdenlive` 文件。
2. 核文件位置、媒体引用与原文件仍在，避免把工程错放进临时下载目录。
3. 关闭并从该路径重开工程，检查 Project Bin、时间线与至少一段预览可用。
4. 若提示媒体离线，先按原路径核文件位置，不能只凭工程存在声称可继续剪。

### 完成、常见问题与恢复

工程可重开、素材可读、原件独立保留，尚未误称成片。

- **工程开了素材不见：** 查移动的路径并重连。
- **只有视频没有工程：** 回 Kdenlive 保存项目。
- **旧项目被盖：** 从备份恢复并重命名。

### 假设与边界

本机工程不等于独立备份；你负责素材存放和版本。此篇不上传云端或发布。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/project_and_asset_management.html)（英文，官方手册）— Kdenlive 项目保存剪辑和素材引用，源文件需保持可访问。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill after importing owned assets and before substantial Kdenlive edits when you need a reopenable local project. Finish with separate `.kdenlive` file whose media previews and paths work, while original video/audio remain. A project stores references/edit state, not a playable final render.

### Preparation and inputs

Choose clear project location/name and note each source folder without moving/deleting originals. If media is on removable drive, ensure it remains accessible next time; otherwise make a stable working copy while preserving source. Avoid overwriting older project versions.

### Execution

1. Use File > Save Project/Save As for a separate `.kdenlive` file.
2. Check project path, media links and source files, avoiding temporary download folders.
3. Close/reopen from path and check Project Bin, timeline and at least one preview.
4. For offline warning inspect source location before claiming project is usable.

### Success, common problems, and recovery

Project reopens with readable media and separate originals, without claiming a rendered video.

- **Media missing:** Check moved path and relink.
- **Only video render:** Save project separately.
- **Old project overwritten:** Restore backup and version name.

### Assumptions and limits

A local project is not an independent backup. You manage media locations and versions. No cloud upload or publishing.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/project_and_asset_management.html) — Kdenlive project stores timeline and asset references; source files must stay accessible.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

