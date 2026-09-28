---
name: check-an-interrupted-ordinary-message-draft
description: "Human-readable steps for finding an interrupted unsent ordinary message draft, checking what was saved, and avoiding an accidental duplicate send."
---
# 写到一半中断后找回普通消息草稿 / Check an Interrupted Ordinary Message Draft

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 3–10 分钟 / 3–10 minutes |
| Requirements / 必要物品 | 原邮件/消息应用、相关账号、主题或收件人线索 / The original mail or message app and account, plus a subject or recipient clue |
| Side effects / 现实副作用 | 可能找到不完整草稿；“没点发送”仍需核实 / You may find only part of a draft; “I didn't click Send” still needs checking |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你写一条**普通、低敏感**邮件或消息，应用被关闭、页面中断或切设备后找不到刚写的文字时，加载这份 Skill。先判断消息是否已发送，再看原应用有没有可恢复的草稿；结果可以是保留一份待核草稿，也可以是明确“未找到”。本篇不发送消息、不登录陌生恢复站、不接触密码、医疗/财务或机密内容。

### 准备与输入

记下你原来使用的应用与账号、收件人/对话、主题或两三个独特词，以及大致中断时间。先不要打开新的同名草稿并开始重写，以免混淆哪段是原文。若账号本身无法访问或疑似被盗，停止并走该平台的正式支持流程，不在这里尝试账号恢复。

### 执行

1. **先排除已发送。** 在原应用和账号的“已发送”或原对话里查一次；如果消息已经发出，先核内容与对象，再决定是否需要普通更正。不要因为输入框空了就当草稿丢失，更不要立即重发。
2. **找应用提供的草稿入口。** 邮件通常有“草稿/Drafts”；消息应用可能把未发送文字留在原对话，也可能根本不保存。按原账号、对话、主题和最近时间查，避免把另一个人的同名草稿当成自己的。不同设备是否同步取决于应用与网络状态；优先在原设备检查。
3. **只读核对恢复程度。** 打开候选后先看开头、结尾和你记得的独特句子；有些应用按间隔自动存，最后几句可能没进草稿。核对 To/Cc、主题、附件和文本是否属于这次消息，不按草稿时间戳保证完整。
4. **保留安全副本但不发送。** 如果草稿可用，让它留在原应用并确认显示已保存；需要本地备份时，只按应用/组织许可复制普通文本到自己控制的安全位置。不要把私人或受管内容粘贴到公共笔记、搜索框或 AI 服务。若多个草稿相似，用日期/用途标记区分，勿盲删。
5. **处理缺失或冲突。** 若只有一部分，补写前先标出缺口；若查不到，记“原应用未找到可用草稿”，再从自己的要点重写。任何后续发送都要重新核收件人、内容与附件，且由你另行决定；找回草稿本身不等于发送。

### 完成、常见问题与补救

你已核实消息究竟有没有发出；若未发送，保留一份内容与对象已核的草稿，或标明原应用没有找到可用草稿。这样可以避免重复发送。只看到“草稿 1”字样却没核内容，不算找回。

- **草稿里只剩半句：** 接受应用可能只存到上次间隔，标缺口，从自己记得的要点补写，不声称逐字恢复。
- **草稿在另一设备看不到：** 回原设备/原账号查，确认应用是否显示同步；不要为同步问题改变账号安全设置。
- **发现同内容已发送：** 停止重发，核原消息；若附件或版本错，另走 H235 的明确更正。
- **草稿对象或附件变了：** 暂停发送，重新核人、文本、附件；不让自动填充替你决定。
- **草稿被删除或应用不保存：** 记录未找到，止步于官方应用入口；不装不明恢复插件或提取浏览器缓存。

### 假设、替代与现实副作用

Gmail 和 Outlook 有草稿机制，但保存时点及跨设备状态不同；一般聊天或网页表单未必有。读屏、语音和移动端可用应用的草稿列表与收件人朗读核对。找到草稿之后，你仍需自己判断是否、何时、向谁发送；本 Skill 不自动完成沟通。

### 来源

