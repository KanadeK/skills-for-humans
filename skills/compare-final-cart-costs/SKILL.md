---
name: compare-final-cart-costs
description: "Human-readable steps for comparing the current total payable for the same fixed basket of ordinary goods across sellers."
---
# 按最终应付额比较同一购物篮 / Compare Final Costs for the Same Basket

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 每组 5–12 分钟 / 5–12 minutes per comparison |
| Requirements / 必要物品 | 固定清单、可用商家的现价与结算费用、记录工具 / Fixed list, current seller prices and checkout charges, a way to record them |
| Side effects / 现实副作用 | “免运费”可能要接受整篮算术 / “Free delivery” may have to face whole-basket arithmetic |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你**已经确定要买的普通商品和数量**，需要比较两家店或两个购买渠道谁让你在这次交易中实际付得更少时，加载这份 Skill。这里比较**同一购物篮、同一货币、同一时点的最终应付额**。它不判断哪条路线更安全省力、哪家送货可靠，也不预测下周价格；取得方式是否可行另行核对。

### 准备与输入

把清单锁定到每件商品的规格与数量。为每个候选商家记录当前商品价、适用折扣、税费、配送/取货/服务等必须支付的费用，以及达到最低购买额的条件。使用实际可得的价格；会员价若你没有资格就用非会员价。线上结算预览和现场明确标价都可以是输入，但要记录查看时间与取得方式；不要把不同货币数字直接相减。

### 执行步骤

1. **先证明篮子相同。** 两边都必须能取得清单里相同用途、规格和数量的商品。缺货、替代品或不同包装量会改变篮子；先解决这些差异，再比总价。若是不同商品混合套装，先用[混合套装与单买比较](../compare-a-bundle-with-separate-items/SKILL.md)核对整份清单。
2. **列出每边的商品小计。** 按这次实际可用的价格和数量逐项相加，不拿广告里最低的单品价代替整篮价格。条件券、会员价和起购优惠须逐条核对资格与适用商品；无法核实的折扣先不计。
3. **加上这次无法避开的费用。** 查结算页或明确说明中的税费、配送、处理、取货或服务费。预选附加项只有在你真正取消且总价已更新后才不算。若必须另买不需要的商品才能满足免运费或最低额，那个方案已不是同一篮子；不要给“免费”补一笔看不见的购买。
4. **比较当前最终应付额。** 例：同一篮子在 A 的商品小计为 12、必付配送 4，合计 16；在 B 商品小计 14、必付配送 1，合计 15。B 商品价更高，却少付 1。若税费或另一必付项目尚未显示，先记“总额未确认”，不宣布赢家。
5. **核对可执行的最后一步。** 付款前再次查看商品明细、数量、费用和最终总额，记下商家、时间和取得方式。只比较你可以实际选择的同类取得方式；配送是否满足时间、温度或交付点要求，先由相应取得任务判断。结算金额临时变化就重算，或暂停。

### 完成与停止

你能给两边展示**完全相同的清单**、当前应付总额、差额和仍未计入的现实代价，就完成了这次金额比较。缺货、费用未显示、币种不同或条件资格不明时，输出“暂不可比”；保留已知数字，不编一个未来运费或折扣。

### 常见报错与补救

- **只比商品小计：** 加上这次必须付的配送、服务和适用税费，再看最终数字。
- **为免运费凑单：** 先退回原清单；若确实新增需求，重新锁定两边同一篮子后再比较。
- **预选服务没有取消：** 在允许时取消并确认总额变动；不能取消就算入必付额。
- **一边用会员价、一边用自己拿不到的券：** 只保留当前真实可用的价格。未来积分或返利不抵扣本次应付额。
- **同款在一店缺货：** 不用相似图片当作同一商品；暂停价格结论，交由缺货或规格核对流程处理。

### 假设、替代与副作用

这份流程只比较购买时的钱款。路程、携带、配送可靠性、售后政策和使用体验可能改变最终选择，但不能伪装为已确认的折扣。商家页面、地区税费、服务范围和货币会变化；按这次可见的最终价格做决定。看不清费用明细或不便使用线上页面时，可用可访问的文字版、放大、读屏、纸笔、计算器或商家正式服务渠道取得数字；若必须登录而你没有资格，不把登录后价格算成自己的。副作用是最醒目的“低价”可能输给结算页。

### 来源

