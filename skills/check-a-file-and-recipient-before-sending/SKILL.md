---
name: check-a-file-and-recipient-before-sending
description: "Human-readable pre-send check for an ordinary low-sensitivity file: intended recipient, actual attached version, unnecessary contents, and attachment versus link mode."
---
# 发送普通文件前核对对象与版本 / Check a File and Recipient Before Sending

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 3–8 分钟 / 3–8 minutes |
| Requirements / 必要物品 | 待发普通文件、明确收件对象、可查看草稿和附件的应用 / Ordinary file, intended recipient, app where draft and payload can be reviewed |
| Side effects / 现实副作用 | 发送按钮会晚几分钟，但错版文件少一次旅行 / Send waits a few minutes; the wrong version travels less often |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你准备通过邮件或聊天给别人发送一份普通、低敏感文件，手指已经靠近“发送”时，加载这份 Skill。目标是**核对真正的收件人、真正附上的版本，以及是否带了不必要内容**，再由你决定发送。它不替你判断私密资料能否外传，也不保证发错后可撤回。

只处理本人有权发送的普通文件。身份证件、医疗或财务资料、凭据、机密项目、群发和正式申报遵守实际政策；不在这里用一套通用清单授权。共享链接的访问范围需要另行核对，不能把“我插入了链接”当成“只给这一个人看”。

### 准备与输入

写清楚一句：**谁**需要**哪份内容的哪个版本**，以附件还是链接接收，用来阅读还是继续编辑。若对方要求的格式尚未确定，先询问或导出并检查可读副本。打开将要使用的文件，确认内容与预期一致；不要仅凭 `final` 或最近修改时间选择。

### 执行

1. **核对对象而非联系人缩写。** 在草稿的“收件人/抄送/密送”或聊天会话顶部，逐个查看完整地址、号码或明确身份；自动补全和相似姓名要展开确认。回复全部时尤其看实际新增的人。多一个不相关对象，就从草稿移除并重查。
2. **从文件本身核对版本。** 打开准备附上的那一份，检查标题、日期、关键内容和你知道的版本差异。若有两个相似文件，分别打开对照，明确当前要交付哪一个。没有确定版本时先暂停，不把“名字看着新”当证明。
3. **看是否多带了内容。** 检查明显不属于这次交付的附加页、其他人的资料、旧批注、空白或草稿内容；不需要的内容应从你有权编辑的交付副本移除，再重新打开核对。看不懂的隐藏信息或权限提示意味着暂停，请实际负责人判断；一次目视检查不等于隐私审计。
4. **核对实际载体。** 在草稿中查看附件名称、数量和上传完成状态；能从草稿预览时打开一次。某些应用会把大附件改成云端链接；若实际是链接，检查链接指向的文件与版本，并按共享范围流程确认谁能看或编辑。未完成上传、失效链接或未知权限都不发送。
5. **读一遍最终草稿。** 消息正文只说明这是什么、版本或日期、希望对方做什么；不要暗示附件已经有，而草稿实际上没有。最后再看一遍收件对象和附件/链接。确认两边匹配后，才由你点击发送。
6. **发送后只核对状态。** 若你选择发送，查看应用是否显示已发送而非仍在草稿或上传中；这不证明对方已读或能打开。需要接收方确认时明确请求。发现发错后，立即按实际平台的取消/求助方式处理；不要把短暂的“撤销发送”窗口当作普遍保障。

### 完成条件

发送前，草稿里是正确对象、正确且已上传的文件或经核对范围的链接，明显无关内容已处理；不确定项会阻止发送。若已发送，只能说应用显示发送成功；对方收到、打开、接受仍需后续观察。任何一个关键事实未知，都以草稿停住为合格结果。

### 常见报错与补救

- **自动补全选中了同名的人：** 删除错误对象，展开真实地址或号码后重新选择；附件是否正确不能弥补收件人错误。
- **两个附件名几乎一样：** 从草稿打开或返回原文件分别比较内容，删掉错误附件并重新附上正确版本，再看上传完成。
- **应用把附件换成云端链接：** 暂停发送，检查链接文件和实际访问范围；不适合时换可用的附件方式或问对方接受什么。
- **发现多余页或旧批注：** 回到交付副本处理并重新导出/附上；别在发送前一秒仅修改源文件，旧附件不会自动更新。
- **已经点了发送才发现问题：** 先查看应用是否确实已发或仍可取消，再按实际平台和影响联系相关人；不能保证召回成功，不继续转发来“稀释”错误。

### 假设、替代与现实副作用

邮件、聊天和云盘各自处理自动补全、附件、链接及发送状态；依你眼前的界面核对。可以用键盘或屏幕阅读器逐个检查收件字段和附件列表，不靠图标颜色猜。你会多花几分钟，但发送出去的副本通常不会随你随后修改源文档而自动变成新版。

### 来源

