---
name: check-a-secondhand-item-condition
description: "Human-readable steps for checking whether a used, refurbished, or open-box item's actual condition matches the exact listing before deciding to buy it."
---
# 买二手商品前核对实际状态 / Check a Secondhand Item's Condition

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 每件 8–15 分钟 / 8–15 minutes per item |
| Requirements / 必要物品 | 准确商品的状态描述、实物或实拍图、必要配件清单 / Exact-item condition text, item or actual photos, essential-parts list |
| Side effects / 现实副作用 | “几乎全新”可能需要具体名词 / “Like new” may need actual nouns |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当一件普通商品标为“二手”“翻新”“开箱”或类似状态，而你要决定是否买**这一件**时加载。目标是把状态描述和当前实物对上，输出接受、拒绝或未确认。它不替你判断产品规格、价格、退换权利，也不认证电器或防护用品的安全。

### 准备与输入

写下准确型号/版本、预定普通用途，以及这次不能缺的部件或说明。保存卖家对状态、已知缺陷、维修/改装、附带物和可否查看实物的原话。线上需要**这件商品的实际照片**，不是品牌图库；现场在获得许可后检查可见外观与标识。若看不清，可要求多角度清晰照片、放大或请可信的人描述；不要求你搬动超出能力的重物。

### 执行

1. **把模糊状态词拆开。** “翻新”是谁做了什么、检查了什么、换了哪些部件？“开箱”是否使用过、是否缺少原附件？这些词本身没有统一到足以替你验收这一件的细节。
2. **核对确切身份。** 对照商品本体/包装的品牌、型号、版本和可见序号位置，确认描述和照片属于你将收到的那一件。序号可由卖家遮住敏感部分；只要足以区分版本即可，不索要对方个人资料。
3. **对照可见状况与清单。** 逐项核对卖家列出的磨损、破损、改动、缺件、必要配件和说明书。看不见的内部状况保持未知；外壳擦净不等于内部已经测试。缺少正常使用必需的部件时，另按规格/兼容性任务核对，或直接不买。
4. **检查安全边界。** 普通二手物也可能被召回；已有召回线索时用独立召回 Skill 核对准确型号和批次。卖家说不清改装、出现明显危险损坏，或商品属于婴儿汽车座椅、防护装备等安全关键类别时，停止本 Skill 的普通验收，不靠外观自行认证安全。
5. **给出窄结论。** 写“状态与证据相符、可继续考虑 / 明确不符 / 未确认”，列出你看到的实际图或实物、卖家描述、关键缺陷与未知。状态通过后仍需分别检查用途、价格和其他限制。

### 成功与停止

你能指出卖家承诺的是哪一件、它实际可见的状态和附带物，以及尚未证明的部分。只收到图库照片、关键缺陷含糊、身份对不上或无法查看必要信息时，保留“未确认”并暂停购买。付款后交涉和退货归售后任务，这份 Skill 在付款前结束。

### 常见报错与补救

- **“像新的一样”但没有细节：** 请卖家列出使用痕迹、修复内容、缺件和对应实拍；没有就不按新品预期购买。
- **不同照片里的序号或颜色不一致：** 先确认是否同一件；无法确认就停止。
- **现场无法安全试机或拆看：** 不强行通电、拆机或自行修理；把未检查部分写为未知，必要时转合格检测。
- **取货时发现与记录不同：** 在付款前重新判定，拒绝把新缺陷当成原先同意的状态。

### 假设、替代与副作用

这里处理普通二手家用品和衣物，不处理安全关键二手用品、账号锁定设备、个人数据清除或法律上的担保解释。地区和平台对“翻新”等词的用法不同，按这件的具体描述与证据判断。网络、视觉、行动或沟通受限时可改为现场同行核对、要求可访问照片与文字，或放弃信息不足的商品。“便宜”不会自动修复一个未说明的缺件。

### 来源

