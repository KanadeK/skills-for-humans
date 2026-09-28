---
name: match-bags-to-flight-allowance
description: "Human steps to check the actual operating airlines and fare for cabin and checked-bag count, size, weight and fees, then compare those rules with the bags you intend to bring."
---
# 按本次航程核对行李件数与尺寸 / Match Flight Bags to This Itinerary's Allowance

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 10–20 分钟 + 航司确认时间 / 10–20 minutes plus airline confirmation |
| Requirements / 必要物品 | 本次票价/舱位与每段实际承运航司、拟带的随身/托运行李、可测量件数尺寸重量的工具或服务 / This fare/cabin and each operating airline, proposed cabin/checked bags, a way to count and measure bags or obtain those measurements |
| Side effects / 现实副作用 | 可能换包、减件或承担经确认的行李费 / You may change bags, reduce pieces, or accept a confirmed bag fee |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已有机票，准备决定本次航程带几件**随身小件、登机箱与托运行李**时，用这份 Skill核对实际航司、票价和每段的件数/尺寸/重量/费用，再量自己手中的包。目标是每件有明确去向且在本次规则内，或在交运行李前解决超限与不明费用。本文只核行李**额度和外部尺寸重量**；箱内物品能否随身/托运是另一项限制核对，不由“箱子合格”自动推出。

### 准备与输入

拿出实际订单、旅客、票价/舱位、各航段及真正执飞的航司，列出拟带小件、登机箱、托运行李与特殊件。代码共享、联程、儿童/婴儿和会籍等条件可能改变适用规则，不以卖票页面的某个通用广告当作本次额度。准备卷尺、秤或可使用的航司量测设施；没工具就借用、查店内服务或到有官方量具的地点确认，不猜自己背包“看起来差不多”。

### 执行

1. **找到这张票适用的实际政策。** 从订单/航司官方行李页核对每位旅客、每段或整张联程票的随身小件、登机箱、托运件数与额外费用条件。若由合作航司执飞或换航司，按航司提供的该订单适用说明核实；规则冲突就向有权承运方确认，不选择看起来最宽的一页。
2. **把允许额度和自己的包分开写。** 为每种包记下本次适用的件数、外部尺寸与重量标准（含轮子、把手等如何计量按航司规则），并量实际装好后的包。特殊物品、助行器、婴儿用品或超大件走该航司专门要求，不装成普通箱子掩盖差异。
3. **解决超额与费用。** 包太大/重、件数多或需要购买托运额度时，先按航司当前允许的减件、换包、预购或现场办理路径选择，读回真实费用、截止与是否已在订单中生效。已付款与“系统接受这件实物”不是一个状态；别以旧截图当费用保证。
4. **临交运再核。** 出发前查看订单/航司通知是否换实际承运方或机型，确认随身行李是否可能因舱位空间被要求在登机口托运；箱内涉及必须留在客舱的物品另做内容核对。到柜台/登机口若工作人员按规则要求调整，以现场正式指示核实，不争辩别家航司旧额度。

### 成功条件

本次实际票价与承运航司的每类行李件数、尺寸、重量、费用已找到，拟带包按同一测量口径逐件比对并解决超限；或未确认项被明确停下并向承运方求证。行李外形合格不证明内件符合安检或危险品规则，也不保证登机箱最终一定留在客舱。

### 常见报错与补救

- **只读“销售航司”却由另一家执飞：** 对照订单中的实际承运方和航司联运规则，必要时请该订单客服说明适用额度。
- **空箱量得合格，装满后超重：** 重新称实际出发状态，按真实规则减件或办理额外额度。
- **把随身小件当第二个登机箱：** 核对该票价对两类物品的定义与放置要求，不用名称不同冒充额外件。
- **会员/信用卡优惠没显示在订单：** 核对适用资格及是否在这段生效，未确认前按待定处理。
- **登机口要求托运登机箱：** 先按航司正式要求处理箱内必须留在客舱的物品，再交箱；不能把外形合格当成拒绝现场安排的依据。

### 假设、替代与现实副作用

这里只做普通旅客行李额度核对，不计算危险物品、海关或赔偿，也不承诺费用。不同航司、票价、路线、合作承运和日期规则可能不同；Delta 页面是实例，不能外推其数值。无法自行测量/搬包时可借量具、用航司服务或请可信的人协助；工作人员对实际箱体的判断仍以本航程规则为准。换包或减件可能麻烦，但比在柜台才发现多出一件更容易处理。

### 来源

