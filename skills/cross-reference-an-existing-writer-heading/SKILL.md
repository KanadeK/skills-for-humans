---
name: cross-reference-an-existing-writer-heading
description: "Human-readable insertion of one Writer heading cross-reference field that remains identifiable after a heading or page change."
---
# 在 Writer 正文中引用一个现有标题 / Cross-Reference an Existing Writer Heading

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 有真正标题样式的非敏感多节 ODT 副本、目标标题 / Non-sensitive multi-section ODT copy with real heading styles and chosen target heading |
| Side effects / 现实副作用 | 正文有能对应目标标题的动态引用 / Body receives a dynamic reference to its intended heading |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你想在正文写“见某节”并让标题改名或页码移动后不至于留下纯手打旧文字时使用本篇。成果是一个指向真正现有标题的 Writer 交叉引用字段，显示内容与目标相符，跳转或更新后仍找得到。它不同于生成全篇目录，只处理一个局部引用。

### 准备与输入

保存 ODT 副本，确定目标标题在 Navigator 中存在且名称唯一或可辨，记下当前显示文字与页码。决定正文需要引用标题文字、编号还是页码，不要把不同格式混用。把光标放在句内正确位置，先不删除可读的上下文词。

### 执行

1. 打开 Insert > Cross-reference，在类型中选 Headings 并选准目标标题。
2. 选需要的引用格式并插入字段，检查显示文字与目标标题当前状态对应。
3. 按当前版本方法跳转或刷新字段，核它不是普通手打字符串且没有指向同名的错标题。
4. 保存重开，再看引用及目标；若显示错误，撤销并重选目标与格式。

### 完成、常见问题与恢复

正文引用能定位到目标标题，文字或页码与当前文稿一致，句子仍通顺。

- **找不到标题：** 先核标题是否用了真正 Heading 样式。
- **指向同名错节：** 重选可辨的目标，不只看标题字面。
- **改标题后旧字仍在：** 更新字段并核对象类型。

### 假设与边界

只处理单个文档内一个已有标题；跨文档、复杂主文档和未保存链接需另行核查。你决定引用含义。

### 来源

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26217-Fields.html)（英文，官方手册）— 交叉引用对话框可选 Headings 目标与引用格式。
- Original synthesis — 将一个文档结构结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when body prose says 'see section...' and a typed old heading or page may become stale after revisions. Finish with one Writer cross-reference field aimed at a real existing heading, displaying the intended target and surviving a navigation or update check. This is one local reference, not a document-wide contents list.

### Preparation and inputs

Save an ODT copy, confirm target appears in Navigator with an identifiable name, and note current text/page. Decide whether body needs heading text, number or page, rather than mixing formats. Place cursor in the right sentence position and preserve surrounding words.

### Execution

1. Open Insert > Cross-reference, choose Headings type and the precise target.
2. Choose the needed reference format, insert field and compare displayed text with current target.
3. Navigate or update fields in this version and check it is not typed text or a wrong same-name heading.
4. Save and reopen, inspect reference and target; undo wrong reference and select correct target and format.

### Success, common problems, and recovery

The body reference identifies the intended heading, displayed text or page agrees with current document, and sentence still reads naturally.

- **Heading absent:** Check real Heading paragraph style.
- **Wrong same-name section:** Select identifiable target, not just name.
- **Old wording remains:** Update fields and inspect object type.

### Assumptions and limits

This handles one existing heading within one document. Cross-document links and master documents require separate checks. You decide the reference meaning.

### Sources

- [LibreOffice Writer Guide 26.2](https://books.libreoffice.org/en/WG262/WG26217-Fields.html) — Cross-references dialog selects a Headings target and reference format.
- Original synthesis — one document-structure outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Writer controls. You choose the content, perform the steps and verify the result.
