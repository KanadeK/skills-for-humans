---
name: import-permitted-video-assets-into-a-kdenlive-bin
description: "Human-readable import of selected permitted media into Kdenlive Project Bin with clip identity, preview and source-file preservation checks."
---
# 把获准视频素材导入 Kdenlive 项目箱并核预览 / Import Permitted Video Assets into a Kdenlive Bin

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存 Kdenlive 工程、几段来源明确的自有视频/音频 / Saved Kdenlive project and a few source-known owned video/audio files |
| Side effects / 现实副作用 | 项目箱显示正确素材而原文件未改 / Bin shows intended assets while source files remain |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有几段来源明确的自有/获准素材，想让它们进入 Kdenlive 工程而不立刻排上时间线时使用本篇。成果是 Project Bin 列出预期文件，缩略图、时长或声音可对上原件，误导入的同名版本被发现。导入不改变原文件，也不说明它已有发布许可。

### 准备与输入

保存工程，先列素材文件名、文件夹、预期内容与使用许可。区分相机原件、代理文件和编辑过的副本，避免同名误用。一次只导入本次需要的几段，不把整个设备下载目录无差别拖进来。

### 执行

1. 在 Project Bin 用 Add Clip or Folder 选明确文件，核导入数量与清单。
2. 逐项查看缩略图/Clip Monitor 头中尾或听代表段，核内容和时长。
3. 对错源、重复或离线项先标记并修正，别把错误素材排入时间线。
4. 保存重开工程，再核至少两项素材可预览且原文件在原位置。

### 完成、常见问题与恢复

需要的素材在项目箱可辨、可预览，误导入已排除，原文件未改。

- **导入代理当原件：** 核路径与 Clip Properties。
- **有同名错片：** 逐个预览确认内容。
- **项目重开离线：** 核稳定素材路径后重连。

### 假设与边界

只导入和核素材，不排列剪辑或声称版权已清。你负责来源与许可。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/project_and_asset_management/project_bin/clips.html)（英文，官方手册）— Add Clip or Folder 把外部资产加入 Project Bin 供预览和编辑。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a few owned or permitted source files should enter a Kdenlive project before being arranged on timeline. Finish with Project Bin listing intended assets, thumbnails/durations/sounds matching sources and same-name wrong versions caught. Import does not alter originals or grant publication rights.

### Preparation and inputs

Save project and list filenames, folders, expected content and rights. Distinguish camera originals, proxies and edited copies to avoid same-name error. Import only the few needed assets, not an entire downloads folder.

### Execution

1. In Project Bin use Add Clip or Folder for selected files and compare count with list.
2. Inspect thumbnail/Clip Monitor at start/middle/end or listen to representative audio for identity/duration.
3. Mark and correct wrong-source, duplicate or offline items before timeline use.
4. Save/reopen project and check at least two assets preview with source files still present.

### Success, common problems, and recovery

Needed assets are identifiable and previewable in bin, wrong imports excluded, and originals untouched.

- **Proxy mistaken as source:** Check path and properties.
- **Same-name wrong clip:** Preview each.
- **Offline on reopen:** Check stable paths and relink.

### Assumptions and limits

This imports/checks media, not timeline editing or copyright clearance. You own sources and rights.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/project_and_asset_management/project_bin/clips.html) — Add Clip or Folder imports external assets into Project Bin for preview/editing.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

