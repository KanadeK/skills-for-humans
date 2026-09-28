---
name: buy-complete-sets-of-separate-supplies
description: "Human-readable instructions for buying separate fixed-size packs of ordinary supplies in quantities that complete a confirmed number of repeated tasks."
---
# 把分别包装的用品买成完整套数 / Buy Complete Sets of Separate Supplies

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 一组任务 5–12 分钟 / 5–12 minutes for one task set |
| Requirements / 必要物品 | 已确定的重复次数、每次所需各项数量、各项现存与独立包装件数 / Confirmed task count, each item's per-task use, usable stock, separate pack counts |
| Side effects / 现实副作用 | 购物篮终于能完成整套，而非只拥有很多标签 / Your basket can finish a whole set instead of owning many labels |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你要重复完成几次同一种普通任务，而每次都要同时消耗**几种分别售卖、分别包装**的用品时，加载这份 Skill。它决定每种用品买几包，确保本次购物确实凑得出计划的完整套数；不负责设计这项任务、核对型号是否适用，或比较不同商家的单位价格。如果所有不同用品都锁在同一个混合包里，那是另一种包装结构，本 Skill 的“分别取整”算法不适用。医疗用品、危险材料和电气维修物料不在范围内。

### 准备与输入

只写这次已确定要完成的次数，以及**每完成一次各项真正消耗多少**。逐项核实家里已可用的存量和现售包装实际件数，确认用品本身适用、可分别购买。另记今天能花的总额、可放置与携带的量，以及有期限商品的适用窗口。未知存量先核实，不把“可能还有一包”当成已到手。

用纸、手机备忘录或你能读到的方式画一张小表：用品、每次用量、已可用、每包件数、缺口。无法看清外包装时放大照片、使用可访问的商品信息，或请店员读出各包的实际件数；数字缺失就先停止该组合的结账判断。

### 执行

1. **算每项的总缺口。** 用“确定的任务次数 × 该项每次用量 − 该项已确认可用量”，负数当作 0。例如计划做 6 个普通标记袋，每个需 1 个袋子和 2 张标签，且两者家里都没有，就分别缺 6 个袋子、12 张标签。只报“共缺 18 件”会把两种东西混在一起。
2. **对每项分别取整。** 若袋子一包 4 个、标签一包 10 张，就需要袋子 2 包、标签 2 包。每项都用自己的缺口除以自己的每包件数，不足一包向上取整；已经够用的项目买 0 包。旧包装或网页图片的件数不代替手中现货。
3. **反查能完成几整套。** 将“已可用 + 本次拟买到”逐项除以每次用量，只数完整套数；所有项目中最少的那个结果就是这篮商品最多能完成的次数。例子里得到袋子 8 个、标签 20 张，分别可做 8 套和 10 套，整篮最多做 8 套，已覆盖计划的 6 套。多出的标签不能替代袋子。
4. **把每项余量、成本和条件摊开。** 例子买后余下袋子 2 个、标签 8 张。若余量没有可信用途、某包超预算、放不下、带不走或日期不合，就尝试其他合适包装规格；确实只能完成较少套数时，先明确修改计划并重算。不要付了半套材料的钱，再假定缺的那项下次一定能买到。
5. **在结账前核对整篮。** 逐项读实际包装件数和总价；任一项被替换、缺货、包装缩量或数量改变，就从第 2 步重算。价格细比属于另一任务，不能以“大袋看起来便宜”覆盖完整套数不足。

### 成功条件

你能列出**每项要买几包、买后各有多少、能完成几整套、各剩多少**，且今天的付款、日期、储位和搬运都可执行。若没有一套完整且可负担的买法，明确输出“调整计划、改规格或暂不买”，也算完成决定。购物篮里每项各有一点，不等于任务能开始。

### 常见报错、补救与停止

- **ERR_ONE_ITEM_SHORT：** 大多数项目已足够，唯独一项不够。以最短项重新计算完整套数，补那一项或降低已确认任务次数；不要用其他项目的余量抵扣。
- **ERR_TOTAL_ITEMS_ONLY：** 只记总件数，丢了种类。按用品重新分行，逐项读取包装件数。
- **ERR_MIXED_PACK：** 商品其实是固定混合装，买一包会同时增加几种用品。停止本 Skill 的分别取整，按混合包的逐类供给重新判断；不要把同一包收费两次。
- **ERR_PACK_CHANGED：** 现货件数与上次记忆不同。用当前标签重算，旧购物清单不是库存接口。
- **ERR_INTERRUPTED：** 离开货架或改了任务次数。保留表格，回来核对手中的每包件数和总价，再算一次最短项后付款。

### 假设、替代与现实副作用

这里假设各项是可独立使用的普通用品，重复任务本身已确定且每次用量有依据。地区、商店、商品形态和身体条件会改变可买到的包装；请用实际件数、你能拿取的商品和可接受的预算，不复制示例数字。若一项必须与特定设备或其他材料兼容，先完成适用性核对。你看不清、拿不到或不能搬动整包时，用可访问说明、店员协助或可行配送取得准确数字与负担条件；关键信息拿不到就停止。

现实副作用是你可能发现两包标签仍只够被袋子限制的套数。算式不会让不完整的一套自动补齐。

