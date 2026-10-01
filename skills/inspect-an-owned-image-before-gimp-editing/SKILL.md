---
name: inspect-an-owned-image-before-gimp-editing
description: "Human-readable read-only intake of an owned image in GIMP, recording pixel dimensions, mode, file identity and a bounded editing purpose."
---
# 在 GIMP 编辑前核原图尺寸与颜色模式 / Inspect an Owned Image Before GIMP Editing

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–10 分钟 / 5–10 minutes |
| Requirements / 必要物品 | 自有或获准普通图片、现有 GIMP 3.2、原文件位置 / Owned or permitted ordinary image, GIMP 3.2 and original location |
| Side effects / 现实副作用 | 编辑依据有原始尺寸模式与文件身份 / Editing begins with known dimensions, mode and source identity |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你准备用 GIMP 处理一张自有普通照片，却还不知道它的像素大小、色彩模式或是否打开了正确版本时使用本篇。成果是一张简短输入卡：原文件名、像素尺寸、模式/色彩空间和本次只想改的一件事；图像内容未被改动。这里是只读入口，不把低像素照片承诺成可大幅打印的成品。

### 准备与输入

先确认你有使用和修改这张图的权利，不是证据、医疗或他人肖像资料。记录原文件所在位置及是否已有复制件，打开图像但暂不保存覆盖。界面缩放比例与实际像素数不同，不把屏幕上看着大当作高分辨率。

### 执行

1. 在 GIMP 查看当前图像标题和文件路径，确认不是同名的另一张。
2. 打开 Image > Image Properties，记录宽高像素、色彩模式/空间、分辨率和文件类型。
3. 写下一项本次目标，例如让水平线更正或导出较小屏幕版，并指出不碰的内容。
4. 关闭属性窗口再核画面与原图相同；若尺寸不符或来源不清，停在选择源文件。

### 完成、常见问题与恢复

输入卡与实际 Image Properties 对应，图像未改，后续操作有清楚目标和原文件可回退。

- **屏幕放大误当像素增加：** 读 Properties 的像素宽高。
- **开错同名文件：** 核路径并重开正确原图。
- **来源权限不明：** 停止修改，先确认许可。

### 假设与边界

只读图像属性不能证明色彩准确、印刷适用或内容真实。你负责来源与用途；分辨率数值也不能凭空增加细节。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-image-properties.html)（英文，官方手册）— Image Properties 显示像素尺寸、分辨率、颜色空间和文件类型。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill before editing an owned ordinary photo in GIMP when you do not yet know its pixel size, color mode or whether the correct source is open. Finish with a short intake note: source file, pixel dimensions, mode/color space and one intended change, while pixels remain untouched. This is read-only intake, not a promise that a small image can support large printing.

### Preparation and inputs

Confirm rights to use and modify this image; avoid evidence, medical or another person's portrait data. Note original location and any existing copy, open it without overwriting. Canvas zoom on screen differs from actual pixel dimensions.

### Execution

1. Check GIMP image title and source path to avoid a same-name different file.
2. Open Image > Image Properties and record pixel width/height, mode/color space, resolution and file type.
3. Write one bounded goal, such as straightening a horizon or smaller screen export, plus content not to change.
4. Close properties and confirm visible image remains unchanged. Stop if source or dimensions are uncertain.

### Success, common problems, and recovery

The intake note matches Image Properties, pixels are unedited, and a clear goal plus recoverable source exists.

- **Zoom mistaken for pixels:** Use pixel width/height in Properties.
- **Wrong same-name file:** Check path and reopen correct source.
- **Permission unclear:** Stop editing until permitted.

### Assumptions and limits

Properties alone cannot certify color accuracy, print suitability or image truth. You own source and purpose; a resolution number cannot invent detail.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-image-properties.html) — Image Properties shows pixel dimensions, resolution, color space and file type.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.