- [Gmail Help：Write & send email](https://support.google.com/mail/answer/9259768?hl=en)（英文，官方）— Gmail 在 Drafts 里自动保存正在写的邮件。
- [Microsoft Support：Save an Outlook message as a draft](https://support.microsoft.com/en-us/outlook/mail/save-an-outlook-message-as-a-eml-file-a-pdf-file-or-as-a-draft)（英文，官方）— 未发送邮件可在 Drafts 找到；自动保存间隔受版本影响。
- [Google Docs Editors Help：Autosave your response progress on a Google Form](https://support.google.com/docs/answer/10952360?hl=en)（英文，官方）— 表单草稿受登录、在线、表单主人设置与时间条件影响，不能推广到所有输入框。
- Original synthesis — 先查已发送，再核草稿内容与对象，避免误发或重复发。

## English

Load this Skill when you were writing an **ordinary, low-sensitivity** email or message and an app closed, a page was interrupted, or you changed device before you could find the text again. Check whether it was sent before looking for an app-provided draft. The result can be a preserved draft to review or an honest “not found.” This does not send a message, use an unfamiliar recovery site, or handle passwords, medical or financial content, or secrets.

### Preparation and inputs

Recall the original app and account, recipient or conversation, subject or a few distinctive words, and roughly when the interruption occurred. Avoid creating and rewriting a new same-named draft before checking what survived. If the account is inaccessible or may be compromised, stop and use the platform's official support route; account recovery is outside this task.

### Execution

1. **Rule out an already sent message first.** Check Sent or the original conversation in the original app and account. If it went out, inspect its content and audience before deciding whether it needs an ordinary correction. An empty composer does not prove loss; do not immediately send another copy.
2. **Use the app's draft entry.** Mail often has Drafts. A messaging app may keep unsent text in the conversation or may save none. Search by account, conversation, subject, and recent time so another person's similar draft is not mistaken for yours. Cross-device sync depends on app and network state; start with the original device.
3. **Check the recovered content before editing.** Read the opening, ending, and your distinctive phrases. Some apps autosave on an interval, so the last lines may be absent. Check To/Cc, subject, attachments, and text against this message. A draft timestamp does not guarantee completeness.
4. **Preserve safely without sending.** Leave a usable draft in the original app and confirm it shows saved. If you need a local backup, copy only ordinary text to a secure location you control when the app and organisation allow it. Do not paste private or managed content into public notes, search boxes, or AI services. Label similar drafts by date or purpose rather than deleting blindly.
5. **Handle gaps or conflicts.** Mark missing passages before rewriting them. If nothing appears, record “no usable draft found in the original app” and rebuild from your own key points. Any later send needs a fresh check of recipients, content, and attachments, and your own decision. Finding a draft is not sending it.

### Success, common problems, and recovery

You determined whether the message was sent. If it was not, you preserved an unsent draft whose content and audience you reviewed, or recorded that no usable draft was found. This avoids a duplicate send. A “Drafts 1” badge without content review is insufficient.

- **The draft has only half a sentence:** It may have saved only at the last interval. Mark the gap and rebuild from your own points rather than claiming exact recovery.
- **The draft is absent on another device:** Check the original device and account and any visible sync state. Do not change account security settings to chase a draft.
- **The same content was already sent:** Stop the duplicate, inspect the original, and use H235's explicit correction for a wrong attachment or version.
- **The recipient or attachment changed:** Pause any send and verify person, text, and file; autocomplete should not decide for you.
- **The draft was deleted or the app does not save one:** Record not found and stop at official app controls; do not install unknown recovery plugins or extract browser caches.

### Assumptions, alternatives, and side effects

Gmail and Outlook have drafts, but save intervals and device sync vary. Ordinary chats and web forms may not. Screen reading, speech, or mobile app lists can help verify draft and recipient details. You still decide whether, when, and to whom to send afterward; this Skill does not complete that communication.

### Sources

- [Gmail Help: Write & send email](https://support.google.com/mail/answer/9259768?hl=en) — Gmail automatically saves composing mail under Drafts.
- [Microsoft Support: Save an Outlook message as a draft](https://support.microsoft.com/en-us/outlook/mail/save-an-outlook-message-as-a-eml-file-a-pdf-file-or-as-a-draft) — unsent mail may be in Drafts; autosave interval varies by version.
- [Google Docs Editors Help: Autosave your response progress on a Google Form](https://support.google.com/docs/answer/10952360?hl=en) — form drafts depend on sign-in, online status, owner settings, and time; not all text fields work this way.
- Original synthesis — check Sent first, then draft content and audience to avoid accidental or duplicate sending.

If AI opens this file, it may explain a draft label. You check, preserve, decide about sending later, or stop.
