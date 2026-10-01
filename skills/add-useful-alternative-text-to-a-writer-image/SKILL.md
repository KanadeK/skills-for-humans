---
name: add-useful-alternative-text-to-a-writer-image
description: "Human-readable accessibility description for one meaningful Writer image, checked against its actual purpose and saved object properties."
---
# 给 Writer 一张有意义图片写可用的替代文字 / Add Useful Alternative Text to a Writer Image

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 含一张有意义且获准图片的非敏感 ODT 副本、图片上下文 / Non-sensitive ODT copy with one meaningful permitted image and its context |
| Side effects / 现实副作用 | 非视觉读者能获得图片承担的关键信息 / A non-visual reader can receive the image's essential point |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你在 Writer 文稿中放了一张承载信息的图片，想让不看图的读者也得到它的关键意思时使用本篇。成果是图片对象中有简短、贴合上下文的 Text Alternative，复杂必要细节再放较长描述；不是把文件名或“图片一张”塞进去。可见图注另有用途，不能代替非视觉说明。

### 准备与输入

保存 ODT 副本，先用一句话说清图片为何在此：它是解释步骤、提供证据还是纯装饰。检查上下段已经说出的信息，避免在替代文字里机械重复全部段落。若图片纯装饰，考虑标记 Decorative 而非硬编内容；先确认实际图片和使用许可。

### 执行

1. 选中正确图片，打开其 Properties > Options 的可及性区域。
2. 在短 Text Alternative 中写图片对本段最重要的信息；确需更多细节时再用长描述。
3. 读一遍不看图的段落加替代文字，检是否足以理解且没有虚构图中未见的结论。
4. 保存重开，核文字仍属于此图对象；若图其实装饰，撤回冗余描述并正确标记。

### 完成、常见问题与恢复

有意义图片有对应关键信息的非视觉说明，语境正确，保存重开仍存在；装饰图片按装饰处理。

- **只写文件名：** 改成图片在此表达的事实或动作。
- **重复整段正文：** 删冗余，只补视觉独有信息。
- **写到错图：** 核对象位置和属性后改正。

### 假设与边界

你负责判断图片意义和文字准确性；此步本身不证明整份文件可及，也不保证任何 PDF 导出自动保留，导出设置需另核。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26211-ImagesAndGraphics.html)（英文，官方手册）— 图片 Options 中可填可及性替代文字，装饰图应区分处理。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when a Writer image conveys information and a reader who cannot see it needs its key point. Finish with concise context-aware Text Alternative in the image properties and a longer description only if essential detail needs it. A filename or 'an image' is not useful. A visible caption serves another purpose and cannot replace non-visual description.

### Preparation and inputs

Save an ODT copy. State why this image is here: step explanation, evidence or pure decoration. Read surrounding paragraphs to avoid mechanically repeating all prose. For a purely decorative image, consider the Decorative flag instead of invented content. Confirm the actual image and permission first.

### Execution

1. Select the correct image and open Properties > Options accessibility area.
2. Write the image's essential message in the short Text Alternative, using a longer description only for necessary detail.
3. Read paragraph plus text alternative without looking at image; check it conveys the point without invented conclusions.
4. Save and reopen, checking text remains on this image object. For a decorative image, remove redundant description and mark it correctly.

### Success, common problems, and recovery

A meaningful image has context-correct essential non-visual text that persists after reopen; decorative imagery is marked as decorative.

- **Only filename entered:** Describe the fact or action conveyed here.
- **Whole paragraph repeated:** Keep only visually unique information.
- **Attached to wrong image:** Check object location and correct.

### Assumptions and limits

You judge image meaning and accuracy. This step alone cannot certify whole-document accessibility or guarantee PDF export preserves it; export settings need separate checks.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26211-ImagesAndGraphics.html) — image Options can hold accessibility text and decorative graphics are handled separately.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.

