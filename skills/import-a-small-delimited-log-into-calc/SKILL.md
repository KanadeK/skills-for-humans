---
name: import-a-small-delimited-log-into-calc
description: "Human-readable preview of a small permitted delimited text file before Calc import, checking separators, headers, encoding and sample rows."
---
# 在 Calc 预览后导入一份分隔文本日志 / Import a Small Delimited Log into Calc

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 现有 Calc、已知来源的无敏感信息 CSV 或分隔文本、工作副本位置 / Existing Calc, source-known non-sensitive CSV or delimited text, working-copy location |
| Side effects / 现实副作用 | 文本字段进入正确的列 / Text fields land in intended columns |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有一份允许使用的小型分隔文本，想把它作为 Calc 表格打开时使用本篇。结果是标题、行数、列数和首末样本能与原文本对上，而不是只看文件成功打开。不要导入来源不明或含别人隐私的表，导入前保留原始文本。

### 准备与输入

先以只读方式看一小段原文，确定列名、实际分隔符、是否有引号包住的备注以及预期记录数。复制原文件或确认有原件可回退。打开 Calc 的文本导入预览，注意当前编码与区域设置，不要先覆盖原件。

### 执行

1. 在预览中只勾选实际分隔符，检查带分隔符的引号备注是否仍在单格。
2. 核对中文或重音字符是否正常；如乱码，回编码选项重选，先不导入。
3. 检查编号列的前导零、日期的区域解析；必要时在预览里把这些列指定为文本。
4. 导入后对照原文核标题、列数、首末行和记录数，再另存 ODS 工作副本。

### 完成、常见问题与恢复

导入后的每个字段落在预定列，特殊字符与首末记录一致，原始文本仍保留。某行字段数异常时先停在校对，不把错列数据用于统计。

- **全部挤在一列：** 回预览改实际分隔符。
- **备注被拆成多列：** 核文本限定符与原文件格式。
- **日期或编号变形：** 重新导入并指定文本列。

### 假设与边界

只处理小型、已知来源、无敏感信息的普通文本。编码与日期解析受来源和本机区域设置影响；来源本身损坏时导入器无法凭空恢复。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26201-Introduction.html)（英文，官方手册）— Calc 的 CSV 打开流程包含导入预览、分隔符与列类型选择。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill when you have a permitted small delimited text log to open as a Calc table. Finish only when headers, row and column counts, and first/last samples match the source text. A file opening without an error is not enough. Keep the original text and avoid unknown-source or private third-party records.

### Preparation and inputs

Inspect a small source excerpt read-only. Identify headers, actual separator, quoted notes and expected record count. Preserve the original or confirm a rollback copy. Open Calc's text-import preview and note encoding and locale before overwriting anything.

### Execution

1. In preview choose only the actual separator and check that a quoted note containing it remains one cell.
2. Check Chinese or accented characters. If garbled, revise encoding before importing.
3. Check leading zeros and date parsing; set affected columns to text in preview when needed.
4. After import, compare headers, columns, first/last rows and record count, then save a separate ODS working copy.

### Success, common problems, and recovery

Fields occupy intended columns, special characters and first/last records match, and the source text remains available. If a row has an unexpected field count, stop rather than using misaligned data.

- **All data in one column:** Return to preview and choose the real separator.
- **Note splits across columns:** Check quote setting against source.
- **Date or code changes:** Re-import with text columns.

### Assumptions and limits

Only small, source-known, non-sensitive text belongs here. Encoding and date parsing depend on source and locale; import settings cannot reconstruct damaged source content.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26201-Introduction.html) — Calc CSV opening includes import preview, separator and column type choices.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
