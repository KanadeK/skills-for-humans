---
name: sort-flight-items-by-cabin-hold-or-stop
description: "Human steps to classify intended flight items under the actual airline, screening and aviation-safety rules as cabin, checked, not permitted, or unresolved before surrendering a bag."
---
# 把航程物品分到随身、托运或暂停 / Sort Flight Items by Cabin, Hold, or Stop

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10–20 分钟 + 官方物品核对时间 / 10–20 minutes plus official item checks |
| Requirements / 必要物品 | 本次航程与所有拟带物品、实际出发地安检机构/航空安全及运营航司的当期物品规则 / Actual itinerary and item list, current item rules from departure screening, aviation-safety authority, and operating airline |
| Side effects / 现实副作用 | 有些物品可能留家、另行处理或待航司确认，不能靠换箱子让限制消失 / Some items may stay home, need another route, or await airline confirmation; changing bags does not erase a restriction |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你准备把普通物品装进随身与托运行李，但不确定哪些物品能过安检、哪些必须留在客舱或完全不能带时，用这份 Skill按**本次出发地安检、航空安全和实际承运航司**的当前规则，把物品分为“随身”“托运”“不带/另寻渠道”“待官方确认”。目标是没有把不明受限品悄悄塞进箱子，也不会在登机口临时交箱时把必须随身的东西一起交走。本文不教授危险品改装、申报规避或安检绕过。

### 准备与输入

列出要带的物品及具体型号/容量/成分线索（如果这些是官方判断所需），特别标出电池/充电宝、气雾剂、液体、锋利物、药品或助行设备等可能有专门规则的类别。查实际出发机场安检机构的物品查询、适用航空危险品规则和运营航司特殊物品页；转机后再次过安检或换航司时逐段核对。普通衣物等已明确允许的物品不必每件逐一搜；无法准确识别内容的瓶罐/设备先列为未知，不让猜测进箱。

### 执行

1. **按物品而非按箱子查询。** 在负责这段出发安检的官方物品库查“可随身、可托运、有限制或禁止”，同时核航空安全机关及运营航司对该物品的额外要求。安检允许随身不等于航司允许上机，托运额度足够也不等于物品可托运；同类外观的不同电池或气雾剂可能规则不同。
2. **把结果写成四栏。** 每件标“随身”“托运”“不带/另行处理”“待官方确认”，旁边记负责方来源、适用航段和条件。若页面没有列该物品，不等于自动允许；向航司/负责安检或航空安全渠道询问。遇到损坏、召回或泄漏的电池/物品，暂停交运并按官方安全指示处理，不尝试遮盖、拆改或混进其他箱。
3. **安排实际可取用性。** 证件、登机牌和可能需现场出示的材料按官方要求保持可取用；对规定必须在客舱的物品，不能放到托运箱。随身行李若可能在登机口改托运，预先知道哪些物品需按当期规则移出并留在身边；不要在队列里盲目交出未核对的包。
4. **临行与交接时再核对。** 对特殊物品、转机/不同航司/不同安检点，复查当期规则和运营方答复。安检或登机口工作人员要求调整时，请其说明适用方式并按正式指引办理。仍有“待确认”的关键物品，就不带它进入安检/托运流程，或在有权渠道明确答复后再继续。

### 成功条件

每个可能受限物品有本航段适用的官方分类与实际去向，不带的物品已从行李中移除，待确认项不被当成已许可，且登机口改托运不会误交必须留在客舱的物品。分类完成也不保证安检人员最终放行或航司一定接收；现场决定按有权机构和航司办理。

### 常见报错与补救

- **物品不在官方搜索结果里：** 不推断“没写就是允许”，问负责方或留家。
- **航司允许箱子但安检不允许某内件：** 按物品规则重新分类，不拿行李尺寸规则为内件辩护。
- **充电宝/备用电池混进待托运箱：** 在交箱前按本航程官方规则核对并移到允许位置；损坏或召回品先停止携带求官方指引。
- **登机口临时要求托运手提箱：** 先找出必须随身/客舱的物品并按工作人员指示处理，不把箱子原样交走。
- **换航司或转机再安检：** 用下一段实际运营方和安检方规则复核，第一段通过不是后续自动许可。

### 假设、替代与现实副作用

这里是普通旅客的物品分类，不提供危险品包装步骤、海关/药品法律、医疗必要性判断或任何通用液体/电池数值。美国 FAA、加拿大 CATSA 的页面用于说明规则职责，其他国家与航司需读自己的官方资料。没有网络或无法辨识型号时可从航司/机场官方柜台或客服核实，未确认前让物品留在家中/合规处置，而非带到安检口试运气。舍弃或改送物品可能带来成本，但隐瞒风险更大。

### 来源

