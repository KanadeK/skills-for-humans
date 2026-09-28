---
name: free-device-space-from-known-disposable-files
description: "Human-readable steps for freeing a small amount of device storage through visible app controls and files you can identify as disposable."
---
# 设备空间不足时只清理确认可弃的文件 / Free Device Space from Known Disposable Files

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 本机存储界面、要完成的一个普通任务、你能辨认的可弃文件 / Device storage view, one ordinary task needing space, and files you can identify as disposable |
| Side effects / 现实副作用 | 空间可能只多一点；系统文件没有被选作祭品 / Space may increase modestly; system files stay off the altar |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当**这台设备**提示本机空间不足，影响下载、拍照或保存一个普通任务时，用这份 Skill 找到少量明确可弃内容并核验是否真的腾出空间。只使用系统或应用可见界面；不删除系统关键目录，不执行命令、清注册表或安装“清理神器”。云端账号配额满是另一份 Skill，因为删同步文件可能在多端传播。

### 准备与输入

先看设备的**本机可用空间**及哪个任务失败，不把云盘“剩余容量”和硬盘容量混为一谈。定一个小目标，例如足够保存这次材料，而非“清得越多越好”。确认你是否有可用备份；对没有第二份的照片、文档、录音和下载原件，先视为不可弃。受管设备按管理员要求，不擅自清应用或系统文件。

### 执行

1. **看用量，不直接按推荐清空。** 打开设备自带的存储界面，看大类和实际可用量；只进入你能辨认的普通下载、你自己生成的临时导出、已不再需要的重复文件或应用提供的缓存选项。系统“临时文件”列表可能夹带回滚资料、下载和回收站内容，每一项都要看说明。
2. **给每个候选一个去留理由。** 看文件名、位置、日期和预览；确认它是可重下的副本或已有独立可用备份。同步文件的“仅保留云端/释放本机空间”是改变本机可用性，通常不同于删除云端原件；离线需要它时不要选。不能辨认就不删。
3. **先选小而明确的一批。** 优先从你明确不再需要的下载副本、完成后的多余导出或应用内可清的缓存开始。使用当前应用的普通删除/清理控件，核其提示是否影响原件或其他设备；不勾选整个目录、不删除未知扩展名和系统文件。
4. **检查结果与回收区。** 回到存储界面，看可用空间是否增加。普通删除若只进回收站，可能还没腾出同等空间；仅对刚才已逐件确认可弃且无独有内容的项目，才考虑应用提供的永久清除。清空整个回收站会影响其他文件，别为了这一批一键清空。
5. **达到目的就停。** 用原来失败的普通任务做一次小型保存/下载检查；若仍不足或没有安全候选，停止清理，改用已授权的其他存储位置/设备或请管理员/相应支持处理，不向系统目录找“隐藏大户”。

### 完成、常见问题与补救

设备显示本机可用空间实际增加，且原任务能继续；或你已确认没有可安全丢弃的内容并选择不删除。删除了几个文件但空间没变化，不算已经解决。

- **推荐清理含“以前的系统版本”：** 先看回滚影响；本 Skill 不以删除系统回退能力换一次普通保存。
- **下载目录里有唯一原件：** 保留，先核是否有可打开的独立备份；“是下载的”不等于可重新取得。
- **删了同步文件后别的设备也不见：** 立即停止，按对应服务的回收/恢复流程核，不继续批量删除。
- **空间数值暂时没变：** 看文件是否仍在回收区或系统尚未更新显示，核对后再决定，勿盲目加大删除量。
- **视觉或操作能力限制逐件核对：** 用列表朗读、放大或可信协助逐项确认；无法识别时停止。

### 假设、替代与现实副作用

本机存储界面、回收站行为和缓存说明因系统/应用而异；Windows 的存储建议只是一个示例，不自动授予“安全可删”判断。可能只腾出一点空间，但能保住唯一原件。云端仅在线文件需要联网才能再用，不把它当离线备份。

### 来源

