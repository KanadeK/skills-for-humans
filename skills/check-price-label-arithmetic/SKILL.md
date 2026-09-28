---
name: check-price-label-arithmetic
description: "Human-readable steps for checking whether a displayed unit price or percentage discount matches the prices and quantity shown for one ordinary item."
---
# 核对价格牌上的单价和折扣算式 / Check Price Label Arithmetic

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 每张价格牌 3–6 分钟 / 3–6 minutes per label |
| Requirements / 必要物品 | 对应商品、当前总价、净含量或划线参考价、价格牌的完整条件 / Exact item, current price, net quantity or stated reference price, and full label conditions |
| Side effects / 现实副作用 | 价格牌可能从“答案”降级为“待核对输入” / A price label may be demoted from answer to input |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你准备使用一张普通商品价格牌上的“每 100 克多少钱”“每件多少钱”或“立减 25%”，但数字似乎对不上时，加载这份 Skill。它给出**算术一致 / 明显不一致 / 信息不足**三种结果，让你知道这个数字能否进入后续价格比较。这里不判断商家是否违法，也不证明划线“原价”曾经真实成交。

### 准备与输入

先找准价格牌对应的确切商品、规格和包装净量；邻近货架牌可能属于另一种尺寸或口味。记录你当前真正适用的总售价、牌上标的单位价及其单位；若核对百分比，再记录同一商品与同一数量的划线参考价和现价。会员、时间、件数限制要一起读。缺少原价、净量或优惠资格时，先标记未知，不凭一个大号百分号补数字。

### 执行步骤

1. **核对牌与货。** 比对品名、型号/规格、净含量和适用日期；无法对应就不要拿这张牌计算。看不清可放大清晰照片、查商家当前可读页面，或请店员读回确切数字。
2. **检查单位价算式。** 把净量换到牌上的单位，用“当前适用总价 ÷ 净量 × 牌上单位量”重算。例：250 毫升现价 1.20，牌上是每 100 毫升，则应为 1.20 ÷ 250 × 100 = 0.48；若显示 4.80，不能把它当正确单位价。若牌用每千克、包装用克，先完成克与千克换算，不混用重量和体积。
3. **检查百分比算式。** 只有同一商品、同一包装量的参考价与现价都可见且参考价大于零时，算“(参考价 − 现价) ÷ 参考价 × 100%”。例如标“原价 10、现价 8”，算术折扣是 20%，不是 25%。这一步只核验牌上两数之间的算术，不证实原价过去真卖过，也不预测以后会卖多少。
4. **按显示精度判定。** 小数价格可能被四舍五入；很小的末位差异先标为“可能是舍入，需核实”，不要当成欺骗证据。差一个数量级、商品/单位对不上、或百分比明显不符，标记“明显不一致”；关键数字没有就标“信息不足”。
5. **决定是否使用这个数字。** 算术一致时，还要确认优惠确实适用于你，才把价格放进后续比较。不一致时用可核实的总价和净量自行重算，或在付款前请店员核对；仍有冲突就不基于这张牌作决定。商家交涉、投诉和售后另行处理。

### 完成与停止

你留下“确切商品、牌上条件、重算式、三态结论”即可结束。算术一致只代表这些**显示出来的数字互相对得上**；无法证明历史参考价、公平性、商品适用性或付款时一定能得到优惠。对不上时停用该牌的单位价/折扣数字，而不是替它猜一个更合理的价格。

### 常见报错与补救

- **误拿隔壁规格的牌：** 重新核对净量和品名；对不上就问清或换一件信息完整的商品。
- **会员价参与了算式，但你没有资格：** 按你能实际支付的价格重算；该会员标签不证明你能省钱。
- **“立减 25%”没有参考价：** 不能核验百分比来源；只记录当前可确认的应付价。
- **单位价略差一分：** 先考虑显示精度和舍入，再请店员确认；不要从末位差异推断意图。
- **价格牌与结算页不同：** 保存商品和两处数字以便核对，未确认前不要宣布最终价；购买后的争议转正式售后流程。

### 假设、替代与副作用

价格和显示精度随地区、商家、货币与优惠而变；这里只算你眼前这件普通商品，不给任何地区的消费者权利结论。手机放大、屏幕阅读、纸笔、计算器、可信同行者或店员读出可替代小字和心算；看不到完整条件时输出“信息不足”。副作用是你可能多看一分钟小字，但减少把错误算式带到收银台的机会。

### 来源

