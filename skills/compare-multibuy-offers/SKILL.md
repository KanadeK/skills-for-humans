---
name: compare-multibuy-offers
description: "Human-readable steps for comparing conditional multi-buy prices for a fixed number of identical ordinary items before paying."
---
# 固定件数下比较多买优惠 / Compare Multi-Buy Offers for a Fixed Quantity

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 每组 3–7 分钟 / 3–7 minutes per comparison |
| Requirements / 必要物品 | 已决定的件数、同款商品、单件价、优惠条件和当前购物篮 / A fixed item count, matching products, single-item price, offer terms, and current basket |
| Side effects / 现实副作用 | “第二件半价”会变成一个可核对的总数 / “Half off the second” becomes a checkable total |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你**已经决定要买几件同款、同规格的普通商品**，却看到“两件价”“买二送一”“第二件折扣”或会员多买价时，加载这份 Skill。它只回答：**为这固定件数，哪种当前可用买法实际付得更少？** 不替你增加需求；若优惠必须多拿不需要的东西，先回到购买量判断。

### 准备与输入

写下这次确定需要的件数、确切商品及每件净量。记录单件现价和每个候选优惠的原文，包括适用商品、开始/截止时间、会员资格、每单上限、是否能重复或叠加、优惠商品是否须同款。只使用你这次确实具备的资格；临时办会员产生的费用或未来优惠不算“已经省下”。看不清小字时放大、查看商家可读页面或请店员读出完整条件。

### 执行步骤

1. **锁定件数与内容。** 例如你要四瓶同一规格的洗手液，就让每个方案都交付四瓶。不能把“额外送一瓶”同时算成已需要的四瓶和一笔免费收益。若包装净量不同，先用[同单位价格比较](../compare-unit-prices/SKILL.md)核对数量口径；不同用途的赠品不参与本次同件数比较。
2. **筛掉不适用的价格。** 逐条核对你购物车里的款式、件数、时间、会员状态和使用次数上限。条件不明时，不把广告最大折扣当作你的价格；先查清或用可确认的单件价。
3. **列出能凑齐固定件数的买法。** 对每个优惠写“优惠组数 × 每组价 + 剩余单件数 × 单件价”。只有商家明确允许重复时，才把同一个多买价用两次。优惠不能叠加时分别计算，不把两张标签自动相乘。
4. **算整单实际应付。** 假设每瓶单价 4，同款两瓶价 7，目标是四瓶：若优惠可重复两次，总价为 14；若每单限用一次，总价为 7 + 4 + 4 = 15；四瓶原价为 16。三个数字的商品数量都是四瓶，才可以排名。若这次商品之间还有不同的强制费用，先把可确认的费用纳入同一口径。
5. **在付款前核实。** 线上可查看实际购物篮或结算预览；现场可请店员核实适用条件。若最终金额与计算不符，暂停把优惠视为成立，按可确认的价格重新比较。价格争议和售后交涉不由本 Skill 完成。

### 完成与停止

你能说出固定件数下每种可用买法的**应付总额、优惠资格和限制**，并选出当前较低的一种，就完成了。没有办法取得同样件数，或优惠条件/结算价无法确认时，输出“暂不可比”；不要为使优惠生效而偷偷改动需求。

### 常见报错与补救

- **“买二送一”，实际只要两件：** 这不是同数量的候选。按两件可确认的价格决定；是否愿意买第三件另交购买量判断。
- **优惠限用一次却算了两次：** 用一组优惠加剩余单件价重算；若商家实际允许重复，以结算信息为准。
- **会员价并不属于你：** 用非会员现价比较。办卡费用和以后可能的购买都不是这次已发生的节省。
- **第二件折扣指指定商品或较低价商品：** 按原文确定折扣落在哪件；无法确认就先不用该优惠数字。
- **标签与结算冲突：** 保存商品、优惠条件和结算信息，请店员核对；不能确认前不宣称“省了”。

### 假设、替代与副作用

这份流程假设你已确定数量和商品能满足用途。不同商家的会员、叠加、限购和付款规则不同；只认你当前可验证的条件，不推断未来价格。若无法站立排队、读取小字或操作线上购物篮，可以在可访问的商品页查看、放大照片、用纸笔或计算器列式、请店员口述当前可用价格；仍缺关键条件就停止。可能的现实副作用是你少拿一件只为触发折扣的商品。

### 来源

