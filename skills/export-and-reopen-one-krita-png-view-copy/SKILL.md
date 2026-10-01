---
name: export-and-reopen-one-krita-png-view-copy
description: "Human workflow to export one original layered Krita painting as a separate PNG, check intended background or transparency and reopen it without replacing the KRA master."
---
# 从 Krita 原稿导出并重开一张 PNG 预览图 / Export and Reopen One Krita PNG View Copy

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存的原创 .kra、明确透明或实色背景要求、本地预览目录 / Saved original .kra, background or transparency requirement and local review folder |
| Side effects / 现实副作用 | 一张能独立打开且背景正确的 PNG 预览副本 / One independently viewable PNG copy with intended background |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已在 Krita 完成一张原创分层稿，需要发给自己或同事看画面，却仍要保留可编辑原稿时，导出一张独立 PNG。完成标准是从磁盘重新打开实际文件，核画面边缘、色彩大致表现和透明或实色背景符合用途。导出成功提示不等于预览真的可读，PNG 也不保留你在 .kra 里安排的可编辑图层。

### 准备与输入

先保存 .kra，记下原稿路径和目标预览文件名。检查背景层当前显示状态及用途是否要求透明；若目标是有文字的屏幕图，缩小看文字和轮廓是否仍能辨认。选择本地私有目录，不把导出和发布混为一谈。

### 执行

1. 从原稿使用 Export 输出为 PNG，核路径、文件名和透明/背景选项，避免用 Save As 把当前工作文件切换成展平格式。
2. 在文件管理器确认 PNG 实际生成，再用独立查看器打开；放大看边缘，缩小看整体。
3. 对照 .kra 核背景、透明区和裁切边界。若不对，回原稿改背景显示或导出选项，再生成新副本。
4. 最后确认 Krita 当前可编辑文档仍是 .kra，图层还在，记录这份 PNG 对应的原稿版本。

### 完成、常见问题与恢复

PNG 从磁盘可独立观看，背景与边缘符合本次审阅用途，.kra 原稿保持可编辑。

- **透明变白：** 核背景层可见性和 PNG 导出透明选项后重导。
- **边缘被裁：** 回工程核画布边界与对象位置，别只改查看器缩放。
- **原稿变 PNG：** 重新打开已保存 .kra，确认图层并继续从它编辑。

### 假设与边界

只交一张本地预览图，不宣称社交平台显示、印刷、版权或读者体验验收。透明显示还受查看器棋盘格/背景影响，需查看实际像素。

### 来源

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/working_with_images.html)（英文，官方手册）— Export 可另存兼容格式而不切换当前原稿；PNG 的透明处理需按背景设置核对。
- Original synthesis — 将一个数字绘画结果、原稿对照和失败停点组合为可核流程。

## English

Use this when an original layered painting needs a separate view copy while its editable .kra remains the master. Produce a PNG and reopen the actual disk file to check edges, approximate appearance and the intended transparent or solid background. An export success message is not a visual check, and the PNG does not preserve the editable Krita layer stack.

### Preparation and inputs

Save the .kra and note its path alongside a distinct preview file name. Inspect background-layer visibility and whether the recipient needs transparency. For text-bearing screen art, check readability at a small display size. Choose a private local folder; export is not publication.

### Execution

1. Use Export from the master to write a PNG, checking destination, name and transparency/background choices rather than switching the working document to a flattened Save As file.
2. Confirm the PNG exists in the file manager and open it in a separate viewer, inspecting edges up close and composition at normal size.
3. Compare with the .kra for background, transparent areas and cropped edges. If wrong, adjust the master view or export choice and generate a fresh copy.
4. Confirm the active editable document is still the .kra with layers intact and record which master version the PNG represents.

### Success, common problems, and recovery

The PNG opens independently with intended background and edges, and the .kra master remains layered and editable.

- **Transparency lost:** Inspect background visibility and PNG transparency choice, then re-export.
- **Edge cropped:** Inspect canvas bounds and object placement in the master.
- **Master switched:** Reopen the saved .kra and continue editing from that layered file.

### Assumptions and limits

This delivers one local preview, not platform appearance, print compliance, rights clearance or viewer acceptance. Transparency display depends on the viewer background, so inspect the actual file.

### Sources

- [Krita 5.3 Manual](https://docs.krita.org/en/user_manual/working_with_images.html) — Export writes a compatible copy without changing the active master; PNG background and transparency need checking.
- Original synthesis — one digital-painting outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Krita controls. You choose the content, perform the steps and verify the result.

