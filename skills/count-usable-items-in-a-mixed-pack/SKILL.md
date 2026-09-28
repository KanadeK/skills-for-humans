---
name: count-usable-items-in-a-mixed-pack
description: "Human-readable instructions for deciding how many mixed packs to buy when the needed items are unevenly distributed among their types."
---
# 按各类需要核对混合装 / Count Usable Items in a Mixed Pack

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 每种组合 5–10 分钟 / 5–10 minutes per assortment |
| Requirements / 必要物品 | 各类实际缺口、包装内逐类件数、可选的单类包装 / Need by type, per-type pack counts, available single-type alternatives |
| Side effects / 现实副作用 | “总共十件”可能不再是一份完整答案 / “Ten in total” may stop being a complete answer |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当一个普通日用品组合包混有不同颜色、规格或款式，而你对每一类的用量不相同时，加载这份 Skill。目标是**按每一类可用件数决定买几包，或改买单类包装**。先由商品规格任务确认哪些类真的能替代；这份 Skill 不把不同款自动当成可互换。药品、保健品、婴幼儿用品和危险材料不在这里靠组合包凑数。

### 准备与输入

写明购买覆盖的真实使用窗口，以及每一类需要多少件、手头已确认可用多少件。接着查看**现售这个包装**的逐类件数，而不只看盒面总件数和图片；还要确认今天总价、预算、携带与放置条件。包装只写“随机混合”“款式可能变化”而没有可保证的逐类件数时，不能用示意图计算固定供给。看不清时放大标签、读可访问说明或请店员指出实际数量。

### 执行

1. **把需求拆成各类缺口。** 例如你接下来确实需要黑笔 6 支、蓝笔 2 支，家里没有可用的，就写成“黑 6、蓝 2”。不要先写“共 8 支”：总数会把颜色差异藏起来。
2. **把一包能提供的数量也逐类写出。** 假设现售混合包明确标着“黑 4、蓝 4”，就记为“每包黑 4、蓝 4”。图片展示的摆放不等于文字承诺；逐类件数不明时先取得准确信息，否则停止这包的数量计算。
3. **逐类补足，再求包数。** 必需类别每包为 0 件时直接排除这款包。其余各类用缺口除以该包提供的同类件数，向上取整；所有类别里所需包数的最大值，才是这款混合包的最少包数。你也可以在纸上逐包加数，直到每类都够。例子中黑笔需要 2 包，蓝笔只需 1 包，因此要靠这款组合包完成全部需求就得买 2 包。
4. **把多出来的件数逐类摊开。** 两包得到黑 8、蓝 8，超出需求的是黑 2、蓝 6。只有在相应使用窗口内有真实用途时，才把余量算作可用；否则比较单类包、较小组合或减少本次购买。不要让 16 件的总数替 6 支用不到的蓝笔辩护。
5. **核对实际可执行性。** 选定的包数须仍适合今天的总支出、日期或使用限制、携带和空间。若包装构成、价格或你对某一类的需求在付款前变化，回到逐类清单重算；详细同单位价格比较交给价格任务。

### 成功条件

结账前你能给出一张短表：**各类缺口、每包各类件数、要买几包、各类预计余量**。买混合包、改单类包或不买，都有对应的可观察理由。只有“总共够多”而某一类仍不够，任务没有完成。

### 常见报错、补救与停止

- **ERR_TOTAL_ONLY：** 只知道“十件装”，不知道哪十件。查实际逐类标签或问清楚；若卖家也无法保证，就不能把它当成满足指定类别的包。
- **ERR_ZERO_OF_NEEDED_TYPE：** 包内没有你必须用的那一类。无论买多少包也补不上，改看单类包装或其他已确认适用的组合。
- **ERR_SURPLUS_IN_WRONG_TYPE：** 一类缺两件，另一类已多六件。分别记录余量，按缺的那一类找更合适的组合，不用总数抵消结构失衡。
- **ERR_VARIANTS_ARE_NOT_SUBSTITUTES：** 颜色、规格或功能相似，但实际用途不接受替代。维持分列；先确认适用性，不能为了让算式好看而合并类别。
- **ERR_PACK_CHANGED：** 线上图片、旧包装或购物清单的构成与手中现货不同。以这次实际能买到且已核实的组合重算；信息不明就停止。

### 假设、替代与现实副作用

这里假设商品是可独立计数的普通用品，类别差异会影响你真实使用。按当地售卖单位和眼前商品标示判断，不把某品牌旧包装当作固定配方。视觉、阅读或拿取不便时要求逐类文字说明、放大标签或请店员展示；无法核实就选构成明确的单类包。已知需要某一类但暂时买不到时，缺货后的改计划属于另一任务。

现实副作用是你可能买两种小包装而非一个看起来丰富的大盒；这个计算器只接受能用到的类别。

### 来源