- [Delta：Baggage Policy and Fees](https://www.delta.com/us/en/baggage/overview) 与 [Carry-On Baggage](https://www.delta.com/us/en/baggage/carry-on-baggage)（英文，美国航司）— 舱位、优惠、航段与合作航司会影响额度，登机口也可能因空间调整随身箱；本文不复制其数值。
- [CATSA：Carry-on or Checked?](https://www.catsa-acsta.gc.ca/en/what-can-bring/carry-or-checked)（英文，加拿大安检机构）— 安检物品分类与航司设定的箱体尺寸、重量和超额费用分属不同职责。
- Original synthesis — 把订单适用规则与实际装满的每件包逐项对照，将超限/未确认状态留在交运前处理。

## English

Use this Skill after booking when deciding how many **personal items, cabin bags, and checked bags** to bring. Find the actual airline, fare, and segment rules for count, external size, weight, and fees; then measure the bags you intend to use. Finish with a clear destination for each compliant bag or resolve the excess before handover. This checks **allowance and outer dimensions/weight**, not whether every item inside is permitted in cabin or hold.

### Preparation and inputs

Have the actual booking, travellers, fare/cabin, every leg, and operating airlines. List personal items, cabin bags, checked bags, and special items. Codeshares, connections, children, infant items, and membership benefits can change applicable rules; a generic sales banner is not your allowance. Use a tape measure, scale, or an accessible official measurement point. Without a tool, borrow one, use an available service, or verify at an airline measurement point instead of judging a backpack by appearance.

### Execution

1. **Find the policy for this ticket.** In the booking and airline's official baggage guidance, check the count and limits for each traveller and leg or through ticket. For a partner-operated leg, read the airline's order-specific applicable-carrier explanation. Ask the responsible airline when pages conflict; do not select the most generous chart by preference.
2. **Separate allowed limits from actual bags.** Record this itinerary's count, outside dimensions and weight for each bag class, using the airline's measurement definition for wheels/handles. Measure bags as actually packed. Mobility aids, infant equipment, oversized or special items follow dedicated rules, not a disguised ordinary suitcase entry.
3. **Resolve excess and fees.** For a large, heavy, or extra bag, choose among that airline's available reduce, swap, prepay, or airport routes. Read back real fees, deadline, and whether a purchased allowance appears in the booking. Paying is not the same as physical acceptance, and an old fee screenshot is not a guarantee.
4. **Recheck before handover.** Watch for a changed operating carrier or aircraft notice. A cabin bag may have to be checked at the gate for capacity; run a separate contents check for anything that must remain in the cabin. Follow current official staff direction at the counter or gate, not another carrier's old allowance.

### Success

For the actual fare and operating carrier, you identified each bag class's count, dimensions, weight, and fee conditions and compared every packed bag under the same measuring rule. Excesses are resolved, or an unknown is explicitly pending airline confirmation. A fitting bag says nothing about screening or dangerous-goods contents and does not guarantee it will stay in the cabin.

### Common errors and recovery

- **Marketing airline differs from operating carrier:** Compare the booking and applicable partner rules; ask support for the rule for this ticket when uncertain.
- **Empty bag fits but full bag is overweight:** Weigh it in its travel state and reduce or arrange the real extra allowance.
- **Personal item is treated as a second cabin case:** Read this fare's definitions and placement rule; a different name does not create an extra piece.
- **Membership or card benefit is absent:** Check eligibility and whether it applies to this leg; leave it pending if unconfirmed.
- **Gate staff asks to check a cabin case:** Under the airline's instruction, address items that must stay in the cabin before handing it over. External fit does not cancel an on-site capacity decision.

### Assumptions, alternatives, and side effects

This is ordinary baggage-allowance checking, not dangerous goods, customs, or compensation guidance, and it promises no price. Carrier, fare, route, partner, and date matter; Delta pages illustrate the differences without exporting their numbers. Use borrowed measuring tools or trusted help if measuring and lifting are hard. Actual staff acceptance follows this itinerary's rules. Changing or reducing bags may be inconvenient but is easier to handle before a check-in desk.

### Sources

- [Delta: Baggage Policy and Fees](https://www.delta.com/us/en/baggage/overview) and [Carry-On Baggage](https://www.delta.com/us/en/baggage/carry-on-baggage) — fare, benefit, leg and partner conditions affect allowances; a cabin case can be limited at a gate. No Delta numeric limit is copied.
- [CATSA: Carry-on or Checked?](https://www.catsa-acsta.gc.ca/en/what-can-bring/carry-or-checked) — screening item rules differ from airline bag size, weight, and excess-fee policy.
- Original synthesis — compare the applicable ticket rules against each fully packed bag and resolve excess before handover.

If AI opens this file, it may locate the airline's current bag chart. You measure, compare, change bags, or ask the carrier.