- [英国 OPSS：购买二手商品](https://www.gov.uk/guidance/consumer-products-buying-second-hand-goods) — 支持检查实际磨损、改装、说明与召回，且某些婴儿安全用品不可用外观做安全判断；具体建议限于该地区。
- [美国 FTC：在网上交易平台购物](https://consumer.ftc.gov/articles/buying-online-marketplace) — 实物照片与状态描述有别于图库和笼统的“翻新/二手”标签；不延伸其付款或退货法律建议。

## English

Load this Skill when an ordinary item is labelled “used,” “refurbished,” “open box,” or similar and you must decide whether to buy **this exact unit**. Match the condition description to the item and finish with accept for further consideration, reject, or unconfirmed. This does not settle specifications, price, return rights, or the safety of electrical or protective equipment.

### Preparation and inputs

Write down the exact model or version, ordinary intended use, and parts or instructions you cannot do without. Save the seller's wording about condition, known defects, repairs or modifications, included pieces, and inspection access. Online, request **photos of this unit**, not catalogue images; in person, inspect visible surfaces and identifiers with permission. Ask for clear views, magnification, or a trusted description if access is difficult. You need not lift more than you safely can.

### Execution

1. **Unpack vague condition words.** Who refurbished it, what did they inspect or replace? Was an “open box” item used, and which original accessories are present? Those words do not, by themselves, specify the condition of this unit.
2. **Match the exact identity.** Compare the item's or box's brand, model, revision, and visible serial-location information with the listing and photos. The seller can hide sensitive serial digits; you only need enough to distinguish the version. Do not request personal data.
3. **Compare visible condition and contents.** Check each stated scuff, crack, modification, missing part, essential accessory, and manual. Internal condition you cannot see remains unknown; a clean shell is not evidence of internal testing. For a part essential to your use, run the separate specification or compatibility check, or reject the item.
4. **Respect the safety boundary.** Used items can also be recalled; use the separate recall Skill when there is a relevant alert. Stop this ordinary inspection if modifications are unexplained, damage suggests danger, or the product is safety critical, such as an infant car seat or protective gear. Appearance cannot certify those items as safe.
5. **Make a narrow record.** Mark “condition matches the evidence, continue considering / clear mismatch / unconfirmed,” and note actual photos or observations, seller wording, key defects, and unknowns. Passing the condition check does not pass purpose, price, or other restrictions.

### Success and stop

You can identify the specific unit promised, its visible state and included parts, and what is still unproven. Stock photos only, vague critical defects, mismatched identity, or blocked inspection of necessary facts means unconfirmed: pause the purchase. After-payment disputes and returns belong elsewhere; this Skill ends before paying.

### Common errors and recovery

- **“Like new” without details:** Ask for wear, work performed, missing parts, and actual-unit photos. Without them, do not apply new-item expectations.
- **Photos disagree on serial area or colour:** Confirm whether they show the same unit; stop if you cannot.
- **You cannot safely test or open it:** Do not force power, dismantle, or repair it. Record uninspected parts as unknown and seek qualified inspection when necessary.
- **Pickup reveals a new discrepancy:** Decide again before payment. A newly visible defect was not part of your earlier acceptance.

### Assumptions, alternatives, and side effects

This covers ordinary used household goods and clothing, not safety-critical used products, account-locked devices, personal-data removal, or legal warranty interpretation. “Refurbished” can mean different things by seller and region; use this item's concrete wording and evidence. If internet, vision, mobility, or communication is a barrier, inspect with a trusted companion, request accessible photos and text, or skip an under-documented item. A low price does not replace a missing accessory.

### Sources

- [UK OPSS: Consumer Products, Buying Second-Hand Goods](https://www.gov.uk/guidance/consumer-products-buying-second-hand-goods) — inspect wear, modifications, instructions, and recalls; some infant safety items cannot be cleared by appearance. Its detailed advice is region-specific.
- [US FTC: Buying From an Online Marketplace](https://consumer.ftc.gov/articles/buying-online-marketplace) — actual-unit photos and specific condition details matter more than stock images and vague “refurbished/used” labels; payment and return-law advice is outside this Skill.