- [美国 FTC：The case of the shrinking packaging](https://consumer.ftc.gov/consumer-alerts/2024/10/case-shrinking-packaging) — 熟悉的包装外观不能代替本次实际内容数量。
- [美国 EPA：Preventing Wasted Food At Home](https://www.epa.gov/recycle/preventing-wasted-food-home) — 食品购物应按真实使用量而非促销总量决定；这里将同一原则谨慎用于普通可计数用品。
- Original synthesis — 逐类缺口、包数与余量的算术流程；笔的数字是示例，不代表某款商品。

## English

Load this Skill when an ordinary pack contains several colours, sizes, or versions and you need uneven amounts of each. The result is **a pack count based on each usable type**, or a decision to buy single-type packs. First establish through product-fit information which types can truly substitute for one another; this Skill never assumes that similar-looking versions are interchangeable. Do not use mixed-pack arithmetic to choose medicines, supplements, infant goods, or hazardous materials.

### Preparation and inputs

Set the real period this purchase covers. Write down how many of each type you need and how many you already know are usable. Read the **current pack's per-type counts**, not just its total count or picture. Note today's total price, your spending limit, and what you can carry and place. “Assorted; contents may vary” without guaranteed counts cannot supply a fixed per-type number. Enlarge the print, use accessible product details, or ask staff to show the actual composition when needed.

### Execution

1. **Separate the gaps by type.** Suppose you really need six black pens and two blue pens, with none available at home. Write “black 6, blue 2” rather than “eight pens”; the total hides the colour constraint.
2. **Write the supply from one pack by type.** If the current pack explicitly states “four black, four blue,” record exactly that. A picture of pens arranged on a box is not a guaranteed count. If the per-type contents cannot be established, stop calculating with that assortment.
3. **Fill each gap, then find the pack count.** If a required type has zero units per pack, rule out this assortment. Otherwise divide each type's gap by the number of that type per pack and round a partial pack up. The largest of those results is the minimum number of mixed packs needed. You can also add one pack at a time on paper until every type is covered. In the example, black needs two packs and blue needs one, so two mixed packs are required to meet both gaps.
4. **Show the remainder by type.** Two example packs provide eight black and eight blue pens, leaving two black and six blue beyond the stated need. Count a remainder as usable only when it has a real use within your chosen period. Otherwise compare single-type packs, a smaller mix, or buying less. Six unneeded blue pens do not become useful because the box says sixteen in total.
5. **Check that the choice works.** The chosen count must still fit today's total spending, any dates or use limits, carrying ability, and space. If pack composition, price, or a required type changes before payment, recalculate the per-type list. Detailed like-for-like unit-price ranking belongs to the price task.

### Success

Before checkout, you can show **the gap for each type, counts per pack, packs to buy, and expected remainder for each type**. A mixed pack, single-type alternative, or no purchase can each be a completed decision. If the total looks ample but one required type is still short, the task is not done.

### Common errors, recovery, and stop points

- **ERR_TOTAL_ONLY:** The pack says “ten pieces” but not which ten. Read the per-type details or ask for them. If the seller cannot guarantee them, do not count this pack as meeting a specific type requirement.
- **ERR_ZERO_OF_NEEDED_TYPE:** A required type is absent. No number of these packs can fill that gap; choose a single-type or another confirmed suitable assortment.
- **ERR_SURPLUS_IN_WRONG_TYPE:** You lack two of one type but already have six extras of another. Record the remainder separately and find a mix that addresses the actual gap.
- **ERR_VARIANTS_ARE_NOT_SUBSTITUTES:** Similar colours, sizes, or functions do not meet the same use. Keep them in separate rows and verify suitability before merging categories for arithmetic.
- **ERR_PACK_CHANGED:** An online picture, old pack, or shopping note differs from the item available now. Recalculate from the verified current contents; stop if they cannot be confirmed.

### Assumptions, alternatives, and side effects

This assumes ordinary independently countable goods whose type affects your actual use. Read the current product and local selling units rather than treating an old brand pack as a fixed recipe. If seeing, reading, or reaching the box is hard, request a per-type written description, enlarge a label image, or ask staff to show it. Choose a clearly specified single-type pack when composition stays unknown. If a required type is unavailable, changing the plan after a stockout is a separate task.

You may leave with two small packs instead of one attractive variety box. This calculator only credits types you can use.

### Sources

- [US FTC: The case of the shrinking packaging](https://consumer.ftc.gov/consumer-alerts/2024/10/case-shrinking-packaging) — familiar packaging does not establish the current quantity inside.
- [US EPA: Preventing Wasted Food At Home](https://www.epa.gov/recycle/preventing-wasted-food-home) — food quantity should track expected use rather than the size of a deal; applied here cautiously to ordinary countable goods.
- Original synthesis — the per-type gap, pack count, and remainder calculation; pen counts are illustrative, not product claims.