- [Microsoft：在 Outlook 中附加文件](https://support.microsoft.com/en-us/outlook/mail/add-pictures-or-attach-files-to-emails-in-outlook)：附件副本与 OneDrive 链接行为不同。
- [Microsoft：在 Outlook 中新建邮件](https://support.microsoft.com/en-us/outlook/mail/create-an-email-message-in-outlook)：收件人字段和建议联系人需要实际核对。
- [Google：Gmail 附件](https://support.google.com/mail/answer/6584?hl=en)：可移除附件，过大附件可能转为 Drive 链接。
- [Google：Gmail 发送与撤销](https://support.google.com/mail/answer/2819488?hl=en)：撤销只在设定的短时间内可用，不是通用补救保证。

## English

Load this Skill when you are about to send an ordinary, low-sensitivity file by email or chat and your finger is near Send. **Check the actual recipient, actual attached version, and unnecessary contents**, then choose whether to send. This does not authorize disclosure of private material or guarantee that a mistaken send can be recalled.

Handle only an ordinary file you may send. Identity, medical, financial, credential, confidential project, mass-mailing, and formal submission tasks follow their real rules; this checklist does not grant permission. A shared link's access scope needs its own check. Inserting a link does not mean that only one intended person can see it.

### Preparation and inputs

State one sentence: **who** needs **which contents and version**, as an attachment or link, for reading or further editing. If the required format is unknown, ask or export and inspect a readable copy first. Open the file you intend to use and check its contents; do not choose by `final` or modification time alone.

### Execution

1. **Check the person, not a contact abbreviation.** Inspect each full address, number, or clear identity in To/Cc/Bcc or at the top of the chat. Expand autocomplete and lookalike names. On Reply All, check the people actually added. Remove an unrelated recipient and recheck the draft.
2. **Check the version from its contents.** Open the exact file to attach and compare title, date, critical contents, and a version difference you know. If two files look alike, open both and decide which is the intended delivery version. Pause when you cannot tell; a newer-looking name is not proof.
3. **Look for extra material.** Inspect obvious unrelated pages, other people's information, old comments, blanks, and draft content. Remove unnecessary content from a delivery copy you may edit and reopen it. Unknown hidden information or a permission warning means pause and ask the responsible person; a visual check is not a privacy audit.
4. **Check the actual payload.** Review attachment name, count, and upload completion in the draft; open the draft preview if available. Some apps replace a large attachment with a cloud link. If it is a link, check the target file/version and use the sharing-scope procedure to confirm who may view or edit it. Do not send while upload, link validity, or permission is unknown.
5. **Read the final draft once.** The message should say what the file is, its version or date, and what you want the recipient to do. Do not promise an attachment that the draft does not contain. Recheck recipient and attachment/link together; then you may press Send.
6. **After sending, check only the visible state.** If you send it, see whether the app says sent rather than draft or uploading. That does not prove receipt, opening, or acceptance. Ask for confirmation if needed. If you discover an error, use the actual platform's cancellation or help path promptly; a short Undo Send period is not a universal safeguard.

### Success

Before sending, the draft has the right recipient, the right uploaded file or a link with checked scope, and no obvious unrelated contents. Unknowns stop the send. If sent, you can only report the app's sent state; the recipient's receipt, opening, and acceptance remain to be observed. Pausing on an unknown key fact is a valid outcome.

### Common errors and recovery

- **Autocomplete picked a lookalike person:** Remove them, inspect the real address or number, and choose again. A correct attachment cannot repair the wrong recipient.
- **Two attachments have nearly identical names:** Open from the draft or compare both source files. Remove the wrong attachment, add the intended version, and wait for upload to finish.
- **The app changed the attachment into a cloud link:** Pause and verify the target and actual access scope. If unsuitable, choose a supported attachment route or ask the recipient what works.
- **An extra page or old comment appears:** Correct and re-export the delivery copy, then reattach it. Editing the source at the last second does not automatically update an old attachment.
- **You pressed Send before spotting the error:** Check whether it was actually sent or still cancellable, then follow the real platform and impact route. Recall is not guaranteed; do not forward the error again to dilute it.

### Assumptions, alternatives, and known side effects

Email, chat, and cloud drives differ in autocomplete, attachments, links, and send state; inspect the interface in front of you. A keyboard or screen reader can review recipient fields and the attachment list without relying on icon color. This costs a few minutes, but a sent copy generally does not become the new version when you later edit the source.

### Sources

- [Microsoft: Add pictures or attach files in Outlook](https://support.microsoft.com/en-us/outlook/mail/add-pictures-or-attach-files-to-emails-in-outlook): An attached copy and a OneDrive link behave differently.
- [Microsoft: Create an email message in Outlook](https://support.microsoft.com/en-us/outlook/mail/create-an-email-message-in-outlook): Recipient fields and suggested contacts require checking.
- [Google: Gmail attachments](https://support.google.com/mail/answer/6584?hl=en): Attachments can be removed and oversized ones may become Drive links.
- [Google: Send or unsend Gmail messages](https://support.google.com/mail/answer/2819488?hl=en): Undo is available only for a chosen short period, not a universal recovery guarantee.

If AI opens this file, it may help format a pre-send checklist. You remain the Human Runtime and inspect the draft, decide, and press Send if appropriate.
