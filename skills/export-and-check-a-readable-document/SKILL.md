---
name: export-and-check-a-readable-document
description: "Human-readable steps to export an ordinary editable document to a requested format and reopen the exported copy to check that its contents remain readable."
---
# 导出文档并检查副本能否读 / Export and Check a Readable Document

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 本人有权处理的普通源文档、原应用、接收方格式要求、查看导出文件的工具 / An ordinary source document you may handle, its app, recipient format requirement, viewer for the export |
| Side effects / 现实副作用 | 同一内容会有可编辑原件和一份待交付副本 / One document now has an editable original and a delivery copy |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你有一份普通可编辑文档，需要给别人一份 PDF、DOCX 或其他可用格式时，加载这份 Skill。目标是**从原应用真正导出副本，再把副本作为独立文件打开核对**。文件名变成 `.pdf` 并不等于内容变成 PDF；“我这里能打开”也不保证对方设备和权限都没问题。

只处理你有权导出的低敏感普通文件。正式申报、合同、财务/医疗记录和要求特定无障碍或长期归档标准的文件按接收方规定处理。发送给谁、哪一版和共享权限的检查属于下一步，不在本 Skill 里替你完成。

### 准备与输入

先问清接收方需要什么：只读查看、继续编辑、打印，还是某个明确的格式与应用？不清楚时问格式或可用查看方式，不默认 PDF 总是最好。打开源文档，确认它是当前版本，记下页数、标题、重要表格/图片和特殊字符，以便比较导出结果。

### 执行

1. **保留可编辑原件。** 确认原文档已保存，选择应用中的“导出”“另存为”或“下载副本”功能；不要在文件管理器里直接改扩展名。给导出副本一个能辨认用途和版本的名称，选择与原件可区分的存放位置或文件名，不接受覆盖原件的提示。
2. **选择真正受支持的格式。** 按接收方要求和当前应用提供的选项导出。若对方只需阅读，PDF 可以是一个选择；若要在某个应用继续编辑，选择其能处理的可编辑格式。应用没有要求的格式时先停下询问替代，而不是造一个同名后缀。
3. **离开编辑界面后打开导出文件。** 从实际保存位置找到副本，使用与编辑器预览不同的查看方式打开。若根本找不到，检查应用是否仍在导出、默认下载目录和保存提示；不要用源文档画面冒充导出成功。
4. **逐项核对可读性。** 比对页数和顺序、标题、正文、表格/图片、页边、特殊字符及需要辨认的小字；放大查看，并按实际阅读方式试滚动、搜索或朗读。重要信息丢失、乱码、截断或顺序错了，就回源文件调整后重新导出，再打开新副本检查。
5. **确认是要交付的那一版。** 打开文件名和位置，记下已检查的导出副本。多个导出结果并存时，明确哪份通过检查，其他份不替它承担“最终版”职责。若需要收件人设备上的实际验证，标为“待对方确认”；在对方打开之前不声称已验收。

### 完成条件

源文档仍可编辑；独立导出的副本存在、能在查看工具里打开，其关键内容与源文档一致，且格式满足已知接收要求。若接收方应用、权限或无障碍要求仍未知，明确记为待确认。发送和对方实际打开是后续步骤，不由文件扩展名或本地预览自动证明。

### 常见报错与补救

- **改了后缀但打不开：** 恢复原文件名，在创建该文档的应用里执行真正的导出。改名不转换文件结构。
- **导出的版面乱了：** 找到错页、字体、表格或图像位置，回源文件修正或换对方支持的格式；重导后重新检查，而不是只改副本文件名。
- **文字看得到却无法方便阅读：** 试放大、搜索或辅助阅读方式，找出问题；若需要特定可及性标准，按该要求补做结构和测试，不把 PDF 标签当合格证。
- **源文档被覆盖：** 停止继续保存到同名位置，先检查应用版本历史或已有副本；恢复原件是否可行取决于实际应用，不保证自动复原。
- **对方没有对应软件：** 先询问其可打开的格式或提供可用替代，再导出和检查；不要要求对方为了普通文件安装陌生程序。

### 假设、替代与现实副作用

不同编辑器、字体、设备和格式支持不同，转换可能改变版面或可编辑性。用实际接收要求选格式，以重新打开的副本和必要时对方反馈判定结果。你会多一份文件，需要避免把旧导出件误发；副本不会因为文件名写了“最终”就自动更新。

### 来源

