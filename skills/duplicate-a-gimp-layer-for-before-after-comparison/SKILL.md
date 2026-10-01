---
name: duplicate-a-gimp-layer-for-before-after-comparison
description: "Human-readable duplicate-layer setup for one owned photo so edits can be compared by visibility while an untouched base remains."
---
# 复制 GIMP 图层做可切换的前后对照 / Duplicate a GIMP Layer for Before-After Comparison

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–15 分钟 / 5–15 minutes |
| Requirements / 必要物品 | 已保存 XCF、当前原始图层、将要做的一项调整 / Saved XCF, current original layer and one planned adjustment |
| Side effects / 现实副作用 | 有底层原貌和可切换修改层 / Untouched base and switchable edited layer exist |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你要在 GIMP 做一次色调或局部调整，又想随时看原样对照时使用本篇。成果是未改的底层和命名清楚的工作副本层，显示开关可比较两者，后续不会误在底层画。它只建立对照结构，不声称编辑后的版本已经更好。

### 准备与输入

打开已保存的 XCF，确认选中的是真正要复制的图像层，不是蒙版、文字层或空白层。记录底层名称和当前图层数，给工作副本拟一个说明用途的名字。检查原图文件也独立保留；图层复制不是外部备份。

### 执行

1. 选择目标图像层，使用 Layer > Duplicate Layers，确认多出一层。
2. 把新层改为说明编辑用途的名字，并选中它作为后续操作目标。
3. 切换新层可见性，核底层显示原貌；再打开新层，核当前画面与复制前一致。
4. 保存 XCF，若误复制别层或底层已被修改，撤销并从保存点重做。

### 完成、常见问题与恢复

底层原样、工作层独立且可切换，当前活动层正确；实际编辑仍待后续 Skill。

- **两个层看不出差别：** 刚复制时本应相同，后续改动再比较。
- **改到原层：** 撤销并选工作层。
- **复制了文字层：** 删除误副本后选图像层。

### 假设与边界

图层可见性只作本地对照，不证明色彩或真实性；你负责确保底层未改。XCF 文件仍需常规备份。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-layer-duplicate.html)（英文，官方手册）— Layer > Duplicate Layers 创建所选图层副本。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill before one GIMP tonal or local edit when you need a quick comparison to the original. Finish with an untouched base layer and a clearly named working copy whose visibility can switch before/after. Future edits should not accidentally paint the base. This sets up comparison without claiming the edited version is better.

### Preparation and inputs

Open saved XCF and ensure selected item is the intended image layer, not a mask, text or empty layer. Note base name and layer count, and plan a purpose-based name for the duplicate. Keep original file separately; a duplicate layer is not external backup.

### Execution

1. Select target image layer and use Layer > Duplicate Layers, confirming one added layer.
2. Rename new layer for intended edit and make it the active target.
3. Toggle new layer visibility to reveal base original, then restore visibility and compare identical starting state.
4. Save XCF. Undo and restart from saved state for wrong layer or modified base.

### Success, common problems, and recovery

Base remains unchanged, work layer is independent and switchable, and active layer is right; the actual edit remains later work.

- **Layers look identical:** They should initially; compare after an edit.
- **Base edited:** Undo and select work copy.
- **Text layer copied:** Remove wrong copy and select image layer.

### Assumptions and limits

Layer visibility is a local comparison tool, not proof of color or truth. You verify base remains untouched. XCF still needs ordinary backup.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-layer-duplicate.html) — Layer > Duplicate Layers copies selected layers.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.

