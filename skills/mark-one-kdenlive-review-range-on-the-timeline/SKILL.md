---
name: mark-one-kdenlive-review-range-on-the-timeline
description: "Human workflow to place and name one Kdenlive timeline range marker for a specific review passage, keeping it distinct from clip markers and render zones."
---
# 在 Kdenlive 时间线上标出一段待复核区间 / Mark One Kdenlive Review Range on the Timeline

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存获准的 Kdenlive 工程、需要复核的具体镜头和起止时点 / Saved permitted project, concrete passage to review and intended start/end times |
| Side effects / 现实副作用 | 一个可导航、范围准确且有明确备注的时间线区间标记 / One navigable timeline range marker with accurate span and clear note |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你发现一段节奏、字幕或转场需要稍后复核，却还不准备改素材或渲染片段时，用一枚时间线区间标记把问题留在工程里。成果是能在时间线上跳到的明确范围，备注写清要核什么和判断标准。它不是 clip marker，也不等于已经设好的导出 Selected Zone。

### 准备与输入

保存工程，先播放问题片段并记起止帧；写一句具体备注，例如“核第二句字幕是否遮住手势”，而不是只写“看看”。确定标记该固定在时间位置还是需要随素材移动，后续插入镜头时要复核这一选择。

### 执行

1. 把播放头移到目标起点，在时间线尺或标记菜单创建 Timeline Marker，先核它出现在时间线而非源片段上。
2. 打开标记编辑窗口，启用 Range Marker，填写覆盖目标片段的持续时间和清楚的备注；需要时选合适类别。
3. 沿时间线从标记起点播放到终点，核范围没有跨过无关镜头；在 Markers 视图点击该项测试能跳到正确位置。
4. 保存重开工程，确认标记和备注仍存在；若随后挪动剪辑，按标记锁定设置重新核对它对应的实际内容。

### 完成、常见问题与恢复

工程中有一枚可见、可跳转的时间线区间标记，起止覆盖待复核内容，备注说明具体检查动作。

- **标在源片段上：** 删除误建的 clip marker，改在时间线尺/Timeline Marker 入口添加。
- **区间过宽：** 回编辑窗口缩短持续时间并重新播放边界。
- **剪辑后标记错位：** 检查标记锁定状态及素材移动方式，按新内容重设范围。

### 假设与边界

本篇只留一条工程内复核区间，不执行修片、导出标记或渲染。标记随剪辑移动的行为依锁定设置而变，最终仍需人眼核范围。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/guides.html)（英文，官方手册）— 时间线标记可以用于区间，在编辑窗口设置 Range Marker 与持续时间，并与片段标记区分。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this when a passage's pacing, caption or transition needs another review but you are not ready to edit or render it. Leave one precise range marker on the timeline with a note stating what to inspect and the decision to make. A timeline range marker is distinct from a marker attached to source footage and from a selected render zone.

### Preparation and inputs

Save the project and play the questionable passage to note its first and last frames. Draft a concrete note such as 'check whether line two hides the hand gesture' rather than 'look at this.' Decide whether the marker should stay on timeline time or move with edits, and review this choice after insertions.

### Execution

1. Move the playhead to the target start and create a Timeline Marker from the ruler or Markers menu. Confirm it appears on the timeline rather than attached to a source clip.
2. Open Edit Marker, enable Range Marker, set duration to cover the passage and enter a specific review note, with an appropriate category if useful.
3. Play from marked start to end and check the span excludes unrelated shots. Select it in the Markers view to confirm navigation reaches the intended position.
4. Save and reopen the project to confirm marker and note persist. After moving clips, recheck the content at the mark according to its lock behavior.

### Success, common problems, and recovery

The project contains one visible, navigable timeline range marker covering the intended passage with a note that names a concrete review action.

- **Attached to clip:** Remove the mistaken clip marker and add a Timeline Marker via the ruler or marker action.
- **Range too wide:** Shorten duration in Edit Marker and replay both boundaries.
- **Moved off target:** Inspect marker lock behavior and clip movement, then reset span against actual content.

### Assumptions and limits

This leaves one review range inside the project; it does not perform the edit, export markers or render footage. Marker movement depends on lock settings, so inspect the actual span after later timeline changes.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/cutting_and_assembling/guides.html) — Timeline markers can represent ranges with a duration in Edit Marker and differ from clip markers.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