- [Microsoft Support：Free up drive space in Windows](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)（英文，官方）— 查看实际空间，逐类核清理建议；某些系统回退文件删除不可逆。
- [Microsoft Support：Manage drive space with Storage Sense](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)（英文，官方）— 回收站、下载文件及云端仅在线状态有不同的清理条件。
- Original synthesis — 以一个任务的空间需求为停点，只处理可识别且可弃的普通项目，逐项核删除影响。

## English

Load this Skill when **this device** reports low local space and an ordinary download, photo, or save cannot finish. Identify a small number of files you can confidently discard, then verify space actually increased. Use visible system or app controls only; do not remove system folders, run commands, edit the registry, or install a “cleaner.” A full cloud-account quota has a separate Skill because synced deletion can spread across devices.

### Preparation and inputs

Check **local available space** and which task failed; cloud quota and disk capacity are different. Set a small goal, such as enough space to save this item, rather than “remove as much as possible.” Check whether a usable backup exists. Treat photos, documents, recordings, and downloaded originals without another copy as non-disposable. Follow administrator instructions on a managed device.

### Execution

1. **Inspect usage before accepting recommendations.** Open the device's built-in storage view and note available space and large categories. Visit only ordinary downloads, your own extra exports, duplicates you can recognise, or an app-provided cache option. A “temporary files” list can include rollback data, Downloads, or Recycle Bin content; read each item's meaning.
2. **Give each candidate a reason.** Check name, location, date, and preview. Confirm it is a replaceable copy or has an independently usable backup. Making a synced file online-only or releasing local space changes local availability and is usually different from deleting its cloud original; do not do that when you need it offline. Keep unidentified items.
3. **Select one small certain batch.** Start with no-longer-needed download copies, extra finished exports, or an app's clearly described cache. Use ordinary delete or cleanup controls and read whether they affect originals or other devices. Do not select entire directories, unknown extensions, or system files.
4. **Check the result and trash.** Return to the storage view to see whether available space rose. Ordinary deletion into a recycle area may not release the same amount yet. Consider permanent removal only for the exact just-checked disposable items when the app allows it. Emptying all trash could remove other files; do not use it as a shortcut for this batch.
5. **Stop at the task goal.** Try one small save or download that previously failed. If space is still short or you have no safe candidate, stop and use an authorised alternative location or device, or ask the administrator or relevant support. Do not search system directories for a “hidden big file.”

### Success, common problems, and recovery

Local available space actually increased and the original task can continue; or you established that no safe disposable item is available and chose not to delete. A few deleted filenames without a space change is not a solved storage problem.

- **Cleanup suggests a previous system version:** Check the rollback consequence. This Skill does not sacrifice system rollback to save one ordinary item.
- **Downloads contains a sole original:** Keep it until an independent backup can be opened. “Downloaded” does not prove it can be retrieved again.
- **A synced file disappears elsewhere after deletion:** Stop immediately and check the service's recovery route before any more bulk deletion.
- **The space figure has not changed:** Check whether items remain in trash or the display has not updated. Do not simply increase the deletion batch.
- **Vision or motor needs limit item-by-item review:** Use list reading, magnification, or trusted help. Stop when an item cannot be identified.

### Assumptions, alternatives, and side effects

Storage views, trash behaviour, and cache descriptions vary by system and app. Windows storage recommendations are examples, not automatic proof that an item is safe to lose. A modest space gain can still preserve the only original. Online-only files require a connection later and are not an offline backup.

### Sources

- [Microsoft Support: Free up drive space in Windows](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows) — inspect actual space and categories; deleting some rollback material is irreversible.
- [Microsoft Support: Manage drive space with Storage Sense](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense) — Recycle Bin, Downloads, and cloud online-only settings have different cleanup effects.
- Original synthesis — use one task's space need as a stopping point and verify each ordinary item and deletion effect.

If AI opens this file, it may explain a storage label. You inspect, remove only a known disposable item, verify, or stop.
