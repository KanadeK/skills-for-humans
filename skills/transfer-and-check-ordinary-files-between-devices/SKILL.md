---
name: transfer-and-check-ordinary-files-between-devices
description: "Human-readable transfer of a small ordinary file set between devices, checking target identity, counts, opened contents, and source retention."
---
# 在两台设备间转移并核对普通文件 / Transfer and Check Ordinary Files Between Devices

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–25 分钟，加传输时间 / 10–25 minutes plus transfer |
| Requirements / 必要物品 | 本人有权处理的普通文件、两台目标明确的设备、已可用的传输方式 / Ordinary files you may manage, two identified devices, an available transfer route |
| Side effects / 现实副作用 | 目标设备多一份副本，来源暂时保留 / Another copy exists on the destination while the source remains |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你要把一小组普通、低敏感文件从自己的一个设备带到另一个设备使用时，加载这份 Skill。目标是**让目标设备上出现正确数量、可打开的文件，并清楚知道来源和目标各保留什么**。传输成功提示不是验收；传输副本也不自动成为经试恢复的备份。

只处理你有权转移的普通文件。账号登录、凭据、设备管理、机密资料外传和软件安装不在这里。选已有且获准使用的传输方式，例如线缆、外接盘、设备间分享或已授权的云端位置；若要新登录或改变共享权限，先停下按对应流程处理。

### 准备与输入

在来源设备列出本批文件名、数量、关键版本与原位置，选一个你能逐个核对的小范围。确认目标设备的名称/身份和预期存放文件夹；附近有同名设备时别靠图标猜。查看目标位置是否已有同名文件，默认不覆盖。估计传输容量与连接是否够用；未知就先传一份普通样本。

### 执行

1. **先复制，保留来源。** 在已有授权界面选择目标文件，执行复制或发送，而不是一开始就剪切/删除。对于设备间分享，确认屏幕上实际接收的设备名称及必要的确认码；目标不对就取消。
2. **等传输结束。** 留意应用是否显示仍在上传、下载、等待接受或失败。用外接盘时完成写入后按系统方式弹出，再物理拔出。不要把进度提示、分享请求或云端占位图标当作完整内容。
3. **在目标设备定位副本。** 打开实际接收位置；不同应用可能放在“下载”、照片库、Quick Share 文件夹或你指定的位置。若找不到，查应用的接收记录与默认位置，不立刻再发一批制造重复。
4. **核对数量与身份。** 将来源清单和目标文件逐项对照文件名、数量及关键版本。相同名字可能已存在旧版；遇到重名先打开区分，不在提示里点覆盖。多文件批次有一项缺失，就标本批未完成并只补缺项。
5. **打开真正要用的内容。** 在目标设备上逐个打开本批关键文件，核对能否显示需要的文字、图片或页数。若本批太大不能全查，记录已抽查哪些和未验证哪些，不把抽样说成全量可读。格式打不开时保留来源，另行导出目标设备支持的格式再传。
6. **决定保留位置。** 核对通过前不删来源。本次若只是为了在第二台设备使用，两边都可保留并写明哪个是工作版本；若以后要腾出空间，先查真实备份和删除影响，再单独决定。此时记录目标路径和结果，不把普通复制当防丢失方案。

### 完成条件

目标设备上的本批文件能按清单找到，数量与版本对应，关键内容实际打开可用；来源仍在，目标位置明确。部分文件未读、仍在下载或无法确定重名版本时，只记录部分完成并保留来源。成功通知或文件图标不能替代这些检查。

### 常见报错与补救

- **分享面板出现多个相似设备：** 核对设备名与接收端提示或确认码，选错就取消；不试探发送给陌生设备。
- **传完数量少了：** 对照来源清单找缺项，只补缺失项并重查，不因为应用写“完成”就忽略它。
- **目标能看到文件但打不开：** 检查下载/复制是否结束和目标是否有可用查看方式；保留来源，用可读格式重新导出或转移。
- **提示同名覆盖：** 取消，分别打开旧目标文件与新来源，决定保留两个版本或改名；不让一次转移抹掉旧工作。
- **外接盘还在写入：** 等待完成并安全弹出；若设备断开，重连后在目标检查文件实际可读性，不以部分文件名出现为完成。

### 假设、替代与现实副作用

各系统的接收目录、可见性、权限和“已完成”提示不同，以实际设备和应用说明为准。可以用列表、键盘、屏幕阅读器或文件搜索核对，而不靠缩略图。设备间普通复制形成另一份现时副本，但如果来源被误删、两份都同步删除或设备同时损坏，这次转移本身不能证明可恢复。两台设备有了文件，也有了两个容易被误认成“最新版”的位置。

### 来源