- [Microsoft：在 Mac 版 Word 中保存或转换为 PDF](https://support.microsoft.com/en-us/word/save-or-convert-to-pdf-on-your-mac)：说明真正的 PDF 导出及保留单独可编辑原件。
- [Google Docs：创建、查看或下载文件](https://support.google.com/docs/answer/49114?hl=en_na&ref_topic=9045929)：可在下载时选择文件类型。
- [Microsoft：Windows 常见文件扩展名](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/common-file-name-extensions-in-windows)：更改扩展名不会转换文件内容。

## English

Load this Skill when you have an ordinary editable document and need to give someone a PDF, DOCX, or another available format. **Actually export a copy from the source app, then open that copy as a separate file and inspect it.** A filename ending in `.pdf` does not turn contents into a PDF. Opening it on your device also does not prove the recipient has the right app or permissions.

Handle only an ordinary low-sensitivity file you may export. Formal submissions, contracts, financial or medical records, and files with specific accessibility or long-term archive standards follow the recipient's actual rules. Checking who receives which version and what sharing rights apply is a later step; this Skill does not send it for you.

### Preparation and inputs

Find out whether the recipient needs read-only viewing, continued editing, printing, or a particular format and app. Ask when unclear; PDF is not automatically the best choice. Open the source document and confirm it is the current version. Note its page count, headings, key tables or images, and unusual characters so you can compare the export.

### Execution

1. **Keep the editable original.** Make sure the source is saved. Use its app's Export, Save As, or Download a copy function; do not merely change the extension in a file manager. Give the output a name that identifies purpose and version and a location or name distinct from the original. Reject a prompt to overwrite the source.
2. **Choose a format the app actually supports.** Export according to the recipient's request and the app's available choices. A PDF may suit reading; someone who must keep editing needs a compatible editable format. If the app cannot create the requested format, pause and ask about an alternative instead of inventing a suffix.
3. **Open the exported file outside the editor view.** Find it at the saved location and open it with a viewer other than the editing preview. If you cannot find it, check whether exporting is still in progress, the default download location, and the save message. The source document on screen is not export proof.
4. **Check readability item by item.** Compare page count and order, headings, body, tables and images, margins, unusual characters, and small type. Zoom, scroll, search, or use reading assistance as appropriate. If key material is missing, garbled, clipped, or out of order, fix the source or export settings, create a new copy, and reopen that new copy.
5. **Identify the checked delivery version.** Record the output name and location. If several exports exist, state which one passed your check; older outputs do not silently inherit “final” status. If actual testing on the recipient's device is needed, mark it pending. Do not claim recipient acceptance before they open it.

### Success

The editable source remains available. A separately exported copy exists and opens in a viewer, its key contents match the source, and its format meets the known recipient requirement. Unknown recipient app, permission, or accessibility requirements are explicitly pending. Sending and the recipient's actual opening are later actions, not proved by an extension or your local preview.

### Common errors and recovery

- **A changed suffix will not open:** Restore the original name and perform a real export from the creating app. Renaming does not convert the file structure.
- **The layout shifts:** Identify the damaged page, font, table, or image. Repair the source or choose another format the recipient supports, then export and inspect again instead of renaming the output.
- **The text is visible but hard to read:** Try zooming, searching, or an assistive reading route to find the problem. If a specific accessibility standard is required, add the needed structure and testing under that requirement; a PDF label is not a certificate.
- **The source was overwritten:** Stop saving to the same name and inspect app version history or existing copies. Whether the original can be restored depends on the actual app; do not promise automatic recovery.
- **The recipient lacks the app:** Ask what format they can open or offer a suitable alternative, then export and check it. Do not require someone to install unfamiliar software for an ordinary file.

### Assumptions, alternatives, and known side effects

Editors, fonts, devices, and formats support different features, so conversion can alter layout or editability. Choose from the real recipient requirement and judge the reopened output, plus recipient feedback when needed. You will have one more file and could send an old export by mistake; “final” in its filename does not keep it updated.

### Sources

- [Microsoft: Save or convert to PDF in Word for Mac](https://support.microsoft.com/en-us/word/save-or-convert-to-pdf-on-your-mac): Describes a real PDF export and a separate editable original.
- [Google Docs: Create, view, or download a file](https://support.google.com/docs/answer/49114?hl=en_na&ref_topic=9045929): Download offers a file type choice.
- [Microsoft: Common file name extensions in Windows](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/common-file-name-extensions-in-windows): Changing an extension does not convert contents.

If AI opens this file, it may help create a comparison checklist. You remain the Human Runtime and export, open, compare, and choose the delivery copy.
