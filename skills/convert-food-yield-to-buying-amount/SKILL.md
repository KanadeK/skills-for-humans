---
name: convert-food-yield-to-buying-amount
description: "Human-readable instructions for buying enough ordinary food when the sold weight differs from the drained or ready-to-use amount a plan needs."
---
# 从可用量倒推购买量 / Convert Food Yield to a Buying Amount

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 每项 5–10 分钟 / 5–10 minutes per item |
| Requirements / 必要物品 | 要用的成品量、商品销售形态、对应的可用量资料 / Needed ready-to-use amount, form sold, evidence for its usable yield |
| Side effects / 现实副作用 | 标签上的总重量不再自动等于盘里的重量 / Labelled total weight no longer silently equals usable food |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你的普通菜谱或明确用途需要“沥干后、去皮后、去核后或按包装说明复水后”的数量，而商店卖的是另一种形态时，加载这份 Skill。它只把**需要的可用量换算为付款前的购买量**；不决定吃多少才健康，不教烹调或食品保存。若成品量与出售量本来就是同一形态，直接使用一般包装选择即可。

### 准备与输入

写下用途需要的**数量、单位和形态**，例如“沥干的豆子 450 克”，再减去家中已确认可用、形态相同的存量；其他形态的存量只有先用可信依据换算成目标形态，才能抵扣。读候选商品的净含量、沥干重量或按包装说明制成的产量；对整颗蔬果等没有成品量标签的商品，只使用与你实际去皮、去核或切除部分方式相符的可靠平均出成资料。不同品种、状态和处理方式不能共用一个随手记住的百分比。

如果标签太小，可放大照片、读可访问的商品说明或请店员展示。若关键形态或出成率仍不明，改选已标明可用量的合适商品，或暂缓这项购买；不要用食品安全日期或外观猜一个出成率。

### 执行

1. **先固定目标形态。** 把“需要 450 克沥干豆子”与“这罐净含量 400 克、其中包括液体”分开写。液体不会自动补成豆子。若用途实际上需要连液体一起用，改按那个真实用途计算。
2. **为每个候选找对应的可用量。** 有沥干重量或按说明制成量时，用该商品实际标示；没有时，找同一种食物、同一购买形态和同一处理终点的可信平均资料。平均值只是计划依据，不能保证这包刚好产出相同重量。没有可信依据就停止精确换算。
3. **倒推数量。** 如果每包可提供一个已知可用量，用“缺口 ÷ 每包可用量”，不足一整包时向上取整。例如缺 450 克沥干豆子，候选每罐标示沥干后 240 克，就需要 2 罐，可用量约 480 克。若资料给的是可用比例，则用“所缺可用量 ÷ 比例”求应买原形重量；比例必须来自匹配形态的资料，不能借隔壁蔬菜的数字。
4. **检查取整后的余量。** 对照你真正会使用的次数、标签日期与开封条件、预算和携带能力。余量没有可信用途时，寻找不同规格、已处理的等价形态，或调整购买决定；不要为了凑满包装而偷偷扩大菜谱。
5. **记录可复核的决定。** 结账前写出“目标可用量 → 本次所用出成依据 → 每包可用量 → 买几包 → 预计余量”。将来源或标签留在这次购物记录里，下次发现实际出成不同才有依据修正。

### 成功条件

你能用相同单位说明为什么买这个原形重量或包数，并知道哪一步是标示值、哪一步只是估计。没有可靠出成资料时，“换可明确计量的商品或暂缓”也是完成；买很多来掩盖未知不是。

### 常见报错、补救与停止

- **ERR_NET_IS_NOT_DRAINED：** 净含量包含液体，用途只需固体。找实际沥干重量或可信同款资料；找不到就换可计量选项，不把净含量当沥干量。
- **ERR_WRONG_FORM：** 拿整颗蔬果的重量去对照去皮切块的需求，或把干品重量直接当复水后的重量。重新命名两端的形态并找对应出成；无法对齐就停止该换算。
- **ERR_YIELD_IS_AVERAGE：** 参考资料给出平均值，实物状态或你的处理方法不同。把结果标成估计，选择你能接受的少量余量；若任务要求精确且不能容忍差异，先取得商品专属数据。
- **ERR_TOO_MANY_PACKS：** 向上取整后余量太多或超预算。比较别的可用规格或改变本次用途计划，而不是默认“总有一天会吃”。
- **ERR_UNREADABLE_LABEL：** 放大、请店员读出具体数字，或换有清楚标示的商品；关键数字未确认时停止付款判断。
- **ERR_INTERRUPTED：** 离开货架后保留目标形态、已核实的出成依据和算出的包数；回来付款前重新确认手中商品、日期与价格，不能把别款的出成套过来。

### 假设、替代与现实副作用

这里假设用途与所需形态已由你确定，食品本身适用且安全条件已另行核实。不同地区的标签、计量单位和商品规格会变；按实际商品与当地解释，不把美国机构餐饮的出成表当成每个家庭的保证。没有秤或不便读小字时，优先选明确按份标示的合适商品，并请店员或同行者帮助读数；需要精确结果却无可靠资料时就不作精确承诺。

现实副作用是你可能买到比直觉多一点的原形食材，也可能发现“沥干后”三个字比罐头的设计更有决定权。

