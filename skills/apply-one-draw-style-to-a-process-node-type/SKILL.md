---
name: apply-one-draw-style-to-a-process-node-type
description: "Human-readable application of one restrained custom Draw style to same-role nodes, keeping decision and action types visually distinct."
---
# 给 Draw 同类流程节点应用一致的自定样式 / Apply One Draw Style to a Process Node Type

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已有两三个同类节点的 ODG 副本、明确视觉含义 / ODG copy with several same-role nodes and clear visual meaning |
| Side effects / 现实副作用 | 同类节点共享清楚而克制的线/填色 / Same-role nodes share restrained line and fill |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一张 Draw 图里同为普通步骤的节点线粗、颜色混乱，读者可能误以为它们有不同含义时使用本篇。成果是同类节点应用一套自定且可读的样式，判断节点仍保持不同编码。这里建立视觉约定，不靠重色或阴影制造假重要性。

### 准备与输入

保存 ODG 副本，先按实际语义分清普通动作节点与判断节点，选一个低干扰线色/填色组合。不要修改全局内置样式以免波及其它对象，先创建或选本图自定样式。记下要应用的节点清单和一个不应改变的对照节点。

### 执行

1. 在 Styles 侧栏建立/选一套自定动作节点样式，核文字对比与边线可辨。
2. 逐个选同类节点应用该样式，不把判断菱形也套成相同含义。
3. 在普通尺寸检查颜色、线条与标签是否一致，图例若已有也要对应。
4. 保存重开，抽查两目标和一排除节点；若全部都变，撤回误改内置样式。

### 完成、常见问题与恢复

同类节点有一致样式，异类仍可区分，图例和文字可读。

- **所有形状都变：** 核是否误改内置样式。
- **字色看不清：** 换更高对比但不过分的组合。
- **图例不一致：** 让图例样本跟目标样式对应。

### 假设与边界

样式只表达图内约定，不证明流程优先级或风险等级。你决定视觉含义；正式行业符号标准另行核。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26204-ChangingObjectAttributes.html)（英文，官方手册）— Draw 自定 Drawing Style 可统一一组对象的填色与线条。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when action nodes in a Draw diagram have inconsistent line or fill and readers might infer different meanings. Finish with same-role nodes using one readable custom style while decision nodes retain a distinct code. This establishes visual consistency without heavy color or shadow falsely elevating importance.

### Preparation and inputs

Save ODG copy and classify action versus decision by actual meaning. Choose a restrained, legible line/fill pair. Avoid editing built-in styles that may affect other objects; create/select a custom style within drawing. List target nodes and one excluded control.

### Execution

1. Create or select a custom action-node style in Styles deck with readable text contrast and line.
2. Apply it to each same-role node, excluding decision diamond.
3. Check fill, line and labels at normal size, and update any legend sample if needed.
4. Save/reopen and inspect two targets plus one excluded node; restore for unintended built-in edit.

### Success, common problems, and recovery

Same-role nodes share style, different roles remain distinguishable and labels/legend read clearly.

- **All shapes changed:** Check accidental built-in style edit.
- **Text lacks contrast:** Use readable restrained contrast.
- **Legend differs:** Match legend sample.

### Assumptions and limits

Style encodes this diagram's convention, not actual priority or risk level. You decide meaning; formal industry notation needs separate review.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26204-ChangingObjectAttributes.html) — custom Draw Drawing Style can unify fill and line attributes across objects.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.