- [FAA：PackSafe for Passengers](https://www.faa.gov/hazmat/packsafe) 与 [Carry-On Baggage Tips](https://www.faa.gov/travelers/prepare_fly/baggage)（英文，美国航空安全机构）— 常见日用品可能受航空危险品限制，登机口托运也需重查必须留在客舱的物品；未列出不等于许可。
- [CATSA：What can I bring?](https://www.catsa-acsta.gc.ca/en/what-can-bring) 与 [Carry-on or Checked?](https://www.catsa-acsta.gc.ca/en/what-can-bring/carry-or-checked)（英文，加拿大安检机构）— 安检可按具体物品查随身/托运/禁止，最终现场决定属安检人员；航司另管箱子额度。
- [Delta：Carry-On Baggage](https://www.delta.com/us/en/baggage/carry-on-baggage)（英文，美国航司）— 合作承运与客舱空间会改变某段随身行李安排，应按实际航司复核。
- Original synthesis — 把安检、航空安全和航司三层要求按物品合并成可执行的四栏分流，不把任何地区限额写成全球通用。

## English

Use this Skill while sorting ordinary possessions into cabin and checked bags when it is unclear what passes screening, what must stay in the cabin, or what cannot travel. Under the **actual departure checkpoint, aviation-safety authority, and operating airline** rules, put each item in “cabin,” “checked,” “leave or another channel,” or “official confirmation pending.” The result avoids hiding an unknown restricted item or surrendering a cabin-only item inside a bag checked at the gate. This file gives no dangerous-goods modification, declaration evasion, or screening-bypass method.

### Preparation and inputs

List intended items and the model, capacity, or ingredient facts an official rule needs. Flag batteries and power banks, aerosols, liquids, sharp objects, medicines, and mobility aids for special checking. Use the departure screening authority's item search, applicable aviation dangerous-goods rules, and operating airline's special-item guidance. Recheck any onward leg with another checkpoint or carrier. Ordinary clearly permitted clothing needs no item-by-item search. An unidentifiable bottle or device stays unknown, not guessed into a bag.

### Execution

1. **Look up items, not merely bags.** In the official search for the departure checkpoint, determine cabin, checked, limited, or prohibited status; check aviation-safety and operating-airline additions for the same item. Checkpoint permission does not force airline cabin acceptance, and a checked-bag allowance does not make every content checkable. Similar-looking batteries or aerosols may have different conditions.
2. **Write a four-column result.** Mark each relevant item “cabin,” “checked,” “leave / another channel,” or “official confirmation pending,” with responsible source, flight leg, and conditions. An item absent from a list is not automatically allowed; ask the responsible airline or screening/safety authority. For damaged, recalled, or leaking battery-powered items, pause handover and seek official safety direction; do not hide, modify, or mix them into a different bag.
3. **Keep required access.** Documents, boarding passes, and materials to show on request stay retrievable under official instructions. An item required in the cabin must not be buried in a checked case. If a cabin case might be checked at the gate, know which items must be removed and kept under the current rule before surrendering it. Do not hand over an unchecked bag in a queue.
4. **Recheck at departure and handover.** For special items, transfers, a new carrier, or another checkpoint, revisit current rules and provider replies. If screening or gate staff directs a change, ask how that rule applies and follow the official process. A critical “pending” item stays out of screening/checked handover until an authorized answer is available.

### Success

Every possibly restricted item has an applicable official classification and real placement for this leg. Items not travelling are out of the bags, pending items are not treated as permitted, and a gate-checked case will not carry something required to stay in the cabin. Classification is not a guarantee of final checkpoint release or airline acceptance; competent officials make on-site decisions.

### Common errors and recovery

- **Item is absent from the official search:** Do not treat silence as permission. Ask the authority or leave it behind.
- **Bag meets airline size but an item fails screening:** Reclassify by the item rule; dimensions are no defence for contents.
- **Power bank or spare battery is in a case to be checked:** Before handover, check this itinerary's official rule and move it to its permitted place. Stop carrying damaged or recalled items pending official direction.
- **Cabin case is gate-checked:** Identify cabin-required items and handle them under staff instructions before surrendering the case.
- **Carrier or checkpoint changes on a connection:** Verify that segment's real operator and screening rules. Passing the first leg grants no automatic later permission.

### Assumptions, alternatives, and side effects

This is ordinary passenger item classification, not dangerous-goods packing steps, customs or medicines law, medical-necessity judgments, or a universal liquid/battery limit. US FAA and Canadian CATSA illustrate different responsibilities; other countries and carriers require their own official sources. Without internet or a readable model, ask airline/airport official staff and keep the unresolved item at home or handle it through a lawful alternate channel, rather than testing it at security. Leaving or rerouting an item may cost money, but concealment is worse.

### Sources

- [FAA: PackSafe](https://www.faa.gov/hazmat/packsafe) and [Carry-on tips](https://www.faa.gov/travelers/prepare_fly/baggage) — everyday goods may be regulated; gate-checked bags need rechecking for cabin-required items; absence from a chart is not permission.
- [CATSA: What can I bring?](https://www.catsa-acsta.gc.ca/en/what-can-bring) and [Carry-on or Checked?](https://www.catsa-acsta.gc.ca/en/what-can-bring/carry-or-checked) — item-specific cabin/hold/prohibited lookup, with final checkpoint decision by screening officers; airlines set bag allowance separately.
- [Delta: Carry-On Baggage](https://www.delta.com/us/en/baggage/carry-on-baggage) — partner operation and cabin space can change a segment's cabin-bag arrangement.
- Original synthesis — combine checkpoint, aviation-safety and carrier item rules into four actionable states without exporting any jurisdiction's numeric limits.

If AI opens this file, it may locate an official item lookup. You classify, remove, confirm, or stop before baggage handover.
