---
name: make-one-writer-section-landscape-and-return-portrait
description: "Human-readable two-boundary Writer page-style change for one wide section, verifying landscape content and portrait neighbours."
---
# 让 Writer 一节横向后再回到纵向 / Make One Writer Section Landscape and Return Portrait

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 15–30 分钟 / 15–30 minutes |
| Requirements / 必要物品 | 已有宽表或宽图的非敏感多页 ODT 副本、明确该节首尾 / Non-sensitive multipage ODT copy with wide section and known start/end |
| Side effects / 现实副作用 | 宽节横向而前后页面继续纵向 / Wide section landscape while neighbouring pages stay portrait |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你有一节宽表或宽图在纵向纸页上被截断，想只让**这一节**用横向页面时使用本篇。成果是该节完整横向、前后页面保持原来的纵向布局，页眉页脚或页码异常被检查。直接对当前页乱改默认页样式可能影响多页，所以先在副本上确定两个边界。

### 准备与输入

保存 ODT 副本，记下横向节首段和末段及相邻页面方向、边距和页码。查看 Writer 的 Landscape 与原纵向页样式是否可用；若文稿已有复杂镜像页或不同页眉，先记录它们，不能假设会自动转移。

### 执行

1. 在宽节开始处插入带页样式的手动分页，选择 Landscape，而非修改所有默认页。
2. 检查宽表或图在横向页完整显示，并核边距及页码是否仍合乎文稿要求。
3. 在宽节末尾插入第二个带页样式的手动分页，选回原纵向页样式。
4. 巡视进入前、横向内、返回后的三处页面；多页意外变向就撤销并重新核边界。

### 完成、常见问题与恢复

只有指定宽节横向，前后仍纵向，内容与页码未失；无法安全界定节尾时暂不改页面样式。

- **后面全横向：** 缺返回纵向的第二个边界。
- **宽内容仍截：** 核页面边距与对象尺寸，不拉伸文字。
- **页码重置：** 查分页对话框的页码选项。

### 假设与边界

只调整一节的页面方向；复杂页眉页脚、奇偶页、装订边距可能需额外核查。你负责实际打印需求，不把预览成功当纸本验收。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26205-FormattingPagesBasics.html)（英文，官方手册）— 横向页样式需要在进入与返回处各用手动分页切换。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one wide table or image clips on portrait pages and **only that section** should be landscape. Finish with the wide section readable in landscape, pages before and after still portrait, and headers/footers or page numbers checked. Changing the default page style directly may affect many pages, so mark both boundaries on a copy.

### Preparation and inputs

Save an ODT copy and note first/last paragraphs of the wide section plus neighbouring orientation, margins and page numbers. Locate Landscape and the original portrait page style. If the document uses mirrored pages or special headers, record them; they may need separate handling.

### Execution

1. At section start insert a manual page break with Landscape page style instead of changing every default page.
2. Check the wide content fits landscape and review margins and page numbering against document needs.
3. At the section end insert a second styled manual page break back to the original portrait style.
4. Inspect one page before, within and after. Undo unexpected orientation changes and recheck boundaries.

### Success, common problems, and recovery

Only the intended wide section is landscape, neighbours remain portrait and content/page numbers survive. If the end boundary cannot be identified, defer the style change.

- **All later pages landscape:** Add the second return-to-portrait boundary.
- **Wide content still clips:** Check margins and object size without distorting text.
- **Page numbers restart:** Check break dialog's page-number option.

### Assumptions and limits

This changes orientation for one section. Complex headers, odd/even styles and binding margins need extra checks. You decide print needs; preview is not paper acceptance.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26205-FormattingPagesBasics.html) — a landscape page style needs manual-break transitions into and out of the section.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.
