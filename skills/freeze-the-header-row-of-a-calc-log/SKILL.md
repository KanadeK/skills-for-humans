---
name: freeze-the-header-row-of-a-calc-log
description: "Human-readable view operation that keeps exactly the first header row visible while scrolling a longer Calc log, with an unfreeze recovery."
---
# 滚动 Calc 日志时固定标题行 / Freeze the Header Row of a Calc Log

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 3–8 分钟 / 3–8 minutes |
| Requirements / 必要物品 | 带首行标题且可滚动的现有 Calc 日志 / Existing Calc log with header in first row and enough rows to scroll |
| Side effects / 现实副作用 | 向下滚动仍能看到字段名 / Column labels remain visible while scrolling |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你看一张较长的 Calc 日志，往下滚动就忘记各列含义时使用本篇。成果是第一行标题留在顶部、数据行继续滚动，并能清楚解除冻结。这里改变视图，不改变记录值、排序或打印范围。若标题并不在第一行，先重新确认要固定的实际行数。

### 准备与输入

确认第一行确实是唯一标题行，第二行开始为活动记录；若上方还有封面或说明，不能套用“只冻一行”。先保存副本并记下当前滚动位置。查本机菜单中 View/Freeze Rows and Columns 对应项，别把“拆分窗口”误认成冻结。

### 执行

1. 选择第二行中的一个普通单元格，确认该单元格上方恰好只有标题行。
2. 执行冻结行列命令，检查标题与数据之间出现固定界线。
3. 向下滚动数屏，观察第一行仍可见、第二行以后的记录实际换页。
4. 试着解除再恢复一次，并保存；若把多行都冻住，先解除后重选第二行。

### 完成、常见问题与恢复

滚动时只有预定标题行保持可见，解除冻结后普通滚动恢复，数据内容与行数没变。

- **多冻了几行：** 解除后改选标题下一行。
- **看起来只是分割：** 用冻结命令并滚动核实。
- **标题行不在首行：** 先确认实际标题范围再决定边界。

### 假设与边界

冻结是视图便利功能，不保证别人打开文件时看到同一缩放或窗位。你需按自己的 Calc 版本核菜单；本篇不改变表内数据。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26201-Introduction.html)（英文，官方手册）— 冻结行列使选定标题在滚动时持续可见。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when a longer Calc log loses its column meanings as you scroll down. Finish with the first header row visible while data rows continue scrolling, and know how to undo the freeze. This changes the view, not values, order or print range. If headers are elsewhere, first identify their actual row span.

### Preparation and inputs

Confirm row one really contains the only headers and data starts in row two. A cover or instructions above it changes the target span. Save a copy and note current scroll position. Locate View/Freeze Rows and Columns in your version; do not confuse window splitting with freezing.

### Execution

1. Select an ordinary cell in row two and confirm exactly the header row lies above it.
2. Use Freeze Rows and Columns and look for the fixed boundary below the header.
3. Scroll down several screens; row one should stay while later data rows change.
4. Unfreeze and restore once, then save. If too many rows stay fixed, unfreeze and select row two again.

### Success, common problems, and recovery

Only the intended header stays visible when scrolling; normal scrolling returns after unfreeze, with data content and row count unchanged.

- **Too many rows frozen:** Unfreeze, then select immediately below header.
- **View merely split:** Use Freeze and test by scrolling.
- **Header not in row one:** Confirm actual header range before freezing.

### Assumptions and limits

Freezing aids the current view and does not guarantee another person's zoom or window state. You verify the menu in your Calc version; this does not alter table data.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26201-Introduction.html) — freezing rows and columns keeps selected headers visible while scrolling.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
