---
name: straighten-a-tilted-photo-horizon-in-gimp
description: "Human-readable GIMP Measure/Straighten pass for one ordinary tilted horizon with edge-crop tradeoff and before/after check."
---
# 在 GIMP 扶正一张轻微倾斜的地平线 / Straighten a Tilted Photo Horizon in GIMP

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 自有普通风景 XCF 副本、真实可作水平参考的线 / Owned ordinary landscape XCF copy and a genuine horizontal reference |
| Side effects / 现实副作用 | 地平线更平，边缘损失已核 / Horizon becomes level with edge loss reviewed |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你拍的一张普通风景略斜，有可信的真实水平线可参照，想把观看时的歪斜纠正时使用本篇。成果是参考线在输出中更水平、旋转造成的空角或裁边得到检查，主体不被误切。若地形本来倾斜或无可信参考，不能硬把山坡拉平。

### 准备与输入

保存 XCF 副本并保留原图，选海平面、建筑水平边或其他可靠基准，不拿道路坡度当水平。记下旋转前画面边缘附近的重要物件，预想扶正后可能要牺牲部分边角。先确认活动图层/图像范围，避免只转了某一层造成拼接错位。

### 执行

1. 用 Measure 沿可信水平线拖一条测量线，观察读角与方向。
2. 选择 Straighten 并预览旋转，核参考线变水平且主体没有被大幅裁出。
3. 检查空角与边界；只做必要的小幅裁切，保留画面用途所需环境。
4. 与原层/原图切换比较，若结果更歪或损失过多，撤销并重选基准；保存后核导出副本。

### 完成、常见问题与恢复

可信参考线较水平，主体与重要边缘仍在，副本可回退。

- **越扶越歪：** 撤销并核参考线与旋转方向。
- **空白三角明显：** 裁少量边或保留原画面。
- **只转一层：** 核变换目标并从 XCF 恢复。

### 假设与边界

只纠正轻微相机倾斜，不修建筑透视或地形。你负责选择真实水平基准；软件读角不能证明景物本身平。

### 来源

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-tool-measure.html)（英文，官方手册）— Measure 工具沿水平线测角并可用 Straighten 旋转。
- Original synthesis — 将一个图像编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill for an ordinary owned landscape that is slightly tilted and has a trustworthy horizontal reference. Finish with that line more level, rotation corners/cropping inspected and subject not cut. If terrain itself slopes or no credible reference exists, do not force a hillside flat.

### Preparation and inputs

Save XCF copy and original. Choose sea horizon, verified level building edge or another reliable reference, not a sloped road. Note important objects near edges that rotation may sacrifice. Check active layer/image target so only one layer is not rotated out of alignment.

### Execution

1. Use Measure along reliable horizontal line, inspecting angle and direction.
2. Use Straighten and preview rotation, checking the line levels and subject remains.
3. Inspect empty corners and crop minimally while keeping necessary context.
4. Compare with original, undo for worse tilt or excessive loss, then save and inspect exported copy.

### Success, common problems, and recovery

Trusted reference is more level, subject and important edges remain, and the edit is reversible from copy.

- **More tilted:** Undo and review reference/direction.
- **Empty corners:** Crop minimally or keep original.
- **Only one layer rotates:** Check transform target and restore from XCF.

### Assumptions and limits

This fixes mild camera tilt, not building perspective or terrain. You choose a true level reference; the measured angle cannot prove the scene itself is flat.

### Sources

- [LibreOffice GIMP 3.2 User Manual](https://docs.gimp.org/3.2/en/gimp-tool-measure.html) — Measure can read a horizon angle and use Straighten to rotate.
- Original synthesis — one image-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain GIMP controls. You choose the content, perform the steps and verify the result.
