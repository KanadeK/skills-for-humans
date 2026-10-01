---
name: make-one-obs-profile-for-private-local-recording
description: "Human workflow to create an OBS Profile for local recording output and distinguish it from Scene Collections and any streaming settings."
---
# 给 OBS 私有本地录制建立独立配置档 / Make One OBS Profile for Private Local Recording

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | OBS Studio、明确本地录制用途和既有配置档 / OBS Studio, defined local recording use and existing profile |
| Side effects / 现实副作用 | 一份名称明确且可切回旧配置的录制 Profile / Named recording Profile with preserved previous settings |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你要做私有本地录像，却不想改坏旧直播配置的分辨率或输出路径时，先建立一份录制专用 Profile。结果是 Profile 名称能辨明用途，切回旧档后旧设置仍在；可视场景仍由 Scene Collection 管理。Profile 不是“不会直播”的安全开关，开始前仍要检查控制区和账号连接状态。

### 准备与输入

记录当前 Profile 名称与关键输出配置，确认没有进行中的录制或推流。给新档取清楚名字，避免“默认 2”之类难以辨认的标签；若旧档已有本次可复用设置，可复制而不是从零猜编码参数。

### 执行

1. 从 Profile 菜单新建或复制本次本地录制档，确认当前活动档切到了新名称。
2. 在该档中检查视频与 Output 页的录制相关项，不填写直播平台密钥或连接任何账户。
3. 切回旧 Profile 核原值，再回新 Profile 核本次设置独立保存。
4. 再看场景集合是否仍需单独切换，记录当前活动的 Profile 与集合配对。

### 完成、常见问题与恢复

专用 Profile 与旧档分别可选，录制设置不覆盖旧值，活动场景集合另有明确记录。

- **以为换档会清场景：** 去 Scene Collection 单独切换，不删旧源。
- **旧输出被改：** 回旧档核值，必要时从已知备份恢复。
- **直播仍可点：** 明确只使用 Start Recording 控件，不把档名当限制。

### 假设与边界

只建立本机录制配置边界，不操作直播帐号、上传或插件，也不保证设备自动选择正确。

### 来源

- [OBS Knowledge Base](https://obsproject.com/kb/profiles)（英文，官方手册）— Profile 保存视频和输出等设置，不保存场景来源。
- Original synthesis — 将一个私人本地录制结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a private local recording needs its own video and output settings without overwriting a prior streaming setup. Create a named Profile and confirm the old one remains available. Scene visuals belong to Scene Collections. A Profile name is not a technical lock against streaming, so inspect controls and account state before work.

### Preparation and inputs

Record current Profile name and key output settings, and confirm no active recording or stream. Choose an unambiguous name rather than 'Default 2.' If prior settings are useful, duplicate them instead of guessing every encoder parameter.

### Execution

1. Create or duplicate a local-recording Profile and verify it becomes the active named profile.
2. Inspect Video and Output recording settings without entering a stream key or connecting an account.
3. Switch to the old Profile to confirm original values, then back to the new one to verify separation.
4. Inspect the active Scene Collection separately and record the chosen profile-collection pairing.

### Success, common problems, and recovery

The dedicated Profile and old one are separately selectable, recording settings do not overwrite old values, and the active collection is known.

- **Scenes unchanged:** Switch Scene Collection separately without deleting old sources.
- **Old output changed:** Check old Profile values and restore from known backup if needed.
- **Stream still available:** Use only Start Recording and do not treat the profile name as a lock.

### Assumptions and limits

This creates a local output-settings boundary, without live accounts, upload or plugins, and does not guarantee device selection.

### Sources

- [OBS Knowledge Base](https://obsproject.com/kb/profiles) — Profiles store video and output settings but not scenes and sources.
- Original synthesis — one private local-recording outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain OBS controls. You choose the content, perform the steps and verify the result.