- [Microsoft：用外接存储迁移到新 Windows PC](https://support.microsoft.com/en-us/windows/experience/backup-recovery/move-your-files-to-a-new-windows-pc-using-an-external-storage-device)：复制后查看目标位置并安全弹出。
- [Microsoft：在 Windows 中安全移除硬件](https://support.microsoft.com/en-us/windows/hardware/safely-remove-hardware-in-windows)：断开外接盘前先完成安全移除。
- [Google：Android 与 Windows 的 Quick Share](https://support.google.com/android/answer/13801258?hl=en)：接收设备确认与接收位置依工具而定。
- [Apple：用隔空投送发送到附近 Apple 设备](https://support.apple.com/en-mide/guide/iphone/iphcd8b9f0af/27/ios/27)：接收项目可能落在下载文件夹或对应应用；需到目标端查找。

## English

Load this Skill when a small set of ordinary low-sensitivity files must be usable on another device you control. **Get the right number of readable files on the target and know what remains at both ends.** A transfer-success notice is not acceptance. A transferred copy is not automatically a backup with a tested restore path.

Handle only ordinary files you may move. Signing in, credentials, device administration, confidential disclosure, and software installation are outside this Skill. Use a transfer route already available and authorized, such as a cable, external drive, nearby sharing, or an approved cloud location. Stop for the proper process if new login or sharing-permission changes are required.

### Preparation and inputs

On the source device, list this batch's names, count, key versions, and original location. Choose a scope you can check file by file. Confirm the target device's name/identity and intended folder; do not guess from an icon when similar devices are nearby. Check for name collisions at the destination and assume no overwrite. Consider capacity and connection; start with one ordinary sample if uncertain.

### Execution

1. **Copy first; retain the source.** Select the intended files in the existing authorized interface and copy or send them rather than cutting or deleting at the start. For nearby sharing, confirm the actual receiver name and any matching code shown on the receiver. Cancel a wrong target.
2. **Wait for completion.** See whether the app is still uploading, downloading, awaiting acceptance, or reporting failure. With an external drive, wait for writes to finish and eject it through the system before unplugging. A progress indicator, share request, or cloud icon without downloaded content is not a completed transfer.
3. **Locate copies on the target.** Open the actual received location. Depending on the tool, it may be Downloads, a photo library, a Quick Share folder, or a place you chose. If absent, inspect the app's receipt record and default folder before sending the whole batch again.
4. **Compare count and identity.** Match target items against the source list by name, count, and key version. An old target file may have the same name. Open and distinguish collisions rather than clicking overwrite. One missing file means the batch is incomplete; resend only what is missing.
5. **Open the content needed for use.** On the target device, open each critical file and check the required text, image, or page count. If a batch is too large to check fully, record the sample and unverified remainder; sampling is not full readability proof. If the target cannot open a format, keep the source and export a supported format before trying again.
6. **Decide what stays where.** Do not delete the source before checking the target. If this is for using files on the second device, both copies may remain; state which is the working version. If you later need space, inspect actual backup and deletion effects in a separate decision. Record the target path and result rather than calling this ordinary copy a loss-protection plan.

### Success

You can find the target batch from the list, counts and versions match, and critical contents actually open on the target. The source remains and the target location is known. Mark partial completion when some items are unread, still downloading, or ambiguous under the same name. A success notice or icon does not replace these checks.

### Common errors and recovery

- **Several similar devices appear:** Check the name, receiver prompt, or matching code. Cancel a wrong choice; do not test by sending to an unfamiliar device.
- **The target count is short:** Compare against the source list, resend only missing items, and recheck. “Complete” in the app is not enough.
- **A target file appears but will not open:** Check whether transfer finished and whether the target has a suitable viewer. Keep the source and export or transfer a readable format.
- **The target asks to overwrite:** Cancel, open both the old target and new source, then keep two distinct versions or rename. Do not erase older work during a transfer.
- **An external drive is still writing:** Wait and eject safely. If disconnected, reconnect and inspect real readability at the destination rather than trusting a partial name list.

### Assumptions, alternatives, and known side effects

Systems differ in received folders, visibility, permissions, and completion messages; follow the actual devices and provider guidance. Lists, keyboard navigation, screen readers, or file search can verify results without thumbnails. A second current copy does not prove recovery if the source is deleted, both synced copies disappear, or both devices fail. Two devices with files also create two locations that may each look like “latest.”

### Sources

- [Microsoft: Move files to a new Windows PC with external storage](https://support.microsoft.com/en-us/windows/experience/backup-recovery/move-your-files-to-a-new-windows-pc-using-an-external-storage-device): Check the destination and eject after copying.
- [Microsoft: Safely remove hardware in Windows](https://support.microsoft.com/en-us/windows/hardware/safely-remove-hardware-in-windows): Eject external storage before disconnecting.
- [Google: Quick Share between Android and Windows](https://support.google.com/android/answer/13801258?hl=en): Receiver confirmation and received location depend on the tool.
- [Apple: Use AirDrop with nearby Apple devices](https://support.apple.com/en-mide/guide/iphone/iphcd8b9f0af/27/ios/27): Received items may land in Downloads or an appropriate app and must be located on the target.

If AI opens this file, it may help compare the two lists. You remain the Human Runtime and choose devices, transfer, open, and retain the right files.
