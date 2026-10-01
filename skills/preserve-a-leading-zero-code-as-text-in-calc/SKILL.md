---
name: preserve-a-leading-zero-code-as-text-in-calc
description: "Human-readable entry and reopen check for a leading-zero identifier in Calc so code 0012 remains text rather than quantity 12."
---
# 在 Calc 保留有前导零的记录编号 / Preserve a Leading-Zero Code as Text in Calc

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–10 分钟 / 5–10 minutes |
| Requirements / 必要物品 | 现有 Calc、应逐字保留的非敏感编号、可保存工作副本 / Existing Calc, non-sensitive exact identifiers and savable working copy |
| Side effects / 现实副作用 | 编号 0012 重开后仍为 0012 / Code 0012 remains 0012 after reopening |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你要录入像 `0012` 这样编号而非数量的内容时使用本篇。成果是在 Calc 内显示、保存并重开后仍逐字保留 `0012`，不把它变成 12 再用显示格式伪装。这里处理一个数据类型决策，不计算编号，也不修改其他列。

### 准备与输入

先确认原编号的精确字符和位数，保存工作副本，圈定仅有编号的那一列。若该列已经把 0012 压成 12，原字符可能不可从现值推回，需要找原始来源。别拿真实手机号或身份证号练习。

### 执行

1. 将编号列设为文本格式，或在单次录入时先键入撇号再键入编号。
2. 输入练习编号 0012 和 0100，移出单元格后用输入栏核实际内容，不只看列宽。
3. 保存为 ODS，关闭并重新打开工作副本，逐个与源编号对照。
4. 确认后才沿用同一列规则录入剩余编号；若重开少零，从原件重输。

### 完成、常见问题与恢复

两个样本和实际需要的编号保存重开仍逐字一致；若源信息已丢失，明确记录不能推断零的个数。

- **只显示补零：** 核类型是否仍为数字，别以格式代替文本。
- **导入时又掉零：** 回导入预览把编号列指定文本。
- **原编号未知：** 回原文件或标签查，不补猜。

### 假设与边界

编号作为文本不参与算术。你负责核对原始字符；本篇不适用于需要数学位数格式的测量值，也不能修复已丢失来源的编码。

### 来源

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html)（英文，官方手册）— 数字录入默认丢前导零，文本格式或前置撇号可保留。
- Original synthesis — 将一个表格结果、原始记录对照和失败停点组合为可核流程。

## English

Use this Skill for an identifier such as `0012` that is a code, not a quantity. Finish only when Calc displays and preserves `0012` after save and reopen, rather than storing 12 and decorating its display. This resolves one data-type decision; do not calculate with the code or change other columns.

### Preparation and inputs

Confirm exact source characters and length, save a working copy and select only the code column. If `0012` was already collapsed to 12, missing characters may not be recoverable from that cell; return to source. Avoid practising with real phone or identity numbers.

### Execution

1. Set the code column to Text format, or prefix one entry with an apostrophe before typing.
2. Enter sample codes 0012 and 0100. Leave each cell and inspect actual content in the input line.
3. Save as ODS, close and reopen the working copy, comparing each code with source character by character.
4. Only then use the same column rule for remaining codes. If zeros disappear, re-enter from source.

### Success, common problems, and recovery

Both samples and needed codes match character for character after reopening. If source characters were lost earlier, record that their count cannot be inferred.

- **Zeros only visual padding:** Check whether value remains numeric; formatting is not text.
- **Import drops zeros:** Set code column to text in preview.
- **Original unknown:** Consult source file or label instead of guessing.

### Assumptions and limits

Identifiers stored as text are not arithmetic inputs. You verify original characters. This is not for measured numbers and cannot reconstruct a lost source code.

### Sources

- [LibreOffice Calc Guide 26.2](https://books.libreoffice.org/en/CG262/CG26202-EnteringandEditingData.html) — numeric input drops leading zeros while text format or an apostrophe preserves them.
- Original synthesis — one spreadsheet outcome, source comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Calc controls. You choose the data, perform the steps and verify the result.