- [英国竞争与市场管理局：单位价短指南](https://competitionandmarkets.blog.gov.uk/2024/01/30/a-short-guide-to-unit-pricing/) — 促销品与多件装未必比单买便宜，应核对当前单位价格。
- [澳大利亚竞争与消费者委员会：商品单位价格](https://www.accc.gov.au/consumers/pricing/unit-prices-for-groceries) — 同类商品多件同价时，单位价可帮助比较；本 Skill 不把澳大利亚的标价义务当作全球规则。
- 固定件数列式、优惠资格核对和停止条件为 Original synthesis。

## English

Load this Skill when you have **already chosen a fixed number of identical ordinary items** but see “two for,” “buy two, get one,” a discounted second item, or a member-only multi-buy offer. It answers one question: **which currently available way costs less for that same count?** It does not create a need for more. If a deal forces extra goods into your basket, decide whether you need them separately.

### Preparation and inputs

Write down the exact count, item, and net amount in each pack. Record the current single-item price and the full terms of each offer: eligible variants, start and end times, membership, per-order limits, repetition, stacking, and whether all items must match. Use only qualifications you actually have now. A joining fee or possible future savings are not savings already realised. Enlarge small print, use a readable seller listing, or ask staff to read the complete terms if needed.

### Execution steps

1. **Lock the count and contents.** If you need four bottles of the same hand wash, make every option deliver four such bottles. Do not count an unwanted bonus bottle both as part of the four you need and as a free gain. If pack sizes differ, first check the quantity basis with [Compare Unit Prices](../compare-unit-prices/SKILL.md). An unrelated gift is not part of this fixed-count comparison.
2. **Exclude inapplicable prices.** Check the variant, count, time, membership, and use limit against your actual basket. An unknown condition does not make an advertised maximum discount your price; confirm it or use a single-item price you can verify.
3. **List ways to reach the fixed count.** For each offer, write “number of offer groups × group price + remaining singles × single price.” Repeat an offer only when its terms permit it. If offers cannot be stacked, calculate them separately rather than multiplying two sale stickers together.
4. **Calculate what you would pay.** Suppose each bottle is 4, two matching bottles cost 7, and you need four. If the offer may be used twice, the total is 14. If it is limited to one use per order, the total is 7 + 4 + 4 = 15. Four singles cost 16. Every total covers four bottles, so the ranking is meaningful. Include any confirmed unavoidable charge that differs between the options.
5. **Confirm before paying.** Online, inspect the actual basket or checkout preview. In a shop, ask staff to confirm the offer conditions if needed. If the final amount differs, stop treating the deal as established and recalculate from a price you can confirm. This Skill does not resolve a seller dispute or an after-sale claim.

### Success and stop

You can state the **total payable amount, eligibility, and limits** for each available way to obtain the fixed count, and choose the lower current total. If the options cannot deliver the same count or the terms or checkout price remain unknown, output “not comparable yet.” Do not silently change how much you need merely to unlock an offer.

### Common errors and recovery

- **“Buy two, get one” when you need only two:** This does not deliver the same quantity. Use a confirmed two-item price; decide on a third item as a separate quantity task.
- **You used a one-time offer twice:** Recalculate with one offer group and the remaining singles, unless the seller confirms it may repeat.
- **You do not have the required membership:** Compare the non-member price. Joining fees and hypothetical later purchases are not realised savings today.
- **The second-item discount applies only to selected or lower-priced items:** Identify which item actually receives the discount. Do not use that number until the terms are clear.
- **Shelf and checkout disagree:** Keep the item, offer wording, and checkout information for a staff check; do not claim a saving while the amount is unresolved.

### Assumptions, alternatives, and side effects

This assumes you have already chosen the quantity and verified that the product suits its purpose. Membership, stacking, limits, and payment rules vary by seller. Use only current, verifiable terms and do not predict later prices. If standing in line, reading small print, or navigating a basket is difficult, use accessible seller information, an enlarged photo, paper or a calculator, or a staff reading of the applicable price. Stop if a decisive term stays unknown. A possible side effect is leaving behind an extra item whose only job was to activate a sticker.

### Sources

- [UK Competition and Markets Authority: short guide to unit pricing](https://competitionandmarkets.blog.gov.uk/2024/01/30/a-short-guide-to-unit-pricing/) — promotional products and multipacks are not necessarily cheaper than individual items; check the current unit price.
- [Australian Competition and Consumer Commission: unit prices for groceries](https://www.accc.gov.au/consumers/pricing/unit-prices-for-groceries) — a unit price helps compare similar multi-item offers; Australian display rules are not treated as worldwide rules here.
- The fixed-count arithmetic, eligibility check, and stop conditions are Original synthesis.
