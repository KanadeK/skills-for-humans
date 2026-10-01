---
name: save-a-separate-gimp-xcf-working-master
description: "Human-readable creation of a native XCF working master for an owned image without overwriting its original photo file."
---
# 给原图另存一份 GIMP XCF 工作主本 / Save a Separate GIMP XCF Working Master

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已打开自有普通图片、明确原文件路径和另存目录 / Open owned ordinary image, known source path and separate save location |
| Side effects / 现实副作用 | 原图保留，XCF 项目可继续分层编辑 / Original stays while XCF remains editable |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已打开一张自有图片，准备做可能需要回退的调整时使用本篇。成果是独立命名的 `.xcf` 工作主本，原 JPEG/PNG 等文件仍在原处且未被覆盖。XCF 保留 GIMP 的图层与后续编辑状态，不是给所有人直接浏览的交付格式。

### 准备与输入

先核原文件名与目录，挑一个不会与原图同名覆盖的工作文件夹。若已有旧 XCF，区分是续改旧项目还是新建副本；不要用同名 Save 覆盖旧版本。记录本次项目名和来源名的对应关系。

### 执行

1. 使用 File > Save As 或首次 Save，选择新路径与清楚的 `.xcf` 文件名。
2. 在保存对话框核扩展名、目录和不会覆盖原 JPEG/PNG 后确认。
3. 关闭或另开 XCF，检查能打开并看到预期图层/画面；仍未改动的原文件也能单独打开。
4. 把原文件与 XCF 位置记下；以后对外文件另用 Export，不在此处改成 JPEG 保存。

### 完成、常见问题与恢复

原图与 XCF 是两个可分别打开的文件，XCF 可继续编辑，原图未覆盖。

- **误存到原目录同名：** 停下核覆盖提示，恢复备份再另存。
- **找不到 XCF：** 核保存目录与文件扩展名。
- **只导出了 JPEG：** 回 GIMP 用 Save 建 XCF 主本。

### 假设与边界

XCF 是工作文件，不代替独立备份；你决定保存位置与版本。此篇不上传或共享任何图像。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-save-dialog.html)（英文，官方手册）— GIMP Save 使用原生 XCF，其他图片格式须另用 Export。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill after opening an owned image before edits that may need revision. Finish with a separately named `.xcf` working master while the original JPEG/PNG remains at its original path untouched. XCF keeps GIMP layers and editing state; it is not the universal viewer-delivery format.

### Preparation and inputs

Check original name and folder and choose a distinct working location. If an older XCF exists, decide whether continuing or creating a new copy; avoid overwriting by identical name. Note the mapping from source to project name.

### Execution

1. Use File > Save As or first Save, choosing a new location and clear `.xcf` name.
2. Confirm extension, folder and no overwrite of original JPEG/PNG before accepting.
3. Reopen XCF and check image/layers, then confirm source file opens separately and remains unchanged.
4. Record both locations. Use Export separately for viewer copies, rather than changing this master to JPEG.

### Success, common problems, and recovery

Original and XCF are separately openable, XCF remains editable, and source was not overwritten.

- **Same name/path:** Stop at overwrite prompt and recover source before new save.
- **XCF missing:** Check destination and extension.
- **Only JPEG exported:** Use Save to create XCF master.

### Assumptions and limits

XCF is a working file, not a separate backup system. You choose location/version. This Skill uploads or shares nothing.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-save-dialog.html) — GIMP Save uses native XCF while other formats require Export.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.