- [美国联邦贸易委员会：网上购物](https://consumer.ftc.gov/articles/online-shopping) — 比较具体商品时应核对尺寸、型号及含运送、处理、税费等的总成本；这里不采用其美国专属权利描述。
- [澳大利亚竞争与消费者委员会：价格展示](https://www.accc.gov.au/business/pricing/price-displays) — 分步追加费用会使初始价格低于最终应付额；只借鉴核对总价的方法，不输出跨地区法律结论。
- 固定购物篮、预选项复核与不可比停止条件为 Original synthesis。

## English

Load this Skill when the **ordinary goods and quantities are already fixed** and you need to compare what two sellers or channels would actually charge for this transaction. It compares the **same basket, currency, and observed time at the final payable amount**. It does not decide which route is easier or safer, whether delivery is reliable, or what prices will be next week. Check the feasibility of each way to obtain the goods separately.

### Preparation and inputs

Lock the list to each item's specification and count. For each available seller, record current item prices, applicable discounts, taxes, unavoidable delivery, pickup, handling, or service charges, and any minimum-order condition. Use prices available to you; if you lack membership, use the non-member amount. A checkout preview or clear in-store price can be an input, but note the time and acquisition method. Do not subtract numbers in different currencies.

### Execution steps

1. **Prove the baskets match.** Both routes must supply the same suitable items, specifications, and quantities. Stockouts, substitutions, and different pack amounts change the basket; resolve them before ranking totals. For a mixed bundle, first use [Compare a Bundle With Separate Items](../compare-a-bundle-with-separate-items/SKILL.md) to check the fixed list.
2. **Add each basket's item subtotal.** Use the prices and counts that apply now, not the lowest advertised price for one attention-grabbing item. Check voucher, member, and minimum-spend conditions against the actual items and your eligibility. Leave an unverified discount out of the confirmed total.
3. **Add unavoidable charges.** Inspect the checkout preview or stated terms for taxes, delivery, handling, pickup, and service fees you must pay this time. Remove a preselected extra only after you actually deselect it and see the total change. Buying an unneeded item to reach free delivery or an order minimum changes the basket; “free” does not make that purchase invisible.
4. **Compare current final amounts.** For the same basket, suppose A has an item subtotal of 12 and mandatory delivery of 4, totalling 16. B has items costing 14 and mandatory delivery of 1, totalling 15. B's items cost more, but you would pay 1 less overall. If a tax or other compulsory charge is not yet shown, mark the total unconfirmed instead of declaring a winner.
5. **Check the last step you can actually take.** Before paying, read the items, counts, charges, and final total again; record seller, time, and acquisition method. Compare only methods you could use. Whether delivery meets your time, temperature, or handoff needs belongs to the acquisition decision. Recalculate or pause if the checkout total changes.

### Success and stop

You can show the **identical list** at both sellers, each current payable total, the difference, and any real-world cost left outside this money comparison. If stock, a charge, currency, or eligibility is unclear, output “not comparable yet.” Keep known figures but do not invent a future fee or discount.

### Common errors and recovery

- **Comparing item subtotals only:** Add delivery, service, and applicable tax you must pay for this transaction, then compare final amounts.
- **Adding goods for free shipping:** Return to the original list. If your needs genuinely change, lock the same revised basket at both sellers and start again.
- **A preselected service remains in the cart:** Deselect it where possible and verify that the total changes. If it cannot be removed, include it as payable.
- **Using a membership price or voucher unavailable to you:** Keep only prices you can use now. Future points or rebates do not reduce today's payment.
- **An item is missing at one seller:** A similar photo is not proof of the same item. Pause the price result and settle the stock or specification question first.

### Assumptions, alternatives, and side effects

This procedure compares money due at purchase. Travel, carrying, delivery reliability, after-sale policies, and use experience may affect your final choice, but they are not confirmed discounts. Seller pages, local taxes, service areas, and currencies vary; use the final amount visible for this transaction. If a fee breakdown is inaccessible, use readable text, magnification, screen reading, paper, a calculator, or the seller's official information channel. If a price requires membership you do not have, do not treat it as yours. The large “low price” on an item page may lose to the checkout total.

### Sources

- [US Federal Trade Commission: Online Shopping](https://consumer.ftc.gov/articles/online-shopping) — compare exact product details and total cost, including shipping, handling, delivery, taxes, and other fees; this Skill does not export US-specific rights claims.
- [Australian Competition and Consumer Commission: Price displays](https://www.accc.gov.au/business/pricing/price-displays) — gradually added charges can make an initial price lower than the final payable amount; only the total-checking method is used, not cross-region legal rules.
- The fixed-basket comparison, preselected-option check, and stop conditions are Original synthesis.