### 来源

- [美国 EPA：Preventing Wasted Food At Home](https://www.epa.gov/recycle/preventing-wasted-food-home) — 购物数量应对应真实会进行的用途，不因大包装或优惠自动增加需要。
- [美国 FTC：The case of the shrinking packaging](https://consumer.ftc.gov/consumer-alerts/2024/10/case-shrinking-packaging) — 熟悉的包装外观不保证本次实际内容数量。
- Original synthesis — 分别取整、反查完整套数与逐项余量的算术流程；袋子和标签的数字仅供演示。

## English

Load this Skill when you will repeat one ordinary task a confirmed number of times, and every repetition consumes **several different supplies sold in separate packs**. You decide how many packs of each item to buy so the basket can complete the planned number of full sets. Designing the task, confirming product compatibility, and detailed unit-price comparison are separate work. If all types are locked into one mixed pack, this separate-rounding method does not apply. Do not use it for medical supplies, hazardous materials, or electrical repair parts.

### Preparation and inputs

Write the number of repetitions you have actually committed to and **how much of each item one repetition uses**. Verify usable stock and the current count in each separately sold pack, and confirm the items themselves fit the task. Note today's total spending limit, carrying and placement capacity, and any applicable date window. Check unknown stock before subtracting it; a possible spare pack is not available stock.

Make a small accessible table on paper or your phone: item, amount per task, usable stock, units per pack, and gap. If the printed count is hard to see, enlarge a clear photo, use accessible product details, or ask staff for the actual number in each pack. Pause checkout if a necessary count remains unknown.

### Execution

1. **Find each separate gap.** Use “confirmed repetitions × units of this item per repetition − verified usable stock,” with a negative result treated as zero. Suppose you will make six ordinary labelled pouches; each needs one pouch and two labels, and you have neither. Your gaps are six pouches and twelve labels. “Eighteen items” hides the two different requirements.
2. **Round packs separately.** If pouches come four to a pack and labels ten to a pack, buy two packs of pouches and two of labels. Divide each item's gap by its own pack count and round a partial pack up. Buy zero packs of an item already covered by stock. An old box or web photo does not establish today's count.
3. **Check how many complete sets the cart supports.** For every item, divide “usable stock + units you plan to buy” by that item's per-task use, counting only whole sets. The smallest result across items is how many complete tasks the basket supports. Here eight pouches support eight sets; twenty labels support ten. The basket supports eight complete sets, covering the six planned. Extra labels cannot replace a pouch.
4. **Show leftovers, cost, and limits by item.** The example leaves two pouches and eight labels. If a remainder has no credible use, a pack exceeds your budget, storage or carrying fails, or a date will not fit, look for another suitable pack size. If you can only make fewer sets, explicitly change the task count and recalculate. Do not pay for half a set while assuming the missing item will definitely be available later.
5. **Recheck the whole basket before payment.** Read each current pack count and total price. If one item is replaced, sold out, reduced in count, or changed in quantity, repeat from step 2. Detailed price ranking is another task; a visually large bag cannot make an incomplete set complete.

### Success

You can state **packs to buy, total available units, complete sets possible, and remainder for each item**, with an affordable, carryable purchase whose dates and space work. If no complete feasible combination exists, “revise the plan, choose another size, or buy nothing yet” is a completed decision. A little of every supply in the basket is not proof the task can start.

### Common errors, recovery, and stop points

- **ERR_ONE_ITEM_SHORT:** Most items are sufficient, but one is not. Recalculate complete sets from the limiting item; add that item or lower the confirmed task count. Other surplus cannot cover its deficit.
- **ERR_TOTAL_ITEMS_ONLY:** A single combined count hides item types. Restore one row per supply and read each pack count.
- **ERR_MIXED_PACK:** One purchase actually adds several types together. Stop separate rounding and assess that mixed pack's per-type supply; do not charge for one pack twice.
- **ERR_PACK_CHANGED:** Current contents differ from an old memory. Recalculate from the item offered now; an old shopping list is not inventory.
- **ERR_INTERRUPTED:** You leave the aisle or change the repetition count. Keep the table, then check each actual pack and price and recalculate the limiting item before paying.

### Assumptions, alternatives, and side effects

This assumes each ordinary supply can be used independently, the repeated task is already confirmed, and its per-task use has a basis. Regions, sellers, package formats, and physical access change what is available. Use actual counts, reachable goods, and your own budget rather than copying the example. Check suitability first if an item must match a device or other material. If print, shelves, or whole packs are inaccessible, obtain exact counts and carrying details through accessible information, staff help, or workable delivery. Stop while a key fact is missing.

You may discover that two label packs are still limited by the number of pouches. Arithmetic does not assemble an incomplete set.

### Sources

- [US EPA: Preventing Wasted Food At Home](https://www.epa.gov/recycle/preventing-wasted-food-home) — shopping amounts should match real uses, rather than growing automatically with a large pack or deal.
- [US FTC: The case of the shrinking packaging](https://consumer.ftc.gov/consumer-alerts/2024/10/case-shrinking-packaging) — a familiar pack appearance does not establish the current amount inside.
- Original synthesis — separate pack rounding, complete-set checking, and per-item remainder arithmetic; pouch and label figures are illustrative.