### 来源

- [美国 USDA Food Buying Guide：About](https://foodbuyingguide.fns.usda.gov/Home/About) — 区分出售形态与可用/可食形态，并用出成资料估算购买量；其数值是机构餐饮的平均计划值。
- [美国 USDA Food Buying Guide：Appendix B](https://foodbuyingguide.fns.usda.gov/Appendix/ResourceAppendixB) — 展示从原形数量倒推待使用形态数量的方法。
- Original synthesis — 家庭购物的取整、余量、停止和记录步骤；例子中的包装数字仅用于演示运算。

## English

Load this Skill when an ordinary recipe or known use calls for an amount **after draining, peeling, removing pits, or preparing a product as its label directs**, while the shop sells another form. You are converting a needed usable amount into a buying amount before payment. This does not prescribe a healthy intake, teach cooking, or handle storage. If the needed and sold forms already match, use an ordinary package-size choice.

### Preparation and inputs

Write the needed **amount, unit, and form**, such as “450 g of drained beans.” Subtract stock you know is usable in that same form; stock in another form counts only after a credible conversion to the target form. Read each candidate's net contents, drained weight, or yield when prepared as directed. For whole produce without a ready-to-use amount on the label, use a credible average yield only when it matches the specific food, its purchased form, and the parts you will remove. Different varieties, condition, and preparation can change yield; do not borrow a remembered percentage from another food.

If print is small, enlarge a clear image, use accessible product information, or ask staff to show the number. If the form or yield remains unknown, choose a suitable product with a stated usable amount or defer this purchase. A date or attractive appearance cannot supply a missing yield factor.

### Execution

1. **Fix the target form.** Write “450 g drained beans” separately from “400 g net contents including liquid.” Packing liquid is not extra beans. If your actual use includes the liquid, calculate for that use instead.
2. **Find the corresponding usable amount.** Prefer the current product's drained weight or prepared yield when it is stated. Otherwise use credible average data for the same food, purchased form, and prepared endpoint. An average helps planning; it does not promise the exact contents of this pack. Stop precise conversion when no matching basis exists.
3. **Convert back to buying units.** For a stated usable amount per pack, divide the gap by that amount and round a partial pack up. If you need 450 g drained and a candidate states 240 g drained per can, two cans provide about 480 g. For a yield fraction, divide the needed usable amount by the matching fraction to estimate the as-purchased weight. Never apply one food's fraction to another.
4. **Check the rounded remainder.** Compare it with real uses, label dates and after-opening conditions, what you can pay, and what you can carry. If the remainder has no credible use, look for another size or an already prepared suitable form, or change this purchase decision. Do not silently expand the recipe to justify the box.
5. **Keep the decision auditable.** Before checkout, record “needed usable amount → yield basis → usable amount per pack → pack count → expected remainder.” Keep the label or source with this shopping note so a different actual yield can inform a later purchase.

### Success

You can explain your chosen as-purchased weight or pack count in one consistent unit, and identify what came from the label versus an estimate. If yield evidence is missing, switching to a clearly measured product or waiting is a completed decision. Extra packs do not turn an unknown into a fact.

### Common errors, recovery, and stop points

- **ERR_NET_IS_NOT_DRAINED:** Net contents include liquid but your use needs solids. Find the drained weight or credible information for that product; otherwise choose a measurable alternative. Do not treat net as drained weight.
- **ERR_WRONG_FORM:** Whole produce is compared with a peeled, cut amount, or dry weight with prepared weight. Name both forms again and find the matching yield. Stop if they cannot be aligned.
- **ERR_YIELD_IS_AVERAGE:** The reference is an average and your product or method differs. Mark the result as an estimate and keep only a small remainder you can actually use. A task requiring exact output needs product-specific evidence first.
- **ERR_TOO_MANY_PACKS:** Rounding up creates too much surplus or exceeds your limit. Compare other suitable sizes or revise this use plan rather than assuming you will eat it someday.
- **ERR_UNREADABLE_LABEL:** Enlarge the text, ask staff for the number, or choose a clearly labelled product. Stop the purchase calculation while a key number is unconfirmed.
- **ERR_INTERRUPTED:** Keep the target form, verified yield basis, and calculated count. When you return before payment, recheck the actual product, date, and price; do not apply another product's yield to this one.

### Assumptions, alternatives, and side effects

This assumes you already know the intended use and form, and that suitability and safety have been checked separately. Labels, units, and package sizes vary by region. Use the actual product and local interpretation; USDA institutional-food averages are not a guarantee for a household pack. Without a scale or accessible small print, prefer a suitable product with a clear per-portion amount and ask staff or a companion to help read it. Do not promise precision when the basis is missing.

You may buy a little more whole food than intuition suggested, or discover that “drained” matters more than the can's graphic design.

### Sources

- [USDA Food Buying Guide: About](https://foodbuyingguide.fns.usda.gov/Home/About) — distinguishes food as purchased from edible or prepared yield and uses average yield data to plan purchasing.
- [USDA Food Buying Guide: Appendix B](https://foodbuyingguide.fns.usda.gov/Appendix/ResourceAppendixB) — examples of converting as-purchased quantities to ready-to-use amounts.
- Original synthesis — household rounding, remainder, stop, and note-taking steps; package figures in the example are illustrative.
