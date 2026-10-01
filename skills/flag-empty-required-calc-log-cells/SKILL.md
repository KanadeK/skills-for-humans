---
name: flag-empty-required-calc-log-cells
description: "Human-readable conditional formatting of one required Calc log column to reveal blanks without inserting guessed data or changing originals."
---
# 标出 Calc 日志必填列的空白格 / Flag Empty Required Calc Log Cells

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 已保存的普通日志、一个已确定必填的数据列、可辨认的单元格样式 / Saved ordinary log, one required data column and discernible cell style |
| Side effects / 现实副作用 | 缺值格可见而原数据未被填造 / Missing cells become visible without invented values |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你知道日志的某一列应该每行都有值，却不能快速看出漏填时使用本篇。结果是已有记录区中的空白格被轻微且可辨认的样式标出，非空格保持正常，原数据不被猜值填入。一次只处理一个必填列，避免把备注这种可空字段误报成错误。

### 准备与输入

保存副本，确定真实记录从第几行到第几行，选定一个必填列如日期列，排除标题和未来空行。手工找一格已知空白、一格已知有值作测试。确认 Calc 的 AutoCalculate 已启用，并选一个不遮文字的条件样式。

### 执行

1. 只选该列已使用的数据区，在 Format > Conditional > Condition 中选择公式条件。
2. 用首个数据格作为相对引用设置空白判断，例如选 B2:B11 时使用 `B2=""`，应用轻度标识样式。
3. 检查已知空格亮起而有值格不亮；再看标题、别列和未使用的空行没有被染色。
4. 保存重开并复核；若整列都亮，撤销或编辑规则的引用和适用范围。

### 完成、常见问题与恢复

选定必填列的实际漏填格被标出，有值格不误标，记录内容与行数未改。

- **整列都亮：** 检查相对引用和规则范围。
- **缺格不亮：** 核自动计算及样式对比度。
- **未来空行也亮：** 缩小到当前数据区，追加时再扩规则。

### 假设与边界

条件格式只辅助发现，不能证明数据正确或自动补全。你决定哪些列必填；不同版本的公式语法与菜单可能不同，应以本机帮助和已知空/非空对照为准。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26203-FormattingData.html)（英文，官方手册）— 条件格式可按公式改变单元格样式，自动计算须启用。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when one log column is required on every recorded row but missing entries are hard to spot. Finish with blanks in the existing record range visibly marked by a modest style, nonblank cells unchanged, and no invented values inserted. Handle one required column at a time so optional notes are not falsely flagged.

### Preparation and inputs

Save a copy, identify first and last actual data rows and one required column such as Date. Exclude header and future unused rows. Find one known blank and one filled cell as tests. Confirm Calc AutoCalculate is on and choose a style that does not obscure text.

### Execution

1. Select only used cells in that column and open Format > Conditional > Condition with a formula condition.
2. Use the first data cell as a relative blank test, for example `B2=""` on B2:B11, and apply a subtle visible style.
3. Check the known blank highlights and the filled cell does not; header, other columns and future rows should remain unaffected.
4. Save and reopen to verify. If every cell lights, undo or edit formula reference and applied range.

### Success, common problems, and recovery

Actual blanks in the chosen required column are marked, filled cells are not, and record contents and row count remain unchanged.

- **Entire column highlights:** Check relative reference and applied range.
- **Blank not marked:** Check AutoCalculate and style visibility.
- **Future blank rows highlight:** Limit range to current data and extend later.

### Assumptions and limits

Conditional formatting only helps locate omissions; it neither proves correctness nor fills data. You decide what is required. Formula syntax and menus may vary; verify with known blank and filled cells.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26203-FormattingData.html) — conditional formatting can apply a style from a formula when AutoCalculate is enabled.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
