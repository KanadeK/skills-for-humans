---
name: set-a-weight-range-for-loose-goods
description: "Human-readable instructions for choosing and checking a usable amount of ordinary loose goods whose exact weight is known only when weighed."
---
# 给称重商品设购买范围 / Set a Weight Range for Loose Goods

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 每项 3–8 分钟 / 3–8 minutes per item |
| Requirements / 必要物品 | 用途所需数量、能接受的上下限、可核实的净重和现场总价 / Needed amount, acceptable lower and upper limits, checkable net weight and current total price |
| Side effects / 现实副作用 | 你可能请人再减一点，而不是带走超量 / You may ask for a little less instead of taking an excess |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当普通散装蔬果、柜台分份商品或按重量出售的预包商品，只有称重后才知道这次**实际要买多少**时，加载这份 Skill。它处理目标量与称重结果之间的“接受、调整或不买”；同单位价格比较、食品是否合格和商家争议是其他任务。不要用它处理危险化学品、药品或必须精确计量的医疗用途。

### 准备与输入

先依据真实用途定一个**最低需要量和最高愿意带走量**，并确认使用的重量单位、今天付款上限、携带能力与储存条件。下限不能低于用途实际要求；上限只包括有可信去向的余量。例如你需要约 450 克普通蔬菜，且能使用额外 100 克，才可以把可接受范围写成 450–550 克；这只是举例，不是通用公差。

看清店家按件、按重量或按预包实际标示收费，并找到可核实的净重与本次总价。自带容器、店家袋子或托盘会改变毛重；需要去皮重时按店家当前流程询问或操作，不凭自己猜显示屏已经扣除了容器。看不见秤或标签时请店员展示读数、使用可读收据或放大照片；仍无法确认就不付款。

### 执行

1. **把范围说清。** 自己取散货时先少取，柜台分份时先说“我需要大约多少，最多接受多少”，并说明你使用的单位。店家不提供分切或调整服务时，直接用现有可选商品判断，不把请求当成必然会被答应。
2. **在付款前看实际净量。** 现场称重就读显示的商品净重；已分装好的随机重量包装则读这包自己的净含量。若容器被一起称入，按店家流程确认去皮重或请店员解释实际商品重量。不要自行改动不熟悉的计量设备。
3. **与上下限比较。** 低于下限，若商家允许且仍可安全处理，就加到足够；高于上限，若可调整就减到范围内。不能调整时换另一份合适的商品或不买。秤读数不是你用量计划的替身。
4. **复核今天的总价和条件。** 实际重量变化会改变实际付款额。确认屏幕或标签上的本次总价仍在上限内，也能带回并按标签条件处理。重量在范围内但价格、日期或携带条件不成立，仍然可以拒绝这份。
5. **结束前留下一个数字。** 记录“目标范围 → 实际净量 → 实际总价 → 接受/调整/不买”。若调整后再次称重，以最后确认的读数为准，不用第一次读数结账。

### 成功条件

结账前你知道这次商品的**实际净量**，它在你事先定下的可用范围内，且实际总价与携带条件可接受。或者你明确选择了调整、换份或不买。只看一个大概袋子体积就付款，不算完成。

### 常见报错、补救与停止

- **ERR_LOOKS_LIKE_HALF_KILO：** 手里看着像半公斤，称出来却多或少。以核实的净重为准，按上下限调整；眼力不是计量工具。
- **ERR_CONTAINER_INCLUDED：** 显示重量可能包含盒、袋或自带容器。请店员说明并按适用流程确认净量；不能确认时停止。
- **ERR_NO_ADJUSTMENT：** 商品已封好或店家不分切。换另一份或接受你范围内的现货；不要先付款再假定可以退掉多余部分。
- **ERR_TOTAL_OVER_LIMIT：** 重量合适但实际总价超出上限。减少可调整的量、选其他合适商品或不买；详细价格口径比较归另一任务。
- **ERR_UNREADABLE_SCALE：** 无法看见读数、收据或包装净量。请求可访问的数字说明；若关键数字仍不可核实，停止购买决定。

### 假设、替代与现实副作用

这里假设商品本身适用，店家允许你在付款前核对本次数量。称重、去皮重、退回散货和分份规则因地点及店家而异；按眼前流程和当地要求，不把某国的设备规则当成全球权利。行动、视力或握力受限时可请店员按范围取货、展示最后净重，或选清楚标示实际重量的合适预包商品。需要准确到无法容忍称重误差的任务，不适合用这种近似采购流程。

现实副作用是你可能多一次称重或少买一点，购物袋不再自行决定晚餐份量。

### 来源