- [英国竞争与市场管理局：食品杂货单位价审查](https://assets.publishing.service.gov.uk/media/64b80ab1ef5371000d7aeefa/CMA_Review_of_unit_pricing_in_the_groceries_sector.pdf) — 记录实际出现的缺失及错误单位价，包括 250 毫升商品被错标为每 100 毫升高得多的价格；这里不移植英国法律义务。
- [英国竞争与市场管理局：价格减让宣传](https://competitionandmarkets.blog.gov.uk/2023/03/31/urgency-and-price-reduction-claims-are-your-online-tactics-legal/) — “原价/现价”与百分比减让引用参考价；显示的算术不足以证明参考价一直是真实常价。
- 三态判断、舍入核对和停止路径为 Original synthesis。

## English

Load this Skill when you are about to use an ordinary product label's “per 100 g,” “per item,” or “25% off” figure, but the numbers seem inconsistent. It gives one of three results: **arithmetically consistent, clearly inconsistent, or insufficient information**. That tells you whether the figure can enter a later price comparison. It does not decide whether a seller broke a law or prove that a crossed-out “was” price was ever genuinely charged.

### Preparation and inputs

Match the label to the exact product, variant, and net pack quantity; the adjacent shelf tag may belong to another size or flavour. Record the current total price actually available to you, the displayed unit price and its unit. To check a percentage, record the stated reference price and current price for the same item and amount. Read membership, time, and quantity limits too. If the reference price, net quantity, or eligibility is missing, mark it unknown instead of filling the gap with a large printed percentage.

### Execution steps

1. **Match label and item.** Check the name, model or variant, net contents, and applicable date. Do not calculate from a tag you cannot match. Enlarge a clear photo, use a readable current seller page, or ask staff to read back the exact figures if needed.
2. **Recalculate the unit price.** Convert net contents to the label's unit and use “current applicable total ÷ net quantity × displayed unit quantity.” If 250 ml costs 1.20 and the label uses per 100 ml, the result is 1.20 ÷ 250 × 100 = 0.48. A displayed 4.80 is not the matching unit price. Convert grams to kilograms first when required; do not substitute volume for weight.
3. **Recalculate a percentage.** Only if a stated reference price and current price describe the same item and pack and the reference is above zero, use “(reference − current) ÷ reference × 100%.” A label saying “was 10, now 8” describes a 20% arithmetic reduction, not 25%. This tests only the two displayed numbers. It cannot establish that the earlier price was genuinely charged or predict a later one.
4. **Respect display precision.** Price displays may round. Mark a tiny last-digit difference “possibly rounding; confirm” instead of treating it as proof of deception. Mark an order-of-magnitude error, mismatched item or unit, or clearly wrong percentage “inconsistent.” Mark absent decisive numbers “insufficient information.”
5. **Decide whether to use the figure.** Even when the arithmetic matches, check that you qualify for the offer before using the price in another comparison. For an inconsistency, recalculate from a confirmed total price and net quantity or ask staff before paying. If the conflict remains, do not decide from this label. Negotiations, complaints, and after-sale work are separate.

### Success and stop

Keep the exact item, label conditions, your calculation, and one of the three outcomes. Arithmetic consistency means only that the **displayed numbers fit each other**. It does not prove a historical reference price, fairness, product suitability, or the amount you will finally be charged. Stop using the suspect unit-price or discount figure when it does not match; do not invent a more plausible price on its behalf.

### Common errors and recovery

- **Using the next variant's tag:** Recheck name and net amount. Ask for clarification or choose an item with complete information if it does not match.
- **The arithmetic uses a member price you cannot access:** Recalculate using the price you can actually pay. A member label is not your saving.
- **“25% off” has no reference price:** Its percentage basis cannot be checked; record only the current payable price you can confirm.
- **A unit price differs by the last cent:** Consider display precision and rounding, then ask staff if it matters. A tiny difference does not establish intent.
- **Shelf and checkout prices disagree:** Keep both figures and the product detail for a check. Do not announce a final price while unresolved; route a post-purchase dispute through the seller's formal process.

### Assumptions, alternatives, and side effects

Prices and display precision vary with region, seller, currency, and offer. This is arithmetic for the ordinary item in front of you, not a consumer-rights ruling. Magnification, screen reading, paper, a calculator, a trusted companion, or a staff reading can replace small print and mental arithmetic. Output “insufficient information” if you still cannot see the full conditions. You may spend one more minute on the small print and avoid carrying an erroneous calculation to checkout.

### Sources

- [UK Competition and Markets Authority: grocery unit-pricing review](https://assets.publishing.service.gov.uk/media/64b80ab1ef5371000d7aeefa/CMA_Review_of_unit_pricing_in_the_groceries_sector.pdf) — documents missing and miscalculated unit prices, including a badly mispriced 250 ml example; UK legal duties are not exported here.
- [UK Competition and Markets Authority: price reduction claims](https://competitionandmarkets.blog.gov.uk/2023/03/31/urgency-and-price-reduction-claims-are-your-online-tactics-legal/) — “was/now” and percentage claims rely on a reference price; matching displayed arithmetic alone does not prove a historic regular price.
- The three-outcome check, rounding treatment, and stop path are Original synthesis.
