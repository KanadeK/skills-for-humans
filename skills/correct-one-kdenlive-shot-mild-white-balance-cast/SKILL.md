---
name: correct-one-kdenlive-shot-mild-white-balance-cast
description: "Human-readable restrained clip-level Kdenlive White Balance correction using a credible neutral point and comparing adjacent shots."
---
# 在 Kdenlive 轻调一段镜头的白平衡偏色 / Correct One Kdenlive Shot Mild White-Balance Cast

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 / 10–20 minutes |
| Requirements / 必要物品 | 自有镜头有轻微冷暖偏色、可信中性物和保存工程 / Owned shot with mild cast, credible neutral object and saved project |
| Side effects / 现实副作用 | 该镜头偏色减轻且邻镜不被改 / Cast on one shot lessens while neighbours stay |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一段自有视频比前后镜头明显偏冷或偏暖，画面内有可确信接近白/灰的物体，想只校这一段时使用本篇。成果是中性物不再明显偏色、人物或环境重要颜色仍可信，前后镜头没有被一起改。若现场本来是彩灯氛围，不能强行调成白天。

### 准备与输入

保存工程，找中性参考与一处已知颜色，在镜头首中尾核光线是否稳定。只选时间线这一镜头，若照明随时间变，单个固定设置可能不够。不要用于商品真实颜色证明、医学或证据影像。

### 执行

1. 给这一片段加 White Balance，使用 Neutral Color 采样可信中性处。
2. 小幅调整并在首中尾预览，核中性物和已知颜色不偏到相反方向。
3. 比较前后镜头与原效果关闭状态，判断连接更自然且没有不真实肤色/物色。
4. 无可靠中性点就撤销并标不确定，满意时保存重开。

### 完成、常见问题与恢复

一段轻微偏色得到谨慎改善，邻镜与必要颜色不误改，来源限制明说。

- **颜色反向偏：** 撤回取样或减弱 Green Tint。
- **三处光不同：** 承认固定设置不足。
- **邻镜也变：** 核效果是否加在轨道/源素材。

### 假设与边界

只做普通镜头视觉校色，不认证真实颜色、产品或证据。你负责中性参考是否可信。

### 来源

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/video_effects/color_image_correction/white_balance.html)（英文，官方手册）— White Balance 的 Neutral Color 取样调白平衡，Green Tint 可单独改。
- Original synthesis — 将一个视频编辑结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one owned shot looks cooler or warmer than neighbouring shots and has a credible near-white/gray object. Finish with less cast on that reference, other important colors plausible, and neighbouring shots unchanged. Intentional colored lighting should not be forced into daylight white.

### Preparation and inputs

Save project, identify neutral and one known color, and check light at beginning/middle/end. Select this timeline shot only. Changing illumination may need more than a fixed setting. Exclude product-color proof, medical and evidence imagery.

### Execution

1. Add White Balance to this clip and sample credible neutral area.
2. Preview first/middle/end for neutral and known color without reversing cast.
3. Compare adjacent shots and bypassed effect for smoother continuity without implausible colors.
4. Undo and mark uncertainty without reliable neutral; otherwise save/reopen.

### Success, common problems, and recovery

One mild cast improves cautiously, neighbours and key colors stay, and source limits are explicit.

- **Opposite cast:** Resample or reduce tint.
- **Lighting varies:** Acknowledge one setting insufficient.
- **Other shots change:** Check clip versus track/bin target.

### Assumptions and limits

This is ordinary clip color correction, not proof of true product/evidence color. You judge neutral reference.

### Sources

- [Kdenlive 26.08 Manual](https://docs.kdenlive.org/en/effects_and_filters/video_effects/color_image_correction/white_balance.html) — White Balance Neutral Color samples reference and Green Tint is separate.
- Original synthesis — one video-editing outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Kdenlive controls. You choose the content, perform the steps and verify the result.