- [英国 Office for Product Safety and Standards：Consumer products: value for your money](https://www.gov.uk/guidance/consumer-products-value-for-your-money) — 以称重购买散货的实例说明最终数量由实际计量确认；制度说明仅适用于其地区。
- [英国 Bromley Trading Standards：Refill shops](https://www.bromley.gov.uk/leaflet/328999/3/733/d) — 区分商品净重、容器皮重和总重，并列出店家可能使用的计量流程；这是英国商家指导，不是跨地区消费者操作指令。
- Original synthesis — 事先设上下限、称重后接受/调整/停止的购物流程。

## English

Load this Skill when ordinary loose produce, a counter portion, or a random-weight prepack has no exact **purchase quantity** until it is weighed. You are comparing a needed range with the measured result and deciding whether to accept, adjust, or decline it before payment. Like-for-like unit-price ranking, product quality, and seller disputes are separate tasks. Do not use this for hazardous chemicals, medicines, or medically exact quantities.

### Preparation and inputs

Set a **minimum needed weight and maximum weight you would actually use**, in a stated unit. Check today's spending ceiling, carrying ability, and storage conditions. The lower limit must cover the real use; the upper limit includes only a credible remainder. For example, if you need about 450 g of an ordinary vegetable and can use another 100 g, you might accept 450–550 g. That is an illustration, not a universal tolerance.

Check whether the shop charges by item, weight, or the actual weight on an individual prepack. Find a way to verify this purchase's net weight and total price. Your own container, a shop bag, or a tray can add weight; when tare matters, follow the shop's current method or ask staff rather than assuming the display already excludes the container. If you cannot see the scale or label, ask staff to show the reading, use an accessible receipt, or enlarge a clear photo. Do not pay while a key number remains unknown.

### Execution

1. **State your range.** Start with a small loose amount when you select it yourself. At a counter, say roughly how much you need and your maximum, using a clear unit. If the shop does not offer portion changes, assess the available items; an adjustment request is not a promise of service.
2. **Read actual net quantity before paying.** For a weighed transaction, check the product's net weight on the display. For a sealed random-weight pack, use that individual pack's label. If a container may have been weighed too, confirm the net amount through the shop's tare procedure or ask staff to explain it. Do not change equipment you do not know how to use.
3. **Compare with both limits.** Below the minimum, add more if the seller allows it and handling remains appropriate. Above the maximum, ask to remove some if possible. If it cannot be adjusted, choose another suitable portion or buy none. The scale is not your use plan.
4. **Recheck today's cost and constraints.** A different actual weight changes what you pay. Confirm the displayed total is within your limit and that you can carry and handle the goods under their label's conditions. Weight within range does not override an unaffordable price, unsuitable date, or impossible trip home.
5. **Keep the final number.** Record “planned range → actual net weight → actual total → accept/adjust/decline.” If the goods are weighed again after adjustment, use the last confirmed reading at checkout, not the first.

### Success

Before checkout you know this purchase's **actual net weight**, it falls within your pre-set usable range, and its real total price and carrying needs are acceptable. Or you deliberately choose an adjustment, another portion, or no purchase. Paying from the apparent size of a bag is not a completed check.

### Common errors, recovery, and stop points

- **ERR_LOOKS_LIKE_HALF_KILO:** A handful looks like half a kilogram but weighs differently. Use the confirmed net reading and adjust against your limits; sight is not a scale.
- **ERR_CONTAINER_INCLUDED:** The displayed weight may include a box, bag, or your container. Ask how net weight is determined under the shop's process. Stop if it cannot be confirmed.
- **ERR_NO_ADJUSTMENT:** The pack is sealed or the seller will not divide it. Choose another portion or an existing pack within your range. Do not pay first and assume the excess can later be returned.
- **ERR_TOTAL_OVER_LIMIT:** Weight works but the actual total exceeds what you can pay. Reduce an adjustable amount, choose another suitable option, or buy none. Detailed price-basis comparison belongs to another task.
- **ERR_UNREADABLE_SCALE:** You cannot access the reading, receipt, or pack weight. Request an accessible number; stop the purchase decision if the key fact remains unavailable.

### Assumptions, alternatives, and side effects

This assumes the product is suitable and the seller lets you check this purchase's quantity before payment. Weighing, tare, returning loose goods, and portioning procedures differ by shop and region. Follow the actual process and local rules; one country's equipment rules are not worldwide consumer rights. If reaching, seeing, or holding goods is difficult, ask staff to select to your range and show the final net weight, or choose a suitable prepack with a clear actual-weight label. A task that cannot tolerate measurement variation needs a more exact process.

You may need one extra weighing step or leave with a little less. The shopping bag no longer chooses dinner size for you.

### Sources

- [UK Office for Product Safety and Standards: Consumer products: value for your money](https://www.gov.uk/guidance/consumer-products-value-for-your-money) — illustrates loose goods whose final quantity is confirmed by weighing; its regulatory discussion is region-specific.
- [UK Bromley Trading Standards: Refill shops](https://www.bromley.gov.uk/leaflet/328999/3/733/d) — distinguishes product net weight from container tare and gross weight and describes possible shop methods; this is UK business guidance, not universal shopper instructions.
- Original synthesis — the pre-set range and accept, adjust, or stop shopping flow.
