---
name: export-and-check-an-impress-slide-only-pdf
description: "Human-readable export of an Impress ODP to a separate slide-only PDF with order, hidden-slide and notes-disclosure checks."
---
# 从 Impress 导出只含幻灯片的 PDF 并核页 / Export and Check an Impress Slide-Only PDF

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存非敏感 ODP 主本、另存 PDF 路径、预期放映页清单 / Saved non-sensitive ODP master, separate PDF destination and intended slide list |
| Side effects / 现实副作用 | PDF 页序经核且备注未误入 / PDF page order checked without accidental notes |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有 ODP 主本，要给只需阅读幻灯片的人一份 PDF 副本时使用本篇。成果是实际 PDF 的页数、页序、首页末页和图片文字与预期一致，讲者备注没有混进对外页面；原 ODP 仍可编辑。它是交付前文件核查，不等于文件已发送或公开发布。

### 准备与输入

先保存 ODP，列出预期输出的可见页与隐藏页，核备注中没有不应出现在导出物的信息。记下首末页标题和总张数。选择独立 PDF 文件名与路径，不能用 PDF 覆盖 ODP 主本。

### 执行

1. 使用 File > Export As > Export as PDF，明确页范围与相关选项，保存独立副本。
2. 打开实际 PDF，逐页核顺序、首末页、关键图片与最长一段文字无截断。
3. 特别检查隐藏页与讲者备注是否按计划不在 PDF，中间至少抽一页。
4. 若发现多页或漏页，回 ODP 修可见状态/导出设置后重导，核主本仍可打开。

### 完成、常见问题与恢复

PDF 只含预期页面、次序可读、备注不泄露，ODP 主本保留；未核设备效果单独注明。

- **隐藏页也出现：** 核 PDF 范围与隐藏页导出设置。
- **备注页混入：** 核导出类型，重新选幻灯片。
- **文字截断：** 回 ODP 改布局再导。

### 假设与边界

不保证任何接收端阅读器或辅助技术体验，也不执行发送或公开发布。你决定披露范围；PDF 不是可编辑 ODP 的替代主本。

### 来源

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26210-SlideShowsPrintEmailExport.html)（英文，官方手册）— Export as PDF 可设置输出范围，实际 PDF 需重开核查。
- Original synthesis — 将一个演示文稿结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when an ODP master needs a PDF copy for someone who only reads slides. Finish with the actual PDF's count, order, first/last page, images and text matching the intended list, no speaker notes accidentally included, and ODP still editable. This is pre-delivery file checking, not sending or publishing.

### Preparation and inputs

Save ODP, list visible and hidden slides expected in output, and inspect Notes for material that must not appear. Note first/last titles and expected count. Choose a separate PDF name and location rather than overwriting the ODP master.

### Execution

1. Use File > Export As > Export as PDF with explicit page range/options and a separate filename.
2. Open actual PDF and check order, first/last slides, key image and longest text for clipping.
3. Check hidden slides and speaker notes against plan, sampling at least one middle page.
4. For extra/missing pages, adjust ODP visibility or export settings and re-export; confirm ODP still opens.

### Success, common problems, and recovery

PDF contains only intended pages in readable order without leaking Notes, while ODP master remains; untested devices are named separately.

- **Hidden slide appears:** Inspect export range and hidden-slide option.
- **Notes included:** Check export type and choose slides only.
- **Text clipped:** Fix ODP layout and export again.

### Assumptions and limits

This cannot guarantee every recipient viewer or assistive-technology experience and does not send or publish. You choose disclosure; PDF is no editable ODP master.

### Sources

- [LibreOffice Impress Guide 26.2](https://books.libreoffice.org/en/IG262/IG26210-SlideShowsPrintEmailExport.html) — Export as PDF offers output choices and the actual PDF needs reopening.
- Original synthesis — one presentation outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Impress controls. You choose the content, perform the steps and verify the result.
